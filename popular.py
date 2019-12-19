import requests
import bs4

html = requests.get('https://www.naver.com/')
soup = bs4.BeautifulSoup(html.text,'html.parser')

tests = soup.select('span.ah_k') #tag가 span 이면서 ah_k는 class 인 데이터

# tests배열을 하나부터 열까지 다 돌면서 test에 문자열 삽입 for문
#for test in tests:   
#   print(test)

# 배열 [0:n] -> 배열의 0번째 인덱스부터 n-1번째 인덱스들의 요소를 가져와 배열 생성
real_keywords = tests[0:20]
#print(real_keywords)

# 참고
#numbers = [i for i in range(0,101)]
#print(numbers)

real2_keywords = [keyword.text for keyword in real_keywords]
#print(real2_keywords)

problem = sorted(real2_keywords)

print('아래의 보기 중 1위를 고르시오')
print(problem)
answer = input('당신이 입력한 답 :')

if answer == real2_keywords[0]:
    print('정답')
else :
    print('오답')

