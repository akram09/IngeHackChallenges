FROM python:3.8-alpine3.12

RUN apk --update add gcc build-base freetype-dev libpng-dev openblas-dev

RUN mkdir /chall 
WORKDIR /chall 




COPY ./flag.txt ./
COPY ./requirements.txt ./ 
COPY ./server.py ./ 
COPY ./start.sh ./

RUN chmod +x start.sh
RUN chmod -R 740 /chall


RUN pip3 install -r requirements.txt

ENTRYPOINT []
CMD ["./start.sh"]

EXPOSE 9999