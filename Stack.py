#In this program we are going to use deque from collections to implement stack
from collections import deque

#Creating a Stack using deque instance

s=deque()

#Appending Operations

while True:
    print()
    print("1.To Push element to top of Stack.")
    print("2.To Pop element from the Stack.")
    print("3.To View the contents of the Stack.")
    print("4.To exit.")
    print()
    inp=int(input("Enter your choice"))
    print()
    if(inp==1):
        print()
        n=int(input("Enter element to be pushed"))
        s.append(n)
        print("Stack after pushing element")
        print(s)
    elif(inp==2):
        print()
        print("Element popped out of stack is")
        print(s.pop())
        print("Stack after popping of element is")
        print(s)
    elif(inp==3):
        print()
        print("The contents of the Stack are")
        print(s)
    elif(inp==4):
        print()
        print("Exited!!Thank You!!!")
        break
    else:
        print()
        print("Enter Correct Input!!")
        continue
