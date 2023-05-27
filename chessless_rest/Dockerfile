#compile stockfish on the base image of the one we are about to use (python)
#this particular image is debian with extra things installed. Make is included somewhere in the FROM stack which we need to compile stockfish.
FROM buildpack-deps:bullseye AS stockfish
COPY chessless/Stockfish/ .
RUN cd src/ && make clean && make -j build ARCH=x86-64-modern COMPCXX=g++ && cd ..

#now actually do the thing with python installed
FROM python:bullseye

WORKDIR /move_server

#copy the compiled binary to the image we are using
COPY --from=stockfish src/stockfish .

#copy everything we need to run the server.
COPY chessless/src/undaemonize.py move_server/app.py requirements.txt chessless/init.sh .

RUN pip install -r requirements.txt

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]
