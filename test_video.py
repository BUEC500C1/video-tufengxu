import tweets_queue
import tweets_to_video
import queue


def test_twitter_video():
    names = ['@BU_Tweets', '@Lakers', '@NBA', '@universal_sci', '@sciencemagazine']
    tweets = get_feeds(names[0])
    assert tweets != ''
