# Admin-Scanner
#### ***Website Admin Panel Finder***

##  How To Install ***(Linux/pc)***

* sudo apt install python3

* sudo apt install python3-pip

* sudo apt install git

* git clone https://github.com/alienwhatever/Admin-Scanner.git cd Admin-Scanner


## How to Install ***(Termux/Android)***

* pkg update && pkg upgrade

* pkg install python3

* pkg install git

* git clone https://github.com/alienwhatever/Admin-Scanner.git

* cd Admin-Scanner

* pip3 install -r requirement.txt

## Usage
```
author: alienwhatever
credit github.com/bdblackhat for list.txt
orginal-source-of-list.txt -  https://github.com/bdblackhat/admin-panel-finder/blob/master/link.txt

This tool is for educational and testing purposes only
I am not responsible for what you do with this tool

Usages:

-site <url of website> - Website to scan

--proxy <prorocol>-<proxyserverip:port> - Scan admin panel using proxy server

 --t <second(s)> - Time delay for a thread to scan (To prevent from getting HTTP 508)

--w <path/of/custom/wordlist> - custom wordlist

Example:
./scan.py -site example.com
./scan.py -site example.com --t 1
./scan.py -site example.com example2.com
./scan.py -site example.com --w /custom/wordlist/list.txt
./scan.py --proxy http-1.2.3.4:8080 -site example.com

```


