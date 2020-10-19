import protobuf.unary.unary_pb2 as unary_pb2
import protobuf.unary.unary_pb2_grpc as unary_pb2_grpc
import logging
import config.config as config
from concurrent import futures

import grpc

class SimpelCom(unary_pb2_grpc.SimpelComServicer):
    def NumberTrade(self, request, context):
        response=f"Hallo {request.name} mit der ID {request.ID}. Wir beglaubigen dir dir die {request.accuracy}" 
        response="Hi"
        return unary_pb2.SimpleResponse(quality="response") 

def serve():
    server=grpc.server(thread_pool=futures.ThreadPoolExecutor(max_workers=2))
    unary_pb2_grpc.add_SimpelComServicer_to_server(servicer=SimpelCom(),server=server)
    server.add_insecure_port(f"[::]:{config.port}")
    server.start()
    server.wait_for_termination()   
    

class Server:
    def serve(self):
        serve()

if __name__=="__main__":
    serve()