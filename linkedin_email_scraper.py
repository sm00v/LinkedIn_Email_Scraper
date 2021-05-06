import json
import requests as r
import argparse
import bs4
import re
import os
import signal
import sys

# ||\\\\ kekw

def filter_names(prospects):
    for entry in prospects:
        name = entry[len(entry)-1]
        length_name = len(name)
        if length_name <= 1 or length_name >= 100: pass
        elif len(name.split(' ')) >= 4: bad.append(name)
        elif not name.replace(' ', '').isalpha(): bad.append(name)
        else:
            try: int(name)
            except Exception: good.append(name);

def parse_page(page):
    start = ';accessibilityText&quot;:&quot;View '
    end = 'âs profi'
    entries = page.split(end)
    new_entries = [entry.split(start) for entry in entries]
    return new_entries

def make_request(page_num):
    if len(args.cookie) <= 0:
        sys.exit('[-] You haven\'t hardcoded or entered your li_at cookie yet d3rp.')
    else:
        url = "https://www.linkedin.com/search/results/index/?keywords=" \
              + str(r.utils.quote(args.keywords)) \
              + "&origin=GLOBAL_SEARCH_HEADER&page=" \
              + str(page_num)
        cookie = {'li_at': '"' + args.cookie + '";'}
        page = r.get(url, cookies=cookie).text
        return page

def control():
    for page_num in range(1, int(args.length_pages) + 1):
        page = make_request(page_num)
        entries = parse_page(page)
        filter_names(entries)
        print("[+] Scraping page " + str(page_num) + " Good:" + str(len(good)) + " Bad:" + str(len(bad)))
    log_names()

def prompt(name):
    fix_name = input('[-] Fix me ['+name+']: ')
    return fix_name

def name_format(name):
    first_name = name.split(' ')[0]
    last_name = name.split(' ')[1]
    f_init = name.split(' ')[0][0]
    l_init = name.split(' ')[1][0]
    delimiter = args.delimiter
    if args.email is not None:
        email = '@' + args.email
    else: email = ''
    if args.first_initial and args.last_initial:
        name = f_init + delimiter + l_init + email; return name
    elif args.first_initial:
        name = f_init + delimiter + last_name + email; return name
    elif args.last_initial:
        name = first_name + delimiter + l_init + email; return name
    else:
        return first_name + delimiter + last_name + email

def log_names():
    global good; good = list(set(good))
    global bad; bad = list(set(bad))
    log_file = open(args.log_file, 'w')
    print('[+] Scraped (saved) '+str(len(good))+' names!')

    for name in good:
        name = name_format(name)
        log_file.write(name); log_file.write('\n')

    print('[-] Names to fix [Enter to skip] ctrl+c if UDGAF: '+str(len(bad)))
    for name in bad:
        new_name = prompt(name)
        if new_name == '':
            pass
        else:
            new_name = name_format(new_name)
            log_file.write(new_name); log_file.write('\n')
    print('[+] Saved to output.txt')

if __name__ == '__main__':
    good = []
    bad = []
    cookie = '' #hardcode me
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', action='store', dest='keywords', nargs='?', required=True,
                        help='Search term keywords.')
    parser.add_argument('-p', action='store', dest='length_pages', nargs='?', default=100, const=100,
                        help='How many linked in pages you want to scrape. [Default all 100]')
    parser.add_argument('-c', action='store', dest='cookie', nargs='?', default=cookie, const=cookie,
                        help='LinkedIn li_at session cookie. [AQEDAR1hbLMFawzeAAABd5bk........CQBPcCMRrTC5t55shATUJv]')
    parser.add_argument('-f', action='store_true', dest='first_initial',
                        help='Save first name as first initial.')
    parser.add_argument('-l', action='store_true', dest='last_initial',
                        help='Save last name as last initial.')
    parser.add_argument('-e', action='store', dest='email',nargs='?', default=None, const=None,
                        help='Append a domain to each name.')
    parser.add_argument('-d', action='store', dest='delimiter',nargs='?', default=' ', const=' ',
                        help='Delimiter to split between first and last name.')
    parser.add_argument('-o', action='store', dest='log_file', nargs='?', default='output.txt', const='output.txt',
                        help='Output list to file.')
    args = parser.parse_args()
    try:
        control()
    except KeyboardInterrupt:
        sys.exit('\n[-] Exiting')