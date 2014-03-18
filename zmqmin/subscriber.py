
import zmq

from .messenger import Messenger

class Subscriber(Messenger):

    # topicfilter blank to get all messages
    def __init__(self, port, url='tcp://127.0.0.1', 
                 context=zmq.Context(), single=False,
                 worker_id='Subscriber', 
                 json=True, topic='', 
                 *args, **kwargs):

        super(Subscriber, self).__init__(
            port, url, single, worker_id, json, 
            *args, **kwargs)

        self.socket = context.socket(zmq.SUB)
        self._connect_socket()
        self.socket.setsockopt(zmq.SUBSCRIBE, topic)
