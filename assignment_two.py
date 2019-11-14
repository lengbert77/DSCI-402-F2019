#Assignment_two Luke Engbert:

#below are the necessary functions to prepare for the function I am writing
def standard_punct_list():
    return ['.','?',',','-',"'",'"',';',':','/',"\t","\n",'!']
def remove_punct(char, punct):
    if char in punct:
       return ''
    return char
    
def get_sentiment_code(filename): 
    lines=open(filename, 'r').readlines()
    codes={}
    for line in lines:
        words=line.lower().strip().replace("\t",' ').replace("\n",' ').split(' ')
        words=[x for x in words if x!='']
        code=float(words[len(words)-1])
        codes[words[0]]=code
    return codes
codes =get_sentiment_code("../data/AFINN-111.txt")    

import functools as ft 
import statistics as st 
#pipeline function cleans up a group of text and returns it in lower case with no punctuation.  
def pipeline(texts):
    for text in texts:
        text=text.lower().replace("\n"," ").replace("\t", " ").split()
        text=["".join([remove_punct(y, standard_punct_list())for y in x]) for x in text if x !='']
    return text
#ex_words is a list of words we don't want to be considered by our function.   
def ex_words():
    return['And','or','if','is','of','then','by','in','with','from','than','a','this','that']
texts='this IS a HappY string?'    
#sentiment_score will be a needed variable in the function.
def sentiment_score(codes,text):
    text=pipeline(text)
    for t in text:
        if t in codes:
           sentiment=codes[t]
           return sentiment
#Part 1.   
#Below: The inputs are 1) a set of sentiment-coded words (as a dict) and 2) a list of text passages (list of strings). 
#You should return a dict of form {word:sentiment}.    
def infer_sentiment_words(codes,texts, stop_words=ex_words()):
    words=set(ft.reduce(lambda x,y:x+y,[pipeline(texts)]))
    words=words.difference(stop_words)
    words=words.difference(codes.keys()) #filter out stop_words and sentiment_code words
    inferred_sentiments={}
    for w in words:
        sents=[]
        for t in pipeline(texts):
            if w in t:
               sents.append(sentiment_score(codes,texts))
        inferred_sentiments[w]=st.mean(sents)
    return inferred_sentiments 
    
    
print(pipeline(['this is     a  happy STRIng!?!...'])) 
print(sentiment_score(codes =get_sentiment_code("../data/AFINN-111.txt") , text=['this is     a  happy STRIng!?!...']))
print(infer_sentiment_words(codes =get_sentiment_code("../data/AFINN-111.txt"),texts=['this is     a  happy STRIng!?!...'],stop_words=ex_words()))


#Part 2
#The following functions read tweets into our workspace, and read them as text.
def read_tweets(filename):	
	data = open(filename, 'rb').read().decode().split("\n")
	tweets = []
	for line in data:
		try:
			tweets.append(json.loads(line.strip()))
		except:
			print("JSON-unopenable tweet encountered")
	return tweets
    
def read_texts(filename):
	tweets = read_tweets(filename)
	text = []
	for tweet in tweets:
		try:
			text.append(unicode(tweet['text']).encode('ascii', 'ignore'))
		except:
			1 == 1
	return text

tweets= read_tweets("./tweets/sanders.json")
#The following function is designed to read tweets into text and then infer sentiment scores for sentiment words in the tweets.
def infer_tweet_word_sentiments(codes,tweets):
    texts1=read_texts(tweets)
    texts= [t["text"] for t in texts1]
    words=set(ft.reduce(lambda x,y:x+y,[pipeline(texts)]))
    words=words.difference(codes.keys()) #filter out sentiment_code words
    inferred_sentiments={}
    for w in words:
        sents=[]
        for t in pipeline(texts):
            if w in t:
               sents.append(sentiment_score(codes,texts))
        inferred_sentiments[w]=st.mean(sents)
    return inferred_sentiments

print(infer_tweet_word_sentiments(codes=get_sentiment_code("../data/AFINN-111.txt"), tweets= ("./tweets/sanders.json")))

#Part3
#3) top_n_words(sentiment_score_dict, n, direction=1)
#The inputs are 1) a dictionary of form {word:sentiment}, 2) a number n, and 3) direction (1 = most positive and 0 = most negative).
#You should return an ordered list of (word, score) tuples arranged in highest-magnitude-first order 
#based on the specified direction.

def top_n_words(sentiment_score_dict, n, direction=1):
    ordered_list=[]
  #This is as far as I've made it so far  






