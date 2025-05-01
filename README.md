# 🎵 Docker M3U File Generator

![Docker Pulls](https://img.shields.io/docker/pulls/stormimousse/docker-m3u-file-generator)
![CI](https://github.com/ElStormus/docker-m3u-file-generator/actions/workflows/docker.yml/badge.svg)

This container automatically generates `.m3u` files in your music folders, which are scanned regularly.

🐳 https://hub.docker.com/r/stormimousse/docker-m3u-file-generator

## 📝 Features

- Automatically generates a `.m3u` playlist per folder.
- Supports two modes:
  1. **Multiple mounted folders** (e.g. `/music1`, `/music2`, etc.).
  2. **Single parent folder containing subfolders** (e.g. `/playlists/Playlist1`, `/playlists/Playlist2`, etc.).
- Recursively scans all subdirectories.
- Runs continuously at a configurable interval.
- Lightweight memory footprint.


## 🚀 Docker Compose

```yaml
version: '3.9'

services:
  playlist-generator:
    image: stormimousse/playlist-generator:latest
    container_name: m3u-file-generator
    volumes:
      # Option 1: separate folders
      - /path/to/music1:/music1
      - /path/to/music2:/music2

      # Option 2: single parent folder
      - /path/to/all_playlists:/playlists
    environment:
      - SCAN_INTERVAL=3600  # Scan interval in seconds

    restart: unless-stopped
```

## 🔧 Environment variables

| Variable       | Mandatory   | Description                             | Default value     |
|----------------|-------------|-----------------------------------------|-------------------|
| `SCAN_INTERVAL`| ❌          | Time between scans (in seconds)         | `3600`            |
