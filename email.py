
# to find if  the
import re 
split_term = '@'
email ='user@eek.ee'

#print(re.split(split_term,email))

print(re.findall('eek.ee',email))


#finding pattern in a phrase
def multi_re_find(patterns, phrase):

    for pat in patterns:
        print("searching for pattern{}".format(pat))
        print(re.findall(pat, phrase))
        print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd.dsds...dssssss...sddddd'
test_patterns = ['sd*']
multi_re_find(test_patterns,test_phrase)