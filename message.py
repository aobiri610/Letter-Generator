print("Hello. Welcome to the letter writing System. Enter a key depending on the type of letter you would like to write. Here are the options:")
print("(A) for apology letter \n(B) for congratulatory letter\n(C) for sympathy leter\n(D) for thank you letter")
print("(E) birthday letter")

choice = input()
words = []
fill_start = "["
fill_end = "]"
start = -1
provided = {}
message = ""
f = open("mess.txt", "w")
if choice.upper() == "A":
    
    message = "I am writing this message to apologize for my actions on [incident time]. I deeply regret my behavior and the [effect] I caused you. I understand that what I did was wrong, and I promise to learn from this mistake and make amends. I value our [relationship], and I hope you can find it in your heart to forgive me. If there's anything I can do to make things right, please let me know. Again, I am sincerely sorry for [behavior], and I will do my best to ensure that it doesn't happen again in the future."
    print("You have selected \"Apology Letter.\" Here is a template:\n" + message + "\n")
    for i, char in enumerate(message):
        if char == fill_start:
            start = i
        if char == fill_end and start != -1:
            word = message[start: i+1]
            words.append(word)
            start = -1
    for word in words:
        given = input("Please fill in the blank for " + word + ": ")
        provided[word] = given
        message = message.replace(word, provided[word])
    print("Here is your message:\n" + message)

if choice.upper() == "B":
    message = "Congratulations on your [achievement]! You have worked incredibly hard, and your dedication has paid off. This accomplishment is a testament to your [skills] and determination.I have always admired your [admirable factor], and it's inspiring to see you reach new heights. May this milestone be the beginning of even greater achievements in your life. I have no doubt that you will continue to excel and make a positive impact on those around you."
    print("You have selected \"Congratulatory Message.\"Here is a template: \n" +message + "\n")
    for i, char in enumerate(message) :
        if char == fill_start:
            start = i
        if char == fill_end and start != -1:
            word = message[start: i+1]
            words.append(word)
            start = -1
    for word in words:
        given = input("Please fill in the blank for "+ word + ": ")
        provided[word] = given
        message = message.replace(word, provided[word])
    print("Here is your message:\n" + message)

if choice.upper() == "C" :  
    message = "I am deeply saddened to hear about [situation]. Words cannot fully express the sorrow I feel for your [issue]  During this period of grief, please know that you are not alone. I am here for you, and if there's anything I can do to provide comfort or support, please don't hesitate to reach out. Wishing you [wishes] during this difficult time." 
    print("You have selected \"Sympathy Message.\"Here is a template: \n" +message + "\n")
    for i, char in enumerate(message) :
        if char == fill_start:
            start = i
        if char == fill_end and start != -1:
            word = message[start: i+1]
            words.append(word)
            start = -1
    for word in words:
        given = input("Please fill in the blank for "+ word + ": ")
        provided[word] = given
        message = message.replace(word, provided[word])
    print("Here is your message:\n" + message)

if choice.upper() == "D" :
    message = "I wanted to take a moment to express my heartfelt gratitude for your [word]. Your [gesture/gift] has meant so much to me and has made a significant difference in my life.It is evident that you genuinely care about others, and I feel incredibly fortunate to have you as [a type of person] in my life. Once again, thank you for everything."
    print("You have selected \"Thank You Message.\"Here is a template: \n" +message + "\n")
    for i, char in enumerate(message) :
        if char == fill_start:
            start = i
        if char == fill_end and start != -1:
            word = message[start: i+1]
            words.append(word)
            start = -1
    for word in words:
        given = input("Please fill in the blank for "+ word + ": ")
        provided[word] = given
        message = message.replace(word, provided[word])
    print("Here is your message:\n" + message)
if choice.upper() == "E":
    message = "Happy Birthday [Name]! On this special day, I want to send you the warmest wishes and the biggest smiles. May your birthday be filled with [positive terms], and all the things that make you happy. Another year older, another year wiser, and with each passing year, you continue to shine brighter. You are an amazing [relation], and I feel so fortunate to have you in my life. May this new year bring you [wishes].Happy Birthday once again! I hope this day brings you all the happiness your heart can hold."
    print("You have selected \"Happy Birthday Message.\"Here is a template: \n" +message + "\n")
    for i, char in enumerate(message) :
        if char == fill_start:
            start = i
        if char == fill_end and start != -1:
            word = message[start: i+1]
            words.append(word)
            start = -1
    for word in words:
        given = input("Please fill in the blank for "+ word + ": ")
        provided[word] = given
        message = message.replace(word, provided[word])
    print("Here is your message:\n" + message)

print("\nThank you for using the message generator system. Your message has been written to a file named \"mess.txt")
f.write(message)
f.close()


  
