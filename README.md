# LinkedIn Username/Email Formattable Scraper
<b>linkedin_email_scraper.py</b> is a  <a href="https://linkedin.com">linkedin.com</a> scraper tool which queries the LinkedIn global search bar and scrapes all names on pages 1-100 (LinkedIn maximum pages).

## 1: linkedin_email_scraper.py usage:
```
usage: linkedin_email_scraper.py [-h] [-k [KEYWORDS]] [-l [LENGTH_PAGES]] [-c [COOKIE]]

optional arguments:
  -h, --help         show this help message and exit
  -k [KEYWORDS]      Search term keywords.
  -l [LENGTH_PAGES]  How many linked in pages you want to scrape. [Default all 100]
  -c [COOKIE]        LinkedIn li_at session cookie. [AQEDAR1hbLMFawzeAAABd5bk........CQBPcCMRrTC5t55shATUJv]
```
   Basic usage of script:
   
    python3 linkedin_email_scraper.py -k "Microsoft" -c AQEDAR1hbLMFawzeAAABd5bk........CQBPcCMRrTC5t55shATUJv
    
   Hardcoded li_at cookie [line 71] in script:
   
    python3 linkedin_email_scraper.py -k "Microsoft"
    
   Specify less pages to scrape:
   
    python3 linkedin_email_scraper.py -k "Microsoft" -l 50

   Example Output of linkedin_email_scraper.py:
   
    $ python3 linkedin_email_scraper.py -k "microsoft" -l 5
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
    [+] Saved to output.txt. Format your own emails n3wb.
    
   Example Output of output.txt:
   
    Jhilakshi Sharma
    Dan Taylor
    Manuel Berrueta
    Gustavo de Camargo
    Will Pearce
    Andrew Wilson
    Matt Burrough
    Mark Gabel
    Teuta H Hyseni
    Scott Guthrie
    Saurabh Swaroop
    Mark Russinovich
    John Lambert
    Neel Gajjar
    Bhakta Pradhan
    Heike Ritter
    Less Lincoln

  Format output.txt to emails:
  
    $ cat output.txt | awk -F " " '{print $1 "." $2 "@microsoft.com"}'
    Jhilakshi.Sharma@microsoft.com
    Dan.Taylor@microsoft.com
    Manuel.Berrueta@microsoft.com
    Gustavo.de@microsoft.com
    Will.Pearce@microsoft.com
    Andrew.Wilson@microsoft.com
    Matt.Burrough@microsoft.com
    Mark.Gabel@microsoft.com
    Teuta.H@microsoft.com
    Scott.Guthrie@microsoft.com
    Saurabh.Swaroop@microsoft.com
    Mark.Russinovich@microsoft.com
    John.Lambert@microsoft.com
    Neel.Gajjar@microsoft.com
    Bhakta.Pradhan@microsoft.com
    Heike.Ritter@microsoft.com
    Less.Lincoln@microsoft.com
    Bret.Arsenault@microsoft.com
    Joey.Victorino@microsoft.com
    Noel.Love@microsoft.com
    Bharat.Shah@microsoft.com
    Justin.Tiplitsky@microsoft.com
    Mitchell.Minkoff@microsoft.com
    Robert.Shearer@microsoft.com
