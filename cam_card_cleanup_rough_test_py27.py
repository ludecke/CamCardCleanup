#!/usr/bin/env python
import os
import re
import inspect

splitline = 0

def lineno():
    #Returns the current line number in our program
    return inspect.currentframe().f_back.f_lineno

result = []

#def inplace_change(filename, old_string, new_string):

#create an object of class "Businesscard" named after the person's full name
#find the string between the first two " in a line and use that as the object's name
#string1 = line()

#for filename in os.listdir(os.getcwd()+"/camcard_export"):
with open("camcard_export/contacts.csv") as f:
    for line in f:
        #Concatenate lines that were split with /n
        if line.startswith('Gesch'):
        	#Return line number and set it to line number of preceding line
          splitline = lineno()
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
        print splitline
            #if "\t" in line:
                #end_position = line.find('\t')
                #print str(line[1:(end_position-2)])
                #result.append(line)
                #print end_position-2
                #print str(line[1:(end_position-2)])


#print result