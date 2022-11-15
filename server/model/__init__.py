from .model import Model

model = None

def get_model():
    global model
    if model is None:
        model = Model()
    return model
