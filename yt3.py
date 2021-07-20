import tkinter as tk
from tkinter import ttk
from pytube import YouTube
from tkinter.filedialog import askdirectory
import sys

main=tk.Tk()
main.title('YouTube Downloader(Ashirwad TechnoCraft)')
img=tk.PhotoImage(file='source//youtube.png')
main.geometry('516x754+400+20')
main.resizable(0,0)
main.iconbitmap(r'source//favicon.ico')

fn=tk.StringVar()
dn=tk.StringVar()
ch=tk.StringVar()
strms=[]
size=0
yt=''
dn.set('Download')

def progrs_chk(stream,chunk,bytes_remaining):
    global size
    progress=(float(abs(bytes_remaining-size)/size))*float(100)
    prog['value']=progress
    prog.update()

def exitt():
    from tkinter import messagebox as mb
    yn = mb.askquestion('Exit','Are you sure to destroy?')
    if yn=='yes':
        main.destroy()

def youtube():
    flag=0
    global yt
    dn.set('Processing...')
    global strms
    try:
        yt=YouTube(fn.get())
        text.delete('1.0','end')
        text.insert('end',f"\nTitle: {yt.title}\n-----------------------------------------------------------")
        text.insert('end',f"\nViews: {yt.views}\n-----------------------------------------------------------")
        text.insert('end',f"\nDescription: {yt.description}\n-----------------------------------------------------------")
        x=yt.length
        h=x//3600
        m=(x%3600)//60
        s=(x%60)
        text.insert('end',f"\nVideo Size: {h}:{m}:{s}\n-----------------------------------------------------------")
        rate=round(float(yt.rating),2)
        text.insert('end',f"\nRatings: {str(rate)}\n-----------------------------------------------------------")
        if(ch.get()=='Video'):
            strms=yt.streams.filter(file_extension='mp4')
        elif(ch.get()=='Audio'):
            strms=yt.streams.filter(only_audio=True)
        else:
            flag=1
            sys.exit()
        if len(strms)!=0:
            text.insert('end',f"\n\t\t   Available Streams\n-----------------------------------------------------------")
            i=1
            for strm in strms:
                text.insert('end',f"\n{str(i)}. {str(strm)}")
                i+=1
            text.insert('end',"\n-----------------------------------------------------------\nEnter Choice: ")
            text.bind('<Return>',onreturn)
        else:
            text.insert('end',"\nNo Video Available...")
    except:
        text.delete('1.0','end')
        if flag==1:
            text.insert('end',"\nSomething is going wrong!")
            dn.set('Download')
        else:
            text.insert('end',f"\nNo Internet Connection...")
            dn.set('Download')

def onreturn(event):
    global size
    global yt
    dn.set('Downloading...')
    yt.register_on_progress_callback(progrs_chk)
    global strms
    try:
        val=int(text.get('end-3c','end-1c'))
        path=askdirectory()
        vd=strms[val-1]
        size=vd.filesize
        sz=round(size/1024000,2)
        text.insert('end',f"\nFile Size: {str(sz)} MB\n-----------------------------------------------------------")
        vd.download(path)
        text.insert('end',f"\nDownloaded to {path}")
        from tkinter import messagebox as mb
        mb.showinfo('Success','Downloaded Successfully')
    except:
        text.insert('end',"\nCan't download file")
    fn.set('')
    dn.set('Download')
    ch.set('Select')
    
        

tk.Label(main,image=img,justify='center').place(x=0,y=500)
advd=['Audio','Video']
c1=ttk.Combobox(main,width=10,textvariable=ch,value=advd)
c1.place(x=410,y=550)
ch.set('Select')
st=ttk.Style()
st.theme_use('clam')
st.configure('Vertical.TScrollbar',orient='vertical',background='#493F41',bordercolor='#493F41',troughcolor='#493F41',lightcolor='black',
                    darkcolor='black',arrowcolor='white',gripcount=0)
fm=tk.Frame(main,bg='#493F41',relief=tk.FLAT,bd=5)
fm.place(x=2,y=0,height=498,width=512)
tk.Label(fm,text='D   I   S   P   L   A   Y',fg='white',bg='#F50E01',relief='solid',font=('Algerian',20,'bold')).pack(padx=1,pady=2,fill='x')
scrol_y = ttk.Scrollbar(fm,style='Vertical.TScrollbar')
text = tk.Text(fm,bg='black',fg='#32E412',wrap=tk.WORD,padx=5,pady=5,yscrollcommand=scrol_y.set)
scrol_y.pack(side=tk.RIGHT,fill='y')
scrol_y.config(command=text.yview)
text.pack(fill=tk.BOTH,expand=1)

st.configure('my.Horizontal.TProgressbar',background='#918488',foreground='#918488')
prog=ttk.Progressbar(main,style='my.Horizontal.TProgressbar',orient=tk.HORIZONTAL,length=245,mode='determinate')
prog.place(x=10,y=705)

st.configure("TButton",background='red',foreground='white',width=15,borderwidth=1,focusthickness=3,focuscolor='none')
e1=ttk.Entry(main,textvariable=fn,justify='center',width=50).place(x=90,y=550)
b1=ttk.Button(main,textvariable=dn,command=youtube).place(x=260,y=700)
ttk.Button(main,text='Exit',command=exitt).place(x=380,y=700)
tk.Label(main,text="Enter Video Link",bg='#383838',fg='white',relief=tk.FLAT,font=('Times New Roman',15,'bold')).place(x=150,y=520)
text.bind('<Return>',onreturn)

