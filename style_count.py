import io
from collections import Counter

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import text 
from bokeh.charts import Bar, output_file, show
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.models.ranges import FactorRange
from bokeh.models import Legend
from bokeh.palettes import Spectral5

infile = '/Users/mkleinert/Spiders/crawl_BA/style_count.csv'
output_file("bar_colormapped.html")

style_df = pd.read_csv(infile)

style_df = style_df.set_index(['style'])
p = Bar(style_df, 'style', values='count', title="Style Count", legend=False)
p.min_border_left = 80

show(p)
