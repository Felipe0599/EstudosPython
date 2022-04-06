A, B, C = map(int, input().split(" "))


maior = A

if B > maior:
    maior = B
if C > maior:
    maior = C


print(maior, "eh o maior")