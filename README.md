BGDeploy
========


Install
-------
Setup.py package installation

	python setup.py install


Parameters
----------
Automated Blue Green Route53 Cutover CLI

usage: bgswitch [-h] [-v] [-c CURRENTELBNAME] [-e NEWELBNAME] [-z DNSZONE]
                [-n RECORDNAME] [-t RECORDTYPE] [-r REGION]

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


Example
=======
Switch the A record alias of A_record.domain.com from foo-elb endpoint address to bar-elb endpoint address.

	bgswitch -r us-west-1 -z domain.com -n Arecord.domain.com -e foo-elb -t A -c bar-elb

