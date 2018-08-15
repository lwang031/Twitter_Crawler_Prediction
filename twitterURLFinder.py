import re 
import lxml.html
from StringIO import StringIO


for i in range(0,int(sys.argv[1]) + 1):
	fname = "tweets"
	fname += str(i)
	fname += ".txt" 

	with open(fname, 'r') as f:
		content = f.readlines()

	newContent = []

	for line in content:
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)

		l = line

		for url in urls:
			if(len(url)>1):
				
				t = lxml.html.parse(StringIO(url))
				if not t == None:
					title = t.find(".//title")

					if not title == None:
						print url
						titleText = title.text
						print titleText

						l += "\t" + titleText

		newContent.append(l)
	with open(fname, 'w') as f:
		f.writelines(newContent)
