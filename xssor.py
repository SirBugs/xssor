#!/usr/bin/python

# // This tool is totally writen in python3
# // Idea & Coing By: Twitter@SirBagoza

# // Importing Modules:
# // ////////////////////

import os
import sys
import time
import requests
import argparse
import colorama
from colorama import Fore, Back, Style
from multiprocessing.dummy import Pool as ThreadPool
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# // Arguments Assigning:
# // //////////////////////

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="single usage for 1 URL")
parser.add_argument("-l", "--list", help="multi usage for more than a URL")
parser.add_argument("-t", "--threads", help="select threads for requests (default: 50)")
parser.add_argument("-o", "--output", help="output file (default: xssor.output)")
args = parser.parse_args()

# // Coloring:
# // ///////////

WHITE = Fore.WHITE
RED = Fore.RED
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
CYAN = Fore.CYAN

# // Logo Printing:
# // ////////////////

print(WHITE+"\n\n\t\t /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$ "); time.sleep(0.1)
print("\t\t| $$  / $$ /$$__  $$ /$$__  $$ /$$__  $$| $$__  $$"); time.sleep(0.1)
print("\t\t|  $$/ $$/| $$  \__/| $$  \__/| $$  \ $$| $$  \ $$"); time.sleep(0.1)
print("\t\t \  $$$$/ |  $$$$$$ |  $$$$$$ | $$  | $$| $$$$$$$/"); time.sleep(0.1)
print("\t\t  >$$  $$  \____  $$ \____  $$| $$  | $$| $$__  $$"); time.sleep(0.1)
print("\t\t /$$/\  $$ /$$  \ $$ /$$  \ $$| $$  | $$| $$  \ $$"); time.sleep(0.1)
print("\t\t| $$  \ $$|  $$$$$$/|  $$$$$$/|  $$$$$$/| $$  | $$"); time.sleep(0.1)
print("\t\t|__/  |__/ \______/  \______/  \______/ |__/  |__/"); time.sleep(0.1)
print("\n\t\t\tVersion: 0.0.1 (For checking params reflections)"); time.sleep(0.1)
print("\t\t\tBy: Twitter@SirBagoza"); time.sleep(0.3)

# // Main Tool Defining:
# // /////////////////////

if str(args.url) == "None" and str(args.list) == "None": # // Checking if -u and -l not used, Then quit() ! There's nothing to do.
	print("\n\n\t[ "+RED+"WARN"+WHITE+" ] Please read the help docs by running:\n\t\tmain.py -h / main.py --help\n\n\t[ "+GREEN+"HELP"+WHITE+" ] To use the tool correctly run:\n\t\tpython3 main.py -u <URL> / python3 main.py <LIST>\n\n")
	quit() # // quitting from the tool.
else:
	pass

if str(args.output) == "None": # // If the output file is set manually, either use xssor.output as default output file.
	file = open("xssor.output", "a+") # // Default
else:
	file = open(str(args.output), "a+") # // Set

if str(args.threads) == "None": # // Checking if to use the default threads (50) or to set it manually by the user through sw "-t".
	Threads = 50 # // Default
else:
	Threads = int(str(args.threads)) # // Set

# // Main Def:
# // ////////////

def xsser(url):
	global file
	try:
		# // Getting all the parameters part after the "?"
		params_part = url.split("?")[1]
		# // Splitting this part via "&", to get each param alone
		all_pamars_with_values = params_part.split("&")
		# // To know how many grapped params from this url
		params_count = len(all_pamars_with_values)
		# // for loop to go through all the params
		for param_to_play in all_pamars_with_values:
			# // Splitting the param name / param value
			param, value = param_to_play.split("=")
			# // Replaing the param value with our tool's KEY!
			played_param = param_to_play.replace(value, "BAGOZAXSSOR>")
			# // Making a whole new url with this changed param!
			new_url = url.replace(param_to_play, played_param)

			# // Now we gonna make the request for this edited url
			# print("[ Testing ] ::  " + new_url)
			r = requests.get(new_url, allow_redirects=False, timeout=3)

			# // Checking now if the request content (( Page Source )) Containing our tool's KEY !!
			if "BAGOZAXSSOR>" in r.text: # // Found XSS Vulnerability, "<" is reflected without encoding.
				print(WHITE+"[ "+GREEN+"VULN"+WHITE+" ] ::  " + new_url)
				file.write("[ XSS Vulnerability Found ] ::  " + new_url + "\n") # // Saving
			elif "BAGOZAXSSOR" in r.text:
				print(WHITE+"[ "+YELLOW+"REFL"+WHITE+" ] ::  " + new_url)
				file.write("[ Reflected ] ::  " + new_url + "\n") # // Saving
			else:
				pass
	except:
		pass

"""
	# // Example for single code usage:
		xsser("https://themes.shopify.com/themes/pacific/styles/bold?surface_detail=listing&surface_inter_position=1&surface_intra_position=3&surface_type=listing")
"""

# // Start Using The Def:
# // //////////////////////

if str(args.list) != "None":
	print("here")
	_STARTER = open(str(args.list), "r").read().split("\n")
	print(_STARTER)
	def main():
		pool = ThreadPool(Threads)
		try:
			results = pool.map(xsser , _STARTER)
			pool.close()
			pool.join()
		except KeyboardInterrupt:
			print("Exiting...")
			sys.exit(0)
	main()
	file.close()
elif str(args.url) != "None":
	xsser(str(args.url))
else:
	quit()

print(WHITE+"\n\t[ "+RED+"QUIT"+WHITE+" ] Thanks for using! Goodbye!")

# // Plans for V: 0.0.2 :: Gonna make checker for (single encoding) too, and the (double encoding)
	# // %3e - %25%33%65

