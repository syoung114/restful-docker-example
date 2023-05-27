from flask import Flask, request
#from chessless.src import undaemonize
import undaemonize

import os.path
app = Flask(__name__)

@app.errorhandler(500)
def internal_error(error):
    return str(error), 500

#@app.route('/eval', methods=['GET'])
@app.route('/eval')
def test():
    stockfish = undaemonize.undaemonize(
        './stockfish',
        f'd'.split(';'),
        False
    ).rstrip()
    return stockfish 
#fen = request.args.get("fen").replace('+', ' ')
#depth = request.args.get("depth")
#stockfish = undaemonize.undaemonize(
#    './stockfish',
#    f'position fen \'{fen}\';go depth {depth}'.split(';'),
#    True
#).rstrip()
#return stockfish 

@app.route('/')
def hello():
    return 'chessless'

if __name__ == '__main__':
    app.run()
