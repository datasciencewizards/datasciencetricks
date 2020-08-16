#pip install deepsegment

from deepsegment import DeepSegment

#declaring segmenter object
segmenter = DeepSegment()

#applying segmentation (tokenization)
segmenter.segment('I am Batman, I live in Gotham')
>>>['I am Batman, I live in Gotham']

#performs well even without punctuation
segmenter.segment('I am Batman i liv in gotham')
>>>['I am Batman', 'i liv in gotham']
