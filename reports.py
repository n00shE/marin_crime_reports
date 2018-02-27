from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
#import urllib2
#from bs4 import BeautifulSoup
import csv

#Script to automate police listings collection
#Written by Ryan Blanchard

'''
TO-DO
-doc?
-add other departments
'''

firstrun = False

names = []
address = []
orig_booking_date = []
latest_charge_date = []
arrest_date = []
arrest_agency = []
arrest_location = []
jail_id = []
dob = []
occupation = []
sex = []
height = []
weight = []
race = []
hair_color = []
eye_color = []
charges = []
cleaned_charges = []
lines = []
stored_chargeindex = []
perm_chargeindex = []
lineloop = []
charged = []
temprange = []
dont_process = []
sheriff_csv = "sheriff.csv"
rafaelpd_csv = "rafaelpd.csv"
fairfaxpd_csv = "fairfaxpd.csv"
novatopd_csv = "novatopd.csv"
centralmarinpd_csv = "centralmarinpd.csv"
sausalitopd_csv = "sausalitopd.csv"
chp_csv = "chp.csv"
doc_csv = "doc.csv"
millvalleypd_csv = "millvalleypd.csv"
pds = [sheriff_csv, rafaelpd_csv, fairfaxpd_csv, novatopd_csv, centralmarinpd_csv, sausalitopd_csv, chp_csv, doc_csv, millvalleypd_csv]
pd_name = ['Marin County Sheriff Department', 'San Rafael PD', 'Fairfax PD', 'Novato PD', 'Central Marin Police Authority', 'Sausalito PD', 'California Highway Patrol', 'Department of Corrections', 'Mill Valley PD',] 
fields = ['Name', 'Address', 'Original Booking Date', 'Latest Charge Date', 'Arrest Date', 'Arrest Agency', 'Arrest Location', 'Jail ID', 'DOB', 'Occupation', 'Sex', 'Height', 'Weight', 'Race', 'Hair Color', 'Eye Color', 'Charges']

#open webpage and navigate to 48hr listing
driver = webdriver.Firefox()
driver.get("https://apps.marincounty.org/BookingLog/")
elem = driver.find_elements_by_xpath('//*[@id="no-sidebar-main-content"]/div[2]/form/div/div[2]/input[1]')[0]
elem.click()

#number of bookings
#bookings = driver.find_elements_by_xpath('//*[@id="menu-sub"]/p/span[1]/strong')
#bookings_text = [x.text for x in bookings]
#bookings_clean = 
#print(bookings_text) 

#find names
name_elements = driver.find_elements_by_xpath('//*[@id="sec1"]/h2')
names = [x.text for x in name_elements]
#print(names)

#find address
address_elements = driver.find_elements_by_xpath('//*[@id="sec1"]/div[1]/table/tbody/tr[2]/td')
address = [x.text for x in address_elements]
#print(address)

#find original booking date
bookdate_elements = driver.find_elements_by_xpath('//*[@id="sec1"]/div[1]/table/tbody/tr[3]/td')
orig_booking_date = [x.text for x in bookdate_elements]
#print(orig_booking_date)

#find latest charge date
chargedate_elements = driver.find_elements_by_xpath('//*[@id="sec1"]/div[1]/table/tbody/tr[4]/td')
latest_charge_date = [x.text for x in chargedate_elements]
#print(latest_charge_date)

#find arrest date
arrestdate_elements = driver.find_elements_by_xpath('//*[@id="sec1"]/div[1]/table/tbody/tr[5]/td')
arrest_date = [x.text for x in arrestdate_elements]
#print(arrest_date)

#find arrest agency
arrestagency_elements = driver.find_elements_by_xpath('//*[@id="sec1"]/div[1]/table/tbody/tr[6]/td')
arrest_agency = [x.text for x in arrestagency_elements]
for agency in arrest_agency:
	if agency not in pd_name:
		print("Need to add " + agency + " to police departments")
#print(arrest_agency)

#find arrest location
arrestlocation_elements = driver.find_elements_by_xpath('//*[@id="sec1"]/div[1]/table/tbody/tr[7]/td')
arrest_location = [x.text for x in arrestlocation_elements]
#print(arrest_location)

#find jail id
jailid_elements = driver.find_elements_by_xpath('//*[@id="sec1"]/div[1]/table/tbody/tr[8]/td')
jail_id = [x.text for x in jailid_elements]
#print(jail_id)

#find dob
dob_elements = driver.find_elements_by_xpath('//*[@id="sec1"]/div[2]/table/tbody/tr[1]/td')
dob = [x.text for x in dob_elements]
#print(dob)

#find occupation
occupation_elements = driver.find_elements_by_xpath('//*[@id="sec1"]/div[2]/table/tbody/tr[2]/td')
occupation = [x.text for x in occupation_elements]
#print(occupation)

#find sex
sex_elements = driver.find_elements_by_xpath('//*[@id="sec1"]/div[2]/table/tbody/tr[3]/td')
sex = [x.text for x in sex_elements]
#print(sex)

#find height
height_elements = driver.find_elements_by_xpath('//*[@id="sec1"]/div[2]/table/tbody/tr[4]/td')
height = [x.text for x in height_elements]
#print(height)

#find weight
weight_elements = driver.find_elements_by_xpath('//*[@id="sec1"]/div[2]/table/tbody/tr[5]/td')
weight = [x.text for x in weight_elements]
#print(weight)

#find race
race_elements = driver.find_elements_by_xpath('//*[@id="sec1"]/div[2]/table/tbody/tr[6]/td')
race = [x.text for x in race_elements]
#print(race)

#find hair_color
haircolor_elements = driver.find_elements_by_xpath('//*[@id="sec1"]/div[2]/table/tbody/tr[7]/td')
hair_color = [x.text for x in haircolor_elements]
#print(hair_color)

#find eye_color
eyecolor_elements = driver.find_elements_by_xpath('//*[@id="sec1"]/div[2]/table/tbody/tr[8]/td')
eye_color = [x.text for x in eyecolor_elements]
#print(eye_color)

#find charges
#charges_elements = driver.find_elements_by_xpath('//*[@id="sec2"]/table')
charges_elements = driver.find_elements(By.TAG_NAME, "tr") 
charges = [x.text for x in charges_elements]
#print(charges)

for chargeindex, item in enumerate(charges):
	#print(chargeindex, item)
	if 'Release Date' in item:
		stored_chargeindex.append(chargeindex + 1)
		i = 1
		try:
			while not 'Name' in charges[chargeindex + i]:
				cleaned_charges.append(charges[chargeindex + i])
				#stored_chargeindex.append(chargeindex)
				i = i + 1
		except:
			pass
			#print("This should happen once!!!")
		lines.append(i - 1)
		#perm_chargeindex.append(stored_chargeindex)
#print(stored_chargeindex)
#print lines
for index, line in enumerate(lines):
	try:
		lineloop.append(range(0, lines[index]))
	except:
		pass
#print lineloop

'''
for index, name in enumerate(names):
	perm_chargeindex.append(charges[stored_chargeindex[index] + lineloop[index][0]])
	if lineloop[index][-1] != 0:
		temprange = range(1, lines[index])
		#print temprange
		for i in temprange:
			perm_chargeindex.append(charges[stored_chargeindex[index] + lineloop[index][i]]) 
#print(perm_chargeindex)
'''

#Begin export process
allarrests = [names, address, orig_booking_date, latest_charge_date, arrest_date, arrest_agency, arrest_location, jail_id, dob, occupation, sex, height, weight, race, hair_color, eye_color]
#print(allarrests)

for pdindex, pd in enumerate(pds): #iterate through pd csvs
	for index, name in enumerate(names):
		temprange = range(0, lines[index])
		charged = []
		if not os.path.isfile(pd):
			open(pd, "w")
		with open(pd, "r") as csvfileread:
			reader = csv.reader(csvfileread, delimiter=',')
			for row in reader:
				for info in row:
					if info == latest_charge_date[index]:
						dont_process = name
			csvfileread.close()
			with open(pd, "a") as csvfile:
				writer = csv.DictWriter(csvfile, fieldnames=fields)
				if firstrun:
					writer.writeheader() #run this once
				for i in temprange:
					charged.append(charges[stored_chargeindex[index] + lineloop[index][i]])
				if allarrests[5][index] == pd_name[pdindex]:
					if dont_process != name:
						if any('spouse' in s for s in charged):
							writer.writerow({'Name' : allarrests[0][index],'Address' : allarrests[1][index], 'Original Booking Date' : allarrests[2][index], 'Latest Charge Date' : allarrests[3][index], 'Arrest Date' : allarrests[4][index], 'Arrest Agency' : allarrests[5][index], 'Arrest Location' : allarrests[6][index], 'Jail ID' : allarrests[7][index], 'DOB' : allarrests[8][index], 'Occupation' : allarrests[9][index], 'Sex' : allarrests[10][index], 'Height' : allarrests[11][index], 'Weight' : allarrests[12][index], 'Race' : allarrests[13][index], 'Hair Color' : allarrests[14][index], 'Eye Color' : allarrests[15][index], 'Charges' : charged})
				
driver.close()
csvfile.close()

#STATIC PAGE
#scrape the page
#site = 'https://apps.marincounty.org/BookingLog/Booking/Action'
#page = urllib2.urlopen(site)
#parsed = BeautifulSoup(page, 'html.parser')

#names = parsed.find('h2', attrs={'id': "sec1"})
#print(names)