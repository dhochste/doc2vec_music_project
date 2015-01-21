"""
This file contains functions for loading Amazon Music Reviews dataframes
and performing Doc2Vec on the reviews.

Part of Project for Insight Data Science - Silicon Valley 2015a

David L. Hochstetler
1/20/15

Much thanks to Matt P. and Ben E. for the dataframe and Doc2Vec help!
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numexpr as ne 		# Used by pandas.query method
import sys
import re
import gensim, logging
import cPickle as pickle 	# Used for pickling/unpickling files


