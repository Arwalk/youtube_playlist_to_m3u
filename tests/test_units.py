# -*- coding: utf-8 -*-

import pytest
from youtube_playlist_to_m3u.tools import build_m3u
import json

__author__ = "Arwalk"
__copyright__ = "Arwalk"
__license__ = "mit"


def test_build_m3u():
    base = '{"_type": "playlist", "entries": [{"_type": "url_transparent", "ie_key": "Youtube", "id": "4pSWW5_bAkw", ' \
           '"url": "4pSWW5_bAkw", "title": "Ocarina of Time 100% Blindfolded Challenge: Part 2.1 [10-28-20]", ' \
           '"description": null, "duration": 8072.0, "view_count": null, "uploader": null}, {"_type": ' \
           '"url_transparent", "ie_key": "Youtube", "id": "R3YYXTffxrc", "url": "R3YYXTffxrc", "title": "Ocarina of ' \
           'Time 100% Blindfolded Challenge: Part 2.2 [11-4-20]", "description": null, "duration": 7717.0, ' \
           '"view_count": null, "uploader": null}, {"_type": "url_transparent", "ie_key": "Youtube", ' \
           '"id": "wVejbeFaRzc", "url": "wVejbeFaRzc", "title": "Ocarina of Time 100% Blindfolded Challenge: Part 2.3 ' \
           '[11-11-20]", "description": null, "duration": 11055.0, "view_count": null, "uploader": null}, ' \
           '{"_type": "url_transparent", "ie_key": "Youtube", "id": "wVejbeFaRzc", "url": "wVejbeFaRzc", ' \
           '"title": "Ocarina of Time 100% Blindfolded Challenge: Part 2.3 [11-11-20]", "description": null, ' \
           '"duration": 11055.0, "view_count": null, "uploader": null}, {"_type": "url_transparent", ' \
           '"ie_key": "Youtube", "id": "teVuChXcwZw", "url": "teVuChXcwZw", "title": "Ocarina of Time 100% ' \
           'Blindfolded Challenge: Part 2.4 [11-18-20]", "description": null, "duration": 12959.0, "view_count": ' \
           'null, "uploader": null}, {"_type": "url_transparent", "ie_key": "Youtube", "id": "5BL9c4NNIuI", ' \
           '"url": "5BL9c4NNIuI", "title": "Ocarina of Time 100% Blindfolded Challenge: Part 2.5 [11-25-20]", ' \
           '"description": null, "duration": 8982.0, "view_count": null, "uploader": null}, {"_type": ' \
           '"url_transparent", "ie_key": "Youtube", "id": "bd54bB3n_x8", "url": "bd54bB3n_x8", "title": "Ocarina of ' \
           'Time 100% Blindfolded Challenge: Part 2.6 [12-2-20]", "description": null, "duration": 11491.0, ' \
           '"view_count": null, "uploader": null}], "id": "PL1YjFQoXGonZMis2BxPuvG5HSatQ-jZ2Y", "title": "temp", ' \
           '"uploader": "Arwalk", "uploader_id": "UC0bmJPX46rathRubNmnxcAg", "uploader_url": ' \
           '"https://www.youtube.com/user/loloquaker", "extractor": "youtube:tab", "webpage_url": ' \
           '"https://www.youtube.com/playlist?list=PL1YjFQoXGonZMis2BxPuvG5HSatQ-jZ2Y", "webpage_url_basename": ' \
           '"playlist", "extractor_key": "YoutubeTab"} '

    expected = ['#EXTM3U\n',
                '\n',
                '#EXTINF:8072, Ocarina of Time 100% Blindfolded Challenge: Part 2.1 [10-28-20]\n',
                'https://youtu.be/4pSWW5_bAkw\n',
                '\n',
                '#EXTINF:7717, Ocarina of Time 100% Blindfolded Challenge: Part 2.2 [11-4-20]\n',
                'https://youtu.be/R3YYXTffxrc\n',
                '\n',
                '#EXTINF:11055, Ocarina of Time 100% Blindfolded Challenge: Part 2.3 [11-11-20]\n',
                'https://youtu.be/wVejbeFaRzc\n',
                '\n',
                '#EXTINF:11055, Ocarina of Time 100% Blindfolded Challenge: Part 2.3 [11-11-20]\n',
                'https://youtu.be/wVejbeFaRzc\n',
                '\n',
                '#EXTINF:12959, Ocarina of Time 100% Blindfolded Challenge: Part 2.4 [11-18-20]\n',
                'https://youtu.be/teVuChXcwZw\n',
                '\n',
                '#EXTINF:8982, Ocarina of Time 100% Blindfolded Challenge: Part 2.5 [11-25-20]\n',
                'https://youtu.be/5BL9c4NNIuI\n',
                '\n',
                '#EXTINF:11491, Ocarina of Time 100% Blindfolded Challenge: Part 2.6 [12-2-20]\n',
                'https://youtu.be/bd54bB3n_x8\n',
                '\n']

    m3u = build_m3u(json.loads(base)["entries"])

    assert m3u == expected
