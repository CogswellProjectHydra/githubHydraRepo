"""Miscellaneous pieces of useful code."""
import ConfigParser
import os

def myHostName( ):
    "this computer's host name in the RenderHost table"
    # open config file
    config = ConfigParser.RawConfigParser ()
    config.read ("C:/Hydra/hydraSettings.cfg")
    
    domain = config.get (section="network", option="dnsDomainExtension")
    
    return os.getenv( 'COMPUTERNAME' ) + domain

def flanged (name):
    return name.startswith ('__') and name.endswith ('__')

def nonFlanged (name):
    return not flanged (name)
