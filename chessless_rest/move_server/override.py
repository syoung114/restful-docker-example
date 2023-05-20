"""
This script is what turns chessless into a rest container architecture.

It works by overriding the undaemonize function so that whenever it is called in playchess, a rest call via `requests` can be made to the docker container that is holding the undaemonize function we actually want.

This is the main script of chessless_rest. That makes it responsible for storing the address of the docker container.

In a real world example, I imagine the codebase would be more integrated with itself and externally overriding an import inside a git submodule to be considered unusual. I choose this approach so that it is easy to understand. Maybe there are benefits though. There is a potential argument to be made about modularity and separation of concerns at the cost of hacked/deceptive imports.
"""

#source:
#https://stackoverflow.com/questions/3012473/how-do-i-override-a-python-import
#https://stackoverflow.com/questions/30379893/replacing-an-imported-module-dependency

import argparse
parser = argparse.ArgumentParser('Play chess with a restful docker host')
parser.add_argument('address', type=str, help='The IP address of the docker container')
args = parser.parse_args()

import sys
del sys.modules['chessless.undaemonize']
sys.modules['chessless.undaemonize'] = __import__('move_request')

from chessless.src import playchess
playchess.depth, playchess.play_as_black = playchess.get_arguments()

import move_request
move_request.fen = playchess.board.fen()
move_request.depth = playchess.depth
move_request.docker_address = args.address

import curses
curses.wrapper(playchess.main)
