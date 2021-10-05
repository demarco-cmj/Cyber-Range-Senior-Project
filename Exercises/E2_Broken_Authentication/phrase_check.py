import settings

#Requests input until the correct phrase is entered
while (1):
    phrase = input()
    if (phrase == settings.phrase):
        print("Stage Completed. Good Job.")
        break
    else:
        print("Incorrect phrase. Try again.")