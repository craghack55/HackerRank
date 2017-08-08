n = raw_input()
elements = list(map(int, raw_input().split()))

print all(i > 0 for i in elements) and any(str(i) == str(i)[::-1] for i in elements)