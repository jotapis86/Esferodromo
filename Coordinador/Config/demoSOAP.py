from pysimplesoap.client import SoapClient

# Ejemplo

client = SoapClient(wsdl="http://www.webservicex.net/CurrencyConvertor.asmx?WSDL",trace=False)
response = client.ConversionRate(FromCurrency="USD",ToCurrency="COP")
print response
result = response['ConversionRateResult']
print result


# Esfero
client = SoapClient(wsdl="http://hsam.co:8080/MegaManager/services/esfero?wsdl",trace=False, soap_server="oracle")
response = client.getMaquinas()
#print response
result = response['out']
print result


# otra opcion

#client = SoapClient(wsdl="http://hsam.co:8080/MegaManager/services/esfero?wsdl", ns="web", trace=False, soap_server="oracle")
#result = client.getMaquinas()
#print result


# parsing XML

import urllib2
from xml.dom.minidom import parseString
dom = parseString(result)

lista = dom.getElementsByTagName("registro")
print "lista = ", lista

for r in lista:
    print r.getElementsByTagName('id')
    

#print "xmlTag 0 :"
#xmlTag = dom.getElementsByTagName('registro')[0].toxml()
#print xmlTag

#xmlData=xmlTag.replace('<id>','').replace('</id>','')
#print xmlData


import urllib2
from xml.etree import ElementTree

print "***"
print "///////////////////+++++++"
print "***"
xml = ElementTree.fromstring(result)
registros = xml.findall(".//registro")
for r in registros:
    print r.findtext(".//id")
