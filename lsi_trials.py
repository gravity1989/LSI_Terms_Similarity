# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 15:00:11 2015

@author: rv
"""

class lsi_similarity:
    
    
    def main(self):
        documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
              "The EPS user interface management system",
              "System and human system engineering testing of EPS",
              "Relation of user perceived response time to error measurement",
              "The generation of random binary unordered trees",
              "The intersection graph of paths in trees",
              "Graph minors IV Widths of trees and well quasi ordering",
              "Graph minors A survey"]

        #remove stop words

        #remove words that appear only once.


if __name__ == '__main__':


    '''
        We need a few thing to do LSI transformation:
        1. corpus: corpus is a list of vectors. [(1,2),(2,3)]
        2. dictionary : mapping between words and ids.
        '''