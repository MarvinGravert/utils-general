import unary.unary_pb2 as unary_pb2
import unary.unary_pb2_grpc as unary_pb2_grpc
import logging

from config.config import PORT
import grpc


def run():
    with grpc.insecure_channel(f"localhost:{PORT}") as channel:
        stub = unary_pb2_grpc.SimpelComStub(channel)
        name = "temperatur"
        data = [10, 20, 21, 20, 18, 14, 11, 10]
        brightness = 10.2
        objToSend = unary_pb2.ProcesData(
            name=name,
            data=data,
            brightness=brightness
        )
        response = stub.NumberTrade(objToSend)
        print(response)
        # if not with=>channel.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run()
