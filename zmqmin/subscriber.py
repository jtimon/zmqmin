
import zmq

from .messenger import Messenger

class Subscriber(Messenger):

    # topicfilter blank to get all messages
    def __init__(self, port, url='tcp://127.0.0.1', 
                 context=zmq.Context(), single=False,
                 worker_id='Subscriber', 
                 json=True, topic='', 
                 *args, **kwargs):

        self.topic = topic

        super(Subscriber, self).__init__(
            port=port, url=url, context=context, 
            single=single, worker_id=worker_id, json=json, 
            *args, **kwargs)

    def _init_socket(self):
        self.socket = self.context.socket(zmq.SUB)
        self.socket.setsockopt(zmq.SUBSCRIBE, self.topic)
