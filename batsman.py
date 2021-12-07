from tkinter import *
from tkinter import filedialog, messagebox, ttk
from tkinter import font
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

plt.rcParams["figure.figsize"] = [8,6]
sns.set_style("darkgrid")

#Starting Tk function
root = Tk()
root.geometry("900x700")
root.config(bg="black")
root.pack_propagate(False)

# Main screen
title = Label(root, text="CRICKET DATA ANALYSIS",bg="black",font=("", 30, 'bold'), fg="white", relief='raised', borderwidth=5, underline=1)
input1 = Entry(root, borderwidth=5, width=60, fg='#00ff00',bg="#000000")
title.place(relx = 0.5, rely = 0.3, anchor=CENTER)
input1.place(relx = 0.5, rely = 0.47, anchor = CENTER)


# histogram plot runs, 4s, 6s 
def fourPlot(object):
    object['4s'].hist(bins = 30)
    plt.xlabel("4s")
    plt.show()

def sixPlot(object):
    object['6s'].hist(bins=30)
    plt.show()
    
def srPlot(object):
    object['SR'].hist(bins=30)
    plt.show()

def boxPlot(selected, object):
    sns.boxplot(y=selected, data = object)
    plt.show()


def Batsman_search():
    
    new_window = Toplevel()
    new_window.geometry("900x700")
    new_window.config(bg="black")
    new_window.pack_propagate(False)
    new_window.title("Batsman Perfomance Analysis")
    #Loading dataset
    bat_data = pd.read_csv("Dataset/Batsman_Data.csv")
    global name
    name = input1.get()
    if name.title()== 'Ms Dhoni':
        name = 'MS Dhoni'
    else:
        name = name.title()
        
    batsman = bat_data[bat_data.Batsman.str.strip() == name]
    batsman_details = batsman[["Runs", "BF", "SR", "4s", "6s"]]
    batsman_cat = batsman[["Opposition", "Ground"]]
    #removing the '-' from the data
    for col in batsman_details:
        batsman_details[col] = batsman_details[col].str.replace("-", "")
        
    #converting the data to numeric
    for col in batsman_details:
        batsman_details[col] = pd.to_numeric(batsman_details[col])

    #Defining text display labels
    headingString = name + "ICC World Cup Analysis till 20"
    heading = Label(new_window, text = headingString)
    runs = Label(new_window, text= "Average Runs scored: "+ str(batsman_details.Runs.mean()), bg="black",font=("", 14, 'bold'), fg="white", relief='raised', borderwidth=5 )
    srate = Label(new_window, text = "Average Strike rate: "+ str(batsman_details.SR.mean()), bg="black",font=("", 20, 'bold'), fg="white", relief='raised', borderwidth=5 )
    bf = Label(new_window, text = "Average Balls faced: "+ str(batsman_details.BF.mean()),bg="black",font=("", 20, 'bold'), fg="white", relief='raised', borderwidth=5)
    fours = Label(new_window, text = "Total 4s in ODI till now: "+ str(batsman_details['4s'].sum()),bg="black",font=("", 20, 'bold'), fg="white", relief='raised', borderwidth=5)
    six = Label(new_window, text = "Total 6s in ODI till now: "+ str(batsman_details['6s'].sum()),bg="black",font=("", 20, 'bold'), fg="white", relief='raised', borderwidth=5)

    #plotting the graphs of different datasets
    # batsman_details.plot()

    # #plotting runs graph
    # batsman_details.Runs.plot()

    # #plotting runs histogram
    # batsman_details.Runs.hist(bins = 50)

    #PLOT buttons
    fourButton = Button(new_window, text = "4s plot", command= lambda: fourPlot(batsman_details))
    fourButton.place(relx=0.3, rely=0.9, anchor=CENTER)

    sixButton = Button(new_window, text = "Six plot", command= lambda: sixPlot(batsman_details))
    sixButton.place(relx=0.4, rely=0.9, anchor=CENTER)
    
    srButton = Button(new_window, text = "Strike Rate", command= lambda: srPlot(batsman_details))
    srButton.place(relx=0.5, rely=0.9, anchor=CENTER)
    

    #BOX PLOT
    options= [
    "Runs", 
    "Strike Rate",
    "4s", 
    "6s", 
    "Balls Faced"
    ]
    
    clicked=StringVar()
    clicked.set(options[0])

    drop=OptionMenu(new_window, clicked, *options)
    drop.place(relx=0.8, rely=0.5, anchor=CENTER)

    boxPlotButton = Button(new_window, text="Show Selection", command =lambda: boxPlot(clicked.get(), batsman_details))
    boxPlotButton.place(relx=0.8, rely=0.8, anchor=CENTER)


    # PLOT LINE GRAPH FOR AGE, AGE_MEAN, AGE_MEDIAN 

    # plt.rcParams["figure.figsize"] = [8,6]
    # fig=plt.figure()
    # ax = fig.add_subplot(111)
    # batsman_details.Runs.plot(kind='kde', ax=ax)
    # batsman_details['BF'].plot(kind='kde', ax=ax, color ='green' )
    # batsman_details['SR'].plot(kind='kde', ax=ax, color ='red')
    # lines,labels = ax.get_legend_handles_labels()
    # ax.legend(lines, labels, loc='best')
    
    # #setting position of labels
    heading.place(relx=0.5, rely=0.1, anchor=CENTER)
    srate.place(relx=0.5, rely=0.3, anchor=CENTER)
    bf.place(relx=0.5, rely=0.4, anchor=CENTER)
    fours.place(relx=0.5, rely=0.5, anchor=CENTER)
    six.place(relx=0.5, rely=0.6, anchor=CENTER)
    runs.place(relx=0.5, rely=0.7, anchor=CENTER)
    
    close_player=Button(new_window,text="Close Window",command= new_window.destroy)
    close_player.place(relx=0.5, rely=0.8, anchor=CENTER)

    
   

searchButton = Button(root, text="Search", command= Batsman_search)
searchButton.place(relx = 0.5, rely = 0.6, anchor = CENTER)



root.mainloop()