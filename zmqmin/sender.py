
import zmq

from .messenger import Messenger

class Sender(Messenger):

    def _init_socket(self):
        self.socket = self.context.socket(zmq.PUSH)
