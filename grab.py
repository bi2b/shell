import requests
from bs4 import BeautifulSoup as bs

s = requests.Session()

def grab(domain, maks, save):
	open(save, 'a+')
	for page in range(1, int(maks) + 1):
		print(f'\nGrabbing Page {page}\n')
		url = f"https://bestwebsiterank.com/domains/{domain}/{page}"
		r = s.get(url)
		soup = bs(r.text, 'html.parser').find('tbody').findAll('tr')
		for i in soup:
			dom = i.a.text.strip()
			with open(save, 'r+') as sip:
				rs = sip.read().splitlines()
				if dom not in rs:
					sip.write(dom + '\n')
					print(f'{dom} >> Saved!')
				else:
					print(f'{dom} >> Already in list!')
				
if __name__ == '__main__':
	domain = input('Domain >> ')
	page = input('Max Page >> ')
	save = input('Save Results To >> ')
	grab(domain, page, save)