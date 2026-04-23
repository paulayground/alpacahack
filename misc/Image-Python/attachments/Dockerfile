# NOTE: This hash is pinned to avoid version and environment differences.
FROM python:3.14.4-slim-trixie@sha256:538a18f1db92b4210a0b71aca2d14c156a96dedbe8867465c8ff4dce04d2ec39
RUN apt-get update && apt-get install -yq socat file

WORKDIR /app

COPY --chmod=444 flag.txt .
COPY --chmod=444 jail.py .

USER nobody:nogroup

ENV PYTHONUNBUFFERED=1

CMD ["socat", "TCP-L:5000,fork,reuseaddr", "EXEC:'python jail.py',stderr"]
