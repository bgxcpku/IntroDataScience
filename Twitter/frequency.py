import sys
import json

def hw(tweet_file):
    """HW function"""
    ls_tweeeet_lines = tweet_file.readlines()
    d_freqency = {}
    i_total = 0
    for s_line in ls_tweeeet_lines:
        d_tweet = json.loads(s_line)
        try:
            s_tweet_text = d_tweet["lang"]
            if s_tweet_text != "en":
                continue
        except:
            pass
        try:
            s_tweet_text = d_tweet["text"]
            s_tweet_text = s_tweet_text.encode('utf-8')
            ls_tweet_text = s_tweet_text.split(' ')
            for s_word in ls_tweet_text:
                i_total += 1
                if s_word in d_freqency:
                    d_freqency[s_word] += 1
                else:
                    d_freqency[s_word] = 1
        except:
            pass
    # i_total = len(d_freqency.keys())
    for s_key in d_freqency:
        str_tp = s_key + ' ' + str(d_freqency[s_key]/float(i_total))
        try:
            str_tp_2 = str_tp.split(' ')
            if str_tp_2[0] != '' and str_tp_2[0].find('\n') == -1:
                try: 
                    val = float(str_tp_2[1])
                    print str_tp
                except:
                    pass
                # print str_tp_2
        except:
            pass
    return


def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()
