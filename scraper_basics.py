from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
	soup=BeautifulSoup(html_file,'lxml') #parser

#to print
print(soup.prettify())

#to fetch specific data from file, say title
match=soup.title.text
print(match)

#to fetch div paragraphs
match=soup.div.text
print(match)

#to fetch specific div part
match=soup.find('div',class_='footer')
print(match)

article=soup.find('div',class_='article')
print(article)

#to fetch article headline
headline=article.h2.a.text
print(headline)

#to fetch article content
summary=article.p.text
print(summary)

#to fetch all the articles in the file
for article in soup.find_all('div',class_='article'):
	headline=article.h2.a.text
	print(headline)

	summary=article.p.text
	print(summary)
	print()
