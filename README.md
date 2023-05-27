# RESTful-Docker-Example

## Introduction

This is an example of using Docker as a host and a Python script as a client. Here the host contains a variety of test scripts that the client can interact with. These include:

### chessless-rest/

[My original chessless program](https://github.com/syoung114/chessless). This is an introductory example which divides an existing program such that a critical operation is performed remotely. In chessless-rest, the chess moves made by the CPU (stockfish) is delegated to a docker container running Flask. I consider this introductory because there are no CRUD operations and the host has no state. It is great as a minimal template though.

## The architecture

TODO

## Usage
This project assumes you are using a Linux distribution and have both Python and Docker installed.

1. Clone this repository and `cd` to it.
2. `chmod +x build.sh run.sh`

## License
**Creative Commons Zero 1.0 Universal**. Public domain, but please read it yourself.
