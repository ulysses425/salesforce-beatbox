import os
from suds.client import Client

# *** Create this file with USERNAME and PASSWORD:
from sfconfig import USERNAME, PASSWORD

# *** set this to the location of the WSDL file
wsdl = 'file:///Users/davidg/ONENW/davisagli.pysf/davisagli/pysf/salesforce.wsdl'

def main():
    # load service definition
    sfc = Client(wsdl)
    
    # log in
    res = sfc.service.login(USERNAME, PASSWORD)
    
    # use different server for subsequent requests
    sfc.client.wsdl.root.childAtPath('service/port/address').set('location', res.serverUrl)
    
    # add SOAP header with session id to subsequent requests
    session_header = sfc.factory.create('SessionHeader')
    session_header.sessionId = res.sessionId
    sfc.client.soapheaders.append(session_header)

    # create a new contact
    # contact = sfc.factory.create('sf:sObject')
    # contact.type = 'Contact'
    # contact.FirstName = 'Bob'
    # contact.LastName = 'Costanza'
    # res = sfc.service.create(contact)

    import pdb; pdb.set_trace()
