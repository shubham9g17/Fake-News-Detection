import string
import re
import nltk
from nltk.stem import WordNetLemmatizer 
import numpy as np

def remove_punct(text):
    return re.sub(r"\W+", " ", text)

def remove_numbers(text):
    text = ''.join([i for i in text if not i.isdigit()])         
    return text

def remove_URL(text):
    url = re.compile(r'https?://\S+|www\.\S+')
    return url.sub(r'',text)

def remove_html(text):
    html=re.compile(r'<.*?>')
    return html.sub(r'',text)

def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def clean_stopwords(text):
    stopwords = set(nltk.corpus.stopwords.words())
    res = []
    text=text.split()
    for word in text:
        if word not in stopwords:
            res.append(word)
    return " ".join(res)

def stem_(x):
    porter_stemmer = nltk.PorterStemmer()
    roots = [porter_stemmer.stem(each) for each in x.split()]
    return " ".join(roots)



 

def lemmi_(x):
    lemmatizer = WordNetLemmatizer()
    li=x.split()
    roots=[]
    for i in li:
        roots.append(lemmatizer.lemmatize(i))
    return " ".join(roots)

