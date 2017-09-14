# Using lightweight alpine image
FROM python:3.6-alpine

# Installing packages
RUN apk update
RUN pip install pipenv

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock bootstrap.sh ./
COPY cashman ./cashman

RUN pipenv install
RUN apk add --no-cache bash
RUN apk add --no-cache curl

# Start app
EXPOSE 5000

ENTRYPOINT ["/usr/src/app/bootstrap.sh"]


