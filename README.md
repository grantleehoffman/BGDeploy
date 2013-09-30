BGDeploy
========


Install
<<<<<<< HEAD
-------
Setup.py package installation

	python setup.py install


Parameters
----------
=======
=======
python setup.py install


Parameters
==========
>>>>>>> b3005c7a4a3efa132cb3440ef15c67739ee26f0d
Automated Blue Green Route53 Cutover CLI

usage: bgswitch [-h] [-v] [-c CURRENTELBNAME] [-e NEWELBNAME] [-z DNSZONE]
                [-n RECORDNAME] [-t RECORDTYPE] [-r REGION]

<<<<<<< HEAD
	optional arguments:
	  -h, --help            show this help message and exit
	  -v, --version         show program's version number and exit
	  -c CURRENTELBNAME, --currentelb CURRENTELBNAME
	                        current elb name (default: None)
	  -e NEWELBNAME, --newelb NEWELBNAME
	                        elb name to add to record alias (default: None)
	  -z DNSZONE, --zone DNSZONE
	                        Route53 hosted domain zone (default: None)
	  -n RECORDNAME, --recordname RECORDNAME
	                        record name to update (default: None)
	  -t RECORDTYPE, --type RECORDTYPE
	                        record typ (default: A)
	  -r REGION, --region REGION
	                        AWS region (default: us-east-1)
=======
Blue Green deployment automation through Route53 updates

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -c CURRENTELBNAME, --currentelb CURRENTELBNAME
                        current elb name (default: None)
  -e NEWELBNAME, --newelb NEWELBNAME
                        elb name to add to record alias (default: None)
  -z DNSZONE, --zone DNSZONE
                        Route53 hosted domain zone (default: None)
  -n RECORDNAME, --recordname RECORDNAME
                        record name to update (default: None)
  -t RECORDTYPE, --type RECORDTYPE
                        record typ (default: A)
  -r REGION, --region REGION
                        AWS region (default: us-east-1)
>>>>>>> b3005c7a4a3efa132cb3440ef15c67739ee26f0d


Example
=======
<<<<<<< HEAD
Switch the A record alias of A_record.domain.com from foo-elb endpoint address to bar-elb endpoint address.

	bgswitch -r us-west-1 -z domain.com -n Arecord.domain.com -e foo-elb -t A -c bar-elb

=======
bgswitch -r us-west-1 -z domain.com -n Arecord.domain.com -e foo-elb -t A -c bar-elb

Switches A record alias of Arecord.domain.com from foo-elb endpoint address to bar-elb endpoint address.
>>>>>>> b3005c7a4a3efa132cb3440ef15c67739ee26f0d
