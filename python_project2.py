import random

# convert the names to numbers

def name_to_number(name):
    if name=='rock':
        number=0
        
    elif name=='Spock':
        number=1
    
    elif name=='paper':
        number=2
        
    elif name=='lizard':
        number=3
        
    elif name=='scissors':
        number=4
        
    else:
        number=none
        print "Invalid name for converting!"
    
    return number

# convert number to name

def number_to_name(number):
    if number==0:
        name='rock'
        
    elif number==1:
        name='Spock'
        
    elif number==2:
        name='paper'
        
    elif number==3:
        name='lizard'
        
    elif number==4:
        name='scissors'
        
    else:
        name=none
        print "Invalid number for converting!"
        
    return name

def rpsls(player_choice):
# player_choice can be one of rock, paper, lizard, scissors
# and Spock
    print "Player chooses",player_choice
    player_number=name_to_number(player_choice)
    comp_number = random.randrange(5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses",comp_choice
    decision = (comp_number+5-player_number)% 5
    if comp_number == player_number:
        print "Player and computer tie!"
    elif decision>2 and decision<=4:
        print "Player wins!"
    elif decision<=2 and decision>0:
        print "Computer wins!"
        
    else:
        print "Invalid output"
        
    print""
    print""
rpsls('rock')
rpsls('Spock')
rpsls('paper')
rpsls('lizard')
rpsls('scissors')
    
    
