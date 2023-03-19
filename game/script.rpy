# Animations
image animation_placeholder = Movie(play="images/animation_placeholder.webm")
image animation_human_fastwakeup = Movie(play="images/animation_human_fastwakeup.webm")
image animation_human_slowwakeup = Movie(play="images/animation_human_slowwakeup.webm")
image animation_human_refuse = Movie(play="images/animation_human_refuse.webm")
image animation_eat = Movie(play="images/animation_eat.webm")
image animation_hygiene = Movie(play="images/animation_hygiene.webm")
image animation_consume_morning = Movie(play="images/animation_consume_morning.webm")
image animation_consume_night = Movie(play="images/animation_consume_night.webm")

default day = 1 # Game starts on Day 1
default wake_up_attempt = 0 # Later in the game it will take several attempts to wake up the human
default work_attempt = 0 # Later in the game it will take several attempts to make the human go to work

# Boolean variables that keep track of state of whether an action has been done or not, or if it is in progress or not.
# Important as they indicate at what point a given menu option can be selected (e.g., player cannot select any option if 
# eating is in progress)
default wake_up_done = False
default wake_up_in_progress = False
default eat_in_progress = False
default eat_done = False
default hygiene_in_progress = False
default hygiene_done = False
default consume_in_progress = False
default consume_done = False
default work_in_progress = False
default work_done = False
default animation = False
default name_selected = False # Work minigame

# Game starts here
label start:
    scene human_sleep
    show screen DayTimeText # Top-left text that displays current day and time (morning/night)
    show screen BottomMenu
    "Meet your new human! To make a good human, you must have the human follow its daily routine.
    Be sure not to deviate from it whatsoever!"
    "A good human eats, takes care of its hygiene, works, and buys the latest items. Make sure
    your human does all these things, and your human will be trained to perfection!"
    call screen BottomMenu

# Wake up option
label wake_up:
    show screen BottomMenu
    play sound "audio/sfx_button.wav"
    $ wake_up_in_progress = True
    # For the earlier part of the game
    if day <= 1054:
        if day <= 50:
            show animation_human_fastwakeup at truecenter
            $ renpy.pause(1, hard=True)
            hide animation_human_fastwakeup
            scene bg_still
            "The human woke up!"
        else: # 51 <= day <= 1054
            show animation_human_slowwakeup at truecenter
            $ renpy.pause(1.65, hard=True)
            hide animation_human_slowwakeup
            scene bg_still
            "The human is burnt out by its job and woke up a bit slower today."
        if day <= 999:
            play music "audio/music_normal.wav"
        else:
            play music "audio/music_glitched.wav"
        $ wake_up_done = True
        $ wake_up_in_progress = False
        call screen BottomMenu
    
    # Second to last in-game day
    elif day == 1055:
        if wake_up_attempt == 0:
            $ animation = True
            $ wake_up_attempt += 1
            "The human does not feel like waking up."
            $ animation = False
        elif wake_up_attempt == 1:
            $ animation = True
            $ wake_up_attempt += 1
            "The human is resisting any attempt to wake up."
            $ animation = False
        elif wake_up_attempt == 2:
            $ animation = True
            $ wake_up_attempt += 1
            show animation_human_slowwakeup at truecenter
            $ renpy.pause(1.65, hard=True)
            hide animation_human_slowwakeup
            scene bg_still
            "The human reluctantly decided to wake up."
            $ animation = False
            $ wake_up_attempt = 0
            $ wake_up_done = True
            $ wake_up_in_progress = False
            play music "audio/music_glitched.wav"
        call screen BottomMenu
    
    # Last in-game day (end of game)
    elif day >= 1056:
        if wake_up_attempt == 0:
            $ animation = True
            $ wake_up_attempt += 1
            "The human does not feel like waking up."
            $ animation = False
        elif wake_up_attempt == 1:
            $ animation = True
            $ wake_up_attempt += 1
            "The human is resisting any attempt to wake up."
            $ animation = False
        elif wake_up_attempt == 2:
            $ animation = True
            $ wake_up_attempt += 1
            "The human thought about waking up, but went back to sleep."
            $ animation = False
        elif wake_up_attempt == 3:
            $ animation = True
            $ wake_up_attempt += 1
            "The human thinks it'll skip work today."
            $ animation = False
        else:
            $ animation = True
            $ wake_up_attempt += 1
            "..."
            $ renpy.pause(3, hard=True)
            "Your human has expired!"
            return
        call screen BottomMenu

# Eat option
label eat:
    show screen BottomMenu
    play sound "audio/sfx_button.wav"
    $ eat_in_progress = True
    window hide
    show animation_eat
    $ renpy.pause(2.0, hard=True)
    hide animation_eat
    if day <= 50:
        "The human ate a healthy meal."
    elif day <= 1000:
        "The human forgot to buy groceries and ate leftovers."
    else:
        "The human is eating West Side Dining-flavored slop. It hopes it doesn't have food poisoning soon."
    $ eat_in_progress = False
    $ eat_done = True
    call screen BottomMenu

# Hygiene option
label hygiene:
    show screen BottomMenu
    play sound "audio/sfx_button.wav"
    $ hygiene_in_progress = True
    window hide
    show animation_hygiene
    $ renpy.pause(2.0, hard=True)
    hide animation_hygiene
    "Human has finished brushing its teeth."
    $ hygiene_done = True
    $ hygiene_in_progress = False
    call screen BottomMenu

# Upon picking the consume option
label consume:
    show screen BottomMenu
    play sound "audio/sfx_button.wav"
    $ consume_in_progress = True
    if work_done: # Human makes purchases in the nighttime
        "The human will make some purchases."
        show animation_consume_night
        $ renpy.pause(2.0, hard=True)
        if day == 1:
            "The human bought a piece of furniture."
        elif day == 2:
            "The human bought a video game called \"Train Your Human \". It'll play the game if it ever has free time... key word {i}if{/i}."
        elif day <= 274:
            "The human has made questionable financial decisions."
        else:
            "The human was unable to purchase anything with its limited budget."
        hide animation_consume_night
    else:
        show animation_consume_morning
        if day < 50:
            "Human is watching the news."
        else:
            "Human is consuming propaganda."
        if day == 1:
            "\"The Animated Perspectives club at Stony Brook University is hosting an anime convention
            called Brook-Con on March 26, 2023 from 12 PM to 8 PM in the SAC.\""
            "\"There's a cosplay contest, an Artist Alley and game room, and numerous panels such as Pokémon GO
            Club's Pokémon Guessing Game & Trivia Panel!\""
            "The human thought this event seemed interesting but would not be able to go due to work responsibilities."
            "It thinks that everyone should go, though!"
        elif day == 2:
            "That Stony Brook University's not having good luck..."
            "Apparently they're raising parking prices and making everyone pay for parking, on top
            of the proposed overall tuition increase."
            "And their catering company Culinart is under investigation for illegal activity?! Outrageous!!!"
        elif day == 3:
            "More pro-capitalism ads have been aired recently."
            "The human doesn't have much money, but watching these ads gave it hope that one day it'll strike gold."
        elif day == 4:
            "The human watches more capitalist propaganda and recalls similar sentiment from its job."
        elif day == 5:
            "The human can't take its eyes off the alluring, direct capitalist propaganda being shown on the TV."
        elif day <= 274:
            "The human almost lost track of time watching capitalist ads."
        elif day <= 1053:
            "The human can now recite the capitalist ads from memory."
        elif day >= 1054:
            "ayhfuioweaqyhfgrejksgvbyaehkfgbrvfeyuhaskjgfvtfgrhydsuigkjretfanbwvjhyzhzsfdvrauiowaeryoitgerwh"

        # Hide textbox and pause game to show that humnan is consuming
        window hide
        $ renpy.pause(3.0, hard=True)
        hide animation_consume_morning
    "The human has finished consuming."
    $ consume_done = True
    $ consume_in_progress = False
    call screen BottomMenu

# Upon picking the Work option
label work:
    show screen BottomMenu
    play sound "audio/sfx_button.wav"
    $ work_in_progress = True

    # Earlier part of the game
    if day <= 1052:
        if day <= 49:
            "It's time for the human to go to work."
        else:
            "The human tires of its daily routine, but it's time for it to go to work."
        jump working
    # When the human refuses to go to work
    elif (day == 1053 and work_attempt == 0) or (day == 1054 and work_attempt <= 1) or (day == 1055 and work_attempt <= 4):
            $ animation = True
            $ work_attempt += 1
            show animation_human_refuse at truecenter
            $ renpy.pause(1, hard=True)
            hide animation_human_refuse
            "The human refuses to go to work."
            $ animation = False
    else:
        $ work_attempt += 1
        "You force the human to go to work."
        jump working
    call screen BottomMenu

# Upon picking the Sleep option
label sleep:
    play sound "audio/sfx_button.wav"
    python: # Reset boolean statements and change the day
        wake_up_done = False
        eat_done = False
        hygiene_done = False
        consume_done = False
        work_done = False
    if day >= 5 and day <= 49: # Timeskip 1
        $ day = 50
    elif day >= 50 and day <= 273: # Timeskip 2
        $ day = 274
    elif day >= 274 and day <= 1052: # Timeskip 3
        $ day = 1053
    else:
        $ day += 1
    
    # Transition to next day
    stop music fadeout 1.0
    hide screen BottomMenu
    hide screen DayTimeText
    
    # Change sleep dialogue based on game progress
    if day <= 50:
        "The human is having a good night's sleep."
    elif day >= 51 and day <= 1000:
        "It's getting harder for the human to sleep, but it eventually did."
    else:
        "The human can barely sleep nowawdays. It took hours for it to sleep."
    
    scene black with fade # Fade to black
    $ renpy.pause(1, hard=True)
    if day <= 1053:
        show text "{size=48}{color=#fff}Day [day]{/color}{/size}" at truecenter with fade
    else:
        show text "{size=48}{color=#fff}Day ???{/color}{/size}" at truecenter with fade
    $ renpy.pause(2, hard=True)
    hide text with fade # Fades the day text away
    scene human_sleep with fade
    show screen DayTimeText
    show screen BottomMenu
    call screen BottomMenu

# Work minigame
label working:
    hide screen BottomMenu
    hide screen DayTimeText
    scene black with fade
    $ renpy.pause(0.25, hard=True)
    scene bg_work with fade
    $ randomNames(names)
    default firstTenNames = names[:10]
    $ sortedNames = sorted(firstTenNames)
    show screen WorkScreen
    call screen WorkScreen

label working2(selected_name):
    $ name_selected = True
    $ curr_name = selected_name
    call screen WorkScreen

label working3(selected_name_ind, index):
    python:
        firstTenNames[selected_name_ind], firstTenNames[index] = firstTenNames[index], firstTenNames[selected_name_ind]
        name_selected = False
        curr_name = ""
    if firstTenNames == sortedNames: # Once the names are sorted
        if day < 50:
            "BOSS: Well done!"
        elif day <= 1000:
            "BOSS: You could've done it faster."
        else:
            "BOSS: {i}Pick up the slack next time or you're fired!{/i}"
        jump work_finished
    call screen WorkScreen

label work_finished:
    scene black with fade
    $ renpy.pause(0.25, hard=True)
    scene bg_still with fade
    show screen DayTimeText
    show screen BottomMenu
    if day < 50:
        "The human has finished work."
    elif day <= 1000:
        "The human had a rough day at work."
    else:
        "The human is losing motivation to continue working."
    python:
        work_attempt = 0
        eat_done = False
        hygiene_done = False
        consume_done = False
        work_in_progress = False
        work_done = True
    call screen BottomMenu