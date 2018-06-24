import twitter
import config
import csv
import time

def save_sorted_follower_list(user_screen_name,input_list):
    with open(r'network_edge.csv', 'a') as f:
        writer = csv.writer(f)
        for followerID in input_list:
            fields_to_write = [user_screen_name,followerID]
            writer.writerow(fields_to_write)

api = twitter.Api(consumer_key=config.twitter_consumer_key,
                      consumer_secret=config.twitter_consumer_secret,
                      access_token_key=config.twitter_access_token,
                      access_token_secret=config.twitter_access_token_secret,
                      sleep_on_rate_limit=True)
                      


#statuses = api.GetUserTimeline(screen_name='eleanorkuanchan')
#print([s.text for s in statuses])

#results = api.GetSearch( raw_query="q=twitter%20&result_type=recent&since=2014-07-19&count=5")

#friend_result = api.GetFriends(screen_name='eleanorkuanchan')

#friend_result.sort(key=lambda x: x.followers_count, reverse=True)

#save_sorted_friend_list(friend_result)


print("starting search")
search_results = api.GetSearch( raw_query="q=coke%20&result_type=popular&l=en&count=5")

for tweet in search_results:
    user_screen_name = tweet.user.screen_name
    print("getting {} follower".format(user_screen_name))
    user_follower_result = api.GetFollowerIDs(screen_name=user_screen_name,total_count=50000)
    print("done getting users follower")
    
    save_sorted_follower_list(user_screen_name,user_follower_result)

    print("waiting a minute next call")
    time.sleep(60)


print("DONE")