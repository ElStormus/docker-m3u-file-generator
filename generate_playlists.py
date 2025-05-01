import os
import time
import logging

AUDIO_EXTENSIONS = ('.mp3', '.flac', '.ogg', '.wav', '.aac', '.m4a', '.opus')

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')

def generate_m3u_for_directory(directory):
    playlist_name = os.path.basename(os.path.normpath(directory)) + '.m3u'
    playlist_path = os.path.join(directory, playlist_name)

    audio_files = [
        f for f in sorted(os.listdir(directory))
        if f.lower().endswith(AUDIO_EXTENSIONS)
    ]

    if not audio_files:
        return False

    with open(playlist_path, 'w', encoding='utf-8') as m3u:
        for file in audio_files:
            m3u.write(f"{file}\n")

    logging.info(f"Playlist created: {playlist_path}")
    return True

def walk_music_folder(root_music_folder):
    for root, _, _ in os.walk(root_music_folder):
        generate_m3u_for_directory(root)

def get_music_dirs(base_dir="/"):
    candidates = [os.path.join(base_dir, d) for d in os.listdir(base_dir)]
    music_dirs = []

    for path in candidates:
        if os.path.isdir(path):
            # Detect volumes like /music1, /music2
            if path.startswith("/music"):
                music_dirs.append(path)
            # Detect a parent folder like /playlists containing subfolders
            elif path.startswith("/playlists"):
                subdirs = [os.path.join(path, sub) for sub in os.listdir(path) if os.path.isdir(os.path.join(path, sub))]
                music_dirs.extend(subdirs)

    logging.info(f"Detected music directories: {music_dirs}")
    return music_dirs

if __name__ == "__main__":
    delay_seconds = int(os.environ.get("SCAN_INTERVAL", "3600"))

    logging.info(f"SCAN_INTERVAL = {delay_seconds} seconds ({delay_seconds / 3600:.2f} hours)")

    while True:
        music_dirs = get_music_dirs()

        if not music_dirs:
            logging.warning("No music directories detected.")

        logging.info("Starting scan...")
        for music_root in music_dirs:
            logging.info(f"Scanning directory: {music_root}")
            walk_music_folder(music_root)

        if delay_seconds < 3600:
            logging.info(f"Waiting {delay_seconds} seconds before next scan...\n")
        else:
            logging.info(f"Waiting {delay_seconds / 3600:.2f} hours before next scan...\n")
        time.sleep(delay_seconds)
