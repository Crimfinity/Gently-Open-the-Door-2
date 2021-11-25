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
    #"Is there?"
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

   
    "I'm so confused."
    "She was okay just a second ago."
    "Why is she crying about breakfast?"
    "Unless…"
    #"No."
    #"No, no, no."
    #"Not this."
    #"Not this again."
    #"I thought it was over!"
    show sayori turned cry oe cm at t11 
    "Sayori stands up, her tears dried up and looks me dead in the eye."

    mc "Sayori."
    mc "I know the voices are telling you to do it, but don't."
    #mc "It's not worth it."
    mc "You are not just a puppet dancing to their whims."
    show sayori neut om at f11 
    s "But, [player]."
    show sayori lup 
    s "You didn't get me breakfast."
    s "I wanted my breakfast and you didn't get me it."
    show sayori cm at t11 
    #mc "That's not a reason to do it."
    #show sayori doub om at f11 
    #s "[player]."
    #show sayori angr 
    #s "I wanted my breakfast and you didn't get me it."
    #s neut "Cause and Effect."
    #s "Setup and Punchline."
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
        linear 60 zoom 3 yoffset 1000 
    show sayori neut oe cm ldown rdown at t11
    pause 60
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

    mc "Hello, hello, [player] from NooseCorp, where we'll uhh..."
    show sayori -e2b om at hf41 
    s "Never ever leave you hanging!"
    #show sayori cm e2b at t41 
    #mc "Where we'll never ever leave you hanging."
    #mc "How can I help?"
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
     

    scene black with fade 
    pause 3
    show bump 
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
    m "Hey, Sayori, do you want to play some Truth or--"
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
    show sayori neut 
    "Baguette" "\"Baguette.\""
    call dclose 
    return 

    #monika crying

    #close door
label pregnancy:
    stop music 
    scene black 
    "I gently open the door."
 
    play sound opend 
    scene bg sroom 
    show sayori turned dist oe cm at t11 
    with wipeleft_door

    mc "Sayori, why'd you call me here?"
    show sayori sad om n3 at f11
    s "[player], we need to talk."
    show sayori cm at t11 
    mc "What is it?"
    show layer master:
        truecenter 
        subpixel True 
        linear 1.4 zoom 2.7 yoffset 300 xoffset 100
    #slow zoom in on sayori's face
    #pregnancy test meme
    pause 2 
    show sayori nerv om oe
    show preg with dissolve:
        truecenter 
        zoom .20
        yoffset -50 xoffset 75
    s "I'm pregnant."
    show sayori cm 
    mc "B-but how!?"
    scene bg sroom 
    show sayori turned nerv om rup n3 ldown at i11 
    with dissolve
    s "Remember when we went out to the park a couple days ago?"
    show sayori cm 
    mc "Yeah..?"
    show sayori om laug at f11 
    s "And we were getting warm and fuzzy?"
    show sayori -n3 n4 flus cm at t11  
    mc "Yeeeeaaahhhh..?"
    show sayori sad om ldown at f11 
    s "And then we hid in the bushes and you uhh…"
    show sayori cm at t11 
    "Sayori swallows nervously."
    show sayori om at f11 
    s "And you held my hand?"
    show sayori cm at t11 
    mc "Oh no…"
    show sayori rup nerv om at f11 
    s "I guess we held hands a bit too hard..."
    show sayori cm at t11 
    mc "Damn it!"
    mc "My mom always said I should use protection!"
    mc "I should've worn my gloves!"
    show sayori worr om at hf11
    s "It's not your fault!"
    show sayori sad 
    s "I wanted to feel your hands too, you know."
    show sayori cm at t11 
    mc "Yeah..."
    show sayori ce om at s11 
    s "Yeah..."
    show sayori cm 

    pause 10.0
    show sayori oe -n4 at t11 
    mc "So, abortion or..?"
    show sayori happ om lup at f11 
    s "Nah I've got it covered, two for one!"
    show sayori at h11 
    pause .15 
    hide sayori 
    stop music 
    play sound sting 
    call skz
    #show s_kill2 
    mc "..."
    mc "Phew, that was close!"
    call dclose 
    return 
label psa:

    stop music 
    play music "mod_assets/6b.ogg"
    "I gently open the door."
    play sound opend 
    scene bg sroomw 
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
    show layer screens at anxiety:
        ease 10 zoom 1.3
    show layer master at anxiety:
        ease 10 zoom 1.5 
    show vignette zorder 5 
    show noise zorder 1:
        alpha .4 
    show ava zorder 2: #at f11 zorder 3:#3:
        yanchor 1.0 ypos 1.03 subpixel True
        dizzy(1.5,.01)
    show n_rects_ghost1 zorder 3:
        dizzy(1.5,.01)
    show n_rects_ghost2 zorder 3:
        dizzy(1.5,.01) 
    show n_rects_ghost3 zorder 3:
        #xoffset -80
        dizzy(1.5,.01)
    

    a "Our fates intertwined forever and ever by a string so thin and so fragile-{nw}"
    a "He loved me and I loved him, but a tragic fate befell us-{nw}"
    a "His dread overtook him, yet I will still forever love him and my limited time with him-{nw}"
 
    a "My only wish was to tell him-{nw}"
    a "Do not dread a horrible future, or it will become your fate.{w=.2}{nw}"
    show black onlayer front
    pause 99999999999999999999999999999999999
    show layer screens 
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

    #play sound sting
    show sayori at falldown 
    hide sayori 

    #mc "Sayori, don't be so dramatic, I'll go get you more cupcakes."

    "I pat her head as the foam starts leaking out of her mouth."
    mc "Sayori, don't be so dramatic, I'll go get you more cupcakes."
    #"She should really clean herself up."
    #"What a slob."
    call dclose 
#close door
    return 
label dg:
    stop music 
    "I gently open the door."
    play music t4 fadein 2
    play sound opend  
    show sayori turned casual cm oe happ at t11 zorder 2 
    show natsuki turned neut lhip rdown casual at t31 zorder 2 
    show yuri turned cm dist casual at t33 zorder 2 
    show sroomz zorder 1 
    with wipeleft_door 
    show sayori ce om lup at f11 zorder 3 
    s "Hello and welcome to the first meeting of the Dead Girls' Society." 
    s oe "Everyone introduce yoursel--{nw}"
    show sayori lsur cm at h11 zorder 2 
    mc "Uh, what's going on?"
    show sayori happ ldown om at f11 
    s "Oh hey, [player]!"
    s rup "This is just the first meeting of the DGS!"
    s ce "You're welcome to watch."
    show sayori cm oe at t11 zorder 2
    mc "Cool."

    "I take a seat at the corner of the room."
    show sayori om neut at f11 zorder 3 
    s "Okay everyone, let's introduce ourselves."
    show sayori cm at t11 zorder 2
    show yuri shy om at s33 zorder 3 
    y "Uuu…"
    show yuri turned dist cm oe rup at t33
    show sayori happ om at f11 zorder 3 
    s "Okay, I'll start."
    show natsuki sad 
    s rdown "My name is Sayori and I hanged myself."
    show sayori cm at t11 
    y "..."
    show sayori neut 
    show yuri dist om lup rup at f33 zorder 3 
    y "My name is Yuri and I stabbed myself."
    show yuri cm at t33 zorder 2
    show natsuki cross dist 
    n "..."
    show yuri neut 
    show sayuri curi 
    n "..."
    show sayori anno om at f11 zorder 3 
    show natsuki neut  
    s "C'mon, Natsuki!"
    show sayori cm neut at t11 zorder 2
    show natsuki turned lhip curi om at f31 zorder 3  
    n "Sayori, do I even count?"
    n doub ce "I never actually died! I was just deleted."
    show natsuki cm at t31 zorder 2
    show sayori rup om at f11 zorder 3 
    s "Well you were sent to the void just like the rest of us, so I think you count."
    show sayori cm happ oe at t11 zorder 2
    show natsuki anno om ldown rdown at f31 zorder 3 
    n "Okay fine…"
    n dist "My name is Natsuki and I got deleted."
    show natsuki cm oe curi at t31 zorder 2
    show sayori lsur 
    show yuri curi 
    play sound knock 

    pause 2.0
    show sayori angr at t43 
    show natsuki angr at t42 
    show yuri angr at t44
    show monika forward nerv om n2 lpoint at l41 zorder 3 
    m "H-hey..."
    show monika happ at f41 
    m "I overheard you guys talking and I was wondering if I could..."
    m laug "...Join you guys?"

    show monika nerv cm ldown at s41 zorder 2
    stop music fadeout 4
    "The girls all stare holes into the wretched one."
    show sayori vang at f43 zorder 3 
    s "{b}{cps=1} N o . {/b}"
    show monika sad om zorder 3 
    m "Oh..." 
    show monika at lhide 
    hide monika 

    "Monika scurries off."
    show sayori at t11 
    show natsuki at t31 
    show yuri neut at t43 
    show sayori anno om at f42 
    s "{i}Anyway...{/i}" 
    show sayori happ 
    show natsuki neut  
    s "Now that we got rid of the pest..."
    show sayori cm neut at t42 zorder 2
    mc "Um, actually, I have a question."
    mc "What do you guys actually do here?"
    show sayori om lup at f42 zorder 3 
    s "We talk about the trauma of dying."
    show sayori cm at t42 zorder 2
    show natsuki happ om ldown at f31 zorder 3 
    n "But mostly we just chill out and hang."
    show natsuki ce cm at t31 zorder 2
    show sayori dist 
    s "..."
    show natsuki om at f31 zorder 3 
    show yuri happ ldown rdown  
    n "Pun entirely intended."
    show natsuki cm oe rdown at t31 
    show sayori om happ at f42 zorder 3  
    s "Thanks, Nat..."
    show sayori cm at t42 zorder 2
    "I shake my head at the shenanigans."
    "Ah girls, never chang--"
    "Wait, is that..."
    stop music fadeout 3 
    window hide 
    show yuri:
        4
        linear 5 alpha 0
    show noose zorder 11 :
        truecenter 
        xoffset 1000 yoffset -400
    show layer master:
        subpixel True 
        truecenter 
        linear 3 xoffset -1015
    show pink zorder 10:
        alpha 0 xoffset 1015
        3
        linear .4 alpha .6 
    #camera pans to the left
    pause 3 
    mc "Ropu-Kun!"
    mc "You're alive!"
    mc "Oh I missed you so much!"
    mc "I thought I lost you!"
    play music t10 
    "I grab Ropu-Kun and hug him tight!"

    mc "I won't let you go this time, I swear!"
    y "Sayori, what is going on..?"
    s "If I knew, I'd tell you."
    mc "Oh my god, we have to make up for so much lost time."
    mc "Let me take you out to dinner."
    mc "How does that sound?"
    window hide 
    show layer master:
        subpixel True 
        #truecenter 
        right
        xoffset -1015
        linear 10 zoom 1.4 yoffset 200 xoffset -1100
    pause 10
    show layer master:
        subpixel True 
        truecenter 
        xoffset -1015  
    n "I am beyond confused."
    y "Isn't that the rope we glued a set of comedic eyes to, so that you could cope with your trauma better?"
    s "I think???"
    scene bg sroom 
    show sayori turned casual lup cm oe worr at t11 #at face zorder 11 
    show natsuki turned casual curi lhip rdown cm oe at t31 
    show yuri turned casual lup rdown curi oe cm at t33 
    show noose zorder 10 at floating:
        yoffset -400 xoffset -150  
    mc "Girls, I can't tell you how grateful I am for you bringing it back to me."
    show sayori at face zorder 11 
    "I hug Sayori to show my appreciation."

    mc "Thank you so much."
    show sayori curi om at f11 zorder 2 
    s "You're welcome???"
    show sayori cm at t11 
    mc "Okay, Ropu-Kun, there's a steak with your name on it!"
    mc "Let's go!"
    stop music 
    play sound closed 
    scene black with wipeleft_door 
    return 
    #close door
label infinity:
    scene black 
    stop music 
    "I gently open the door."
    play sound opend
    pause .15 
    "There's another door."
    "Huh."
    "I gently open the door again."
    play sound opend
    pause .15 
    "And another door."
    "Okay."
    "I gently open the door once more."
    play sound opend
    pause .15 
    "More doors??"
    play sound opend
    pause .15 
    "How many doors are there!?"
    "I gently open the door another time."
    play sound opend
    pause .15 
    "Phew! A hallway!"
    "It's dark, but that should be okay."
    "I walk forward into the dark abyss."
    "Okay and there should be-"

    play sound "sfx/smack.ogg"

    "ANOTHER DOOR!?"
    "Ugh."
    "I open the door, not very gently this time."
    play sound opend
    pause .15 
    "Oh my God."
    "It's another door."
    "Fuck this."
    "I try to kick the door down."

    play sound "sfx/fall2.ogg"
    mc "AH FUCK!"

    "I break my leg."
    "Ouchie. That hurtie my stumpy wumpy."
    "I crawl to the doorknob and open it."
    window hide 
    scene white with dissolve_scene_full 
    pause .3 
    show white onlayer front:
        .1
        linear 3 alpha 0 
    scene black 
    show noose at floating:
        yoffset -200
    #blinded by light
    #dark room with noose in it

    mc "What the…?"
    show sayori turned om neut e3a at l41 
    s "You know what you must do."
    show sayori cm 
    mc "..."
    mc "Yes."

    show layer master:
        truecenter 
        linear 1 zoom 1.15
    "I crawl up to the noose, barely standing on my two feet."
    "Looking through it, I see my future reflected within the noose."
    "I know what I must do."
    scene black 
    show noose at floating:
        truecenter 
        zoom 1.8
        yoffset -300
    with dissolve

    "I take the noose and stare at it longingly."

    mc "I'm sorry, Ropu-Kun."

    "I get it closer to my head."
    "Clearing my throat, time to make my move."
    "I make out with the noose."
    #pause 1.3 
    play sound "mod_assets/kiss.wav" #its a small wav ok?
    pause 1.3
    #mc "Blegh, why is it so soggy?"
    #show sayori turned neut oe om rup at l31 
    #s "The rope's a slut."
    #show sayori cm 
    #mc "..."
    call dclose 
    #close door
label madden:
    "I gently open the door."

    play sound opend 
    show black zorder 3:
        yoffset -720
    show sroom base zorder 1
    show s_kill2 zorder 5:
        zoom 1.1 rotate -7 xcenter 640
        yoffset -1700
        yanchor 0
    with wipeleft_door 
    play sound sting
    mc "Sayori!"

    "No…"
    "I approach the hanging body of my best friend."
    "I should've seen this coming…"
    "I look up to see Sayori's lifeless face."
    "Oh Sayori, what did you do…-{nw}"
    "Wait a minute."
    show layer master:
        ease 1 yoffset 100 
    pause 1 
    "I look further up only to be met with an endless void."

    mc "Where the hell is the rope attached to…?"

    "I move up the chair that's been thrown carelessly on the ground and jump on."
    "Okay, so I need to climb that rope..."
    hide s_kill2
    show s_kill3 zorder 5:
        zoom 1.1 xcenter 640 rotate -7
        yoffset -1230
        yanchor 0
        parallel:
            rotate 0
            ease .2 rotate 15 
            ease .2 rotate 0

    "I jump from the chair and use Sayori's limp head for another boost."
    "That jump should do it."
    "And..."
    "Catch!"
    "I'm gripping the rope."
    show layer master:
        yoffset 100 
        ease 1.4 yoffset 300
    "Now it's time to climb."
    "Let's see where this void takes us."
    show layer master:
        yoffset 300 
        ease 1.4 yoffset 400
    "Using all my upper body strength, I begin to climb the endless rope."
    "At first, the void is a simple blackness, while terrifying, it is at the very least comprehensible."
    show layer master:
        yoffset 400 
        ease .7 yoffset 450
    "So, I climb."
    show layer master:
        yoffset 450 
        ease 1.4 yoffset 500
    "I climb, I climb and I climb."
    "My arms shake."
    "My face melts."
    show layer master:
        yoffset 500 
        ease 1.4 yoffset 600
    "I feel like I'm losing myself."
    "The void gets ever darker."
    "Ever deeper."
    "All the light touches..."
    play sound "mod_assets/lk.mp3"
    show lionking zorder 6:
        alpha 0 
        yoffset -600
        linear 1 alpha 1 
    extend "is our kingdom."
    "Mufasa" "\"A king's time as ruler rises and falls like the sun. One day, Simba, the sun will set on my time here, and will rise with you as the new king.\""
    "Simba" "\"And this will all be mine?\""
    "Mufasa" "\"Everything.\""
    "Simba" "\"Everything the light touches.  What about that shadowy place?\""
    "Mufasa" "\"That's beyond our borders. You must never go there, Simba.\""
    "Simba" "\"But I thought a king can do whatever he wants.\""
    "Mufasa" "\"Oh, there's more to being king than... getting your way all the time.\""

  

    "Simba" "\"There's more?\""
    "Mufasa" "\"Simba...\""

    

    "Mufasa" "\"Everything you see exists together, in a delicate balance. As king, you need to understand that balance, and respect all the creatures-- from the crawling ant to the leaping antelope.\""
    "Simba" "\"But, Dad, don't we eat the antelope?\""
    "Mufasa" "\"Yes, Simba, but let me explain. When we die, our bodies become the grass. And the antelope eat the grass. And so we are all connected in the great Circle of Life.\""
    show monika forward happ om lpoint casual ce at l31 zorder 30:
        yoffset -600
    m "Good morning, sire!"
    show monika sad cm 
    "Mufasa" "GOD, FUCK OFF, MONIKA!"
    call dclose 

    show layer master:
        yoffset 100 
        ease 1.4 yoffset 300
    "Is a rope."
    "A singular rope."
    "And so I climb."
    "Every ounce of my strength is attributed to pulling myself up."
    "At first, I'm going at a decent pace."
    "But eventually, I slow to a crawl."
    "My body can't take it."
    "But I must."
    "I must push on!"
    "I climb and I climb, the never ending struggle!"
    "My entire body is just a puddle of implications and suggestions!"
    "Am I here?"
    "Is here even real?"
    "Am I real?"
    "My surroundings warp around, shades of colour so extravagant, that we have no words for it."
    "It's like I can see a whole new spectrum of light!"
    "The colours!"
    show veins onlayer front 
    "My retinas bleed in, my eye sockets bulge out."
    "I can't feel my body."
    "I can't see the rope!"
    "The weight of the entire world is on me!"
    "The pain!"
    "The suffering!"
    "AAAAAAAAAAAAAAAAAAAAAAAAAA--{nw}"
    show white onlayer master zorder 3:
        alpha 0
        linear 1 alpha 1
    #flash of white light
    #blinking animation
    pause 1.5 
    scene white 
    window hide 
    hide white onlayer front 
    scene black with close_eye 
    pause .15 
    scene black 
    show madden happ based at i11 
    with open_eyes 
    "Wh-what…?"
    "Where am I?"
    show madden at f11 
    jm "Hello, child."
    show madden at t11 
    mc "Who are you?"
    show madden at f11 
    jm "I am The Master of football strategy."
    show layer master:
        ease 3 zoom 1.15 rotate 25 
    jm "Arbiter of all things pigskin."
    jm "I see you have found my realm."
    show madden at t11 
    mc "Are you…"
    mc "Are you God?"
    show madden at f11 zorder 2 
    jm "Hahahaha!"
    jm "So, child…"
    jm "In the name of the hall of fame, would you like to join me in my never ending battle for all things football?"
    jm "Follow my teachings and you shall become a football man."
    mc "I'm honestly more of a soccer guy."
    show madden mad 
    pause 5.0
    window hide 
    show layer master at anxiety 
    show noise zorder 1 
    show white onlayer front:
        alpha 0
        linear 5 alpha 1 
    show madden:
        dizzy(1.5,.01)
        1
        dizzy(3,.01)
        1 
        dizzy(5,.01)
    pause 5 
    stop sound 
    stop music 
    scene bg sroom 
    hide white onlayer front 
    #madden shakes
    #mc disintegrates
    #screams of the damned
    #white flash
    #madden jumpscare
    #back to black screen
    play ambient birds 
    "What!?"
    "Huh!?"
    "What just…"
    "Ugh."
    "Must've been a dream."
    "..."
    "For some reason, I want to play some Madden 08."
    "Vince Young is calling to me."
    "Anyway..."
    hide veins onlayer front
    stop ambient 
    call dclose 
    return

    #transition to next skit
label dib:
    "I gently open the door."
    play sound opend 
    scene bg sroom 
    show yuri turned mib neut at t33 
    show natsuki turned mib doub cm at t31
    show sayori turned casual lup cm oe ldown rdown at t11 
    with wipeleft_door 
    #DiB and Sayori

    show natsuki om at f31 
    n "Okay, where's the baby!?"
    show natsuki angr cm at t31
    show sayori om rup at f11
    s "I-I don't know, I swear!"
    show sayori cm neut at t11
    show yuri om at f33  
    y "Look, Sayori, I'm a nice, shy, quiet girl."
    y "I'd let you relax, maybe have a nice sip of tea-"
    show yuri anno cm at t33 
    show sayori neut om at f11 
    s "I prefer juice."
    show sayori cm at t11
    show yuri om at f11 
    y "{i}Tea{/i}, while you got more cooperative, but my partner here..."
    show natsuki neut om at f31 
    show yuri cm neut at t33 
    n "S'up."
    show natsuki cm at t31 
    show yuri dist om at f33 
    y "She's a bit more chaotic."
    show yuri cm neut at t33 
    show natsuki om happ at f31 
    n "I once bit off a suspect's ear."
    show natsuki cm neut at t31
    show yuri om at f33  
    y "I was there. I can confirm."
    show natsuki cm at t31 
    show yuri neut cm at t33 
    mc "Uh, what's going on!?"
    show yuri om lsur at hf33 
    show natsuki om lsur at hf31 
    ny "Huh!?"
    show natsuki cm at t31 
    y "How did he get in here!?"
    show yuri cm at t33 
    n "..."
    show yuri curi om at f33  
    y "Did you leave the door unlocked?"
    show yuri neut at t33 
    n "..."
    mc "Natsuki, Yuri, why are you dressed up like this?"
    show natsuki doub om at f31 
    n "We ain't the Nat and Yuri you know."
    n sedu "We're the DiB."
    show natsuki cm at t31 
    show yuri om neut at f33 
    y "The Dokis in Black."
    show yuri cm at t33 
    show natsuki neut om at f31 
    n "Not the Black Dokis. We get confused a lot."
    show sayori neut om at f11 
    show natsuki anno cm at t31 
    s "That sounds racist."
    show natsuki doub om at f31 
    n "It is racist. Have you seen Tiffa--{nw}"
    stop music 
    show yt onlayer front 
    pause 1  
    #DMCA Copyright notice
    #snap back to reality
    hide yt onlayer front 
    mc "Okay then, DiB, why are you here?"
    show natsuki neut om at f31 
    n "We're here looking for a baby."
    show natsuki cm at t31
    mc "A baby?"
    show yuri neut om at f33 
    y "Yes. This baby is the centre of a time anomaly that needs to be fixed before the entire timestream collapses in on itself."
    show yuri cm at t33 
    show sayori curi om lup at f11 
    s "I don't have a baby!"
    show yuri flus n3 
    show natsuki anno 
    show sayori cm at t11 
    mc "Yet."
    show lsur om at f11 
    s "...oh!"

    show sayori laug n3 cm at t11
    "Sayori seductively looks at me."
    "I wink."
    show sayori lsur 
    show yuri -n3 
    show natsuki om ce at f31 
    n "Leave the flirting for the bedroom, fellas."
    show sayori curi om at f11 
    show natsuki cm at t31 
    s "But you're in my bedroom."
    show yuri om at f33 
    show sayori cm neut ldown rdown at t11 
    y "We're looking for this baby in particular."
    show yuri cm at t33 
    "Yuri shows me a picture of a particularly cute baby that has pink eyes."

    mc "Oh yeah, I threw it in the garbage."
    show natsuki angr om oe at f31 
    n "You threw me in the--"
    show natsuki ce doub at f31 
    n "Nevermind. Okay listen, [player], you're going to need to grab the baby from the trash and wear this."
    show natsuki at d31 
    "Natsuki holds up the attire of a Garapagalos delivery-person."

    mc "Why?"
    show yuri om at f33 
    y "To seal the time loop that this baby is the centre off."
    show yuri cm at t33 
    mc "Will you stop bothering us if I do it?"
    show yuri om at f33 
    y "Yes."
    show yuri cm at t33 
    mc "Fine, I guess."
    show yuri dist 
    show natsuki dist 
    show sayori e2d 
    "I start to switch into my delivery attire."
    show sayori n4 
    "Natsuki and Yuri look away, while Sayori keeps looking at me."
    show sayori worr -e2d at f11 
    s "Come quick, okay?"
    show sayori cm at t11 
    mc "I sure hope not."
    show sayori -n4 happ 
    "We chuckle to ourselves."
    show yuri neut 
    show natsuki neut 
    "I finally get dressed and tell the girls that they can look again."
    show natsuki om at f31 
    n "Anyway, we're going to have to stop by Guam on the way, so we can time travel back."
    show natsuki cm at t31 
    mc "What's Guam?"
    show yuri happ om at f33 
    show sayori lsur 
    y "It's a sidespace dimensional city where DiB headquarters are centred at."
    show yuri cm at t33 
    mc "Sidespace dimensional city..?"
    show sayori om rup at f11 
    s "Big words make me go boom boom."
    show sayori cm at t11
    show natsuki om curi at f31 
    n "You ready, [player]?"
    show natsuki cm neut at t31 
    "I shrug my shoulders."
    show natsuki om at f31 
    n "Good enough."
    show natsuki cm at t31 
    call dclose 
    return
    #close door
label rank:
    "I gently open the door."
    play sound opend 
    scene sroom 
    show sayori turned happ cm casual at t11 
    show natsuki cross nuet cm at t33  
    show yuri turned cm neut ldown rdown at t31 
    with wipeleft_door 
    #sayori, natsuki, yuri
    show sayori happ om at f11 
    s "Okay, guys, welcome to the Friend Ranking Competition!!!"

    #applause

    s ce "Today on Friend Ranking, I'll be ranking my best-ever friendies..."
    show sayori at hf11 
    s oe "The Literature Club!"
    show sayori cm at t11 
    "I lean over to Yuri and Natsuki."

    show yuri lsur 
    show natsuki curi 
    mc "So, you guys nervous?"

    show natsuki turned curi om rhup at f33 
    n "Dude, I've been pampering her for an entire month trying to win this!"
    n ce "Of course I'm nervous."
    show natsuki dist cm at t33 
    show yuri neut om rup at f31 
    y "I would like to think Sayori and I are very close."
    show yuri cm at t31 
    mc "I'm her childhood friend, so I'm pretty sure I'll win."
    #show natsuki doub om at f33  
    #n "Yeah, but you're a boy."
    #show natsuki cm curi at t33 
    #mc "Exactly."
    #show natsuki om at f33 
    # "What does that mean?"
    #how natsuki vsur cm at t33 
    #"I wink at Natsuki."
    #show natsuki rdown ce om at f33  
    #n "Ew, ew, ew, ew."
    show natsuki worr at t33 
    s "Okay, buddies, are you ready?"
    show natsuki flus om ce lhip at f33 
    n "Just tell us the rankings."
    show natsuki cm 
    show sayori nerv om at f11 
    s "Alright, alright."
    show sayori happ 
    s "So, at third place, we have..."
    show yuri shy n3
    show natsuki worr n3 
    show layer master:
        truecenter 
        linear 4.201 zoom 1.35
    play sound "mod_assets/dr1.mp3"
    pause 4.201
    #drum roll
    play sound "mod_assets/dr2.mp3"
    show sayori lup neut om at f11   
    show natsuki dist -n3 n2 
    show yuri turned sad -n3  
    s "Yuri."
    show sayori cm at t11 
    show yuri om at f31 
    show sayori sad 
    y "Oh."
    y ce "Expected, but still disappointing."
    show sayori om at f11 
    show natsuki neut 
    s "Don't be sad Yuri!"
    show sayori happ rup 
    s "Your big boobies always have a place in my heart!"
    show sayori ce cm ldown rdown at t11 
    show yuri dist om at f31 
    y "I appreciate the sentiment, Sayori."
    show sayori neut om oe at f21 
    show yuri cm neut at lhide 
    hide yuri 
    show natsuki at t22  
    s "Now for second place..."
    show natsuki sedu om rhip at f22 
    n "Are you ready to eat my dust, [player]?"
    show natsuki anno at t22 
    mc "I doubt she'll pick you before me."
    show natsuki lsur 
    show sayori happ om ce rup at f21 
    show natsuki shoc 
    s "Mr. Cow!"
    show natsuki angr om at f22 
    show sayori cm neut at t21  
    mcn "Mr. Cow!?"
    show sayori happ om rup at f21
    show natsuki cm at t22 
    s "Mr. Cow is always with me."
    s ce "Plus he also has big udders!"

    show sayori cm at t21 
    "Wouldn't that make him a she???"
    "Questions for later."

    show sayori neut oe rdown om ldown at f21
    s "Now for first place..."
    show natsuki laug ce lhip  om at f22 
    n "This is gonna be me."
    show natsuki angr cm rdown ldown at t22 
    mc "C'mon Natsuki, don't get your hopes up."
    show natsuki pout om at f22 
    n "I have a feeling, though."
    show natsuki anno cm at t22 
    mc "I'm surprised your dad didn't beat all the feeling out of you."
    show natsuki om at f22 
    n "Low blow, [player]."
    show natsuki cm vang at t22 
    mc "Like the ones your dad gave to you?"
    show natsuki om at f22 
    n "You son of a--"
    show natsuki shoc cm at h22 
    show sayori angr om lup at hf21 
    s "Natsuki!"
    show sayori cm at t21 
    show natsuki happ 
    mc "What?"
    show natsuki om e3a at f22 
    n "HAHA EAT MY SHORTS, [player]!"
    show natsuki -e3a cm at t22 
    mc "I thought..."
    show natsuki at t21 zorder 1 
    show sayori happ 
    pause .3 
    show natsuki at t22 
    "Natsuki goes over and hugs Sayori super tightly."
    show natsuki at thide 
    hide natsuki 
    show sayori happ at t11  
    "I limp over."
    "Huh. This is how rejection feels like."

    show sayori worr om rdown lup at f11 
    s "[player], are you sad?"
    show sayori cm at t11 
    mc "N-no…"
    mc "Yes."
    mc "Yes, I'm very sad."
    mc "We're childhood friends, Sayori."
    mc "I thought I was your best buddy."
    show sayori sad om at f11
    s "Well, we're not buddies."
    show sayori cm at t11 
    mc "We're not!?"
    show sayori om at f11 
    s "No, because I..."
    show sayori cm at t11 
    n "Oh god, I don't like where this is going."
    mc "Where what is going?"
    show sayori om at f11 
    s "Because I love you."
    show sayori n3 cm ldown rdown dist at t11 
    mc "..."

    "I'm stunned."

    mc "Sayori, are you for real?"
    show sayori cry 
    "She nods her head repeatedly."

    mc "Wow, I..."
    mc "Well Sayori, I love y--{nw}"
    show monika forward om lpoint happ ce at l31 
    show sayori angr 
    m "Hey guys, I heard you were doing a friend ranking competition!"
    show monika cm lsur 
    mc "OH MY GOD, FUCK OFF MONIKA!"
    show monika sad 
    show natsuki turned vang om at r33
    n "SERIOUSLY, FUCKIN' BITCH!"
    show natsuki cm 
    show sayori vang om lup at f11 
    s "LIKE WOW, I DIDN'T INVITE YOU FOR A REASON!"
    s ce "YOU'RE NOT EVEN MY FRIEND!"
    show monika cry om at l31 
    show sayori cm at t11 
    m "I thought..."
    show monika cm 
    show sayori om at f11 
    s "YEAH WELL, THINK OUTSIDE!"
    s doub "Dumb skank."
    show sayori cm at t11 
    show monika ce 
    pause .5 
    show monika at lhide 
    hide monika 
    call dclose 
    return 
    #monika crying

    #y "That was absolutely deserved."
    ##s "Obviously."
    #n "Yeah fuck her."

    #close door
label baby:
    "I gently open the door."
    "Were you worried I was going to try and call you out again FiT?"
    play sound opend 
    scene bg sroom 
    show sayori turned casual vsur cm oe at t22:
        dizzy(.15, .01)

    "I see a Garapagalos package in the middle of the room."
    "Sayori is cowering in fear, poking it with a stick."

    mc "Uhh, Sayori, why are you poking a cardboard box with a stick?"
    show sayori pani om at hf22 
    s "It's crying, [player]."
    show sayori cm at t11 
    mc "The box is crying?"
    show sayori om at f11 
    s "It's crying!"
    show sayori cm at t11 
    mc "Uh huh."
    mc "I don't hear anythin--{nw}"
    play sound baby 
    #play cry sfx
    pause 2 
    "Shocked, I cower behind Sayori."

    mc "Why is the box crying!?!?"
    show sayori cry om lup at f11 
    s "I don't know!"
    show sayori cm at t11 
    mc "Did you order it!?"
    show sayori angr om at f11 
    s "No! Some guy just gave it to me!"
    s neut ldown rdown "Kinda looked like you, actually."
    show sayori cm at t11
    mc "Did you open it?"
    show sayori worr om at f11
    s "N-no!"
    show sayori cm at t11 
    mc "Then go open it!"
    show sayori doub om at f11
    s "You do it!"
    show sayori cm at t11 
    mc "No, you!"
    #show sayori angr om at f11
    #s "You're the man!"
    #show sayori cm at t11 
    #mc "That's sexist."
    show sayori angr om at f11
    s "Just do it, [player] or I'll kill myself!"
    show sayori cm at t11 
    mc "Oh wow, so killing yourself is so worthless now that we're using it as an ultimatum in an unrelated situation."
    show sayori at thide 
    hide sayori 
    "Sayori, tired of my whining, pushes me towards the crying box."
    show vignette with dissolve 
    "I gulp and proceed to slowly tear it open."
    "Leaning in, I take a glimpse of what's inside."
    hide vignette with dissolve 
    mc "Huh..."
    show sayori turned worr om casual at f11 
    s "So? What's inside?"
    show sayori cm 
    mc "A baby."
    show sayori curi rup om at f11 
    s "A what?"
    show sayori neut cm at t11 
    mc "A baby."
    mc "There is a baby inside the package."
    show sayori curi rup om at f11 
    s "Why is there a baby inside the package?"
    show sayori anno cm at t11 
    mc "It's your package, why would I know?"
    mc "Did you order a baby in a package?"
    show sayori ce om rdown at f11 
    s "No, [player], I did not order a baby in a package."
    show sayori cm att11 
    mc "Then why is there a baby inside this package?"
    show sayori angr om oe at hf11 
    s "I don't know!"
    show sayori anno ce at d11 
    "Sayori sighs, obviously fed up with the situation."
    show sayori oe neut
    "She leans in and looks at the now calm baby."

    mc "Hey, it stopped crying."
    show sayori neut om at f11 
    s "Yeah, it..."
    show sayori happ 
    s "It did."

    show sayori lsur cm at t11 
    "Sayori's eyes dilate, her hands shake and her lips are left ajar."
    "She doesn't want to admit it, but it seems that Sayori has found love."
    show sayori om at f11 
    s "Wow..."
    show sayori cm at t11 
    mc "Please don't have a maternal moment, Sayori."
    show sayori happ rup lup at f11 
    s "But it's so cute!"
    show sayori cm at t11 
    pause 1.0
    play sound baby 

    mc "Great, now it's crying."
    mc "Thanks Sayori."
    show sayori worr om at f11
    s "Do you think it did a poopie?"
    show sayori cm neut at t11
    mc "It doesn't smell like it, so I would guess not."
    show sayori dist om at f11 
    s "Hm…"
    s curi "Then why is it crying?"

    show sayori cm at t11 
    "Sayori starts to gently shake the baby."

    show sayori sad om rup at f11 
    s "C'mon little baby, why're you crying?"
    show sayori cm at t11 
    mc "Here, lemme try."
    show sayori neut at t22 

    show nbaby with dissolve:
        truecenter 
        zoom .5
    "Sayori hands me the crying abomination."
    "I grab it from below its armpits."
    show layer master:
        truecenter 
        ease 2 zoom 1.3
    "I look deep into its odd pink eyes."

    mc "So…"
    show sayori vsur rup at h22 

    show nbaby:
        truecenter 
        zoom .5
        dizzy(1.5,.01)
    "I start to violently shake the eldritch being."
    
    mc "TELL ME YOUR SECRETS, CHILD!"
    show sayori cry om at f22 
    s "STOP, [player] YOU'RE HURTING THE CUTE BABY!"
    show sayori vsur cm at h22
    $ style.say_dialogue = style.edited
    n "DON'T CALL ME CUTE!"
    $ style.say_dialogue = style.normal
    show layer master 
    mc "AHH!"
    s "AHH!"
    show nbaby:
        truecenter
        zoom .5 
        alpha 1 
        yoffset 0
        parallel:
            ease 1 rotate 1000 zoom 0 yoffest -400 
        parallel:
            .6
            linear .4 alpha 0 
    #baby natsuki gets thrown out of the window transform
    pause .6
    play sound "mod_assets/glass.mp3"
    pause .4 

    play sound "mod_assets/alarm.mp3"
    pause 2 
    #show sayori neut om at f22  
    #s "So we just killed a baby."
    #show sayori cm at t22 

    #pause 15

    #mc "Cool."
    call dclose 
    #close door
label nvm:
    call dopen 
    "On second thought, I'd rather not."
    "I gently close the door."
    call dclose 
label sdrip:
    "I gently open the door."
    play sound opend 
    scene bg sroom 
    with wipeleft_door
    play sound "mod_assets/drip.mp3"
    show sdrip at i11  
    pause .2 
    scene black 
    stop sound 
    return 
label lights:
    scene black 
    "I gently open the door."
    play sound opend 
    "It's dark and cold."
    "I can't make out a single shape of figure."
    "I'm lost in a silent, empty yet vast void."
    "Where am I?"
    "Wait..."
    "Did I forget to turn the lights on?"
    scene sroomn
    show s_killb
    play sound "gui/sfx/select.ogg" 

    #nighttime sayori bg with her hanging.
    "Phew. That's better."
    call dclose 
    return
label comedy:
    call dopen 
    mc "Hi."
    show sayori happ om oe lup rdown at f11 
    s "Heyaaa!"
    show sayori cm at t11 
    pause 1 
    show sayori neut 
    pause 1

    mc "I can’t think of anything funny to say."
    show sayori om at f11 
    s "Yeah me neither."
    show sayori cm at t11 
    mc "..."
    s dist "..."
    show sayori neut 
    mc "Being funny is hard."
    show sayori happ om at h11 
    s "Oh I got it!"
    show sayori cm at h11 
    pause .15 
    hide sayori 
    call skz 
    play sound sting 

    mc "Oh yeah! That should be funny!"
    mc "..."
    mc "Eh, it was funnier the first time around."

    call dclose 
    return 
label dad:
    "I gently open the door."
    play sound opend 
    scene bg sroom 
    show sayori hang lsur om at skillr:
        yoffset 350 zoom .82
    with wipeleft_door 
    s "[player], I’m dying!"
    show sayori cm 
    mc "Hi dying, I’m [player]!"
    show sayori neut m1
    s "Please help me!"
    show sayori -m1 cm angr 
    mc "I would, but I don’t see {i}me{/i} anywhere around here!"
    show sayori angr om
    s "I…hate…you…"
    show sayori cm 
    mc "I’ll pass the message onto you when I see him."
    call dclose 
    return 
label immortal:
    "I gently open the door."
    play sound opend
    scene bg sroom 
    show s_kill at skillr 
    with wipeleft_door 

    show vignette with dissolve 
    "Oh no!"
    "Sayori…"
    "She's…"
    "She's dead--{nw}"
    hide s_kill 
    hide vignette 
    show sayori hang om oe at skillr 
    s "[player], help me get down!"
    show sayori cm 
    mc "Huh!?!?"
    mc "You're alive?"
    show sayori om 
    s "Yes, now help me get out of this noose!"
    show sayori cm 
    mc "I don't understand."
    mc "How does that work?"
    s dist om "Well I tried to kill myself…"
    s lsur "But I guess I'm immortal?"
    show sayori cm 
    mc "Huh. Neat."
    s neut om "So, will you help me get down?"
    show sayori anno cm 
    mc "I don't know, I kinda have some eggs to attend to..."
    mc "I'll go check up on that and I'll come back."
    s pout om "I'm literally suffocating."
    show sayori cm 
    mc "You'll live."
    s om "I-"
    show sayori cm 
    call dclose 
    return
label lmao:
    call dopen 
    show sayori om dist at f11 
    s "I’m depressed."
    show sayori cm at t11 
    "I don’t know how to feel. The burden of someone’s feeling is so great…"
    show sayori lsur 
    mc "Lmao ok."
    show sayori angr om ldown rdown at f11 
    s "You’re mean."
    show sayori cm at t11 
    mc "Okay lmao."

    "Oh my God, what’s happening, did I forget..?"
    show sayori anno ce om at f11 
    s "Stop saying lmao out loud, it’s really weird and stupid."
    show sayori cm at t11 
    mc "Lmao it’s a condition."
    show sayori neut om oe at f11 
    s "Why are you crying?"
    show sayori worr cm at t11 
    "My feet become weak and I fall to my knees."

    mc "My medicine, lmao, I lost my medicine lmao."

    "Lmao it’s invading my thoughts."
    show sayori shoc 
    mc "I can’t stop lmao lmao."
    mc "Help lmao lmao lmao."

    "Lmao Lmao LMao Lmao Lmao Lmao..."
    show sayori vang om lup lgun e1g at f11 
    #you see her raise the gun into her hands
    s "[player]!"
    show sayori cm e1h at t11 
    mc "Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao Lmao {nw}"
    window hide 
    play sound shot
    scene black 
    pause 2
    play sound fall 
    pause 1.5 
    play sound closed  
    #close door
    #mc "Why do you have a gun in your hand?"
    #s "Oh, it’s a Chekov’s gun!"
    #mc "I feel like someone else would appreciate that more than I would."
    window hide 
    pause 2 
    return 

label flying:
    "I gently open the door."
    play sound opend 
    scene bg sroom 
    show sayori hang neut om at skillr:
        yoffset 350 zoom .82
    with wipeleft_door 
    #sayori hanging by the noose

    s "Look, [player], I’m flying!"
    show sayori cm 
    mc "You’re hanging."
    s pout om "I’m {i}flying{/i}."
    show sayori angr cm 
    mc "You’re going to die."
    s neut om "We all die eventually."
    s anno "You’re just jealous I’m going to die flying."
    show sayori cm neut 
    call dclose
label higher:
    
    "I gently open the door."
    play sound opend 
    scene black 
    show mooncrawl zorder 0:
        truecenter
        zoom .86 
        xoffset 5 yoffset -1166 
    show s_kill zorder 1:
        zoom .26  
        truecenter 
        subpixel True  
        xoffset 100 yoffset -350 zoom .8 
    show windowcut zorder 2:
        subpixel True  
    show sayori hang dist cm at skillr zorder 3:
        subpixel True  
        yoffset 350 zoom .82
    with wipeleft_door 

    s om "No... It's too low."
    s neut "We need to go higher."
    window hide  
    show sayori cm zorder 99:
        subpixel True 
        block: 
            ease 1 zoom 14 xoffset -5400 yoffset -900
    show windowcut zorder 2:
        truecenter 
        subpixel True
        parallel:
            ease 1 zoom 10.42 xoffset -4000 yoffset -642
        parallel:
            .7 
            ease .3 alpha 0
    show mooncrawl zorder 0:
        truecenter 
        zoom .86 xoffset 5 yoffset -1166
        subpixel True 
        block:
            ease 1 zoom 1.07 yoffset -1746 xoffset 0 
    show s_killb zorder 1:
        subpixel True
        truecenter  
        zoom .16 yoffset 120  xoffset -320 alpha 0 
        ease 1 zoom .192 yoffset 142-300  xoffset -359 alpha 1 
    pause 1 
    "I gently leave the house."
    hide windowcut 
    hide sayori 
    hide s_killb
    #sayori hanging from the roof
    show sayori hang neut om:
        truecenter 
        zoom .153 yoffset 142-319 xoffset -359
    s "No... Higher..."
    show sayori cm 
    mc "sayori, stop."
    show sayori om 
    s "Higher."
    show sayori cm anno 
    mc "sayori jesus fuck."
    show sayori angr om 
    s "I WANT TO GO HIGHER, VARIOUS ARTISTS!!!"
    show sayori cm 
    mc "sigh"
    window hide  
    "... I gently go to the moon."
    #sayori hanging from the moon.
    #{wait for 2 seconds}

    s "..."
    s "Higher."
    return  
label dopen:
    "I gently open the door."
    play sound opend 
    scene bg sroom 
    show sayori turned neut cm oe ldown rdown at t11 
    with wipeleft_door 
    return 
label dopenh:
    "I gently open the door."
    play sound opend 
    scene bg sroom 
    show s_kill
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

    