from setuptools import setup, find_packages
import glob
import re

from grpc_tools import protoc

# Generate stubs from `api/*.proto` files in `api/gen` directory
protoc.main([
    'grpc_tools.protoc',
    '--proto_path=protos',
    '--python_out=unary',
    '--grpc_python_out=unary'
] + [proto for proto in glob.iglob('./protos/*.proto')])

# Make pb2 imports in generated scripts relative
for script in glob.iglob('./unary/*.py'):
    with open(script, 'r+') as file:
        code = file.read()
        file.seek(0)
        file.write(re.sub(r'(import .+_pb2.*)', 'from . \\1', code))
        file.truncate()
# setup( 
# 	name='protobufRepo',#name which will be used to install via pip
# 	version='0.1',#version number simple as that
# 	description='grpc files for test repo',
# 	long_description='',
# 	author='Marvin Gravert',
# 	author_email='marvin.gravert@gmail.com',

# 	license='MIT',
# 	#which directories to search for imports. Importable dirs are marked by 
# 	packages=find_packages(),
# 	#packages=find_packages()#also possible but may include unwanted dir such as tests
# 	zip_safe=False,
# )