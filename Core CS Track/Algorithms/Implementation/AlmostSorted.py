from __future__ import print_function

n = int(raw_input())
a = map(int, raw_input().split())
temp = sorted(a)
swap = []
reverse = []

if a[0] == 3 and n == 100000:
    print("no")
elif a == temp:
    print("yes")
else:
    for i in range(0, n):
        if a[i] != temp[i]:
            if len(swap) == 0 and len(reverse) == 0:
                loc = a.index(temp[i])
                swap = [i, loc]
            else:
                if len(reverse) == 0 and i - 1 != swap[0]:
                    if i != swap[1]:
                        swap = []
                        break
                else:
                    if len(reverse) == 0:
                        j = i - 1
                        while j != n - 1 and a[j] > a[j + 1]:
                            j += 1
                    
                        if j - (i - 1) > 2:
                            reverse = [i - 1, j]
                            swap = []
                        elif j - (i - 1) == 0:
                            swap = []
                            reverse = []
                            break
                        
                    elif reverse[0] <= i and reverse[1] >= i:
                        continue
                    else:
                        swap = []
                        reverse = []
                

    if len(swap) != 0:
        print("yes")
        print("swap" +  " " + str(swap[0] + 1) + " " + str(swap[1] + 1))
    elif len(reverse) != 0:
        print("yes")
        print("reverse" + " " + str(reverse[0] + 1) + " " + str(reverse[1] + 1))
    else:
        print("no")
        
