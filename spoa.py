from tkinter import messagebox

try:    
    import customtkinter as t
    from pygame import mixer
    import ctypes
    import os,sys
    import random
    from mutagen.mp3 import MP3
    from mutagen.wave import WAVE
    import schedule
    from pytube import YouTube 
    from moviepy.editor import *



    RUNNING = True
    mixer.init()
    PlaylistOK = True
    PLAYLISTJOB = ""

    def stops():
        global PlaylistOK
        PlaylistOK = False
        try:mixer.music.stop()
        except:pass
        
    def DownloadVideomp3():
        global varS,UrlEntry
        try:
            SongsD = os.path.join(os.getcwd(),"Songs")

            url = varS.get() 
            try:yt = YouTube(url) 
            except:pass
            video = yt.streams.filter(only_audio=True).first()
            Name = []
            for i in video.title:
                if i == '"' or i=="'":
                    pass
                else:Name.append(i)
            Fname = ""
            for i in Name:
                Fname += i
            video.download(output_path=SongsD,filename=f"{Fname[0:20]}.mp4")

            def MP4ToMP3(mp4, mp3):
                FILETOCONVERT = AudioFileClip(mp4)
                FILETOCONVERT.write_audiofile(mp3)
                FILETOCONVERT.close()

            LOL1 = os.path.join(SongsD,f"{Fname[0:20]}.mp4")
            LOL2 = os.path.join(SongsD,f"{Fname[0:20]}.mp3")

            VIDEO_FILE_PATH = LOL1
            AUDIO_FILE_PATH = LOL2

            MP4ToMP3(VIDEO_FILE_PATH, AUDIO_FILE_PATH)
            os.remove(os.path.join(SongsD,f"{Fname[0:20]}.mp4"))

        except:pass
        UrlEntry.delete(0,t.END)

    def loopplay():
        try:mixer.music.play(-1)
        except:pass
        
    def plays():
        try:mixer.music.play()
        except:pass

    def Play_list():
        global GoodList,mixer,new,PlaylistOK,PLAYLISTJOB
        temp = len(GoodList)
        song = random.randint(0,temp-1)

        try:schedule.cancel_job(PLAYLISTJOB)
        except:pass
        
        loadMusic(GoodList[song])
        mixer.music.play()
        if GoodList[song][-4:] == ".mp3":
            audio = MP3(os.path.join(new,GoodList[song]))
        elif GoodList[song][-4:] ==".wav":
            audio = WAVE(os.path.join(new,GoodList[song]))
        TimeS = audio.info.length

        TimeS = int(TimeS)
        
        PLAYLISTJOB = schedule.every(TimeS).seconds.do(Play_list)
        


    def volume_edit(vol_slider_var):
        vol = vol_slider_var.get()
        if vol == 0:
            try:mixer.music.set_volume(0)
            except:pass
        elif vol == 1:
            try:mixer.music.set_volume(0.1)
            except:pass
        elif vol == 2:
            try:mixer.music.set_volume(0.2)
            except:pass
        elif vol == 3:
            try:mixer.music.set_volume(0.3)
            except:pass
        elif vol == 4:
            try:mixer.music.set_volume(0.4)
            except:pass
        elif vol == 5:
            try:mixer.music.set_volume(0.5)
            except:pass
        elif vol == 6:
            try:mixer.music.set_volume(0.6)
            except:pass
        elif vol == 7:
            try:mixer.music.set_volume(0.7)
            except:pass
        elif vol == 8:
            try:mixer.music.set_volume(0.8)
            except:pass
        elif vol == 9:
            try:mixer.music.set_volume(0.9)
            except:pass
        elif vol == 10:
            try:mixer.music.set_volume(1)
            except:pass
        else:pass

    def create(i,x,y):
        temp = i[:15]
        temp = temp[:-4]
        button = t.CTkButton(Songs,text=f"{temp}",
                            fg_color="#b884ed",bg_color="transparent",hover_color="#521e87",corner_radius=20,border_color="#dbc1f6",border_width=1,width=100,
                            text_color="#0d0516",font=("Calibri",12))
        button.place(x=x,y=y)
        button.configure(command=lambda: loadMusic(i))

    def prot():
        global RUNNING
        window.destroy()
        RUNNING = False
        

    def loadMusic(name):
        mixer.music.load(f"./Songs/{name}")

    window = t.CTk()
    window.title("Ringo No Malum 🍎")
    window.resizable(False,False)
    window.protocol("WM_DELETE_WINDOW", prot)
    w = 876
    h = 355
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    window._set_appearance_mode("dark")

    appleRaw = "./EXP/apple.ico"

    id = "mycompany.myproduct.subproduct.version"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(id)

    window.iconbitmap(appleRaw)

    Frame = t.CTkFrame(window,border_color="red",border_width=3,fg_color="#660000")
    Frame.pack(fill="both",expand = 1)

    RnM = "RnM"
    YtDownload = "YtDownloader"

    tabs = t.CTkTabview(Frame,corner_radius=20, 
                            bg_color="transparent",fg_color="#3d0404",
                            border_color="#7e82ab",border_width=2,
                            segmented_button_fg_color="#181c45",segmented_button_selected_color="#10122e",
                            segmented_button_selected_hover_color="#04040b",segmented_button_unselected_color="#282f73",
                            segmented_button_unselected_hover_color="#52588f",
                            text_color="#907eab")

    tabs.add(RnM)
    tabs.add(YtDownload)
    tabs.pack(fill="both",expand = 1)



    FrameRnM = tabs.tab(RnM)
    FrameYtDler = tabs.tab(YtDownload)

    #-----------------Ringo No Malum-------------Ringo No Malum-------------Ringo No Malum-- 

    RnMTitle = t.CTkLabel(FrameRnM,text="𝙍𝙣𝙈",bg_color="transparent", fg_color="transparent",text_color="#73282f",font=("Calibri",14)).place(x=0,y=0)

    vol_slider_var = t.IntVar(FrameRnM,value=0)

    volume_slider = t.CTkSlider(FrameRnM, orientation="vertical",from_=0,to=10,variable=vol_slider_var,command=lambda e:volume_edit(vol_slider_var),
                                    border_width=2,
                                    fg_color="#593d81",
                                    progress_color="#1c102e",
                                    border_color="#907eab",
                                    button_color="#472873",
                                    button_hover_color="#0e0817",
                                    button_corner_radius=20)
    vol_slider_var.set(2)
    mixer.music.set_volume(0.2)
    volume_slider.place(x=14,y=35)

    Songs = t.CTkFrame(FrameRnM,fg_color="transparent",border_width=2,border_color="#ff0000",width=600,height=270,corner_radius=10)
    Songs.place(x=60,y=2)

    Commands = t.CTkFrame(FrameRnM,width=170,height=270,fg_color="transparent",border_color="#10122e",border_width=2,corner_radius=15)
    Commands.place(x=665,y=0)

    play = t.CTkButton(Commands,text="Play",width=70,bg_color="transparent", fg_color="#b30000",text_color="#efcccc",border_color="#e09999",border_width=1,hover_color="#110000",font=("Shadows Into Light",13),command=plays).place(x=5,y=10)#55
    playLoop = t.CTkButton(Commands,text="PlayLoop",width=70,bg_color="transparent", fg_color="#b30000",text_color="#efcccc",border_color="#e09999",border_width=1,hover_color="#110000",font=("Lobster",13),command=loopplay).place(x=90,y=10)
    pause = t.CTkButton(Commands,text="Pause",width=70,bg_color="transparent", fg_color="#b30000",text_color="#efcccc",border_color="#e09999",border_width=1,hover_color="#110000",font=("Lobster",13),command=lambda:mixer.music.pause()).place(x=5,y=55)#145
    unpause = t.CTkButton(Commands,text="Unpause",width=70,bg_color="transparent", fg_color="#b30000",text_color="#efcccc",border_color="#e09999",border_width=1,hover_color="#110000",font=("Lobster",13),command=lambda:mixer.music.unpause()).place(x=90,y=55)#190
    RandomPlay = t.CTkButton(Commands,text="PlayList",width=70,bg_color="transparent", fg_color="#b30000",text_color="#efcccc",border_color="#e09999",border_width=1,hover_color="#110000",font=("Lobster",13),command=Play_list,anchor=t.CENTER).place(x=5,y=100)
    unload = t.CTkButton(Commands,text="Unload",width=70,bg_color="transparent", fg_color="#b30000",text_color="#efcccc",border_color="#e09999",border_width=1,hover_color="#110000",font=("Lobster",13),command=lambda:mixer.music.unload()).place(x=90,y=100)#235
    stop = t.CTkButton(Commands,text="Stop",width=70,bg_color="transparent", fg_color="#b30000",text_color="#efcccc",border_color="#e09999",border_width=1,hover_color="#110000",font=("Lobster",13),command=stops).place(x=5,y=145)
    quit = t.CTkButton(Commands,text="Quit",width=70,bg_color="transparent", fg_color="#b30000",text_color="#efcccc",border_color="#e09999",border_width=1,hover_color="#110000",font=("Lobster",13),command=prot).place(x=90,y=145)#235 5 47 47 47

    current_dir = os.getcwd()
    new = os.path.join(current_dir,"Songs")
    listSongs = os.listdir(new)

    x = 10
    y = 10

    GoodList = []

    for i in listSongs:
        GoodList.append(i)

    for i in GoodList:
        create(i,x,y)
        x += 120
        if x >= 500:
            x= 10
            y+=45
        if y > 270:
            break


    #-----------------YT DOWNLOADER-------------YT DOWNLOADER-------------YT DOWNLOADER-- 

    varS = t.StringVar(FrameYtDler)
    
    ytlabelTitle =t.CTkLabel(FrameYtDler,text="𝙔𝙩𝘿",bg_color="transparent", fg_color="transparent",text_color="#73282f",font=("Calibri",14)).place(x=0,y=0)

    labelUrl = t.CTkLabel(FrameYtDler,text="𝐔𝐫𝐥:",bg_color="transparent", fg_color="transparent",text_color="#2f3786",font=("Calibri",35)).place(x=20,y=40)
    UrlEntry = t.CTkEntry(FrameYtDler,textvariable=varS,width=300,height=33,bg_color="transparent",fg_color="#231439",border_color="#907eab",border_width=1,text_color="#6b528f",corner_radius=15,placeholder_text="[ YouTube Video Url ]",placeholder_text_color="#c7bed5")
    UrlEntry.place(x=80,y=46)
    DownloadVideo =t.CTkButton(FrameYtDler,width=180,text="𝑫𝒐𝒘𝒏𝒍𝒐𝒂𝒅",bg_color="transparent",fg_color="#8e0000",corner_radius=15,border_color="#ea9999",border_width=1,hover_color="#140000",text_color="#e06666",font=("Calibri",30),command=DownloadVideomp3).place(x=130,y=90)
    
    

    while RUNNING:
        window.update()
        schedule.run_pending()
        if not PlaylistOK:
            try:schedule.cancel_job(PLAYLISTJOB)
            except:pass
            PlaylistOK = True
            
except:messagebox.showerror("RnM Failed","Couldn't Boot")
