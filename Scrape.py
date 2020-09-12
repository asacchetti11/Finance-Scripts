import requests
import json

def scrape():
	with requests.get('https://www.sec.gov/include/ticker.txt') as req:
		if (req.status_code != 200):
			print('Error retrieving')
		else:
			line_data = req.text.split('\n')
			data_dict = {x.upper():y for (x,y) in [i.split('\t') for i in line_data]}
			with open('tickers.txt', 'w') as file:
				json.dump(data_dict, file)

def main():
	#scrape()
	with open('tickers.txt', 'r') as file:
		data = json.load(file)
		while (True):
			s = input('Give ticker:').upper()
			print(s in data)
			#write code to scan all tickers for country and state, group them by state and maybe city



if __name__ == '__main__':
	main()