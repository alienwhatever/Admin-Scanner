#!/usr/bin/env python3

##### list.txt is get form --> https://github.com/bdblackhat/admin-panel-finder/edit/master/link.txt
try:
	import requests
	import pyfiglet
	from colorama import Fore
	import os
	import sys
	from progress.bar import Bar	# module for loading
except:
	print("Require Module Not Found \n Try pip3 install -r requirement.txt")
	exit()


red = Fore.RED
yellow = Fore.YELLOW
green = '\033[1;32;40m'
white = '\033[0;37;40m'
blue = Fore.BLUE

extimate = []

def banner():	# banner
	print(yellow)
	## logo
	print(f"""
 /\  _|._ _ o._ (_  _ _.._ ._  _ ._ 
/--\(_|| | ||| |__)(_(_|| || |(/_| 
*----------------------------------*{green}
Developer => Unknow 4L13N
Country   => Myanmar
Email	  => unknow4l13n@gmail.com
github	  => https://github.com/swam-htet-a{white}
  """)




# open and list
def open_list():
	print("Reading Lines")
	f = open('list.txt', 'r')
	admin_list = f.readlines()
	print(f"{len(admin_list)} numbers of lines found in list.txt!")

	scan(admin_list)

# scan
def scan(admin_list):
	global extimate
	print(blue)
	url = input("Enter Website To Scan \n[example http://www.1234fakeweb.com]: ")
	try:
		requests.get(url)
	except:
		print(f"{red}Error Wrong Url Or Server Down!")
		print(f"{blue}Example Url: http://www.fakeweb.com")
		print(f"{blue}Example Url: http://fakeweb.com")

	# make sure the url
	if url[-1] == '/':
		url_length = len(url) - 1
		url = url[0:url_length]	# pure url to requests

	else:
		pass

	print(green)
	bar = Bar('Processing', max=len(admin_list))	# loading
	for lines in admin_list:
		lines_len = len(lines)	# lenght of lines
		minus_len = lines_len - 1 # minus 1 from length of lines
		link = lines[0:minus_len]	# url to requests
		scan = url + '/' + link
		try:
			# Scanning
			r = requests.get(scan)
			if r.status_code == 200:
				# admin url found
				extimate.append(scan)	# add to extimate admin url list
				bar.next()
			else:
				# admin url not found
				bar.next()
		except:
			pass

	bar.finish()
	print("")

	# print out the extimate admin url list
	print(f"{green}{'*' * 10} Extimate Admin Panel Url List {'*' * 10}")
	for links in extimate:
		print(links)
	print(white)

# fun to start program
def final_fun():
	banner()
	open_list()
	# open_list will start the scan fun:


if __name__ == '__main__':
	final_fun()

else:
	print("Error")
