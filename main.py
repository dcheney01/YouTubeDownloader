from tkinter import *
from pytube import YouTube
import shutil  # to move a file

root = Tk()  # initializes the display window
root.geometry('500x300')  # size the display window width x height
root.resizable(0, 0)  # set the fix size of the window
root.title("Download all of your favorite videos")  # give the window a tile

Label(root, text='Youtube Video Downloader', font='arial 20 bold').pack()
#  Label() widget use to display text that users can't modify
#  root is the name of the window
#  text displays the title of the label
#  font the text is written in
#  pack organized widget in block

#  Create field to enter link
link = StringVar()  # string type variable that stores the link entered by the user
Label(root, text='Paste Link Here:', font='arial 15 bold').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)
#  Entry() creates a text field for the user to input to


def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()  # get the link and convert to string
    filepath = video.download()  # download the video and output the filepath
    Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=210)

    #  move the file to downloads
    destination = "C:\\Users\\danie\\Downloads"  # put the file in downloads
   # source = filepath.split('')  # name of the file to be moved, parse with
    # print(source)
    shutil.move(filepath, destination)  # get the last element in the list


Button(root, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=2, command=downloader).place(x=180, y=150)
root.mainloop()
