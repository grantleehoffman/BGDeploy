BGDeploy
========


Install
-------
Setup.py package installation

	python setup.py install


Parameters
----------

Automated Blue/Green Route53 Cutover CLI

	usage: bgswitch [-h] [-v] [-e CURRENTELBNAME] [-u UPDATEELBNAME] -z DNSZONE -n
	                RECORDNAME [-t RECORDTYPE] [-r REGION] [-l TTL]
	                [--create-only]

	Arguments:
	  -h, --help            show this help message and exit
	  -v, --version         show program's version number and exit
	  -e CURRENTELBNAME, --elbname CURRENTELBNAME
	                        elb name (default: None)
	  -u UPDATEELBNAME, --elbupdate UPDATEELBNAME
	                        elb name to add to record alias (default: None)
	  -z DNSZONE, --zone DNSZONE
	                        Route53 hosted domain zone (default: None)
	  -n RECORDNAME, --recordname RECORDNAME
	                        record name to update (default: None)
	  -t RECORDTYPE, --type RECORDTYPE
	                        record typ (default: A)
	  -r REGION, --region REGION
	                        AWS region (default: us-east-1)
	  -l TTL, --ttl TTL     time to live number (default: 30)
	  --create-only         Create a new Record entry in the zone (default: False)


Example
-------
Switch the A record alias of Arecord.domain.com from "foo-elb" endpoint address to the updated endpoint address of "bar-elb".

	bgswitch -r us-west-1 -z domain.com -n Arecord.domain.com -e foo-elb -u bar-elb

