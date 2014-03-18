
import zmq

from .messenger import Messenger

class Sender(Messenger):

    def __init__(self, port, url='tcp://127.0.0.1', 
                 context=zmq.Context(), single=False,
                 worker_id='Sender', 
                 json=True, 
                 *args, **kwargs):

        super(Sender, self).__init__(
            port, url, single, worker_id, json, 
            *args, **kwargs)

        self.socket = context.socket(zmq.PUSH)
        self._connect_socket()
