"""
1: 1 (세로)
2: 1+1+1 (세로세로)+(가로가로)+(2x2)
방법(n) = 방법(n-1) + 방법(n-2) * 2
(방법(n-1)에서 끝에 세로로 하나 추가) + (방법(n-2)에서 끝에 가로2개로 추가) + (방법(n-2)에서 끝에 2x2로 추가)
"""
n = int(input())
a = [0, 1, 3]   # a[n]은 2xn 크기의 직사각형을 채우는 방법의 수
for i in range(3, n + 1):
    a.append(a[i-1] + a[i-2]*2)
print(a[n] % 10007)