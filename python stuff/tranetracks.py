import os
import time
import sys
import random
import base64
import json
import zlib
import ctypes
#import shit
#i dont even have it written why do i have libraries for saving what the fuck

def clear_screen():
     os.system('cls' if os.name == 'nt' else 'clear')

#for my impatient ass
print("DEBUG MODE")
print("Y/N")
debug= input("> ")
def typewriter(text):
    if debug== "y":
        print(text)
    else:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05) 
        print("")
def slowtype(text):
    if debug== "l":
        print(text)
    else:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.3) 
        print("")
def temptype(text):
    if debug== "l":
        print(text)
    else:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05) 
        print("")

clear_screen()

#all praise f-strings for requiring this line to exist
nl = "\n"
apo= "'"
#whoever made indentions SO DAMN ANNOYING will feel my wrath, i will skin you
while True:
    typewriter("Welcome to TRANETRACKS, Python edition")
    print("")
    print("")
    time.sleep(2)
    typewriter(f"======OPTIONS======")
    typewriter(f"NEW GAME (N){nl}CREDITS (C)")
    print("")
    menu= input("> ").lower()
    if menu== "c":
        typewriter("TRANETRACKS is an original story written by Charter E. Menning")
        typewriter("Programming: Charter")
        typewriter("Writing: Charter")
        typewriter("Prompt: Mrs. Webb")
        typewriter("Trans shit: Mom, Dad, Mrs. Webb")
        typewriter("Staying awake: Monster Energy, Bigelow Tea, Mountain Dew: Baha Blast, ADHD meds")
        typewriter("Nirvana, Tally Hall, Mac DeMarco, John Coltrane, INOHA, and  for just existing")
        typewriter("Special thanks to J.R Kaufman for his praise of the original story, Maze Williams; my beautiful boyfriend")
        typewriter("Congratulations to the Franklin Central Marching Band for making BOA Finals for the first time in school history and making ISSMA Finals for the first time since 2011...")
        typewriter("========================")
        typewriter("Click enter to return to main menu")
        goback= input("> ")
        clear_screen()
        continue
    elif menu=="n":
        break
#but what broke :( 
#my heart trying to write this bs



while True:
    typewriter("What is your name?")
    username = input("> ")
    funni = username.lower()
    upname = username.upper()

    if funni== "wyvern": 
            typewriter("A main character are we?")
            break
    elif funni== "charter":
        typewriter("Oh look, a dumbass")
        typewriter("give a password")
        password = int(input("> "))
        if password == (84623): 
            typewriter("thanks")
            break
        else:
            typewriter("get the fuck away from my code")
            print("killing all processes now")
            ctypes.memset(0, 1, 1)
    elif funni== "niko":
        typewriter('"Wyvern! Thats my name!"')
        typewriter("choose a different name...")
        continue
    elif funni == "goose":
        typewriter('"Hey bud, you might wanna do somethin else..."\nchoose a different name...')
        continue
    elif funni== "faye":
        typewriter('"Real original dumbass"')
        typewriter("choose a different name...")
        continue
    #took me way to long to figure out how or statements work,
    elif funni== "mr. knapp" or funni== "mark" or funni== "knapp" or funni== "mr knapp": 
        typewriter("Hey Mr. Knapp, if you're reading this I actually completed this thing, suprising...")
        break
    #ew deadname gross
    elif funni== "lucas":
        typewriter('"ugh dont worry itll get better soon bud"')
        break
    elif funni== "maze":
        typewriter('"HAIII I LOVE YOU MAZE THANKS FOR PLAYING MY SHIT!!!!" -char <3')
        break
    elif funni== "dad" or funni== "todd" or funni== "tzero":
        typewriter('"fadder stop snooping, da code will now kill itself"')
        ctypes.memset(0, 1, 1)
    elif funni== "mom" or funni== "tanya" or funni== "tatiana":
        typewriter('"stop snooping in my coding stuff, mom!"')
        break
    elif funni== "carter" or funni== "levi":
        typewriter('"fuck you get off my computer you douchebag"')
        ctypes.memset(0, 1, 1)
    elif funni== " " or funni=="":
        typewriter("Invalid Name, Names should not be blank.")
        continue
    
    else:
        break
typewriter("...")
typewriter(f"Welcome, {username}!")
typewriter("...")
typewriter("Have you read the short story, TRANETRACKS?")
#i think i wrote it, i guess i mightve idk maybe
typewriter(f"Y/N")
readstory = input("> ").lower()
if readstory== "y":
    typewriter("Amazing!")
else:
    typewriter(f"I suggest you read it in full (ask char) {nl} but the game can be played without prior reading! ")

typewriter("type anything to begin!")
gamestart = input("> ").lower()

if gamestart== "anything":
    typewriter("heh thats funny man lmao")
    time.sleep(1) 


for _ in range(35):
    print("")
    time.sleep(0.05)
clear_screen()
#fun fact this used to be 35 lines of just print("") time.sleep(0.05) becuz i didnt know how loops worked

typewriter(f"Within the expansive ruins and flora of unincorporated Big Run-Deam joint wilderness, {nl} some of the last remaining infrastructure from pre-anarchtic America lies, the foliage of its tracks was disrupted for the first time in so many dawns.{nl} The psithurism of trees that bank along the manmade line of the tracks and the fluttering of{nl} plants growing liminal to the crossties filled the air.{nl} There upon those abandoned crossties sat a quartet.")
print("")
typewriter(f"This quartet, possibly the first humans to lay foot upon the tracks in years, {nl} sat quite disappointingly compared to what one would imagine the appearance of the only souls to visit there in ages to be.")
print("")
typewriter(f"These humans names were: Niko, Faye, Goose, and you, {username}...")
print("")
typewriter(f"You shift your foot in the ground, the sound of rocks scraping against each other creeps from the ground. {nl} You look up, the overcast sky peers through a small, straight line gap between the trees, {nl} Looking down the rails, you see a wall of fog, the tracks consumed by the mist.")
print("")
typewriter(f'You hear the young voice of NIKO to your left{nl}"We arrive alas..."')
print("")
typewriter(f"You chuckle, NIKO has a habit of talking in a very, whimsical fasion...{nl} You consider making fun of him for it...")
print("")
#may my chromebook browser and codehs terminal cry trying to display this text unless debug=y
typewriter(f"Poke fun at NIKO?")
print("Y/N")
mock= input("> ").lower()



if mock== "y":
    print("")
    typewriter(f'You laugh a little harder,{nl} "Do you always gotta talk like that, Niko?"')
    print("")
    typewriter(f'"Is there something wrong with it?" NIKO looks over at you, annoyed, {nl}"I suppose it{apo}s just my dialect, I guess I don{apo}t really think about it but I guess you do..."')
    print("")
    typewriter(f'FAYE laughs,{nl} "Bold of you to assume that {username} puts much thought into anything!"')
    print("")
    typewriter(f'You laugh in spite of yourself,{nl} "Oh shut up Faye,"')
    print("")
    typewriter(f'Niko smiles, "Anyways..."')
else: 
    print("")
    typewriter(f'You look over at NIKO, you say,{nl}"I suppose so, we oughta start heading out"')



typewriter(f'You look around one last time before preparing to take off when NIKO runs ahead of everyone, {nl} "Guys wait!" NIKO pants, "We s-should get a picture before we go!"{nl} NIKO holds a camera in his hands, its silver and black with the word "MINOLTA" emblazoned on it...{nl}')
print("")
typewriter(f'You huddle with FAYE and GOOSE to get in the photo, you see them doing various gestures and facial expressions')
print("")
typewriter(f'You try to decide a face and pose to do')
print("")
typewriter(f'Should you:{nl} A: Smile and peace sign, B: Stick your tongue out and flip the bird?')
print("")
typewriter(f'A/B')
pose= input("> ").lower()



if pose== "a":
    typewriter(f'You lean in and smile, your left hand making a peace sign...{nl}... {nl}"CLICK!" {nl} NIKO{apo}S camera shutter clicks,"')
    typewriter(f'NIKO laughs,{nl} "Whats with the pose, {username}, hehe?" NIKO chuckles, {nl}"Are you trying to be a hippie or something?"')
    print("")
    typewriter(f'You glare at NIKO...')
    typewriter(f'"Oh shut up..."')
    typewriter(f'GOOSE looks over, slightly chuckling, {nl}"I mean he{apo}s not wrong..."')
    typewriter(f'You roll your eyes, "Yea whatever..."')
else:
    typewriter(f'You lean in and stick your tongue out, your flip your middle finger at the camera, laughing...{nl}... {nl}"CLICK!" {nl} NIKO{apo}S camera shutter clicks,')
    typewriter(f'You, GOOSE, and FAYE all laugh, NIKO slightly annoyed at your rude gesture, {nl}"{username}! You shouldn{apo}t do that!" NIKO cries out, though he fails at hiding his amusement.')
    typewriter(f'GOOSE laughs, {nl} "God I cannot wait for that roll to get developed! I{apo}m not sure exactly how {username} looked but I could tell that was definitely... something..." GOOSE laughs slightly harder.')

typewriter(f"NIKO lowers his camera, letting it hang from his neck. He turns around, slowing his pace to let you and the rest of the group catch up...")
typewriter(f"The group aligns. {nl}GOOSE looks over at you")
typewriter(f'"Hey {username}, how far do you think it{apo}ll be?')
print("")
typewriter(f"For the first time since you arrived, you remember why you're here in the first place...{nl}You think back to when you met the three you're with...")
typewriter(f"You think back to when you ran away, a wave of fear, sadness, and anger washes over you, you try to block the memory...")
print("")
slowtype("Do you want to remember why you ran away?")
print("")
slowtype("Y/Y")

nochoice= input("> ").lower()
choiceloop= int(0)
while True:
    if choiceloop== (2):
        temptype(f"Do you want to remember?")
        temptype(f"Y/Y")
        nochoice= input("> ")
    if nochoice=="y":
        if choiceloop== (2):
            choiceloop= int(0)
    
        break
    else:
        slowtype(f"You don't have a choice in this, {username}...") #oooo slow and spoopy
        choiceloop= int(2)
        continue

clear_screen()

typewriter(f"You find yourself thinking back to the day you ran away...")
typewriter(f"The trees and the tracks and everything around you fades away...")
temptype(f"...")
time.sleep(0.8)
print("")
print("")
temptype(f"...")
time.sleep(0.5)
print("")
print("")

temptype(f'"{upname}!"')
temptype(f'A man{apo}s voice roars behind a closed door.{nl}You{apo}re huddled up in a fetal position, you have your back to the door')
temptype(f'Through tears you yell,{nl} "D-Dad! P-Please stop!"')
temptype(f'Loud banging eminates from behind it, the doorknob jiggles...')
temptype(f'"WHY IS THIS DOOR LOCKED?!"{nl}"LET ME IN!"')
print("")
temptype(f"The banging of the door makes you sob harder than you already were, you contemplate whether you should let him in or stand your ground...")
print("")
temptype(f"Let dad in?")
temptype(f" Y/N")

lethim= input("> ").lower()

if lethim== "y":
    print("")
    temptype(f"Hands trembling, you unlock the door...")
    slowtype(f"...")
    temptype(f'The door flies open with a "BANG!"')
    temptype(f'The frame of a tall man wielding a club lumbers through the door..."')
    temptype(f'"WHAT THE HELL IS WRONG WITH YOU?!"{nl}He shouts...')
    print("")
    typewriter(f'Before you have a chance to respond, he charges you, club in air')
    typewriter(f"Suddenly...")
    typewriter(f"Everything")
    typewriter(f"Goes")
    time.sleep(2)
    clear_screen()
    for _ in range(30):
        print("")
    print("                                                                                                                        ", end="")
    slowtype(f"d a r k . . .")
    clear_screen()
    typewriter(f'Your eyes blur in and out of focus...')
    typewriter(f'Your head is throbbing with pain...')
    typewriter(f'You realize when you try to move your limbs that you{apo}re tied down...')
    typewriter(f'...')
    typewriter(f'After a couple minutes you can finally see, ')
    typewriter(f'You lift your head to see you{apo}re tied down to your own bed.')
    typewriter(f'Looking around, you see the door, nails poke through the frame, it{apo}s boarded up from outside...')
    typewriter(f'It{apo}s completley silent, no one seems to be nearby...')
    print("")
    typewriter(f'You wonder if you should try to get out yourself or call for help')
    print("")
    typewriter(f'Call for help (H) or find another way? (F)')
    print("")
    typewriter("H/F")
    print("")
    hf= input("> ").lower()
    dhelp= int(0)
    while True:
        if dhelp== (2):
            typewriter("It seems like you'll have to do this yourself")
            typewriter("Click F to continue")
            hf= input("> ")
        if hf== "f":
            typewriter(f'You look around...')
            typewriter(f'You spot a hunting knife sitting at the edge of the nightstand to your right.')
            typewriter(f'Using what little range of motion you have, you repeatedly shake the bed, making the nightstand shake too...')
            typewriter(f'With each shake, the knife creeps closer to the edge of the nightstand.')
            print("")
            typewriter("...")
            print("")
            typewriter("The knife falls right into your hand, poking your right palm as it falls, you wince, a small trail of blood trickles down your palm.")
            typewriter("You reposition the knife in your hand, you manage to get the blade to press against the rope binding your hand. You start to cut through the rope.")
            typewriter("...")
            print("")
            typewriter("You eventually manage to cut through the rope, freeing your hand.")
            typewriter("You free the rest of your body before standing up, unbound.")
            break
        else:
            typewriter("You try to call for help")
            typewriter(f'"Please! Someone! Help!"{nl}"I-I{apo}m tied up and can{apo}t move!')
            typewriter("...")
            typewriter("No one responds...")
            dhelp= int(2)
            continue
    typewriter("i guess it")
