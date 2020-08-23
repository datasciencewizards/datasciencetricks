from bs4 import BeautifulSoup
import requests
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#fetching text from wikipedia
res = requests.get('https://en.wikipedia.org/wiki/The_Big_Bang_Theory')
soup = BeautifulSoup(res.text,"html5lib")
text = soup.get_text(strip=True)

#removing noise from data - stopwords and punctuations
tokens = word_tokenize(text)
stops = stopwords.words('english')
punc = list(string.punctuation) + ["''", "``", "'s","-"] 
noise = stops+ punc
tokens = [w.lower() for w in tokens if not w.lower() in noise] 

#frequency distribution graph
freq = nltk.FreqDist(tokens)
freq.plot(7)
