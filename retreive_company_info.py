__author__ = 'michael'
from bs4 import BeautifulSoup
import urllib, urllib2, re, collections, time
completeList = open('data/complete_employers.txt','w+')
employerList = open('data/test_capecod_employers.txt', 'r').readlines()
current_line = []
a=[]
myDictionary={
    'Company Name'         : '',
    'Street Address'       : '',
    ", '', "               : '',
    '\xc2\xa0'             : '',
    '\r\n\t\t'             : '',
    'Contact Name'         : '',
    'Phone #'              : '',
    '\r\n\t\t\r\n\t\t'     : '',
    'Employee Size Range ' : '',
    '\n\n'                 : '',
    'Employer information is provided by Infogroup&reg, Omaha, NE, 800/555-5211. Copyright&copy 2011 All Rights Reserved.\n' : '',
    }

def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(match):
        return myDictionary[match.group(0)]

    return rx.sub(one_xlat,thisString)

for line in employerList:
    time.sleep(3)
    thisLine = line.split("\t")
    thisUrl =  thisLine[0]
    response = urllib.urlopen(thisUrl)
    data = response.read()
    soup = BeautifulSoup(data)
    for link in soup.find_all('td'):
        thisString =(link.get_text()).encode("utf-8", errors="ignore")
        thisCompany = multiple_replace(thisString, myDictionary)
        thisLine.append(str(thisCompany.strip()))
        testLine = str(thisCompany).strip()
        #print testLine.split(", '',")
    ifthisLine
    completeList.write(str(thisLine)+"\n")
        #print len(thisCompany.strip())