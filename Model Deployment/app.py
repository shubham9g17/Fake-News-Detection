import pickle
import numpy as np
import pandas as pd
from Preprocessing import *

def clean(x):
    x.lower()
    x=remove_URL(x)
    x=remove_html(x)
    x=remove_emoji(x)
    x=remove_punct(x)
    x=remove_numbers(x)
    x=clean_stopwords(x)
    x=lemmi_(x)
    return x



classifier = pickle.load(open('final_model.pkl', 'rb'))



def getPredictions(feats):
    feats=clean(str(feats))
    return 'Real' if classifier.predict([feats])[0] else 'Fake'