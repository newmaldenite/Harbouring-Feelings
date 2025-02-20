# Define characters with anime-style color coding
define j = Character("Jiro", color="#7cb5ec", what_color="#666666")
define m = Character("Mai", color="#ff9d9d", what_color="#666666")
define gui.text_color = "#666666"

# Backgrounds and sprites (you'd add actual image files to project)
image bg docks = "docks.jpg"
image jiro neutral = "jiro_neutral.png"
image jiro nervous = "jiro_nervous.png"
image mai neutral = "mai_neutral.png"
image mai smile = "mai_smile.png"
image mai blush = "mai_blush.png"

# Start the game
label harbouring:
    scene bg docks with fade
    play music "audio/bgm.mp3" fadein 2.0
    $ renpy.music.set_volume(0.5, delay=0.5)  # 50% volume
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
    pause 1.5
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
    pause 2.0
    hide screen code_display

    j "So we’re... using a base image, adding our app, and telling it how to run?"
    show mai smile with dissolve

    m "Mhm. Now, let's actually build the container. Here, hold this."
    show jiro neutral with dissolve
    "She hands him a clipboard. Their fingers brush, and both instantly pull back, eyes darting away."

    j "R-right. Uh... so the command is?"

    show screen code_display("docker build -t my-container .") with dissolve
    pause 1.0
    hide screen code_display

    m "See? We're packing everything up. It’s like sealing the container before shipping it out."

    j "A-and then we... run it? Like starting the journey?"

    show screen code_display("docker run my-container") with dissolve
    pause 1.0
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