import unary.unary_pb2 as unary_pb2
import unary.unary_pb2_grpc as unary_pb2_grpc
import logging
from concurrent import futures
from config.config import PORT

import grpc


class SimpelCom(unary_pb2_grpc.SimpelComServicer):
    def NumberTrade(self, request, context):
        logging.error(f"Data: {request.name}")
        accuracy = sum(request.data)/len(request.data)
        std = request.brightness*4
        objToReturn = unary_pb2.ProcesQuality(
            quality="good",
            accuracy=accuracy,
            standard_deviation=std,
        )
        return objToReturn


def serve():
    server = grpc.server(thread_pool=futures.ThreadPoolExecutor(max_workers=2))
    unary_pb2_grpc.add_SimpelComServicer_to_server(
        servicer=SimpelCom(), server=server)
    server.add_insecure_port(f"[::]:{PORT}")
    server.start()
    server.wait_for_termination()


class Server:
    def serve(self):
        logging.error(f"Server started on Port {PORT}")
        serve()


if __name__ == "__main__":
    Server().serve()
