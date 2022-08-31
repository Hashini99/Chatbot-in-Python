def welcome(bot_name,birth_year):
    print("Hello! I'm {0}.".format(bot_name))
    print("I was created in {0}. ".format(birth_year))

def guest_name():
    print('What is your name.')
    name=input()
    print("What a pretty name you have {0}!".format(name))

welcome('ABC','2022')
guest_name()