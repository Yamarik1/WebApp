from tkinter import *
from helper import get_grid_list

def make_grid_window(yearList):
    
    
    
    gridWindow = Tk()

    
    gridWindow.title("Grid Window")
    gridWindow.geometry("1200x900")

    canvas = Canvas(gridWindow)
    
    def on_mousewheel(event):
        if event.num == 4:
            canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            canvas.yview_scroll(1, "units")
        else:
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    scrollbar = Scrollbar(gridWindow, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y) 

    canvas.pack(side="left", fill="both", expand = True)
    canvas.configure(yscrollcommand=scrollbar.set)

    tableFrame = Frame(canvas)

    canvas.create_window((0,0), window=tableFrame, anchor="nw")

    def update_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    tableFrame.bind("<Configure>", update_scroll_region)

    cleanList = get_grid_list(yearList)
    # print(cleanList[1])
    for i in range(len(cleanList)):
        for j in range(len(cleanList[0])):

            entry = Entry(tableFrame, width=20)
            entry.grid(row=i, column=j)
            entry.insert(END, cleanList[i][j])

    # scrollbar.config(command=tableFrame)

    canvas.bind("<Button-4>", on_mousewheel)
    canvas.bind("<Button-5>", on_mousewheel)
    canvas.bind("<MouseWheel>", on_mousewheel)

    gridWindow.mainloop() 