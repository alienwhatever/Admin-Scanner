#!/usr/bin/env python3

##### list.txt is get form --> https://github.com/bdblackhat/admin-panel-finder/blob/master/link.txt
try:
	import argparse
	import requests
	from colorama import Fore
	import os
	import sys
	from progress.bar import Bar	# module for loading
except:
	print("Require Module Not Found \n Try pip3 install -r requirements.txt")
	exit()


parser = argparse.ArgumentParser()
parser.add_argument('url', metavar="url", type=str, help="Target url to scan", nargs="+")
parser.add_argument('-w', metavar="-w", type=str, help="Custom wordlist") 	# to ADD PARSER
args = parser.parse_args()

# define colors
red = Fore.RED
yellow = Fore.YELLOW
green = '\033[1;32;42m'
white = Fore.WHITE
blue = Fore.BLUE

extimate = []

def banner():	# banner
	print(f"""
{white} [MADE IN MYANMAR]{yellow}
*----------------------------------*{white}""")
	
	
# open the list and call the scan function
def open_list(url):
	print("Reading Lines")
	# check if user define -w custom wordlist value or not
	# if -w custom word list is not define use default wordlist to scan
	if args.w == "" or None:
		try:
			print(args.w)
			f = open(args.w, 'r')

		except Exception as error:
			print(error)
			return 1
	else:
		f = open('list.txt', 'r')

	admin_list = f.readlines()

	print(f"{len(admin_list)} numbers of lines found in list.txt!")

	scan(admin_list, url)

# scan
def scan(admin_list, url):
	global extimate

	# make sure the url
	if url[:7] == "http://" or url[:8] == "https://":
		pass
	else:
		url = 'http://' + url

	print("[Target url] - " + url)

	print(blue)

	try:
		requests.get(url)
	except:
		print(f"\n{red}[Error] Wrong/Bad Url Or Server Down!")
		print("Include http or https in url")
		print(f"{white}Example Url: http://www.fakeweb.com")
		print(f"{white}Example Url: https://fakeweb.com")
		sys.exit()


	print(white)
	bar = Bar('Processing', max=len(admin_list))	# loading

	for panel in admin_list:
		admin_url = url + '/' + panel
		admin_url = admin_url.encode().decode()

		try:
			# Scanning
			r = requests.get(admin_url.strip())
			if r.status_code == 200:
				# admin url found
				extimate.append(admin_url)	# add to extimate admin url list
				bar.next()
			else:
				# admin url not found
				bar.next()
		except:
			pass

	bar.finish()
	print("")

	if len(extimate) == 0:
		print(f"\n{red}Sorry No Admin Panel Found!{white}")

	else:
		# print out the extimate admin url list
		print(f"{'*' * 10} {green}Extimate Admin Panel URL(s) List{white} {'*' * 10}")
		for links in extimate:
			print(links)
		print(white)

# fun to start program
def final_fun(url):
	banner()
	open_list(url)
	# open_list will start the scan function:


if __name__ == '__main__':
	if args.url != '' or None:
		url = args.url

		final_fun(url[0])
	else:
        	sys.exit(f"Defind the argument!\n Type python3 {__name__}")

else:
	print("Error")

