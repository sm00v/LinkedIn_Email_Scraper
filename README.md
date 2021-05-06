# LinkedIn Username/Email Formattable Scraper
<b>linkedin_email_scraper.py</b> is a  <a href="https://linkedin.com">linkedin.com</a> scraper tool which queries the LinkedIn global search bar and scrapes all names on pages 1-100 (LinkedIn maximum pages).

## linkedin_email_scraper.py usage:
```
usage: linkedin_email_scraper.py [-h] -k [KEYWORDS] [-p [LENGTH_PAGES]] [-c [COOKIE]] [-f] [-l] [-e [EMAIL]] [-d [DELIMITER]] [-o [LOG_FILE]]

optional arguments:
  -h, --help         show this help message and exit
  -k [KEYWORDS]      Search term keywords.
  -p [LENGTH_PAGES]  How many linkedin pages you want to scrape. [Default all 100]
  -c [COOKIE]        LinkedIn li_at session cookie. [AQEDAR1hbLMFawzeAAABd5bk........CQBPcCMRrTC5t55shATUJv]
  -f                 Save first name as first initial.
  -l                 Save last name as last initial.
  -e [EMAIL]         Append a domain to each name.
  -d [DELIMITER]     Delimiter to split between first and last name.
  -o [LOG_FILE]      Output list to file.
```
   Basic usage of script:
   
    python3 linkedin_email_scraper.py -k "Microsoft" -c AQEDAR1hbLMFawzeAAABd5bk........CQBPcCMRrTC5t55shATUJv
    
   Hardcoded li_at cookie [line 95] in script:
   
    python3 linkedin_email_scraper.py -k "Microsoft"
    
   Specify less pages to scrape:
   
    python3 linkedin_email_scraper.py -k "Microsoft" -p 50

   Advanced usage of linkedin_email_scraper.py:
   
    $ python3 linkedin_email_scraper.py -k "microsoft" -p 5 -d "." -e microsoft.com -f -o microsoft.txt
    [+] Scraping page 1 Good:12 Bad:1
    [+] Scraping page 2 Good:21 Bad:1
    [+] Scraping page 3 Good:28 Bad:3
    [+] Scraping page 4 Good:36 Bad:4
    [+] Scraping page 5 Good:44 Bad:4
    [+] Scraped (saved) 43 names!
    [-] Names to fix [Enter to skip] ctrl+c if UDGAF: 4
    [-] Fix me [Angela M.]: 
    [-] Fix me [Ryan D.]: 
    [-] Fix me [Yuri Diogenes, M.S. Cybersecurity]: Yuri Diogenes
    [-] Fix me [Nina K.]: 
    [+] Saved to microsoft.txt
    
   Example output of microsoft.txt:
   
    M.Russinovich@microsoft.com
    S.Oneeta@microsoft.com
    J.Tiplitsky@microsoft.com
    B.Arsenault@microsoft.com
    A.Patil@microsoft.com
    D.Weston@microsoft.com
    D.Taylor@microsoft.com
    S.Lieu@microsoft.com
    K.Kennebrew@microsoft.com
    J.Victorino@microsoft.com
    Y.Diogenes@microsoft.com
