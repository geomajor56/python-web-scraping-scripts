__author__ = 'michael'
from bs4 import BeautifulSoup
import re
f = open('data/employer_details.txt','r')
a=[]
soup = BeautifulSoup(f)
myDictionary={
    'Company Name'         : '',
    'Street Address'       : '',
    #'\r\n\t\t'           : '',
    '\xc2\xa0'             : '',
    '\r\n\t\t'             : '',
    'Contact Name'         : '',
    'Phone #'              :'',
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

for link in soup.find_all('td'):
    thisString =(link.get_text()).encode("utf-8", errors="ignore")
    #print thisString
    a.append(multiple_replace(thisString, myDictionary))
print (a)
    #print len((a[3].strip("\t")))




