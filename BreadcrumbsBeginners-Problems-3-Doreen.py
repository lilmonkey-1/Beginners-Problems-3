#rollercoaster

x = int(input("what's your height in cm"))
if 130 <= x:
   print("you can ride the rollercoaster:)")
elif 1 <= x:
   print("you can't ride the rollercoaster :(")
elif 130 == x:
   print("you can ride the rollercoaster :)")

#choose your own adventure

print("You are entering a haunted mansion alone because you lost a dare. You knock on the door but nobody answers.")

option1 = input("Do you choose to WAIT or CLIMB IN THROUGH THE WINDOW? (wait/climb)")
if option1 == “wait”:
    print("You wait and wait and wait and its the middle of a cold winters night in London so you freeze to death.")
if option1 == “climb”:
    option2 = input("You stumble through the decrypt window, cutting yourself on the broken glass. It is dark and you can't see. Do you choose to TURN ON YOUR PHONE FLASHLIGHT or KEEP WALKING THROUGH THE DARK? (flashlight/walk)")

    if option2 == “flashlight”:
        print("You switch on your flashlight and see a deformed purple man with no face except for a pair of bloodshot eyes staring at you from the middle of the hallway. You die from shock.")
    if option2 == “walk”:
        option3 = input("You clumsily clatter through the darkness of the hallway, almost falling into what looks like a tall purple mannequin, but you can't be quite sure because frankly its dark asf. Shadowy hands seem to grab at you from the walls. You find your way into the dining room where a goblet of cold baked beans sits on the table. It kind of has a green tinge. Next to it a paper cup of perfectly fresh oreo chocolate froyo calls to you. Do you choose to EAT THE BEANS or EAT THE FROYO? (beans/froyo)")

        if option3 == “beans”:
            print("Are you kidding me. Who do you think you are. Beans? OVER FROYO??? The gods smite you for being rancid.")
        if option3 == “froyo”:
            option4 = input("You slurp up that yummy froyo. As you're guzzling your gullet, a crackling high pitched squeal comes from the closet. A humongous long necked pale face with dangling black hair snakes out from the crack. YOU ATE HER FROYO YOU LIL RAT!! Do you choose to RUN AWAY or FIGHT? (run/fight)")
            if option4 == “fight”:
                print("You box her on the left ear. She bites your leg off. You die from bloodlossbro. GG")
            if option4 == “run”:
                print("You flee into the darkness but her neck stretching ability is formidable. She catches up to you in a matter of seconds and suffocates you anaconda style. GG")
