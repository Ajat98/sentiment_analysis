from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#First version using TextBlob
pos_count = 0
pos_correct = 0
with open('positive.txt', 'r') as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)
        if analysis.sentiment.polarity >= 0.0001:
            if analysis.sentiment.polarity > 0:
                pos_correct += 1
            pos_count += 1

neg_count = 0
neg_correct = 0
with open('negative.txt', 'r') as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)
        if analysis.sentiment.polarity <= -0.0001:
            if analysis.sentiment.polarity <= 0:
                neg_correct += 1
            neg_count += 1

#Issue with classifying as 0 sentiment polarity. 

print("Positive accuracy = {}% with {} samples".format(pos_correct/pos_count*100.0, pos_count))
print("Negative accuracy = {}% with {} samples".format(neg_correct/neg_count*100.0, neg_count))

#Second version using vadersentiment
#Using vadersentiment
thresh = 0.5
analyzer = SentimentIntensityAnalyzer()

#Positive sentiment
pos_count = 0
pos_correct = 0
with open('positive.txt', 'r') as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if vs['compound'] >= thresh or vs['compound'] <= -thresh:
            if vs['compound'] > 0:
                pos_correct += 1
            pos_count += 1

#Neg sentiment
neg_count = 0
neg_correct = 0
with open('negative.txt', 'r') as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if vs['compound'] >= thresh or vs['compound'] <= -thresh:
            if vs['compound'] <= 0:
                neg_correct += 1
            neg_count += 1

print("Positive accuracy = {}% with {} samples".format(pos_correct/pos_count*100.0, pos_count))
print("Negative accuracy = {}% with {} samples".format(neg_correct/neg_count*100.0, neg_count))


#Improved from above
thresh = 0.5

#Positive sentiment
pos_count = 0
pos_correct = 0
with open('positive.txt', 'r') as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if not vs['neg'] > 0.1:
            if vs['pos'] - vs['neg'] > 0:
                pos_correct += 1
            pos_count += 1

#Neg sentiment
neg_count = 0
neg_correct = 0
with open('negative.txt', 'r') as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if not vs['pos'] > 0.1:
            if vs['pos'] - vs['neg'] <= 0:
                neg_correct += 1
            neg_count += 1

print("Positive accuracy = {}% with {} samples".format(pos_correct/pos_count*100.0, pos_count))
print("Negative accuracy = {}% with {} samples".format(neg_correct/neg_count*100.0, neg_count))


# %%


