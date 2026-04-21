# Word to vector conversion:
# One Hot Encodeing: (Not mostly used)

## Disadvantages
# sparse matrix- overfitting
# ML-Algorithm - no fixed input
# out of vocabulary
# No semantix meaning is captured

# Bag of Words (BOW)

# TF-IDF (Term Frequrency - Inverse Document Frequency)

## Word Embeddings:
#   In NLP, word embedding is a term used for the representation of words for text analysis, typically in the form of
# a real valued vector that encodes the meaning of the word such that the words that are closer in the vector space are expected 
# to be similar in meaning.


## Techniques to train a model using word 2 vec:
#  1. CBOW- continous bag of words
#  2. skipgram


# for small dataset use cbow technique.
# for large dataset use skipgram technique

# Gensim is the pre-tranined google word2vec
