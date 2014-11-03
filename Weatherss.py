#Bader Alsalem 
#210219676
country = raw_input("Please, enter a country\n(no spaces): ")

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "api.openweathermap.org"
port = 80
host_ip = socket.gethostbyname(host)
request = "GET /data/2.5/weather?q={} HTTP/1.1".format(country)
s.connect((host, port))
s.send(request.encode())
s.close()
