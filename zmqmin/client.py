
import zmq

from .messenger import Messenger

class Client(Messenger):

    def __init__(self, port, url='tcp://127.0.0.1', 
                 context=zmq.Context(),
                 worker_id='Client', 
                 json=True, 
                 *args, **kwargs):

        super(Client, self).__init__(
            port, url, False, worker_id, json, 
            *args, **kwargs)

        self.socket = context.socket(zmq.REQ)
        self._connect_socket()

    def send_request(self, request):
        self.send_message(request)
        return self.receive_message()
