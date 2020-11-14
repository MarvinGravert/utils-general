"""
Generate the protocol buffer code for python from proto files located in the
protos file. For each file create own folder
Adjust the import statements
"""
import glob
from io import TextIOBase
import re
from grpc_tools import protoc
from os import mkdir

# assume all code protocol buffers are in protos


def generate_proto_code():
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
    """
    for file_name in file_name_list:
        for script in glob.iglob(f"./{file_name}/*.py"):
            with open(script, 'r+') as file:
                code = file.read()
                file.seek(0)
                file.write(re.sub(r'(import .+_pb2.*)', 'from . \\1', code))
                file.truncate()


if __name__ == "__main__":
    generate_proto_code()
