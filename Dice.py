import random
Dice1 = {}
Dice2 = {}
Dice3 = {}
win1 = 0
win2 = 0
win3 = 0

print('-'*75)
print("""
                    <주사위 놀이를 하자>
    총 3개의 주사위 숫자를 다음과 같이 띄어쓰기로 구분해서 입력해주세요. 
    (*주의-마지막에는 엔터를 입력해주세요*)
    (ex)Dice : 1 2 3 4 5 6
        """)
print('-'*75)

# 각각의 주사위 눈을 입력받는 부분
# input은 컴퓨터 자판으로 입력받는 함수
# split("")은 큰따옴표("") 내부에 있는 기호로 입력 받은 문자를 나누어 입력받는 함수
print("Dice1 : ")
Dice1 = input().split(" ")  # '1 2 3'을 입력하면 띄어쓰기로 구분하여 '1','2','3'으로 나누고 배열에 저장
print("Dice2 : ")
Dice2 = input().split(" ")
print("Dice3 : ")
Dice3 = input().split(" ")
print("How many times do I want to run? : ")

n = int(input()) # 입력받은 수를 int형으로 n에 저장
print(' ')
for i in range(1, n+1): # n번 반복 시행
    a = random.choice(Dice1) # DIce1 배열의 요소 중 무작위로 하나 뽑아 a에 저장
    b = random.choice(Dice2)
    c = random.choice(Dice3)
    if a > b and a > c: # 만약 a가 b와 c보다 크다면
        win1 = win1+1 # win1의 값을 1 증가
    elif b > c and b > a:
        win2 = win2+1
    elif c > a and c > b:
        win3 = win3+1
    print("%d번째 시도 : %c | %c | %c" % (i, a, b, c))

print("Dice1 Win : %d" % win1)
print("Dice2 Win : %d" % win2)
print("Dice3 Win : %d" % win3)
print("각각의 확률 : %f | %f | %f" % (win1/n, win2/n, win3/n))
input()
