FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk add git
RUN python -m pip install git+https://github.com/richardpenman/whois.git
COPY . .
RUN pip3 install -r requirements.txt 
