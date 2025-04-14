# 🎵 Docker M3U File Generator

![Docker Pulls](https://img.shields.io/docker/pulls/elstormus/playlist-generator?style=flat-square)
![CI](https://github.com/ElStormus/docker-m3u-file-generator/actions/workflows/docker.yml/badge.svg)

This container automatically generates `.m3u` files in your music folders, which are scanned regularly.

## 🚀 Docker Compose

```yaml
version: '3.9'

services:
  playlist-generator:
    image: stormimousse/playlist-generator:latest
    container_name: m3u-file-generator

    volumes:
      - /path/to/music/folder:/music1
      - /path/to/music/folder:/music2

    environment:
      - MUSIC_DIRS=/music1,/music2,
      - SCAN_INTERVAL=3600

    restart: unless-stopped
```

## 🔧 Environment variables

| Variable       | Mandatory   | Description                             | Default value     |
|----------------|-------------|-----------------------------------------|-------------------|
| `MUSIC_DIRS`   | ✅          | Internal paths to be scanned (commas)   | `/music`          |
| `SCAN_INTERVAL`| ❌          | Time between scans (in seconds)         | `3600`            |
