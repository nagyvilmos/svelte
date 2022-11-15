import logging
from json_store import get_store
from .migrate import set_model
from .session import get_session, request_token

log = logging.getLogger('model')
log.setLevel(logging.DEBUG)

model = None

class Model:
    def __init__(self):
        self.store = get_store()
        self._init_model()

    def _init_model(self):
        """set up the inital data"""
        set_model()

    def action_auth(self, session, req):
        return session

    def request(self, req):
        """
            Entry point for the API
            req contains a json structure, if the 
        """
        session = get_session(req)

        action = {
            'request_token': [request_token, False]
        }.get(req.get('action'), [None, True])
        action_func = action[0]
        action_auth = action[1]

        if action_auth and session is None:
            return self.reply()
        if action_func is not None:
            # possibly we can get a different session back
            session = action_func(session, req)
        return self.reply(session)

    def reply(self, session=None):
        """
            Exit point for the API
        """
        if session is None:
            # any defaults can be returned here:
            return {'success': False,
                    'response': 'No active session',
                    'data': None}
        return session.get_session_data()
        