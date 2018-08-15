

from datetime import datetime
from whoosh.scoring import BM25F	

class TimeWeighting(BM25F):
	use_final = True
	def final(self, searcher, docnum, score):
		time = 0
		try:
			datestr = searcher.stored_fields(docnum).get("coords")
			time = int(datestr)
		except:
			time = 0	
		return score + time*0.0000001

		


def search(term, numResults):
	res = []
	from whoosh.qparser import QueryParser
	with ix.searcher(weighting=TimeWeighting()) as searcher:
		query = QueryParser("text", ix.schema).parse(term)
		results = searcher.search(query, limit=numResults)
		for r in results:
			res.append([r["text"],r.score, r["place"]])
	

	return res
