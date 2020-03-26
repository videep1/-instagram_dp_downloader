from tkinter import *
from bs4 import BeautifulSoup
from PIL import Image,ImageTk
import json,requests,urllib.request,tkinter as tk
def CreateWidgets():
    urlLabel=Label(win,text="INSTAGRAM ID:",background="tan4")
    urlLabel.grid(row=0,column=0,padx=5,pady=5)

    win.urlEntry=Entry(win,width=30,textvariable=insta_id)
    win.urlEntry.grid(row=0,column=1,columnspan=2,pady=5)

    dwldBTN=Button(win,text="download",command=downloader,highlightbackground="green")
    dwldBTN.grid(row=0,column=3,padx=5,pady=5)

    win.resultLabel=Label(win,textvariable=dwldtxt,background="tan4")
    win.resultLabel.grid(row=1,column=0,columnspan=4,padx=5,pady=5)
    win.resultLabel.config(font=("Courier",25))

    win.previewLabel=Label(win,text="DP PREVIEW:",background="tan4")
    win.previewLabel.grid(row=3,column=0,padx=5,pady=5)

    win.dpLabel=Label(win,background="tan4")
    win.dpLabel.grid(row=4,column=1,columnspan=2,padx=1,pady=1)

def downloader():
    download_path = r"C:\Users\videe\ "
    insta_username=insta_id.get()
    insta_url="https://www.instagram.com/"+insta_username
    insta_response=requests.get(insta_url)
    soup=BeautifulSoup(insta_response.text,'html.parser')
    script=soup.find('script',text=re.compile('window._sharedData'))
    page_json=script.text.split('=',1)[1].rstrip(';')
    data=json.loads(page_json)
    dp_url=data['entry_data']['ProfilePage'][0]['graphql']['user']['profile_pic_url_hd']
    dp_name=download_path+insta_username+'.jpg'
    urllib.request.urlretrieve(dp_url,dp_name)
    dp_image=Image.open(dp_name)
    dp_image=dp_image.resize((200,200),Image.ANTIALIAS)
    image=ImageTk.PhotoImage(dp_image)
    win.dpLabel.config(image=image)
    win.dpLabel.photo=image
    dwldtxt.set('DP DOWNLOADED SUCCESSFULLY')

win=tk.Tk()
win.geometry("510x350")
win.title("DP DOWNLOADER")  
win.config(background="tan4")
insta_id=StringVar()
dwldtxt=StringVar()
CreateWidgets()
win.mainloop()






