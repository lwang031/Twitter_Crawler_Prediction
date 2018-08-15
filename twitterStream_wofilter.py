# -*- coding: utf-8 -*-
import json
import re
import sys

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

reload(sys)
sys.setdefaultencoding('utf-8')#this is for dealing with weird characters like emoticons

#consumer key, consumer secret, access token, access secret. These are given when you register a new app with twitter.
ckey="2mrZ03hb8Gkj7B4QELnPHG8dk"
csecret="iCIcdpaaru2USDnUZNj4pVeuqWFCzkrsEKZqNo7Es1vt1J9BWi"
atoken="3060718058-JKMeKV3vsPMxRi0FJ5I8j0Ijudv9tuw9XMwNi9v"
asecret="rOMFdpCGnDKjErrKogzDfEQ86BWB7QF5GPE5QAhWZpOWf"


#these will be the terms used in the stream filter. Essentially the same as search terms on twitter.com. You have to have at least one search term.
terms = []
terms.append('a')
terms.append('i')
terms.append('the')
terms.append('it')
terms.append('is')#I used simple english words so that we can essentially get all english tweets.


'''
to write to the output file efficiently, I have 1024 byte chunks that fill up as tweets come in.
As soon as the current chunk is full, it writes to file and a new chunk begins.
Once 10240 chunks have been written to file, a new filename is chosen, that way the files will all be about 10mb each.
'''
maxChunks = 10240 #maximum number of chunks to be written to each file.
maxChunkSize = 1024 #maximum size of each chunk. these are sized at 10240 and 1024 because 10240*1024bytes = 10mb.
buffer = ""#this is the current chunk.
chunkCount = 0#number of chunks written to current file so far.
fileCount = 0#number of files that have been written so far.
fileName = "tweets"+str(fileCount)+".txt"#name of the current file being written to.

class listener(StreamListener):#this is a class that contains functions for dealing with the incoming tweets.

	def on_data(self, data):#this function runs everytime a new tweet arrives
		global terms
		global maxChunks
		global maxChunkSize
		global buffer
		global chunkCount
		global fileCount
		global fileName#the global statments just tell the class to use the variables from above.

		try:#this is encapsulated in a try.catch block in order to keep the stream going even if there was an error on one of the tweets.

			tweet = json.loads(data)#the tweets come in json format. this converts the json into a python dictionary.
			tweetText = tweet["text"].replace('\n', '').replace('\r', '')#this first grabs the text part of the tweet then removes the new lines and carriage returns. that way the tweet is only one line.

			#For extracting urls later
			#tweetText = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', "URL", tweetText)
			

		
			if  len(buffer)<maxChunkSize:#if the current chunk is not full yet
				buffer += "\n"#add a new line
				buffer+=tweetText.lower()#add the new tweet in lowercase.
			else:#if the current chunk is full
				print "writing to " + fileName
				outputFile = open(fileName, 'a')
				outputFile.write(buffer)
				outputFile.close()#write it to the current file
				
				chunkCount += 1#increment the chunk counter
				buffer = ""#clear the chunk buffer
				buffer+=tweetText.lower()#put the new tweet in the chunk buffer

				if chunkCount>maxChunks:#if the last chunk was the 1024th chunk
					fileCount+=1#increment the file counter
					fileName = "tweets"+str(fileCount)+".txt"#reset the filename
					chunkCount = 0#reset the number of chunks to zero

			return(True)

		except Exception as e:#if there was an error
			print >> sys.stderr, "ERR:", str(e)#print err to stderr

	def on_error(self, status):#i dont really know what this does but it was in the examlpe to i put it in.
		print status

auth = OAuthHandler(ckey, csecret)#authorize the app with twitter
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())#start the stream with a listener object.
twitterStream.filter(languages=["en"], track=terms)#filter the stream according to language and our search terms