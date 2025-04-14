import os
import time

AUDIO_EXTENSIONS = ('.mp3', '.flac', '.ogg', '.wav', '.aac', '.m4a')

def generate_m3u_for_directory(directory):
    playlist_name = os.path.basename(directory.rstrip("/")) + '.m3u'
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

    print(f"Created playlist : {playlist_path}")
    return True

def walk_music_folder(root_music_folder):
    for root, _, _ in os.walk(root_music_folder):
        generate_m3u_for_directory(root)

if __name__ == "__main__":
    music_dirs = os.environ.get("MUSIC_DIRS", "/music").split(",")
    delay_seconds = int(os.environ.get("SCAN_INTERVAL", "3600"))

    while True:
        print("Scanning...")
        for music_root in music_dirs:
            if not os.path.isdir(music_root):
                print(f"The directory does not exist:{music_root}")
            else:
                print(f"Scan of : {music_root}")
                walk_music_folder(music_root)
        
        delay_hours = delay_seconds / 3600
        print(f"Wait {delay_hours:.2f} seconds before next scan...")
        time.sleep(delay_seconds)