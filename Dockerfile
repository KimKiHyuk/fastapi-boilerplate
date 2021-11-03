FROM python:3.9-alpine3.13

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk add gcc jq libc-dev

COPY . ./

RUN jq -r '.default \
    | to_entries[]  \
    | .key + .value.version' \
    Pipfile.lock > requirements.txt && \
    pip install -r requirements.txt

ENV DOT_ENV=test
ENV PORT="8000"
ENV TZ=UTC


CMD ["sh", "-c",  "uvicorn src.app:app --host 0.0.0.0 --port ${PORT}"]

