import sys
import json

def hw(tweet_file):
    """HW function"""
    ls_tweeeet_lines = tweet_file.readlines()
    d_freqency = {}
    for s_line in ls_tweeeet_lines:
        d_tweet = json.loads(s_line)
        # print d_tweet
        try:
            ld_hashtags = d_tweet["entities"]["hashtags"]
            # print ld_hashtags
            for d_hashtag in ld_hashtags:
                s_hash_text = d_hashtag["text"].encode('utf-8')
                if s_hash_text in d_freqency:
                    d_freqency[s_hash_text] += 1
                else:
                    d_freqency[s_hash_text] = 1
        except KeyError:
            pass

    ##TODO : Pick top ten from Dictionary##
    t = sorted(d_freqency.iteritems(), key=lambda x:-x[1])[:10]

    for x in t:
        print "{0} {1}".format(*x)

    return


def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()
