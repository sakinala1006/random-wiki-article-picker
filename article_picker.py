#author sai srinija sakinala

import random
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup
		
def bs(url):
	response = requests.get(url)
	if response.status_code == 200:
		return BeautifulSoup(response.text, 'html.parser')
	return 0

def output_text(page_offset, article_offset):
	url = "https://en.wikipedia.org/w/index.php?title=Category:All_Wikipedia_articles_written_in_American_English&pageuntil=7th+United+States+Congress#mw-pages"
	print("Picking an article")

	for i in tqdm(range(0, page_offset)):
		
		soup = bs(url)
		l = soup.find("div",{"id":"mw-pages"})
		url = "https://en.wikipedia.org"+l.find_all('a')[1]['href']

	soup = bs(url)
	l = soup.find("div",{"id":"mw-pages"})


	article = l.find_all('a')[article_offset].get_text()
	article_link = "https://en.wikipedia.org" + l.find_all('a')[article_offset-1]['href']
	article_name = l.find_all('a')[article_offset-1].text
	print("Article picked is: "+ article_name)
	dec = raw_input("Do you wanna read this article? Press N to pick another article. If you want to read this article, press any other key: ")
	if dec == 'N' or dec=='n':
		print("Picking another article!")
		main()

	soup = bs(article_link)
	text = ''
	l = soup.find("div",{"class":"mw-parser-output"})
	for i in l.find_all('p'):
		text += i.text
	print(text)
	dec = raw_input("Do you want to read another article? Press N if you want to quit, press any other key otherwise:")
	if dec == 'N' or dec == 'n':
		print("BYE! See you again!")
	else:
		main()


def main():
	#in wikipedia, each page has links to 200 articles. Hence we get page_offset
	#and article_offset to navigate

	number_of_articles = 2000

	random_article = random.randrange(0, 2000)
	
	print(random_article)

	page_offset = random_article/200
	article_offset = random_article%200

	output_text(page_offset, article_offset)
	

if __name__ == "__main__":
	main()