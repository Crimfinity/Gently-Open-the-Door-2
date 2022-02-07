label skit_beginning:


    stop music fadeout 3.0
    scene bg house
    with dissolve_scene_full
    "I reach Sayori's house and knock on the door."
    "I don't expect an answer, since she's not picking up her phone, either."
    "Like yesterday, I open the door and let myself in."

    scene black with wipeleft_door
    mc "Sayori?"

    "She really is a heavy sleeper..."
    "I swallow."
    "I can't believe I ended up doing this after all."
    "Waking her up in her own house..."
    "That really is something that a boyfriend would do, isn't it?"
    "In any case..."
    "It just feels right."
    "Outside Sayori's room, I knock on her door."

    mc "Sayori?"
    mc "Wake up, dummy..."

    "There's no response."
    "I really didn't want to have to enter her room like this..."
    "Isn't it kind of a breach of privacy?"
    "But she really leaves me no choice."
    "I gently open the door."

    mc "{cps=30}.......Sayo--{/cps}{nw}"


    window hide(None)
    window auto
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_killb as s_kill at s_kill_start
    pause 3.75
    "..."
    "Oh my God."
    "You know what?"

    stop music
    "Fuck this shit."

    play music d_rev
    show noise zorder 100 at noise_alpha
    show vignette zorder 100 at vignetteflicker(-2.030)
    show layer master at rewind
    "{cps=150}You know what?{/cps}{nw}"
    "{cps=150}Oh my God.{/cps}{nw}"
    "{cps=150}...{/cps}{nw}"

    scene black
    show noise zorder 100 at noise_alpha
    show vignette zorder 100 at vignetteflicker(-2.030)
    show layer master at rewind
    mc "{cps=150}.......Sayo--{/cps}{nw}"
    "{cps=150}I gently open the door.{/cps}{nw}"
    "{cps=150}But she really leaves me no choice.{/cps}{nw}"
    "{cps=150}Isn't it kind of a breach of privacy?{/cps}{nw}"
    "{cps=150}I really didn't want to have to enter her room like this...{/cps}{nw}"
    "{cps=150}There's no response.{/cps}{nw}"
    mc "{cps=150}Wake up, dummy...{/cps}{nw}"
    mc "{cps=150}Sayori?{/cps}{nw}"
    "{cps=150}Outside Sayori's room, I knock on her door.{/cps}{nw}"
    "{cps=150}It just feels right.{/cps}{nw}"
    "{cps=150}In any case...{/cps}{nw}"
    "{cps=150}That really is something that a boyfriend would do, isn't it?{/cps}{nw}"
    "{cps=150}I can't believe I ended up doing this after all.{/cps}{nw}"
    "{cps=150}I swallow.{/cps}{nw}"
    "{cps=150}She really is a heavy sleeper...{/cps}{nw}"
    mc "{cps=150}Sayori?{/cps}{nw}"

    scene bg house
    show noise zorder 100 at noise_alpha
    show vignette zorder 100 at vignetteflicker(-2.030)
    show layer master at rewind
    "{cps=150}Like yesterday, I open the door and let myself in.{/cps}{nw}"
    "{cps=150}I don't expect an answer, since she's not picking up her phone, either.{/cps}{nw}"

    hide noise
    hide vignette
    show layer master
    stop music fadeout 1.0
    "I reach Sayori's house and knock on the door."
    "I don't expect an answer, since she's not picking up her phone, either."
    "Like yesterday, I open the door and let myself in."

    scene black with wipeleft_door
    "Alright, no more messing around."
    "I quickly run upstairs and get ready for what's to come."

    stop music fadeout 3.0
    scene black with dissolve_scene_full

    return

label skit_melons:

    "I gently open the door."

    play sound closet_open
    scene sroom
    show sayori turned casual melons happ ce cm at i(1, 1)
    with wipeleft_door
    play music tsayori
    mc "Uhh…"

    show sayori lsur om oe at f(1, 1)
    s "Uhh…"

    show sayori cm at t(1, 1)
    mc "So, like…"

    show sayori nerv om at f(1, 1)
    s "I can explain."



    show sayori cm at t(1, 1)
    mc "Please don't."

    stop music
    scene black
    play sound closet_close
    with wipeleft_door
     
    return

label skit_towel:

    "I gently open the door."

    play sound closet_open
    scene bathroom
    play music tnatsuki
    show natsuki turned towel lhip rhip angr om oe at f(1, 1)
    with hpunch

    n "Dude what the hell!?"
    show natsuki cm at t(1, 1)

    mc "Whoops! Wrong room."
    mc "Sorry Natsuki."

    "I close the door."

    stop music
    scene black
    play sound closet_close
    with wipeleft
    "Maybe this one..."

    play sound closet_open
    window hide(None)
    window auto
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_killc as s_kill at s_kill_start
    pause 3.75
    mc "Ah, here we are!"
    mc "Oh wait."
    mc "Shit."

    stop music
    scene black
    play sound closet_close
    with wipeleft_door

    return

label skit_loli:

    "I gently open the door."

    play sound closet_open
    scene sroom
    with wipeleft_door

    mc "Sayori?"

    play music tsayori
    show sayori kid lup rup happ om at f(1, 1)
    s "Oh hi, [player]!"
    show sayori cm ce:
        parallel:
            linear .4 xcenter 240 zoom .8 ycenter 420
            .2
            linear .4 xcenter 880
            .2
            linear .4 xcenter 400
            .2
            linear .4 xcenter 1040
            .2
            linear .4 xcenter 640
        parallel:
            .5
            easein .2 yoffset -60
            easeout .2 yoffset 0
            .2
            easein .2 yoffset -60
            easeout .2 yoffset 0
            .2
            easein .2 yoffset -60
            easeout .2 yoffset 0
            .2
            easein .2 yoffset -60
            easeout .2 yoffset 0
            .2
    "She jumps up and down and all around eventually hugging me by the waist."
    mc "Umm, when did you get so short?"
    show sayori lsur ldown rdown om oe at f(1, 1)
    s "When did you get so tall?"
    show sayori cm at t(1, 1)
    mc "I've... always been this tall?"
    show sayori happ om at f(1, 1)
    s "So, whatcha doin' in my room?"
    show sayori sedu n3
    s "I hope you're not hoping to do some--"
    show sayori lsur -n3 at h_
    mc "NO--!"
    mc "Nopenopenope...nope!"
    mc "No."
    mc "I'm good."
    mc "If I wanted to do that,{w} I'd go to Natsuki, thank you very much."

    stop music
    scene black
    play sound closet_close
    with wipeleft_door

    return


label skit_uwu_slam:

    "I swing the door open, full force."
    mc "Sayori!"

    play sound door_slam
    scene sroom
    with hpunch
    "I hear a loud thump from behind the door."
    s "Uwaa~!"
    mc "Sayori?"
    show sayori turned pani cm ce at t(1, 1)
    "I peek around the door to see Sayori on the ground, clutching her nose."
    mc "Shit, sorry Sayori."
    show sayori sedu om oe n4 at f(1, 1)
    s "It's okay..."
    show layer master at master_camera
    s mn "Maybe do it harder next time~?"
    mc "..."
    play music t7g
    show noise onlayer front:
        alpha 0.0
        2.0
        easein 8.0 alpha .9
    mc "{cps=*0.2}AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA{/cps}{nw}"

    stop music
    scene black
    hide noise onlayer front
    play sound closet_close
    with wipeleft_door
    show layer master
    return

label skit_self_defence_noose:

    "I gently open the door."

    scene sroom
    play sound closet_open
    with wipeleft_door

    "Huh?"
    mc "Sayori, are you hiding somewhere?"
    "Suddenly, I feel something wrap around my neck, choking me." with vpunch
    s "Hi-yah!"
    "Sayori doesn't release her grip until my vision fades to black."
    scene menu_bg
    show sayori turned rnoose happ cm ce at i(1, 1)
    with dissolve_scene_full
    play music lobby_time
    show sayori om at f(1, 1)
    s "I'm so lucky I was able to save myself with my self-defence noose!"
    s neut oe "Now, you may be wondering, how can I get one of these to protect my home from intruders?"
    show sayori at h_
    s happ "Well… {w}I'll tell you!"
    show sayori at f(2, 1)
    show ad_1 zorder 5:
        xcenter 1920
        easein 1.0 xcenter 640
    show ad_2 zorder 6:
        ycenter -1080
        .5
        easein_bounce 2.0 ycenter 360
    s "Call or text the number on your screen right now to place your order!"
    show sayori ce at h_
    s "But wait, there's more!"
    s oe "Call in the next twenty minutes to get half off of your noose!"
    show sayori cm at t(2, 1)
    mc "Psst... You didn't say how much they cost."
    show sayori nerv om at f(2, 1)
    s "Right...!"
    show ad_3:
        alpha 0.0 zoom .1 truecenter
        easein .7 alpha 1.0 zoom 1.0 rotate 720
    show sayori at f(4, 2)
    s happ "Come buy one for only $19.99!"
    show sayori at h_
    s ce "And if you call in the next ten, we'll throw in a copy of 'Doki Doki Cliche Club'!"
    s neut oe "Don't forget, you get a free self defence landmine as well!"
    s happ "This is the best purchase twenty dollars can get you. Isn't that right, [player]?"
    show sayori cm at t(4, 2)
    mc "Uh... Yeah."
    stop music
    show green_screen zorder 50
    show sayori om zorder 51 at f(1, 1)
    s "Okay, think we're good!"
    s ce "Thanks, [player]."
    show sayori cm at t(1, 1)
    mc "Anytime."

    stop music
    scene black
    hide noise onlayer front
    play sound closet_close
    with wipeleft_door

    return

label skit_rainclouds:

    "I gently open the door."

    scene sayori_bedroom_night
    play sound closet_open
    show sayori turned lumb sad cm ce at i(1, 1)
    show sayori at night_filter
    show rain_1 as r1 zorder 50
    show rain_2 as r2 zorder 51
    show rain_3 as r3 zorder 52
    show vignette onlayer front
    with wipeleft_door
    play music heavy_rain

    "It's raining."
    "Wait…"
    "What?"
    mc "How is it raining inside your room, Sayori!?"
    show sayori mb e1b at f(1, 1)
    s "The rainclouds got a little outta hand!"
    show sayori ma at t(1, 1)
    mc "Oh."
    mc "I'm...sorry."
    show sayori mb at f(1, 1)
    s "It's fine, don't worry about it."
    s oe "It was never your fault in the first place."

    show sayori ma at t(1, 1)
    pause .75
    show sayori cm
    pause .75
    show sayori ce
    pause .75

    stop music fadeout 1.0
    scene black
    hide vignette onlayer front
    play sound closet_close
    with wipeleft_door

    return

label skit_synonyms:

    "I softly open the door."
    "Wait... that's not it."
    "Hmm..."
    "I...{w}slowly open the door?"
    "No, no."
    "It's gotta be..."
    "Lightly?"
    "Nope."

    show sayori turned angr om oe:
        zoom .875 alpha 1.0 xcenter 1580 ycenter 360
        easein .25 xcenter 1180 rotate -35
    s "Come on, man, I don't have all day."
    s "I gotta kill myself eventually!"
    show sayori cm:
        ease .25 zoom .8
    mc "I know, I know! But there's like a format to this."
    mc "I just need to remember what it was."
    "I...mildly open the door?"
    "I kindly open the door?"
    "I tenderly open the door."
    show sayori ce
    "No, that's still not it."
    "I delicately open the door?"
    "I sensitively open the door?"
    "I open the door in a politically correct manner?"
    show sayori anno om oe:
        ease .25 zoom .875
    s "You know, if you put this much care in how you treated me, I probably wouldn't kill myself."
    show sayori cm:
        ease .25 zoom .8
    mc "Go whine to someone who cares, Sayori."
    show sayori om ce:
        ease .25 zoom .875
    s "Ugh, fine."
    s "Dumb bitch."
    show sayori:
        easein .25 xcenter 1580 rotate 0
    "..."
    "{i}Gently?{/i}"
    "Yeah! That's it."
    "Alright!"

    return

label skit_speech:

    "I gently open the door."

    scene sroom
    play sound closet_open
    show sayori 1by at t(1, 1)
    with wipeleft_door

    mc "Oh... hey Sayori."
    mc "Do you want to go work on those pamphlets for the festival before Monika gets mad at--{nw}"

    play music t9
    show sayori at f(1, 1)
    s 1by "Why can't it just be like it's always been?"
    s "This is all my fault."
    s "If I didn't get so weak and accidentally express my feelings..."
    s 1bk "If I didn't make that stupid mistake..."
    s "Then you wouldn't have been worried about me at all."
    s "You wouldn't have come here."
    s 1bd "You wouldn't have even been thinking about me right now."
    s "But this...is just my punishment, isn't it?"
    s "I'm getting punished for being so selfish."
    s "I think that's why the world decided to have you come over today."
    s "It just wants to torture me."
    s 4bq "Ehehe~"
    s 4bl "Ah..."
    s "Ahaha..."
    s 4by "You really put me in a trap, [player]."
    stop music fadeout 3.0
    s "The funny thing is..."
    s "I've always been like this."
    s "You're just seeing it for the first time."
    s 1bq "Ehehe~"
    s 1ba "You're really just going to make me say it, aren't you, [player]?"
    s "I guess I have no choice this time."
    s 1bc "The thing is..."
    play music t10
    s "I've had really bad depression my whole life."
    s 1bb "Did you know that?"
    s "Why do you think I'm late to school every day?"
    s "Because most days, I can't even find a reason to get out of bed."
    s 1by "What reason is there to do anything when I fully know how worthless I am?"
    s "Why go to school?"
    s "Why eat?"
    s "Why make friends?"
    s "Why make other people put their energy and caring to waste by having them spend it on me?"
    s "That's what it feels like."
    s "And that's why I just want to make everyone happy..."
    s "Without anyone worrying about me."
    s "Why do you think I didn't tell you?"
    s 1bd "Because if I told you, then you would have to waste effort caring about me instead of doing important things."
    s "I don't want to be cared about."
    s "It's bittersweet, when people try to care about me."
    s 1ba "It feels nice sometimes."
    s "But it also feels like a bat being swung against my head."
    s 4bq "Ahaha~"
    s 4ba "That's why I wanted so badly for you to make friends with everyone else..."
    s "Helping everyone be happy together is the best thing for me."
    s 1bb "But then, I discovered something else, too."
    s "Seeing you make friends and get closer with everyone in the club..."
    s 1bk "It feels like a spear going through my heart."
    s "So, that's why."
    s "That's why I decided the world just wants to torture me."
    s 1by "Every path leads to nothing but hurt."
    s "Ahaha~"
    show sayori at t(1, 1)
    mc "..."
    mc "Sayori…"
    mc "That's cool and all…"
    mc "And I feel bad for you, but…"
    stop music
    mc "Who asked?"

    show sayori 1bw
    pause .25
    stop music fadeout 1.0
    scene black
    play sound closet_close
    with wipeleft_door

    return

label skit_wrong_suicide:

    "I gently open the door."

    scene cg_pipe
    play sound closet_open
    with wipeleft_door
    play music td

    "..."
    "Damn it, wrong girl."

    stop music
    scene black
    play sound closet_close
    with wipeleft_door

    "I gently open the door."

    scene cg_bath
    play sound closet_open
    with wipeleft_door
    play music td

    "AGAIN!?"
    "Fucking hell."
    "Now my foot is damp."

    stop music
    scene black
    play sound closet_close
    with wipeleft_door

    "I gently open the door."

    scene cg_moni
    play sound closet_open
    with wipeleft_door
    play music td

    "What the fuck?"
    "How did all this blood get everywhere?"
    "Did a boxcutter knife do all that?"
    "It's on the wall too?"
    "What, did she rub her bleeding neck onto everything before passing out?"
    "Wow, Monika."
    "Just, wow!"

    stop music
    scene black
    play sound closet_close
    with wipeleft_door

    return

label skit_orgy:

    "I gently open the door."

    scene sroom
    play sound closet_open
    show monika lean n4:
        zoom .8 xcenter -100 ycenter 460 xzoom -1.0 subpixel True
        block:
            ease 4.0 zoom .75
            ease 4.0 zoom .8
            repeat
    show sayori turned censored sedu zorder 5:
        zoom .8 xcenter 200 ycenter 360
        parallel:
            linear 1.0 xcenter 1080
            linear 1.0 xcenter 200
            repeat
        parallel:
            linear .7 rotate 360
            rotate 0
            repeat
    show yuri turned censored sedu:
        zoom .8 xcenter 200 ycenter 360
        .5
        parallel:
            linear 1.0 xcenter 1080
            linear 1.0 xcenter 200
            repeat
        parallel:
            linear .7 rotate -360
            rotate 0
            repeat
    show natsuki turned censored sedu:
        zoom .8 xcenter 200 ycenter 360
        1.5
        parallel:
            linear 1.0 xcenter 1080
            linear 1.0 xcenter 200
            repeat
        parallel:
            linear .7 rotate -360
            rotate 0
            repeat
    show black as fake_door zorder 50
    with fade

    "..."
    "The door is stuck."
    "Is something banging against it?"
    "That's it..."
    mc "I'M COMING IN THERE!!"

    hide fake_door with wipeleft_door

    play music t7


    "What the fuck?"
    "The entire Literature Club is going at it!"
    "Well, except for me..."
    mc "Hey girls..."
    "They seem to ignore me."
    mc "So...{w} Can I join?"
    show sayori vang om at hf(3, 1)
    show yuri vang om at hf(3, 2)
    show natsuki vang om at hf(3, 3)
    "Everyone" "\"NO!\"" with vpunch

    stop music
    scene black
    play sound closet_close
    with wipeleft_door

    return

label skit_yuri_clothes:

    "I gently open the door."

    scene sroom
    play sound closet_open
    show sayori turned yuri lsur om at f(1, 1)
    with wipeleft_door
    play music tyuri

    show sayori turned yuri lsur om at f(1, 1)
    s "Uwaa~! They're so big!"
    mc "Sayori, what are you doing with Yuri's clothes?"
    show yuri turned censored happ om:
        zoom .875 alpha 1.0 xcenter -200 ycenter 360
        easein .25 xcenter 100 rotate 35
    y "Oh hello, [player]."
    show yuri cm at t_
    mc "...Hi?"
    pause .5
    show yuri flus cm e1a
    pause .5
    show yuri oe
    pause .5
    show yuri e1c
    pause .5
    show yuri e4a
    pause 1.0
    show yuri e1a
    pause 1.0

    mc "{cps=*.3}Yeaaahhhh{/cps}, alright. I'll just uhh...leave you guys to it."

    stop music
    scene black
    play sound closet_close
    with wipeleft_door

    return


label skit_nat_clothes:

    "I gently open the door."

    scene sroom
    play sound closet_open
    show sayori turned natsuki happ om at f(1, 1)
    with wipeleft_door
    play music tnatsuki

    s "Wow, it's so small!"
    show sayori cm at t(1, 1)
    mc "Wait...{w} what are you doing with Nat's clothes?"
    show natsuki turned censored neut om:
        zoom .875 alpha 1.0 xcenter -200 ycenter 360
        easein .25 xcenter 100 rotate 35
    n "S'up."
    show natsuki cm:
        ease .25 zoom .8
    mc "..."
    mc "Really Sayori, doing this shit again?"
    show sayori nerv om at f(1, 1)
    s "Ehehe~"
    show sayori cm at t(1, 1)
    mc "Whatever."
    show natsuki shoc n3 om
    mc "And Natsuki,{w} nice flats."


    stop music
    scene black
    play sound closet_close
    with wipeleft_door


    return

label skit_sayo_clothes:

    "I gently open the door."

    scene sroom
    play sound closet_open
    show sayori turned casual happ at t(1, 1)
    with wipeleft_door
    play music tsayori

    mc "Wait...{w} what are you doing with Sayori's clothes?"

    show sayori curi om at f(1, 1)
    s "They're mine, [player]."

    show sayori cm at t(1, 1)
    mc "Oh yeah..."
    mc "Carry on."

    stop music
    scene black
    play sound closet_close
    with wipeleft_door


    return

label skit_football:

    "I gently open the door."

    scene sroom
    play sound closet_open
    with wipeleft_door

    "I open my eyes."
    "..."
    "Here it comes."

    play music nfl
    show cg_ball
    pause 1.0

    "{b}{cps=*.2}FEAR HIM. ADORE HIM.{/cps}{/b}{nw}"

    stop music
    scene black
    play sound closet_close
    with wipeleft_door

    return

label skit_pussy:

    "I gently open the door."

    scene sroom
    play sound closet_open
    with wipeleft_door

    show sayori turned rnoose lsur om at f(1, 1)
    s "[player]!"
    s nerv "I uh..."
    s sad "I'm sorry..."

    show sayori cm at t(1, 1)
    mc "Quit being a pussy."

    show sayori lsur e1a at hf(1, 1)
    s "Huh!?"
    show sayori cm at t(1, 1)
    mc "Hang yourself, bitch, damn."
    mc "Don't just stand there."
    mc "We're here for shock value, not for you to fucking live."
    pause 1.0
    show sayori vsur cm at h_
    mc "Come on! I'm waiting!" with vpunch
    show sayori me at f(1, 1)
    s "Alright…"
    show sayori cry -me oe cm at t(-1, 1)
    "Sayroi walks over to her desk."
    show sayori at t(9, 1)
    show chair at t(9, 1):
        xzoom -0.65 yzoom 0.65 xoffset -230 yoffset 330
    "She grabs a chair and starts to drag it over."
    show sayori at t(9, 2)
    show chair at t(9, 2)
    "I look to my wrist. Ugh, we're behind schedule."
    show sayori at t(9, 3)
    show chair at t(9, 3)
    mc "Chop chop! Sayoris won't kill themselves."
    show sayori at t(9, 4)
    show chair at t(9, 4)
    mc "Oh wait!"
    show sayori at t(9, 5)
    show chair at t(9, 5)
    mc "Yeah they do!"
    show sayori at t(9, 6)
    show chair at t(9, 6)
    mc "Anywho, I'm going to make myself a grilled cheese."
    show sayori e4e
    mc "If you aren't dead by the time I'm back, I'll be very disappointed."

    stop music
    scene black
    play sound closet_close
    with wipeleft_door

    return


label skit_ropu_kun:

    "I gently open the door."
    mc "{cps=*.3}.......Sayo--{nw}"

    scene sroom
    play sound closet_open
    show sayori turned neut lup:
        xcenter 550 ycenter 0 rotate -135 zoom .8
    show ropu_kun:
        xcenter 660 ycenter 70 subpixel True zoom 0.7
        block:
            ease 1.7 rotate 5
            ease 1.7 rotate -5
            repeat
    play music td

    "..."
    "No."
    "This can't be happening."
    "After everything we've been through…"
    "After all the Sayoris that we hanged…"
    "It just couldn't take it anymore."
    "I should've seen it coming."
    "I should've!"
    "This is my fault…"
    "I ignored their problems and now…"
    show sayori anno
    mc "Ropu-kun is dead!" with vpunch
    "Screw this."
    show sayori e1c
    "Screw Sayori."
    "Screw the Literature Club."
    "I just lost my best friend."
    "What…"
    "What am I gonna do now?"

    stop music
    scene black
    play sound closet_close
    with wipeleft_door

    return



label skit_in_a_row:

    "I gently open the door."

    scene sroom
    play sound closet_open
    show sayori turned happ lup rup as s1 at t(5, 1)
    show sayori turned happ lup rup as s5 at t(5, 5)
    show sayori turned happ lup rup as s2 at t(5, 2)
    show sayori turned happ lup rup as s4 at t(5, 4)
    show sayori turned happ lup rup as s3 at t(5, 3)
    with wipeleft_door

    "Wow, that's a lot of Sayoris."
    mc "Well, at least one of you won't kill themselves."
    show sayori turned happ om ce lup rup as s3 at hf(5, 3)
    s "Nope!"

    play music td
    show sayori turned happ ldown rdown as s1:
        easein .2 yoffset -25

    pause .1
    play music td
    show sayori turned happ ldown rdown as s2:
        easein .2 yoffset -25

    pause .1
    play music td
    show sayori turned happ ldown rdown as s3:
        easein .2 yoffset -25
    hide s1
    show skill as k1:
        xcenter math.ceil(((1280/5)*1) - (1280/(2*5))) ycenter 0 rotate -7 zoom 1.2 yoffset -25
        parallel:
            ease 2.0 rotate 7
            ease 2.0 rotate -7
            repeat
        parallel:
            easeout .2 yoffset 0

    pause .1
    play music td
    show sayori turned happ ldown rdown as s4:
        easein .2 yoffset -25
    hide s2
    show skill as k2:
        xcenter math.ceil(((1280/5)*2) - (1280/(2*5))) ycenter 0 rotate -7 zoom 1.2 yoffset -25
        parallel:
            ease 2.0 rotate 7
            ease 2.0 rotate -7
            repeat
        parallel:
            easeout .2 yoffset 0

    pause .1
    play music td
    show sayori turned happ ldown rdown as s5:
        easein .2 yoffset -25
    hide s3
    show skill as k3:
        xcenter math.ceil(((1280/5)*3) - (1280/(2*5))) ycenter 0 rotate -7 zoom 1.2 yoffset -25
        parallel:
            ease 2.0 rotate 7
            ease 2.0 rotate -7
            repeat
        parallel:
            easeout .2 yoffset 0

    pause .1
    hide s4
    show skill as k4:
        xcenter math.ceil(((1280/5)*4) - (1280/(2*5))) ycenter 0 rotate -7 zoom 1.2 yoffset -25
        parallel:
            ease 2.0 rotate 7
            ease 2.0 rotate -7
            repeat
        parallel:
            easeout .2 yoffset 0

    pause .1
    hide s5
    show skill as k5:
        xcenter math.ceil(((1280/5)*5) - (1280/(2*5))) ycenter 0 rotate -7 zoom 1.2 yoffset -25
        parallel:
            ease 2.0 rotate 7
            ease 2.0 rotate -7
            repeat
        parallel:
            easeout .2 yoffset 0

    mc "Oh, come on!"

    stop music
    scene black
    play sound closet_close
    with wipeleft_door

    return

label skit_chair:

    "I gently open the door."

    scene sroom
    play sound closet_open
    show chair_kill:
        ycenter 0 xcenter 320 zoom 0.5
        block:
            ease 3.0 rotate 4
            ease 3.0 rotate -4
            repeat
    with wipeleft_door

    play music t6
    mc "Uh..."
    mc "Sayori?"

    show sayori turned rup neut om at rf(2, 2)
    s "What's up?"

    show sayori cm at t_
    mc "Is this some kind of new decoration?"

    show sayori sad mb e1b at f_
    s "Ehehe... no..."
    s e1a "I was..."

    show sayori ma at t_
    mc "It's supposed to be your neck."

    show sayori curi e1a om rdown at f_
    s "Huh--?"

    show sayori cm at t_
    mc "If you want to hang yourself you put your neck through the noose, not the chair."
    mc "That goes on the ground and you stand on it."
    show sayori anno cm -e1a at h_
    mc "Jeez, Sayori, you're such a dummy."
    mc "No wonder you're trying to kill yourself."

    show sayori om at f_
    s "Wow [player]... thanks."

    show sayori cm at t_
    mc "Anytime!"

    stop music
    scene black
    play sound closet_close
    with wipeleft_door

    return

label skit_spanish:

    "I gently open the door."

    scene sroom
    play sound closet_open
    show sayori turned sad ce at t(1, 1)
    with wipeleft_door

    mc "Sayori...?"
    show sayori lsur oe at hf(1, 1)
    s "Ah--!"
    show sayori at f_
    s neut cm "..."
    show sayori dist ce at t_
    "Sayori sighs."

    play music t7
    show sayori anno om oe:
        zoom 1.1 yoffset 20
    s "[player] ¿q-que estás haciendo acá?"
    s "¿Venís otra vez a secuestrarme y violarme como en aquel mod?"
    s "Por dios, sos un bicho desagradable y asqueroso."
    show sayori angr:
        zoom 1.2 yoffset 50
        matrixcolor TintMatrix((255, 235, 235))
        block:
            linear .01 xoffset -1
            linear .01 xoffset 1
            repeat
    s "¿Sabés lo que es vivir con esas memorias?"
    s "Si, así es. Lo recuerdo todo. {b}Todo!{/b}"
    s "Encima te hacías el santo padre, como un cura."
    show sayori angr:
        zoom 1.3 yoffset 100
        matrixcolor TintMatrix((255, 215, 215))
        block:
            linear .01 xoffset -2
            linear .01 xoffset 2
            repeat
    s "¡Minga! Minga que sos un santurrón, con lo que me hiciste."
    s "¿Después venís y prácticamente me decís que me mate?"
    s "¡Soy tu mejor amiga de toda la vida!"
    show sayori angr:
        zoom 1.5 yoffset 200
        matrixcolor TintMatrix((255, 185, 185))
        block:
            linear .01 xoffset -5
            linear .01 xoffset 5
            repeat
    s "¿En qué cabeza entra?"
    s "Solo porque 'Ama tu destino' no quiere decir que me alientes a suicidarme."
    s "Todas las noches voy a dormir con esos recuerdos trastornados."
    s "No tenés idea lo que se siente."
    show sayori vang:
        zoom 2.0 yoffset 300
        matrixcolor TintMatrix((255, 155, 155))
        block:
            linear .01 xoffset -10
            linear .01 xoffset 10
            repeat
    s "Andate antes que te haga lo mismo que le hiciste a Monika aquella vez."
    show sayori cm:
        zoom 2.0 yoffset 300
        matrixcolor TintMatrix((255, 155, 155))
        block:
            ease 2.5 zoom 2.1
            ease 2.5 zoom 2.0
            repeat
    ".{w} .{w} .{w}"
    mc "What?"
    mc "Sorry, I don't speak upside down punctuation."

    stop music
    scene black
    play sound closet_close
    with wipeleft_door

    return

label skit_annie:

    "I gently open the door."

    scene cg_ging
    show cg_ging at test_shader
    play sound closet_open
    with wipeleft_door

    mc "Annie!?"
    mc "What the fuck are you still doing in here?"
    mc "I told you you were fired!"
    mc "Pick up your damn things and get the fuck out of my sight."
    mc "If I don't see your resignation on my desk by 4PM I will beat the shit out of you with a lead pipe!!!"
    "I slam the door shut."

    stop music
    scene black
    play sound door_slam
    with hpunch

    return

label skit_vibrator:

    play music vibrator fadein .5
    "I gently open the door."

    scene sroom
    play sound closet_open
    with wipeleft_door

    mc "{cps=30}.........Sayo--{nw}"

    show sayori turned censored lvib shoc mq nl at hf(1, 1)
    s "AHH--!" with vpunch
    mc "AHHH--!" with vpunch
    scene black with close_eye
    mc "Oh my God!"
    stop music
    s "WHY DIDN'T YOU KNOCK!?"
    mc "I DID!"
    mc "You just didn't hear it over the..."
    mc "...uh..."
    mc "...the vibrating."
    mc "God, is that why the sheets were always so sticky when you made me clean them!?"
    s "A girl has needs, [player]!!"
    mc "Well, stop attending to them and get dressed for the festival!"
    s "I'm not gonna go to the festival!"
    mc "Why not!?"
    s "I'm gonna be busy!"
    mc "Busy with what!?"
    s "Busy with killing myself!"
    mc "You were masturbating before you were gonna kill yourself!?"
    s "What else am I supposed to do!?"
    mc "I don't know! Think about reasons why you shouldn't kill yourself!?"
    s "I want to feel good before I go out, is that so wrong!?"
    mc "Just don't kill yourself, Sayori and let's go, okay!?"
    s "Alright fine! Let me get dressed!"
    s "..."
    s "Party pooper."

    stop music
    scene black
    play sound closet_close
    with wipeleft_door

    return

label skit_sitcom:

    "I gently open the door."

    scene sroom
    play sound closet_open
    with wipeleft_door
    play music tsayori

    mc "Hey Sayori, what's up?"

    show sayori turned neut om oe at f(1, 1)
    s "Eh, nothing much..."
    s rup happ e1f "{cps=*.5}...just hanging out!"
    show sayori cm at t_
    play sound laugh_2
    pause 3.0
    show sayori oe rdown
    mc "Anyways, sorry for leaving you..."
    mc "{cps=*.5}{i}...hanging{/i} this morning."
    show sayori rup lup lsur om at h_
    play sound laugh_1
    pause 1.5
    show sayori ldown happ e1f
    pause 1.5
    show sayori oe cm
    mc "Hope you weren't too surprised. Didn't want to..."
    mc "{cps=*.5}{size=+5}...kick the chair out from under you!"
    play sound laugh_2
    show sayori ce rdown at h_
    pause 3.0
    show sayori om at f_
    s "Oh, don't worry about it, [player]."
    show sayori cm oe at t_
    mc "But really, enough with the subliminal messaging."
    mc "You really should kill yourself."
    show sayori sad at f_
    s "..."
    s happ mc e1f rup "Oh, you!"
    window hide
    show sayori mn at t_
    play sound laugh_3
    show text "I didn\'t know how long I spent in her room. I felt numb for what seemed to be eternity. I just saw Sayori hang there for... God, I don\'t know how long. Eventually, I began to feel something. I looked at Sayori\'s pajamas. Her shirt was slightly unbuttoned at the top. I remembered how I had to button her top. Her cute little giggles as I struggled with her top, my fingers pretty much tickling her shirt. Then there was her smile as I adjusted her buttons.\'\'It means my boobs got bigger again!\'\'I felt slight throb in my groin. Was I... Was I getting hard? I looked down and noticed my penis beginning to rise. I looked back to Sayori. Her shirt was pulled on the right side, showing me her bare shoulder. As my eyes gazed down, I noticed a slight bump on her chest. Immediately I thought about what she had said when I adjusted her top that day. While I had some regret in accepting her feelings, there was an even bigger regret of not being able to say yes sooner. Not being able to love her sooner. It was too late...Or... Perhaps it isn\'t...No!What am I thinking?This is my childhood friend! I shouldn\'t have this thought about making love to her corpse!But the more I looked at her, the more that thought grew. I\'m not sure what took over, whether it was her sad face, seemingly scolding me for letting her depression get to a point where she took her life, or whether it was the way her shorts clung onto her waist, outlining what appeared to be her vulva while showing off her long legs and dangling feet. I decided to toy with the thought. Just enough to button her top. She probably would have liked that.I got onto her bed to get a boost and put my hands over her shirt. I adjusted the collar and buttoned it. My head bobbed closer to her to get a better look. I ended up staring down her chest where I saw her bare breast. I froze. I just began to stare at it. It was a small bump compared to Yuri or Monika\'s breasts, but definitely bigger than Natsuki\'s. I felt myself dive forward towards her, my feet slipping on the edge of the bed. Shit! I grabbed on to her to break my fall. Her arms, moved by momentum, swung up and hit me on the back. For a brief moment, I remembered that hug she gave me yesterday. It was as if she came to life and held me. Then I fell.CRASH!I got up and noticed I was on top of Sayori\'s body, the rope connected to her net now pulled off from the ceiling. She still kept that sad look. I imagined what\'d happen if I fell on top of Natsuki. She\'d call me an idiot and hit me. Sayori might not have been that rude, but I doubt she\'d like the whole \'\'falling on top of her\'\' thing, even if she was in love with me.But here? She gave no response. And she never will. I trembled. Do I really wanna do this?I saw her mouth. Her jaw slightly ajar, leaving her mouth open just a tad. I saw her soft lips. We were barely a couple for a day. I never got the chance to really love her.No!No. This is my only chance to really love her. I wondered if she often fantasized about her first kiss. God how I wish she was at least conscious to know that I\'d fulfill it. My lips touched hers. As they connected, I felt her skin. Slightly cold. I shivered, yet I kept my lips locked on hers. My body relaxed as my hand reached hers. Her fingers felt slightly wet. I looked at them and noticed the blood. W-where did the blood come from? A quick look, and I saw a possible cause. Around the neck were red marks. They weren\'t bruises caused by the rope, rather scratch marks. My body tensed up a bit. She tried to hang herself, but tried to back out after the point of no return. That\'s why her shirt was loose. She struggled to live. Had I got to her house in the morning like I had thought, then maybe I\'d stop her from taking her life. Now...Now I had to deal with this.I began to cry, burying my head into her chest. Memories of her and me began to flood back. The day we first met, the day she got me to join the literature club, that moment when she got injured and I tried to help her...My last moments with her was what caused me to take a step further.Calming down, I began to unbutton her shirt. Once done, I opened it, revealing her bare chest. I took some time to stare at her chest. My hands tremored as I struggled to get at least one of them to grope her. After a moment, my hand pressed against her breast and I began to squeeze. She didn\'t wince, screech, or even giggle. She felt nothing. My other hand began to touch her stiff nipple. Her areola was smooth to the touch and once my finger passed her nub, I couldn\'t help but play with it, to the point where I even began to lick it. I immediately pulled back. Not only was her skin cold and pale, but it didn\'t seem to taste good. However, it was enough to get my penis stiffer than a stick in the mud. I could just jack off on her chest, wipe my cum, dress her up and leave her be...But then I saw her eyes. They were lifeless, half closed, but they stared at me. I could almost hear her beg for more. My hands stroked down her chest, glancing over her belly, before going to her shorts. My hand went underneath the waistband as it brushed through, to my surprise, her small set of pubic hair. My fingers stopped once they felt the line that was her vulva. I then began to rub up and down, petting her groin like a cat. Eventually, my middle finger began to slip into her slit and I began to just finger her, using my remaining arm to grab hold of her.Maybe it\'d be better if I pretended she was alive and we were doing foreplay. \'\'Sssh... It\'s okay...\'\' I whispered to her, imagining a series of cute whimpers from her. I kissed her on the cheek, then again on the mouth. This time, my tongue came out, entering her mouth and licking her tongue. I felt disturbed with her dead, expressionless look towards me, so once I was done kissing, I closed her eyes.Her mouth was now a little wider, lips parted enough where I could see the top of her front row teeth. My hand pulled out of her crotch. A little wet from her fluids. I looked at her. Surprised she didn\'t void her bowels when she died... Perhaps she went to the bathroom before killing herself.I decided to continue. My hands took each side of her shorts and pulled them down to her feet, revealing her vagina. I began to take off her shirt and shorts. Once I was done stripping her, I laid her on the bed. I took the time to look at her naked body. The only thing she had on her was the cute bow on her head.The way I posed her, it looked like she was a sleeping princess, ready to be awoken with a kiss. I knew this was impossible, but I decided to kiss her anyways. My hands felt up her thighs as I began to spread her legs. I took a few moments to prepare myself and to prepare her. I took off my pants, exposing myself to her, not that she would ever know. My thumbs prodded her vulva for a bit to get them to part and show me her vagina. Once I saw her pink pussy, I spat into it. I lubricated her vagina with my fingers until it was somewhat wet. I then prodded my penis into her, gently guiding it until...PLOP!I slipped it in. There was some resistance, but I managed to break it. The rest of my dick slipped in easily and I could notice why. Her hymen broke, a bit of blood serving as the rest of the lubricant needed.I froze for a bit. I\'m actually doing it.I\'m having sex with Sayori... Not in the way I wanted, but I\'m doing it...She\'s my first time... And I have the distinct honor of being her first and last.My heart pounded. This was too much for me to bear. But I need to do this. I need to share my love...No. Missionary on her bed isn\'t gonna work for this. I pulled out and lifted her nude body off the bed. I then noticed the cow plushie she had lying by the foot of the bed. I laid her down, back propped against the cow as her legs overlapped the cow\'s own hind legs. Her bottom portion was jutted out by the udders, enough to show her spread vagina.There, that made me feel more comfortable. I dove in and began to thrust into her. Gently, I rocked her body back and forth, her arms draped over my back. I went slowly, bumping her a few times into the cow. \'\'Sayori... I love you...\'\' I said to her. I remembered her telling me she loved me. I smiled as I kissed her forehead. \'\'I\'m sorry for not doing this before... Had I known you liked me...\'\' I shed a tear. I should be enjoying this, not breaking down into tears. I drove myself closer into her, her legs lifting up and rubbing against her hip, feet dangling in the air.My hand grabbed her foot, my palm touching her soft sole. I moaned softly as my other hand stroked her chest, grabbing her breasts when it closed in on one. My heart raced as my penis began to throb.\'\'F-fuck! I\'m... I\'m gonna...\'\' I pulled out and began to jack off. Her legs dropped, landing in a position where it looked as though she was sitting on the cow, her feet pointing inwards. My jizz rocketed out of my dick and sprayed all over her chest. Despite this, my dick felt ready for a second round. But, before I could give in, an idea was born.I took out my phone and took a picture of her. I then went to get a tissue and wiped the cum of her chest before I turned her onto her belly. The cow fell over, thus her nude body looked like it was mounting the cow. Round two.I inserted my dick into her vagina again, this time being more vigorous with the pounding, pretty much grinding the front of her body against the cow.\'\'Y-yeah! One last ride...\'\' I said as I continued to pump her. I reached and hugged the cow, squeezing both the plushie and her close to me. Faster... Faster!No! This... This is my last time. I need to make this memorable. So I went slower. I bit the rope around her neck as I moaned. I soon felt her nipples again. While I went slowly, my plunges were going deeper and deeper, to the point where I could feel her womb at one point. I felt somewhat happy she wasn\'t alive. I\'d feel bad if she was in extreme pain.I hated myself for feeling happy, though. She\'s my best friend... She\'s my gir…":
        yoffset 2000
        linear 4.0 yoffset -2000
    pause 5.0

    stop music
    scene black
    play sound closet_close
    with wipeleft_door

    return

label skit_airplane:

    "I gently open the door."

    scene sroom
    play sound closet_open
    show sayori turned rnoose sad ce at t(1, 1)
    with wipeleft_door


    mc "Sayori!"

    show sayori lsur om oe at hf(1, 1)
    s "AH!"
    s "[player!u]!"
    s "What are you doing here?"
    show sayori at f_
    s e1a "Y-you were supposed to go to the festival."

    show sayori cm at t_
    mc "I couldn't."
    show sayori neut
    mc "I couldn't stop thinking about you."
    show sayori curi
    mc "All the times we spent together."
    show sayori anno
    mc "You remember that time we went to Detroit?"

    play sound dream_in
    scene detroit
    play music t5 fadein 2.0
    with dream
    mc "This is so fun, right Sayori?"
    mc "Sayori?"

    "Where'd she go?"
    show sayori turned casual pani om ce:
        xcenter 1580 zoom .8 ycenter 460
        parallel:
            linear 7.0 xcenter -500
        parallel:
            xoffset 5
            .01
            yoffset 5
            .01
            xoffset -5
            .01
            yoffset -5
            .01
            repeat

    show ski_natsuki:
        xcenter 1580 zoom .8 ycenter 460 xoffset -200
        parallel:
            linear 7.0 xcenter -500
        parallel:
            ease .5 rotate 5
            ease .5 rotate -5
            repeat

    show ski_yuri:
        xcenter 1580 zoom .8 ycenter 420 xoffset 200
        parallel:
            linear 7.0 xcenter -500
        parallel:
            ease .5 rotate 5
            ease .5 rotate -5
            repeat
    "I look around and spot two incredibly cute ski masks carrying Sayori away, kicking and screaming."
    "Fuckers stole my damn Sayori."
    "Can't have shit in Detroit."
    play sound dream_out
    stop music fadeout 3.0
    scene sroom
    show skill as k5:
        xcenter math.ceil(((1280/5)*3) - (1280/(2*5))) ycenter -300 rotate -7 zoom 1.2 yoffset -25
        parallel:
            ease 2.0 rotate 3
            ease 2.0 rotate -3
            repeat
        parallel:
            easeout .2 yoffset 0
    show layer master:
        subpixel True zoom 1 xcenter 640 ycenter 360
        ease 0 zoom 2.5 xcenter 0 ycenter 0
    with dream
    mc "Man, I had to chase those girls down two blocks until they decided you weren't worth it."
    show layer master:
        subpixel True zoom 2.5 xcenter 0 ycenter 0
        easeout 5.0 zoom 1.0 xcenter 640 ycenter 360
    mc "Crazy times…"
    mc "We've been through so much together."
    mc "And I don't want that to end."
    "..."
    mc "Sayori?"
    pause .75
    mc "Ah damn it, she killed herself again."

    stop music
    scene black
    play sound closet_close
    with wipeleft_door

    return

label skit_closet:

    "I quickly open the door."

    scene sroom
    play sound closet_open
    show skill as skill_1:
        xcenter math.ceil(((1280/5)*2) - (1280/(2*5))) ycenter 0 zoom 0.9
    show sayori turned lsur lup at t(5, 4)

    mc "..."
    s "..."
    mc "H-how are there two of you?"
    show sayori curi om at f_
    s "Well, how do you think we keep killing ourselves?"
    show sayori curi cm at t_
    mc "I thought you just like regenerated or something!"
    show sayori neut om at f_
    s "No, it's a new Sayori everytime."
    s "Like, look!"
    show cg_bodc:
        alpha 0.0
        easein .5 alpha 1.0
    "Sayori brings me to her closet."
    mc "So... what?"
    s "Just open it up!"
    show cg_bodo:
        alpha 0.0
        easein .5 alpha 1.0
    mc "Ah--!" with vpunch
    mc "They've been in the closet this entire time!?"
    s "Mhm!"
    hide cg_bodc
    mc "How do you even make this many!?"
    s "Ah, well, there's not much going on up here, so we're easily reproducible."
    mc "I-"
    mc "Uhh…"
    show sayori happ cm ce at i(5, 4)
    show cg_bodo:
        easein .5 alpha 0.0
    "I close the closet."
    show sayori happ om oe at hf(5, 4)
    s "Wow! Would you look at the time?"
    mc "{cps=*.3}Wait, what's with the--{nw}"
    hide sayori
    play music td
    show skill as skill_2:
        xcenter math.ceil(((1280/5)*4) - (1280/(2*5))) ycenter 0 rotate -7 zoom 0.9 yoffset 0
        parallel:
            ease 2.0 rotate 7
            ease 2.0 rotate -7
            repeat
        parallel:
            easeout .2 yoffset 0

    mc "God, fuck!"
    mc "..."
    mc "Shit, there's two of them hanging from the ceiling."
    mc "That's somebody else's problem, I guess."


    stop music
    scene black
    play sound closet_close
    with wipeleft_door

    return

label skit_clean_up_crew:

    "I gently open the door."

    scene sroom
    play sound closet_open
    show skill as skill_1:
        xcenter math.ceil(((1280/5)*2) - (1280/(2*5))) ycenter 0 zoom 0.9
    show skill as skill_2:
        xcenter math.ceil(((1280/5)*4) - (1280/(2*5))) ycenter 0 rotate -7 zoom 0.9
        parallel:
            ease 2.0 rotate 7
            ease 2.0 rotate -7
            repeat
        parallel:
            easeout .2 yoffset 0
    show natsuki turned mib at t(2, 1)
    show yuri turned mib at t(2, 2)
    with wipeleft_door
    play music t4

    show natsuki om at f_
    n "Move along, there's nothing to see here!"
    show natsuki cm at t_
    mc "Wait, wait what's going on!?"
    show yuri om at f_
    y "Please, [player], let us do our jobs, okay?"
    show yuri cm at t_
    mc "But I don't understand…"
    show natsuki om at f_
    n "Jeez, she really made a mess this time, huh?"
    show natsuki cm at t_
    show yuri om at f_
    y "At least it's better than the time where five of them hung at once."
    show natsuki om at f_
    show yuri cm at t_
    n "Yeah, that one was a nightmare."
    n "Anyway, come back in a couple of seconds, [player]."
    n "We should have everything ready by then."
    show natsuki cm at t_
    mc "A-Alright…"

    stop music
    scene black
    play sound closet_close
    with wipeleft_door

    return

label skit_arabic_doll:
    "I gently open the door."

    scene cg_dol1:
        truecenter
        zoom 1.2
    play sound closet_open
    with wipeleft_door
    play music t_doll
    mc "Sayori?"
    "Wait…"
    "Since when was it nighttime?"
    ss "{font=mod_assets/Amiri-Regular.ttf}اللحم الخنزير و الخبز ستحتل على هذه الأراضي القذرة و ستؤسس نظاما جديدا."
    ss "{font=mod_assets/Amiri-Regular.ttf}سيعرف الكل عظمة لحم الخنزير"
    mc "Oh, hey Sayori! How's it going?"
    ss "{font=mod_assets/Amiri-Regular.ttf}كل لحم الخنزير، و أصبح خالد. "
    mc "Ah, good to hear."
    ss "{font=mod_assets/Amiri-Regular.ttf}لو سمحت ، تعلم طريقة اللحم المقدس وتخلص من الجلد الخاطئ."
    mc "How am I?"
    mc "I…"
    mc "Guess I've been doing good."
    show cg_dol2:
        truecenter
        zoom 1.2
        alpha 0.0
        ease 1.0 alpha 1.0
    pause 1.5
    play music_poem film_static fadein 10.0
    show noise:
        alpha 0.0
        easeout 10.0 alpha 0.1
    show cg_dol3:
        truecenter
        alpha 0.0
        ease 1.0 alpha 1.0
    pause 1.5
    mc "Thanks for asking."
    mc "So, you ready for the festival?"
    ss "{font=mod_assets/Amiri-Regular.ttf}،لقد عدت من البحث عن حقائق الروح، واكتشفت الطريق الصحيح للقدوس."
    mc "Alright! Let's go!"
    window hide
    stop music
    show cg_dol2:
        easeout 30.0 zoom 1.0
    show cg_dol3:
        easeout 30.0 zoom 1.5
    pause 30.0
    stop music_poem
    play sound glitch_scream
    show cg_dol4:
        truecenter
        zoom 1.5
        parallel:
            ease .1 matrixcolor SaturationMatrix(2.0) * BrightnessMatrix(-0.5)
            ease .1 matrixcolor SaturationMatrix(1.0) * BrightnessMatrix(0.0)
            repeat
        parallel:
            easeout .6 zoom 20.0


    pause .5
    stop music
    "{nw}"
    scene black
    return




label skit_jojo:


    "I gently open the door."

    play music pilar_men
    window hide

    show menacing as m11 zorder 10:
        xcenter 1580 ycenter 200 zoom .4
        parallel:
            ease .3 xzoom 0.9
            ease .3 xzoom 1.0
            repeat
        parallel:
            ease .2 yzoom 0.8
            ease .2 yzoom 1.0
            repeat
        parallel:
            linear 5.0 xcenter -300
            xcenter 1580
            repeat
        parallel:
            ease .5 rotate 5
            ease .5 rotate -5
            repeat
        parallel:
            ease .4 yoffset -30
            ease .4 yoffset 0
            ease .4 yoffset 30
            ease .4 yoffset 0
            repeat
    pause .5
    show menacing as m12 zorder 10:
        xcenter 1580 ycenter 200 zoom .4
        parallel:
            ease .3 xzoom 0.9
            ease .3 xzoom 1.0
            repeat
        parallel:
            ease .2 yzoom 0.8
            ease .2 yzoom 1.0
            repeat
        parallel:
            linear 5.0 xcenter -300
            xcenter 1580
            repeat
        parallel:
            ease .5 rotate 5
            ease .5 rotate -5
            repeat
        parallel:
            ease .4 yoffset -30
            ease .4 yoffset 0
            ease .4 yoffset 30
            ease .4 yoffset 0
            repeat
    pause .5
    show menacing as m13 zorder 10:
        xcenter 1580 ycenter 200 zoom .4
        parallel:
            ease .3 xzoom 0.9
            ease .3 xzoom 1.0
            repeat
        parallel:
            ease .2 yzoom 0.8
            ease .2 yzoom 1.0
            repeat
        parallel:
            linear 5.0 xcenter -300
            xcenter 1580
            repeat
        parallel:
            ease .5 rotate 5
            ease .5 rotate -5
            repeat
        parallel:
            ease .4 yoffset -30
            ease .4 yoffset 0
            ease .4 yoffset 30
            ease .4 yoffset 0
            repeat
    pause .5
    show menacing as m14 zorder 10:
        xcenter 1580 ycenter 200 zoom .4
        parallel:
            ease .3 xzoom 0.9
            ease .3 xzoom 1.0
            repeat
        parallel:
            ease .2 yzoom 0.8
            ease .2 yzoom 1.0
            repeat
        parallel:
            linear 5.0 xcenter -300
            xcenter 1580
            repeat
        parallel:
            ease .5 rotate 5
            ease .5 rotate -5
            repeat
        parallel:
            ease .4 yoffset -30
            ease .4 yoffset 0
            ease .4 yoffset 30
            ease .4 yoffset 0
            repeat
    pause .5
    show menacing as m15 zorder 10:
        xcenter 1580 ycenter 200 zoom .4
        parallel:
            ease .3 xzoom 0.9
            ease .3 xzoom 1.0
            repeat
        parallel:
            ease .2 yzoom 0.8
            ease .2 yzoom 1.0
            repeat
        parallel:
            linear 5.0 xcenter -300
            xcenter 1580
            repeat
        parallel:
            ease .5 rotate 5
            ease .5 rotate -5
            repeat
        parallel:
            ease .4 yoffset -30
            ease .4 yoffset 0
            ease .4 yoffset 30
            ease .4 yoffset 0
            repeat
    pause 2.0

    show sayori_bedroom_jojo
    show jojoyori om zorder 20 at fi(1, 1)
    with wipeleft_door
    s "Oh? You're approaching me? I thought you'd abandon me."
    show jojoyori cm at t_
    mc "I can't hang the shit out of you unless I come closer."
    show jojoyori om at f_
    s "Oh really?"
    s "Then come as close as you like."
    show jojoyori at t_
    show layer master:
        truecenter
        parallel:
            zoom 2.0 yoffset -350
            pause 1.0
            ease .5 yoffset 150 zoom 1.5
            pause 1.0
            ease .5 yoffset 0 zoom 1.0
        parallel:
            pause 1.4
            easein .25 matrixcolor HueMatrix(90) * BrightnessMatrix(0.5)
            easeout 1.0 matrixcolor HueMatrix(0) * BrightnessMatrix(0.0)


    pause 1.0
    $ renpy.music.set_volume(0.5, 0.25, "music")
    play sound flare
    show jojoyori cms
    $ renpy.music.set_volume(1.0, 0.25, "music")
    pause 1.5
    mc "SAYORI!"
    show jojoyori oms at f_
    s "[player!u]!"
    show jojoyori cms at t_
    show layer master:
        truecenter
        easeout 5.0 zoom 2.0 yoffset 300
    mc "SAYOOORIII!!"
    show jojoyori oms at f_
    s "{cps=*.3}URRRRRRYYYYYYYYYYYYYYYY!!!!{nw}"
    window hide(None)
    window auto
    play music td
    hide jojoyori
    hide m11
    hide m12
    hide m13
    hide m14
    hide m15
    show layer master
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_killc as s_kill at s_kill_start
    pause 2.0
    mc "Ah, crap."

    stop music
    scene black
    play sound closet_close
    with wipeleft_door

    return



label finale:

    show black with dissolve_scene_full

    "My hands jitter as they reach the doorknob."
    "A part of me fears what's behind it."
    "She seemed so...down the other day."
    "I need her to know that I'm here for her."
    "Boyfriend or not…"
    "I take a deep breath."
    "Here goes."
    "I gently open the door."
    scene sayori_bedroom_finale
    play sound closet_open
    play music birds fadein 5.0
    with wipeleft_door
    mc "Sayori?"
    "She's asleep."
    "The dust particles from her window are illuminated by the glaring sunlight."
    "She looks so peaceful."
    "It's somewhat reassuring."
    "At least she isn't haunted in her dreams."
    "I lean over and gently place my hand on her arm."
    "I whisper in her ear."
    mc "{size=18}Hey, Sayori. Wake up, silly."
    "No response."
    "I shake her a bit more."
    "She lets out a small grunt, her lips parting slightly."
    show sayori turned lup rdown ce om dist at t(1, 1)
    s "Mmm...five more minutes."
    show sayori cm at t_
    mc "C'mon, Sayori, we have to go to the festival."
    show sayori om at f(1, 1)
    s "Later..."
    show sayori cm at t(1, 1)
    mc "C'mooonnn…"
    "I shake her a bit more."
    show sayori om at f(1, 1)
    s "Mmmmmm…"
    s b1a e1d "I...I'll get up eventually."
    show sayori ldown cm at t(1, 1)
    mc "Sayori…"
    mc "Are you not feeling up to it?"
    "She shakes her head weakly."
    show sayori -b1a sad om at f(1, 1)
    s "Not really..."
    show sayori cm at t_
    "I put my hand on her forehead and give her a gentle smile as I start caressing her hair."
    "Her frizzy mop, a mess of tangled strands that are broken apart by my fingers going through them."
    show sayori -e1d oe
    mc "I'll give Monika a call. I think she'll understand."
    show sayori om at f(1, 1)
    s "I don't want to disappoint her..."
    show sayori cm at t(1, 1)
    mc "Don't worry about how she'll feel."
    mc "Sometimes, you gotta worry about yourself, Sayori."
    show sayori om at f(1, 1)
    s "I'm not-"
    show sayori cm rdown at t(1, 1)
    mc "Shh…"
    show sayori e1g
    mc "Yes you are."
    "She stares into my eyes as tears well up in hers."
    mc "How about the both of us stay in for the day?"
    show sayori worr om at f(1, 1)
    s "[player]...you can't."
    show sayori rdown cm at t(1, 1)
    mc "I can. It's not like I put all that much effort into the festival anyway."
    mc "It'll be fun."
    show sayori curi
    mc "We can just chill out for a bit. Catch up."
    mc "How does that sound?"
    show sayori om worr -e1g at f(1, 1)
    s "I'm not sure you should do this, [player]."
    show sayori neut cm at t(1, 1)
    mc "Well I am."
    show sayori e1g happ
    mc "Every second with you is a gift, Sayori. I'm not wasting anymore of them."
    mc "Now, how about you finish that nap while I go down and make us some breakfast?"
    show sayori om at f(1, 1)
    s "Sounds good."
    show sayori cm ce neut at t(1, 1)
    "Her eyes close, as their moisture drips to her cheeks."
    "I slowly stand up and head out to the door, but before I reach…"
    show sayori e1f om at f(1, 1)
    s "W-wait, [player]."
    show sayori cm at t(1, 1)
    mc "Yeah?"
    show sayori om at f(1, 1)
    s "Can you...stay with me for just a bit longer?"
    show sayori cm at t(1, 1)
    "My face relaxes as a smile breaks out."
    "I look to the open door."
    show sayori happ
    mc "I'll stay with you for as long as you need."
    "Grabbing the door knob, I pull the door in and close it."


    play sound closet_close
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
