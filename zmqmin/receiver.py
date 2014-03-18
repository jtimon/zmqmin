
import zmq

from .messenger import Messenger

class Receiver(Messenger):

    def __init__(self, port, url='tcp://127.0.0.1', 
                 context=zmq.Context(), single=False,
                 worker_id='Receiver', 
                 json=True, 
                 *args, **kwargs):

        super(Receiver, self).__init__(
            port, url, single, worker_id, json, 
            *args, **kwargs)

        self.socket = context.socket(zmq.PULL)
        self._connect_socket()
