import re

# patterns = ['term1', 'term2']

text = "This is a string with term1, not the other!"


# for pattern in patterns:
#     print("I'm searching for: " + pattern)

#     if re.search(pattern, text):
#         print("MATCH!")
#     else:
#         print("NO MATCH!")

match = re.search('term1', text)

print(type(match))  # match.start()는 몇번째 문자열에서 match 되었는지 보여줌.

# 정규 표현식은 문자열을 분할하는 기능도 한다.
# split()
split_term = '@'

email = 'user@gmail.com'

print(re.split(split_term, email))

# findall - 찾고자하는 문자를 전부 배열로 만들어서 저장 ['match','match'] 와 같이 저장함.
print(re.findall('match', 'text pharse match match in middle'))

# 정규식의 핵심은 따로 있다.
# medich 구문


def multi_re_find(patterns, phrase):

    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print('\n')

# test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dsssss...sdddd'
# test_patterns = ['sd*']# *를 쓰면 s나 d가 들어간 모든 조합을 다 잘라서 배열로 저장함.
# test_patterns = ['sd+']  # sd로 시작하는 모든 글자 단어를 잘라서 배열로 저장
# test_patterns = ['sd?']  # * 과 똑같이 동작하는 것 같음.
# test_patterns = ['sd{3}']  # s + d 3개의 조합을 찾음 (sddd)
# test_patterns = ['sd{1,3}']  # s 뒤에 d가 1개또는 3개인 것을 찾음.
# test_patterns = ['s[sd]+'] # 이렇게 쓰면 s뒤에 1개 이상의 s나 d가 있는 조합을 모두 찾아온다.

# test_phrase = "This is a string! But it has puncuation. How can we remove it?"
# test_patterns = ['[^!.?]+'] # 이렇게 쓰면 문장 내에서 ! . ?를 기준으로 잘라서 배열로 저장한다.
# test_patterns = ['[A-Z]+'] # 문장 내에서 대문자 A-Z를 가져와서 전부 보여줌.
# test_patterns = ['[a-z]+'] #문장내에서 a-z를 전부 가져와서 보여줌.


test_phrase = 'This is a string with numbers 12312 and a symbol #hashtag'

test_patterns = [r'\d+']


print(test_patterns)
multi_re_find(test_patterns, test_phrase)
