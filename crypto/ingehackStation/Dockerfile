FROM ubuntu:18.04


RUN apt-get update && apt-get install -y \
    python3-pip \
    xinetd \
    python3-dev 

RUN mkdir /chall 
WORKDIR /chall 

RUN useradd -M -d /chall chall 
# print on connection failed
RUN echo "========= Connection failed ===========" > /etc/banner_fail
COPY ctf.xinetd /etc/xinetd.d/chall

COPY ./flag.txt ./
COPY ./requirements.txt ./ 
COPY ./station.py ./ 
COPY ./start.sh ./


RUN chown -R chall:chall /chall && chmod -R 740 /chall
RUN pip3 install -r requirements.txt

ENTRYPOINT []
CMD ["/usr/sbin/xinetd", "-dontfork"]

EXPOSE 9999