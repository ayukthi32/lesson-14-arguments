#acp
def shutdown():
    user_input = input("Do you want to shut down?")
    if user_input=="yes":
        print("shutting down")
    elif user_input=="no":
        print("abort shutting down")
    else:
        print("sorry")
    
shutdown()