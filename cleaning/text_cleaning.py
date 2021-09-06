import re
from spellchecker import SpellChecker

import nltk
nltk.download('stopwords')
nltk.download('punkt')
french_stopwords = nltk.corpus.stopwords.words('french')
french_stopwords.remove('l') # litre

from french_lefff_lemmatizer.french_lefff_lemmatizer import FrenchLefffLemmatizer
lemmatizer = FrenchLefffLemmatizer()


def clean_text(text):
    """
    Applies some pre-processing on the given text
    @param text: string
    @return: text after processing: string
    """
    
    # convert text to lowercase
    text = text.lower()

    # remove numbers, symbols and ponctuation
    text = re.sub(r"[^a-z]", " ", text)

    # remove leading whitespaces
    text = text.strip()

    # remove stop words
    tokenize_sentence = nltk.tokenize.word_tokenize(text)
    words_w_stopwords = [i for i in tokenize_sentence if i not in french_stopwords]

    # lemitization
    words_lemmatize = (lemmatizer.lemmatize(w) for w in words_w_stopwords)
    text = ' '.join(w for w in words_lemmatize)

    # spell check
    spell = SpellChecker(language='fr')
    text = spell.correction(text)

    return text

