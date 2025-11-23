name=input("enter your good name : ")
print(f"hiiiii " + name +"!")
print("lets write our to-do list ")
print(f"shall we start {name} ? ")
permission=input("press yes or no: ")
if permission == "yes":
    print("how many blocks u want? ",end=(""))
    num=int(input())
    x=1
    while x<=num:
        print(f"{x})\t",)
        a=input("\n")
        x+=1
elif permission == "no":
    print("see you , next time!")

        

