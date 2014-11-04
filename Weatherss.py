#Bader Alsalem 
#210219676
country = raw_input("Please, enter a country: ")
 
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "api.openweathermap.org"
port = 80
request = "GET /data/2.5/weather?q={} HTTP/1.1\r\nHost: api.openweathermap.org\r\n\r\n"
s.connect((host, port))
s.send(request.format(country))
data01 = s.recv(1024)
data02 = s.recv(1024)
s.close()
tempStart = data01.find("temp") + 6
tempEnd = data01.find("pressure") - 2
dcrpStart = data01.find("description") + 14
dcrpEnd = data01.find("icon") - 3
tempraK = data01[tempStart:tempEnd]
tempraC = float(tempraK) - 273.15
descrip = data01[dcrpStart:dcrpEnd]
 
print "The temperature in {0} is {1}C and the weather is {2}".format(country, tempraC, descrip)
