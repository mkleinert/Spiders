import io
from collections import Counter

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import text 
from bokeh.charts import Scatter, Bar, output_file, show
from bokeh.plotting import figure
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, Range1d, LabelSet, Label
from bokeh.palettes import inferno,viridis 
from bokeh.palettes import Dark2_5 as palette
import itertools

infile = '/Users/mkleinert/Spiders/crawl_BA/style_desc.csv'
stop_words = text.ENGLISH_STOP_WORDS.union(['beer','bottle','glass','head','like','ve'])
ngram_vectorizer = CountVectorizer(analyzer='word', ngram_range=(1, 1), min_df=1,stop_words=stop_words)

style_df = pd.read_csv(infile)
grouped = style_df.groupby('style').agg(sum)

mypalette24 = viridis(230)
appended_data = []

for idx,style in enumerate(grouped.index):
    X = ngram_vectorizer.fit_transform(grouped.loc[style])
    vocab = ngram_vectorizer.get_feature_names()
    word_freq_df = pd.DataFrame({'term': ngram_vectorizer.get_feature_names(), 'occurrences':np.asarray(X.sum(axis=0)).ravel().tolist()})
    word_freq_df['frequency'] = word_freq_df['occurrences']/np.sum(word_freq_df['occurrences'])
    word_freq_df['style'] = grouped.index[idx]
    bokeh_freq =  word_freq_df.sort_values('occurrences',ascending = False).head(n=10)
    appended_data.append(bokeh_freq)

appended_data = pd.concat(appended_data)
source = ColumnDataSource(ColumnDataSource.from_df(appended_data))

p = figure(title='Beer Style Descriptors',plot_width=1000, plot_height=1000,x_range=(0, 1200),  y_range=(.005, .018))
color = mypalette24
p.scatter(x='occurrences', y='frequency', size=8, source=source, color=color,legend='style') #mypalette24[idx]
p.xaxis[0].axis_label = 'Count'
p.yaxis[0].axis_label = 'Frequency'
p.xaxis.major_tick_line_width = 3

labels = LabelSet(x='occurrences', y='frequency', text='term', level='glyph',
              x_offset=5, y_offset=5, source=source, render_mode='canvas')

p.add_layout(labels)

show(p)
