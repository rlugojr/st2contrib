from st2actions.runners.pythonrunner import Action
from pyremedy.ars import ARS
from pyremedy.exceptions import ARSError

class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)
        self.client = self._get_client()

    def _get_client(self):
        servername = self.config['servername']
        serverport = self.config['serverport']
        username = self.config['username']
        password = self.config['password']
        return ARS(server=servername, port=serverport, user=username, password=password)
