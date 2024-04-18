from tkinter import *      
from googlesearch import *
#from tkVideoPlayer import TkinterVideo
def voice():
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    z=r.recognize_google(audio)
    s=z.split(" ")
    try:  
        print("" + r.recognize_google(audio))
    #except sr.UnknownValueError:
    # print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    #for searching      
    import webbrowser
    #to search, will ask search query at the time of execution
    query = r.recognize_google(audio)
    y=(s[0])
    import win32com.client as wincl
    if y=="open":
            speak = wincl.Dispatch("SAPI.SpVoice")
            x=""
            for i in range(1,len(s)):
                x+=(s[i])
            speak.Speak("okay opening "+x)
            
            import os
            os.system(x+'.exe')
    elif y=="play":
        speak= wincl.Dispatch("SAPI.SpVoice")
        speak.Speak("playing a song")
        webbrowser.open("https://www.youtube.com/watch?v=LYmWO4vvYHg&t=37s") 
    elif y=="project":
        speak = wincl.Dispatch("SAPI.SpVoice")
        speak.Speak("Opening project 2.0 ")
            
        import os
        from supabase import create_client, Client
        import json
        

        supabase: Client = create_client("https://gndtrrzxqwpfgiilmppk.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImduZHRycnp4cXdwZmdpaWxtcHBrIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzExMDY4MTQsImV4cCI6MTk4NjY4MjgxNH0.SiRXNykHWc9srIgAFNemYQqdENt3IfkqVyMxnLLnA90")
        data = supabase.table("bag2").select("*").execute()


        # Assert we pulled real data.
        list1=[]
        list=[3587,3386,4889,3952,3950,3949]
        #data1 = supabase.table('bag2').delete().match({'data':3386}).execute()
        for i in data.data:
            list1.append(i['data'])
        def br1():
            
            supabase: Client = create_client("https://gndtrrzxqwpfgiilmppk.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImduZHRycnp4cXdwZmdpaWxtcHBrIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzExMDY4MTQsImV4cCI6MTk4NjY4MjgxNH0.SiRXNykHWc9srIgAFNemYQqdENt3IfkqVyMxnLLnA90")
            data1 = supabase.table('bag2').delete().match({'data':3587}).execute()
        def br2():
            supabase: Client = create_client("https://gndtrrzxqwpfgiilmppk.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImduZHRycnp4cXdwZmdpaWxtcHBrIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzExMDY4MTQsImV4cCI6MTk4NjY4MjgxNH0.SiRXNykHWc9srIgAFNemYQqdENt3IfkqVyMxnLLnA90")
            data2 = supabase.table('bag2').delete().match({'data':3386}).execute()
        def br3():
            supabase: Client = create_client("https://gndtrrzxqwpfgiilmppk.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImduZHRycnp4cXdwZmdpaWxtcHBrIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzExMDY4MTQsImV4cCI6MTk4NjY4MjgxNH0.SiRXNykHWc9srIgAFNemYQqdENt3IfkqVyMxnLLnA90")
            data3 = supabase.table('bag2').delete().match({'data':4889}).execute()
        def br4():
            supabase: Client = create_client("https://gndtrrzxqwpfgiilmppk.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImduZHRycnp4cXdwZmdpaWxtcHBrIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzExMDY4MTQsImV4cCI6MTk4NjY4MjgxNH0.SiRXNykHWc9srIgAFNemYQqdENt3IfkqVyMxnLLnA90") 
            data4 = supabase.table('bag2').delete().match({'data':3952}).execute()
        def br5():
            supabase: Client = create_client("https://gndtrrzxqwpfgiilmppk.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImduZHRycnp4cXdwZmdpaWxtcHBrIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzExMDY4MTQsImV4cCI6MTk4NjY4MjgxNH0.SiRXNykHWc9srIgAFNemYQqdENt3IfkqVyMxnLLnA90")
            data5 = supabase.table('bag2').delete().match({'data':3950}).execute()
        def br6():
            supabase: Client = create_client("https://gndtrrzxqwpfgiilmppk.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImduZHRycnp4cXdwZmdpaWxtcHBrIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzExMDY4MTQsImV4cCI6MTk4NjY4MjgxNH0.SiRXNykHWc9srIgAFNemYQqdENt3IfkqVyMxnLLnA90")
            data6 = supabase.table('bag2').delete().match({'data':3949}).execute()
        def bag1ready():
                    r= Toplevel()
                    canvas=Canvas(r,width = 1080, height = 1080, bg = 'white')
                    canvas.pack(expand= YES)
                    f="data6.gif"
                    gif1= PhotoImage(file=f)
                    canvas.create_image(0, 0, image = gif1, anchor = NW)
                    b=Button(r,text="OK",font=("Helica",35),bg="black",fg="white",command=lambda: [br1(),r.destroy(),root.destroy()])
                    b.pack(side="bottom")
                    r.mainloop()
        def bag2ready():
                    r= Toplevel()
                    canvas=Canvas(r,width = 1080, height = 1080, bg = 'white')
                    canvas.pack(expand= YES)
                    f="data3.gif"
                    gif1= PhotoImage(file=f)
                    canvas.create_image(0, 0, image = gif1, anchor = NW)
                    b=Button(r,text="OK",font=("Helica",35),bg="black",fg="white",command=lambda: [br2(),r.destroy(),root.destroy()])
                    b.pack(side="bottom")
                    r.mainloop()
        def bag3ready():
                    r= Toplevel()
                    canvas=Canvas(r,width = 1080, height = 1080, bg = 'white')
                    canvas.pack(expand= YES)
                    f="data5.gif"
                    gif1= PhotoImage(file=f)
                    canvas.create_image(0, 0, image = gif1, anchor = NW)
                    b=Button(r,text="OK",font=("Helica",35),bg="black",fg="white",command=lambda:[br3(),r.destroy(),root.destroy()])
                    b.pack(side="bottom")
                    r.mainloop()
        def bag4ready():
                    r= Toplevel()
                    canvas=Canvas(r,width = 1080, height = 1080, bg = 'white')
                    canvas.pack(expand= YES)
                    f="data4.gif"
                    gif1= PhotoImage(file=f)
                    canvas.create_image(0, 0, image = gif1, anchor = NW)
                    b=Button(r,text="OK",font=("Helica",35),bg="black",fg="white",command=lambda:[br4(),r.destroy(),root.destroy()])
                    b.pack(side="bottom")
                    r.mainloop()
        def bag5ready():
                    r= Toplevel()
                    canvas=Canvas(r,width = 1080, height = 1080, bg = 'white')
                    canvas.pack(expand= YES)
                    f="data1.gif"
                    gif1= PhotoImage(file=f)
                    canvas.create_image(0, 0, image = gif1, anchor = NW)
                    b=Button(r,text="OK",font=("Helica",35),bg="black",fg="white",command=lambda:[br5(),r.destroy(),root.destroy()])
                    b.pack(side="bottom")
                    r.mainloop()
        def bag6ready():
                    r= Toplevel()
                    canvas=Canvas(r,width = 1080, height = 1080, bg = 'white')
                    canvas.pack(expand= YES)
                    f="data2.gif"
                    gif1= PhotoImage(file=f)
                    canvas.create_image(0, 0, image = gif1, anchor = NW)
                    b=Button(r,text="OK",font=("Helica",35),bg="black",fg="white",command=lambda:[br6(),r.destroy(),root.destroy()])
                    b.pack(side="bottom")
                    r.mainloop()

                    
        def bagnotready():
                    r= Toplevel()
                    r.config(bg="black")
                    canvas=Canvas(r,width = 1080, height = 1080, bg = 'white')
                    canvas.pack(expand= YES)
                    f="nobag.gif"
                    gif1= PhotoImage(file=f)
                    canvas.create_image(0, 0, image = gif1, anchor = NW)
                    b=Button(r,text="OK",font=("Helica",35),bg="black",fg="white",command=lambda:(r.destroy()))
                    b.pack(side="bottom")
                    r.mainloop()
        root=Toplevel()
        root.title("mainpage")
        label=Label(root,text="SELECT BAG NUMBER!",font=("Monotype",30))
              
        label.pack()
        f="bag1.gif"
        f1="bag2.gif"
        f2="bag3.gif"
        f3="bag4.gif"
        f4="bag5.gif"
        f5="bag6.gif"
        
        img= PhotoImage(file=f)
        img1=PhotoImage(file=f1)
        img2=PhotoImage(file=f2)
        img3=PhotoImage(file=f3)
        img4=PhotoImage(file=f4)
        img5=PhotoImage(file=f5)
        if 3587 in list1:
            bu=Button(root, image=img ,command=lambda:[bag1ready()])
            bu.pack()
        elif 3587 not in list1:
            bu=Button(root, image=img, command=lambda:[bagnotready()])
            bu.pack()
        if 3386 in list1:
            bu1=Button(root, image=img1,command=lambda:[bag2ready()])
            bu1.pack()
        elif 3386 not in list1:
            bu1=Button(root, image=img1, command=lambda:[bagnotready()])
            bu1.pack()
        if 4889 in list1:
            bu2=Button(root, image=img2,command=lambda:[bag3ready()])
            bu2.pack()
        elif 4889 not in list1:
            bu2=Button(root, image=img2, command=lambda:[bagnotready()])
            bu2.pack()
        if 3952 in list1:       
            bu3=Button(root, image=img3,command=lambda:[bag4ready()])
            bu3.pack()
        elif 3952 not in list1:
            bu3=Button(root, image=img3, command=lambda:[bagnotready()])
            bu3.pack()
        if 3950 in list1:
            bu4=Button(root, image=img4,command=lambda:[bag5ready()])
            bu4.pack()
        elif 3950 not in list1:
            bu4=Button(root, image=img4, command=lambda:[bagnotready()])
            bu4.pack()
        if 3949 in list1:    
            bu5=Button(root, image=img5,command=lambda:[bag6ready()])
            bu5.pack()
        elif 3949 not in list1:
            bu5=Button(root, image=img5, command=lambda:[bagnotready()])
            bu5.pack()
        mainloop()
        
    
        

                

    else:
        #chrome_path = r'x %s'
        speak= wincl.Dispatch("SAPI.SpVoice")
        speak.Speak("searching for "+query)
    # for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):5
        webbrowser.open("https://google.com/search?q=%s" % query)
# main voice assisstant button




'''def vd():
    import tkinter as tk
    from tkVideoPlayer import TkinterVideof

    root = tk.Toplevel()
    videoplayer = TkinterVideo(master=root)
    videoplayer.load("vsv.mp4")
    videoplayer.pack(expand=True,fill="both")
    root.after(8000,lambda:root.destroy())
    videoplayer.play() # play the video
    root.mainloop()'''
root = Tk()  
root.geometry=("100*100")
root.config(bg="black")
root.title("StrawHats")    
f="img.gif" 
img = PhotoImage(file=f) 
output1="click"
b=Button(root,image=img,command=lambda:[voice()])
b.pack()
mainloop()   



