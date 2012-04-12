__author__ = 'michael'

import urllib, urllib2, re, collections, time

empUrl = re.compile('<a href="(.*)" target')
nextPage = re.compile('Param.value=\'(\d+)\'')
pages = re.compile('Displaying Page <strong>(\d)</strong> of (\d)</TD>')

c = open('data/capecod_employers.txt', 'w+')
naicsCode = open('data/final_naics.txt', 'r').readlines()
capeCodTowns = ['000031', '000032', '000033', '000034', '000035', '000036', '000037', '000038', '000039', '000040', '000042', '000043', '000044', '000045', '000046', ]

def getNaicsUrl(naics, town):
    thisUrl = ''
    query_args = collections.OrderedDict()
    query_args['gCountyCode'] = town
    query_args['naicsHint'] = naics
    encoded_args = urllib.urlencode(query_args)
    thisUrl = 'http://lmi2.detma.org/lmi/employer_list.asp?' + encoded_args
    openReadUrl(thisUrl, town, naics)


def buildAdditionalPages(thisUrl, currentPage, totalPages,a, b):
    while currentPage <= totalPages:
        query_args = collections.OrderedDict()
        query_args['gSTFIPS'] = '25'
        query_args['codeType'] = 10
        query_args['Command'] = 'Goto'
        query_args['Param'] = currentPage
        encoded_args = urllib.urlencode(query_args)
        anotherUrl = (thisUrl + '&' + encoded_args)
        response = urllib.urlopen(anotherUrl)
        data = response.readlines()
        empBaseUrl = 'http://lmi2.detma.org/lmi/'

        for line in data:
            thisEmployer = empUrl.search(line)
            if thisEmployer:
                employerUrl = empBaseUrl + thisEmployer.group(1)
                print employerUrl
                c.write(employerUrl + "\t" + a + "\t" + b + "\t" + "\n")
        currentPage += 1
        response.close()

def openReadUrl(thisUrl, a, b):
    response = urllib.urlopen(thisUrl)
    data = response.readlines()
    empBaseUrl = 'http://lmi2.detma.org/lmi/'

    for line in data:
        thisEmployer = empUrl.search(line)
        moreThanOne = pages.search(line)
        if thisEmployer:
            employerUrl = empBaseUrl + thisEmployer.group(1)
            print employerUrl
            c.write(employerUrl + "\t" + a + "\t" + b + "\t" + "\n")
           
        if moreThanOne:
            currentPage = int(moreThanOne.group(1)) + 1
            totalPages = int(moreThanOne.group(2))
            buildAdditionalPages(thisUrl, currentPage, totalPages,a, b)
    response.close()

for thisCode in naicsCode:
    print thisCode
    time.sleep(5)
    for thisTown in capeCodTowns:
        print thisTown
        time.sleep(5)
        getNaicsUrl(thisCode.strip(), thisTown)

c.close()

