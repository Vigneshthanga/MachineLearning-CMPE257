import json
import requests
import csv

class AirQualityDC:
	def getAQ(self):
		URL = "https://api.openaq.org/v1/measurements"
  
# sending get request and saving the response as response object 
		PARAMS = {'city':'Boston-Cambridge-Quincy', 'limit':'10000' , 'date_from':'2019-01-01', 'format':'csv'}
		#r = requests.get(url = URL, params = PARAMS) 
		download = requests.get(url = URL, params=PARAMS)
		decoded_content = download.content.decode('utf-8')
		cr = csv.reader(decoded_content.splitlines(), delimiter=',')
		my_list = list(cr)
		with open('AQ_Boston_Cam-Quincy.csv', 'w') as f:
			for row in my_list:
				f.write(str(row))
				f.write('\n')
				print(row)
# extracting data in json format 
		#print(r)
		#data = r.json()
		#print(type(r))
		
		#r = json.dumps(data)
		#loaded_r = json.loads(r)
		#print(loaded_r)
		#with open('data.json', 'w') as outfile:
		#	json.dump(data, outfile)
		
		#with open('test.csv', 'w') as f:
		#	for key in data.keys():
		#		f.write("%s,%s\n"%(key,data[key]))
		#
collectObj = AirQualityDC()
collectObj.getAQ()