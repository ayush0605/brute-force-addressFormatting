import re
from fuzzywuzzy import fuzz
import numpy as np

#Calculated fuzzy score (Normalized similarity score)
def comp(x,y):
    if(x==x and y==y):
        x=re.sub("\s+", " ", re.sub("[^A-Za-z0-9]", " ", x)).strip().title()
        y=re.sub("\s+", " ", re.sub("[^A-Za-z0-9]", " ", y)).strip().title()
        return fuzz.ratio(x,y)
    else:
        return np.nan