with open("nex.txt","w") as f:
    f.write("Hello from python's files \n")
    f.write("I am in the next line")
    f.write("Good Day everyone once again")
with open("nex.txt","r") as f:
    content=f.read()
    print(content)
with open("nex.txt","a") as f:
    f.write("\n")
    f.write("Hello noones getting deleted")
    f.write("\nDod any one get deleted")