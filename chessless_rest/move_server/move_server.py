from flask import Flask, request
from chessless import undaemonize
#import undaemonize

app = Flask(__name__)

@app.route('/entry', methods=['GET'])
def test():
    fen = request.args.get("fen")
    depth = request.args.get("depth")
    stockfish = undaemonize.undaemonize(
        '/home/steven/desktop/restful-docker-example/chessless_rest/chessless/Stockfish/src/stockfish',
        f'position fen \'{fen}\';go depth {depth}'.split(';'),
        True
    ).rstrip()
    return stockfish 

@app.route('/')
def hello():
    return 'skdfjslkdf'

if __name__ == '__main__':
    app.run()
