import re
from collections import defaultdict
class Code:
	def __init__(self):
		self.index = defaultdict(list)
		self.documents = {}
		self.__unique_id = 0
 
	def Search(self, word):
		"""
		Given a word, search for it and retrieve the top 10 paragraphs (Documents) that contain it
		"""
		word = word.lower()
		if self.index.get(word):
			return ([self.documents.get(id, None) for id in self.index.get(word)])[:10],len(self.index.get(word))
		return [],0

	def tokenize(self, document):
		return document.split(' ')   # Tokenize to words by splitting at whitespace 
 
	def indexing(self, document):
		"""
		Index a given document
		"""
		for token in [t.lower() for t in self.tokenize(document)]:   # Converting the words to lowercase after tokenizing the document
 
				if self.__unique_id not in self.index[token]:
					 self.index[token].append(self.__unique_id)
 
		self.documents[self.__unique_id] = document  # Generate a unique ID for every document that is index
		self.__unique_id += 1
	def clear(self):
		"""
		Clear the index and all indexed documents
		"""
		self.index.clear()
		self.documents.clear()
		
	def sen(self,d,query):
		d=d.replace("\r\n","\n")
		d=d.split("\n\n\n") # Splitting paragraphs
		# print(d)
		for i in d:
			i.replace("\n"," ")
			print(i)
			self.indexing(i)  # Indexing document
		l=[]
		le=0
		l,le=self.Search(query)  # Search a word in documents and returns top 10 results
		self.clear()		  # Clear the index and documents
		return l,le
