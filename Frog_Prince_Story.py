# Add your program code here.
def main():
    print("Welcome to The Frog Prince!")
    print("Before the story beings, please answer a few questions.")
    print("After typing your answer, please hit Enter.")
    keepPlaying = "yes"
    while keepPlaying.lower() == "yes":
        name = input("What's your name, adventurer? ")
        gem = input("What's your favorite kind of gem? " )
        monster = input("What's scarier, a werewolf or a troll? ")
        weapon = input("If you had to fight, would you rather have a rock or a stick? ")
        gender = input("Are you a boy, a girl? ")
    
        print(f"Thank you for your responses, {name}.")
        print("Mom and Dad were fighting again.") 
        print("As you listened to them scream, yell, and throw things, you decide you've had enough.")
        print("You open your window, climb out onto the oak tree growing beside your house, and climb down, jumping the last few feet and landing softly on the grass.")
        print("You glance at the setting sun as you make your way towards the woods.")
        print("The sounds of your parents' screaming fades as you disappear past the treeline.")
        print("The sun dips below the horizon as you make your way into the forest.")
        print("As you walk down the path, you hear strange sounds in the distance; they get louder the deeper you go.")
        print("As you round the bend you come upon a snake, hissing at the toad he's trapped in the coils of his body. You stop and stare, and to your astonishement, the frog begins to speak!")
        print(" 'Please help me', the frog croaks frantcially. 'I'm not an ordinary frog, and this evil snake is trying to kill me!' ")
        print(f"'Turn around and go back from where you came, little {gender}! Something even worse than me is coming!")
        action_1 = input("Do you run, or do you try to help?: ").lower()
        if action_1 == "run":
            print("The talking frog and the talking snake are just too much for you to deal with.")
            print("You spin on your heel and sprint back down the path. The woods have gotten dark, and you never see the tree branch until you trip over it.")
            print("Your ankle throbs, and when you look up you see a fork in the path that you didn't notice before.")
            print(f"You hear the snake's hisses echoing, 'Better hurry! The {monster} is close by, and she's hungry!'")
            action_1a = input("Do you go right or left? ")
            if action_1a == "right":
               print("You run for what feels like hours, until you finally emerge from the treeline and see your house. As your parents scream at you, you wonder what happened to the frog, and what would have happened if you'd decided to help him. The End.")
            elif action_1a == "left":
                print(f"You get up and run, trying to ignore your throbbing ankle. In the distance, you hear crashing and grunting and wonder if it's the {monster} the snake threatened you with. You're still wondering when something crashes into you from behind. As it gobbles you up you realize that it doesn't matter. The end.")  
            else:
                print(f"As you lay there trying to decide, a {monster} springs out down from the treetops and lands on your back. The stench of its breath is the last thing you ever smell. The End.")     
        elif action_1 == "help":
            print(f"Looking around quickly, you spot a {weapon} and snatch it up, swinging it at the snake. It hisses in rage and pain, quickly uncoiling and slithering away.")
            print("'Nice shot!', croaks the frog. 'But that snake wasn't joking. There is something much worse coming. Pick me up and run exactly where I tell you!")
            action_2 = input("If you follow the frog's instructions, hit 1 and press enter. If you have questions, hit 2 and press enter.")
            if action_2 == "2":
                print(f"'Slow down there.' you say. 'First, tell me why-' But suddenly, a huge {monster} comes crashing out of the forest. The last thing you see before you're eaten is the frog, hopping away with its life. The end.")
            elif action_2 == "1":
                print("You pick up the frog and begin to run. He croaks 'Right!' 'Left!' And as you follow his directions you notice something funny.")
                print("You seem lighter and faster than you ever have before. You run for what seems like hours, without getting tired. And even though it's completely dark, you see every branch and every rock in your path. You don't trip or stumble once.")
                print("Finally, the frog leads you to a cave, its entrance concealed by bushes on a hillside. 'Tell me your name,' he says.")
                print(f"'My name is {name},' you reply.")
                print(f"'Thank you for saving me, {name}. I'm not really a frog, but an elf who was placed under a curse.'")
                print("'Will you help me return to my true form and save my kingdom?'")
                action_3 = input("If you decide to help the elven frog, press 1. If you refuse, press 2. ")
                if action_3 == "1":
                    print(f"'Thank you, {name}, I knew you were brave the moment I laid eyes on you. Take this {gem} as a symbol of your agreement.")
                    print(f"The time will come when this {gem} may save us both. To be continued...")
                elif action_3 == "2":
                    print(f"'Of course, {name}, you've already saved me once. I can't ask you to do it again. Take this {gem} as token of my gratitude. It will keep you safe and guide you home.' The End") 
                else:
                    print("You hesitate, unable to make up your mind. Finally, the frog says, 'I'm sorry. Maybe you're not the one I was hoping for.'")
                    print("And with that he hops out of the cave and into the night. The End.") 
        keepPlaying = input("Would you like to keep playing?").lower()                       

            
if __name__ == "__main__":
    main()
    
