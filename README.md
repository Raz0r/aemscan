[![Build Status](https://travis-ci.org/Raz0r/aemscan.svg?branch=master)](https://travis-ci.org/Raz0r/aemscan)

## aemscan
#### *Adobe Experience Manager Vulnerability Scanner*

https://raz0r.name/releases/adobe-experience-manager-vulnerability-scanner/

### Features

* Default credentials bruteforce
* Info leak via default error page
* WebDav support check (WebDav OSGI XXE CVE-2015-1833)
* Version detection
* Useful paths scanner

### Installation

`$ python setup.py install`

### Usage

`$ aemscan <url>`

### TODO

* CVE-2016-0956 "Apache Sling Framework 2.3.6 Information Disclosure"
* CVE-2018-5006, CVE-2018-12809 "Adobe Experience Manager Server-Side Request Forgery"

### Links
* [Adobe CQ Pentesting Guide](https://resources.infosecinstitute.com/adobe-cq-pentesting-guide-part-1/)
* [Hacking Adobe Experience Manager sites](https://www.slideshare.net/0ang3el/hacking-aem-sites)
* [Adobe Experience Manager Security Check List](https://helpx.adobe.com/experience-manager/6-3/sites/administering/using/security-checklist.html)
