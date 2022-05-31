# importing element tree
# under the alias of ET
import xml.etree.ElementTree as ET
import snowflake.connector

# Passing the path of the
# xml document to enable the
# parsing process
tree = ET.parse('posts.xml')
 
# getting the parent tag of
# the xml document
root = tree.getroot()

fl = []

i=0
while i<len(root):
    fl.append(root[i].attrib)
    i=i+1

output = ""
# try:
#     with open("users.csv", "a") as o:
#         o.write("Id,Reputation,CreationDate,DisplayName,LastAccessDate,WebsiteURL,Location,Views,Upvotes,Downvotes,AccountID")
# except:
#     print("error")

i=0
while i<len(fl):
    values = list(fl[i].values())
    keys = list(fl[i].keys())
    print(values)
    j=0
    while j<len(values):
        if keys[j] != "AboutMe":
            output = output + str(values[j]) + ','
        j=j+1
    output += '\n'
    # output = f"{fl[i]['Id']},{fl[i]['UserId']},{fl[i]['Name']},{fl[i]['Date']},{fl[i]['Class']},{fl[i]['TagBased']}\n"
    i = i+1
    try:
        with open("posts.csv", "a") as o:
            o.write(output)
    except:
        print("error")
    # o.write('This text will be added to the file')

# print(output)