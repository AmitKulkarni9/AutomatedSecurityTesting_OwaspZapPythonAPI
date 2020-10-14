# Automated-Security-Testing
#Contains the shell and python scripts. 
#Can be used with any UI Automation tool like Selenium, Protractor etc. and automate Security testing.

#Steps:
1. Start/Enable ZAP so that it can proxy the browser
2. Start UI automated regression tests so that ZAP can proxy all the pages of the application
3. After regression tests is done, run the zap_spider_scan_report.py script which will spider the application pages and then will do the Active and/or Passive scan to generate the security report containing the vulnerabilities and suggestions to fix those vulnerabilities.
