
import zmq
from  multiprocessing import Process

from .messenger import Messenger

class Server(Messenger, Process):

    def __init__(self, port, url='tcp://127.0.0.1', 
                 single=True, 
                 worker_id='Server', 
                 json=True, 
                 *args, **kwargs):

        super(Server, self).__init__(
            port, url, single, worker_id, json, 
            *args, **kwargs)

    def _init_server(self):
        context = zmq.Context()
        self.socket = context.socket(zmq.REP)
        self._connect_socket()

    def run(self):
        self._init_server()
        while True:
            request = self.receive_message()
            response = self.calculate_response(request)
            self.send_message(response)
