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

    logging.info(f"Created playlist : {playlist_path}")
    return True

def walk_music_folder(root_music_folder):
    for root, _, _ in os.walk(root_music_folder):
        generate_m3u_for_directory(root)

def get_music_dirs_from_mounts(base_dir="/"):
    candidates = [os.path.join(base_dir, d) for d in os.listdir(base_dir)]
    music_dirs = [d for d in candidates if os.path.isdir(d) and d.startswith("/music")]

    logging.info(f"Mounted files detected: {music_dirs}")
    return music_dirs

if __name__ == "__main__":
    delay_seconds = int(os.environ.get("SCAN_INTERVAL", "3600"))

    while True:
        music_dirs = get_music_dirs_from_mounts()

        if not music_dirs:
            logging.warning("Mounted folders detected: No mounted folders found starting with /music*.")

        logging.info("Scanning...")
        for music_root in music_dirs:
            logging.info(f"Scan of : {music_root}")
            walk_music_folder(music_root)

        delay_hours = delay_seconds / 3600
        if delay_seconds < 3600:
            logging.info(f"Wait {delay_seconds} seconds before next scan...\n")
        else:
            logging.info(f"Wait {delay_seconds / 3600:.2f} hours before next scan...\n")

        time.sleep(delay_seconds)
