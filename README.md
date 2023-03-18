# Train Your Human

You are a "god" that controls a human. A perfect human follows its daily routine: eat, take care of hygiene, works, and buys the latest things. To ensure that you create a perfect human, be sure not to deviate from it whatsoever!

## About

**Trigger warning: This game features hints towards depression and death.**

**Train Your Human** is a PC game where the player is a "god" (up to their interpretation) that controls a human as it partakes in its daily routine of eating, taking care of hygiene, watching TV, working, and buying the latest  things! The player must ensure that it does not deviate from it whatsoever so that the human can be trained to perfection! While embracing the minimalistic aesthetic inspired by the games [KIDS](https://playkids.ch/) and [Can Your Pet](https://canyour.pet/), the player will soon find that getting the human to partake in its daily routine is not as easy as it seems...

This game was created during the 2023 Ren'Py Competition hosted by Stony Brook University's Game Development and Design Club from March 9, 2023 to March 16, 2023.

## How to Install

Officially released versions are available to download for PC (Windows and Linux) and Mac in this repository's [Releases page](https://github.com/jaredtjahjadi/TrainYourHuman/releases).

## How to Build

### Requirements

- [Ren'Py](https://www.renpy.org/)
  - This game was developed using Ren'Py 8.0.3; there is no guarantee that it will work for older or newer releases of Ren'Py.
- Your preferred IDE to view and/or edit code (ex: Visual Studio Code)
- A tool to clone GitHub repositories (Git Bash, GitHub Desktop, etc.)

### Build Instructions

1. **Download Ren'Py and set up the Ren'Py Launcher.** Instructions can be found in the official Ren'Py [Quickstart guide](https://www.renpy.org/doc/html/quickstart.html#the-ren-py-launcher) under the "The Ren'Py Launcher" section. Be sure to know what your project directory is - in the Ren'Py Launcher, this can be found under "Preferences."
2. **Clone this repository.** The instructions will depend on the tool you use to clone Git repositories.
   - In Git Bash, if you prefer to clone using HTTPS, type in the following commands:

            cd <project directory>    
            git clone https://github.com/jaredtjahjadi/TrainYourHuman.git
    
      Or if you prefer to clone using SSH, type in the following commands:

            cd <project directory>    
            git clone git@github.com:jaredtjahjadi/TrainYourHuman.git

    - Before cloning with GitHub Desktop, be sure that you are currently on the main page of this repository. Scroll up and click on the green "Code" button at the top of the page. Then click on "Open with GitHub Desktop..." and the program will open. Click on the "Choose..." button and select the previously mentioned Ren'Py project directory. Finally, click on the blue "Clone" button.
    - More detailed instructions can be found in [GitHub's official repository cloning guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
3. **Ensure the folders are in the correct order.** If you followed the cloning steps correctly, it should look like something along the lines of "\<project directory\>\TrainYourHuman."
4. **You should now see the game in the Ren'Py Launcher.** It will appear under "PROJECTS:" in the left-hand side of the launcher. Click on the game to see further options to view game assets, edit the source code, or launch the game.
5. **Pressing Shift+D while in-game will reveal a Developer Menu.** This menu includes useful debugging tools such as Auto Reload and an Image Location Picker.

## Known Issues

- After clicking the last dialogue box at the end of the game, the game crashes saying "An exception has occurred."
- In the last in-game day, when the player prompts the human to wake up, the eating animation plays after clicking out of the first few dialogue boxes.
- The work minigame does not work properly.
  - The intended behavior is to select ten random names from a pool of names, display them on the screen, and re-randomize the ten random names for each in-game day.
  - The current behavior is that on Day 1, the first ten names in the pool are selected and displayed on the screen (i.e., the list is not randomized). From Day 2 onwards, the same ten names are shown in the order that the player ended on in Day 1. In other words, the ten names are already sorted. The current method of overcoming this issue is to resort any of the two names; the player will have completed the minigame and can further progress in the game.

## Features to Be Implemented in the Future

Due to time constraints, several features were unable to be implemented in the game before the Ren'Py Competition submission deadline. Along with fixing the above issues, future versions of the game will hopefully implement the following features:

- Showering at night (no more stinky human!)
- Changing title screen after game completion
- Further distortion in names being sorted when work minigame is played as the game progresses
- Implement title screen music
- Change "Start" option in Title Screen to say "New Life"
- Disable saving feature altogether (not visible in-game but auto-saves and quick saves are still generated in the files)
- More work minigames
- More interactivity in Eat, Hygiene, and Consume options

## Credits

**Writers:** Dani Duong, Jared Tjahjadi  
**Programmer:** Jared Tjahjadi  
**Artist:** Dani Duong  
**Music:** Dani Duong  
**SFX:** [Mixkit](https://mixkit.co/free-sound-effects/click/)  
**Special Thanks:** Stony Brook University Game Development and Design Club (GDDC)