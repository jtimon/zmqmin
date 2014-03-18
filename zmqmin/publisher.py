
import zmq

from .messenger import Messenger

class Publisher(Messenger):

    def __init__(self, port, url='tcp://127.0.0.1', 
                 context=zmq.Context(), single=False,
                 worker_id='Publisher', 
                 json=True, 
                 *args, **kwargs):

        super(Publisher, self).__init__(
            port, url, single, worker_id, json, 
            *args, **kwargs)

        self.socket = context.socket(zmq.PUB)
        self._connect_socket()
