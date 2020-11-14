from setuptools import setup, find_packages

import gen_code

gen_code.generate_proto_code()

setup(
    name='protobufRepo',  # name which will be used to install via pip
    version='0.1',  # version number simple as that
    description='grpc files for test repo',
    long_description='',
    author='Marvin Gravert',
    author_email='marvin.gravert@gmail.com',

    license='MIT',
    # which directories to search for imports. Importable dirs are marked by
    packages=find_packages(),
    # packages=find_packages()#also possible but may include unwanted dir such as tests
    zip_safe=False,
)
