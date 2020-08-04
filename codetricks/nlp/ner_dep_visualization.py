import spacy
from spacy import displacy
 
#sample text to analyze
text = "Sheldon Cooper was born in Texas"

#loading and initializing the model
nlp = spacy.load('en_core_web_sm')
doc = nlp(text)

#visualizaing dependency parse
displacy.serve(doc, style="dep")

#visualizaing entity recognizer
displacy.serve(doc, style="ent")
