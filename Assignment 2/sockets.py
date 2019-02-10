""" URL : http://data.pr4e.org/intro-short.txt """

""" program to retrieve the URL and print out the headers and data.
Make sure to change the code to retrieve the above URL - the values are different for each URL. """



import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80)) #connect to the host
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()