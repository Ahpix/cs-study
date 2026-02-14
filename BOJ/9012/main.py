n = int(input())

for i in range(n):
    stack = []
    ps = input()
    for j in ps:
        if j == "(":
            stack.append(j)
        else:
            if not stack:
                print("NO")
                break
            stack.pop()       
    else:
        if stack:
            print("NO")
        else:
            print("YES")
