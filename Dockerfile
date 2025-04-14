FROM python:3.13-slim

LABEL maintainer="@ElStormus"
LABEL version="1.0"
LABEL description="Automatic generation of M3U files from music folders."

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY generate_playlists.py .

CMD ["python", "generate_playlists.py"]
