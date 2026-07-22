score = 0
print("wlecome to the quiz")
ans = input("Q1. What is the capital of India: ")
if ans.lower()=="delhi":
    print("Correct!")
    score +=1
else:
    print("Wrong!")

ans = input("Q2. Best Captain of India: ")
if ans.lower() == "rohit sharma":
     print("Correct!")
     score+=1
else:
     print("Wrong!")

ans = input("Q3. 2+2 = ?: ")
if ans.lower() == "4":
     print("Correct!")
     score+=1
else:
     print("Wrong!")

print("\nYour Score:", score, "/3")

