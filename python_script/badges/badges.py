# importing element tree
# under the alias of ET
import xml.etree.ElementTree as ET
import snowflake.connector

# Passing the path of the
# xml document to enable the
# parsing process
tree = ET.parse('Badges.xml')
 
# getting the parent tag of
# the xml document
root = tree.getroot()

fl = []

i=0
while i<len(root):
    fl.append(root[i].attrib)
    i=i+1

output = ""
i=0
with open("badged.csv", "a") as o:
    o.write("Id,UserId,Name,Date,Class,TagBased")

while i<len(fl):
    values = fl[i].values()
    print(values)
    output = f"{fl[i]['Id']},{fl[i]['UserId']},{fl[i]['Name']},{fl[i]['Date']},{fl[i]['Class']},{fl[i]['TagBased']}\n"
    i = i+1
    with open("badged.csv", "a") as o:
        o.write(output)
    # o.write('This text will be added to the file')

# print(output)

# Id="1" UserId="5" Name="Student" Date="2010-07-28T19:09:00.243" Class="3" TagBased="False" 