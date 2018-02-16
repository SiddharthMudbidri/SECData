
import urllib2
import zipfile


url = 'https://www.sec.gov/files/dera/data/financial-statement-data-sets/2017q4.zip'  #URL to download the code from


print "downloading from SEC website "
f = urllib2.urlopen(url)
data = f.read()
with open("SECdata.zip", "wb") as code:
    code.write(data)
SECfiles = zipfile.ZipFile('SECdata.zip')  #saving as SECdata.zip
SECfiles.extractall()   #Extracting zip file contents

filename = "sub.txt"
subfile = open(filename, 'r')
result = [line.split('\t') for line in subfile.readlines()] #Reading the sub.txt file and passing into the Result using the tab delimiter
#print result

company = "AMERICAN AIRLINES GROUP INC."  #Company to search for to find net revenue
for sublist in result:
    for i in sublist:
        if i == company:    #to find matching string "American Airlines"
            adshkey = sublist[0]  #store adsh key to use in the next section of code
            print sublist
            
            
filename = "num.txt"
numfile = open(filename, 'r')
numfileresult = [line.split('\t') for line in numfile.readlines()]  #Reading num file and passing it into numfileresult

netsalesrevenue = "NetIncomeLoss" 
netsalesrevenue1 = "NetIncomeProfit"

for sublist in numfileresult:
    for i in sublist:
        if i == adshkey:    #searching for American Airlines adsh key
            if sublist[1] == netsalesrevenue or sublist[1] == netsalesrevenue1: #searching for Netincome in the array of lists
                print "Net income for American Airlines as of date  "+ sublist[4][0:4]+"-"+ sublist[4][4:6]+"-"+sublist[4][6:8]+" is "+sublist[1][9:len(sublist[1])] +" USD", sublist[7]
                

