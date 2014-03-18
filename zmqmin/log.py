import zmq
import time
import sys
import pprint
from  multiprocessing import Process

default_port = "6000"

def json_sub_logger(ports):
    context = zmq.Context()
    socket = context.socket(zmq.SUB)

    for port in ports:
        print "Log subscribed to port %s" % port
        socket.connect("tcp://localhost:%s" % port)

    # topicfilter blank to get all messages
    socket.setsockopt(zmq.SUBSCRIBE, "")

    while True:
        data = socket.recv_json()
        pprint.pprint(data)

if __name__ == "__main__":

    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    else:
        ports = [default_port]
    
    Process(target=json_sub_logger, args=(ports,)).start()
