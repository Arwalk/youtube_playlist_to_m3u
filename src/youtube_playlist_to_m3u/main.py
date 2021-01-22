# -*- coding: utf-8 -*-

import argparse
import sys
import logging
import youtube_dl

from youtube_playlist_to_m3u import __version__

__author__ = "Arwalk"
__copyright__ = "Arwalk"
__license__ = "mit"

from youtube_playlist_to_m3u.tools import PlaylistExtractorFromLogs, build_m3u

_logger = logging.getLogger(__name__)

def get_arg_parser():
    parser = argparse.ArgumentParser(
        description="Builds a M3U playlist from a youtube playlist link")
    parser.add_argument(
        "--version",
        action="version",
        version="youtube_playlist_to_m3u {ver}".format(ver=__version__))
    parser.add_argument(
        dest="link",
        help="the link to the youtube playlist",
        type=str)
    parser.add_argument(
        dest="outputfile",
        help="the name of the file to output",
        type=str)
    return parser

def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Builds a M3U playlist from a youtube playlist link")
    parser.add_argument(
        "--version",
        action="version",
        version="youtube_playlist_to_m3u {ver}".format(ver=__version__))
    parser.add_argument(
        dest="link",
        help="the link to the youtube playlist",
        type=str)
    parser.add_argument(
        dest="outputfile",
        help="the name of the file to output",
        type=str)
    return get_arg_parser().parse_args(args)



def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)

    extractor = PlaylistExtractorFromLogs()

    ydl_opts = {
        'dump_single_json': True,
        'extract_flat': True,
        'logger': extractor
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([args.link]) # it doesn't actually download anything, don't worry.

    if extractor.entries is not None :
        m3u = build_m3u(extractor.entries)
        m3u = [bytes(x, 'utf-8').decode('utf-8', 'ignore') for x in m3u]
        with open(args.outputfile, "w", encoding='utf-8') as output_file:
            output_file.writelines(m3u)

def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
