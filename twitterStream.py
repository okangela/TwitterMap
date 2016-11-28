import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from elasticsearch import Elasticsearch

# create instance of elasticsearch
es = Elasticsearch([{'host': ****, 'port': 9200}])

class TweetStreamListener(StreamListener):
    # on success
    def on_data(self, data):

        # decode json
        dict_data = json.loads(data)
        # print dict_data
        # add text and sentiment info to elasticsearch
        if dict_data['geo'] != None:
            es.index(index="twitter",
                     doc_type="json",
                     body={"user": dict_data['user']['id'],
                            "text": dict_data['text'],
                            "coordinates": dict_data['geo']})
            print "Update!"
        return True

    # on failure
    def on_error(self, status):
        print status
        return True

if __name__ == '__main__':
    # create instance of the tweepy tweet stream listener
    listener = TweetStreamListener()

    consumer_key = "****"                                                                                            
    consumer_secret = "****"                                                                
                                                                                                                                          
    access_token = "********"                                                                   
    access_token_secret = "****"                                                                 
                                                                                                                                          
    # set twitter keys/tokens                                                                                                             
    auth = OAuthHandler(consumer_key, consumer_secret)                                                                                    
    auth.set_access_token(access_token, access_token_secret)                                                                              
                                                                                                                                          
    # create instance of the tweepy stream                                                                                                
    stream = Stream(auth, listener)                                                                                                       
                                                                                                                                          
    stream.filter(locations=[-180, -90, 180, 90])                                                                                         
    # stream.filter(track=["Trump", "Hillary", "America", "China", "Japan", "Russia", "France", "Australia"])                             
