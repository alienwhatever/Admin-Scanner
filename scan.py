#!/usr/bin/env python3

##### list.txt is get form --> https://github.com/bdblackhat/admin-panel-finder/edit/master/link.txt
try:
	import requests
	import pyfiglet
	from colorama import Fore
	import os
	from progress.bar import Bar	# module for loading
except:
	print("Require Module Not Found \n Try pip3 install -r requirement.txt")


red = Fore.RED
yellow = Fore.YELLOW
green = '\033[1;32;40m'
blue = Fore.BLUE

extimate = []

def banner():	# banner
	print(yellow)
	## logo
	print("""
      _           _                __                 __
     /.\       ___FJ    _ _____    LJ   _ ___        F __".   ____      ___ _    _ ___     _ ___      ____     _ ___
    //_\\     F __  L  J '_  _ `,      J '__ J      J (___|  F ___J.   F __` L  J '__ J   J '__ J    F __ J   J '__ ",
   / ___ \   | |--| |  | |_||_| |  FJ  | |__| |     J\___ \ | |---LJ  | |--| |  | |__| |  | |__| |  | _____J  | |__|-J
  / L___J \  F L__J J  F L LJ J J J  L F L  J J    .--___) \F L___--. F L__J J  F L  J J  F L  J J  F L___--. F L  `-'
 J__L   J__LJ\____,__LJ__L LJ J__LJ__LJ__L  J__L   J\______J\______/FJ\____,__LJ__L  J__LJ__L  J__LJ\______/FJ__L
 |__L   J__| J____,__F|__L LJ J__||__||__L  J__|    J______FJ______F  J____,__F|__L  J__||__L  J__| J______F |__L
				*-----------------------------------*
				This Program Was Made By Unknow 4L13N""")



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
	url = input("Enter Website To Scan [example http://www.1234fakeweb.com]: ")
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

# fun to start program
def final_fun():
	banner()
	open_list()
	# open_list will start the scan fun

if __name__ == '__main__':
	final_fun()
