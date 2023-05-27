# RESTful-Docker-Example

## Introduction

This is an example of using Docker as a host and a Python script as a client. Here the host contains a variety of test scripts that the client can interact with. These include:

### chessless-rest/

[My original chessless program](https://github.com/syoung114/chessless). This is an introductory example which divides an existing program such that a critical operation is performed remotely. In chessless-rest, the chess moves made by the CPU (stockfish) is delegated to a docker container running Flask. I consider this introductory because there are no CRUD operations and the host has no state. It is great as a minimal template though.

## Usage
Each example has some scripts in a sh/ folder that suggest its usage. If you are familiar with docker (and you have it installed, of course) you can figure out the usage easily by looking at these scripts. `chmod +x` as usual.

This repository contains submodules so remember to **recursively** activate them if you did not do so during the `git clone` command.


## Contributions

Go right ahead. Submit an issue first.

## License
Each example has its own license due chessless having particular dependencies.
