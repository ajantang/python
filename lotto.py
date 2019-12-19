import random

lotto = range(1,46)

number = random.sample(lotto, 6)

number.sort() # 정렬 결과 저장
sorted(number) # 정렬 결과 미저장
print(number)

#alt + shift + 위 or 아래 -> 줄복사
#alt + 위 or 아래 -> 코드 줄이동