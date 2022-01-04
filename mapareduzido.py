#!/usr/bin/env python

from os import system
import curses, commands, time
import socket
import socket
def execute_cmd():
	while True:
		screen.clear()
		screen.border(0)

        	o = commands.getoutput("cat mapadesenho1")

		p = commands.getoutput("ping -i 0 -c 5 200.129.176.4| grep ttl | wc -l")
		p2 = commands.getoutput("ping -i 0 -c 5 200.139.25.34| grep ttl | wc -l")
		p4 = commands.getoutput("ping -i 0 -c 5 200.139.24.14| grep ttl | wc -l")

		try:
                   v = HOST = '200.139.25.50'     # Endereco IP do Servidor
                   b = HOST = '200.138.149.218'
		           c = HOST = '200.138.149.187'  

		   PORT = 80            # Porta que o Servidor esta
                   tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                   dest = (HOST, PORT)
                   a=tcp.connect(dest)
                   v=1
		   c=1
		   b=1
		
		except:
                
		   v=0
		   c=0
		   b=0

                   print v 
		   print c
		   print b
		   tcp.close()

		screen.addstr(2, 25, o)
		curses.start_color()

		curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
		curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        
		time.sleep(1)
		l = len(p)

		if l > 1:
			p = 0
			p2 = 0
			p4 = 0
		pings = int(p)
		ping2 = int(p2)
		ping4 = int(p4)
	
		if pings == 5:
 			screen.addstr(17,40,"* Palmas",curses.color_pair(2))      
		elif pings < 5:
			screen.addstr(17,40,"* Palmas",curses.color_pair(1))
		if v == 1:
			screen.addstr(9,40,"* Araguaina",curses.color_pair(2))		     
		elif v == 0:
			screen.addstr(9,40,"* Araguaina",curses.color_pair(1))
		if ping2 == 5:
			screen.addstr(23,35,"* Gurupi",curses.color_pair(2))
		elif ping2 < 5:
			screen.addstr(23,35,"* Gurupi",curses.color_pair(1))
		if b == 1:
			screen.addstr(19,40,"* Porto Nacional",curses.color_pair(2))
		elif b == 0:
			screen.addstr(19,40,"* Porto Nacional",curses.color_pair(1))
		if ping4 == 5:
			screen.addstr(5,40,"* Araguatins",curses.color_pair(2))
		elif ping4 < 5:
			screen.addstr(5,40,"* Araguatins",curses.color_pair(1))
		if c == 1:
			screen.addstr(16,33,"* Paraiso do Tocantins",curses.color_pair(2))
		elif c == 0:
			screen.addstr(16,33,"* Paraiso do Tocantins",curses.color_pair(1))

	
		screen.refresh()

x=0
while x != ord('4'):
	screen = curses.initscr()
	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, "Escolha uma Numero...")
	screen.addstr(4, 4, "1 - MAP")
	screen.addstr(5, 4, "4 - Exit")
	screen.refresh()

	x = screen.getch()

	if x == ord('1'):
		curses.endwin()
		execute_cmd()
        
	curses.endwin()

