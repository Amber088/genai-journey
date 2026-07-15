#Task1 
# f = open('MyFile.txt','w')
# f.write("Amber Jain\nBITS\nAIML")
# f.close()
# f = open('MyFile.txt','r')
# txt = f.read()
# print(txt)

#Task2
f = open('MyFile.txt','w')
f.write("Python\nMachine Learning\nGen Ai")
f.close()
with open("MyFile.txt",'r') as file:
    lines = file.readlines()
print(lines[1])

