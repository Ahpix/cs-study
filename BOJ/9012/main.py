n = int(input())
isChecked = False

for i in range(n):
    stack = []
    ps = input()
    isChecked = False
    for j in ps:
        if j == "(":
            stack.append(j)
        else:
            if not stack:
                print("NO")
                isChecked = True
                break
            stack.pop()       
    if stack:
        print("NO")
    else:
        if isChecked:
            continue
        else:
            print("YES")
