# chessless-rest

See my original chessless code [here](https://github.com/syoung114/chessless).

## Some notes about the design decisions:

You might consider containerizing a flask application redundant because the underlying flask application can also be port forwarded and assigned a domain. However, although this scenario is an example, I have some arguments on why containerizing flask is a good idea:

1. Security. Because the application is virtualized and there are minimal dependences on the system, the number of system exploits are minimized. If somebody could obtain the underlying filesystem, there is nothing new to find. There is the python source code, sure, but it's open source anyway. I'd use a compiled langauge in situations where intellectual property was a greater concern.

2. Dependencies/reproducibility. This one is self-explanatory. Everything that is required to "make it run on my machine" is listed in requirements.txt and the Dockerfile. Just working with Flask and requirements.txt ignores system variations in the OS/distribution. And as mentioned in the previous point, what is in the docker image is isolated and minimally reproducible.

3. Portability. If it can run docker, it can run this app.

## License

You may use the code as a template and use that template however you like but the underlying chessless/Stockfish code is licensed under GPL-3.0. By "template" I mean a body of work that ought to be replaced with a work of your owm.
