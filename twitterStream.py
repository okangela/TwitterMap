import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from elasticsearch import Elasticsearch

# create instance of elasticsearch
es = Elasticsearch([{'host': 54.163.11.20, 'port': 9200}])

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

    consumer_key = "sCjnEgnu4yGQ2Upemv4M7Siiv"                                                                                            
    consumer_secret = "ymUhZwSfTOF8fLuJW8nGxyG71iRSua39Mv30oH9xTYZVPzQqxp"                                                                
                                                                                                                                          
    access_token = "4554433517-t6b77MH6eeRDOt70BG4ep8Dp5FGbFPwFaHKtyyf"                                                                   
    access_token_secret = "iLVcknCw7BeZtmJjamr7HFsvzoWMMrBECtdQZB0Ja8AsU"                                                                 
                                                                                                                                          
    # set twitter keys/tokens                                                                                                             
    auth = OAuthHandler(consumer_key, consumer_secret)                                                                                    
    auth.set_access_token(access_token, access_token_secret)                                                                              
                                                                                                                                          
    # create instance of the tweepy stream                                                                                                
    stream = Stream(auth, listener)                                                                                                       
                                                                                                                                          
    stream.filter(locations=[-180, -90, 180, 90])                                                                                         
    # stream.filter(track=["Trump", "Hillary", "America", "China", "Japan", "Russia", "France", "Australia"])                             
