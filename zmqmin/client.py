
import zmq

from .messenger import Messenger

class Client(Messenger):

    def _init_socket(self):
        self.socket = self.context.socket(zmq.REQ)

    def send_request(self, request):
        self.send_message(request)
        return self.receive_message()
