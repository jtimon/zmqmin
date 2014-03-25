
import zmq
from  multiprocessing import Process

class Device(Process):

    def __init__(self, frontend_port, backend_port, 
                 front_url='tcp://127.0.0.1', 
                 back_url='tcp://127.0.0.1', 
                 *args, **kwargs):

        self.frontend_port = frontend_port
        self.backend_port = backend_port
        self.front_url = front_url
        self.back_url = back_url

        super(Device, self).__init__(*args, **kwargs)

    def _create_frontend(self):
        raise NotImplementedError
    def _create_backend(self):
        raise NotImplementedError
    def _connect(self):
        raise NotImplementedError

    def run(self):
        self.context = zmq.Context()

        self._create_frontend()
        self._create_backend()
        print "%s connecting %s:%s to %s:%s" % (
            self.__class__.__name__, 
            self.front_url, 
            self.frontend_port, 
            self.back_url, 
            self.backend_port)
        self._connect()
    
class Forwarder(Device):

    def _create_frontend(self):
        self.frontend = self.context.socket(zmq.SUB)
        self.frontend.bind("%s:%s" % (self.front_url, self.frontend_port))
        self.frontend.setsockopt(zmq.SUBSCRIBE, "")

    def _create_backend(self):
        self.backend = self.context.socket(zmq.PUB)
        self.backend.bind("%s:%s" % (self.back_url, self.backend_port))

    def _connect(self):
        zmq.device(zmq.FORWARDER, self.frontend, self.backend)

class Streamer(Device):

    def _create_frontend(self):
        self.frontend = self.context.socket(zmq.PULL)
        self.frontend.bind("%s:%s" % (self.front_url, self.frontend_port))

    def _create_backend(self):
        self.backend = self.context.socket(zmq.PUSH)
        self.backend.bind("%s:%s" % (self.back_url, self.backend_port))

    def _connect(self):
        zmq.device(zmq.STREAMER, self.frontend, self.backend)

class Queue(Device):

    def _create_frontend(self):
        self.frontend = self.context.socket(zmq.XREP)
        self.frontend.bind("%s:%s" % (self.front_url, self.frontend_port))

    def _create_backend(self):
        self.backend = self.context.socket(zmq.XREQ)
        self.backend.bind("%s:%s" % (self.back_url, self.backend_port))

    def _connect(self):
        zmq.device(zmq.QUEUE, self.frontend, self.backend)
