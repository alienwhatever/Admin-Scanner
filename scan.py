#!/usr/bin/python3

from threading import Lock, Thread
from requests import get
from requests.exceptions import ConnectionError as fail
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
--proxy <prorocol>-<proxyserverip:port> - Scan admin panel using proxy server
<url of website> - Website to scan

Example:
./{0} example.com
./{0} --proxy http-1.2.3.4:8080 example.com
""".format(argv[0]))
    exit()
else:
    if '--proxy' in argv[1]:
        websites_to_scan = argv[3:]
        proxy_enable = True
        proxyprotocol, proxyserver = argv[2].split('-')
        print ('Using Proxy - True')
    else:
        websites_to_scan = argv[1:]

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


print (msg)
for website in websites_to_scan:
    if website[-1] != '/':
        website = website + '/'
    # put admin panel urls to queue
    with open('list.txt', 'r') as f:
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
