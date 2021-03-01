FROM python:3.9-alpine3.13

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . ./

RUN apk add gcc jq libc-dev


RUN jq -r '.default \
    | to_entries[]  \
    | .key + .value.version' \
    Pipfile.lock > requirements.txt && \
    pip install -r requirements.txt

ENV DOT_ENV=test
ENV PORT=8000
ENV TZ=UTC

CMD ["uvicorn", "src.app:app", "--port", ${PORT}, "--reload"]

