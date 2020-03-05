#!/usr/bin/env python3

# -*- coding: utf-8 -*-

###############################################################################

'''Dezoominfo scrapes employee information from zoominfo.com'''
 
###############################################################################

from __future__ import nested_scopes

import argparse
import csv
import pprint
import tempfile
import re
import sys
import time

from pyvirtualdisplay import Display
from selenium import webdriver
from fake_useragent import UserAgent

###########################################################################

# www.oreilly.com/library/view/python-cookbook/0596001673/ch03s15.html
def multiple_replace(adict, text):
        regex = re.compile("|".join(map(re.escape, adict.keys(  ))))
        return regex.sub(lambda match: adict[match.group(0)], text)

###########################################################################

def main(args):
    ua = UserAgent()

    display = Display(visible=0, size=(800, 600))
    display.start()


    profile = webdriver.FirefoxProfile()
    profile.set_preference('general.useragent.override', ua.random)

    log = tempfile.NamedTemporaryFile()
    browser = webdriver.Firefox(service_log_path=log.name)


    for i in range(1,int(args.pages)+1):
        browser.get('%s?pageNum=%s' % (args.url,i))

        # added becuse cloudflair checking
        while 'zoominfo.com' not in browser.title.lower():
            time.sleep(1)

        names = browser.find_elements_by_class_name('tableRow_personName')
        titles = browser.find_elements_by_class_name('job-title')

        time.sleep(1) #timing bug, sometimes not all names

        for i,name in enumerate(names):

            if not name.text: continue

            first = name.text.strip().split(' ')[0]
            last = name.text.strip().split(' ')[-1]
            title = ' '.join(titles[i].text.strip().replace(',',' ').split())

            print(
                multiple_replace({
                    'f':first[0],
                    'F':first,
                    'l':last[0],
                    'L':last,
                    'T':title,
                    'D':args.domain},
                        args.output))


    browser.quit()
    display.stop()

###############################################################################

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Dezoominfo scrapes employee information from zoominfo.com')
        #epilog='URL FORMAT: https://www.zoominfo.com/pic/COMPANY/NUMBER\r\n\r\n')

    parser.add_argument('--url',
	required=True,	
        help='set url to scrape (https://www.zoominfo.com/pic/COMPANY/NUMBER)')			

    parser.add_argument('--pages',
	required=True,	
	help='set number of pages to scrape.')			

    parser.add_argument('--domain',
	required=True,	
	help='set domain to use for output formatting.')			

    parser.add_argument('--output',
	required=False,	
        default='F,L,T,fL@D',
        help='set format to output f,F,l,L,D,T [F,L,T,fL@D]')			

    args = parser.parse_args()

    try:
        main(args)
    except (KeyboardInterrupt, SystemExit):
        sys.exit()

###############################################################################


