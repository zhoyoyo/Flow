from bs4 import BeautifulSoup
import urllib2
url = 'http://www.iie.org/Services/Project-Atlas/Australia/International-Students-In-Australia'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())

print(soup.prettify())

soup.find_all('div',{'class','tabContent'}).contents
# universities = soup.findAll('a',{'class','institution'})

# for eachuniversity in universities:
# 	print eachuniversity['href']+','+eachuniversity.string