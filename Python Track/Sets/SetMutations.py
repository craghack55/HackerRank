_, a = input(), set(input().split())

for _ in range(int(input())):
    op, *nums = input().split()[0], input().split()
    getattr(a, op)(*nums)

print(sum(map(int, a)))