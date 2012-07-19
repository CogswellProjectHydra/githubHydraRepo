"""Miscellaneous pieces of useful code."""

import os

def myHostName( ):
    "this computer's host name in the RenderHost table"

    return os.getenv( 'COMPUTERNAME' ) + '.cpc.local'

