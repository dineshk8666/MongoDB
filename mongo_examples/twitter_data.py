from tweepy import API
lookup = 'BigData'
api = API()
search = []
page = 1
MaxPage = 10
while(page<=MaxPage):
    tweets = api.search(lookup, page=page)
    for tweet in tweets:
        search.append(tweet)
    page =  page + 1

print len(search)
