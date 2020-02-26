from driplineorg/dripline-python:v4.1.0

COPY . /usr/local/src/dripline-python-extension-example

WORKDIR /usr/local/src/dripline-python-extension-example
RUN pip install .

WORKDIR /
