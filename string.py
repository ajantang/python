# 명단에서 이름을 뽑나서 영어 소개와 한글 소개 작성

import random

name = ['홍','희동','둘리']
eng_name = {
    '홍':'hong',
    '희동':'dong',
    '둘리':'dul'
}

지목된사람 = random.choice(name)
지목된영어이름 = eng_name[지목된사람]

intro = '저는 '+지목된사람+'입니다. '+'My name is '+지목된영어이름
intro2 = '저는 {}입니다. My name is {}'.format(지목된사람, 지목된영어이름)
intro3 = f'저는 {지목된사람}입니다. My name is {지목된영어이름}'

print(intro)
print(intro2)
print(intro3)
