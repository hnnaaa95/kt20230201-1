N = input("N을 입력하세요:")
step2 = '100'
count = 0
goal= N
while step2!=goal:
    if len(N)>=2:
        step1=str(int(N[0])+int(N[-1]))
        step2=str(int(N[-1]+step1[-1]))
        N=step2
        count+=1
    else:
        step2= str(int(N[-1]+N[-1]))
        N=step2
        count+=1
    
print(count)
