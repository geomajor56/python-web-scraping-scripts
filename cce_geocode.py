from geopy import geocoders
import time
employers = open('c:/test_geocode.txt','r')
#employers = open('c:/CapeCodEmployerst.txt','r')
postfile = open('c:/postgis.txt','w')
g = geocoders.Google('ABQIAAAAtFyUNEQ3n4aHEPSQDzuAhBTZ5gKDkOFqRiuwbsRGj8uW7t8vdBTuQwOFfmJ7l3mIk2WL3yG0HxuM8Q')

town = {
        '31': 'Barnstable', 
        '32': 'Bourne', 
        '33': 'Brewster', 
        '34': 'Chatham', 
        '35': 'Dennis', 
        '36': 'Eastham', 
        '37': 'Falmouth', 
        '38': 'Harwich', 
        '39': 'Mashpee', 
        '40': 'Orleans', 
        '42': 'Provincetown', 
        '43': 'Sandwich', 
        '44': 'Truro', 
        '45': 'Wellfleet', 
        '46': 'Yarmouth' 
        }

thisLine=employers.readline()
googledAddress=""
geoCodeAddress=""
thisTown=""
def geoThis(addr):
        place, (lat, lng) = g.geocode(addr)
        thisAddress=place.split(",")
        print thisAddress
        gAddress = thisAddress[0]
        gTown = thisAddress[1]
        parse_state_zip = thisAddress[2].split(" ")
        gState = parse_state_zip[1]
        gZip = parse_state_zip[2]
        googledAddress = gAddress+"\t"+gTown+"\t"+gState+"\t"+gZip+"\t"+str(lat)+"\t"+str(lng)+"\n"
        postfile.write(googledAddress)
def getTown(townNum):
    (town[(townNum)])
    return thisTown
 
while thisLine:
    time.sleep(5)
    splitLine=thisLine.split("\t")
    empId = splitLine[0]
    empName = splitLine[1]
    naics2 = splitLine[2]
    naics4 = splitLine[3]
    address = splitLine[4]
    townNum = splitLine[5]
    village = splitLine[6]
    if village.strip()=="none":
        getThis=townNum.strip()
        village = getTown(getThis)
    state = splitLine[7]
    zipcode = "0"+splitLine[8]
    geoCodeAddress = address+","+village+","+state+","+zipcode
    geoThis(geoCodeAddress)
          
    thisLine=employers.readline()
    
print " I am done as well as an idiot"
employers.close()
postfile.close()
