init python:
    renpy.music.register_channel("ambient", "sfx", True)
    renpy.music.register_channel("ambient2", "sfx", True)
    renpy.music.register_channel("track1", "music", True)
    renpy.music.register_channel("track2", "music", True)
default persistent.finished = False 
define audio.sting = "mod_assets/sting.ogg"
define audio.baby = "mod_assets/baby.mp3"
define audio.sizzle = "mod_assets/sizzle.ogg"
define audio.birds = "mod_assets/birds.ogg"
define audio.phones = "mod_assets/phones.mp3"
define audio.knock = "mod_assets/knock.ogg"
define close_eye = ImageDissolve("mod_assets/close_eye.png", 0.15, ramplen=64)

image sayata1 = "mod_assets/sayori/sayata.png"
image sayata2 = "mod_assets/sayori/sayata2.png"
image blackzoom:
    "black"
    zoom 20 
image nbaby = "mod_assets/nbaby.png"
image yt = "mod_assets/yt.png"
image preg = "mod_assets/preg.png" 
image aspect = "mod_assets/fitsfetish.png"
image vhs:
    alpha .35
    "mod_assets/vhs/1.png"
    .0366666
    "mod_assets/vhs/2.png"
    .0366666
    "mod_assets/vhs/3.png"
    .0366666
    "mod_assets/vhs/4.png"
    .0366666
    "mod_assets/vhs/5.png"
    .0366666
    repeat 
image sans = "mod_assets/sans.png"
image note:
    "mod_assets/note.png"
    zoom .2
image logoback = "mod_assets/logoback.png"
image logotext = "mod_assets/logotext.png"
image bump = "mod_assets/bump.png"
image baguette = "mod_assets/baguette.png"
image sroomz:
    "bg/sayori_bedroom.png"
    truecenter
    zoom 1.8 
    xoffset 500  
image sroom = "bg/sayori_bedroom.png"
image sroomf = "mod_assets/sroomf.png"
image sroom base = "bg/sayori_bedroom.png"
image bg sroomw = "mod_assets/sroomw.jpg"
image noose = "mod_assets/noose.png"
image pink = "#b59"
image lionking = "mod_assets/lk.png"
image sdrip = "mod_assets/sayori/sdrip.png"
image sroomn = "mod_assets/sroomn.png"
image mooncrawl = "mod_assets/mooncrawl.png"
image moon = "mod_assets/moon.png"
image windowcut = "mod_assets/windowcut.png"
image closetc = "mod_assets/bodies_closed.png"
image closeto = "mod_assets/monika_bodies.png"

#layeredimage ava:
#    always "ava_ngelion"#

#    group e:
#        attribute fucke default null# = "n_rects_ghost1"
#        attribute ey:
#            "n_rects_ghost1"
#    group ee:
#        attribute fuckee default null# = "n_rects_ghost1"
##        attribute eyy:
#            "n_rects_ghost2"
#    group eee:
#        attribute fuckeee default null# = "n_rects_ghost1"
##        attribute eyyy:
#           "n_rects_ghost3"
transform shake:
    dizzy(1.5, 0.01) 

transform anxiety:
    truecenter
    subpixel True
    zoom 1.2
    parallel:
        block:
            rotate 0
            ease 5 rotate 3
            time 1
            ease 5 rotate -3    
            ease 5 rotate 0
            repeat
    parallel:
        block:
            dizzy(.8, 2.0)










# Sayori's Definitions

image sayori 1a = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/ab.png")
image sayori 1b = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/bb.png")
image sayori 1c = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/cb.png")
image sayori 1d = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/db.png")
image sayori 1e = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/eb.png")
image sayori 1f = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/fb.png")
image sayori 1g = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/gb.png")
image sayori 1h = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/hb.png")
image sayori 1i = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/ib.png")
image sayori 1j = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/jb.png")
image sayori 1k = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/kb.png")
image sayori 1l = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/lb.png")
image sayori 1m = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/mb.png")
image sayori 1n = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/nb.png")
image sayori 1o = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/ob.png")
image sayori 1p = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/pb.png")
image sayori 1q = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/qb.png")
image sayori 1r = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/rb.png")
image sayori 1s = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/sb.png")
image sayori 1t = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/tb.png")
image sayori 1u = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/ub.png")
image sayori 1v = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/vb.png")
image sayori 1w = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/wb.png")
image sayori 1x = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/xb.png")
image sayori 1y = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/1rb.png", (0, 0), "mod_assets/sayori/yb.png")

image sayori 2 = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/ab.png")
image sayori 2a = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/ab.png")
image sayori 2b = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/bb.png")
image sayori 2c = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/cb.png")
image sayori 2d = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/db.png")
image sayori 2e = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/eb.png")
image sayori 2f = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/fb.png")
image sayori 2g = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/gb.png")
image sayori 2h = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/hb.png")
image sayori 2i = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/ib.png")
image sayori 2j = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/jb.png")
image sayori 2k = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/kb.png")
image sayori 2l = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/lb.png")
image sayori 2m = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/mb.png")
image sayori 2n = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/nb.png")
image sayori 2o = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/ob.png")
image sayori 2p = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/pb.png")
image sayori 2q = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/qb.png")
image sayori 2r = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/rb.png")
image sayori 2s = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/sb.png")
image sayori 2t = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/tb.png")
image sayori 2u = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/ub.png")
image sayori 2v = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/vb.png")
image sayori 2w = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/wb.png")
image sayori 2x = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/xb.png")
image sayori 2y = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1lb.png", (0, 0), "mod_assets/sayori/2rb.png", (0, 0), "mod_assets/sayori/yb.png")




# Definitions.rpy

# This section defines stuff for DDLC and your mod!
# Use this as a starting point if you would like to override with your own.

## Note: For Android, make sure to change the default package name of to 
## your own package name in options.rpy under define package_name. 
##Your package name is what you defined in Ren'Py Launcher in the Android section

define persistent.demo = False
define persistent.steam = ("steamapps" in config.basedir.lower())
# Change this to True to enable Developer Mode
define config.developer = True

python early:
    import singleton
    me = singleton.SingleInstance()

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    
    # Get's position of Music
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0

    # Delete's All Saves
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)

    # Delete's Characters
    def delete_character(name):
        import os
        if renpy.android:
            try: os.remove(os.path.realpath("/sdcard/Android/data/"+package_name+"/characters/") + name + ".chr")
            except: pass
        else:
            try: os.remove(config.basedir + "/characters/" + name + ".chr")
            except: pass

    # Restores Character's CHR
    def restore_all_characters():
        if renpy.android:
            try: file(os.path.realpath("/sdcard/Android/data/"+package_name+"/characters/monika.chr"))
            except: open(os.path.realpath("/sdcard/Android/data/"+package_name+"/characters/monika.chr"), "wb").write(renpy.file("monika.chr").read())
            try: file(os.path.realpath("/sdcard/Android/data/"+package_name+"/characters/natsuki.chr"))
            except: open(os.path.realpath("/sdcard/Android/data/"+package_name+"/characters/natsuki.chr"), "wb").write(renpy.file("natsuki.chr").read())
            try: file(os.path.realpath("/sdcard/Android/data/"+package_name+"/characters/yuri.chr"))
            except: open(os.path.realpath("/sdcard/Android/data/"+package_name+"/characters/yuri.chr"), "wb").write(renpy.file("yuri.chr").read())
            try: file(os.path.realpath("/sdcard/Android/data/"+package_name+"/characters/sayori.chr"))
            except: open(os.path.realpath("/sdcard/Android/data/"+package_name+"/characters/sayori.chr"), "wb").write(renpy.file("sayori.chr").read())
        else:
            try: renpy.file("../characters/monika.chr")
            except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
            try: renpy.file("../characters/natsuki.chr")
            except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
            try: renpy.file("../characters/yuri.chr")
            except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
            try: renpy.file("../characters/sayori.chr")
            except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())
    
    # Restores Characters if their playthough matches current run.
    def restore_relevant_characters():
        restore_all_characters()
        if persistent.playthrough == 1 or persistent.playthrough == 2:
            delete_character("sayori")
        elif persistent.playthrough == 3:
            delete_character("sayori")
            delete_character("natsuki")
            delete_character("yuri")
        elif persistent.playthrough == 4:
            delete_character("monika")

    # Controls time.
    def pause(time=None):
        #global _windows_hidden
        if not time:
            #_windows_hidden = True
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            #_windows_hidden = False
            return
        if time <= 0: return
        #_windows_hidden = True
        renpy.pause(time)
        #_windows_hidden = False

# Music

# This section is where you can reference DDLC audio and add your own!
# audio. - tells Ren'Py this is sound
# t1 - tells Ren'Py the label of the music/sound file
# <loop 22.073> - tells Ren'Py to loop the song at that time interval
# "bgm/1.ogg" - location of your music
define audio.t1 = "mod_assets/sweden_acoustic.ogg" # Doki Doki Literature Club! - Main Theme
define audio.t2 = "<loop 4.499>bgm/2.ogg" # Ohayou Sayori! - Sayori Theme
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg" # Main Theme - In Game 
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg" # Dreams of Love and Literature - Poem Game Theme
define audio.t4g = "<loop 1.000>bgm/4g.ogg"
define audio.t5 = "<loop 4.444>bgm/5.ogg" # Okay Everyone! - Sharing Poems Theme

# Doki Poem Theme
define audio.tmonika = "<loop 4.444>bgm/5_monika.ogg" # Okay Everyone! (Monika)
define audio.tsayori = "<loop 4.444>bgm/5_sayori.ogg" # Okay Everyone! (Sayori)
define audio.tnatsuki = "<loop 4.444>bgm/5_natsuki.ogg" # Okay Everyone! (Natsuki)
define audio.tyuri = "<loop 4.444>bgm/5_yuri.ogg" # Okay Everyone! (Yuri)

define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg" # Play With Me - Yuri/Natsuki Theme
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg" # Poem Panic - Argument Theme
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg" # Daijoubu! - Argument Resolved Theme
define audio.t9 = "<loop 3.172>bgm/9.ogg" # My Feelings - Emotional Theme
define audio.t9g = "<loop 1.532>bgm/9g.ogg" # My Feelings but 207% Speed
define audio.t10 = "<loop 5.861>bgm/10.ogg" # My Confession - Sayori Confession Theme
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"
define audio.shot = "mod_assets/shot.ogg"
define audio.m1 = "<loop 0>bgm/m1.ogg" # Just Monika. - Just Monika.
define audio.mend = "<loop 6.424>bgm/monika-end.ogg" # I Still Love You - Monika Post-Delete Theme

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.opend = "sfx/closet-open.ogg"
define audio.closed = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"

# Backgrounds
# To define a new color background do like so
# image blue = "#XXXXXX" where X is your hex digits (#158353)
# To define a new background, do so like this
# image bg bathroom = "mod_assets/bathroom.png" (make sure you use the right file type [.png, .jpg])
image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"
image bg residential_day = "bg/residential.png" # Start of DDLC BG
image bg class_day = "bg/class.png" # The classroom BG
image bg corridor = "bg/corridor.png" # The hallway BG
image bg club_day = "bg/club.png" # The club BG
image bg club_day2: # Glitched Club BG
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"
image bg closet = "bg/closet.png" # The closet BG
image bg bedroom = "bg/bedroom.png" # MC's Room BG
image bg sroom = "bg/sayori_bedroom.png" # Sayori's Room BG
image bg house = "bg/house.png" # Sayori's House BG
image bg kitchen = "bg/kitchen.png" # MC's Kitchen BG

image bg notebook = "bg/notebook.png" # Poem Game Notebook Scene
image bg notebook-glitch = "bg/notebook-glitch.png" # Glitched Poem Game BG

image bg glitch = LiveTile("bg/glitch.jpg")

image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0



image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0


image natsuki mouth = LiveComposite((960, 960), (0, 0), "natsuki/0.png", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

image n_moving_mouth:
    "images/natsuki/mouth.png"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

image natsuki_ghost_blood:
    "#00000000"
    "natsuki/ghost_blood.png" with ImageDissolve("images/menu/wipedown.png", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    "natsuki/ghost1.png"
image natsuki ghost1:
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Image("natsuki/ghost2.png")
image natsuki ghost3 = Image("natsuki/ghost3.png")
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"
image natsuki glitch1:
    "natsuki/glitch1.png"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/scream.png")
image natsuki vomit = "natsuki/vomit.png"

image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"

# Yuri's Definitions
# Sprites with 1y1 are Yuri's Yandere Sprites


image y_glitch_head:
    "images/yuri/za.png"
    0.15
    "images/yuri/zb.png"
    0.15
    "images/yuri/zc.png"
    0.15
    "images/yuri/zd.png"
    0.15
    repeat

image yuri stab_1 = "yuri/stab/1.png"
image yuri stab_2 = "yuri/stab/2.png"
image yuri stab_3 = "yuri/stab/3.png"
image yuri stab_4 = "yuri/stab/4.png"
image yuri stab_5 = "yuri/stab/5.png"
image yuri stab_6 = LiveComposite((960,960), (0, 0), "yuri/stab/6-mask.png", (0, 0), "yuri stab_6_eyes", (0, 0), "yuri/stab/6.png")

image yuri stab_6_eyes:
    "yuri/stab/6-eyes.png"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.2
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.2
        repeat
    parallel:
        2.05
        easeout 1.0 yoffset -15
        linear 10 yoffset -15


image yuri oneeye = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/oneeye.png", (0, 0), "yuri oneeye2")
image yuri oneeye2:
    "yuri/oneeye2.png"
    subpixel True
    pause 5.0
    linear 60 xoffset -50 yoffset 20

image yuri glitch:
    "yuri/glitch1.png"
    pause 0.1
    "yuri/glitch2.png"
    pause 0.1
    "yuri/glitch3.png"
    pause 0.1
    "yuri/glitch4.png"
    pause 0.1
    "yuri/glitch5.png"
    pause 0.1
    repeat
image yuri glitch2:
    "yuri/0a.png"
    pause 0.1
    "yuri/0b.png"
    pause 0.5
    "yuri/0a.png"
    pause 0.3
    "yuri/0b.png"
    pause 0.3
    "yuri 1"

image yuri eyes = LiveComposite((1280, 720), (0, 0), "yuri/eyes1.png", (0, 0), "yuripupils")

image yuri eyes_base = "yuri/eyes1.png"

image yuripupils:
    "yuri/eyes2.png"
    yuripupils_move

image yuri cuts = "yuri/cuts.png"

image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"



image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat

# Character Variables

# This configure the character variables for writing dialog for each character
## To define a new character with assets, do so like this
# define e = DynamicCharacter('e_name', image='eileen', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
## To define a new character without assets, do so like this
# define en = Character('Eileen & Nat', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define a = DynamicCharacter('a_name', image ='ava', what_prefix='"{font=mod_assets/wingding.ttf}', what_suffix='{/font}"', ctc="ctc", ctc_position="fixed")
image ava ngelion = "mod_assets/ava.png"
define _dismiss_pause = config.developer
default a_name = "{font=mod_assets/wingding.ttf}Ava"

# Persistent Variables

# These variables are load at game startup and exist on all saves.
## To make a new persistent variable, do so like this
# default persistent.monika = X 
# X is either true/false, a number, array (see persistent.clear for arrays) or string based off your choosing
default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None
default persistent.first_poem = None
default persistent.seen_colors_poem = None
default persistent.monika_back = None

# Other Persistent Variables
default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None

# Default Name Variables
## To define a default name do so like this
# default e_name = "Eileen"
default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"

# Poem Variables
# This is how much each character likes your poem day by day
# -1 - Bad, 0 - Neutral, 1 - Good
## To add a new poem person to the poem and their like status
# default e_poemappeal = [0, 0, 0]
default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]

# The last winner of the poem game
default poemwinner = ['sayori', 'sayori', 'sayori']

# This keeps track on who already read your poem
default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False

# This stores how many poems you read so far.
default poemsread = 0

# This stores who likes your poem the most.
# This controls which exclusive scene you will get each chapter.
default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0

# Tracks whether we watched Natsuki's and Yuri's exclusive scenes
default n_exclusivewatched = False
default y_exclusivewatched = False

# Tracks whether Yuri runs away after the first exclusive scene of Act 2
default y_gave = False
default y_ranaway = False

# Tracks if we get to Natsuki's and Yuri's third poem
default n_read3 = False
default y_read3 = False

# Tracks who we chose to side with in Chapter 1
default ch1_choice = "sayori"

default n_poemearly = False

# Tracks whether we wanted to help Sayori and/or Monika
default help_sayori = None
default help_monika = None

# Tracks who we chose to spend time with in Chapter 4
default ch4_scene = "yuri"
default ch4_name = "Yuri"

# Tracks if we accepted Sayori's Confession
default sayori_confess = True

# We read Natsuki's third poem in Chapter 23
default natsuki_23 = None

