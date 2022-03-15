import sys

read = sys.stdin.readline

arr = list(map(str, read().strip()))

stack = []
postfix = []

isp = { '(' : 0 , '*' : 2, '/' : 2, ')' : 0 , '+' : 1 , '-' : 1  }
icp = { '(' : 3 , '*' : 2, '/' : 2, ')' : 0 , '+' : 1, '-' : 1 }
print(arr)
for word in arr:
    if word.isdigit() :  #숫자일 경우 무조건 append
        postfix.append(word)
    else: # 수식일경우
        if len(stack) < 1 : # 스택에 아무값도 없으면 append
            stack.append(word)
        else: # 스택에 값이 있으면 비교
            if word == ')': # 들어오는 수식이 끝나는 괄호이면
                while stack: # ( 가 나올때까지 pop해서 post배열에 넣는다.
                    if stack[-1] != '(' :
                        postfix.append(stack.pop())
                    else:
                        break
                stack.pop() # 괄호 pop
            else: # 괄호가 아닌 수식이 들어올 경우
                while stack:
                    if isp[stack[-1]] < icp[word] : # 비교하여 우선순위가 큰 수식이 append
                        stack.append(word)
                        break
                    else: # 비교해서 stack 최상위 값이 들어오는 값보다 우선순위가 작을 때까지 pop
                        postfix.append(stack.pop())
#남아있는 stack의 값을 모두 pop
while stack:
    postfix.append(stack.pop())


print(postfix)
