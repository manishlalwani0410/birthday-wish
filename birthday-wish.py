from datetime import date
today = date.today()
print("\n\n\t\tBirthday wish From Manish Lalwani\n\n")
print(f"It's {today}. Ohhhh Wait a Minute is That.... Okay Here We Go.....\n\n\n\n")
letter = '''Hello, <|NAME|>
It is Your Birthday.  
It's Time to Party and Make Your Birthday as Special as You Are! 
I Hope Your day is Fantastic, and The Year Ahead is Even Better Still. 
Happy birthday <|NAME|>!
Let Me Present You Something Press 1 to Get a Virtual Cake Press 2 to Get a Virtual Card 
'''
cake = ''' 
    Ƹ̵̡Ӝ̵̨̄Ʒ                Ƹ̵̡Ӝ̵̨̄Ʒ
           ,,,,,,,,,,
           ||||||||||
        @@@@@@@@@@@@@@@@
        ################
        @@@@@@@@@@@@@@@@
        ################
    Ƹ̵̡Ӝ̵̨̄Ʒ                Ƹ̵̡Ӝ̵̨̄Ʒ
'''
card = '''
    Ƹ̵̡Ӝ̵̨̄Ʒ                  Ƹ̵̡Ӝ̵̨̄Ʒ
        #################
        #     happy     #
        #     birth     #
        #      day      #
        #     🤗🥰     #
        #     😜😝     #
        #################
    Ƹ̵̡Ӝ̵̨̄Ʒ                  Ƹ̵̡Ӝ̵̨̄Ʒ
'''
extra = '''
Here's a Beautiful Swoard to Cut Cake 
        |
        |
        |
        |
        |
      | | |
      |___|
        |
        |
\n\n\n
'''

rose = '''Here's a Ugly Rose for a Beautiful people
                  ▒███░   ░████████▒
               █████▒░█████░▒▒▒▒▒▒█████
              ██▒▒▒▒██████████████▒▒▒██░
             ██▒▒▒▒███▒██▒██▒▒█████▒░▒██
             █░▒▒▒██▒████████████▒█▒▒▒█░
             █▒▒▒▒██▒▒▒░▓▓▒░▓▒▒████▒▒██
             █▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒█▒█░▒████
         ███████████▒▒▒▒▒▒▒▒██████▒██▓▒███
         ██▒▒▒▒▒▒█████▒▒▒▒▒▒▒▒█████▒▒▒▒▒██
           ██▒▒▒▒▒▒▒▓██████▒▒▒▒▒██▒▒▒▒▒▒███
        █████▒▒▒▒▒▒▒▒▒▒████▒▒▒██▒▒▒▒▒▒███
        ██▒▒▒███▒▒▒▒▒▒▒▒▒▒▓█████▒▒▒▒▒███
        ███▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒███▓▒▒███
          █████▒▒████▒▒▒▒▒▒▒▒▒▒█████
             ████▒▒██████▒▒▒▒█████
                ███▒▒██████████
                  ████▓──█▓█
                        ████
                        █░█     █████████
                        █▓█   █████████████
      ░█████████       ████  ██▓███▒▓████
     █████████████     █░███████░██████
       ████░▒███▒██    █▓██████████
         █████▓▒█████─████
             ██████████▓█
                      █▓█    ████▒█▓▒█
                     █▓██  █████████████
                     █▓█  ██▒████░█████
                    ██████████▒██████
                    █▓███████████
                   ████
                   █▒█
                   ███
\n\n\n
'''
playstation = '''
Here's a controller of ps 
     ▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄
    █░░░█░░░░░░░░░░▄▄░██░█
    █░▀▀█▀▀░▄▀░▄▀░░▀▀░▄▄░█
    █░░░▀░░░▄▄▄▄▄░░██░▀▀░█
     ▀▄▄▄▄▄▀─────▀▄▄▄▄▄▄▀
\n\n\n
'''

teddy = '''
Here's a cute teddy bear for you
   ▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄
   █▒▒░░░░░░░░░▒▒█
    █░░█░░░░░█░░█
 ▄▄  █░░░▀█▀░░░█  ▄▄
█░░█ ▀▄░░░░░░░▄▀ █░░█
\n\n\n
'''

cats='''
Here's a cute Cats for you
    /\__/\  /\__/\\
    (=o.o=) (=o.o=)
    | \_\_/ \_/_/ |
    \_(“)(“) (“)(“)_/
'''
name = input("Enter Your Name(I know Your Name But This Device Doesn't): ")
letter = letter.replace("<|NAME|>", name)
print(letter)
val = int(input("I know You Wanted to Enter Both But Enter Anyone First😂🤣: "))
if(val == 1):
    print("Why I've Created Card with too much hard work😣😔\nOkay leave it... It's your bday Enjoy")
    print(cake)
    print(extra)
elif(val == 2) :
    print("Awww thanks For opening card it's really sweet.... Might this card is not to much high but belive me It's from my bottom of my heart😉🤣")
    print(card)
else:
    print("You are too wierd I've alredy said only 1 & 2 then why different number😶🤕😡")

val1 = int(input("now enter second one😂🤣: "))
if(val1 == 1):
    print(cake)
    print(extra)
elif(val1 == 2):
    print("Might card is not to much high but belive me It's from my bottom of my heart🤣")
    print(card)
else:
    print("You are too wierd I've alredy said only 1 & 2 then why different number😶🤕😡")
print("What do you want a teddy(1), a rose(2), a playstation controller(3), or pair of cats(4)")
gift = int(input("Enter number corspoinding to thing which you want:"))
if (gift == 2):
    print (rose) 
elif (gift == 1):
    print(teddy)
elif (gift == 4):
    print(cats)
elif (gift == 3):
    print(playstation)
else:
    print("Enter a vaild opition.....")