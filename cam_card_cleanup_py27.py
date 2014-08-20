import os
import re


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

for filename in os.listdir(os.getcwd()+"/camcard_export"):
	with open("camcard_export/"+filename) as f:
		for line in f:
			#create an object of class "Businesscard" named after the person's full name
			#find the string between the first two " in a line and use that as the object's name
			cardname = initial
			end_position = str.index('\"\t')
			cardname = str(line[1:(end_position-1)])
			germany = Team("Germany")
			if line.contains(":+49"):
				counter=0
				keyword_found = True
			if keyword_found and counter == 1:
				repetitions = int(line[26:30])
			if keyword_found and counter == 2:
				sapline = line.strip()
				if sapline not in result:
					result[sapline]=0
				result[sapline]+=repetitions


			counter+=1

print result
sorted_result = sorted(result.iteritems(), key=lambda sapline: sapline[1], reverse=True)
print sorted_result

with open ("data/output_file.csv", 'w') as f:
	for sapline, count in sorted_result:
		f.write ("{};{}\n".format(sapline, count))

#python 3 auf mac installieren, aufruf mit "python3"
#utf-8 ausgeben




#for string, repetitions in result:

#hausaufgabe: sort dictionary by value
			
#if line.startswith("--"):