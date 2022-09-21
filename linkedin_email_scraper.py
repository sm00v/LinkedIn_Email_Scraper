import sys
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By
import argparse


def create_profile():
    profile = webdriver.FirefoxProfile()
    if args.proxy is not None:
        profile.set_preference("network.proxy.type", 5)
        profile.set_preference("network.proxy.socks", args.proxy)
        profile.set_preference("network.proxy.socks_port", args.proxy_port)
        profile.set_preference("network.proxy.socks_remote_dns", True)
        profile.set_preference("general.useragent.override", "Gecko")
        profile.update_preferences()
        return profile
    else:
        profile.set_preference("browser.privatebrowsing.autostart", True)
        profile.update_preferences()
        return profile

def load_browser():
    profile = create_profile()
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, firefox_profile=profile)
    return driver

def argparser():
    cookie = '' #hardcode me

    parser = argparse.ArgumentParser(description="Selenium LinkedIn Scraper >:D")
    parser.add_argument("-p", "--proxy", help="The proxy ip in format {10.0.0.1}.", default='127.0.0.1')
    parser.add_argument("-pp", "--proxy_port", type=int, help="The proxy port in format {1080}.", default=1080)
    parser.add_argument('-c', action='store', dest='cookie', nargs='?', default=cookie, const=cookie,
                        help='LinkedIn li_at session cookie. [AQEDAR1hbLMFawzeAAABd5bk........CQBPcCMRrTC5t55shATUJv]')
    parser.add_argument('-fi', action='store_true', dest='first_initial',
                        help='Save first name as first initial.')
    parser.add_argument('-li', action='store_true', dest='last_initial',
                        help='Save last name as last initial.')
    parser.add_argument('-f', action='store_true', dest='first_name',
                        help='Save first name.')
    parser.add_argument('-l', action='store_true', dest='last_name',
                        help='Save last name.')
    parser.add_argument('-e', action='store', dest='email', nargs='?', default=None, const=None,
                        help='Append a domain to each name.')
    parser.add_argument('-d', action='store', dest='delimiter', nargs='?', default='', const='',
                        help='Delimiter to split between first and last name.')
    parser.add_argument('-i', action='store', dest='company_id', nargs='?', default=None, const=None,
                        help='Company ID found in URL of LinkedIn business page. [XXXXXXX]')
    parser.add_argument('-o', action='store', dest='log_file', nargs='?', default='output.txt', const='output.txt',
                        help='Output list to file.')
    return parser.parse_args()

def find_names(): # search for names in loaded page
    raw_names = []
    for num in range(1,11):
        path = f"/html/body/div[" + str(num)
        for x in range(1, 11):
            try:
                name = driver.find_element_by_xpath(f"{path}]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/ul/li[{x}]/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]").text
                if name:
                    raw_names.append(name)
                    # print(f"Found name: ",name)
            except Exception as e:
                # print("[-] Exception caught at find_names()")
                pass
    return raw_names

def login():
    if len(args.cookie) <= 0:
        sys.exit('[-] You haven\'t hardcoded or entered your li_at cookie yet d3rp.')

    print('[+] Logging in')
    search_url = f'https://www.linkedin.com/search/results/people/?currentCompany=["{args.company_id}"]&origin=COMPANY_PAGE_CANNED_SEARCH&page=1'
    driver.get(url)
    time.sleep(2)
    driver.add_cookie({'name': 'li_at', 'value': args.cookie})
    driver.get(search_url)
    time.sleep(5)

def get_pages():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    print("[+] Waiting for hidden elements to unhide.")
    # pages = int(WebDriverWait(driver, 15).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[6]/div[3]/div[2]/div/div[1]/main/div/div/div[3]/div/div/ul/li[10]/button/span"))).text)
    time.sleep(5)
    # pages = int(driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[3]/div/div/ul/li[10]/button/span").text)
    pages = None
    for x in range(1,11):
        try:
            pages = int(driver.find_element_by_xpath(f"/html/body/div[{x}]/div[3]/div[2]/div/div[1]/main/div/div/div[3]/div/div/ul/li[10]/button/span").text)
            if pages:
                break
        except Exception:
            pass
    if pages == None:
        pages = 10
    print(f'[+] Got {pages} pages, finding names.')
    return pages

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


    elif args.first_name and args.last_name:
        name = first_name + delimiter + last_name + email; return name
    elif args.first_name:
        name = first_name + email; return name
    elif args.last_name:
        name = last_name + email; return name
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
    print('[+] Saved to ' + str(args.log_file))

def filter_names(prospects):
    for name in prospects:
        if not name.replace(' ', '').isalpha(): bad.append(name)
        else: good.append(name)

if __name__ == '__main__':
    url = 'https://www.linkedin.com/'

    all_names = []
    good = []
    bad = []
    try:
        args = argparser()
        driver = load_browser()
        login()
        pages = get_pages()
        for page in range(1, pages+1):
            search_url = f'https://www.linkedin.com/search/results/people/?currentCompany=["{args.company_id}"]&origin=COMPANY_PAGE_CANNED_SEARCH&page={page}'
            if page != 1:
                driver.get(search_url)
                time.sleep(3)
            try:
                entries = find_names()
            except Exception as e:
                break
            try:
                filter_names(entries)
            except Exception as e:
                break
            print("[+] Scraping page " + str(page) + " Good:" + str(len(good)) + " Bad:" + str(len(bad)))
        log_names()
        driver.quit()
        sys.exit()
    except KeyboardInterrupt:
        sys.exit('\n[-] Exiting')
