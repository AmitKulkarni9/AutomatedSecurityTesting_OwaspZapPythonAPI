import time
from pprint import pprint
from zapv2 import ZAPv2

target = 'http://localhost:8080' #target url for scan

zap = ZAPv2(proxies={'http':'http://localhost:8090','https':'http://localhost:8090'})  

apikey = 'q3bb8vid3divcqe81g4f041f7p'
print 'Accessing target %s' % target
zap.urlopen(target)

print 'Traditional Spidering target %s' % target
zap.spider.scan(target)
time.sleep(5)
while (int(zap.spider.status()) < 100):
    time.sleep(5)
    print ('Spider progress %: ' + zap.spider.status())
    time.sleep(5)
print ('Spider completed')

print 'Scanning target %s' % target
zap.ascan.scan(target)
time.sleep(5)
while (int(zap.ascan.status()) < 100):
    time.sleep(5)
    print ('Ascan progress %: ' + zap.ascan.status())
    time.sleep(5)
print ('Ascan completed')

#Report the results
print 'Hosts: ' + ', '.join(zap.core.hosts)
print 'Alerts: '
pprint (zap.core.alerts()) #prints all alerts. can be commented
# HTML Report
with open ('report.html', 'w') as f:f.write(zap.core.htmlreport(apikey = 'q3bb8vid3divcqe81g4f041f7p'))
# XML Report
with open ('report.xml', 'w') as f:f.write(zap.core.xmlreport(apikey = 'q3bb8vid3divcqe81g4f041f7p'))

zap.core.shutdown()