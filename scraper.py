from bs4 import BeautifulSoup
import requests
import csv

#fetch source code of a website to scrape from
source=requests.get('http://www.justvish.in/').text

soup=BeautifulSoup(source,'lxml')

csv_file=open('jv_scrape.csv','w')

csv_writer=csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video_link'])

#print(soup.prettify())

for article in soup.find_all('article'):
	#print(article.prettify())

	headline=article.h2.a.text
	print(headline)

	summary=article.find('div',class_='entry-content').p.text
	print(summary)

	try:
		video_source=article.find('iframe',class_='youtube-player')['src']
		print(video_source)

		video_id=video_source.split('/')[4]
		video_id=video_id.split('?')[0]
		print(video_id)

		yt_link=f'https://youtube.com/watch?v={video_id}'
	except Exception as e:
		yt_link=None

	print(yt_link)

	print()

	csv_writer.writerow([headline,summary,yt_link])

csv_file.close()