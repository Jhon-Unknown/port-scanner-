#!/usr/bin/env python3
#1/5/2025
#Port scanner Project 
import sys
import socket
from datetime import datetime 
#Define our target

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate host name into ipv4
else:
	print("invalid amount of arguments.")
	print("syntax: python3 scanner.py <ip>")
	sys.exit(1)
	
# makes it look good and readable 
print("-" * 50)
print("Scanning target: "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

# Loop for the port scanner, you can chnage the range into anything
socket.setdefaulttimeout(1)

try:
	for port in range(58, 100):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# ensure the socket respects the global timeout in environments that ignore the default
		s.settimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"port {port} is open")
		s.close()
# if we want our port scanner to stop, or we encountered errors. 
		
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
	
except socket.gaierror:
	print("Host name could not be resolved.")
	sys.exit()
	
except socket.error:
	print("could not connect to server.")
	sys.exit()
