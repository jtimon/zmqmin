
import zmq

class Messenger(object):

    def __init__(self, port, url='tcp://127.0.0.1', 
                 context=zmq.Context(), single=False,
                 worker_id='Messenger', 
                 json=True, 
                 *args, **kwargs):

        self.port = port
        self.url = url
        self.single = single
        self.worker_id = worker_id
        self.json = json
        self.context = context

        self._connect_socket()

        super(Messenger, self).__init__(*args, **kwargs)

    def _init_socket(self):
        raise NotImplementedError

    def _connect_socket(self):
        self._init_socket()
        full_url = '%s:%s' % (self.url, self.port)
        if self.single:
            self.socket.bind(full_url)
        else:
            self.socket.connect(full_url)
        print '%s connected to %s' % (self.worker_id, full_url)

    def send_message(self, message):
        if self.json:
            self.socket.send_json(message)
        else:
            self.socket.send(message)            

    def receive_message(self, force=False):
        if force:
            if self.json:
                return self.socket.recv_json(zmq.DONTWAIT)
            return self.socket.recv(zmq.DONTWAIT)
        else:
            if self.json:
                return self.socket.recv_json()
            return self.socket.recv()
