import io
from collections import Counter

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import text 
from bokeh.charts import Bar, output_file, show

infile = '/Users/mkleinert/Spiders/crawl_BA/KBS_desc.csv'
stop_words = text.ENGLISH_STOP_WORDS.union(['beer','bottle','glass','head','like','ve'])
ngram_vectorizer = CountVectorizer(analyzer='word', ngram_range=(1, 1), min_df=1,stop_words=stop_words)

with io.open(infile, 'r', encoding='utf8') as fin:
    X = ngram_vectorizer.fit_transform(fin)
    vocab = ngram_vectorizer.get_feature_names()
    counts = X.sum(axis=0).A1
    freq_distribution = Counter(dict(zip(vocab, counts)))
    print (freq_distribution.most_common(10))
    top_words = freq_distribution.most_common(10)
    words_df = pd.DataFrame(top_words)
    words_df.columns = ['word','count']
    words_df.index = words_df['word']
    # print words_df
    bar = Bar(words_df,values='count' )
    output_file("stacked_bar.html")
    show (bar)
    # print freq_distribution