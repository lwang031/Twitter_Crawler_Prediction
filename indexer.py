import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import whoosh.index as index
from whoosh.index import create_in
from whoosh.fields import *
from whoosh import scoring
from whoosh.scoring import BM25F

### --- IMPORTANT --- ###
buildIndex = True #when this is true, documents will be added to the index. when it is false, the pre-built index will be loaded instead, ready to be searched. 

if buildIndex:

	schema = Schema(text=TEXT(stored=True), time=TEXT(stored=True), coords=TEXT(stored=True), user=TEXT(stored=True), place=TEXT(stored=True))
	ix = create_in(".", schema) #uncomment this line if you want to add documents to a previous index. 
	#ix = index.open_dir(".") #uncomment this line if you want to build a brand new index.
	
	for i in range(201,206): #the range of documents to be parsed
		count = 0
		writer = ix.writer()

		### --- IMPORTANT --- ###
		fName = "../Part 1/data/tweets" + str(i) + ".txt" #this path must point to wherever you have the tweet files. So you will need to change "../Part 1/tweets" to somethin else, depending on where you have the tweets stored.
		print "loading " + fName
		f = open(fName, 'rb')
		try:
			reader = csv.reader(f, delimiter="\t")
			
			while True:
				try:
					row = next(reader)
					

					if len(row)>=6:
						if count%100==0:
							print "adding ", str(float(count)/1000)
						d = [unicode(str(row[0]), 'utf-8'), unicode(str(row[1]), 'utf-8'), unicode(str(row[2]), 'utf-8'), unicode(str(row[3]), 'utf-8'), unicode(str(row[5]), 'utf-8')] 
						writer.add_document(text=d[0],time = d[1], coords = d[2], user = d[3], 	place = d[4] )
					elif len(row)>=5:
						if count%100==0:
							print "adding ", str(float(count)/1000)
						d = [unicode(str(row[0]), 'utf-8'), unicode(str(row[1]), 'utf-8'), unicode(str(row[2]), 'utf-8'), unicode(str(row[3]), 'utf-8'), unicode("_", 'utf-8')] 
						writer.add_document(text=d[0],time = d[1], coords = d[2], user = d[3], 	place = d[4] )
				except csv.Error: 
					continue
				except StopIteration:
					break
				count += 1
				if count>10000:#this limits the indexer to the first 1000 tweets of each file. I did this to make the indexer build faster. You can make this larger but the index will take longer to build and will take u more space.
					break
		finally:	
			f.close()


		print "commiting"		
		writer.commit()
		print "done"
else:
	ix = index.open_dir(".")	