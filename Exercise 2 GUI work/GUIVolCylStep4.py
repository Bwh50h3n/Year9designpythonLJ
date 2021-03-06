import tkinter as tk
import math

def calcVolCylinder(radius, height):

	#process

	#calc if radius and height are +
	if (radius >= 0 and height >= 0):
		vol = math.pi * radius * radius * height
		vol = round(vol,2)
		return(vol)
	else:
		return(-1)
def runMe(*args):
	print("Runnning")
	r = radiusEntry.get() 
	try:
		r = float(r) #cast r to float
	except:
		r = -1


	radiusEntry.delete(0, tk.END)

	h = heightEntry.get() #gets value and stores in r
	
	try:
		h = float(h) #casts r to float
	except:
		h = -1

	heightEntry.delete(0,tk.END) #deltes content of entry tk.END gets last char

	

	volume = calcVolCylinder(r,h)
	print(volume)

	if volume != -1:
		output.config(state = "normal")
		output.delete("1.0",tk.END) #delete everything
		result = "\n\n\tr\t= "+str(r)+" units\n\th\t= "+str(h)+" units\n\tvolume\t= "+str(volume)+" units\u00B3"
		output.insert(tk.END,result)
		output.config(state = "disabled")	

		file.write(str(r)+"\n")
		file.write(str(h)+"\n")
		file.write(str(volume)+"\n")
	else:
		output.config(state = "normal")
		output.delete("1.0",tk.END) #delete everything
		output.insert(tk.END,"INVALID INPUT")
		output.config(state = "disabled")

def checkSelect():
	state = var.get()

	if state == 1:
		print("High Contrast")
		title.config(fg = "pink", bg = "grey")
		radiusLabel.config(bg = "grey", fg = "pink")
		heightLabel.config(bg = "grey", fg = "pink")
		radiusEntry.config(bg = "grey", fg = "pink")
		heightEntry.config(bg = "grey", fg = "pink")
		output.config(bg = "grey", fg = "pink")
	else:
		print("Low Constrast")
		title.config(fg = "white", bg = "pink")
		radiusLabel.config(fg = "black", bg = "white")
		heightLabel.config(fg = "black", bg = "white")
		radiusEntry.config(fg = "black", bg = "white")
		heightEntry.config(fg = "black", bg = "white")
		output.config(fg = "black", bg = "white")

#main Program
file = open("data.txt","w") 
root = tk.Tk()

title = tk.Label(root, text = "Cylinder Volume Calculator")
#colour
title.config(fg = "white", bg = "pink")
#position (pack is a placment function)
title.pack(fill = tk.BOTH)

divider = tk.Label(root)
divider.config(bg = "black", height = 1)
divider.pack(fill = tk.BOTH)

#radius title, W=west
radiusLabel = tk.Label(root, text = "Radius:")
radiusLabel.config(anchor = tk.W)
radiusLabel.pack(fill = tk.BOTH)
#input box for radius
radiusEntry = tk.Entry(root)
radiusEntry.config()
radiusEntry.pack(fill = tk.BOTH)
#same for height
heightLabel = tk.Label(root, text = "Height:")
heightLabel.config(anchor = tk.W)
heightLabel.pack(fill = tk.BOTH)

heightEntry = tk.Entry(root)
heightEntry.config()
heightEntry.pack(fill = tk.BOTH)

divider = tk.Label(root)
divider.config(bg = "black", height = 1)
divider.pack(fill = tk.BOTH)
#output
output = tk.Text(root)
output.config(width = 50, height = 10, state = "disabled", borderwidth = 2, relief = "groove")
output.pack()

btnrun = tk.Button(root, text = "CALCULATE", highlightbackground='#3E4149')
btnrun.config(fg="blue", command = runMe) #binds command of run me
btnrun.pack(fill = tk.BOTH)

var = tk.IntVar()


check = tk.Checkbutton(root, text = "High Contrast", variable = var, command = checkSelect)
check.config(anchor = tk.W)
check.pack(fill = tk.BOTH)


root.bind("<Return>",runMe)
root.mainloop()
file.close()
print("End Program")
