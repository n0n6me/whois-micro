# whois-micro

simple whois api. use https://domain.tld/aaa.tld for getting whois information about aaa.tld domain as json structure

run from hub.docker.com:
docker run -d -p 80:80 m0nkeydog/whois:latest

building from repo:
docker build -t whois-micro .
docker run -d -p 80:80 whois-micro

