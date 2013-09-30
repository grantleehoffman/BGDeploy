#!/usr/bin/env python
'''
Created on Sep 24, 2013

@author: Grant Hoffman
@email: grantleehoffman@gmail.com
github: github.com/grantleehoffman/BGDeploy

'''
import argparse, sys, os, inspect

#Find package paths from arguments script
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], "project")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

# Python2.7 expected:
if sys.version_info[0] != 2 or sys.version_info[1] < 7:
    sys.exit('This program needs Python2.7+')

#Argument parsing for CLI
desc = """Blue Green deployment automation through Route53 updates"""
parser = argparse.ArgumentParser(description=desc, version='1.0', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-c', '--currentelb',
                    help='current elb name',
                    dest='currentelbname',
                    action='store',
                    )
parser.add_argument('-e', '--newelb',
                    help='elb name to add to record alias',
                    dest='newelbname',
                    action='store',
                    )
parser.add_argument('-z', '--zone',
                    help='Route53 hosted domain zone',
                    dest='dnszone',
                    action='store',
                    )
parser.add_argument('-n', '--recordname',
                    help='record name to update',
                    dest='recordname',
                    action='store',
                    )
parser.add_argument('-t', '--type',
                    help='record typ',
                    dest='recordtype',
                    action='store',
                    default='A',
                    )
parser.add_argument('-r', '--region',
                    help='AWS region',
                    dest='region',
                    action='store',
                    default='us-east-1',
                    )

args = parser.parse_args()

recordname = args.recordname    
recordtype = args.recordtype
DNSZone = args.dnszone
region = args.region
newelbname = args.newelbname
currentelbname = args.currentelbname

if len(vars(args)) < 6:
    parser.error("Please specify all options")

if __name__ == '__main__':
    from project.deployment import deployment
    #Create deployment object, and run update on object
    new = deployment(recordname, recordtype, DNSZone, region, newelbname, currentelbname)
    new.update(recordname, recordtype, DNSZone, region, newelbname, currentelbname)
    

    

    
