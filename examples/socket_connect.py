import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("packageman.comlu.com", 80))
