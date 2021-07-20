import tkinter as tk
from tkinter import ttk
import pafy
from tkinter.filedialog import askdirectory

main=tk.Tk()
main.title('YouTube Downloader(Ashirwad TechnoCraft)')
img=tk.PhotoImage(file='source//youtube.png')
main.geometry('516x754+400+20')
main.resizable(0,0)
main.iconbitmap(r'source//favicon.ico')

fn=tk.StringVar()
dn=tk.StringVar()
strms=[]
yt=''
dn.set('Download')

def progrs_chk(total,recvd,ratio,rate,eta):
    prog['value']=(ratio*100)
    prog.update()

def exitt():
    from tkinter import messagebox as mb
    yn = mb.askquestion('Exit','Are you sure to destroy?')
    if yn=='yes':
        main.destroy()

def youtube():
    global yt
    dn.set('Processing...')
    global strms
    try:
        yt=pafy.new(fn.get())
        text.delete('1.0','end')
        text.insert('end',f"\nTitle: {yt.title}\n-----------------------------------------------------------")
        text.insert('end',f"\nViews: {yt.viewcount}\n-----------------------------------------------------------")
        #text.insert('end',f"\nDescription: {yt.notes}\n-----------------------------------------------------------")
        text.insert('end',f"\nAuthor: {yt.author}\n-----------------------------------------------------------")
        text.insert('end',f"\nVideo Size: {yt.duration}\n-----------------------------------------------------------")
        text.insert('end',f"\nRatings: {round(yt.rating,1)}\n-----------------------------------------------------------")
        text.insert('end',f"\nLikes: {yt.likes}; Dislikes: {yt.dislikes}\n-----------------------------------------------------------")
        strms=yt.allstreams
        if len(strms)!=0:
            text.insert('end',f"\n\t\t   Available Streams\n-----------------------------------------------------------")
            i=1
            for strm in strms:
                text.insert('end',f"\n{str(i)}. Mediatype: {strm.mediatype}; Resolution: {strm.resolution}; Extension: {strm.extension}; File size: {str(round(strm.get_filesize()/1024000,2))} MB")
                i=i+1
            text.insert('end',"\n-----------------------------------------------------------\nEnter Choice: ")
            text.bind('<Return>',onreturn)
        else:
            text.insert('end',"\nNo Video Available...")
    except:
        text.delete('1.0','end')
        text.insert('end',f"\nNo Internet Connection...")
        dn.set('Download')

def onreturn(event):
    global yt
    dn.set('Downloading...')
    #yt.register_on_progress_callback(progrs_chk)
    global strms
    try:
        val=int(text.get('end-3c','end-1c'))
        path=askdirectory()
        vd=strms[val-1]
        #text.insert('end',f"\nFile Size: {str(sz)} MB\n-----------------------------------------------------------")
        vd.download(filepath=path,callback=progrs_chk)
        text.insert('end',f"\nDownloaded to {path}")
        from tkinter import messagebox as mb
        mb.showinfo('Success','Downloaded Successfully')
    except:
        text.insert('end',"\nCan't download file")
    fn.set('')
    dn.set('Download')
    
        

tk.Label(main,image=img,justify='center').place(x=0,y=500)
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
e1=ttk.Entry(main,textvariable=fn,justify='center',width=50).place(x=100,y=550)
b1=ttk.Button(main,textvariable=dn,command=youtube).place(x=260,y=700)
ttk.Button(main,text='Exit',command=exitt).place(x=380,y=700)
tk.Label(main,text="Enter Video Link",bg='#383838',fg='white',relief=tk.FLAT,font=('Times New Roman',15,'bold')).place(x=160,y=520)
text.bind('<Return>',onreturn)

