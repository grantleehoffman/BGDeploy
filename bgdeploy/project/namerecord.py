

from Route53 import Route53

class namerecord:
    def __init__(self, recordname, recordtype, ttl, DNSZone, region, newelbname, currentelbname=None):
        self._recordname = recordname
        self._recordtype = recordtype
        self._ttl = ttl
        self._DNSZone = DNSZone
        self._region = region
        self._newelbname = newelbname
        self._currentelbname = currentelbname
        
    def update(self):
        #instantiate Record changelist
        updaterecord = Route53(self._recordname, self._DNSZone, self._recordtype, self._ttl, self._region, self._currentelbname)
        #get current elb info and add delete record change to list
        currentelbendpoint = updaterecord.getelbinfo(self._currentelbname)
        updaterecord.deleterecord(currentelbendpoint)
        #get new elb info and add create record change to list
        newelbendpoint = updaterecord.getelbinfo(self._newelbname)
        updaterecord.createrecord(newelbendpoint)
        updaterecord.commitrecord() 
            
    def create(self):
        #Get ELB info 
        updaterecord = Route53(self._recordname, self._DNSZone, self._recordtype, self._ttl, self._region, self._newelbname)
        newelbendpoint = updaterecord.getelbinfo(self._newelbname)
        updaterecord.createrecord(newelbendpoint)
        updaterecord.commitrecord() 

       
        
    
