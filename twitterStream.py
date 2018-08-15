# -*- coding: utf-8 -*-
import json
import re
import sys
import time

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
terms.append("the")
terms.append("i")
terms.append("to")
terms.append("a")
terms.append("and")
terms.append("is")
terms.append("in")
terms.append("it")
terms.append("you")
terms.append("of")
terms.append("tinyurl")
terms.append("com")
terms.append("for")
terms.append("on")
terms.append("my")
terms.append("s")
terms.append("that")
terms.append("at")
terms.append("with")
terms.append("me")
terms.append("do")
terms.append("have")
terms.append("just")
terms.append("this")
terms.append("be")
terms.append("n")
terms.append("t")
terms.append("so")
terms.append("are")
terms.append("m")
terms.append("not")
terms.append("was")
terms.append("but")
terms.append("out")
terms.append("up")
terms.append("what")
terms.append("now")
terms.append("new")
terms.append("from")
terms.append("your")
terms.append("like")
terms.append("good")
terms.append("no")
terms.append("get")
terms.append("all")
terms.append("about")
terms.append("we")
terms.append("if")
terms.append("time")
terms.append("as")
terms.append("day")
terms.append("will")
terms.append("one")
terms.append("twitter")
terms.append("how")
terms.append("can")
terms.append("some")
terms.append("an")
terms.append("am")
terms.append("by")
terms.append("going")
terms.append("they")
terms.append("go")
terms.append("or")
terms.append("has")
terms.append("rt")
terms.append("know")
terms.append("today")
terms.append("there")
terms.append("love")
terms.append("more")
terms.append("work")
terms.append("too")
terms.append("got")
terms.append("he")
terms.append("back")
terms.append("think")
terms.append("did")
terms.append("lol")
terms.append("when")
terms.append("see")
terms.append("really")
terms.append("had")
terms.append("great")
terms.append("off")
terms.append("would")
terms.append("need")
terms.append("here")
terms.append("thanks")
terms.append("been")
terms.append("blog")
terms.append("still")
terms.append("people")
terms.append("who")
terms.append("night")
terms.append("ll")
terms.append("want")
terms.append("why")
terms.append("bit")
terms.append("ly")
terms.append("home")
terms.append("re")
terms.append("should")
terms.append("well")
terms.append("oh")
terms.append("much")
terms.append("u")
terms.append("ve")
terms.append("then")
terms.append("right")
terms.append("make")
terms.append("last")
terms.append("over")
terms.append("way")
terms.append("can")
terms.append("t")
terms.append("does")
terms.append("getting")
terms.append("watching")
terms.append("its")
terms.append("only")
terms.append("her")
terms.append("post")
terms.append("his")
terms.append("morning")
terms.append("very")
terms.append("she")
terms.append("them")
terms.append("could")
terms.append("first")
terms.append("than")
terms.append("better")
terms.append("after")
terms.append("tonight")
terms.append("our")
terms.append("again")
terms.append("down")
terms.append("twitpic")
terms.append("com")
terms.append("news")
terms.append("man")
terms.append("im")
terms.append("looking")
terms.append("us")
terms.append("tomorrow")
terms.append("best")
terms.append("into")
terms.append("any")
terms.append("hope")
terms.append("week")
terms.append("nice")
terms.append("show")
terms.append("yes")
terms.append("where")
terms.append("take")
terms.append("check")
terms.append("come")
terms.append("trying")
terms.append("fun")
terms.append("say")
terms.append("working")
terms.append("next")
terms.append("happy")
terms.append("were")
terms.append("even")
terms.append("live")
terms.append("watch")
terms.append("feel")
terms.append("thing")
terms.append("life")
terms.append("little")
terms.append("never")
terms.append("something")
terms.append("bad")
terms.append("free")
terms.append("doing")
terms.append("world")
terms.append("ff")
terms.append("im")
terms.append("video")
terms.append("sure")
terms.append("yeah")
terms.append("bed")
terms.append("let")
terms.append("use")
terms.append("their")
terms.append("look")
terms.append("being")
terms.append("long")
terms.append("done")
terms.append("sleep")
terms.append("before")
terms.append("year")
terms.append("find")
terms.append("awesome")
terms.append("big")
terms.append("un")
terms.append("things")
terms.append("ok")
terms.append("another")
terms.append("d")
terms.append("him")
terms.append("cool")
terms.append("old")
terms.append("ever")
terms.append("help")
terms.append("anyone")
terms.append("made")
terms.append("ready")
terms.append("days")
terms.append("die")
terms.append("other")
terms.append("read")
terms.append("because")
terms.append("two")
terms.append("playing")
terms.append("though")
terms.append("is")
terms.append("gd")
terms.append("house")
terms.append("always")
terms.append("also")
terms.append("listening")
terms.append("maybe")
terms.append("please")
terms.append("wow")
terms.append("haha")
terms.append("having")
terms.append("thank")
terms.append("pretty")
terms.append("game")
terms.append("someone")
terms.append("school")
terms.append("those")
terms.append("snow")
terms.append("twurl")
terms.append("nl")
terms.append("gonna")
terms.append("hey")
terms.append("many")
terms.append("start")
terms.append("wait")
terms.append("while")
terms.append("google")
terms.append("finally")
terms.append("everyone")
terms.append("para")
terms.append("try")
terms.append("god")
terms.append("weekend")
terms.append("most")
terms.append("iphone")
terms.append("stuff")
terms.append("around")
terms.append("music")
terms.append("looks")
terms.append("may")
terms.append("thought")
terms.append("keep")
terms.append("yet")
terms.append("reading")
terms.append("must")
terms.append("which")
terms.append("same")
terms.append("real")
terms.append("follow")
terms.append("bit")
terms.append("hours")
terms.append("might")
terms.append("actually")
terms.append("online")
terms.append("job")
terms.append("friends")
terms.append("said")
terms.append("obama")
terms.append("coffee")
terms.append("hate")
terms.append("hard")
terms.append("soon")
terms.append("tweet")
terms.append("por")
terms.append("making")
terms.append("wish")
terms.append("call")
terms.append("movie")
terms.append("tell")
terms.append("thinking")
terms.append("via")
terms.append("site")
terms.append("facebook")
terms.append("few")
terms.append("found")
terms.append("these")
terms.append("tv")
terms.append("sorry")
terms.append("through")
terms.append("already")
terms.append("lot")
terms.append("makes")
terms.append("give")
terms.append("put")
'''
terms.append("waiting")
terms.append("stop")
terms.append("play")
terms.append("says")
terms.append("away")
terms.append("coming")
terms.append("early")
terms.append("dinner")
terms.append("phone")
terms.append("cold")
terms.append("using")
terms.append("times")
terms.append("book")
terms.append("kids")
terms.append("went")
terms.append("nothing")
terms.append("every")
terms.append("years")
terms.append("top")
terms.append("office")
terms.append("friend")
terms.append("talk")
terms.append("feeling")
terms.append("hour")
terms.append("head")
terms.append("web")
terms.append("food")
terms.append("amazing")
terms.append("car")
terms.append("lost")
terms.append("end")
terms.append("girl")
terms.append("since")
terms.append("guess")
terms.append("lunch")
terms.append("hot")
terms.append("sounds")
terms.append("b")
terms.append("funny")
terms.append("idea")
terms.append("glad")
terms.append("saw")
terms.append("hear")
terms.append("mean")
terms.append("name")
terms.append("damn")
terms.append("myself")
terms.append("guy")
terms.append("song")
terms.append("yay")
terms.append("least")
terms.append("business")
terms.append("run")
terms.append("place")
terms.append("friday")
terms.append("buy")
terms.append("enough")
terms.append("anything")
terms.append("late")
terms.append("photo")
terms.append("party")
terms.append("link")
terms.append("interesting")
terms.append("used")
terms.append("shit")
terms.append("tired")
terms.append("internet")
terms.append("following")
terms.append("left")
terms.append("guys")
terms.append("money")
terms.append("far")
terms.append("own")
terms.append("seems")
terms.append("media")
terms.append("baby")
terms.append("class")
terms.append("x")
terms.append("social")
terms.append("seen")
terms.append("miss")
terms.append("forward")
terms.append("part")
terms.append("until")
terms.append("open")
terms.append("win")
terms.append("hi")
terms.append("almost")
terms.append("dont")
terms.append("n")
terms.append("windows")
terms.append("needs")
terms.append("re")
terms.append("super")
terms.append("finished")
terms.append("crazy")
terms.append("update")
terms.append("email")
terms.append("probably")
terms.append("welcome")
terms.append("else")
terms.append("full")
terms.append("eat")
terms.append("city")
terms.append("everything")
terms.append("mind")
terms.append("believe")
terms.append("taking")
terms.append("test")
terms.append("family")
terms.append("break")
terms.append("birthday")
terms.append("started")
terms.append("minutes")
terms.append("weather")
terms.append("later")
terms.append("set")
terms.append("room")
terms.append("such")
terms.append("without")
terms.append("sunday")
terms.append("high")
terms.append("change")
terms.append("tweets")
terms.append("omg")
terms.append("black")
terms.append("meeting")
terms.append("kind")
terms.append("list")
terms.append("page")
terms.append("talking")
terms.append("fuck")
terms.append("wondering")
terms.append("sick")
terms.append("story")
terms.append("word")
terms.append("eating")
terms.append("sweet")
terms.append("both")
terms.append("remember")
terms.append("quite")
terms.append("red")
terms.append("excited")
terms.append("website")
terms.append("pm")
terms.append("rock")
terms.append("article")
terms.append("wrong")
terms.append("gotta")
terms.append("luck")
terms.append("wants")
terms.append("heard")
terms.append("radio")
terms.append("updated")
terms.append("hit")
terms.append("gets")
terms.append("totally")
terms.append("yesterday")
terms.append("won")
terms.append("t")
terms.append("once")
terms.append("hell")
terms.append("true")
terms.append("mac")
terms.append("called")
terms.append("dog")
terms.append("writing")
terms.append("wonder")
terms.append("stay")
terms.append("followers")
terms.append("took")
terms.append("mom")
terms.append("sun")
terms.append("half")
terms.append("app")
terms.append("monday")
terms.append("beautiful")
terms.append("computer")
terms.append("send")
terms.append("whole")
'''







'''
to write to the output file efficiently, I have 1024 byte chunks that fill up as tweets come in.
As soon as the current chunk is full, it writes to file and a new chunk begins.
Once 10240 chunks have been written to file, a new filename is chosen, that way the files will all be about 10mb each.
'''

# 1KB*1000 = 1MB
# 1KB*10000 = 10MB
maxChunks = int(sys.argv[2])#10240/4 #maximum number of chunks to be written to each file.
maxChunkSize = int(sys.argv[1])#1024*4 #maximum size of each chunk. these are sized at 10240 and 1024 because 10240*1024bytes = 10mb.
buffer = ""#this is the current chunk.
chunkCount = 0#number of chunks written to current file so far.
fileCount = 220#number of files that have been written so far.
fileName = "tweets"+str(fileCount)+".txt"#name of the current file being written to.



def startStream():
	try:
		twitterStream.filter( track=terms)#filter the stream according to language and our search terms
	except Exception as e:
		print >> sys.stderr, "ERR2:", str(e)
		startStream()
	

def __unicode__(self):
   return unicode(self.some_field) or u''

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
			if "text" in tweet.keys():

				meta = []

				'''
				if tweet["created_at"]:
					meta.append(tweet["created_at"])
				else:
					meta.append("_")


				if tweet["timestamp_ms"]:
					meta.append(tweet["timestamp_ms"])
				else:
					meta.append("_")
				'''
				meta.append("_")
				meta.append(str(int(round(time.time()*1000))))


				if "coordinates" in tweet.keys():
					meta.append(tweet["coordinates"])
				else:
					meta.append("_")

				
				if "user" in tweet.keys():
					tweet["user"]["name"]
				else:
					meta.append("_")
				
				if "place" in tweet.keys():
					place = tweet["place"]
					if not place == None:
						fullName = place["full_name"]
						if not fullName == None:
							meta.append(fullName)
						else:
							meta.append("_")
					else:
						meta.append("_")
				else:
					meta.append("_")
				

				
				tweetText = tweet["text"].replace('\n', '').replace('\r', '')#this first grabs the text part of the tweet then removes the new lines and carriage returns. that way the tweet is only one line.

				#For extracting urls later
				#tweetText = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', "URL", tweetText)
				

			
				if  len(buffer)<maxChunkSize:#if the current chunk is not full yet
					buffer += "\n"#add a new line
					buffer+=tweetText#add the new tweet in lowercase.
					for m in meta:
						buffer += "\t"
						if m==None:
							buffer += "_"
						else:
								buffer += m

				else:#if the current chunk is full
					print "writing to " + fileName, str(chunkCount)+"/"+str(maxChunks)
					outputFile = open(fileName, 'a')
					outputFile.write(buffer)
					outputFile.close()#write it to the current file
					
					chunkCount += 1#increment the chunk counter
					buffer = "\n"#add a new line
					buffer+=tweetText#add the new tweet in lowercase.
					for m in meta:
						buffer += "\t"
						if not m==None:
							buffer += m
						else:
							buffer += "_"

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
startStream()

