### Tokenization with the help of NLTK: TEXT PRE-PROCESSING TECHNIQUES

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

# --------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------

# LEMMATIZATION:

# WordNet Lemmatizer
# Lemmatization technique is like stemming. The output we will get after lemmatization is called 'lemma',which is a root word rather
# than root stem, the output of stemming. After lemmatization, we will be getting a valid word that means the same thing.

# use Cases
# Q/A, chatbot, text summarization

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
''' pos(parts of speech) values can be
    n - Noun
    v - verb
    a - adverb
    a - adjective
'''

print(lemmatizer.lemmatize("going",pos='v'))

# Output
# go

for word in words:
    print(word + "---->" + lemmatizer.lemmatize(word,pos='v'))

# Output
# eating---->eat
# eats---->eat
# eaten---->eat
# writing---->write
# writes---->write
# programming---->program
# programs---->program
# history---->history
# finally---->finally
# finalized---->finalize

print(lemmatizer.lemmatize('fairly'), lemmatizer.lemmatize('sportingly'))

# Output:
# fairly sportingly

# --------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------

# STOPWORDS

# Text preprocessing - Stopwords with the help of NLTK

paragraph = """I have three visions for India. In 3000 years of our history, people from all over 
               the world have come and invaded us, captured our lands, conquered our minds. 
               From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
               the French, the Dutch, all of them came and looted us, took over what was ours. 
               Yet we have not done this to any other nation. We have not conquered anyone. 
               We have not grabbed their land, their culture, 
               their history and tried to enforce our way of life on them. 
               Why? Because we respect the freedom of others.That is why my 
               first vision is that of freedom. I believe that India got its first vision of 
               this in 1857, when we started the War of Independence. It is this freedom that
               we must protect and nurture and build on. If we are not free, no one will respect us.
               My second vision for India’s development. For fifty years we have been a developing nation.
               It is time we see ourselves as a developed nation. We are among the top 5 nations of the world
               in terms of GDP. We have a 10 percent growth rate in most areas. Our poverty levels are falling.
               Our achievements are being globally recognised today. Yet we lack the self-confidence to
               see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect?
               I have a third vision. India must stand up to the world. Because I believe that unless India 
               stands up to the world, no one will respect us. Only strength respects strength. We must be 
               strong not only as a military power but also as an economic power. Both must go hand-in-hand. 
               My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of 
               space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.
               I was lucky to have worked with all three of them closely and consider this the great opportunity of my life. 
               I see four milestones in my career"""

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

import nltk
nltk.download('stopwords')

stopwords.words('english') #It will give all the stopwords in english - he, she, aren't, they, we etc

stemmer = PorterStemmer()
sentences = nltk.sent_tokenize(paragraph)
snowball_sentences = nltk.sent_tokenize(paragraph)
lemma_sentences = nltk.sent_tokenize(paragraph)


# print(sentences)

# output:
# ['I have three visions for India.', 'In 3000 years of our history, people from all over \n               the world have come and invaded us, captured our lands, conquered our minds.', 'From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,\n               the French, the Dutch, all of them came and looted us, took over what was ours.', 'Yet we
#  have not done this to any other nation.', 'We have not conquered anyone.', 'We have not grabbed their land, their culture, \n               their history and tried to enforce our way of life on them.', 'Why?', 'Because we respect the freedom of others.That is why my \n               first vision is that of freedom.', 'I believe that India got its first vision of \n               
# this in 1857, when we started the War of Independence.', 'It is this freedom that\n               we must protect and nurture and build on.', 'If we are not free, no one will respect us.', 'My second vision for India’s development.', 'For fifty years we have been a developing nation.', 'It is time we see ourselves as a developed nation.', 'We are among the top 5 nations of the world\n               
# in terms of GDP.', 'We have a 10 percent growth rate in most areas.', 'Our poverty levels are falling.', 'Our achievements are being globally recognised today.', 'Yet we lack the self-confidence to\n               see ourselves as a developed nation, self-reliant and self-assured.', 'Isn’t this incorrect?', 'I have a third vision.', 'India must stand up to the world.', 'Because I believe that unless India \n               
# stands up to the world, no one will respect us.', 'Only strength respects strength.', 'We must be \n               strong not only as a military power but also as an economic power.', 'Both must go hand-in-hand.', 'My good fortune was to have worked with three great minds.', 'Dr. Vikram Sarabhai of the Dept.', 'of \n               space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.', 
# 'I was lucky to have worked with all three of them closely and consider this the great opportunity of my life.', 'I see four milestones in my career']

# Apply stopwords and filter and then apply Stemming

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i]= ' '.join(words) #converting all the words into sentences

# print(sentences)

# ['i three vision india .', 'in 3000 year histori , peopl world come invad us , captur land , conquer mind .', 'from alexand onward , greek , turk , mogul , portugues , british , french , dutch , came loot us , took .', 'yet done nation .',
# 'we conquer anyon .', 'we grab land , cultur , histori tri enforc way life .', 'whi ?', 'becaus respect freedom others.that first vision freedom .', 'i believ india got first vision 1857 , start war independ .', 'it freedom must protect nurtur build .',
# 'if free , one respect us .', 'my second vision india ’ develop .', 'for fifti year develop nation .', 'it time see develop nation .', 'we among top 5 nation world term gdp .', 'we 10 percent growth rate area .', 'our poverti level fall .', 'our achiev global recognis today .',
# 'yet lack self-confid see develop nation , self-reli self-assur .', 'isn ’ incorrect ?', 'i third vision .', 'india must stand world .', 'becaus i believ unless india stand world , one respect us .', 'onli strength respect strength .', 'we must strong militari power also econom power .',
# 'both must go hand-in-hand .', 'my good fortun work three great mind .', 'dr. vikram sarabhai dept .', 'space , professor satish dhawan , succeed dr. brahm prakash , father nuclear materi .', 'i lucki work three close consid great opportun life .', 'i see four mileston career']


from nltk.stem import SnowballStemmer
snowballstemmer = SnowballStemmer('english')
for i in range(len(snowball_sentences)):
    words = nltk.word_tokenize(snowball_sentences[i])
    words = [snowballstemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    snowball_sentences[i]= ' '.join(words) #converting all the words into sentences

print(snowball_sentences)

# Output:
# ['i three vision india .', 'in 3000 year histori , peopl world come invad us , captur land , conquer mind .', 'from alexand onward , greek , turk , mogul , portugues , british , french , dutch , came loot us , took .',
# 'yet done nation .', 'we conquer anyon .', 'we grab land , cultur , histori tri enforc way life .', 'whi ?', 'becaus respect freedom others.that first vision freedom .', 'i believ india got first vision 1857 , start war independ .',
# 'it freedom must protect nurtur build .', 'if free , one respect us .', 'my second vision india ’ develop .', 'for fifti year develop nation .', 'it time see develop nation .', 'we among top 5 nation world term gdp .', 
# 'we 10 percent growth rate area .', 'our poverti level fall .', 'our achiev global recognis today .', 'yet lack self-confid see develop nation , self-reli self-assur .', 'isn ’ incorrect ?', 'i third vision .', 'india must stand world .',
# 'becaus i believ unless india stand world , one respect us .', 'onli strength respect strength .', 'we must strong militari power also econom power .', 'both must go hand-in-hand .', 'my good fortun work three great mind .', 'dr. vikram sarabhai dept .',
# 'space , professor satish dhawan , succeed dr. brahm prakash , father nuclear materi .', 'i lucki work three close consid great opportun life .', 'i see four mileston career']

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

for i in range(len(lemma_sentences)):
    words = nltk.word_tokenize(lemma_sentences[i])
    words = [lemmatizer.lemmatize(word.lower(), pos = 'v') for word in words if word not in set(stopwords.words('english'))]
    lemma_sentences[i]= ' '.join(words) #converting all the words into sentences

print(lemma_sentences)

# Output:
# ['i three visions india .', 'in 3000 years history , people world come invade us , capture land , conquer mind .', 'from alexander onwards , greeks , turks , moguls , portuguese , british , french , dutch , come loot us , take .', 'yet do nation .',
#  'we conquer anyone .', 'we grab land , culture , history try enforce way life .', 'why ?', 'because respect freedom others.that first vision freedom .', 'i believe india get first vision 1857 , start war independence .', 'it freedom must protect nurture build .',
#  'if free , one respect us .', 'my second vision india ’ development .', 'for fifty years develop nation .', 'it time see develop nation .', 'we among top 5 nations world term gdp .', 'we 10 percent growth rate areas .', 'our poverty level fall .',
#  'our achievements globally recognise today .', 'yet lack self-confidence see develop nation , self-reliant self-assured .', 'isn ’ incorrect ?', 'i third vision .', 'india must stand world .', 'because i believe unless india stand world , one respect us .',
#  'only strength respect strength .', 'we must strong military power also economic power .', 'both must go hand-in-hand .', 'my good fortune work three great mind .', 'dr. vikram sarabhai dept .', 'space , professor satish dhawan , succeed dr. brahm prakash , father nuclear material .',
#  'i lucky work three closely consider great opportunity life .', 'i see four milestones career']

#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------

# Parts of speech Tagging
nltk.download('averaged_perceptron_tagger_eng', quiet=True)
nltk.download('punkt', quiet=True)

sentence = "Taj Mahal is a beautiful monument."
tokens = nltk.word_tokenize(sentence)
print(nltk.pos_tag(tokens))

# Output:
# [('Taj', 'NNP'), ('Mahal', 'NNP'), ('is', 'VBZ'), ('a', 'DT'), ('beautiful', 'JJ'), ('monument', 'NN'), ('.', '.')]
# Here NNP, VBZ, DT are pos tags

# --------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------

# Name Entity Recognition

sentence="The Eiffel Tower was built from 1887 to 1889 by Gustave Eiffel, whose company specialized in building metal frameworks and structures."

import nltk
words=nltk.word_tokenize(sentence)

tag_elements=nltk.pos_tag(words)

nltk.download('maxent_ne_chunker')

nltk.download('words')

nltk.download('maxent_ne_chunker_tab')

nltk.ne_chunk(tag_elements).draw()

# --------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------





