# 🎵 Docker M3U File Generator

![Docker Pulls](https://img.shields.io/docker/pulls/stormimousse/docker-m3u-file-generator/?style=flat-square)
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
      - /path/to/music/folder1:/music1
      - /path/to/music/folder2:/music2
      - /path/to/music/folder3:/music3
    # - /path/to/music/folderX:/musicX

    environment:
      - SCAN_INTERVAL=3600 # in seconds

    restart: unless-stopped
```

## 🔧 Environment variables

| Variable       | Mandatory   | Description                             | Default value     |
|----------------|-------------|-----------------------------------------|-------------------|
| `SCAN_INTERVAL`| ❌          | Time between scans (in seconds)         | `3600`            |
