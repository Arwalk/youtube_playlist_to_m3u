import json

def build_m3u(entries):
    m3u = ["#EXTM3U\n", '\n']

    for entry in entries:
        duration = int(entry['duration'])
        title = entry['title']
        m3u.append(f"#EXTINF:{duration}, {title}\n")
        m3u.append(f"https://youtu.be/{entry['id']}\n")
        m3u.append('\n')

    return m3u

def get_entries_from_msg(msg):
    return json.loads(msg)["entries"]

class PlaylistExtractorFromLogs(object):

    def __init__(self):
        self.entries = None

    def get_playlist(self, original_msg):
        self.entries = get_entries_from_msg(original_msg)

    def debug(self, msg : str):
        if msg.startswith('{"_type": "playlist"'):
            self.get_playlist(msg)

    def warning(self, msg):
        print(msg)
        pass

    def error(self, msg):
        print(msg)


