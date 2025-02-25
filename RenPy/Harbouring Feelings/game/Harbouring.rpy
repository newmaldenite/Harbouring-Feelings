init python:
    gui.text_font = "fonts/DarwinSerif-Regular.ttf"
    gui.name_text_font = "fonts/DarwinSerif-Regular.ttf"
    gui.text_size = 28
    gui.name_text_size = 34
    gui.text_color = "#444444"

# Define characters with anime-style color coding
define j = Character("Jiro", color="#4f93d2", what_color="#3f3f3f")
define m = Character("Mai", color="#f47a7a", what_color="#3f3f3f")

# Backgrounds and sprites (you'd add actual image files to project)
image bg docks = "docks.jpg"
image jiro neutral = "jiro_neutral.png"
image jiro nervous = "jiro_nervous.png"
image mai neutral = "mai_neutral.png"
image mai smile = "mai_smile.png"
image mai blush = "mai_blush.png"

# Add to character definitions
default persistent.docker_knowledge = 0

# Custom GUI styling (add before label harbouring)
style anime_frame:
    background Frame("gui/textbox.png", 12, 12)
    padding (35, 30)

style anime_button:
    hover_sound "audio/hover.ogg"
    activate_sound "audio/select.ogg"

style anime_button_text:
    font "fonts/anime-inept.ttf"
    hover_color "#ff99cc"

# Start the game
label harbouring:
    scene bg docks with fade
    stop music fadeout 1.0
    play music "audio/bgm.mp3" fadein 2.0
    $ renpy.music.set_volume(0.3, delay=0.5)  # 50% volume
    show jiro neutral at right
    show mai neutral at left

    "The salty sea breeze drifted through the docks as Jiro adjusted his gloves."
    "He stole a quick glance at Mai, who stood beside him, her hair catching the afternoon sun."

    m "Jiro, are you even paying attention? We have to get this container ready."
    show jiro nervous with dissolve

    j "I-I know that! I was just... thinking. Containers. Right. Let’s start... with, um... preparing it?"

    show mai smile with dissolve
    m "You're so awkward sometimes. Yes, first, we need something to put in the container. You can’t ship an empty one, you know."

    j "Oh! That means we need an application first, right? Something to package?"
    
    show mai neutral with dissolve
    "She kneels and scribbles on a notepad."
    
    # Code display using Ren'Py's code formatting
    show screen code_display("""
    // app.js
    console.log("Hello from our container!");
    """) with dissolve
    pause 4.0
    hide screen code_display

    j "That’s... simple. I thought it would be more complicated."

    m "Silly! Keeping things lightweight is important. Now, we need a Dockerfile to tell Docker how to package it up."
    m "Think of it like... instructions for packing a gift."

    show screen code_display("""
    // Dockerfile
    FROM node:14
    COPY app.js /app.js
    CMD ["node", "app.js"]
    """) with dissolve
    pause 5.0
    hide screen code_display

    m "Now, what's the FIRST line we need in a Dockerfile?"
    
    label docker_question_1:
    menu:
        "FROM specifies the base image":
            $ persistent.docker_knowledge += 1
            m "Exactly! We need a foundation to build on."
            jump continue_1
        "RUN npm install":
            m "Not yet! We need to choose a base image first."
            jump docker_question_1
        "COPY . /app":
            m "Almost, but we need a base image before copying files."
            jump docker_question_1

    label continue_1:

    j "So we’re... using a base image, adding our app, and telling it how to run?"
    show mai smile with dissolve

    m "Mhm. Now, let's actually build the container. Here, hold this."
    show mai neutral with hpunch
    show jiro neutral with dissolve
    "She hands him a clipboard. Their fingers brush, and both instantly pull back, eyes darting away."

    j "R-right. Uh... so the command is?"

    show screen code_display("docker build -t my-container .") with dissolve
    pause 4.0
    hide screen code_display

    m "What does the '-t' flag do in this command?"
    
    label docker_question_2:
    menu:
        "Tag the image with a name":
            $ persistent.docker_knowledge += 1
            m "Right! Makes it easier to reference later."
            jump continue_2
        "Test the container":
            m "Good guess, but that's what 'run' is for!"
            jump docker_question_2
        "Timeout setting":
            m "Nope, that's not related to building. Try again!"
            jump docker_question_2

    label continue_2:
    
    show mai smile with dissolve
    m "See? We're packing everything up. It’s like sealing the container before shipping it out."

    j "A-and then we... run it? Like starting the journey?"

    show screen code_display("docker run my-container") with dissolve
    pause 4.0
    hide screen code_display

    show mai blush with dissolve
    "She leans against the railing, looking out at the horizon."
    m "Bingo! Now the container is running, just like our ship setting sail."
    m "Kind of poetic, don’t you think?"

    j "Yeah... It is."

    # scene bg docks sunset with fade
    # show jiro neutral at left
    # show mai blush at right
    "A comfortable silence settles between them as the last container is loaded onto the ship."
    "Mai turns to him, her expression suddenly more serious."
    show mai neutral with dissolve

    m "Jiro... Sometimes, you have to package up what’s inside and just... send it out there."
    m "Otherwise, it never reaches the destination."

    show jiro nervous with dissolve
    j "Y-you mean—?"

    show mai blush with hpunch
    m "I mean—Docker. Obviously. What else would I be talking about?"

    j "O-of course! Haha... Just Docker..."
    "He scratches the back of his head."

    play sound "ship_horn.ogg"
    # scene bg docks night with fade
    "The ship’s horn blares as it departs, carrying its containers across the waves."
    "And yet, another kind of cargo remained—unspoken words, waiting for the right time to be sent."

label ending:
    scene black with fade  # Fade to black

    # Show "The End" in the center
    show text "{b}{color=#f3f3f3}The End{/color}{/b}" at truecenter
    with Dissolve(2.0)
        
    pause 3.0  # Keep "The End" visible for a few seconds or until the player clicks

    # Show "... for now." in the bottom right corner
    $ renpy.music.stop(fadeout=5.0)
    show text "{i}{color=#f3f3f3}... for now.{/color}{/i}" at Position(xalign=0.95, yalign=0.95)
    with Dissolve(1.5)

    pause 3.0  # Wait before returning to the main menu

    return

# Custom screen for code display
screen code_display(code_text):
    frame:
        xalign 0.5
        yalign 0.25
        background "#1e1e1e"
        padding (20, 20)
        text code_text:
            color "#dcdcdc"
            font "Ubuntu-R.ttf"
            size 24