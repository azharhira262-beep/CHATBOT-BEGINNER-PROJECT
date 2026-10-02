#PERSONAL CHATBOT ASSISTANT 
print("Welcome to  CHATBOT ASSISTANT")
print("LET'S TALK,BUDDY!!")
print(" type bye to exist!!")


responses= {"hello":"hy","how are you":"i am fine wht about you!",
          "what is your name":"i am your chatbotBUDDY",
          "what is name of country":"pakistan",
          "what is your fvrt colour": "black color is my fvrt"}

def getbotresponse(userinput):
    userinput=userinput.lower()
    for eachkey in responses:
        if eachkey in userinput:
            print("You:",eachkey)
            return responses[eachkey]
    return "i dont know this i will learn soon"


while True:
    usercall = input(" buddy ask me a question:")
    
    if "bye" in usercall.lower():
        print("Bye buddy! See you SoOn")
        break
    reply = getbotresponse( usercall)
    print("chatbot:", reply)





