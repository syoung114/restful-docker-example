"""
This script is what turns chessless into a rest container architecture.

It works by overriding the undaemonize function so that whenever it is called in playchess, a rest call via `requests` can be made to the docker container that is holding the undaemonize function we actually want.

This is the main script of chessless_rest. That makes it responsible for storing the address of the docker container.

In a real world example, I imagine the codebase would be more integrated with itself and externally overriding an import inside a git submodule to be considered unusual. I choose this approach so that it is easy to understand. Maybe there are benefits though. There is a potential argument to be made about modularity and separation of concerns at the cost of hacked/deceptive imports.
"""

#source:
#https://stackoverflow.com/questions/3012473/how-do-i-override-a-python-import
#https://stackoverflow.com/question30379893/replacing-an-imported-module-dependency 

import argparse
parser = argparse.ArgumentParser('Play chess with a restful docker host')
parser.add_argument('address', type=str, help='The IP address of the docker container')
args = parser.parse_args()

import sys
#del sys.modules['chessless.undaemonize'] #module has not been loaded yet so no del needed
sys.modules['undaemonize'] = __import__('move_server.undaemonize')

from chessless.src import playchess
playchess.depth, playchess.play_as_black = playchess.get_arguments()

import move_server.undaemonize
move_server.undaemonize.docker_address = args.address
move_server.undaemonize.depth = playchess.depth
move_server.undaemonize.just_last_line = True

import chess
def stockfish_move():
    move_server.undaemonize.fen = playchess.board.fen()

    stockfish = move_server.undaemonize.undaemonize()
    
    sf_move = playchess.regex.search(stockfish).group(0)
    sf_uci = chess.Move.from_uci(sf_move)
    playchess.board.push(sf_uci)

playchess.stockfish_move = stockfish_move

import curses
curses.wrapper(playchess.main)
