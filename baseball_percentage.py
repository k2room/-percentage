import random

def Strike(num, ans): # 스트라이크 개수를 판별하는 함수
    st = 0
    for i in range (0,3): # 각각의 자리수를 비교하여 같으면 st를 1 증가시킨다
        if ans[i] == num[i]:
            st += 1
    return st

def Ball(num, ans): # 볼의 개수를 판별하는 함수
    ba = 0
    for i in range (0,3):
        for j in range (0,3):
            if num[i] == ans[j]:
                ba+=1
    return ba

def check():
    print("몇 회 반복시행 하시겠습니까? : ", end='')
    n = int(input())
    # result 배열은 결과 저장; 순서대로 out, 1S, 1B, 2S, 2B, 1S 1B, 3S, 2S 1B, 1S 2B, 3B의 결과값 저장
    #result = ['0','0','0','0','0','0','0','0','0','0']
    result = [0,0,0,0,0,0,0,0,0,0]
    for i in range(1,n+1):
        ans = random.sample(range(1,10),3) # 무작위로 정답 생성
        num = random.sample(range(1,10),3) # 무작위로 예측하는 답 생성

        st = Strike(num, ans) # 스트라이크의 개수를 저장한다
        ba = Ball(num, ans) - st # 볼의 개수를 저장한다

        print('%d번째 시행 : %d S | %d B'%(i, st, ba)) # 스트라이크, 볼의 개수를 차례로 출력한다

        if(st==0):
            if(ba==0):
                result[0] += 1
            elif(ba==1):
                result[2] += 1
            elif(ba==2):
                result[4] += 1
            elif(ba==3):
                result[9] += 1
        elif(st==1):
            if(ba==0):
                result[1] += 1
            elif(ba==1):
                result[5] += 1
            elif(ba==2):
                result[8] += 1
        elif(st==2):
            if(ba==0):
                result[3] += 1
            elif(ba==1):
                result[7] += 1
        elif(st==3):
            result[6] += 1

    print('''
        out   : %d        
        1S    : %d 
        1B    : %d        
        2S    : %d
        2B    : %d        
        1S 1B : %d
        3S    : %d        
        2S 1B : %d
        1S 2B : %d        
        3B    : %d
    '''%(result[0], result[1],result[2], result[3],result[4], result[5],result[6], result[7],result[8], result[9]))

play_again = 'yes'
while play_again == 'yes' or play_again == 'y':
    check()
    play_again = input('Do you want to play again? (y/n): ')
