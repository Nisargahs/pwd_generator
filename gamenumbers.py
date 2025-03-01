import random 

def fixnumber(start=100,stop=200):
    return random.randint(start,stop)


def game():
    num=fixnumber ()
    tries_left =10 
    while tries_left:
        given = int(input("make a given\n"))
        status=compare(num,given)
        if status=='=':
            print("you win!!")
            break
        tries_left -=1
        print(f"my number is {status} your given")
    else:
        print(f"you lost .my number was {num} ") 
 

def compare(computer_num,given):
    if computer_num <given:
        return'<'
    elif computer_num>given:
        return'>'
    return '='


game()