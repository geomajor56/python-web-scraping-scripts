import re
import urllib, urllib2

thisEmployer = re.compile('<a href="(.*)" target')
multiPages = re.compile('Displaying Page <strong>1</strong> of (\d+)')
url_a = "http://lmi2.detma.org/lmi/employer_list.asp?gSTFIPS=25&gCountyCode="
url_b = "&naicsHint="
url_c = "&codeType=10&Command=Goto&Param="
goto = '1'
town_code = ["000031"]
naics_code_four = []
naics = open('data/naics07.txt','r')

a = naics.readlines()
for line in a:
    try:
        theseParts = line.split("\t")
        naics_code = (theseParts[1])
        if len(naics_code)==4:
            naics_code_four.append(naics_code)
    except:
        continue


for thisTown in town_code:
    for thisNaics in naics_code_four:
        urlArray = url_a + thisTown + url_b + thisNaics + url_c+goto
        try:
            thisPage = urllib.request.urlopen(urlArray).read().decode("utf-8")
        except:
            continue
        try:
            num = multiPages.search(thisPage)
            numOfPages = int(num.group(1))
        except:
            continue
        if numOfPages >1:
            gotoList = list(range(2,numOfPages+1))
            for nextNum in gotoList:
                nextUrl = url_a + thisTown + url_b + thisNaics + url_c+str(nextNum)
                print(nextUrl)
