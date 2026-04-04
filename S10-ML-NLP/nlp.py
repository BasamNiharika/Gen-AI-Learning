### Tokenization with the help of NLTK:

corpus = """
Hello, Welcome to Solugenix.
Go to official sgx's website, check for new roles opened for freshers.
Thanks for reaching out to us!
"""
print(corpus)

# Output

# Hello, Welcome to Solugenix.
# Go to official sgx's website, check for new roles opened for freshers.
# Thanks for reaching out to us!

# --------------------------------------------------------------------------------------------------------------------------

# TOKENIZATION

# Paragraph --> sentences 
# use sent_tokenize from nltk
from nltk import sent_tokenize
documents = sent_tokenize(corpus)
print(documents)

# output:
# ['\nHello, Welcome to Solugenix.', "Go to official sgx's website, check for new roles opened for freshers.", 'Thanks for reaching out to us!']

# ----------------------------------------------------------------------------------------------------------------------------

# use word_tokenize from nltk
from nltk import word_tokenize
# Sentences --> words
for sentence in documents:
    print(word_tokenize(sentence))

# Output:
# ['Hello', ',', 'Welcome', 'to', 'Solugenix', '.']
# ['Go', 'to', 'official', 'sgx', "'s", 'website', ',', 'check', 'for', 'new', 'roles', 'opened', 'for', 'freshers', '.']
# ['Thanks', 'for', 'reaching', 'out', 'to', 'us', '!']

# -----------------------------------------------------------------------------------------------------------------------------

# paragraph --> words
token_list = word_tokenize(corpus)
print(f"tokenization {token_list}")

# Output:
# tokenization $['Hello', ',', 'Welcome', 'to', 'Solugenix', '.', 'Go', 'to', 'official', 'sgx', "'s", 'website', ',', 'check', 'for', 'new', 'roles', 'opened', 'for', 'freshers', '.', 'Thanks', 'for', 'reaching', 'out', 'to', 'us', '!']

#------------------------------------------------------------------------------------------------------------------------------ 

# tokenization for punctuation
from nltk import wordpunct_tokenize
punctuaion_token_list = wordpunct_tokenize(corpus)
print(punctuaion_token_list)

# Output:
# ['Hello', ',', 'Welcome', 'to', 'Solugenix', '.', 'Go', 'to', 'official', 'sgx', "'", 's', 'website', ',', 'check', 'for', 'new', 'roles', 'opened', 'for', 'freshers', '.', 'Thanks', 'for', 'reaching', 'out', 'to', 'us', '!']

# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------

### Stemming and Its Types - Text Preprocessing

# Stemming is the process of reducing a word to its word stem that affixes to suffixes and prefixes or to the roots
# of words known as a lemma. Stemming is important in natural language understanding(NLU) and Natural language processing.

# Classification problem
# comments of a product is a positive review or negative review.
# Reviews -----> eating, eaten, eat [goes, going, goes] --->go

words = ["eating", "eats", "eaten", "writing", "writes", "programming", "programs", "history", "finally", "finalized"]

# PorterStemmer
from nltk.stem import PorterStemmer
stemming = PorterStemmer()
for word in words:
    print(word+"------>"+stemming.stem(word))

# Output:
# eating------>eat
# eats------>eat
# eaten------>eaten
# writing------>write
# writes------>write
# programming------>program
# programs------>program
# history------>histori
# finally------>final
# finalized------>final

print(stemming.stem('congratulation'))   

# Output:
# congratul                      // disadvantage of stemming techniques - it is stemming meaning less words

# ----------------------------------------------------------------------------------------------------------------------------

# RegexpStemmer class
# NLTK has RegexpStemmer class with the help of which we can we easily implement Regular Expression Stemmer algorithms.
# It basically takes a single regular expression and removes any prefix or suffix that matches the expression.

from nltk.stem import RegexpStemmer
regex_stemmer = RegexpStemmer('ing$|s$|e$|able$', min=4)

print(regex_stemmer.stem('eating'))

# Output:
# eat

print(regex_stemmer.stem('ingeating'))

# Output:
# ingeat                   // meaningless - disadvantage of stemming

# ----------------------------------------------------------------------------------------------------------------------------

# Snowball Stemmer
from nltk.stem import SnowballStemmer
snowball_stemmer = SnowballStemmer('english')    # assigning language parameter - english
for word in words:
    print(word+"----->"+snowball_stemmer.stem(word))

# Output:'
# eating----->eat
# eats----->eat
# eaten----->eaten
# writing----->write
# writes----->write
# programming----->program
# programs----->program
# history----->histori
# finally----->final
# finalized----->final

# -----------------------------------------------------------------------------------------------------------------------------

# Difference between porterStemmer and snowballStemmer

# snowballStemmer is better than porterStemmer

print(stemming.stem('fairly'),stemming.stem('sportingly'))  # PorterStemmer
# output - fairli sportingli

print(snowball_stemmer.stem('fairly'), snowball_stemmer.stem('sportingly'))  # SnowballStemmer
# output - fair sport


# Conclusion:
# There are few disadvantages of stemming techniques, that's why we go for lemmatization.












