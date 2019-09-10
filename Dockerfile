FROM python:2.7
MAINTAINER AJ Bowen <aj@soulshake.net>

COPY . /src/
WORKDIR /src/
#RUN pip install .
ARG COMMIT_HASH
ENV COMMIT_HASH=${COMMIT_HASH}
ENV foo=bar
COPY doit.sh /src
CMD /src/doit.sh
#CMD ["swag"]
