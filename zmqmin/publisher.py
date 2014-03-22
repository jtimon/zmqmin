
import zmq

from .messenger import Messenger

class Publisher(Messenger):

    def _init_socket(self):
        self.socket = self.context.socket(zmq.PUB)
