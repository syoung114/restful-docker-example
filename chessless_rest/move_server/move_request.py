import requests

docker_address = ''
fen = ''
depth = -1

def undaemonize(pathargs, stdins, just_last_line=False):
    #I am intentionally ignoring the arguments I just passed because REST arguments should be encapsulated.
    #Instead fen and depth are used and are defined in override.py.
    succinct = 1 if just_last_line else 0
    r = requests.get(f'{docker_address}?fen={fen}&depth={depth}&succinct={succinct}')
    return r.text
