""" In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_166940.xml (Sum ends with 56) """

from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#address = input('Enter location: ')
url = 'http://py4e-data.dr-chuck.net/comments_166940.xml'

stringxml = urlopen(url, context=ctx).read()
sum = 0
xmltree = ET.fromstring(stringxml)
counts = xmltree.findall('comments/comment/count')

for count in counts:
    sum += int(count.text)

print(sum)
