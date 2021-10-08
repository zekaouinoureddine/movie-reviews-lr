import re
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('stopwords')
nltk.download('wordnet')


def decontracted(x):
    x = str(x).lower()
    x = x.replace(",000,000", " m").replace(",000", " k").replace("′", "'").replace("’", "'")\
        .replace("won't", " will not").replace("cannot", " can not").replace("can't", " can not")\
        .replace("n't", " not").replace("what's", " what is").replace("it's", " it is")\
        .replace("'ve", " have").replace("'m", " am").replace("'re", " are")\
        .replace("he's", " he is").replace("she's", " she is").replace("'s", " own")\
        .replace("%", " percent ").replace("₹", " rupee ").replace("$", " dollar ")\
        .replace("€", " euro ").replace("'ll", " will").replace("how's"," how has").replace("y'all"," you all")\
        .replace("o'clock"," of the clock").replace("ne'er"," never").replace("let's"," let us")\
        .replace("finna"," fixing to").replace("gonna"," going to").replace("gimme"," give me").replace("gotta"," got to").replace("'d"," would")\
        .replace("daresn't"," dare not").replace("dasn't"," dare not").replace("e'er"," ever").replace("everyone's"," everyone is")\
        .replace("'cause'"," because")
    x = re.sub(r"([0-9]+)000000", r"\1m", x)
    x = re.sub(r"([0-9]+)000", r"\1k", x)
    return x

def remove_html(sentence): 
    pattern = re.compile('<.*?>')
    cleaned_sentence = re.sub(pattern,' ',sentence)
    return cleaned_sentence

def remove_url(sentence):
    text = re.sub(r"http\S+", " ", sentence)
    cleaned_sentence = re.sub(r"www.\S+", " ", text)
    return cleaned_sentence

def remove_punctuations(sentence):
    cleaned_sentence  = re.sub('[^a-zA-Z]',' ',sentence)
    return cleaned_sentence

def remove_patterns(sentence): 
    cleaned_sentence = re.sub("\\s*\\b(?=\\w*(\\w)\\1{2,})\\w*\\b",' ',sentence)
    return cleaned_sentence

def remove_stopwords(sentence):
    default_stopwords = set(nltk.corpus.stopwords.words('english'))
    remove_not = set(['no', 'nor', 'not'])
    custom_stopwords = default_stopwords - remove_not
    review = [words.lower() for words in sentence.split() if words not in custom_stopwords]
    cleaned_sentence = " ".join(review)
    return cleaned_sentence

def stem_text(sentence):
    stemmer = PorterStemmer()
    stemmed_sentence = stemmer.stem(sentence)
    return stemmed_sentence

def lemmatize_text(sentence):
    lemmatizer = WordNetLemmatizer()
    lemmatized_sentence = lemmatizer.lemmatize(sentence)
    return lemmatized_sentence


def clean_data(sentence):
    cleaned_sentence = lemmatize_text(stem_text(remove_stopwords(remove_patterns(remove_punctuations(remove_url(remove_html(decontracted(sentence))))))))
    return cleaned_sentence