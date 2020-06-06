#!/usr/bin/env python
# coding: utf-8

# In[20]:



import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import tweepy
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt 
import seaborn as sns
import string
import nltk
nltk.download('stopwords')
import warnings 
warnings.filterwarnings("ignore", category=DeprecationWarning)


# In[21]:


# This is how the Naive Bayes classifier expects the input
def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict


# In[22]:


# This is how the Naive Bayes classifier expects the input
def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]

    my_dict = dict([(word, True) for word in useful_words])
    return my_dict


# In[23]:


create_word_features(["the", "quick", "brown", "quick", "a", "fox"])


# In[24]:


neg_reviews = []
for fileid in movie_reviews.fileids('neg'):
    words = movie_reviews.words(fileid)
    neg_reviews.append((create_word_features(words), "negative"))


# In[25]:


pos_reviews = []
for fileid in movie_reviews.fileids('pos'):
    words = movie_reviews.words(fileid)
    pos_reviews.append((create_word_features(words), "positive"))


# In[26]:


train_set = neg_reviews[:750] + pos_reviews[:750]
test_set =  neg_reviews[750:] + pos_reviews[750:]


# In[29]:


classifier = nltk.NaiveBayesClassifier.train(train_set)


# In[30]:


accuracy = nltk.classify.util.accuracy(classifier, test_set)
print(accuracy * 100)


# In[38]:


import re
import tweepy
import pandas as pd
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
import string
import nltk
import warnings
from textblob import TextBlob

def twts(name,n):
    consumer_key = 'b6KVEubTSuy3whcRz1BIfIoAp'
    consumer_secret = 'hK7N9OULsGTBqjx0WwHizTJBlOgEoaScAE8xJMyjgGKd3hogpo'
    access_token = '1068036191721787392-PElOyO26UTQoFWF6biUJbaQ9vrZhWB'
    access_token_secret = 'JhtafgxCltxlqwtvhTJx0KK93vqqaJhPtyq4mrPT0m0Cx'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    public_tweets = api.search(name)

    for tweet in public_tweets[:n]:
        print(tweet.text)

    data = pd.DataFrame(data=[tweet.text for tweet in public_tweets], columns=['Tweets'])
    display(data.head(2))
    
    def remove_pattern(input_txt, pattern):
        r = re.findall(pattern, str(input_txt))
        for i in r:
            input_txt = re.sub(i, '', str(input_txt))

        return input_txt


    data['tidy_tweet'] = np.vectorize(remove_pattern)(data['Tweets'], "@[\W]*")
    data['tidy_tweet'] = np.vectorize(remove_pattern)(data['Tweets'], "http://")
    # df = pd.DataFrame({'tidytweets':tidy_tweet, 'tweet'= Tweets})
    data['tidy_tweet'] = data['tidy_tweet'].str.replace("[^a-zA-Z#]", " ")
    #data['tidy_tweet'] = data['tidy_tweet'].str.replace(, ' ')
    data['tidy_tweet'] = data['tidy_tweet'].fillna("")
    data['tidy_tweet'] = data['tidy_tweet'].apply(lambda x: ' '.join([w for w in x.split() if len(w) > 3]))
    display(data.head())

    data["tidy_tweet"][0]
    
    sent=[]
    
    for i in range(0,len(data["tidy_tweet"])):
        review_santa = data["tidy_tweet"][i]
        print(data["Tweets"][i])
        print(review_santa)

        
        words = word_tokenize(review_santa)
        words = create_word_features(words)
        sen = classifier.classify(words)
        print(sen)
        sent.append(sen)
        
    print(sent)
    data['sentiment']= sent
        
    display(data.head(2))
        
    c= list(data.groupby('sentiment').size())
    #print (c)
    
    posper="Percentage of positive tweets: {}%".format(c[1]*100/len(data['sentiment']))
    negper="Percentage of negative tweets: {}%".format(c[0]*100/len(data['sentiment']))
    print(posper,negper)    
    
    
    z = name +','+','+ ','+','+str(c[1]*100/len(data['sentiment']))+','+ str(c[0]*100/len(data['sentiment']))+'\n'
    with open(r'C:\Users\Khyati Kansagra\Desktop\SMDM\twitterdata.csv', 'a',encoding='utf-8') as newFile:
        newFile.write(z)
        data.to_csv(newFile, header=False)
        
   
    
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt

    wordcloud = WordCloud(width=480, height=480, margin=0, background_color="white").generate(' '.join(data['tidy_tweet']))

    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.show()
    
    wordcloud.to_file(r"C:\Users\Khyati Kansagra\Desktop\SMDM\Wordclouds"+name+".png")
    
tvshows=["#theoffice","#arrow","#daredevil","#theflash","#the100","#outlander","#parksandrecreation","#breakingbad","#houseofcards","#thisisus","#sexandthecity","#gameofthrones","#thevampirediaries","#teenwolf","#hannibal","#thewalkingdead","#thehauntingofhillhouse","#riverdale","#sherlock","#howtogetawaywithmurder","#dexter","#thewire","#suits","#sense8","#alteredcarbon","#gotham","#thebigbangtheory","#orangeisthenewblack","#strangerthings"]
    
for j in range(0, len(tvshows)):
    twts(tvshows[j],2)


# In[ ]:




