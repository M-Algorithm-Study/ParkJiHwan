n = int(input())
print(sum([(3*x - n+2)//2 for x in range((n+1)//3, (n+1)//2)]))