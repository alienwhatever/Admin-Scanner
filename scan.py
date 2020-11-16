#!/usr/bin/python3

from threading import Lock, Thread
from requests import get
from requests.exceptions import ConnectionError as fail
from requests.exceptions import MissingSchema as noschema
from queue import Queue
from time import time
from sys import argv


proxy_enable = False


msg = """
author: alienwhatever
credit github.com/bdblackhat for list.txt
orginal-source-of-list.txt -  https://github.com/bdblackhat/admin-panel-finder/blob/master/link.txt

This tool is for educational and testing purposes only
I am not responsible for what you do with this tool
"""

msg

# show usage to user
if len(argv) == 1:
    print (msg)
    print ('Usages:')
    print ("""
-site <url of website> - Website to scan

--proxy <prorocol>-<proxyserverip:port> - Scan admin panel using proxy server

--w <path/of/custom/wordlist> - custom wordlist

Example:
./{0} -site example.com
./{0} -site example.com example2.com
./{0} -site example.com --w /custom/wordlist/list.txt
./{0} --proxy http-1.2.3.4:8080 -site example.com
""".format(argv[0]))
    exit()
else:
    file_to_open = 'list.txt'
    if '--proxy' in argv[1:]:
        proxy_enable = True
        proxyprotocol, proxyserver = argv[argv.index('--proxy')+1].split('-')
        print ('Using Proxy - True')


    if '-site' not in argv[1:]:
        print ('Which site you wanna scan!!!!')
        exit()

    if '-site' in argv[1:]:
        check = argv[argv.index('-site')+2:]
        websites_to_scan = argv[argv.index('-site')+1:]
        for i in check:
            if i[:2] == '--' or i[:1] == '-':
                websites_to_scan = argv[argv.index('-site')+1]

    if '--w' in argv[1:]:
        file_to_open = argv[argv.index('--w')+1]
# used threading things #
# Lock
# Thread
print_lock = Lock()

admin_panel_list = []

q = Queue()
# run thread function using Queue and Thread()
def thread(website):
    worker = q.get()
    try:
        if proxy_enable:
            r = get('{}{}'.format(website, worker), proxies={proxyprotocol: proxyserver}, allow_redirects=True)
        if not proxy_enable:
            r = get('{}{}'.format(website, worker), allow_redirects=True)

        if r.status_code != 404:
            print ('    Success: ', worker)

    except fail:
        print ('Connection Error')

    except noschema:
        print ('ERROR ERROR ERROR ERROR ERROR')
        print ('ERROR: Where is URL Scheme!!!!!!! example: https://example.com or http://example.com not exmple.com')
        exit()


print (msg)
if type(websites_to_scan) is str:
    websites_to_scan = [websites_to_scan]

for website in websites_to_scan:
    if website[-1] != '/':
        website = website + '/'
    # put admin panel urls to queue
    with open(file_to_open, 'r') as f:
        for line in f:
            q.put(line.strip().encode().decode('utf-8'))
    # create thread and run till Queue is empty
    print ('Result for {}:'.format(website))
    while not q.empty():
        t = Thread(target=thread, args=(website,))
        t.daemon = True
        t.start()

    t.join()
    print('\n')
