import boto.route53.record
import boto.ec2.elb
import re
import sys

class DNS:
    '''
    Class for Deleting, Creating, Commiting DNS
    '''
    def __init__(self, recordname, zone, recordtype, awsregion, elbname):
        self.zone = zone
        self.recordtype = recordtype
        self.recordname = recordname
        self.awsregion = awsregion
        self.elbname = elbname
        
        #Create connections to AWS
        try:
            self.conn = boto.route53.connection.Route53Connection()
        except:
            print "Error connecting to AWS Route53"
            sys.exit()
        try:
            zoneinfo = self.conn.get_hosted_zone_by_name(zone)
            self.zoneid = re.sub("/hostedzone/", "", zoneinfo['GetHostedZoneResponse']['HostedZone']['Id'])
        except:
            print "error getting zone_id from elb api"
            sys.exit()
        try:    
            self.elbconn = boto.ec2.elb.connect_to_region(awsregion)
        except:
            print "Error connecting to AWS ELB"
            sys.exit()
    
        #Create recordset list
        self.recordset = boto.route53.record.ResourceRecordSets(self.conn, hosted_zone_id=self.zoneid)        

    def getelbinfo(self, awsregion, elbname):
        
        #### Get current elb info
        currentelb = self.elbconn.get_all_load_balancers(load_balancer_names=elbname)
        for e in currentelb:
            self.elb_zone_id = e.canonical_hosted_zone_name_id  
            self.elbendpoint = e.canonical_hosted_zone_name
        return self.elbendpoint

    def deleterecord(self, recordname, zone, recordtype, elbendpoint, ttl="30"):
        try:
            deleterecord = self.recordset.add_change("DELETE", recordname, recordtype, ttl, identifier=self.awsregion, region=self.awsregion)
            deleterecord.set_alias(self.elb_zone_id, alias_dns_name=elbendpoint)
            print "record %s deleted from changelist" % recordname 
        except:
            print "Error finding record to delete"
            sys.exit()
            
    def createrecord(self, recordname, zone, recordtype, elbendpoint, ttl="30"):
        try:
            updaterecord = self.recordset.add_change("CREATE", recordname, recordtype, ttl, identifier=self.awsregion, region=self.awsregion)
            updaterecord.set_alias(self.elb_zone_id, alias_dns_name=elbendpoint)
            print "record %s added to changelist" % recordname
        except:
            print "Error creating record"
            sys.exit()
            
    def commitrecord(self):
        try:
            self.recordset.commit()
            print "record changelist commited"
        except:
            print "Error commiting record"
            sys.exit()
