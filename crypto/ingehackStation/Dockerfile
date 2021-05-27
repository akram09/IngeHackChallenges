FROM ubuntu:18.04


RUN apt-get update && apt-get install -y \
    python3-pip \
    xinetd \
    python3-dev 

RUN mkdir /chall 
WORKDIR /chall 

RUN useradd -M -d /chall chall 


COPY ./flag.txt ./
COPY ./requirements.txt ./ 
COPY ./station.py ./ 
COPY ./start.sh ./


RUN chown -R chall:chall /chall && chmod -R 740 /chall
RUN pip3 install -r requirements.txt

ENTRYPOINT []
CMD ["./start.sh"]

EXPOSE 9999