#problems: create widget doesnt work in for loop
#cannot get from entry on edit window



import tkinter as tk
from datetime import datetime
import sys
import time
import webbrowser
import os

frames = []
widgets = []
notifiedtimes=[]

def getvalue():
	onoff=turntolist("state.txt")
	if "on" in onoff:
		return 1
	else:
		return 0
def notify():
        time_string = time.strftime("%H:%M")
        if time_string not in notifiedtimes:
	        os.system("""osascript -e 'display notification "Reminder from class Goer" with title "It is time for class"'""")
	        notifiedtimes.append(time_string)
'''
the files txt files used are in a format there it goes
"object,data associated with object,object2"

ex: "science, link to science class, history, link to history class"
this so the txt can be converted to a list and allow other functions 
to read/manipulate the file
'''

#functions used to read/convert/delete files of this format
#turns file into list
def turntolist(filename):
	file=open(filename, "r")
	filestring = file.read()
	return filestring.split(",")

#delete the article and the value
def deletelistitem(file,delarticlename):
	listfile=turntolist("ClassLinks.txt")
	articlelist=listfile[::2]
	delitemindex=articlelist.index(delarticlename)*2
	listfile.pop(delitemindex)
	listfile.pop(delitemindex)
	rewritefile=open(file, "w")
	for i in range(0,len(listfile)-1,1):
		rewritefile.write(listfile[i]+",")

#delete the value
def deletelistvalue(file,delarticlename):
	listfile=turntolist("ClassLinks.txt")
	articlelist=listfile[::2]
	delitemindex=articlelist.index(delarticlename)*2
	listfile.pop(delitemindex+1)
	rewritefile=open(file, "w")
	for i in range(0,len(listfile)-1,1):
		rewritefile.write(listfile[i]+",")

def readvalue(listname,article):
	valueindex=listname.index(article)
	return listname[valueindex+1]

#functional bits

#this function returns the link to the class
def findlink(classname):
	listclass = turntolist("ClassLinks.txt")
	classnamelist=listclass[::2]
	#the slice here removes all odd indexes,
	#leaving only class names, removing links
	if classname in classnamelist:
		classindex=classnamelist.index(classname)
		linkindex= classindex*2+1
		print(linkindex)
		#finds class in list of classes,
		#then doubles and +1 to find index of link to class
		return listclass[linkindex]
	else:
		return "class not found"

#this function opens the browser
def gotoclass(inputclass):
	openclasslink = findlink(inputclass)
	webbrowser.open(openclasslink)

#this creates more widgets for when there are moew classes added

def createclasswidgets(name,number):
	#reads value of num class
	#lenclasslist=len(turntolist("ClassLinks.txt"))-1
	#numclass=lenclasslist/2
	classlabel = tk.Label(classframe,width=17,font=("Helvetica", 20),text=name)
	classbtn= tk.Button(classframe,width=10,relief="flat",text="Go to class",command=lambda: gotoclass(name))
	classbtn.config(fg="#4A86E8")
	widgets.append(classframe)
	modnumber=number%2
	if number != 0:
		rownumber=((number-modnumber)/2)
	else:
		rownumber=0
	if int(modnumber) == 0:
		classlabel.grid(row=int(rownumber),column=0)
		classbtn.grid(row=int(rownumber),column=1)
	else:
		classlabel.grid(row=int(rownumber),column=3)
		classbtn.grid(row=int(rownumber),column=4)

#loads all the classes, this runs everytime the root window is ran
def loadclasses():
	listclass=turntolist("ClassLinks.txt")
	classnamelist=listclass[::2]
	for i in range(0,len(classnamelist)-1,1):
		createclasswidgets(classnamelist[i],i)

#GUI specific functions
def getdate():
	now = datetime.now()

	current_time = now.strftime("%A"+", "+"%m" + "/"+"%d")
	return current_time

def tickingclock():
    time_string = time.strftime("%H:%M")
    alarmtimes=turntolist("times.txt")
    state = var.get()
    statelist=turntolist("state.txt")
    if state==1:
    	if "off" in statelist:
    		rewritefile=open("state.txt", "w")
    		rewritefile.write("on")

    	if time_string in alarmtimes:
    		notify()
    
    if state==0:
    	if "on" in statelist:
    		rewritefile=open("state.txt", "w")
    		rewritefile.write("off")

    clock.config(text=time_string)
    clock.after(1000, tickingclock)

def addorchange():
	newclassname=classnameentry.get()
	print(newclassname)
	newclasslink=classlinkentry.get()
	print(newclasslink)
	listclass=turntolist("ClassLinks.txt")
	classnamelist=listclass[::2]
	print("hi")
	if newclassname in classnamelist:
		delclassindex=classnamelist.index(newclassname)*2
		listclass.pop(delclassindex)
		listclass.pop(delclassindex)
	#now the class and the link is deleted from the list,
	#rewrtie the file with the current list
		rewritefile=open("ClassLinks.txt", "w")
		for i in range(0,len(listclass)-1,1):
			rewritefile.write(listclass[i]+",")
		appendclassfile=open("ClassLinks.txt", "a")
		appendclassfile.write(newclassname+","+newclasslink+",")
		print("class edited")
	else:
		appendclassfile=open("ClassLinks.txt", "a")
		appendclassfile.write(newclassname+","+newclasslink+",")
		print("class added")




def addclass(newclassname,newclasslink):
	listclass=turntolist("ClassLinks.txt")
	if newclassname in listclass:
		print("class already added")
	else:
		appendclassfile=open("ClassLinks.txt", "a")
		appendclassfile.write(newclassname+","+newclasslink+",")
		print("class added")

def deleteclass():
	delclassname=classnameentry.get()
	#go to class names, search for name to delete, delete it and the link after it
	listclass=turntolist("ClassLinks.txt")
	classnamelist=listclass[::2]
	delclassindex=classnamelist.index(delclassname)*2
	listclass.pop(delclassindex)
	listclass.pop(delclassindex)
	#now the class and the link is deleted from the list,
	#rewrtie the file with the current list
	rewritefile=open("ClassLinks.txt", "w")
	for i in range(0,len(listclass)-1,1):
		rewritefile.write(listclass[i]+",")
	print(delclassname+" deleted")

def addtime():
	listtime=turntolist("times.txt")
	newtime=timeentry.get()
	if newtime in listtime and var==1:
		print("class already added")
	else:
		appendclassfile=open("times.txt", "a")
		appendclassfile.write(newtime+",")
		print("time added")

def deletetime():
	listtime=turntolist("times.txt")
	newtime=timeentry.get()
	deltimeindex=listtime.index(newtime)
	listtime.pop(delclassindex)
	print("time deleted")

root = tk.Tk()
root.title("Class Goer")
var = tk.IntVar(value=getvalue())

clockiconpng = tk.PhotoImage(file="Images/clockicon.png")
peniconpng = tk.PhotoImage(file="Images/editpenicon.png")
schedule=tk.PhotoImage(file="Images/schedule.png")
topframe = tk.Frame(root, bg="#EDEDED")
topframe.pack()

date = tk.Label(topframe, text = getdate(), font=("Helvetica", 50))
date.config(fg="white", bg="#4A86E8",anchor="w",width=15, padx=20)
date.grid(row=0, column=0)

clockicon = tk.Label(topframe,image=clockiconpng)
clockicon.config(bg="#EDEDED")
clockicon.grid(row=0, column=1)

clock = tk.Label(topframe,font=("Helvetica", 50))
clock.config(fg="black", bg="#EDEDED", anchor="w")
clock.grid(row=0, column=2)
tickingclock()

parentframe=tk.Frame(root)
parentframe.pack()

classframe = tk.Frame(parentframe, borderwidth=2, relief="groove")
frames.append(classframe)

classframe.pack()

divider2 = tk.Label(root)
divider2.config(bg="#4A86E8", height=1)
divider2.pack(fill="both")

scheduleimg=tk.Label(root, image=schedule, width=650)
scheduleimg.pack()

divider5 = tk.Label(root)
divider5.config(bg="#4A86E8", height=1)
divider5.pack(fill="both")

editwindow=tk.Frame(root)
editwindow.pack()


divider4 = tk.Label(editwindow, text="Enter in Class name and Link to class", font=("Helvetica", 20))
divider4.pack(fill="both")

addorchangeframe=tk.Frame(editwindow)
addorchangeframe.pack()

classnameentry=tk.Entry(addorchangeframe)
classnameentry.grid(column=1,row=0)

addorchangebtn=tk.Button(addorchangeframe,text="Add or change",command=addorchange)
addorchangebtn.grid(column=2,row=0)

classlinkentry=tk.Entry(addorchangeframe)
classlinkentry.grid(column=1,row=1)

deletebtn=tk.Button(addorchangeframe,text="Delete",command=deleteclass)
deletebtn.grid(column=2,row=1)

divider7 = tk.Label(root)
divider7.config(bg="#4A86E8", height=1)
divider7.pack(fill="both")

divider6 = tk.Label(editwindow, text="Edit alarm times", font=("Helvetica", 20))
divider6.pack(fill="both")

timeframe=tk.Frame(editwindow)
timeframe.pack()

timeentry=tk.Entry(timeframe)
timeentry.config(width=20)
timeentry.grid(row=0,column=0)

alarmcheck= tk.Checkbutton(timeframe, text="notifications", variable=var)
alarmcheck.grid(row=1,column=0)


addtimebtn=tk.Button(timeframe,text="add", command=addtime)
addtimebtn.grid(row=0,column=1)

deletetimebtn=tk.Button(timeframe,text="Delete",command=deletetime)
deletetimebtn.grid(row=0,column=2)

loadclasses()
root.mainloop()

