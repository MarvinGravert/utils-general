from logging import INFO
import unary.unary_pb2 as unary_pb2
import unary.unary_pb2_grpc
import logging

import config.config as config

import grpc

def run():
    with grpc.insecure_channel(f"localhost:{config.port}") as channel:
        stub=unary_pb2_grpc.SimpelComStub(channel)
        objToSend=unary_pb2.SimpleCall(name="HDF")
        logging.info(f"{type(objToSend)}")
        response=stub.NumberTrade(unary_pb2.SimpleCall(name="hi"))
        print(response)
        #if not with=>channel.close()

if __name__=="__main__":
    logging.basicConfig(level=INFO)
    run()