if __name__ == '__main__':
    N = int(input())

    result = []
    for i in range(0, N):
        commands = map(str, raw_input().strip().split(' '))
        
        if commands[0] == "print":
            print result
        else:
            if commands[0] == "insert":
                result.insert(int(commands[1]), int(commands[2]))
            elif commands[0] == "remove":
                result.remove(int(commands[1]))
            elif commands[0] == "append":
                result.append(int(commands[1]))
            elif commands[0] == "sort":
                result.sort()
            elif commands[0] == "pop":
                result = result.pop()
            elif commands[0] == "reverse":
                result = result.reverse()
