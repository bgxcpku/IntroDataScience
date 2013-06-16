import sys
import json

def hw(tweet_file, d_senti):
    # print 'Hello, world!'
    li_senti_score = []
    ls_tweeeet_lines = tweet_file.readlines()
    for s_line in ls_tweeeet_lines:
        d_tweet = json.loads(s_line)
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
        li_senti_score.append(i_senti_score)

    d_new_senti = {}
    for i, s_line in enumerate(ls_tweeeet_lines):
        if li_senti_score[i] == 0:
            continue
        d_tweet = json.loads(s_line)
        try:
            s_tweet_text = d_tweet["text"]
            s_tweet_text = s_tweet_text.encode('utf-8')
            ls_tweet_text = s_tweet_text.split(' ')
            for s_word in ls_tweet_text:
                if s_word in d_senti:
                    continue
                else:
                    if s_word in d_new_senti:
                        d_new_senti[s_word] += li_senti_score[i]
                    else:
                        d_new_senti[s_word] = li_senti_score[i]
        except:
            pass
    for s_word in d_new_senti:
        if len(s_word) == 0:
            continue
        elif d_new_senti[s_word] >= 5:
            print s_word + ' 5'
        elif d_new_senti[s_word] <= -5:
            print s_word + ' -5'
        else:
            print s_word + ' ' + str(d_new_senti[s_word])
        
    

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
