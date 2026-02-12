ascii_art = '''
.       .
                                                    \     /
                                                 ._  '   '  _.
                                                   '  o@o  '
                                                     o@@@o
                                                 .-'  o@o  '-.
                                                     .   .
                                                    /     \
                                                   .       .

                             'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            /ssssssss.
                      /sssssssSSSSssssssssss.
        /\         /sssssSSSSSSSSSSSSSSSssssssssssss.              Dani
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''

prompts ={
    "welcome": "Welcome to Treasure Island.\n Your mission is to find the treasure.",
    "gameover": "Game over.",
    "youwin": "You Win!",
    "leftright": "Left or right? ",
    "fall": "Fall in a hole.\n Game over.",
    "swimorwait": "Swim or wait? ",
    "attacked": "Attacked by trout.\n Game over.",
    "whichdoor": "Which Door? Tell me the color. ",
    "burned": "Burned by fire.\n Game over.",
    "eaten": "Eaten by beasts. Game over.",
}

def get_prompt(id):
    '''
    This function retrieves the text of the prompt based on the id
    
    :param id: Description
    '''
    output = prompts[id]
    return output

# The game starts here
print(ascii_art, "\n")
print(get_prompt("welcome"))
leftright = input(get_prompt("leftright")).lower()
if leftright != "left":
    print(get_prompt("fall"))
else:
    swimorwait = input(get_prompt("swimorwait")).lower()
    if swimorwait != "wait":
        print(get_prompt("attacked"))
    else:
        whichdoor = input(get_prompt("whichdoor")).lower()
        if whichdoor == "blue":
            print(get_prompt("eaten"))
        elif whichdoor == "red":
            print(get_prompt("burned"))
        elif whichdoor == "yellow":
            print(get_prompt("youwin"))
        else:
            print(get_prompt("gameover"))

    