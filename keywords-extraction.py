# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 14:18:53 2020

@author: snmuj
"""

#pip install PyICU-2.6-cp38-cp38-win_amd64.whl

#pip install pycld2-0.41-cp38-cp38-win_amd64.whl

import os
from nltk.parse import stanford as SParse
from nltk.tag import stanford as STag
from nltk.tokenize import StanfordSegmenter

from polyglot.text import Text
from rake_nltk import Rake

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

os.environ['STANFORD_MODELS'] = 'C:\\Users\\snmuj\\OneDrive\\Documents\\salm\\stanford-segmenter-2018-10-16\\data;C:\\Users\\lenovo\\Documents\\salm\\stanford-postagger-full-2018-10-16\\models'
os.environ['STANFORD_PARSER'] = 'C:\\Users\\snmuj\\OneDrive\\Documents\\salm\\stanford-parser-full-2018-10-17'
os.environ['CLASSPATH'] = 'C:\\Users\\snmuj\\OneDrive\\Documents\\stanford-parser-full-2018-10-17'
os.environ['JAVAHOME'] = 'C:\Program Files\Java\jdk-14.0.2_windows-x64_bin.exe'

segmenter = StanfordSegmenter('C:\\Users\\snmuj\\OneDrive\\Documents\\salm\\stanford-segmenter-2018-10-16\\stanford-segmenter-3.9.2.jar')
segmenter.default_config('ar')
text = segmenter.segment_file('text file')
print(text)

tagger = STag.StanfordPOSTagger('arabic.tagger', 'C:\\Users\\snmuj\\OneDrive\\Documents\\stanford-postagger-full-2018-10-16\\stanford-postagger.jar')
for tag in tagger.tag(text.split()):
	print(tag[1])
    
parser = SParse.StanfordParser(model_path='edu/stanford/nlp/models/lexparser/arabicFactored.ser.gz')
sentences = parser.raw_parse_sents(text.split('.'))
for line in sentences:
	for sentence in line:
		print(sentence)
sentence.draw()


from polyglot.text import Text
text = Text(text)
for sent in text.sentences:
    print(sent, "\n")
    for entity in sent.entities:
        print(entity.tag, entity)
        
        
with open(r'text file', encoding='utf-8') as file:
    novels = file.read()
print(novels[:106])


import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")
arb_stopwords = set(nltk.corpus.stopwords.words("arabic"))

# Get Arabic stopwords and print some of them
arb_stopwords = (nltk.corpus.stopwords.words('arabic'))
arb_stopwords[:414]


rake = Rake(stopwords=stopwords.words('arabic'), punctuations=',./»:،؛":.,’،\''.split(), language='arabic', max_length=3)
rake.extract_keywords_from_text(novels)
for phrase in rake.get_ranked_phrases()[:24]:
 print(phrase)
 
