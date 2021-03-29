from tkinter import *  # importing GUI stuff

root = Tk()
# title of the root window
root.title("Race Strategy by ADN Racing Team")
root.geometry('1000x700')  # size of the root window
root.iconbitmap("")  # Icon for the app


# avg laps calcs
lap_times = {}
total = 0
counter = 0
avg = 0
# Lap times window opener


def openLapTimesWindow():

    LapTimesWindow = Toplevel(root)
    LapTimesWindow.title("Lap Times")
    LapTimesWindow.geometry('850x450')

    # lap times window fields
    label_laps = Label(LapTimesWindow, text="Insert your Stint's Lap Times " + "\n" + "Format: MM:SS:sss").grid(
        row=0, column=1)
    
    def clear_button():
        for i in range(40):
            entry[i].delete(0, END)

    clear_button = Button(LapTimesWindow, text="Clear Laps", command=clear_button, padx=25, pady=5, fg="red", bg="white").grid(row=0, column= 4)

    label = ["label_lap1", "label_lap2", "label_lap3", "label_lap4", "label_lap5", "label_lap6", "label_lap7", "label_lap8", "label_lap9", "label_lap10", "label_lap11", "label_lap12", "label_lap13", "label_lap14", "label_lap15", "label_lap16", "label_lap17", "label_lap18", "label_lap19", "label_lap20",
             "label_lap21", "label_lap22", "label_lap23", "label_lap24", "label_lap25", "label_lap26", "label_lap27", "label_lap28", "label_lap29", "label_lap30", "label_lap31", "label_lap32", "label_lap33", "label_lap34", "label_lap35", "label_lap36", "label_lap37", "label_lap38", "label_lap39", "label_lap40"]
    entry = ["entry_lap1", "entry_lap2", "entry_lap3", "entry_lap4", "entry_lap5", "entry_lap6", "entry_lap7", "entry_lap8", "entry_lap9", "entry_lap10", "entry_lap11", "entry_lap12", "entry_lap13", "entry_lap14", "entry_lap15", "entry_lap16", "entry_lap17", "entry_lap18", "entry_lap19", "entry_lap20",
             "entry_lap21", "entry_lap22", "entry_lap23", "entry_lap24", "entry_lap25", "entry_lap26", "entry_lap27", "entry_lap28", "entry_lap29", "entry_lap30", "entry_lap31", "entry_lap32", "entry_lap33", "entry_lap34", "entry_lap35", "entry_lap36", "entry_lap37", "entry_lap38", "entry_lap39", "entry_lap40"]

    for x in range(40):
        def label_column_location(): 
            if x <= 9:
                return 0
            elif 10 <= x <= 19:
                return 3
            elif 20 <= x <= 29:
                return 6
            elif 30 <= x <= 39:
                return 9

        def entry_column_location():
            if x <= 9:
                return 1
            elif 10 <= x <= 19:
                return 4
            elif 20 <= x <= 29:
                return 7
            elif 30 <= x <= 39:
                return 10

        def row_location():
            if x <= 9:
                return x + 1
            elif 10 <= x <= 19:
                return abs(9 - x)
            elif 20 <= x <= 29:
                return abs(19 - x)
            elif 30 <= x <= 39:
                return abs(29 - x)

        label[x] = Label(LapTimesWindow, text="Lap " + str(1 + x) + ": ")
        label[x].grid(row=row_location(), column=label_column_location())
        entry[x] = Entry(LapTimesWindow, width=17, borderwidth=2)
        entry[x].grid(row=row_location(), column=entry_column_location(), columnspan=1, padx=5, pady=10)

    def submitLaps():
        global lap_times
        for i in range(40):
            lap_times["Lap " + str(i + 1)] = entry[i].get()
        #Get Seconds from lap times Dictionary
        # we now have the parsed lap time data in sec |  We now have to convert it back to MM:SS:sss
        global total
        global counter
        global avg
        for lap in lap_times:
            try: #avoid counting a dict without a value or with wrong value
                minutes, seconds, tenths = lap_times[lap].split(':')
                seconds = int(minutes) * 60 + int(seconds) + int(tenths) * 0.001
            except ValueError:
                #print("check lap times they should be in MM:SS:sss format!") #gotta add the lap no. here
                continue
            
            
            counter += 1
            total += seconds
            total_stint_sec = round(total, 3)

            avg = total / counter
            avg = round(avg, 3)
            print(total)
            #convert the avg sec back to a time format
            minutes = avg // 60 
            minutes_str = str(int(minutes))

            seconds = avg % 60
            seconds_str = str(int(seconds))

            millis = seconds % 1
            millis_str = str(round(millis, 3))
            whole, fractional = millis_str.split('.') # get sss part of the millis as a whole number
        
        total_label = Label(LapTimesWindow, text="Total Stint Time: " + "\n" + str(total_stint_sec) + " Seconds").grid(row=2, column=11)
        avg_label= Label(LapTimesWindow, text="Average Stint Lap Time: " + "\n"  + str(avg) + " Seconds", fg="blue").grid(row= 3, column=11)
        time_label = Label(LapTimesWindow, text="In Time Format: "+ "\n"+ minutes_str + ":" + seconds_str + ":" + fractional, fg="blue").grid(row=4, column=11)

        # refreshes for a new stint
        lap_times.clear() 
        total = 0
        counter = 0
        avg = 0


    button_submit = Button(LapTimesWindow, text="Submit Laps Times", command=submitLaps,
                               padx=20, pady=5, fg="black", bg="white").grid(row=1, column=11)



    LapTimesWindow.mainloop()


button_OpenWindow_LapTimes = Button(root, text="Insert Laptimes", command=openLapTimesWindow,
                                    padx=15, pady=10, fg="black", bg="white").grid(row=0, column=0)


root.mainloop()
