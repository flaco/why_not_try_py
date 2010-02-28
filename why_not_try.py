import urllib
import re
from BeautifulSoup import BeautifulSoup

page = "http://nytimes.com"
html = urllib.urlopen(page).read()
html = re.sub('\n\"\' ,.?!-', '', html)
soup = BeautifulSoup(html)
text = soup.findAll(text=True)
word_list = {}

def visible(element):
	if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
		return False
	elif re.match('<!--.*-->', element):
		return False
	return True

lines = filter(visible, text)
words = []
for l in lines:
  words += [s.lower() for s in l.split()]
for word in words:
	if word in word_list:
		word_list[word] += 1
	else:
		if word.isalpha():
			word_list[word] = 1
word_list = sorted(word_list.items(), key = lambda (v,k) : (k,v))
word_list.reverse()

f = open('popular_word_list.txt', 'w')
f.write("Most common words from " + page + " \n")
for i in word_list:
	f.write(str(i[0]) + " : " + str(i[1]) + " \n")
