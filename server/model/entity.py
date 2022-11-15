from .entity_data import EntityData
from . import field


# defined here, the mongo DB is callable through the entity class:
store = None


def init_model(new_store):
    global store
    store = new_store


class Entity(EntityData):
    """Entity within the model"""
    _collection = None
    _key = field.name

    def __init__(self, data=None, key=None):
        if key is not None:
            data = type(self).load(key)
        super().__init__(data)
        self.validate()
        self.saved = field._id in self._data.keys()

    def save(self):
        # nothing happening
        if len(self._changed) == 0:
            return
        if not self.validate():
            Exception('Invalid entity')
        data = self.get_changed_values()
        col = type(self).collection
        key = self.get_

    @classmethod
    def collection(cls):
        return cls.__name__.lower() if cls._collection is None else cls._collection

    @classmethod
    def list(cls, where=None):
        return store.get(cls.collection(), where=where)

    @classmethod
    def load(cls, key):
        data = cls.list(lambda d: d.get[cls._key] == key)
        return data[0] if len(data)>0 else None
