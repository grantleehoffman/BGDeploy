BGDeploy
========


Install
-------
__Setup.py package installation__

	python setup.py install

Setup
-----
__IAM Credential Access__
1. Use IAM Instance Based Roles with access to ELB (Read-only) and Route53 (Read/Write)

Or

1. Create an IAM user with access to ELB (Read-only) & Route53(Read/Write)
2. Create a Access Key for the user and add the credentials to either of the following:

* AWS\_SECRET\_ACCESS\_KEY & AWS\_ACCESS\_KEY\_ID environmental variables

```
export AWS_ACCESS_KEY_ID=<your access key>
export AWS_SECRET_ACCESS_KEY=<your secret key>
```

* Boto config file at ~/.boto or /etc/boto.cfg for all system users

```
[Credentials]
aws_access_key_id = <your access key>
aws_secret_access_key = <your secret key>
```

Parameters
----------

__Automated Blue/Green Route53 Cutover CLI__

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

