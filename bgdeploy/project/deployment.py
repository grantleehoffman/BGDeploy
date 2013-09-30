

from DNS import DNS

class deployment:
    def __init__(self, recordname, recordtype, DNSZone, region, newelbname, currentelbname):
        self. recordname = recordname
        self.recordtype = recordtype
        self.DNSZone = DNSZone
        self.region = region
        self.newelbname = newelbname
        self.currentelbname = currentelbname
        
    def update(self, recordname, recordtype, DNSZone, region, newelbname, currentelbname):
        #Get ELB info 
        updaterecord = DNS(recordname, DNSZone, recordtype, region, currentelbname)
        currentelbendpoint = updaterecord.getelbinfo(region, currentelbname)
        newelbendpoint = updaterecord.getelbinfo(region, newelbname)
        #updatelb = DNS(recordname,DNSZone,recordtype,newelbendpoint,region,newelbname)
        updaterecord.deleterecord(recordname, DNSZone, recordtype, currentelbendpoint)
        updaterecord.createrecord(recordname, DNSZone, recordtype, newelbendpoint)
        updaterecord.commitrecord() 
            


       
        
    
