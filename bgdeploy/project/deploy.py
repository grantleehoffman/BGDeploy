#!/usr/bin/env python
'''
Created on Sep 24, 2013

@author: Grant Hoffman
@email: grantleehoffman@gmail.com
github: github.com/grantleehoffman

'''
#from project import DNS
from DNS import DNS

class deploy:
    def __init__(self,recordname,recordtype,DNSZone,region,newelbname,currentelbname):
        self. recordname = recordname
        self.recordtype = recordtype
        self.DNSZone = DNSZone
        self.region = region
        self.newelbname = newelbname
        self.currentelbname = currentelbname
        

        #Get ELB info 
        updatelb = DNS(recordname,DNSZone,recordtype,region,currentelbname)
        currentelbendpoint = updatelb.getelbinfo(region,currentelbname)
        newelbendpoint = updatelb.getelbinfo(region,newelbname)
        
        #updatelb = DNS(recordname,DNSZone,recordtype,newelbendpoint,region,newelbname)
        updatelb.deleterecord(recordname, DNSZone, recordtype, currentelbendpoint)
        updatelb.createrecord(recordname, DNSZone, recordtype, newelbendpoint)
        updatelb.commitrecord() 
            


       
        
    