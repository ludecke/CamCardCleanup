#!/usr/bin/env python
import os
import re

result = []

#def inplace_change(filename, old_string, new_string):

#create an object of class "Businesscard" named after the person's full name
#find the string between the first two " in a line and use that as the object's name
#string1 = line()

#for filename in os.listdir(os.getcwd()+"/camcard_export"):
with open("camcard_export/contacts.csv") as f:
    for line in f:
        if line.startswith('Gesch'):
            #concatenate two lines
        line = re.sub('\nGesch', 'Gesch', line)
        #if line.__contains__('\nGesch'):
            #line.replace('\nGesch', ';Gesch')
        print line
            #if "\t" in line:
                #end_position = line.find('\t')
                #print str(line[1:(end_position-2)])
                #result.append(line)
                #print end_position-2
                #print str(line[1:(end_position-2)])


#print result
