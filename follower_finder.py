import twitter
import config
import csv
import time

def save_follower_results(follower_list,screen_name):
    with open(r'ff_network_edge.csv', 'a') as f:
        writer = csv.writer(f)
        for followerID in follower_list:
            fields_to_write = [screen_name,followerID]
            writer.writerow(fields_to_write)

def getAllFollowersForUser(script_screen_name, api):
    print("Gathering followers for: {}".format(script_screen_name))
    cursor_value = -1 
    page_counter = 0
    while not cursor_value == 0:
        print("   Follower page: {}".format(page_counter))
        user_follower_result = api.GetFollowerIDsPaged(screen_name=script_screen_name,cursor=cursor_value)

        # save our results
        save_follower_results(user_follower_result[2],script_screen_name)

        # get a new cursor value (make sure that we cover the entire list)
        cursor_value = user_follower_result[0]

        page_counter = page_counter + 1

        time.sleep(60)

def main_function(user_list):  

    api = twitter.Api(consumer_key=config.twitter_consumer_key,
                        consumer_secret=config.twitter_consumer_secret,
                        access_token_key=config.twitter_access_token,
                        access_token_secret=config.twitter_access_token_secret,
                        sleep_on_rate_limit=True)

    

    # for every user in the list, get all their followers

    for user in user_list:
        getAllFollowersForUser(user,api)

    print("Done")

