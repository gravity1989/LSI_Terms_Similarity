import pprint
from gensim import corpora

__author__ = 'bv'
from gensim.corpora import Dictionary
import gensim


class MyCorpus(object):
    def __init__(self):
        self.stopList = set('a for of the and to in'.split())

    def __iter__(self):
        for line in open('resources/myCorpus.txt'):
            yield self.dictionary.doc2bow(line.lower().split())



    def create_Dictionary(self):
        self.dictionary = corpora.Dictionary(line.lower().split() for line in open('resources/mycorpus.txt'))
        #find ids of all stopwords from dictionary
        stop_ids = [self.dictionary.token2id[stopword] for stopword in self.stopList
            if stopword in self.dictionary.token2id]
        #find ids of all words in dictionary which have frequency equal to 1.
        rare_ids = [ tokenid for tokenid,docFreq in self.dictionary.dfs.items()
                     if docFreq == 1]
        self.dictionary.filter_tokens(stop_ids+rare_ids)
        self.dictionary.compactify()
        pprint.pprint(self.dictionary.token2id)
        return  self.dictionary



if __name__ == '__main__':
    myCorpus = MyCorpus()
    dictionary = myCorpus.create_Dictionary()
    for vector in myCorpus:
        print(vector)