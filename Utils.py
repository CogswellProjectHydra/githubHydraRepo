"""Miscellaneous pieces of useful code."""

import os

def myHostName( ):
    "this computer's host name in the RenderHost table"

    return os.getenv( 'COMPUTERNAME' ) + '.cpc.local'

def flanged (name):
    return name.startswith ('__') and name.endswith ('__')

def nonFlanged (name):
    return not flanged (name)
