import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import wikipedia

#fetching text
text = wikipedia.page("The Big Bang Theory").content

#removing noise from data - stopwords and punctuations
tokens = word_tokenize(text)
stops = stopwords.words('english')
punc = list(string.punctuation) + ["''", "``", "'s","-", "==", '==='] 
noise = stops+ punc
tokens = [w.lower() for w in tokens if not w.lower() in noise] 

#frequency distribution graph
freq = nltk.FreqDist(tokens)
plt = freq.plot(7)
