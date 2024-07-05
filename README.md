# Simple Python Reverse Shell
Basic python3 reverse shell used against a docker container.

## Quickstart
To use, first build the package
```
docker build -t python-reverse-shell .
```
Then you'll need to run the docker container
```
docker run --rm --name reverse-shell python-reverse-shell
```

On your host machine, you'll then need to open a port to listen to incoming connections on. By default (in the reverse shell code), you will be getting attempted connections to your docker ip address on port `12345`. Because of how docker works, we won't need to expose this to a port locally (hence why we didn't specify a `-p <port>` in the run command). You can listen for an open port by running:
```
nc -lvp 12345
```

