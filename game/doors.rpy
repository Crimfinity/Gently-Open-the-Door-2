label neckrope:

    stop music fadeout 3 
    scene black with fade  
    play ambient birds fadein 4 
    pause 5
    

    scene bg kitchen with dissolve_scene_full 

    mc "{image=note}I'm makin' breakfast and it smells really good.{image=note}"
    mc "{image=note}I hope that it tastes...uhhh...{w=.2}just as good.{image=note}"
    mc "Or is at least...edible?"
    mc "{image=note}Yeah!{image=note}"
    mc "{image=note}Doodoredooroo, I'm hummin' a song.{image=note}"

    play ambient2 sizzle fadein 2 
    "I lay my tired eyes on the sizzling bacon."
    "It's coming to life."
    "Even though the pig is very, very much dead."
    "God bless those creatures made out of ham."
    "But not the Islamic God, the other one."
    "But aren't they the same one?"
    pause .7 
    "Back on track." 
    "Seems like everything's really going right in the world."
    "I'm making a good breakfast, Monika texted me that it'll be fine if Sayori and I didn't show up at the festival..."
    "All is well."
    pause .75
    #"..."
    "I feel a shiver crawling down my spine."
    "Not...everything is well."
    "Sayori's alive, but…"
    "I'm not going to ignore the fact that she's still struggling."
    "I should be thankful that when I opened that door, she was still..."
    "Still..."
    "..."
    "I swallow."
    stop ambient2 fadeout 6
    "I crank down the heat on the bacon and the sizzle dies down."
    scene black with close_eye 
    "Closing my eyes, I focus on the sounds emitted by the surroundings."
    stop ambient fadeout 3 
    window hide 
    pause 3.0

    "Nothing."
    "Not a single prittle or prattle."
    "I can't even hear a breath."
    "She couldn't have…?"
    "No, no, there's no way."
    "Is there?"
    "I shake my head and chuckle to myself."
    "Don't be paranoid, [player]."
    "Don't baby her. Be there for her."
    "That's all that matters."
    window hide 
    pause 1.5 
    show s_kill at face:
        zoom 2.5
        yoffset 2400

    
    play music td 
    pause 1 
    stop music fadeout 4  
    play sound fall 
    scene bg kitchen with open_eyes 
    
   

    "I fall down, my breath erratic."
    "I…"
    "I have to check!"
    scene black with wipeleft 
    "I run up the stairs, my mind rushing with every possibility."
    "Please God, don't let this happen again."
    "Please!"
    "I reach the door and lean in, my ear flat against the wooden surface."
    "I can't hear a thing."
    "..."
    "One more time."
    "I gently open the door."
    play sound opend 
    scene bg sroom with wipeleft_door
    window hide 

    show sayori turned ce neut cm lup rdown at t11 
    pause .4 
    show sayori oe 
    pause .25 
    show sayori at h11 
    pause .2 

    "She's still here."
    "My heartbeat relaxes, the ringing in my ear disappears and my breath settles."
 
    show sayori turned worr lup rdown om oe at f11 

    s "Hey, [player]..."
    show sayori cm at t11 
    mc "Yeah, Sayori?"
    show sayori sad om rup ldown at f11 
    s "Where's my breakfast?"
    show sayori cm at t11 
    mc "Huh?"
    show sayori pout om rdown at f11 
    s "My breakfast, [player]."
    show sayori angr 
    s "{cps=10}Where is it?"
    show sayori cm at t11 
    mc "I'm workin--{nw}"
    show layer master at vpunch 
    show sayori vang om at hf11 
    s "WHERE IS IT!?"
    s lup "I WANT MY BREAKFAST!"
    s "YOU PROMISED ME BREAKFAST!"
    show sayori cm at t11 
    mc "D-don't worry, Sayori, I'll get on it, just one--"
    show layer master at vpunch 
    show sayori om at hf11 
    s "I TRUSTED YOU, [player!u]!"
    show sayori cry ce om ldown rdown 
    s "I TRUSTED YOU!"
    show sayori vang om lup e1h 
    s "I TRUSTED BREAKFAST!"
    show sayori -e1h e4e cm sad at t11 
    "What the hell is going on!?"
    show sayori at falldown
    hide sayori 
    #"She falls to the floor and starts crying."

    mc "Sayori..."

    "She sobs into the carpet."
    "I'm so confused."
    "She was okay just a second ago."
    "Why is she crying about breakfast?"
    "Unless…"
    "No."
    "No, no, no."
    "Not this."
    "Not this again."
    "I thought it was over!"
    show sayori turned cry oe cm at t11 
    "Sayori stands up, her tears dried up and looks me dead in the eye."

    mc "Sayori."
    mc "I know the voices are telling you to do it, but don't."
    mc "It's not worth it."
    mc "You are not just a puppet dancing to their whims."
    show sayori neut om at f11 
    s "But, [player]."
    show sayori lup 
    s "You didn't get me breakfast."
    show sayori cm at t11 
    mc "That's not a reason to do it."
    show sayori doub om at f11 
    s "[player]."
    show sayori angr 
    s "I wanted my breakfast and you didn't get me it."
    s neut "Cause and Effect."
    s "Setup and Punchline."
    show sayori cm neut rnoose at t11 
    mc "No."
    mc "Don't do it."

    #"Her tears begin flowing once more."

    mc "Sayori, I swear to fucking God, if you do this I will-{nw}"

    show sayori at h11 
    pause .1 
    hide sayori 
    play music td 
    call skz 
    #*sayori hangs herself*

    pause 1 
    stop music 
    mc "..."
    show layer master
    #scene bg sroom 
    #show sk
    "I sigh."

    mc "Well,{w=.4} shi--{nw}"
    scene black 
    play sound "mod_assets/boom.mp3"
    show logoback:
        truecenter 
        zoom .6 
        ease 1.5 zoom .8
    pause 1.5
    play sound "mod_assets/boom.mp3"
    show logotext:
        truecenter
        zoom .8
    pause 2
    scene black with fade 
    #*I GENTLY OPEN THE DOOR: NOW WITH EVEN MORE DOOR drops*
    return
    # fade to black


label nc1:
    #NooseCorp Act I - Too Big To Handle
    "I gently open the door."
    play sound opend 
    scene bg sroom with wipeleft_door
    

    play ambient phones fadein 2 
    #Sayori is running around from place to place

    mc "Sayori?"
    mc "What's going on--"
    show sayori turned happ om rup e1b at hf11
    s "Hello, hello, Sayori from NooseCorp, where we'll never ever leave you hanging." 
    show sayori neut 
    s "Can you please hold?"
    show sayori cm rdown at t11
    pause .5 
    show sayori at t41 
    pause .2 
    
    #Sayori runs to the other side of the room

    mc "Sayori, hey, wait a bit--{nw}"
    show sayori happ rup om at f41
    s "Hello, hello, Sayori from NooseCorp, where we'll never ever leave you hanging."
    show sayori neut 
    s "Can you please hold?"
    show sayori neut cm rdown at t44  
    #Sayori runs to the other side of the room

    mc "Seriously, Sayori, what is going--"
    show sayori happ rup om at f44 
    s "Hello, hello, Sayori from NooseCorp, where we'll never ever leave you hanging."
    s "Can you please hold?"

    #Sayori runs to the middle of the room
    show sayori neut cm at t11 
    "Oh my God."

    show sayori lsur -e1b 
    stop ambient 
    mc "SAYORI!"
    show sayori neut at face 
    #sayori transform to face
    "I grab her by the shoulders and pull her to me."

    show sayori happ om 
    s "Hello, hello, Sayori from NooseCorp, where we'll never ever leave you hanging."
    s ce "Can you please hold?"
    show sayori neut cm oe
    mc "Sayori, it’s me."
    show sayori ce 
    pause .2 
    show sayori oe 
    pause .4
    show sayori om happ 
    s "Oh! Hi 'me'!"
    show sayori cm at t11 
    mc "What is going on?"
    show sayori neut om at f11 
    s "Remember that ad we recorded for the self-defense noose?"
    show sayori cm at t11 
    mc "The one that we did in the beginning of the last volume of I Gently Open The Door which the audience should definitely play before this one?"
    #show sayori turned neut cm oe rup at t11
    #pause 2 
    #show layer master  
    show sayori lup happ ce om at hf11 
    s "Yeah that's the one!"
    show layer master:
        truecenter
        subpixel True 
        linear 2 zoom 1.2 
    show sayori neut oe cm ldown rdown at t11
    pause 2 
    show layer master  
    #Sayori looks directly at the player for a second

    show sayori nerv om at f11 
    s "Anyway, a lot of people want self-defense nooses!"
    s "It's like, the new hot thing!"
    s happ "Especially with single, Japanese salarymen!"
    s ce lup "It's even trending number one on Chirpy!"
    show sayori oe cm at t11  
    mc "That's pretty cool."
    show sayori rup om at f11 
    s "Apparently people are so in love with it, that depression rates have nose-dived!"
    s nerv ldown rdown "Although suicide rates have skyrocketed."
    s neut "Haven't figured out why just yet."

    show sayori cm at t11 
    "Huh?"
    "What's the link there?"

    show sayori nerv rup n2 om at f11 
    s "And now there's just so much demand, that I can't keep up."
    show sayori curi cm at t11 
    mc "Have you thought about expanding?"
    show sayori doub ce om -n2 at f11 
    s "They're not giving me enough time to expand!"
    s dist "I have to answer all these calls."
    show sayori cm neut oe at t11 
    mc "Well, umm…"
    mc "I'm always willing to help."
    show sayori lsur at f11 
    s "R-really!?"

    show sayori happ ce rup lup om at hr11

    s "Thank you, thank you, thank you, [player]!"
    show sayori nerv ldown at s11 
    s "Uhm…"
    show sayori oe at f11 
    s happ "Welcome to NooseCorp, I guess!"
    show sayori cm neut at t11 
    mc "We'll probably have to get some paperwork sorted out for employment, but yeah."
    show sayori happ 
    mc "Time to get to work, then."
    show sayori ce om rdown lup at f11 
    s "Yes sir!"
    play ambient phones fadein 4
    show sayori e2b cm at t41 
    "Sayori goes to answer one of the many ringing phones."
    "Alright, then."
    show sayori om 
    "I walk up to the ringing phone and pick up."

    mc "Hello, hello, [player] from NooseCorp, where we'll uhh…"
    show sayori -e2b om at hf41 
    s "Never ever leave you hanging!"
    show sayori cm e2b at t41 
    mc "Where we'll never ever leave you hanging."
    mc "How can I help?"
    stop ambient 

    play sound closed 
    scene black with wipeleft_door 

    #close door
    return
label sans:
    stop music 
    "I gently open the door as I feel my sins crawl on my back."
    play sound opend 
    scene bg sroom 
    show sans at i11
    with wipeleft_door 
    play sound "mod_assets/megal-.ogg"
    pause .611
    scene black 
    pause 2 
    #show sayori sans
    #play megalovania for like the first 10 notes
    #close door
    return 
label gta:
    "I gently open the door."
    play sound opend 
    scene bg sroom 
    show sayori turned cm oe neut at t11
    with wipeleft_door 

    #open door

    mc "Wassup, can a loc come up in your crib?"
    show sayori anno om lup at f11 
    s "Man, fuck you, I'll see you at school."
    show sayori cm at t11 
    mc "Ay noose bitch, don't hate me 'cause I'm beautiful, noose bitch."
    show sayori lsur 
    mc "Maybe if you got rid of that old yee-yee ass haircut you got, you'd get some dicks in your snatch."
    mc "Oh, better yet, maybe I'll actually love your dog ass if I ever stop fucking with that tsundere or yandere I'm fucking with."

    "I lean in and go for the knockout punch."

    show sayori sad at s11 
    mc "{image=note}Noose Bitch...{image=note}"

    show sayori lsur at h11 
    "I flip her the bird."
    show sayori curi om at f11 
    #call updatecosole ("Barber shops are now available{fast}", "Visit a barber to get a new haircut{fast}")
    s vang"What-{w=.8}{nw}"
    show sayori cm at t11 
    call updateconsole ("Barber shops are now available{fast}", "Visit a barber to get a new haircut{fast}")

    
    play sound closed
    scene black with wipeleft_door  
    return 
label dmc:
    #Dumbass MC

    "I gently open the…"
    show bump:
        alpha 0
        linear 60 alpha 1
    "Gently open the…"
    "The…"
    "Uhh…"
    "What was I doing…?"
    "Huh…"
    "Hey, wow."
    "This wall is really bumpy."
    "Sayori has a really bumpy wall outside her room."
    "How funky."
    "There's like..."
    
    "One bump."
    "Two bumps."
    "Three bumps."
    "Four bumps."
    "Five bumps."
    "Six bumps."
    window hide 
    pause 3 

    #fade to black…"
    #return

    "Sixty four thousand three hundred and sixty five bumps."
    "Sixty four thousand three hundred and sixty six bumps."
    scene black 
    "Oh, now I remember what I was supposed to do a month ago!"
    "I need to go and check up on Sayori!"
    "Silly [player], always so forgetful…"
 
    return 
label nude:
    #Nude Sayori
    stop music 
    "I gently open the door."
    play sound opend
    scene bg sroom
    show sayori turned nude neut cm oe at t11
    with wipeleft_door 

    mc "Hey Sayori."
    show sayori om at f11 
    s "Hey."
    show sayori cm at t11 
    mc "I think I left my pen in here."
    show sayori lup om at f11 
    s "Ah, okay, I think it's by my desk."
    s happ "Lemme get it."

    show sayori cm at d11 
    "Sayori bends down to get the pen and hands it to me."

    mc "Thanks!"
    show sayori ce om ldown at f11
    s "Anytime!"
    play sound closed
    scene black with wipeleft_door 
    return 
label delivery:
    #MC is an Amazon Deliveryman

    "I gently open the door."
    stop music 
    play sound opend
    scene bg sroom 
    show sayori turned casual neut cm oe at i11 
    with wipeleft_door 
    #open door
    show sayori turned doub om lup at f11 
    s "Uhh, hello?"
    s curi "[player], is that you?"
    show sayori neut cm at t11 
    mc "Garapagalos delivery!"
    show sayori happ 
    mc "Here's your package!"

    "I hand the cardboard box over to the salmon-haired girl."

    show sayori ce rup om at hf11 
    s "Oh finally!"
    s oe "This better have all the rope stuff I wanted!"
    s pout "The tracking said it was stuck in Guam for a week!"
    s doub "How does that even happen? And where is 'Guam' anyways?"
    s neut "Is it like an underwater city or something?"
    show sayori cm oe ldown at t11 
    mc "Sidespace Dimensional City, actually."
    show sayori happ om at f11 
    s "Oh! That makes sense."
    show sayori neut cm at t11 

    pause .5 
    
    play sound baby 
    pause .4 
    show sayori lsur lup rup at h11
    pause 2.6 
    "Shocked by the cry, the airhead drops the package to the ground."

    show sayori shoc 
    s "..."
    mc "..."
    show sayori vang om at hf11 
    s "I didn't order a crying rope!"
    show sayori cm at t11 
    mc "Well woops, I gotta go!"
    mc "Have a good day, bye!"
    show sayori angr om at f11 
    s "Wait, come back here--{nw}"
    play sound closed 
    scene black with wipeleft_door
    #close door
    return
label method: #still need the waving sayori 
    
    "I gently open the door."
    play sound opend 
    scene bg sroom 
    show sayori turned neut cm oe at t11 
    with wipeleft_door 
    show sayori happ om at f11 
    s "Hey, [player], I need your opinion on something."
    show sayori cm at t11 
    mc "What's up?"
    show sayori neut om at f11 
    s "Which way of committing suicide is better?"
    show sayori cm at t11 

    "She holds up three pictures of different suicide methods."
    "One showing a woman shooting herself, another showing a woman taking a toaster into a bathtub and another of a woman hanging herself."

    mc "Hmmmmm…"
    show sayori pout om lup at f11 
    s "Come onnnnnn!"
    show sayori cm at t11 
    mc "Alright, fine."
    mc "I'll have to go with the classic hanging yourself."
    show sayori happ om at f11 
    s "Fine choice."

    show sayori at h11 
    pause .1 
    play sound sting  
    hide sayori 
    call skz 
    #show s_kill2 
    #s_kill

    mc "Okay, I'mma go now."
    mc "See ya, Sayori."
    #(with a smile and a wave)
    s "See ya!"
    stop music 
    play sound closed
    scene black with wipeleft_door 
    #close door
    return 
label db1:
    #"I gently open the door."
    call dopen 

    mc "Hey, Sayori! Natsuki made cupcakes, do you want some?"
    show sayori anno om lup at f11 
    s "[player], I have diabetes."
    show sayori cm at t11 
    mc "..."
    mc "I'll take that as a yes."

    "I leave the three trays of cupcakes and leave."
    call dclose 
    return 
label schizo:
    #Schizophrenic Sayori

    "I gently open the door."
    play sound opend 
    scene bg sroom 
    show sayori turned casual neut cm oe ldown rdown at t11 
    show natsuki turned happ casual cm oe at t31 
    show yuri turned casual happ cm at t33 
    with wipeleft_door 
    #the entire gang is here! except monika
    show sayori happ lup rup om at hf11 
    s "[player]! You're finally here!"
    show sayori ldown 
    s "Come, we're gonna play some Truth or Dare."
    show sayori neut cm at t11 
    mc "Sayori, we talked about this."
    mc "You have to take your meds."
    show sayori sad om rdown at f11 
    s "B-but, I don't wanna…"
    show sayori dist at s11 
    s "It always makes me feel so funky..."
    show sayori sad cm 
    mc "It's for your own good."

    "I go over to her dresser and grab her pill bottle, unscrewing it and handing her two pills."

    show sayori om at f11 
    s "Do I have to?"
    show sayori cm ce sad at t11 
    mc "Yes, Sayori, you have to."
    show sayori neut at d11 
    "She takes the pills and with one gulp, swallows them both down."
    show sayori oe 
    window hide 
    pause 3.0
    hide natsuki with dissolve 
    show sayori sad 
    pause 3.5 
    hide yuri with dissolve 
    show sayori cry ce at s11 
    #natsuki fades, sayori starts to get sad
    #yuri fades, sayori starts crying
    #mc fades/screen goes black
    pause 3 
    show sayori oe 
    show black onlayer front:
        alpha 0
        linear 3 alpha 1 
    pause 1 
    s "No, not you too...{w=1}{nw}"
    pause 1 
    scene black 
    hide black onlayer front 
    play sound opend 
    pause .15 
    m "Hey, Sayori, do you want to play some Truth or --{nw}"
    show layer master at hpunch 
    s "OF COURSE YOU'RE THE ONLY ONE WHO'S REAL!"
    s "Just my luck."
    m "..."
    m "I'll go."
    s "Please."
    call dclose 
    return 
label bread:
    #Baguette

    "I gently open the door."
    play sound opend 
    scene bg sroom with wipeleft_door 
    show baguette at floating with dissolve

    mc "It's a baguette."
    "Baguette" "\"Baguette.\""
    mc "Baguette."
    "Baguette" "\"Baguette.\""
    show sayori turned happ om oe lup rdown at r33 
    s "Oh hey, a baguette."
    show sayori cm 
    mc "Baguette."
    show sayori neut om at f33 
    s "Baguette."
    show sayori cm at t33 
    "Baguette" "\"Baguette.\""
    show monika forward happ ce om lpoint at l31
    show sayori vang ldown  
    m "Baguette!"
    show layer master at vpunch 
    show monika cm lsur 
    mc "GOD FUCK OFF MONIKA!"
    show monika cry 
    show sayori om at f33 
    s "NO ONE ASKED JEEZ!"
    show sayori cm 
    pause .3 
    show monika ce at t31 
    pause .5 
    show monika at lhide 
    hide monika 
    pause 3.5 
    "Baguette" "\"Baguette.\""
    call dclose 
    return 

    #monika crying

    #close door
label pregnancy:
    #Pregnancy

    play sound opend 
    scene bg sroom 
    show sayori turned casual dist oe cm at t11 
    with wipeleft_door

    mc "Sayori, why'd you call me here?"
    show sayori sad om at f11
    s "[player], we need to talk."
    show sayori cm at t11 
    mc "What is it?"
    show layer master:
        truecenter 
        subpixel True 
        linear 1.7 zoom 1.4
    #slow zoom in on sayori's face
    #pregnancy test meme
    
    s "I'm pregnant."
    mc "B-but how!?"
    s "Remember when we out to the park a couple days ago?"
    mc "Yeah…?"
    s "And we were getting warm and fuzzy?"
    mc "Yeeeeaaahhhh…?"
    s "And then we hid in the bushes and you uhh…"

    "Sayori swallows nervously."

    s "And you held my hand?"
    mc "Oh no…"
    s "I guess we held hands a bit too hard…"
    mc "Damn it!"
    mc "My mom always said I should use protection!"
    mc "I should've worn my gloves!"
    s "It's not your fault!"
    s "I wanted to feel your hands too, you know."
    mc "Yeah…"
    s "Yeah…"

    pause 10.0

    mc "So, abortion or…?"

    s "Nah I've got it covered, two for one!"
    #s_kill

    mc "..."
    mc "Phew, that was close!"
label psa:

    stop music 
    play music "mod_assets/6b.ogg"
    "I gently open the door."
    play sound opend 
    scene bg sroom 
    show sayori 1a at t11 zorder 5 
    show vhs zorder 10 onlayer front 
    show aspect zorder 20 onlayer front 
    with wipeleft_door 
    #Pedo PSA

    show sayori 2r at f11 
    s "Hey, kids!"
    show sayori 2a at t11 
    mc "Hiya, Sayori!"
    show sayori 2b at f11 
    s "Look, there's nothing cooler than talking and being with someone you like."
    s 1b "But when someone older than you tries to talk to you or touch you in a way that makes you feel uncomfortable…"
    s 1j "That's no good!"
    s 1b "If you're ever in that situation, first: you gotta say no!"
    s 1r "Then, you gotta get out of there and stop talking to that person!"
    s 1c "Most importantly, you have to tell a person you trust!"
    s 1b"Like your parents and a trusted adult!"
    show sayori 1a at t11 
    mc "Thanks Sayori!"
    show sayori 1i at f11 
    s "And remember adults…"
    show sayori 1c
    s "If you ever think about a child in a sexual context..."
    show sayori 1x at f11 
    show noise zorder 1:
        alpha .4
    show layer master:
        truecenter
        ease .4 zoom 1.7 yoffset 250
    stop music
    hide vhs onlayer front 
    hide aspect onlayer front 
    s "Don't!" 
    #call dclose 
    #stop music 
    play sound closed 
    scene black
    with wipeleft_scene  
    return 

label dyslexia:
    #Dyslexia
    "I genlty opnen the door.{w=2.0}"
    "I...{w=1.0}"
    "I open gnetly the door.{w=2.0}"
    "Door gtenly the oepn I. {w=2.0}"
    "I braeknodwn itno teras."
    show sayori turned om sad at l11 
    #sayori walks into frame looking sad

    s "[player]...?"
    s "Cmoe hree."

    
    show sayori turned cm sad at i11 onlayer front 
    play sound opend 
    scene bg sroom with wipeleft_scene 
    show sayori turned cm neut at i11 
    hide sayori onlayer front  

    "She opens the gently door."
    "I did it."
    "knid of."

    show sayori worr om rup at f11 
    s "Are you oaky?"
    show sayori cm at t11 
    "I nod my haed."

    show sayori neut om at f11 
    s "Do uoy wnat me to klil msylef?"
    show sayori rdown cm at t11 
    mc "Kill mylsef?"
    show sayori sad ce om at f11 
    s "I'll tkae taht as a sey."
    show sayori cm at t11 
    mc "Huh?"

    hide sayori 
    play sound sting 
    call skz 
    #s_kill
    pause 1 
    "..."
    "..."
    "I berkarwnodn otni treas."

    call dclose 
    return 
label ava:
    stop music 
    "I gently open the door."
    play sound opend 
    scene bg sroom 
    show ava ngelion at i11 
    with wipeleft_door 
    mc "Wow, Sayori!"
    mc "You look different!"
    mc "Did you get a haircut?"
    play sound "mod_assets/glitch_scream.ogg"
    show layer master at anxiety 
    show vignette zorder 5 
    show noise zorder 1:
        alpha .4 
    show ava at f11 zorder 3
    show n_rects_ghost1 zorder 3 
    show n_rects_ghost2 zorder 3 
    show n_rects_ghost3 zorder 3
    

    a "Our fates intertwined forever and ever by a string so thin and so fragile-{nw}"
    a "He loved me and I loved him, but a tragic fate befell us-{nw}"
    a "His dread overtook him, yet I will still forever love him and my limited time with him-{nw}"
 
    a "My only wish was to tell him-{nw}"
    a "Do not dread a horrible future, or it will become your fate.{w=.2}{nw}"
    show black onlayer front
    pause 99999999999999999999999999999999999
    hide black onlayer front
    scene bg sroom
    mc "Ahaha!"
    mc "Relatable."
    call dclose  
    
    return 


label db2:

    #Sayori has Diabetes 2

    "I gently open the door."
    play sound opend 
    scene bg sroom 
    show sayori turned dist cm e0a n2 ldown rdown at t11 
    with wipeleft_door
   
    mc "Hey Sayori, did you eat the cupcakes?"

    "I look to the ground and see three empty trays and crumbs all over the place."
    show sayori om lup at s11 
    s "Gurr...hurr…"
    show sayori cm 
    "Sayori seems so sluggish."

    mc "Are you okay, Sayori?"
    show sayori ldown om 
    s "[player]...the...i-ins-"
    show sayori cm 
    s "..."
    mc "Do you need more cupcakes?"
    play sound fall 
    show sayori at falldown 
    hide sayori 
    

    "Sayori's on the ground, spazzing out."
    show sayori turned:
        rotate 90 yoffset 200
        ypos .3
        dizzy(1.5, 0.01) 
     
        
    "White foam is being produced from her mouth."
    
    "She must be really excited for more cupcakes."

    play music td 
    show sayori at falldown 
    hide sayori 
    #s_kill sfx
    mc "Sayori, don't be so dramatic, I'll go get you more cupcakes."

    "I pat her head as the foam starts leaking out of her mouth."
    "She should really clean herself up."
    "What a slob."
    call dclose 
#close door
    return 
label dopen:
    "I gently open the door."
    play sound opend 
    scene bg sroom 
    show sayori turned neut cm oe ldown rdown at t11 
    with wipeleft_door 
    return 
label dclose:
    stop music 
    play sound closed 
    scene black with wipeleft_scene  
    return 
label skz:
   

    show s_kill2:
        zoom 1.1 rotate -7 xcenter 640
        yoffset -1700
        yanchor 0
        parallel:

            ease 2.0 rotate 7
            ease 2.0 rotate -7
            repeat
      

    return 
label sk:
    play music td 

    