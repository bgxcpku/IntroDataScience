import sys
import json

def hw(tweet_file, d_senti):
    # print 'Hello, world!'
    d_freqency = {}
    for s_line in tweet_file.readlines():
        d_tweet = json.loads(s_line)
        try:
            s_tweet_place = d_tweet["place"]
            s_country_code = s_tweet_place["country_code"]
            s_country_code = s_country_code.encode('utf-8')
            if s_country_code == "US":
                s_state = s_tweet_place["full_name"]
                s_state = s_state.encode('utf-8')
                s_state = s_state.split(' ')
                # print s_state
                s_state = s_state[-1]
                # print s_state
                if s_state == 'US':
                    continue
                try:
                    s_tweet_text = d_tweet["text"]
                    s_tweet_text = s_tweet_text.encode('utf-8')
                    ls_tweet_text = s_tweet_text.split(' ')
                    i_senti_score = 0
                    for s_word in ls_tweet_text:
                        if s_word in d_senti:
                            i_senti_score += d_senti[s_word]
                except:
                    i_senti_score = 0
                if s_state in d_freqency:
                    d_freqency[s_state] += i_senti_score
                else:
                    d_freqency[s_state] = i_senti_score
        #     s_tweet_text = s_tweet_text.encode('utf-8')
        #     ls_tweet_text = s_tweet_text.split(' ')
        #     i_senti_score = 0
        #     for s_word in ls_tweet_text:
        #         if s_word in d_senti:
        #             i_senti_score += d_senti[s_word]
        except:
            pass
        #     i_senti_score = 0
        # print i_senti_score
    # for s_state in d_freqency:
    #     print s_state, d_freqency[s_state]
    t = sorted(d_freqency.iteritems(), key=lambda x:-x[1])[:1]

    for x in t:
        print x[0]
        # print "{0} {1}".format(*x)
    return
    

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    d_senti = {}
    ls_lines = sent_file.readlines()
    for s_line in ls_lines:
        if s_line == ls_lines[-1]:
            ls_line = s_line.split('\t')
        else:
            ls_line = s_line[:-1].split('\t')
        d_senti[ls_line[0]] = int(ls_line[1])
    tweet_file = open(sys.argv[2])
    hw(tweet_file, d_senti)
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()
