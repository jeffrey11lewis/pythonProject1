print('this is the story of finding the meaning of life.\n')
def gameOver(reason):
        print("\n" + reason)
        print('game OVER.')
        playAgain()

def playAgain():
        print("play again? y or n")
        answer = input(">").lower()
        if "y" in answer:
                openingLines()
        elif "n" in answer:
                exit()
        else:
                exit()

def openingLines():
        print('You wake up late at night and decide to head outside to smell the fresh air.')
        print('Once you get outside, you have a choice to make.\n')

        print('should you:')
        print('1. reflect on your life decisions')
        print('2. draw a zebra on the sidewalk with chalk')

        answer = input(">")

        if answer == "1":
                print('you decide that all of the decisions you have made in life are incorrect and you leave to find yourself')
                gameOver("you find yourself lost somewhere in a third-world country. night is approaching and you've run out of time. bummer.")

        elif answer == "2":
                print('YAY. you now understand that not everything in life is as serious as it is made out to be and choose to go to sleep.\n')
                scenarioTwo()
        else:
                print('please enter only "1" or "2".\n')
                openingLines()

def scenarioTwo():
        print("after drawing your zebra and getting a good night's rest, you get up and get in the car.")
        print("you get a bit down the road when a guy cuts you off and flips you the bird.")
        print("\n you have a choice to make. \n")
        print("should you:")
        print("1. retaliate and rear end them off the road")
        print("2. make a heart with your hand and play some Bobby McFerrin (the greatest musician of all time)")

        answer = input(">")

        if answer == "1":
                print("you rear end the man just to find out he's an undercover FBI Agent.")
                print("did you not learn ANYTHING from your zebra last night..? *sigh*")
                scenarioThree()
        elif answer == "2":
                print("you look at your phone to find 'don't worry, be happy' on your Spotify playlist and end up running yourself off the road.")
                gameOver("never thought i'd say this, but it seems like you should've rear ended that guy.")

        else:
                print('please enter only "1" or "2".\n')
                scenarioTwo()
def scenarioThree():
        print("you're approaching 200mph quickly; lights and sirens are blaring behind you, but you might just get away at this rate.")
        print("a turn is coming up")
        print("\nshould you:")
        print("1. take the turn that's coming up")
        print("2. slow down, stop your vehicle, step out, and reason with the agent")

        answer = input(">")
        if answer == "1":
                print("you take the turn and end up finding a spot to hide. you hang around to let the dust settle a bit.")
                scenarioFour()
        if answer == "2":
                print("...seriously? did you actually think this would work??")
                print("the FBI agent runs you over. twice. that was a terrible idea.")
                gameOver("i have no words.")
        else:
                print('please enter only "1" or "2".\n')
                scenarioThree()
openingLines()



