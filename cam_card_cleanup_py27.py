#!/usr/bin/env python
import os
import re
import inspect

class Businesscard:

 def __init__(self, name):
    self.name = name
    self.lastname = lastname
    self.firstname = firstname
    self.company = company
    self.jobtitle = jobtitle
    self.email = email
    self.city = city
    self.addressline1 = addressline1
    self.postalcode = postalcode
    self.fedstate = fedstate
    self.website = website
    self.cellphone = cellphone
    self.officephone = officephone

result = []


#def inplace_change(filename, old_string, new_string):

#create an object of class "Businesscard" named after the person's full name
#find the string between the first two " in a line and use that as the object's name
#string1 = line()

#for filename in os.listdir(os.getcwd()+"/camcard_export"):
with open("camcard_export/contacts.csv") as f:
    for line in f:
        if line.startswith("Gesch"):
            print line
        #Concatenate lines that were split with /n
        #if 'Gesch' in line:
            #Return line number and set it to line number of preceding line
            #print num
          #join split line with its second part
          #for line in f:
            #if lineno() == splitline
            #line.rstrip("\n")
            #Perform operations for splitlines
        #Perform operations for non-splitlines
            
            #concatenate two lines
        #line = re.sub('\nGesch', 'Gesch', line)
        #if line.__contains__('\nGesch'):
            #line.replace('\nGesch', ';Gesch')
        #print line
        #print splitline
            #if "\t" in line:
                #end_position = line.find('\t')
                #print str(line[1:(end_position-2)])
                #result.append(line)
                #print end_position-2
                #print str(line[1:(end_position-2)])


#print result