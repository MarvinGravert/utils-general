"""
Generate the protocol buffer code for python from proto files located in the
protos file. For each file create own folder
Adjust the import statements
"""
import glob
import re
from grpc_tools import protoc
from os import mkdir
from itertools import chain
# assume all code protocol buffers are in protos


def generate_proto_code():
    """
    Generates proto code and returns list of generated pyton modules
    Return: list of generated modules as strings
    """
    """
    Get file names
    """
    file_path_list = list()
    file_name_list = list()
    for file_path in glob.iglob("./protos/*.proto"):
        file_path_list.append(file_path)
        isolated_file_name = file_path.split("/")[2].split(".")[0]
        file_name_list.append(isolated_file_name)
    """
    Create Folder
    based on filename
    """
    for file_name in file_name_list:
        try:
            mkdir(file_name)
        except FileExistsError:
            pass

    """
    Generate the code into the folder
    """
    for file_path, file_name in zip(file_path_list, file_name_list):
        protoc.main([
            'grpc_tools.protoc',
            '--proto_path=protos',
            f'--python_out={file_name}',
            f'--grpc_python_out={file_name}',
            file_path])
    """
    Adjust the import statement

    GRPC doesnt really handle seperating proto file and python file
    thus the python interpreter has a problem finding the module e.g.:
    import example_a_pb2 as example__a__pb => import not working as the module
    is not on $PATH
    Instead the interpreter needs to be told to look in the same current dir:
    from . import client_stream_pb2 as client__stream__pb2
    """
    for file_name in file_name_list:
        for script in glob.iglob(f"./{file_name}/*.py"):
            with open(script, 'r+') as file:
                code = file.read()
                file.seek(0)
                file.write(re.sub(r'(import .+_pb2.*)', 'from . \\1', code))
                file.truncate()

    return list(chain.from_iterable(
        [[f"{name}_pb2", f"{name}_pb2_grpc"] for name in file_name_list]))


if __name__ == "__main__":
    generate_proto_code()
