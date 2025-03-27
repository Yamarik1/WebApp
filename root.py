import tkinter as tk
from helper import *
from grid_window import *
from tkinter import messagebox
# from tkcalendar import Calendar


def make_window():

    years = []
    
    data = read_data(years)
    # print(years)
    cleanData = clean_data(data, years)

    

    # print(cleanData)
    # print(data)
    # # print("test")
    root = Tk()

    # cal = Calendar(root, selectmode = 'day', year = 2025, month = 3, dat = 22)
    # cal.pack(pady = 20)

    # def grad_date():

    #     date.config(text = "Date is:" + cal.get_date())

    # Button(root, text = "Get Date", command= grad_date).pack(pady = 20)

    # date = Label(root, text = "")
    # date.pack(pady = 20)
    # root window title and dimension
    root.title("Fittness Info")
    # Set geometry (widthxheight)
    root.geometry('1200x900')

    # adding menu bar in root window
    # new item in menu bar labelled as 'New'
    # adding more items in the menu bar 
    menu = Menu(root)
    item = Menu(menu)
    item.add_command(label='New')
    menu.add_cascade(label='File', menu=item)
    root.config(menu=menu)
    
    # btn.pack(side="left")
    topFrame = Frame(root,borderwidth=2, relief="solid", width=500, height=100, highlightbackground="black", highlightthickness=1)
    topFrame.pack(padx = 50, pady = 10, fill=tk.BOTH)
    yearFrame = Frame(topFrame, borderwidth=2, relief="solid", width=100, height=100, highlightbackground="black", highlightthickness=1)
    yearFrame.pack(side = tk.LEFT, padx = 10, pady=15, fill=tk.BOTH)

    

    yearText = Label(yearFrame, text='Year')
    yearText.pack(side="left")

    checkFrame = Frame(topFrame, borderwidth=2, relief="solid", width = 300, height=100, highlightbackground="black", highlightthickness=1)

    check_vars = {}
    colVal = 0
    rowVal = 0
    for i, item in enumerate(years):
        var = tk.BooleanVar()
        check_vars[item] = var
        check_button = tk.Checkbutton(checkFrame, text=item, variable=var)
        check_button.grid(row=rowVal, column=colVal, sticky="w")
        if (rowVal + 1) % 3 == 0:
            rowVal = 0
            colVal += 1
        else:
            rowVal += 1

    lowerBox = Frame(root,borderwidth=2, relief="solid", width=500, height=200, highlightbackground="black", highlightthickness=1)
    lowerBox.pack(side=tk.TOP,padx=50,  pady = 10, fill=tk.BOTH)
    lowerBox.grid_columnconfigure(0, weight=1)
    lowerBox.grid_columnconfigure(1, weight=1)
    lowerBox.grid_columnconfigure(2, weight=1)
    # hide_frame(lowerBox)
    heartLabel = Label(lowerBox, text="Heart")
    heartLabel.grid(row=0, column=0, sticky="w", padx = 75)
    heartBox = Frame(lowerBox, borderwidth=2, relief="solid", width=100, height=100, highlightbackground="black", highlightthickness=1)
    heartBox.grid(row=1, column=0, sticky="w", pady =10, padx = 10)

    stepLabel =Label(lowerBox, text="Steps")
    stepLabel.grid(row=0, column=1, padx = 10)
    stepsBox = Frame(lowerBox, borderwidth=2, relief="solid", width=100, height=100, highlightbackground="black", highlightthickness=1)
    stepsBox.grid(row=1, column=1, sticky="n", pady = 10)

    milesLabel = Label(lowerBox, text="Miles")
    milesLabel.grid(row=0, column=2, sticky = 'e', padx = 75)
    milesBox = Frame(lowerBox, borderwidth=2, relief="solid", width=100, height=100, highlightbackground="black", highlightthickness=1)
    milesBox.grid(row=1, column=2, sticky="e", pady=10, padx = 10)
    
    hide_frame(lowerBox)

    gridFrame = Frame(root)
    gridFrame.pack(side=TOP)

    hide_frame(gridFrame)
    
    def confirmValues():

        # hide_frame(gridFrame)
        selectedYears = []
        for item, var in check_vars.items():
            # print(var.get())
            if var.get() == True:
                selectedYears.append(item)
        try:
            yearList = get_list(cleanData, selectedYears)
            if len(yearList) == 0:
                raise ValueError("Please select at least one year")
        except ValueError as e:
            messagebox.showerror("Error", e)
            return
        

        totalInsights = get_insights(yearList)
        # print(totalInsights)
        heartVal = totalInsights[0]
        stepsVal = totalInsights[1]
        milesVal = totalInsights[2] * .000621371
        # heartText = "Total: " + str(testHeart) + "\nPer Year: 10"

        heartTotal = Label(heartBox, text=("Total: " + str(heartVal)))
        heartTotal.grid(row=0, column=0, sticky='w', padx=5, pady=10)
        heartYear = Label(heartBox, text="Per Year: " + str(heartVal / (len(yearList)/365)) )
        heartYear.grid(row=1, column=0, sticky='w', padx=5, pady=10)
        heartWeek = Label(heartBox, text="Per Week: " + str(heartVal / (len(yearList) / 56)))
        heartWeek.grid(row=2, column=0, sticky='w', padx=5, pady=10)
        heartDay = Label(heartBox, text="Per Day: " + str(heartVal / (len(yearList) / 1)))
        heartDay.grid(row=3, column=0, sticky='w', padx=5, pady=10)


        stepsTotal = Label(stepsBox, text=("Total: " + str(stepsVal)))
        stepsTotal.grid(row=0, column=0, sticky='w', padx=5, pady=10)
        stepsYear = Label(stepsBox, text="Per Year: " + str(stepsVal / (len(yearList)/365)) )
        stepsYear.grid(row=1, column=0, sticky='w', padx=5, pady=10)
        stepsWeek = Label(stepsBox, text="Per Week: " + str(stepsVal / (len(yearList) / 56)))
        stepsWeek.grid(row=2, column=0, sticky='w', padx=5, pady=10)
        stepsDay = Label(stepsBox, text="Per Day: " + str(stepsVal / (len(yearList) / 1)))
        stepsDay.grid(row=3, column=0, sticky='w', padx=5, pady=10)

        milesTotal = Label(milesBox, text=("Total: " + str(milesVal)))
        milesTotal.grid(row=0, column=0, sticky='w', padx=5, pady=10)
        milesYear = Label(milesBox, text="Per Year: " + str(milesVal / (len(yearList)/365)) )
        milesYear.grid(row=1, column=0, sticky='w', padx=5, pady=10)
        milesWeek = Label(milesBox, text="Per Week: " + str(milesVal / (len(yearList) / 56)))
        milesWeek.grid(row=2, column=0, sticky='w', padx=5, pady=10)
        milesDay = Label(milesBox, text="Per Day: " + str(milesVal / (len(yearList) / 1)))
        milesDay.grid(row=3, column=0, sticky='w', padx=5, pady=10)



        lowerBox.pack(side=tk.TOP,padx=50,  pady = 10, fill=tk.BOTH)

        

        # print(yearList)
        # print(selectedYears)

        def grid_window():
            make_grid_window(yearList)

        gridBtn = tk.Button(lowerBox, text="Get Grid", command=grid_window)
        gridBtn.grid(row=4, column=0, sticky = 'w')


    checkFrame.pack(side = tk.LEFT, padx=10, pady=15, fill=tk.BOTH)
    # yearSelect = Label(yearFrame, text='Test')
    # # yearSelect.pack(side='left')
    # selectedYears = []
    confirmBtn = tk.Button(topFrame, text="Confirm Years", command=confirmValues)
    confirmBtn.pack(side = tk.LEFT)

    

    root.mainloop()

make_window()