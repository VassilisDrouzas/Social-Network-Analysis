import twitter
import itertools
import time

api = twitter.Api(consumer_key='<consumer_key>',                     #put your twitter credentials here
                  consumer_secret='<consumer_secret>',
                  access_token_key='<access_token_key>',
                  access_token_secret='<access_token_secret')


def getfriends(username):
   
    friends = api.GetFriends(screen_name=username)
    
    friends_list = []
    for i in friends:
        friends_list.append((username,i.screen_name))
    
    return friends_list




Tseries = getfriends("TSeries")
to_filter = [i[0:2] for i in Tseries ]

celebrities=to_filter[5:18]

list = []
for people in celebrities:
    list.append(getfriends(people[1]))
    time.sleep(90)


data = list(itertools.chain.from_iterable(list))

save = [i[0:2] for i in data ]

with open('C:/Users/user/Desktop/dataset.csv', 'w') as f:
    f.write('\n'.join('{}, {}'.format(x[0],x[1]) for x in save))