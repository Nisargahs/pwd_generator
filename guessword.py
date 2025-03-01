def game():
    word="tiger"
    tries_left =10 
    while tries_left:
        given = str(input("make a given\n"))
        status=compare(word,given)
        if status=='=':
            print("you win!!")
            break
        tries_left -=1
        print(f"my word doesnot contain {status} your given")

    else:
        print(f"you lost.my word was {word} ") 
 

def compare(computer_word,given):
    if computer_word ==given:
        print(f"letter is present ")
    elif computer_word>given:
        return(f'letter is not present')
    
game()