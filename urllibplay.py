__author__ = 'michael'
from bs4 import BeautifulSoup
import urllib, urllib2, re, collections, time

empUrl = re.compile('<a href="(.*)" target')
nextPage = re.compile('Param.value=\'(\d+)\'')
pages = re.compile('Displaying Page <strong>(\d)</strong> of (\d)</TD>')

c=open('data/test.txt','w+')
naicsCode = open('data/naics07.txt','r').readlines()
capeCodTowns = ['000031','000032' ]

def getNaicsUrl(naics, town):
    thisUrl=''
    query_args = collections.OrderedDict()
    query_args['gCountyCode'] = town
    query_args['naicsHint']= naics
    encoded_args = urllib.urlencode(query_args)
    thisUrl = 'http://lmi2.detma.org/lmi/employer_list.asp?' + encoded_args
    print 'naics url: ',thisUrl,'\n',
    openReadUrl(thisUrl,town,naics)

def openReadUrl(thisUrl, a, b):
    response = urllib.urlopen(thisUrl)
    data = response.readlines()
    empBaseUrl = 'http://lmi2.detma.org/lmi/'

    for line in data:
        thisEmployer = empUrl.search(line)
        moreThanOne = pages.search(line)
        thisPageNum  = nextPage.search(line)

        if thisEmployer:
            employerUrl = empBaseUrl+thisEmployer.group(1)
            #c.write(employerUrl+"\t"+a+"\t"+b+"\t"+"\n")
        if moreThanOne:
            total_pages = moreThanOne(1)
            print total_pages
            page_num = thisPageNum.group(1)
            query_args = collections.OrderedDict()
            query_args['gSTFIPS'] = '25'
            query_args['codeType'] = 10
            query_args['Command']='Goto'
            query_args['Param'] = page_num
            encoded_args = urllib.urlencode(query_args)
            anotherUrl = (thisUrl+ '&' + encoded_args)
            #c.write(anotherUrl+"\t"+a+"\t"+b+"\t"+"\n")
            #print(c)

for thisCode in naicsCode:
    time.sleep(3)
    for thisTown in capeCodTowns:
        time.sleep(3)
        getNaicsUrl(thisCode.strip(), thisTown)

c.close()
