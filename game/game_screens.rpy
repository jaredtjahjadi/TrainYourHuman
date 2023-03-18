init python:
    import random # Random package needed to randomize names without it being a headache
    
    # Pool of random names. Generated from https://www.name-generator.org.uk/quick/
    names = ["Sarah Shepard", "Leyton Henry", "Rachael Ali", "Martina Bloggs", "Raihan Rosario",
            "Cade Cisneros", "Louisa Soto", "Ned John", "Jannat Doherty", "Richard Levy",
            "Carlo Price", "Douglas Bernard", "Mahnoor Paul", "Brandon Page", "Marjorie Lambert",
            "Maisha Elliott", "Aryan Bates", "Kaitlyn Hart", "Angelica Mckenzie", "Tamara Michael",
            "Wolfie"
            ]
    
    curr_name = "" # Current name the user has selected
    
    # Randomizes the names
    def randomNames(l):
        random.shuffle(l)
    
    style.name_text = Style(style.default)
    style.name_text.color = "#f00"
    style.name_text.hover_color = "#ffaeae"

    style.selected_name_text = Style(style.default)
    style.selected_name_text.color = "#a71616"
    
    style.sorted_name_text = Style(style.default)
    style.sorted_name_text.color = "#2f9738"
    style.sorted_name_text.hover_color = "#b5ffb3"

    style.selected_sorted_name_text = Style(style.default)
    style.selected_sorted_name_text.color = "#004712"
    style.selected_sorted_name_text.hover_color = "#316330"

# Text in top-left of screen that indicates the current day (based on day variable) and time (morning or night)
screen DayTimeText():
    if day <= 1053:
        text "Day [day] - " + ("Night" if work_done else "Morning") yalign 0.01
    else:
        text "Day ??? - " + ("Night" if work_done else "Morning")

screen BottomMenu(): # Menu that is displayed at the bottom of the screen at (almost) all times
    add "images/icon_bar.png" yalign 1.0
    hbox spacing 1280.0 / 8.65: # Buttons are evenly split up
        yalign 1.0 # Buttons appear at bottom of screen

        # Wake up option
        imagebutton:
            # Gray out the wake up option if the human has already waken up
            if wake_up_done:
                idle "images/icon_wake_up_grey.png"
            # Make the option to wake up available if the human hasn't waken up
            else:
                idle "images/icon_wake_up.png"
                if wake_up_in_progress == False or ((animation == False) and wake_up_in_progress and ((day == 1055 and wake_up_attempt <= 2) or (day == 1056 and wake_up_attempt <= 4))):
                    action Jump("wake_up")
        
        # Next three options: Eat, hygiene, consume
        # First check if wake up is done. If not, grey out option
        # If so, check if the given action is done. If so, grey out option
        # If not, jump to the appropriate label in script.rpy

        # Eat option
        imagebutton:
            if wake_up_done:
                if eat_done:
                    idle "images/icon_eat_grey.png"
                else:
                    idle "images/icon_eat.png"
                    if wake_up_in_progress == False and consume_in_progress == False and eat_in_progress == False and hygiene_in_progress == False:
                        action Jump("eat")
            else:
                idle "images/icon_eat_grey.png"
        
        # Hygiene option
        imagebutton:
            if wake_up_done:
                if hygiene_done:
                    idle "images/icon_hygiene_grey.png"
                else:
                    idle "images/icon_hygiene.png"
                    if consume_in_progress == False and eat_in_progress == False and hygiene_in_progress == False:
                        action Jump("hygiene")
            else:
                idle "images/icon_hygiene_grey.png"
        
        # Consume option
        imagebutton:
            if wake_up_done:
                if consume_done:
                    idle "images/icon_consume_grey.png"
                else:
                    idle "images/icon_consume.png"
                    if consume_in_progress == False and eat_in_progress == False and hygiene_in_progress == False:
                        action Jump("consume")
            else:
                idle "images/icon_consume_grey.png"
        
        # Work option
        imagebutton:
            # Conditions for non-greyed out button: Only appears if eat, hygiene, and consume are done and work is not done
            if eat_done and hygiene_done and consume_done and work_done == False:
                idle "images/icon_work.png"
                # Conditions for work action
                if work_in_progress == False or ((animation == False) and work_in_progress and ((day == 1053 and work_attempt == 1) or (day == 1054 and work_attempt <= 2) or (day == 1055 and work_attempt <= 5))):
                    action Jump("work")
            # Conditions for greyed out button
            else:
                idle "images/icon_work_grey.png"

        # Sleep option
        imagebutton:
            if eat_done and consume_done and hygiene_done and work_done:
                idle "images/icon_sleep.png"
                action Jump("sleep")
            else:
                idle "images/icon_sleep_grey.png"

screen WorkScreen():
    $ randomNames(names)
    vbox ypos 70 spacing 27 xalign 0.5:
        textbutton "[firstTenNames[0]]":
            if firstTenNames[0] == sortedNames[0] and firstTenNames[0] == curr_name:
                text_style "selected_sorted_name_text"
            elif firstTenNames[0] == sortedNames[0]:
                text_style "sorted_name_text"
            elif firstTenNames[0] == curr_name:
                text_style "selected_name_text"
            else:
                text_style "name_text"
            # If no name has not already been selected and the index of curr_name != 0 (i.e., we're not clicking on curr_name again)
            if name_selected:
                action Call("working3", firstTenNames.index(curr_name), 0) # Swap names
            # If a name has not already been selected
            elif name_selected == False:
                action Call("working2", firstTenNames[0])
        textbutton "[firstTenNames[1]]":
            if firstTenNames[1] == sortedNames[1] and firstTenNames[1] == curr_name:
                text_style "selected_sorted_name_text"
            elif firstTenNames[1] == sortedNames[1]:
                text_style "sorted_name_text"
            elif firstTenNames[1] == curr_name:
                text_style "selected_name_text"
            else:
                text_style "name_text"
            if name_selected:
                action Call("working3", firstTenNames.index(curr_name), 1) # Swap names
            # If a name has not already been selected
            elif name_selected == False:
                action Call("working2", firstTenNames[1])
        textbutton "[firstTenNames[2]]":
            if firstTenNames[2] == sortedNames[2] and firstTenNames[2] == curr_name:
                text_style "selected_sorted_name_text"
            elif firstTenNames[2] == sortedNames[2]:
                text_style "sorted_name_text"
            elif firstTenNames[2] == curr_name:
                text_style "selected_name_text"
            else:
                text_style "name_text"
            if name_selected:
                action Call("working3", firstTenNames.index(curr_name), 2) # Swap names
            # If a name has not already been selected
            elif name_selected == False:
                action Call("working2", firstTenNames[2])
        textbutton "[firstTenNames[3]]":
            if firstTenNames[3] == sortedNames[3] and firstTenNames[3] == curr_name:
                text_style "selected_sorted_name_text"
            elif firstTenNames[3] == sortedNames[3]:
                text_style "sorted_name_text"
            elif firstTenNames[3] == curr_name:
                text_style "selected_name_text"
            else:
                text_style "name_text"
            if name_selected:
                action Call("working3", firstTenNames.index(curr_name), 3) # Swap names
            # If a name has not already been selected
            elif name_selected == False:
                action Call("working2", firstTenNames[3])
        textbutton "[firstTenNames[4]]":
            if firstTenNames[4] == sortedNames[4] and firstTenNames[4] == curr_name:
                text_style "selected_sorted_name_text"
            elif firstTenNames[4] == sortedNames[4]:
                text_style "sorted_name_text"
            elif firstTenNames[4] == curr_name:
                text_style "selected_name_text"
            else:
                text_style "name_text"
            if name_selected:
                action Call("working3", firstTenNames.index(curr_name), 4) # Swap names
            # If a name has not already been selected
            elif name_selected == False:
                action Call("working2", firstTenNames[4])
        textbutton "[firstTenNames[5]]":
            if firstTenNames[5] == sortedNames[5] and firstTenNames[5] == curr_name:
                text_style "selected_sorted_name_text"
            elif firstTenNames[5] == sortedNames[5]:
                text_style "sorted_name_text"
            elif firstTenNames[5] == curr_name:
                text_style "selected_name_text"
            else:
                text_style "name_text"
            if name_selected:
                action Call("working3", firstTenNames.index(curr_name), 5) # Swap names
            # If a name has not already been selected
            elif name_selected == False:
                action Call("working2", firstTenNames[5])
        textbutton "[firstTenNames[6]]":
            if firstTenNames[6] == sortedNames[6] and firstTenNames[6] == curr_name:
                text_style "selected_sorted_name_text"
            elif firstTenNames[6] == sortedNames[6]:
                text_style "sorted_name_text"
            elif firstTenNames[6] == curr_name:
                text_style "selected_name_text"
            else:
                text_style "name_text"
            if name_selected:
                action Call("working3", firstTenNames.index(curr_name), 6) # Swap names
            # If a name has not already been selected
            elif name_selected == False:
                action Call("working2", firstTenNames[6])
        textbutton "[firstTenNames[7]]":
            if firstTenNames[7] == sortedNames[7] and firstTenNames[7] == curr_name:
                text_style "selected_sorted_name_text"
            elif firstTenNames[7] == sortedNames[7]:
                text_style "sorted_name_text"
            elif firstTenNames[7] == curr_name:
                text_style "selected_name_text"
            else:
                text_style "name_text"
            if name_selected:
                action Call("working3", firstTenNames.index(curr_name), 7) # Swap names
            # If a name has not already been selected
            elif name_selected == False:
                action Call("working2", firstTenNames[7])
        textbutton "[firstTenNames[8]]":
            if firstTenNames[8] == sortedNames[8] and firstTenNames[8] == curr_name:
                text_style "selected_sorted_name_text"
            elif firstTenNames[8] == sortedNames[8]:
                text_style "sorted_name_text"
            elif firstTenNames[8] == curr_name:
                text_style "selected_name_text"
            else:
                text_style "name_text"
            if name_selected:
                action Call("working3", firstTenNames.index(curr_name), 8) # Swap names
            # If a name has not already been selected
            elif name_selected == False:
                action Call("working2", firstTenNames[8])
        textbutton "[firstTenNames[9]]":
            if firstTenNames[9] == sortedNames[9] and firstTenNames[9] == curr_name:
                text_style "selected_sorted_name_text"
            elif firstTenNames[9] == sortedNames[9]:
                text_style "sorted_name_text"
            elif firstTenNames[9] == curr_name:
                text_style "selected_name_text"
            else:
                text_style "name_text"
            if name_selected:
                action Call("working3", firstTenNames.index(curr_name), 9) # Swap names
            # If a name has not already been selected
            elif name_selected == False:
                action Call("working2", firstTenNames[9])