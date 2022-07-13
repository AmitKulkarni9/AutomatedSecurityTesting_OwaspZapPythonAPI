#!/bin/bash

#Go to OWASP/Zed Attack Proxy directory 
cd ZedAttackProxy
./zap.sh -daemon -port 8090 -host localhost -config api.apikey = 'APIKEY' & 
echo Let ZAP daemon mode start up... 
sleep 20
##Go to nightwatch directory and start regression test-suites
cd /c/nightwatch
nightwatch
##Go to python directory and run ZAP Scan and Report
cd /c/Python27/Scripts
python ./zap_spider_scan_report.py
