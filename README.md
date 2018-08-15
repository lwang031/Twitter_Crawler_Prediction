# Twitter_Crawler_Prediction

## Phase I. Collect Tweets

### Overview
uses `tweepy` to interact with Twitter's API. Set size of chunk, `chunk size`, and number of chunk needed, `chunk count`. Save tweets into each chunk untill it's full, and save the chunk into a file, `tweets<filecount>.txt`. Python has the module `json` to convert json file to Python dictionary directly. Keep saveing file until it reaches the `chunk count`.
### Limitations
   tweets will be missed during the reinitialization of the stream if twitter connection is interrupted. 
### Instructions on running the crawler:
   1. `./twitterStream.sh<chunk size><chunk count>`
   2. Scans files for urls. If url found, retreives the title of the linked page. Parses through files tweets0.txt - tweets<fileCount>.txt
	`twitterURLFinder.py <fileCount>`
	

## Phase II. 
### Overview
#### Back End
   Implement indexing and searching function with Whoosh library in Python.
#### Front End
   Build web-based interface with Flask library in python. Implement map function with flask-googlemaps library.
### Index Structures
   Implement Okapi BM25 scoring function with Whoosh. 
   Add time factor: `timeFactor = 1/(currentTime - tweetTime)`. Most recent posts have largest value. It's then wegighted to blance its relevance to the BM25 score.
    `Overall Score = Score(BM25) + Score(time)`
### Limitations
   1. Take in duplicates and retweets as normal. 
   2. It's not a dynamic interface. 
   3. Most tweets don't have geo information.

### Instructions on deploying the system
   1. pip install whoosh, flask, geocoder, flask-googlemaps
   2.run indexSearch.py
`python indexSearch.py`
    3. run app.py
`python app.py`
    4. Input search query into the search box
![image](https://user-images.githubusercontent.com/5117029/44162830-7e07ad80-a08f-11e8-82a6-c023cea0c75e.png)
![image](https://user-images.githubusercontent.com/5117029/44162834-819b3480-a08f-11e8-86cd-8802d37701ac.png)
