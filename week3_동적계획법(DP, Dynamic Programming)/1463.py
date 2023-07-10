"""
1 : 0
2->1 : 1
3->1 or 3->2 : 1 or 1+1=2
4->2 or 4->3 : 1+1=2 or 1+1=2
5->4 : 1+2=3
6->2 or 6->3 or 6->5 : 1+1=2 or 1+1=2 or 1+3=4
7->6 : 1+2=3
8->4 or 8->7 : 1+2=3 or 1+3=4
9->3 or 9->8 : 1+1=2 or 1+3=4
10->5 or 10->9 : 1+3=4 or 1+2=3
10은 2로 나누어 떨어지지만 1을 빼는 것을 먼저해야 연산이 최소 ..?
11->10 : 1+3=4
11처럼 2나 3으로 나누어 떨어지지 않으면 일단 무조건 1 빼기
12->4 or 12->6 or 12->11 : 1+2=3 or 1+2=3 or 1+4=5
13->12 : 1+3=4
14->7 or 14->13 : 1+3=4 or 1+4=5
15->5 or 15->14 : 1+3=4 or 1+4=5
다 비교 해봐야 되나 ..?
"""
N = int(input())
a = [0] * (N + 1)   # a[N]은 정수 N을 1로 만드는 최소연산횟수
for i in range(2, N + 1):
    if i % 3 == 0:
        if i % 2 == 0:
            a[i] = min(a[i-1], a[i//3], a[i//2]) + 1
        else:
            a[i] = min(a[i-1], a[i//3]) + 1
    else:
        if i % 2 == 0:
            a[i] = min(a[i-1], a[i//2]) + 1
        else:
            a[i] = a[i-1] + 1
print(a[N])