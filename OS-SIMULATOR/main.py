#importing modules
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import sys
import time
import datetime
import os
from copy import deepcopy

from PIL import Image, ImageTk

# end of module importing


# getting current directory of the app
try:
    currentDirectory = os.getcwd()
    ####print(currentDirectory)
except:
    pass
    print ( " Error : Cannot find the Current Directory. " )
# end of getting current directory



# creating the tkinter root that will accommodate the UI
root = Tk()
root.title ( "OS Simulation" )
# The Graphical User Interface's activation.
root.resizable( width = FALSE , height = FALSE )
root.geometry( "900x600" )
root.config ( background = "LIGHTBLUE" )
#

# Backgrounds
mainMenu_bg = PhotoImage(file = currentDirectory + "\\resources\\background\\mainMenu.png" )
pa_bg = PhotoImage(file = currentDirectory + "\\resources\\background\\partitionedAllocation.png" )
pm_bg = PhotoImage(file = currentDirectory + "\\resources\\background\\processManagement.png" )
aboutUs_bg = PhotoImage(file = currentDirectory + "\\resources\\background\\aboutUs.png" )

sc_bg = PhotoImage(file = currentDirectory + "\\resources\\background\\singleContiguous.png" )
spa_bg = PhotoImage(file = currentDirectory + "\\resources\\background\\staticPartitionedAllocation.png" )
dff_bg = PhotoImage(file = currentDirectory + "\\resources\\background\\dynamicFirstFit.png" )
dbf_bg = PhotoImage(file = currentDirectory + "\\resources\\background\\dynamicBestFit.png" )
fcfs_bg = PhotoImage(file = currentDirectory + "\\resources\\background\\firstComeFirstServe.png" )
sjf_bg = PhotoImage(file = currentDirectory + "\\resources\\background\\shortestJobFirst.png" )
srtf_bg = PhotoImage(file = currentDirectory + "\\resources\\background\\shortestRemainingTimeFirst.png" )
rr_bg = PhotoImage(file = currentDirectory + "\\resources\\background\\roundRobin.png" )
p_bg = PhotoImage(file = currentDirectory + "\\resources\\background\\priorityScheduling.png" )

# Buttons
aboutUs_btn = PhotoImage(file = currentDirectory + "\\resources\\buttons\\aboutUs.png" )
mainMenu_btn = PhotoImage(file = currentDirectory + "\\resources\\buttons\\mainMenu.png" )


class main:
    def __init__( self ):
        pass

    # The program has two list which contains a reference to all the program's widgets
    # And what this function does is it tries to clear/destroy all of these widgets
    # using the lists which contains the program's widgets.
    # The two lists are:
    #   - self.basicWidgetList: For most of the basic widgets
    #   - self.physicalMemWidgets: For the widgets used to display physical memory map
    def clearWidgets( self ):
        try:
            self.tick_on = False
            self.clearWidgetList( self.basicWidgetList )
            self.clearWidgetList( self.physicalMemWidgets )
        except:
            pass
        return


    # This function destroys all of the widgets inside the inputted widgetsToClear list.
    def clearWidgetList ( self, widgetsToClear):
        for widget in widgetsToClear:
            widget.destroy()


    # For getting the current date
    def current_date( self ):
        self.dateString  =  datetime.date.today().strftime("%B %d, %Y")
        self.dateLBL.config(text = self.dateString)


    # This updates the clock widget
    def tick( self ):
        if self.tick_on:
            self.timeString  =  time.strftime("%H:%M:%S")
            self.clockLBL.config(text = self.timeString)
            self.clockLBL.after(200, self.tick )
        else:
            pass
            
    def mainMenu_window( self ):
        root.title ( "OS Simulation: Main Menu" )
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.mainMenuBG = Label ( root , image = mainMenu_bg, bg = "black" )
        self.mainMenuBG.place(x = 0, y = 0)
        self.basicWidgetList.append( self.mainMenuBG )

        self.aboutBTN  =  Button ( root , image = aboutUs_btn, command = self.aboutUs_window, bg = "#f4e033" )
        self.aboutBTN.place (x = 840 ,y = 20)
        self.basicWidgetList.append( self.aboutBTN )

        self.dateLBL  =  Label( root , font = ('Cooper Black', 14),  bg = "#99d9ea")
        self.dateLBL.place(x = 313, y = 350)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )

        self.clockLBL  =  Label( root , font = ('Cooper Black', 14),  bg = "#99d9ea" )
        self.clockLBL.place(x = 513, y = 350)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.scmmBTN  =  Button ( root , text = 'Single Contiguous',command = self.scmmBTN_Pressed , font = ('Papyrus', 13, 'bold'), width  =  20, bg = "#659bdb" )
        self.scmmBTN.place (x = 330 ,y = 450)
        self.basicWidgetList.append( self.scmmBTN )

        self.paBTN  =  Button ( root , text = 'Partitioned Allocation',command = self.partitionedAllocation_window , font = ('Papyrus', 13, 'bold'), width  =  20, bg = "#659bdb" )
        self.paBTN.place (x = 60 ,y = 450)
        self.basicWidgetList.append( self.paBTN )

        self.pmBTN  =  Button ( root , text = 'Process Management',command = self.processManagement_window , font = ('Papyrus', 13, 'bold'), width  =  20, bg = "#659bdb" )
        self.pmBTN.place (x = 600 ,y = 450)
        self.basicWidgetList.append( self.pmBTN )

        
    def scmmBTN_Pressed( self ):
        scmm_program.input1_window()

    def partitionedAllocation_window( self ):
        root.title ( "OS Simulation: Partitioned Allocation" )
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.paBG = Label ( root , image = pa_bg, bg = "black" )
        self.paBG.place(x = 0, y = 0)
        self.basicWidgetList.append( self.paBG )

        self.aboutBTN  =  Button ( root , image = aboutUs_btn, command = self.aboutUs_window, bg = "#f4e033" )
        self.aboutBTN.place (x = 840 ,y = 20)
        self.basicWidgetList.append( self.aboutBTN )

        self.dateLBL  =  Label( root , font = ('Cooper Black', 14),  bg = "#99d9ea")
        self.dateLBL.place(x = 313, y = 350)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )

        self.clockLBL  =  Label( root , font = ('Cooper Black', 14),  bg = "#99d9ea" )
        self.clockLBL.place(x = 513, y = 350)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.mainMenuBTN  =  Button ( root , text = 'Main Menu',command = self.mainMenu_window , font = ('Papyrus', 10, 'bold'), width  =  10, bg = "#659bdb" )
        self.mainMenuBTN.place (x = 405 ,y = 380)
        self.basicWidgetList.append( self.mainMenuBTN )

        self.sffBTN  =  Button ( root , text = 'Static First Fit',command = self.sffBTN_Pressed , font = ('Papyrus', 13, 'bold'), width  =  20, bg = "#659bdb" )
        self.sffBTN.place (x = 60 ,y = 450)
        self.basicWidgetList.append( self.sffBTN )

        self.dffBTN  =  Button ( root , text = 'Dynamic First Fit',command = self.dffBTN_Pressed , font = ('Papyrus', 13, 'bold'), width  =  20, bg = "#659bdb" )
        self.dffBTN.place (x = 330 ,y = 450)
        self.basicWidgetList.append( self.dffBTN )

        self.dbfBTN  =  Button ( root , text = 'Dynamic Best Fit',command = self.dbfBTN_Pressed , font = ('Papyrus', 13, 'bold'), width  =  20, bg = "#659bdb" )
        self.dbfBTN.place (x = 600 ,y = 450)
        self.basicWidgetList.append( self.dbfBTN )


    def sffBTN_Pressed( self ):
        spa_program.mainInput1_window()

    def dffBTN_Pressed( self ):
        dff_program.input1_window()

    def dbfBTN_Pressed( self ):
        dbf_program.input1_window()

        
    def processManagement_window( self ):
        root.title ( "OS Simulation: Process Management" )
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.pmBG = Label ( root , image = pm_bg, bg = "black" )
        self.pmBG.place(x = 0, y = 0)
        self.basicWidgetList.append( self.pmBG )

        self.aboutBTN  =  Button ( root , image = aboutUs_btn, command = self.aboutUs_window, bg = "#f4e033" )
        self.aboutBTN.place (x = 840 ,y = 20)
        self.basicWidgetList.append( self.aboutBTN )

        self.dateLBL  =  Label( root , font = ('Cooper Black', 14),  bg = "#99d9ea")
        self.dateLBL.place(x = 313, y = 350)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )

        self.clockLBL  =  Label( root , font = ('Cooper Black', 14),  bg = "#99d9ea" )
        self.clockLBL.place(x = 513, y = 350)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.mainMenuBTN  =  Button ( root , text = 'Main Menu',command = self.mainMenu_window , font = ('Papyrus', 10, 'bold'), width  =  10, bg = "#659bdb" )
        self.mainMenuBTN.place (x = 405 ,y = 380)
        self.basicWidgetList.append( self.mainMenuBTN )

        self.roundRobinBTN  =  Button ( root , text = 'Round Robin',command = self.roundRobinBTN_Pressed , font = ('Papyrus', 13, 'bold'), width  =  20, bg = "#659bdb" )
        self.roundRobinBTN.place (x = 200 ,y = 425)
        self.basicWidgetList.append( self.roundRobinBTN )

        self.prioritySchedulingBTN  =  Button ( root , text = 'Priority Scheduling',command = self.prioritySchedulingBTN_Pressed , font = ('Papyrus', 13, 'bold'), width  =  20, bg = "#659bdb" )
        self.prioritySchedulingBTN.place (x = 470 ,y = 425)
        self.basicWidgetList.append( self.prioritySchedulingBTN )

        self.fcfsBTN  =  Button ( root , text = 'First Come First Serve',command = self.fcfsBTN_Pressed , font = ('Papyrus', 13, 'bold'), width  =  20, bg = "#659bdb" )
        self.fcfsBTN.place (x = 60 ,y = 485)
        self.basicWidgetList.append( self.fcfsBTN )

        self.sjfBTN  =  Button ( root , text = 'Shortest Job First',command = self.sjfBTN_Pressed , font = ('Papyrus', 13, 'bold'), width  =  20, bg = "#659bdb" )
        self.sjfBTN.place (x = 330 ,y = 485)
        self.basicWidgetList.append( self.sjfBTN )

        self.srtfBTN  =  Button ( root , text = 'Shortest Remaining Time',command = self.srtfBTN_Pressed , font = ('Papyrus', 13, 'bold'), width  =  20, bg = "#659bdb" )
        self.srtfBTN.place (x = 600 ,y = 485)
        self.basicWidgetList.append( self.srtfBTN )

    def roundRobinBTN_Pressed( self ):
        rr_program.input1_window()

    def prioritySchedulingBTN_Pressed( self ):
        p_program.input1_window()

    def fcfsBTN_Pressed( self ):
        fcfs_program.input1_window()

    def sjfBTN_Pressed( self ):
        sjf_program.input1_window()

    def srtfBTN_Pressed( self ):
        srtf_program.input1_window()
    

    def aboutUs_window( self ):
        root.title ( "OS Simulation: About Us" )
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.aboutUsBG = Label ( root , image = aboutUs_bg, bg = "black" )
        self.aboutUsBG.place(x = 0, y = 0)
        self.basicWidgetList.append( self.aboutUsBG )

        self.mainMenuBTN  =  Button ( root , text = 'Main Menu',command = self.mainMenu_window , font = ('Papyrus', 10, 'bold'), width  =  10, bg = "#659bdb" )
        self.mainMenuBTN.place (x = 30 ,y = 40)
        self.basicWidgetList.append( self.mainMenuBTN )

        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Papyrus', 10, 'bold'), width  =  10, bg = "#659bdb" )
        self.exitBTN.place (x = 760 ,y = 40)
        self.basicWidgetList.append( self.exitBTN )



# SCMM PROGRAM: Line 227-1337

# SCMM_program class which contains most of all the program's code.
# This contains all the window functions and miscellaneous functions
# To know each function's description, look at the documentation at the first line. ( *Ctrl + h* line 27 and 37 )
class singleContiguousProgram:
    def __init__ ( self ):
        pass

    
    # For getting the current date
    def current_date( self ):
        self.dateString  =  datetime.date.today().strftime("%B %d, %Y")
        self.dateLBL.config(text = self.dateString)

    
    # This updates the clock widget
    def tick( self ):
        if self.tick_on:
            self.timeString  =  time.strftime("%H:%M:%S")
            self.clockLBL.config(text = self.timeString)
            self.clockLBL.after(200, self.tick )
        else:
            pass


    # This function returns True if timeInput is not in proper time format
    # Else, returns False if the input is in proper time format
    # Time format is HH:MM
    def isNotTimeFormat( self, timeInput):
        try:
            time.strptime( timeInput, '%H:%M')
            return False
        except ValueError:
            return True

    # This function returns True if the integerInput is not an Integer.
    # If it is an integer, return False.
    def isNotInteger( self, integerInput):
        try:
            self.intTest = int(integerInput)
            return False
        except ValueError:
            return True

    # The program has two list which contains a reference to all the program's widgets
    # And what this function does is it tries to clear/destroy all of these widgets
    # using the lists which contains the program's widgets.
    # The two lists are:
    #   - self.basicWidgetList: For most of the basic widgets
    #   - self.physicalMemWidgets: For the widgets used to display physical memory map
    def clearWidgets( self ):
        try:
            self.tick_on = False
            self.clearWidgetList( self.basicWidgetList )
            self.clearWidgetList( self.physicalMemWidgets )
        except:
            pass
        return


    # This function destroys all of the widgets inside the inputted widgetsToClear list.
    def clearWidgetList ( self, widgetsToClear):
        for widget in widgetsToClear:
            widget.destroy()

    # This function displays the necessary widgets for physical memory map.
    # To get a general gist, the program has around 50 labels which acts as the physical memory map.
    # In addition, it has a text label which marks each section of the physical memory map.
    def displayMap( self, tempPointer, tempColor, tempText, tempPercentage, tempTotalSize ):
        self.tempPointer = int(tempPointer)
        self.tempColor = tempColor
        self.tempText = tempText
        self.tempPercentage = tempPercentage
        self.tempTotalSize = tempTotalSize
        
        if self.tempPercentage != 0:
            self.tempLBL = Label( root , text = "          " * 25 , font = ('Times New Roman', 1),  bg = self.tempColor)
            self.tempLBL.place(x = 80, y = self.yCounter)
            self.yCounter += 7
            self.physicalMemWidgets.append( self.tempLBL )
            
            self.tempLBL = Label( root , text = self.tempText , font = ('Times New Roman', 10),  bg = self.tempColor)
            self.tempLBL.place(x = 350, y = self.yCounter)
            self.physicalMemWidgets.append( self.tempLBL )
        for i in range( int( self.tempPercentage / 2 ) ):
            if self.tempPointer != 0:
                self.tempLBL = Label( root , text = "          " * 25 , font = ('Times New Roman', 1),  bg = self.tempColor)
                self.tempLBL.place(x = 80, y = self.yCounter)
                self.yCounter += 7
                self.physicalMemWidgets.append( self.tempLBL )
                self.tempPointer -= 1
            else:
                pass
        if self.tempPercentage != 0:
            self.tempLBL  =  Label( root , text = tempTotalSize , font = ('Times New Roman', 10),  bg = self.tempColor)
            self.tempLBL.place(x = 50, y = self.yCounter - 15)
            self.physicalMemWidgets.append( self.tempLBL )
        return


    # This functions has all the necessary computations for the computation result.
    def mainInput1_computeBTN_Pressed ( self ):
        if messagebox.askyesno( "Confirmation..." , " Are you sure you want to compute? " ) == True :
            self.size1 = self.size1ENTRY.get()
            self.size2 = self.size2ENTRY.get()
            self.size3 = self.size3ENTRY.get()
            self.size4 = self.size4ENTRY.get()
            self.size5 = self.size5ENTRY.get()

            self.memSize = self.memSizeENTRY.get()
            self.osSize = self.osSizeENTRY.get()

            self.memSize_Check = self.isNotInteger( self.memSize )
            self.osSize_Check = self.isNotInteger( self.osSize )
 
            self.size1_Check = self.isNotInteger( self.size1 )
            #print ( self.size1_Check )
            self.size2_Check = self.isNotInteger( self.size2 )
            self.size3_Check = self.isNotInteger( self.size3 )
            self.size4_Check = self.isNotInteger( self.size4 )
            self.size5_Check = self.isNotInteger( self.size5 )
            
            
            self.arrivalTime1 = self.arrivalTime1ENTRY.get()
            self.arrivalTime2 = self.arrivalTime2ENTRY.get()
            self.arrivalTime3 = self.arrivalTime3ENTRY.get()
            self.arrivalTime4 = self.arrivalTime4ENTRY.get()
            self.arrivalTime5 = self.arrivalTime5ENTRY.get()

            self.arrivalTime1_Check = self.isNotTimeFormat( self.arrivalTime1 )
            self.arrivalTime2_Check = self.isNotTimeFormat( self.arrivalTime2 )
            self.arrivalTime3_Check = self.isNotTimeFormat( self.arrivalTime3 )
            self.arrivalTime4_Check = self.isNotTimeFormat( self.arrivalTime4 )
            self.arrivalTime5_Check = self.isNotTimeFormat( self.arrivalTime5 )

            self.runTime1 = self.runTime1ENTRY.get()
            self.runTime2 = self.runTime2ENTRY.get()
            self.runTime3 = self.runTime3ENTRY.get()
            self.runTime4 = self.runTime4ENTRY.get()
            self.runTime5 = self.runTime5ENTRY.get()
        
            self.runTime1_Check = self.isNotTimeFormat( self.runTime1 )
            self.runTime2_Check = self.isNotTimeFormat( self.runTime2 )
            self.runTime3_Check = self.isNotTimeFormat( self.runTime3 )
            self.runTime4_Check = self.isNotTimeFormat( self.runTime4 )
            self.runTime5_Check = self.isNotTimeFormat( self.runTime5 )

            if self.memSize_Check or self.osSize_Check :
                #print ( "Error: Invalid Memory or OS Size input." )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Memory or OS Size input." )
            elif int(self.memSize) < int(self.osSize):
                ##print ( "ting" )
                #print ( " Error: Os Size can't exceed Memory Size. " )
                messagebox.showinfo( "Compute Error" , "Error: Os Size can't exceed Memory Size." )
            elif self.size1_Check or self.size2_Check or self.size3_Check or self.size4_Check or self.size5_Check:
                #print ( "Error: Size input detected as not an integer." )
                messagebox.showinfo( "Compute Error" , "Error: Size input detected as not an integer." )
            elif (int(self.size1) > ( int(self.memSize) - int(self.osSize))) or (int(self.size2) > ( int(self.memSize) - int(self.osSize))) or (int(self.size3) > ( int(self.memSize) - int(self.osSize))) or (int(self.size4) > ( int(self.memSize) - int(self.osSize))) or (int(self.size5) > ( int(self.memSize) - int(self.osSize))):
                #print ( "Error: Size input should not exceed ( Memory Size - OS Size )." )
                messagebox.showinfo( "Compute Error" , "Error: Size input should not exceed ( Memory Size - OS Size )." )
            elif self.arrivalTime1_Check or self.arrivalTime2_Check or self.arrivalTime3_Check or self.arrivalTime4_Check or self.arrivalTime5_Check:
                #print ( " Error in arrival time input " )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Arrival Time Input." )
            elif self.runTime1_Check or self.runTime2_Check or self.runTime3_Check or self.runTime4_Check or self.runTime5_Check:
                #print ( "Error: Invalid Run Time Input." )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Run Time Input." )
            else:
                self.osPercentage = float(( int(self.osSize) / int(self.memSize) ) * 100 )
                self.job1Percentage = float(( int(self.size1) / int(self.memSize) ) * 100 )
                self.wasted1 = float(self.memSize) - (int(self.osSize) + int(self.size1))
                self.wasted1Percentage = int(( int(self.wasted1) / int(self.memSize) ) * 100 )
                #self.physicalMemInfo1 = [ [ self.osPercentage, "#f2f5f4", "OS Size", "" ], [ (self.osPercentage + self.job1Percentage), "#c2c4c3", "Job 1 Size", self.osSize], [ 0, "#979998", "Wasted", (int(self.osSize) + int(self.size1))]]

                self.job2Percentage = float(( int(self.size2) / int(self.memSize) ) * 100 )
                self.wasted2 = float(self.memSize) - (int(self.osSize) + int(self.size2))
                self.wasted2Percentage = float(( int(self.wasted2) / int(self.memSize) ) * 100 )
                #self.physicalMemInfo2 = [ [ self.osPercentage, "#f2f5f4", "OS Size", "" ], [ (self.osPercentage + self.job2Percentage), "#c2c4c3", "Job 2 Size", self.osSize], [ 0, "#979998", "Wasted", (int(self.osSize) + int(self.size2))]]
                
                self.job3Percentage = float(( int(self.size3) / int(self.memSize) ) * 100 )
                self.wasted3 = float(self.memSize) - (int(self.osSize) + int(self.size3))
                self.wasted3Percentage = float(( int(self.wasted3) / int(self.memSize) ) * 100 )
                #self.physicalMemInfo3 = [ [ self.osPercentage, "#f2f5f4", "OS Size", "" ], [ (self.osPercentage + self.job3Percentage), "#c2c4c3", "Job 3 Size", self.osSize], [ 0, "#979998", "Wasted", (int(self.osSize) + int(self.size3))]]

                self.job4Percentage = float(( int(self.size4) / int(self.memSize) ) * 100 )
                self.wasted4 = float(self.memSize) - (int(self.osSize) + int(self.size4))
                self.wasted4Percentage = float(( int(self.wasted4) / int(self.memSize) ) * 100 )
                #self.physicalMemInfo4 = [ [ self.osPercentage, "#f2f5f4", "OS Size", "" ], [ (self.osPercentage + self.job4Percentage), "#c2c4c3", "Job 4 Size", self.osSize], [ 0, "#979998", "Wasted", (int(self.osSize) + int(self.size4))]]

                self.job5Percentage = float(( int(self.size5) / int(self.memSize) ) * 100 )
                self.wasted5 = float(self.memSize) - (int(self.osSize) + int(self.size5))
                self.wasted5Percentage = float(( int(self.wasted5) / int(self.memSize) ) * 100 )
                #self.physicalMemInfo5 = [ [ self.osPercentage, "#f2f5f4", "OS Size", "" ], [ (self.osPercentage + self.job5Percentage), "#c2c4c3", "Job 5 Size", self.osSize], [ 0, "#979998", "Wasted", (int(self.osSize) + int(self.size5))]]
                
                self.time_zero = datetime.datetime.strptime('00:00', '%H:%M')
                
                self.startTime1 = datetime.datetime.strptime( self.arrivalTime1, '%H:%M')
                if (self.startTime1 - datetime.datetime.strptime( self.arrivalTime1, '%H:%M')).total_seconds() < 0:
                    self.cpuWait1 = "0:00:00"
                    self.startTime1 = datetime.datetime.strptime( self.arrivalTime1, '%H:%M')
                else:
                    self.cpuWait1 = self.startTime1 - datetime.datetime.strptime( self.arrivalTime1, '%H:%M')

                self.finishTime1 = ( self.startTime1 - self.time_zero + (datetime.datetime.strptime(self.runTime1, '%H:%M')))
                self.startTime2 = self.finishTime1

                if (self.startTime2 - datetime.datetime.strptime( self.arrivalTime2, '%H:%M')).total_seconds() < 0:
                    self.cpuWait2 = "0:00:00"
                    self.startTime2 = datetime.datetime.strptime( self.arrivalTime2, '%H:%M')
                else:
                    self.cpuWait2 = self.startTime2 - datetime.datetime.strptime( self.arrivalTime2, '%H:%M')

                self.finishTime2 = ( self.startTime2 - self.time_zero + (datetime.datetime.strptime(self.runTime2, '%H:%M')))
                self.startTime3 = self.finishTime2

                if (self.startTime3 - datetime.datetime.strptime( self.arrivalTime3, '%H:%M')).total_seconds() < 0:
                    self.cpuWait3 = "0:00:00"
                    self.startTime3 = datetime.datetime.strptime( self.arrivalTime3, '%H:%M')
                else:
                    self.cpuWait3 = self.startTime3 - datetime.datetime.strptime( self.arrivalTime3, '%H:%M')

                self.finishTime3 = ( self.startTime3 - self.time_zero + (datetime.datetime.strptime(self.runTime3, '%H:%M')))
                self.startTime4 = self.finishTime3

                if (self.startTime4 - datetime.datetime.strptime( self.arrivalTime4, '%H:%M')).total_seconds() < 0:
                    self.startTime4 = datetime.datetime.strptime( self.arrivalTime4, '%H:%M')
                    self.cpuWait4 = "0:00:00"
                else:
                    self.cpuWait4 = self.startTime4 - datetime.datetime.strptime( self.arrivalTime4, '%H:%M')

                self.finishTime4 = ( self.startTime4 - self.time_zero + (datetime.datetime.strptime(self.runTime4, '%H:%M')))
                self.startTime5 = self.finishTime4

                if (self.startTime5 - datetime.datetime.strptime( self.arrivalTime5, '%H:%M')).total_seconds() < 0:
                    self.startTime5 = datetime.datetime.strptime( self.arrivalTime5, '%H:%M')
                    self.cpuWait5 = "0:00:00"
                else:
                    self.cpuWait5 = self.startTime5 - datetime.datetime.strptime( self.arrivalTime5, '%H:%M')

                self.finishTime5 = ( self.startTime5 - self.time_zero + (datetime.datetime.strptime(self.runTime5, '%H:%M')))
                
                #print( self.cpuWait3, self.startTime3, datetime.datetime.strptime( self.arrivalTime3, '%H:%M'))
                #print( self.cpuWait4, self.startTime4, datetime.datetime.strptime( self.arrivalTime4, '%H:%M'))
                #print( self.cpuWait5, self.startTime4, datetime.datetime.strptime( self.arrivalTime5, '%H:%M'))
                #print ( " Success " )
                self.result1_window()


    def mainMenuBTN_Pressed( self ):
        main.mainMenu_window()

    def aboutUsBTN_Pressed( self ):
        main.aboutUs_window()
   

    # From here, and down to the last function are the windows/pages of the GUI.
    def input1_window ( self ):
        root.title ( "Single Contiguous Memory Management" )
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.singleContgiousBG = Label ( root , image = sc_bg, bg = "black" )
        self.singleContgiousBG.place(x = 0, y = 0)
        self.basicWidgetList.append( self.singleContgiousBG )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#fff0c3" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#fff0c3")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )

        self.mainMenuBTN  =  Button ( root , image = mainMenu_btn, command = self.mainMenuBTN_Pressed , bg = "#fff0c3" )
        self.mainMenuBTN.place (x = 850 ,y = 60)
        self.basicWidgetList.append( self.mainMenuBTN )

        self.aboutBTN  =  Button ( root , image = aboutUs_btn, command = self.aboutUsBTN_Pressed, bg = "#fff0c3" )
        self.aboutBTN.place (x = 850 ,y = 10)
        self.basicWidgetList.append( self.aboutBTN )
        
        
        self.title1LBL  =  Label( root , text = "Single Contiguous" , font = ('Times New Roman', 20),  bg = "#fff0c3")
        self.title1LBL.place(x = 100, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Memory Management" , font = ('Times New Roman', 20),  bg = "#fff0c3")
        self.title2LBL.place(x = 75, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.jobLBL  =  Label( root , text = "Job" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.jobLBL.place(x = 125, y = 130)
        self.basicWidgetList.append( self.jobLBL )

        self.job1LBL  =  Label( root , text = "1" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job1LBL.place(x = 135, y = 190)
        self.basicWidgetList.append( self.job1LBL )
        
        self.job2LBL  =  Label( root , text = "2" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job2LBL.place(x = 135, y = 250)
        self.basicWidgetList.append( self.job2LBL )
        
        self.job3LBL  =  Label( root , text = "3" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job3LBL.place(x = 135, y = 310)
        self.basicWidgetList.append( self.job3LBL )
        
        self.job4LBL  =  Label( root , text = "4" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job4LBL.place(x = 135, y = 370)
        self.basicWidgetList.append( self.job4LBL )
        
        self.job5LBL  =  Label( root , text = "5" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job5LBL.place(x = 135, y = 430)
        self.basicWidgetList.append( self.job5LBL )
        
        self.sizeLBL  =  Label( root , text = "Size" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.sizeLBL.place(x = 275, y = 130)
        self.basicWidgetList.append( self.sizeLBL )
        
        self.size1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size1ENTRY.place(x = 225, y = 190)
        self.basicWidgetList.append( self.size1ENTRY )
        
        self.size2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size2ENTRY.place(x = 225, y = 250)
        self.basicWidgetList.append( self.size2ENTRY )
        
        self.size3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size3ENTRY.place(x = 225, y = 310)
        self.basicWidgetList.append( self.size3ENTRY )
        
        self.size4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size4ENTRY.place(x = 225, y = 370)
        self.basicWidgetList.append( self.size4ENTRY )
        
        self.size5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size5ENTRY.place(x = 225, y = 430)
        self.basicWidgetList.append( self.size5ENTRY )
        
        self.arrivalTimeLBL  =  Label( root , text = "Arrival Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.arrivalTimeLBL.place(x = 505, y = 130)
        self.basicWidgetList.append( self.arrivalTimeLBL )

        self.arrivalTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime1ENTRY.place(x = 490, y = 190)
        self.basicWidgetList.append( self.arrivalTime1ENTRY )
        
        self.arrivalTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime2ENTRY.place(x = 490, y = 250)
        self.basicWidgetList.append( self.arrivalTime2ENTRY )
        
        self.arrivalTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime3ENTRY.place(x = 490, y = 310)
        self.basicWidgetList.append( self.arrivalTime3ENTRY )
        
        self.arrivalTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime4ENTRY.place(x = 490, y = 370)
        self.basicWidgetList.append( self.arrivalTime4ENTRY )
        
        self.arrivalTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime5ENTRY.place(x = 490, y = 430)
        self.basicWidgetList.append( self.arrivalTime5ENTRY )
        
        self.runTimeLBL  =  Label( root , text = "Run Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.runTimeLBL.place(x = 725, y = 130)
        self.basicWidgetList.append( self.runTimeLBL )
        
        self.runTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.runTime1ENTRY.place(x = 700, y = 190)
        self.basicWidgetList.append( self.runTime1ENTRY )
        
        self.runTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.runTime2ENTRY.place(x = 700, y = 250)
        self.basicWidgetList.append( self.runTime2ENTRY )
        
        self.runTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.runTime3ENTRY.place(x = 700, y = 310)
        self.basicWidgetList.append( self.runTime3ENTRY )
        
        self.runTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.runTime4ENTRY.place(x = 700, y = 370)
        self.basicWidgetList.append( self.runTime4ENTRY )
        
        self.runTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.runTime5ENTRY.place(x = 700, y = 430)
        self.basicWidgetList.append( self.runTime5ENTRY )

        self.memSizeLBL  =  Label( root , text = "Memory Size" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.memSizeLBL.place(x = 150, y = 500)
        self.basicWidgetList.append( self.memSizeLBL )
        
        self.memSizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.memSizeENTRY.place(x = 130, y = 550 )
        self.basicWidgetList.append( self.memSizeENTRY )

        self.osSizeLBL  =  Label( root , text = "OS Size" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.osSizeLBL.place(x = 660, y = 500)
        self.basicWidgetList.append( self.osSizeLBL )
        
        self.osSizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.osSizeENTRY.place(x = 625, y = 550 )
        self.basicWidgetList.append( self.osSizeENTRY )
        
        self.computeBTN  =  Button ( root , text = 'Compute',command = self.mainInput1_computeBTN_Pressed , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.computeBTN.place (x = 390 ,y = 500)
        self.basicWidgetList.append( self.computeBTN )

        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 550)
        self.basicWidgetList.append( self.exitBTN )

        
    def result1_window ( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.singleContgiousBG = Label ( root , image = sc_bg, bg = "black" )
        self.singleContgiousBG.place(x = 0, y = 0)
        self.basicWidgetList.append( self.singleContgiousBG )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#fff0c3" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#fff0c3")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )

        self.title1LBL  =  Label( root , text = "Single Contiguous" , font = ('Times New Roman', 20),  bg = "#fff0c3")
        self.title1LBL.place(x = 100, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Memory Management Result" , font = ('Times New Roman', 20),  bg = "#fff0c3")
        self.title2LBL.place(x = 40, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.jobLBL  =  Label( root , text = "Job" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.jobLBL.place(x = 125, y = 130)
        self.basicWidgetList.append( self.jobLBL )

        self.job1LBL  =  Label( root , text = "1" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job1LBL.place(x = 135, y = 190)
        self.basicWidgetList.append( self.job1LBL )
        
        self.job2LBL  =  Label( root , text = "2" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job2LBL.place(x = 135, y = 250)
        self.basicWidgetList.append( self.job2LBL )
        
        self.job3LBL  =  Label( root , text = "3" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job3LBL.place(x = 135, y = 310)
        self.basicWidgetList.append( self.job3LBL )
        
        self.job4LBL  =  Label( root , text = "4" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job4LBL.place(x = 135, y = 370)
        self.basicWidgetList.append( self.job4LBL )
        
        self.job5LBL  =  Label( root , text = "5" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job5LBL.place(x = 135, y = 430)
        self.basicWidgetList.append( self.job5LBL )

        self.startTimeLBL  =  Label( root , text = "Start Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.startTimeLBL.place(x = 250, y = 130)
        self.basicWidgetList.append( self.startTimeLBL )
        
        self.startTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.startTime1ENTRY.place(x = 225, y = 190)
        self.startTime1ENTRY.insert( 0, self.startTime1.time() )
        self.startTime1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.startTime1ENTRY )
        
        self.startTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.startTime2ENTRY.place(x = 225, y = 250)
        self.startTime2ENTRY.insert( 0, self.startTime2.time() )
        self.startTime2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.startTime2ENTRY )
        
        self.startTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.startTime3ENTRY.place(x = 225, y = 310)
        self.startTime3ENTRY.insert( 0, self.startTime3.time() )
        self.startTime3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.startTime3ENTRY )
        
        self.startTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.startTime4ENTRY.place(x = 225, y = 370)
        self.startTime4ENTRY.insert( 0, self.startTime4.time() )
        self.startTime4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.startTime4ENTRY )
        
        self.startTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.startTime5ENTRY.place(x = 225, y = 430)
        self.startTime5ENTRY.insert( 0, self.startTime5.time() )
        self.startTime5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.startTime5ENTRY )

        self.finishTimeLBL  =  Label( root , text = "Finish Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.finishTimeLBL.place(x = 510, y = 130)
        self.basicWidgetList.append( self.finishTimeLBL )

        self.finishTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.finishTime1ENTRY.place(x = 490, y = 190)
        self.finishTime1ENTRY.insert( 0, self.finishTime1.time() )
        self.finishTime1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.finishTime1ENTRY )
        
        self.finishTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.finishTime2ENTRY.place(x = 490, y = 250)
        self.finishTime2ENTRY.insert( 0, self.finishTime2.time() )
        self.finishTime2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.finishTime2ENTRY )
        
        self.finishTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.finishTime3ENTRY.place(x = 490, y = 310)
        self.finishTime3ENTRY.insert( 0, self.finishTime3.time() )
        self.finishTime3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.finishTime3ENTRY )
        
        self.finishTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.finishTime4ENTRY.place(x = 490, y = 370)
        self.finishTime4ENTRY.insert( 0, self.finishTime4.time() )
        self.finishTime4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.finishTime4ENTRY )
        
        self.finishTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.finishTime5ENTRY.place(x = 490, y = 430)
        self.finishTime5ENTRY.insert( 0, self.finishTime5.time() )
        self.finishTime5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.finishTime5ENTRY )

        self.cpuWaitLBL  =  Label( root , text = "CPU Wait" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.cpuWaitLBL.place(x = 725, y = 130)
        self.basicWidgetList.append( self.cpuWaitLBL )
        
        self.cpuWait1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuWait1ENTRY.place(x = 700, y = 190)
        self.cpuWait1ENTRY.insert( 0, self.cpuWait1 )
        self.cpuWait1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.cpuWait1ENTRY )
        
        self.cpuWait2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuWait2ENTRY.place(x = 700, y = 250)
        self.cpuWait2ENTRY.insert( 0, self.cpuWait2 )
        self.cpuWait2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.cpuWait2ENTRY )
        
        self.cpuWait3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuWait3ENTRY.place(x = 700, y = 310)
        self.cpuWait3ENTRY.insert( 0, self.cpuWait3 )
        self.cpuWait3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.cpuWait3ENTRY )
        
        self.cpuWait4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuWait4ENTRY.place(x = 700, y = 370)
        self.cpuWait4ENTRY.insert( 0, self.cpuWait4 )
        self.cpuWait4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.cpuWait4ENTRY )
        
        self.cpuWait5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuWait5ENTRY.place(x = 700, y = 430)
        self.cpuWait5ENTRY.insert( 0, self.cpuWait5 )
        self.cpuWait5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.cpuWait5ENTRY )

        self.backBTN  =  Button ( root , text = 'BACK',command = self.input1_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 300 ,y = 500)
        self.basicWidgetList.append( self.backBTN )
        
        self.nextBTN  =  Button ( root , text = 'NEXT',command = self.result2_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.nextBTN.place (x = 480 ,y = 500)
        self.basicWidgetList.append( self.nextBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 550)
        self.basicWidgetList.append( self.exitBTN )


    def result2_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.singleContgiousBG = Label ( root , image = sc_bg, bg = "black" )
        self.singleContgiousBG.place(x = 0, y = 0)
        self.basicWidgetList.append( self.singleContgiousBG )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#fff0c3" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#fff0c3")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )

        self.title1LBL  =  Label( root , text = "Single Contiguous" , font = ('Times New Roman', 20),  bg = "#fff0c3")
        self.title1LBL.place(x = 100, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Memory Management Result" , font = ('Times New Roman', 20),  bg = "#fff0c3")
        self.title2LBL.place(x = 40, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Physical Memory Map" , font = ('Times New Roman', 20),  bg = "#c6e3ad")
        self.title3LBL.place(x = 540, y = 135)
        self.basicWidgetList.append( self.title3LBL )
        self.title3LBL  =  Label( root , text = "At {}, Job 1 Started".format(str(self.startTime1.time())) , font = ('Times New Roman', 12),  bg = "#c6e3ad")
        self.title3LBL.place(x = 580, y = 175)
        self.basicWidgetList.append( self.title3LBL )
        
        self.physicalMemWidgets = []
        self.yCounter = 140
        #self.physicalMemInfo1 = [ [ 30, "#f2f5f4", "OS Size", "" ], [ 75, "#c2c4c3", "Job Size", "312"], [ 0, "#979998", "Wasted", "412"] ]
        self.tempColor = "#f2f5f4"
        self.indexPointer = 0
        self.tempTypePrinted = False
        
        self.markLBL  =  Label( root , text = 0 , font = ('Times New Roman', 10),  bg = "#c6e3ad")
        self.markLBL.place(x = 60, y = self.yCounter - 20)
        self.physicalMemWidgets.append( self.markLBL )

        self.tempTotalSize = int(self.osSize)
        self.displayMap( self.osPercentage, "#f5f3ed", "Os Size", self.osPercentage, self.tempTotalSize )

        self.tempTotalSize = int(self.osSize) + int(self.size1)
        self.displayMap( self.job1Percentage, "#c2c4c3", "Job 1 Size", self.job1Percentage, self.tempTotalSize )

        self.tempTotalSize = int(self.osSize) + int(self.size1) + int(self.wasted1)
        self.displayMap( self.wasted1Percentage, "#979998", "Wasted size", self.wasted1Percentage, self.tempTotalSize )
        
        self.osSizeLBL  =  Label( root , text = "OS Size" , font = ('Times New Roman', 15),  bg = "#f5f3ed")
        self.osSizeLBL.place(x = 515, y = 245)
        self.basicWidgetList.append( self.osSizeLBL )

        self.osSizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.osSizeENTRY.place(x = 480, y = 285)
        self.osSizeENTRY.insert( 0, self.osSize )
        self.osSizeENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.osSizeENTRY )

        self.memSizeLBL  =  Label( root , text = "Memory Size" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.memSizeLBL.place(x = 705, y = 245)
        self.basicWidgetList.append( self.memSizeLBL )

        self.memSizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.memSizeENTRY.place(x = 690, y = 285)
        self.memSizeENTRY.insert( 0, self.memSize )
        self.memSizeENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.memSizeENTRY )

        self.job1SizeLBL  =  Label( root , text = "Job 1 Size" , font = ('Times New Roman', 15),  bg = "#c2c4c3")
        self.job1SizeLBL.place(x = 505, y = 345)
        self.basicWidgetList.append( self.job1SizeLBL )

        self.job1SizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.job1SizeENTRY.place(x = 480, y = 385)
        self.job1SizeENTRY.insert( 0, self.size1 )
        self.job1SizeENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.job1SizeENTRY )

        self.wastedSizeLBL  =  Label( root , text = "Wasted Size" , font = ('Times New Roman', 15),  bg = "#979998")
        self.wastedSizeLBL.place(x = 710, y = 345)
        self.basicWidgetList.append( self.wastedSizeLBL )

        self.wastedSizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.wastedSizeENTRY.place(x = 690, y = 385)
        self.wastedSizeENTRY.insert( 0, int(self.wasted1) )
        self.wastedSizeENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.wastedSizeENTRY )
        
        self.backBTN  =  Button ( root , text = 'BACK',command = self.result1_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 200 ,y = 530)
        self.basicWidgetList.append( self.backBTN )
        self.nextBTN  =  Button ( root , text = 'NEXT',command = self.result3_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.nextBTN.place (x = 580 ,y = 530)
        self.basicWidgetList.append( self.nextBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 530)
        self.basicWidgetList.append( self.exitBTN )

    def result3_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.singleContgiousBG = Label ( root , image = sc_bg, bg = "black" )
        self.singleContgiousBG.place(x = 0, y = 0)
        self.basicWidgetList.append( self.singleContgiousBG )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#fff0c3" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#fff0c3")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )

        self.title1LBL  =  Label( root , text = "Single Contiguous" , font = ('Times New Roman', 20),  bg = "#fff0c3")
        self.title1LBL.place(x = 100, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Memory Management Result" , font = ('Times New Roman', 20),  bg = "#fff0c3")
        self.title2LBL.place(x = 40, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Physical Memory Map" , font = ('Times New Roman', 20),  bg = "#c6e3ad")
        self.title3LBL.place(x = 540, y = 135)
        self.basicWidgetList.append( self.title3LBL )
        if self.cpuWait2 == "0:00:00":
            self.title3LBL  =  Label( root , text = "At {}, Job 2 Started".format(str(self.startTime2.time())) , font = ('Times New Roman', 12),  bg = "#c6e3ad")
            self.title3LBL.place(x = 580, y = 175)
            self.title3LBL  =  Label( root , text = "Earlier at {}, Job 1 Terminated".format(str(self.finishTime1.time())) , font = ('Times New Roman', 12),  bg = "#c6e3ad")
            self.title3LBL.place(x = 550, y = 200)
            self.basicWidgetList.append( self.title3LBL )
        else:
            self.title3LBL  =  Label( root , text = "At {}, Job 1 Terminated and Job 2 Started".format(str(self.startTime2.time())) , font = ('Times New Roman', 12),  bg = "#c6e3ad")
            self.title3LBL.place(x = 510, y = 175)
        self.basicWidgetList.append( self.title3LBL )
        
        self.physicalMemWidgets = []
        self.yCounter = 140
        #self.physicalMemInfo1 = [ [ 30, "#f2f5f4", "OS Size", "" ], [ 75, "#c2c4c3", "Job Size", "312"], [ 0, "#979998", "Wasted", "412"] ]
        self.tempColor = "#f2f5f4"
        self.indexPointer = 0
        self.tempTypePrinted = False
        
        self.markLBL  =  Label( root , text = 0 , font = ('Times New Roman', 10),  bg = "#c6e3ad")
        self.markLBL.place(x = 60, y = self.yCounter - 20)
        self.physicalMemWidgets.append( self.markLBL )

        self.tempTotalSize = int(self.osSize)
        self.displayMap( self.osPercentage, "#f5f3ed", "Os Size", self.osPercentage, self.tempTotalSize )

        self.tempTotalSize = int(self.osSize) + int(self.size2)
        self.displayMap( self.job2Percentage, "#c2c4c3", "Job 2 Size", self.job2Percentage, self.tempTotalSize )

        self.tempTotalSize = int(self.osSize) + int(self.size2) + int(self.wasted2)
        self.displayMap( self.wasted2Percentage, "#979998", "Wasted size", self.wasted2Percentage, self.tempTotalSize )
        
        self.osSizeLBL  =  Label( root , text = "OS Size" , font = ('Times New Roman', 15),  bg = "#f5f3ed")
        self.osSizeLBL.place(x = 515, y = 245)
        self.basicWidgetList.append( self.osSizeLBL )

        self.osSizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.osSizeENTRY.place(x = 480, y = 285)
        self.osSizeENTRY.insert( 0, self.osSize )
        self.osSizeENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.osSizeENTRY )

        self.memSizeLBL  =  Label( root , text = "Memory Size" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.memSizeLBL.place(x = 705, y = 245)
        self.basicWidgetList.append( self.memSizeLBL )

        self.memSizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.memSizeENTRY.place(x = 690, y = 285)
        self.memSizeENTRY.insert( 0, self.memSize )
        self.memSizeENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.memSizeENTRY )

        self.job2SizeLBL  =  Label( root , text = "Job 2 Size" , font = ('Times New Roman', 15),  bg = "#c2c4c3")
        self.job2SizeLBL.place(x = 505, y = 345)
        self.basicWidgetList.append( self.job2SizeLBL )

        self.job2SizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.job2SizeENTRY.place(x = 480, y = 385)
        self.job2SizeENTRY.insert( 0, self.size2 )
        self.job2SizeENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.job2SizeENTRY )

        self.wastedSizeLBL  =  Label( root , text = "Wasted Size" , font = ('Times New Roman', 15),  bg = "#979998")
        self.wastedSizeLBL.place(x = 710, y = 345)
        self.basicWidgetList.append( self.wastedSizeLBL )

        self.wastedSizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.wastedSizeENTRY.place(x = 690, y = 385)
        self.wastedSizeENTRY.insert( 0, int(self.wasted2) )
        self.wastedSizeENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.wastedSizeENTRY )
        
        self.backBTN  =  Button ( root , text = 'BACK',command = self.result2_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 200 ,y = 530)
        self.basicWidgetList.append( self.backBTN )
        self.nextBTN  =  Button ( root , text = 'NEXT',command = self.result4_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.nextBTN.place (x = 580 ,y = 530)
        self.basicWidgetList.append( self.nextBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 530)
        self.basicWidgetList.append( self.exitBTN )


    def result4_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.singleContgiousBG = Label ( root , image = sc_bg, bg = "black" )
        self.singleContgiousBG.place(x = 0, y = 0)
        self.basicWidgetList.append( self.singleContgiousBG )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#fff0c3" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#fff0c3")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )

        self.title1LBL  =  Label( root , text = "Single Contiguous" , font = ('Times New Roman', 20),  bg = "#fff0c3")
        self.title1LBL.place(x = 100, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Memory Management Result" , font = ('Times New Roman', 20),  bg = "#fff0c3")
        self.title2LBL.place(x = 40, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Physical Memory Map" , font = ('Times New Roman', 20),  bg = "#c6e3ad")
        self.title3LBL.place(x = 540, y = 135)
        self.basicWidgetList.append( self.title3LBL )
        if self.cpuWait3 == "0:00:00":
            self.title3LBL  =  Label( root , text = "At {}, Job 3 Started".format(str(self.startTime3.time())) , font = ('Times New Roman', 12),  bg = "#c6e3ad")
            self.title3LBL.place(x = 580, y = 175)
            self.title3LBL  =  Label( root , text = "Earlier at {}, Job 2 Terminated".format(str(self.finishTime2.time())) , font = ('Times New Roman', 12),  bg = "#c6e3ad")
            self.title3LBL.place(x = 550, y = 200)
            self.basicWidgetList.append( self.title3LBL )
        else:
            self.title3LBL  =  Label( root , text = "At {}, Job 2 Terminated and Job 3 Started".format(str(self.startTime3.time())) , font = ('Times New Roman', 12),  bg = "#c6e3ad")
            self.title3LBL.place(x = 510, y = 175)
        self.basicWidgetList.append( self.title3LBL )
        
        self.physicalMemWidgets = []
        self.yCounter = 140
        self.tempColor = "#f2f5f4"
        self.indexPointer = 0
        self.tempTypePrinted = False
        
        self.markLBL  =  Label( root , text = 0 , font = ('Times New Roman', 10),  bg = "#c6e3ad")
        self.markLBL.place(x = 60, y = self.yCounter - 20)
        self.physicalMemWidgets.append( self.markLBL )

        self.tempTotalSize = int(self.osSize)
        self.displayMap( self.osPercentage, "#f5f3ed", "Os Size", self.osPercentage, self.tempTotalSize )

        self.tempTotalSize = int(self.osSize) + int(self.size3) 
        self.displayMap( self.job3Percentage, "#c2c4c3", "Job 3 Size", self.job3Percentage, self.tempTotalSize )

        self.tempTotalSize = int(self.osSize) + int(self.size3) + int(self.wasted3) 
        self.displayMap( self.wasted3Percentage, "#979998", "Wasted size", self.wasted3Percentage, self.tempTotalSize )
        
        self.osSizeLBL  =  Label( root , text = "OS Size" , font = ('Times New Roman', 15),  bg = "#f5f3ed")
        self.osSizeLBL.place(x = 515, y = 245)
        self.basicWidgetList.append( self.osSizeLBL )

        self.osSizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.osSizeENTRY.place(x = 480, y = 285)
        self.osSizeENTRY.insert( 0, self.osSize )
        self.osSizeENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.osSizeENTRY )

        self.memSizeLBL  =  Label( root , text = "Memory Size" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.memSizeLBL.place(x = 705, y = 245)
        self.basicWidgetList.append( self.memSizeLBL )

        self.memSizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.memSizeENTRY.place(x = 690, y = 285)
        self.memSizeENTRY.insert( 0, self.memSize )
        self.memSizeENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.memSizeENTRY )

        self.job3SizeLBL  =  Label( root , text = "Job 3 Size" , font = ('Times New Roman', 15),  bg = "#c2c4c3")
        self.job3SizeLBL.place(x = 505, y = 345)
        self.basicWidgetList.append( self.job3SizeLBL )

        self.job3SizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.job3SizeENTRY.place(x = 480, y = 385)
        self.job3SizeENTRY.insert( 0, self.size3 )
        self.job3SizeENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.job3SizeENTRY )

        self.wastedSizeLBL  =  Label( root , text = "Wasted Size" , font = ('Times New Roman', 15),  bg = "#979998")
        self.wastedSizeLBL.place(x = 710, y = 345)
        self.basicWidgetList.append( self.wastedSizeLBL )

        self.wastedSizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.wastedSizeENTRY.place(x = 690, y = 385)
        self.wastedSizeENTRY.insert( 0, int(self.wasted3) )
        self.wastedSizeENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.wastedSizeENTRY )
        
        self.backBTN  =  Button ( root , text = 'BACK',command = self.result3_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 200 ,y = 530)
        self.basicWidgetList.append( self.backBTN )
        self.nextBTN  =  Button ( root , text = 'NEXT',command = self.result5_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.nextBTN.place (x = 580 ,y = 530)
        self.basicWidgetList.append( self.nextBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 530)
        self.basicWidgetList.append( self.exitBTN )


    def result5_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.singleContgiousBG = Label ( root , image = sc_bg, bg = "black" )
        self.singleContgiousBG.place(x = 0, y = 0)
        self.basicWidgetList.append( self.singleContgiousBG )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#fff0c3" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#fff0c3")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )

        self.title1LBL  =  Label( root , text = "Single Contiguous" , font = ('Times New Roman', 20),  bg = "#fff0c3")
        self.title1LBL.place(x = 100, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Memory Management Result" , font = ('Times New Roman', 20),  bg = "#fff0c3")
        self.title2LBL.place(x = 40, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Physical Memory Map" , font = ('Times New Roman', 20),  bg = "#c6e3ad")
        self.title3LBL.place(x = 540, y = 135)
        self.basicWidgetList.append( self.title3LBL )
        if self.cpuWait4 == "0:00:00":
            self.title3LBL  =  Label( root , text = "At {}, Job 4 Started".format(str(self.startTime4.time())) , font = ('Times New Roman', 12),  bg = "#c6e3ad")
            self.title3LBL.place(x = 580, y = 175)
            self.basicWidgetList.append( self.title3LBL )
            self.title3LBL  =  Label( root , text = "Earlier at {}, Job 3 Terminated".format(str(self.finishTime3.time())) , font = ('Times New Roman', 12),  bg = "#c6e3ad")
            self.title3LBL.place(x = 550, y = 200)
            self.basicWidgetList.append( self.title3LBL )
        else:
            self.title3LBL  =  Label( root , text = "At {}, Job 3 Terminated and Job 4 Started".format(str(self.startTime4.time())) , font = ('Times New Roman', 12),  bg = "#c6e3ad")
            self.title3LBL.place(x = 510, y = 175)
            self.basicWidgetList.append( self.title3LBL )
        
        self.physicalMemWidgets = []
        self.yCounter = 140
        self.tempColor = "#f2f5f4"
        self.indexPointer = 0
        self.tempTypePrinted = False
        
        self.markLBL  =  Label( root , text = 0 , font = ('Times New Roman', 10),  bg = "#c6e3ad")
        self.markLBL.place(x = 60, y = self.yCounter - 20)
        self.physicalMemWidgets.append( self.markLBL )

        self.tempTotalSize = int(self.osSize)
        self.displayMap( self.osPercentage, "#f5f3ed", "Os Size", self.osPercentage, self.tempTotalSize )

        self.tempTotalSize = int(self.osSize) + int(self.size4) 
        self.displayMap( self.job4Percentage, "#c2c4c3", "Job 4 Size", self.job4Percentage, self.tempTotalSize )

        self.tempTotalSize = int(self.osSize) + int(self.size4) + int(self.wasted4) 
        self.displayMap( self.wasted4Percentage, "#979998", "Wasted size", self.wasted4Percentage, self.tempTotalSize )
        
        self.osSizeLBL  =  Label( root , text = "OS Size" , font = ('Times New Roman', 15),  bg = "#f5f3ed")
        self.osSizeLBL.place(x = 515, y = 245)
        self.basicWidgetList.append( self.osSizeLBL )

        self.osSizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.osSizeENTRY.place(x = 480, y = 285)
        self.osSizeENTRY.insert( 0, self.osSize )
        self.osSizeENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.osSizeENTRY )

        self.memSizeLBL  =  Label( root , text = "Memory Size" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.memSizeLBL.place(x = 705, y = 245)
        self.basicWidgetList.append( self.memSizeLBL )

        self.memSizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.memSizeENTRY.place(x = 690, y = 285)
        self.memSizeENTRY.insert( 0, self.memSize )
        self.memSizeENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.memSizeENTRY )

        self.job4SizeLBL  =  Label( root , text = "Job 4 Size" , font = ('Times New Roman', 15),  bg = "#c2c4c3")
        self.job4SizeLBL.place(x = 505, y = 345)
        self.basicWidgetList.append( self.job4SizeLBL )

        self.job4SizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.job4SizeENTRY.place(x = 480, y = 385)
        self.job4SizeENTRY.insert( 0, self.size4 )
        self.job4SizeENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.job4SizeENTRY )

        self.wastedSizeLBL  =  Label( root , text = "Wasted Size" , font = ('Times New Roman', 15),  bg = "#979998")
        self.wastedSizeLBL.place(x = 710, y = 345)
        self.basicWidgetList.append( self.wastedSizeLBL )

        self.wastedSizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.wastedSizeENTRY.place(x = 690, y = 385)
        self.wastedSizeENTRY.insert( 0, int(self.wasted4) )
        self.wastedSizeENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.wastedSizeENTRY )
        
        self.backBTN  =  Button ( root , text = 'BACK',command = self.result4_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 200 ,y = 530)
        self.basicWidgetList.append( self.backBTN )
        self.nextBTN  =  Button ( root , text = 'NEXT',command = self.result6_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.nextBTN.place (x = 580 ,y = 530)
        self.basicWidgetList.append( self.nextBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 530)
        self.basicWidgetList.append( self.exitBTN )


    def result6_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.singleContgiousBG = Label ( root , image = sc_bg, bg = "black" )
        self.singleContgiousBG.place(x = 0, y = 0)
        self.basicWidgetList.append( self.singleContgiousBG )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#fff0c3" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#fff0c3")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )

        self.title1LBL  =  Label( root , text = "Single Contiguous" , font = ('Times New Roman', 20),  bg = "#fff0c3")
        self.title1LBL.place(x = 100, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Memory Management Result" , font = ('Times New Roman', 20),  bg = "#fff0c3")
        self.title2LBL.place(x = 40, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Physical Memory Map" , font = ('Times New Roman', 20),  bg = "#c6e3ad")
        self.title3LBL.place(x = 540, y = 135)
        self.basicWidgetList.append( self.title3LBL )
        if self.cpuWait5 == "0:00:00":
            self.title3LBL  =  Label( root , text = "At {}, Job 5 Started".format(str(self.startTime5.time())) , font = ('Times New Roman', 12),  bg = "#c6e3ad")
            self.title3LBL.place(x = 580, y = 175)
            self.title3LBL  =  Label( root , text = "Earlier at {}, Job 4 Terminated".format(str(self.finishTime4.time())) , font = ('Times New Roman', 12),  bg = "#c6e3ad")
            self.title3LBL.place(x = 550, y = 200)
            self.basicWidgetList.append( self.title3LBL )
        else:
            self.title3LBL  =  Label( root , text = "At {}, Job 4 Terminated and Job 5 Started".format(str(self.startTime5.time())) , font = ('Times New Roman', 12),  bg = "#c6e3ad")
            self.title3LBL.place(x = 510, y = 175)
        self.basicWidgetList.append( self.title3LBL )
        
        self.physicalMemWidgets = []
        self.yCounter = 140
        self.tempColor = "#f2f5f4"
        self.indexPointer = 0
        self.tempTypePrinted = False
        
        self.markLBL  =  Label( root , text = 0 , font = ('Times New Roman', 10),  bg = "#c6e3ad")
        self.markLBL.place(x = 60, y = self.yCounter - 20)
        self.physicalMemWidgets.append( self.markLBL )

        self.tempTotalSize = int(self.osSize)
        self.displayMap( self.osPercentage, "#f5f3ed", "Os Size", self.osPercentage, self.tempTotalSize )

        self.tempTotalSize = int(self.osSize) + int(self.size5) 
        self.displayMap( self.job5Percentage, "#c2c4c3", "Job 5 Size", self.job5Percentage, self.tempTotalSize )

        self.tempTotalSize = int(self.osSize) + int(self.size5) + int(self.wasted5) 
        self.displayMap( self.wasted5Percentage, "#979998", "Wasted size", self.wasted5Percentage, self.tempTotalSize )
        
        self.osSizeLBL  =  Label( root , text = "OS Size" , font = ('Times New Roman', 15),  bg = "#f5f3ed")
        self.osSizeLBL.place(x = 515, y = 245)
        self.basicWidgetList.append( self.osSizeLBL )

        self.osSizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.osSizeENTRY.place(x = 480, y = 285)
        self.osSizeENTRY.insert( 0, self.osSize )
        self.osSizeENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.osSizeENTRY )

        self.memSizeLBL  =  Label( root , text = "Memory Size" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.memSizeLBL.place(x = 705, y = 245)
        self.basicWidgetList.append( self.memSizeLBL )

        self.memSizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.memSizeENTRY.place(x = 690, y = 285)
        self.memSizeENTRY.insert( 0, self.memSize )
        self.memSizeENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.memSizeENTRY )

        self.job5SizeLBL  =  Label( root , text = "Job 5 Size" , font = ('Times New Roman', 15),  bg = "#c2c4c3")
        self.job5SizeLBL.place(x = 505, y = 345)
        self.basicWidgetList.append( self.job5SizeLBL )

        self.job5SizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.job5SizeENTRY.place(x = 480, y = 385)
        self.job5SizeENTRY.insert( 0, self.size5 )
        self.job5SizeENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.job5SizeENTRY )

        self.wastedSizeLBL  =  Label( root , text = "Wasted Size" , font = ('Times New Roman', 15),  bg = "#979998")
        self.wastedSizeLBL.place(x = 710, y = 345)
        self.basicWidgetList.append( self.wastedSizeLBL )

        self.wastedSizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.wastedSizeENTRY.place(x = 690, y = 385)
        self.wastedSizeENTRY.insert( 0, int(self.wasted5) )
        self.wastedSizeENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.wastedSizeENTRY )
        
        self.backBTN  =  Button ( root , text = 'BACK',command = self.result5_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 200 ,y = 530)
        self.basicWidgetList.append( self.backBTN )
        self.nextBTN  =  Button ( root , text = 'TRY NEW INPUT',command = self.input1_window , font = ('Poppins', 16, 'bold'), width  =  14, bg = "#659bdb" )
        self.nextBTN.place (x = 580 ,y = 530)
        self.basicWidgetList.append( self.nextBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 530)
        self.basicWidgetList.append( self.exitBTN )
# END OF SCMM PROGRAM: Line 227-1337



# SPA PROGRAM: Line 1340-2838

# Global Variables
partition1 = 8
partition2 = 32
partition3 = 32
partition4 = 120
partition5 = 520
partitionSizes = [ partition1, partition2, partition3, partition4, partition5 ]

osSize = 312
memSize = 1024

size1 = 5
size2 = 32
size3 = 50
size4 = 130
size5 = 150

jobSizes = [ size1, size2, size3, size4, size5 ]

osPercentage = float(( float(osSize) / float(memSize) ) * 100 )
partition1Percentage = float(( float(partition1) / float(memSize) ) * 100 )
partition2Percentage = float(( float(partition2) / float(memSize) ) * 100 )
partition3Percentage = float(( float(partition3) / float(memSize) ) * 100 )
partition4Percentage = float(( float(partition4) / float(memSize) ) * 100 )
partition5Percentage = float(( float(partition5) / float(memSize) ) * 100 )


allPartitionPercentage = [ partition1Percentage,
                           partition2Percentage,
                           partition3Percentage,
                           partition4Percentage,
                           partition5Percentage ]
basicWidgetList = []
physicalMemWidgets = []
# */ End of Global variable code block.



# This is a node class for the result windows ( i.e. memMap_window, pat_window )
# Check line 41 and 52 to get the description of the Node class' functions.
class Node:
    def __init__( self, time = "*:**:**" , data = None, timeType = "After", titleText = "Jx Terminated" ):
        self.backPointer = None
        self.nextPointer = None
        self.data = data
        self.time = time
        self.timeType = timeType
        self.titleText = titleText
        if self.data == None:
            self.data = [ "Available", "Available", "Available", "Available", "Available" ]

    # For getting the current date
    def current_date( self ):
        self.dateString  =  datetime.date.today().strftime("%B %d, %Y")
        self.dateLBL.config(text = self.dateString)

    # This updates the clock widget
    def tick( self ):
        if self.tick_on:
            self.timeString  =  time.strftime("%H:%M:%S")
            self.clockLBL.config(text = self.timeString)
            self.clockLBL.after(200, self.tick )
        else:
            pass


    # The program has two list which contains a reference to all the program's widgets
    # And what this function does is it tries to clear/destroy all of these widgets
    # using the lists which contains the program's widgets.
    # The two lists are:
    #   - basicWidgetList: For most of the basic widgets
    #   - self.physicalMemWidgets: For the widgets used to display physical memory map
    def clearWidgets( self ):
        try:
            self.tick_on = False
            self.clearWidgetList( basicWidgetList )
            self.clearWidgetList( physicalMemWidgets )
        except:
            pass
        return


    # This function destroys all of the widgets inside the inputted widgetsToClear list.
    def clearWidgetList ( self, widgetsToClear):
        for widget in widgetsToClear:
            widget.destroy()

            
    # This function displays the necessary widgets for physical memory map.
    # To get a general gist, the program has around 50 labels which acts as the physical memory map.
    # In addition, it has a text label which marks each section of the physical memory map.
    def displayMap( self, tempPointer, tempColor, tempText, tempPercentage, tempTotalSize ):
        self.tempPointer = int(tempPointer)
        self.tempColor = tempColor
        self.tempText = tempText
        self.tempPercentage = tempPercentage
        self.tempTotalSize = tempTotalSize
        
        if self.tempPercentage != 0:
            self.tempLBL = Label( root , text = "          " * 25 , font = ('Times New Roman', 1),  bg = self.tempColor)
            self.tempLBL.place(x = 80, y = self.yCounter)
            self.yCounter += 7
            physicalMemWidgets.append( self.tempLBL )
            
            self.tempLBL = Label( root , text = self.tempText , font = ('Times New Roman', 10),  bg = self.tempColor)
            self.tempLBL.place(x = 350, y = self.yCounter)
            physicalMemWidgets.append( self.tempLBL )
        for i in range( int( self.tempPercentage / 2 ) ):
            if self.tempPointer != 0:
                self.tempLBL = Label( root , text = "          " * 25 , font = ('Times New Roman', 1),  bg = self.tempColor)
                self.tempLBL.place(x = 80, y = self.yCounter)
                self.yCounter += 7
                physicalMemWidgets.append( self.tempLBL )
                self.tempPointer -= 1
            else:
                pass
        if self.tempPercentage != 0:
            self.tempLBL  =  Label( root , text = tempTotalSize , font = ('Times New Roman', 10),  bg = self.tempColor)
            self.tempLBL.place(x = 50, y = self.yCounter - 15)
            physicalMemWidgets.append( self.tempLBL )

        return


    # This function points which window to go back on.
    def memMap_backBTN_Pressed( self ):
        if self.backPointer == None:
            spa_program.mainResult1_window()
        else:
            self.backPointer.pat_window()


    # For displaying the physical memory map
    def memMap_window( self ):
        #print( partitionSizes )
        self.clearWidgets()
        basicWidgetList = []
        self.nextAvailable = True
        
        self.staticPartitionedBG = Label ( root , image = spa_bg, bg = "black" )
        self.staticPartitionedBG.place(x = 0, y = 0)
        basicWidgetList.append( self.staticPartitionedBG )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffc800" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffc800")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        basicWidgetList.append( self.dateLBL )

        self.title1LBL  =  Label( root , text = "Static First Fit"  , font = ('Times New Roman', 20),  bg = "#ffc800")
        self.title1LBL.place(x = 120, y = 20)
        basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Partitioned Allocation" , font = ('Times New Roman', 20),  bg = "#ffc800")
        self.title2LBL.place(x = 75, y = 65)
        basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Physical Memory Map" , font = ('Times New Roman', 20),  bg = "#c6e3ad")
        self.title3LBL.place(x = 490, y = 120)
        basicWidgetList.append( self.title3LBL )
        self.title3LBL  =  Label( root , text = "{} {}, {}".format(str(self.timeType), str(self.time), str(self.titleText)) , font = ('Times New Roman', 12),  bg = "#c6e3ad")
        if self.timeType == "After":
            self.title3LBL.place(x = 525, y = 153)
        else:
            self.title3LBL.place(x = 543, y = 153)
        basicWidgetList.append( self.title3LBL )
        
        physicalMemWidgets = []
        self.yCounter = 140
        self.indexPointer = 0
        
        self.markLBL  =  Label( root , text = 0 , font = ('Times New Roman', 10),  bg = "#c6e3ad")
        self.markLBL.place(x = 60, y = self.yCounter - 20)
        physicalMemWidgets.append( self.markLBL )

        self.tempTotalSize = int(osSize)
        self.displayMap( osPercentage, "#f5f3ed", "Os Size", osPercentage, self.tempTotalSize )
                
        self.tempTotalSize = int(osSize) + int(partition1) 
        self.displayMap( partition1Percentage, "#f77777", self.data[0], partition1Percentage, self.tempTotalSize )
                
        self.tempTotalSize = int(osSize) + int(partition1) + int(partition2)
        self.displayMap( partition2Percentage, "#f7d977", self.data[1], partition2Percentage, self.tempTotalSize )

        self.tempTotalSize = int(osSize) + int(partition1) + int(partition2) + int(partition3)
        self.displayMap( partition3Percentage, "#77f7e6", self.data[2], partition3Percentage, self.tempTotalSize )

        self.tempTotalSize = int(osSize) + int(partition1) + int(partition2) + int(partition3) + int(partition4)
        self.displayMap( partition4Percentage, "#77d5f7", self.data[3], partition4Percentage, self.tempTotalSize )

        self.tempTotalSize = int(osSize) + int(partition1) + int(partition2) + int(partition3) + int(partition4) + int(partition5)
        self.displayMap( partition5Percentage, "#d577f7", self.data[4], partition5Percentage, self.tempTotalSize )

        self.partitionLBL  =  Label( root , text = "Partition" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.partitionLBL.place(x = 420, y = 180)
        basicWidgetList.append( self.partitionLBL )

        self.partition1LBL  =  Label( root , text = "1" , font = ('Times New Roman', 15),  bg = "#f77777")
        self.partition1LBL.place(x = 440, y = 240)
        basicWidgetList.append( self.partition1LBL )
        
        self.partition2LBL  =  Label( root , text = "2" , font = ('Times New Roman', 15),  bg = "#f7d977")
        self.partition2LBL.place(x = 440, y = 300)
        basicWidgetList.append( self.partition2LBL )
        
        self.partition3LBL  =  Label( root , text = "3" , font = ('Times New Roman', 15),  bg = "#77f7e6")
        self.partition3LBL.place(x = 440, y = 360)
        basicWidgetList.append( self.partition3LBL )
        
        self.partition4LBL  =  Label( root , text = "4" , font = ('Times New Roman', 15),  bg = "#77d5f7")
        self.partition4LBL.place(x = 440, y = 420)
        basicWidgetList.append( self.partition4LBL )
        
        self.partition5LBL  =  Label( root , text = "5" , font = ('Times New Roman', 15),  bg = "#d577f7")
        self.partition5LBL.place(x = 440, y = 480)
        basicWidgetList.append( self.partition5LBL )

        self.allFragmentation = []

        for i in range( len(self.data) ):
            if self.data[i] != "Available":
                self.tempJobNum = int(self.data[i][11]) - 1
                self.allFragmentation.append( int(partitionSizes[i]) - int(jobSizes[self.tempJobNum]) )
            else:
                self.allFragmentation.append( "--" )

        self.fragmentationLBL  =  Label( root , text = "Internal Fragmentation" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.fragmentationLBL.place(x = 510, y = 180)
        basicWidgetList.append( self.fragmentationLBL )

        self.fragmentation1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fragmentation1ENTRY.place(x = 530, y = 240)
        self.fragmentation1ENTRY.insert( 0, self.allFragmentation[0] )
        self.fragmentation1ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.fragmentation1ENTRY )
        
        self.fragmentation2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fragmentation2ENTRY.place(x = 530, y = 300)
        self.fragmentation2ENTRY.insert( 0, self.allFragmentation[1] )
        self.fragmentation2ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.fragmentation2ENTRY )
        
        self.fragmentation3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fragmentation3ENTRY.place(x = 530, y = 360)
        self.fragmentation3ENTRY.insert( 0, self.allFragmentation[2] )
        self.fragmentation3ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.fragmentation3ENTRY )
        
        self.fragmentation4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fragmentation4ENTRY.place(x = 530, y = 420)
        self.fragmentation4ENTRY.insert( 0, self.allFragmentation[3] )
        self.fragmentation4ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.fragmentation4ENTRY )
        
        self.fragmentation5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fragmentation5ENTRY.place(x = 530, y = 480)
        self.fragmentation5ENTRY.insert( 0, self.allFragmentation[4] )
        self.fragmentation5ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.fragmentation5ENTRY )

        self.statusLBL  =  Label( root , text = "Status" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.statusLBL.place(x = 740, y = 180)
        basicWidgetList.append( self.statusLBL )
        
        self.status1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.status1ENTRY.place(x = 700, y = 240)
        self.status1ENTRY.insert( 0, self.data[0] )
        self.status1ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.status1ENTRY )
        
        self.status2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.status2ENTRY.place(x = 700, y = 300)
        self.status2ENTRY.insert( 0, self.data[1] )
        self.status2ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.status2ENTRY )
        
        self.status3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.status3ENTRY.place(x = 700, y = 360)
        self.status3ENTRY.insert( 0, self.data[2] )
        self.status3ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.status3ENTRY )
        
        self.status4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.status4ENTRY.place(x = 700, y = 420)
        self.status4ENTRY.insert( 0, self.data[3] )
        self.status4ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.status4ENTRY )
        
        self.status5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.status5ENTRY.place(x = 700, y = 480)
        self.status5ENTRY.insert( 0, self.data[4] )
        self.status5ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.status5ENTRY )

        self.backBTN  =  Button ( root , text = 'BACK',command = self.memMap_backBTN_Pressed , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 200 ,y = 530)
        basicWidgetList.append( self.backBTN )
        self.nextBTN  =  Button ( root , text = 'NEXT',command = self.pat_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.nextBTN.place (x = 580 ,y = 530)
        basicWidgetList.append( self.nextBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 530)
        basicWidgetList.append( self.exitBTN )


    # This function points which window to go next.
    def pat_nextBTN_Pressed( self ):
        if self.nextPointer == None:
            spa_program.mainInput1_window()
        else:
            self.nextPointer.memMap_window()


    # For displaying the partition allocation table.
    def pat_window( self ):
        self.clearWidgets()
        basicWidgetList = []
        
        self.staticPartitionedBG = Label ( root , image = spa_bg, bg = "black" )
        self.staticPartitionedBG.place(x = 0, y = 0)
        basicWidgetList.append( self.staticPartitionedBG )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffc800" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffc800")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        basicWidgetList.append( self.dateLBL )
        
        self.title1LBL  =  Label( root , text = "Static First Fit"  , font = ('Times New Roman', 20),  bg = "#ffc800")
        self.title1LBL.place(x = 120, y = 20)
        basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Partitioned Allocation" , font = ('Times New Roman', 20),  bg = "#ffc800")
        self.title2LBL.place(x = 75, y = 65)
        basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Partition Allocation Table" , font = ('Times New Roman', 20),  bg = "#c6e3ad")
        self.title3LBL.place(x = 345, y = 120)
        basicWidgetList.append( self.title3LBL )
        self.title3LBL  =  Label( root , text = "{} {}, {}".format(str(self.timeType), str(self.time), str(self.titleText)) , font = ('Times New Roman', 12),  bg = "#c6e3ad")
        if self.timeType == "After":
            self.title3LBL.place(x = 392, y = 150)
        else:
            self.title3LBL.place(x = 417, y = 150)
        basicWidgetList.append( self.title3LBL )

        self.partitionLBL  =  Label( root , text = "Partition" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.partitionLBL.place(x = 90, y = 180)
        basicWidgetList.append( self.partitionLBL )

        self.partition1LBL  =  Label( root , text = "1" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.partition1LBL.place(x = 120, y = 240)
        basicWidgetList.append( self.partition1LBL )
        
        self.partition2LBL  =  Label( root , text = "2" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.partition2LBL.place(x = 120, y = 300)
        basicWidgetList.append( self.partition2LBL )
        
        self.partition3LBL  =  Label( root , text = "3" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.partition3LBL.place(x = 120, y = 360)
        basicWidgetList.append( self.partition3LBL )
        
        self.partition4LBL  =  Label( root , text = "4" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.partition4LBL.place(x = 120, y = 420)
        basicWidgetList.append( self.partition4LBL )
        
        self.partition5LBL  =  Label( root , text = "5" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.partition5LBL.place(x = 120, y = 480)
        basicWidgetList.append( self.partition5LBL )
        
        self.partitionSizeLBL  =  Label( root , text = "Partition Size" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.partitionSizeLBL.place(x = 235, y = 180)
        basicWidgetList.append( self.partitionSizeLBL )
        
        self.partitionSize1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.partitionSize1ENTRY.place(x = 225, y = 240)
        self.partitionSize1ENTRY.insert( 0, partition1 )
        self.partitionSize1ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.partitionSize1ENTRY )
        
        self.partitionSize2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.partitionSize2ENTRY.place(x = 225, y = 300)
        self.partitionSize2ENTRY.insert( 0, partition2 )
        self.partitionSize2ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.partitionSize2ENTRY )
        
        self.partitionSize3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.partitionSize3ENTRY.place(x = 225, y = 360)
        self.partitionSize3ENTRY.insert( 0, partition3 )
        self.partitionSize3ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.partitionSize3ENTRY )
        
        self.partitionSize4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.partitionSize4ENTRY.place(x = 225, y = 420)
        self.partitionSize4ENTRY.insert( 0, partition4 )
        self.partitionSize4ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.partitionSize4ENTRY )
        
        self.partitionSize5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.partitionSize5ENTRY.place(x = 225, y = 480)
        self.partitionSize5ENTRY.insert( 0, partition5 )
        self.partitionSize5ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.partitionSize5ENTRY )
        
        self.locationLBL  =  Label( root , text = "Location" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.locationLBL.place(x = 520, y = 180)
        basicWidgetList.append( self.locationLBL )

        self.location1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.location1ENTRY.place(x = 490, y = 240)
        self.location1ENTRY.insert( 0, int(osSize) )
        self.location1ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.location1ENTRY )
        
        self.location2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.location2ENTRY.place(x = 490, y = 300)
        self.location2ENTRY.insert( 0, int(osSize) + int(partition1) )
        self.location2ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.location2ENTRY )
        
        self.location3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.location3ENTRY.place(x = 490, y = 360)
        self.location3ENTRY.insert( 0, int(osSize) + int(partition1) + int(partition2) )
        self.location3ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.location3ENTRY )
        
        self.location4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.location4ENTRY.place(x = 490, y = 420)
        self.location4ENTRY.insert( 0, int(osSize) + int(partition1) + int(partition2) + int(partition3) )
        self.location4ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.location4ENTRY )
        
        self.location5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.location5ENTRY.place(x = 490, y = 480)
        self.location5ENTRY.insert( 0, int(osSize) + int(partition1) + int(partition2) + int(partition3) + int(partition4) )
        self.location5ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.location5ENTRY )
        
        self.statusLBL  =  Label( root , text = "Status" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.statusLBL.place(x = 740, y = 180)
        basicWidgetList.append( self.statusLBL )
        
        self.status1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.status1ENTRY.place(x = 700, y = 240)
        self.status1ENTRY.insert( 0, self.data[0] )
        self.status1ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.status1ENTRY )
        
        self.status2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.status2ENTRY.place(x = 700, y = 300)
        self.status2ENTRY.insert( 0, self.data[1] )
        self.status2ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.status2ENTRY )
        
        self.status3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.status3ENTRY.place(x = 700, y = 360)
        self.status3ENTRY.insert( 0, self.data[2] )
        self.status3ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.status3ENTRY )
        
        self.status4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.status4ENTRY.place(x = 700, y = 420)
        self.status4ENTRY.insert( 0, self.data[3] )
        self.status4ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.status4ENTRY )
        
        self.status5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.status5ENTRY.place(x = 700, y = 480)
        self.status5ENTRY.insert( 0, self.data[4] )
        self.status5ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.status5ENTRY )

        self.backBTN  =  Button ( root , text = 'BACK',command = self.memMap_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 200 ,y = 530)
        basicWidgetList.append( self.backBTN )
        if self.nextPointer == None:
            self.nextBTN  =  Button ( root , text = 'TRY NEW INPUT',command = self.pat_nextBTN_Pressed , font = ('Poppins', 16, 'bold'), width  =  14, bg = "#659bdb" )
        else:
            self.nextBTN  =  Button ( root , text = 'NEXT',command = self.pat_nextBTN_Pressed , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.nextBTN.place (x = 580 ,y = 530)
        basicWidgetList.append( self.nextBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 530)
        basicWidgetList.append( self.exitBTN )
        #self.allJobResults = [ [ startTime, finishTime, cpuWait, partitionLocation ] ]


class staticPartitionedAllocation:
    def __init__ ( self ):
        self.headNode = None

    # To clear the linked list of nodes.
    def clearNodes( self ):
        self.headNode = None
        return

    # To add a node into the linked list
    def addResultNode( self, time, resultData, timeType, titleText ): # ( self, time = "9:00:00" , data = None, timeType = "At", titleText = "Jx removed" ):
        self.tempNode = Node( time, resultData, timeType, titleText )

        if self.headNode == None:
            self.headNode = self.tempNode
        else:
            self.headNode.backPointer = self.tempNode
            self.tempNode.nextPointer = self.headNode

            self.headNode = self.tempNode
        return
    
    # For getting the current date
    def current_date( self ):
        self.dateString  =  datetime.date.today().strftime("%B %d, %Y")
        self.dateLBL.config(text = self.dateString)

    # This updates the clock widget
    def tick( self ):
        if self.tick_on:
            self.timeString  =  time.strftime("%H:%M:%S")
            self.clockLBL.config(text = self.timeString)
            self.clockLBL.after(200, self.tick )
        else:
            pass


    # This function returns True if timeInput is not in proper time format
    # Else, returns False if the input is in proper time format
    # Time format is HH:MM
    def isNotTimeFormat( self, timeInput):
        try:
            time.strptime( timeInput, '%H:%M')
            return False
        except ValueError:
            return True


    # This function returns True if the integerInput is not an Integer.
    # If it is an integer, return False.
    def isNotInteger( self, integerInput):
        try:
            self.intTest = int(integerInput)
            return False
        except ValueError:
            return True

    # This function checks if a certain time( check_time ) is between two time ( begin_time and end_time )
    def is_time_between(self, begin_time, end_time, check_time=None):
        # If check time is not given, default to current UTC time
        check_time = check_time or datetime.utcnow().time()
        if begin_time < end_time:
            return check_time >= begin_time and check_time <= end_time
        else: # crosses midnight
            return check_time >= begin_time or check_time <= end_time

    # This function checks if a certain job could fit into any of the partitions.
    def cantFitInPartition( self, tempJob ):
        try:
            ##print( partitionSizes )
            ##print ( "start" )
            self.tempJob = int(tempJob)
            self.tempResult = True
            ##print ( "2" )
            for i in range( len( partitionSizes) ):
                ##print( " partition size: " , partitionSizes[i] )
                ##print ( " temp job: " , self.tempJob )
                if int(partitionSizes[i]) >= self.tempJob:
                    ##print( "2.2" )
                    self.tempResult = False
                    break
            ##print ( "3" )
            return self.tempResult
        except:
            return True


    # The program has two list which contains a reference to all the program's widgets
    # And what this function does is it tries to clear/destroy all of these widgets
    # using the lists which contains the program's widgets.
    # The two lists are:
    #   - basicWidgetList: For most of the basic widgets
    #   - self.physicalMemWidgets: For the widgets used to display physical memory map
    def clearWidgets( self ):
        try:
            self.tick_on = False
            self.clearWidgetList( basicWidgetList )
            self.clearWidgetList( physicalMemWidgets )
        except:
            pass
        return


    # This function destroys all of the widgets inside the inputted widgetsToClear list.
    def clearWidgetList ( self, widgetsToClear):
        for widget in widgetsToClear:
            widget.destroy()


    # This function displays the necessary widgets for physical memory map.
    # To get a general gist, the program has around 50 labels which acts as the physical memory map.
    # In addition, it has a text label which marks each section of the physical memory map.
    def displayMap( self, tempPointer, tempColor, tempText, tempPercentage, tempTotalSize ):
        self.tempPointer = int(tempPointer)
        self.tempColor = tempColor
        self.tempText = tempText
        self.tempPercentage = tempPercentage
        self.tempTotalSize = tempTotalSize
        
        if self.tempPercentage != 0:
            self.tempLBL = Label( root , text = "          " * 25 , font = ('Times New Roman', 1),  bg = self.tempColor)
            self.tempLBL.place(x = 80, y = self.yCounter)
            self.yCounter += 5
            physicalMemWidgets.append( self.tempLBL )
            
            self.tempLBL = Label( root , text = self.tempText , font = ('Times New Roman', 10),  bg = self.tempColor)
            self.tempLBL.place(x = 350, y = self.yCounter)
            physicalMemWidgets.append( self.tempLBL )
        for i in range( int( self.tempPercentage / 2 ) ):
            if self.tempPointer != 0:
                self.tempLBL = Label( root , text = "          " * 25 , font = ('Times New Roman', 1),  bg = self.tempColor)
                self.tempLBL.place(x = 80, y = self.yCounter)
                self.yCounter += 5
                physicalMemWidgets.append( self.tempLBL )
                self.tempPointer -= 1
            else:
                pass
        if self.tempPercentage != 0:
            self.tempLBL  =  Label( root , text = tempTotalSize , font = ('Times New Roman', 10),  bg = self.tempColor)
            self.tempLBL.place(x = 50, y = self.yCounter - 15)
            physicalMemWidgets.append( self.tempLBL )

        return


    # This function is for setting partitions
    def mainInput1_setPartitionBTN_Pressed ( self ):
        global physicalMemWidgets

        global partition1
        global partition2
        global partition3
        global partition4
        global partition5
        global partitionSizes

        global osSize
        global memSize

        global size1
        global size2
        global size3
        global size4
        global size5
        global jobSizes

        global osPercentage
        global partition1Percentage
        global partition2Percentage
        global partition3Percentage
        global partition4Percentage
        global partition5Percentage
        global allPartitionPercentage
        if messagebox.askyesno( "Confirmation..." , " Are you sure you want to set partition? " ) == True :
            #self.nextAvailable = False
            partition1 = self.partition1ENTRY.get()
            partition2 = self.partition2ENTRY.get()
            partition3 = self.partition3ENTRY.get()
            partition4 = self.partition4ENTRY.get()
            partition5 = self.partition5ENTRY.get()

            self.partition1_Check = self.isNotInteger( partition1 )
            self.partition2_Check = self.isNotInteger( partition2 )
            self.partition3_Check = self.isNotInteger( partition3 )
            self.partition4_Check = self.isNotInteger( partition4 )
            self.partition5_Check = self.isNotInteger( partition5 )

            memSize = self.memSizeENTRY.get()
            osSize = self.osSizeENTRY.get()

            self.memSize_Check = self.isNotInteger( memSize )
            self.osSize_Check = self.isNotInteger( osSize )

            self.totalSize = 0

            try:
                self.totalSize = int(partition1) + int(partition2) + int(partition3) + int(partition4) + int(partition5) + int(osSize)
            except:
                pass

            if self.memSize_Check or self.osSize_Check :
                #print ( "Error: Invalid Memory or OS Size input." )
                messagebox.showinfo( "Partition Error" , "Error: Invalid Memory or OS Size input." )
            elif int(memSize) < int(osSize):
                ##print ( "ting" )
                #print ( " Error: Os Size can't exceed Memory Size. " )
                messagebox.showinfo( "Partition Error" , "Error: Os Size can't exceed Memory Size." )
            elif self.partition1_Check or self.partition2_Check or self.partition3_Check or self.partition4_Check or self.partition5_Check:
                #print ( "Error: Partition Size input." )
                messagebox.showinfo( "Partition Error" , "Error: Partition Size input." )
            elif int(self.totalSize) > int(memSize):
                #print ( "Error: Total taken size exceeded Memory Size." )
                messagebox.showinfo( "Partition Error" , "Error: Total taken size exceeded Memory Size." )
            elif int(self.totalSize) != int(memSize):
                #print ( "Error: Total taken size must be equal to Memory Size." )
                messagebox.showinfo( "Partition Error" , "Error: Total taken size must be equal to Memory Size." )
            else:
                self.clearWidgetList( physicalMemWidgets )
                physicalMemWidgets = []
                
                osPercentage = float(( float(osSize) / float(memSize) ) * 100 )
                partition1Percentage = float(( float(partition1) / float(memSize) ) * 100 )
                partition2Percentage = float(( float(partition2) / float(memSize) ) * 100 )
                partition3Percentage = float(( float(partition3) / float(memSize) ) * 100 )
                partition4Percentage = float(( float(partition4) / float(memSize) ) * 100 )
                partition5Percentage = float(( float(partition5) / float(memSize) ) * 100 )


                allPartitionPercentage = [ partition1Percentage,
                                           partition2Percentage,
                                           partition3Percentage,
                                           partition4Percentage,
                                           partition5Percentage ]

                self.yCounter = 185
                self.indexPointer = 0
        
                self.markLBL  =  Label( root , text = 0 , font = ('Times New Roman', 10),  bg = "#c6e3ad")
                self.markLBL.place(x = 60, y = self.yCounter - 20)
                physicalMemWidgets.append( self.markLBL )

                self.tempTotalSize = int(osSize)
                self.displayMap( osPercentage, "#f5f3ed", "Os Size", osPercentage, self.tempTotalSize )
                
                self.tempTotalSize = int(osSize) + int(partition1) 
                self.displayMap( partition1Percentage, "#f77777", "Partition 1", partition1Percentage, self.tempTotalSize )
                
                self.tempTotalSize = int(osSize) + int(partition1) + int(partition2)
                self.displayMap( partition2Percentage, "#f7d977", "Partition 2", partition2Percentage, self.tempTotalSize )

                self.tempTotalSize = int(osSize) + int(partition1) + int(partition2) + int(partition3)
                self.displayMap( partition3Percentage, "#77f7e6", "Partition 3", partition3Percentage, self.tempTotalSize )

                self.tempTotalSize = int(osSize) + int(partition1) + int(partition2) + int(partition3) + int(partition4)
                self.displayMap( partition4Percentage, "#77d5f7", "Partition 4", partition4Percentage, self.tempTotalSize )

                self.tempTotalSize = int(osSize) + int(partition1) + int(partition2) + int(partition3) + int(partition4) + int(partition5)
                self.displayMap( partition5Percentage, "#d577f7", "Partition 5", partition5Percentage, self.tempTotalSize )

                #self.nextAvailable = True
                partition1 = int(partition1)
                partition2 = int(partition2)
                partition3 = int(partition3)
                partition4 = int(partition4)
                partition5 = int(partition5)
                partitionSizes = [ partition1, partition2, partition3, partition4, partition5 ]
                ##print( partitionSizes )
                messagebox.showinfo( "Partition Success" , "The partitions has been set." )


    # This function checks if the user is eligible to continue into the next window
    def mainInput1_nextBTN_Pressed ( self ):
        if messagebox.askyesno( "Confirmation..." , " Are you sure you want to move on? " ) == True :
            if self.nextAvailable == True:
                self.mainInput2_window()
            else:
                #print ( "Error: Please make sure that you've correctly set the partition." )
                messagebox.showinfo( "Partition Error" , "Error: Please make sure that you've correctly set the partition." )

    def mainMenuBTN_Pressed( self ):
        main.mainMenu_window()

    def aboutUsBTN_Pressed( self ):
        main.aboutUs_window()
        

    # For taking user's input of partitions
    def mainInput1_window( self ):
        root.title ( "Static First Fit Partitioned Allocation" )
        self.clearWidgets()
        basicWidgetList = []
        self.nextAvailable = True
        
        self.staticPartitionedBG = Label ( root , image = spa_bg, bg = "black" )
        self.staticPartitionedBG.place(x = 0, y = 0)
        basicWidgetList.append( self.staticPartitionedBG )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffc800" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffc800")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        basicWidgetList.append( self.dateLBL )

        self.mainMenuBTN  =  Button ( root , image = mainMenu_btn, command = self.mainMenuBTN_Pressed , bg = "#ffc800" )
        self.mainMenuBTN.place (x = 850 ,y = 60)
        basicWidgetList.append( self.mainMenuBTN )

        self.aboutBTN  =  Button ( root , image = aboutUs_btn, command = self.aboutUsBTN_Pressed, bg = "#ffc800" )
        self.aboutBTN.place (x = 850 ,y = 10)
        basicWidgetList.append( self.aboutBTN )

        self.title1LBL  =  Label( root , text = "Static First Fit"  , font = ('Times New Roman', 20),  bg = "#ffc800")
        self.title1LBL.place(x = 120, y = 20)
        basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Partitioned Allocation" , font = ('Times New Roman', 20),  bg = "#ffc800")
        self.title2LBL.place(x = 75, y = 65)
        basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Partition Set" , font = ('Times New Roman', 20),  bg = "#c6e3ad")
        self.title3LBL.place(x = 140, y = 135)
        basicWidgetList.append( self.title3LBL )
        
        ##
        physicalMemWidgets = []
        self.yCounter = 185
        self.indexPointer = 0
        
        self.markLBL  =  Label( root , text = 0 , font = ('Times New Roman', 10),  bg = "#c6e3ad")
        self.markLBL.place(x = 60, y = self.yCounter - 20)
        physicalMemWidgets.append( self.markLBL )

        self.tempTotalSize = int(osSize)
        self.displayMap( osPercentage, "#f5f3ed", "Os Size", osPercentage, self.tempTotalSize )
                
        self.tempTotalSize = int(osSize) + int(partition1) 
        self.displayMap( partition1Percentage, "#f77777", "Partition 1", partition1Percentage, self.tempTotalSize )
                
        self.tempTotalSize = int(osSize) + int(partition1) + int(partition2)
        self.displayMap( partition2Percentage, "#f7d977", "Partition 2", partition2Percentage, self.tempTotalSize )

        self.tempTotalSize = int(osSize) + int(partition1) + int(partition2) + int(partition3)
        self.displayMap( partition3Percentage, "#77f7e6", "Partition 3", partition3Percentage, self.tempTotalSize )

        self.tempTotalSize = int(osSize) + int(partition1) + int(partition2) + int(partition3) + int(partition4)
        self.displayMap( partition4Percentage, "#77d5f7", "Partition 4", partition4Percentage, self.tempTotalSize )

        self.tempTotalSize = int(osSize) + int(partition1) + int(partition2) + int(partition3) + int(partition4) + int(partition5)
        self.displayMap( partition5Percentage, "#d577f7", "Partition 5", partition5Percentage, self.tempTotalSize )
        ##

        self.osSizeLBL  =  Label( root , text = "OS Size" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.osSizeLBL.place(x = 660, y = 500)
        basicWidgetList.append( self.osSizeLBL )

        self.osSizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.osSizeENTRY.place(x = 625, y = 540)
        self.osSizeENTRY.insert( 0, 312 )
        basicWidgetList.append( self.osSizeENTRY )
        
        self.memSizeLBL  =  Label( root , text = "Memory Size" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.memSizeLBL.place(x = 150, y = 500)
        basicWidgetList.append( self.memSizeLBL )

        self.memSizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.memSizeENTRY.place(x = 130, y = 540)
        self.memSizeENTRY.insert( 0, 1024 )
        basicWidgetList.append( self.memSizeENTRY )

        self.partition1LBL  =  Label( root , text = "Parition 1" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.partition1LBL.place(x = 520, y = 200)
        basicWidgetList.append( self.partition1LBL )

        self.partition1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.partition1ENTRY.place(x = 620, y = 202)
        self.partition1ENTRY.insert( 0, 8 )
        basicWidgetList.append( self.partition1ENTRY )

        self.partition2LBL  =  Label( root , text = "Parition 2" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.partition2LBL.place(x = 520, y = 240)
        basicWidgetList.append( self.partition2LBL )

        self.partition2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.partition2ENTRY.place(x = 620, y = 242)
        self.partition2ENTRY.insert( 0, 32 )
        basicWidgetList.append( self.partition2ENTRY )

        self.partition3LBL  =  Label( root , text = "Parition 3" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.partition3LBL.place(x = 520, y = 280)
        basicWidgetList.append( self.partition3LBL )

        self.partition3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.partition3ENTRY.place(x = 620, y = 282)
        self.partition3ENTRY.insert( 0, 32 )
        basicWidgetList.append( self.partition3ENTRY )

        self.partition4LBL  =  Label( root , text = "Parition 4" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.partition4LBL.place(x = 520, y = 320)
        basicWidgetList.append( self.partition4LBL )

        self.partition4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.partition4ENTRY.place(x = 620, y = 322)
        self.partition4ENTRY.insert( 0, 120 )
        basicWidgetList.append( self.partition4ENTRY )

        self.partition5LBL  =  Label( root , text = "Parition 5" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.partition5LBL.place(x = 520, y = 360)
        basicWidgetList.append( self.partition5LBL )

        self.partition5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.partition5ENTRY.place(x = 620, y = 362)
        self.partition5ENTRY.insert( 0, 520 )
        basicWidgetList.append( self.partition5ENTRY )

        self.setPartitionBTN  =  Button ( root , text = 'Set Partition',command = self.mainInput1_setPartitionBTN_Pressed , font = ('Poppins', 10, 'bold'), width  =  13, bg = "#659bdb" )
        self.setPartitionBTN.place (x = 605 ,y = 405)
        basicWidgetList.append( self.setPartitionBTN )

        self.nextBTN  =  Button ( root , text = 'Next',command = self.mainInput1_nextBTN_Pressed , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.nextBTN.place (x = 390 ,y = 500)
        basicWidgetList.append( self.nextBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 550)
        basicWidgetList.append( self.exitBTN )


    # Generates the result windows using the help of the Node class.
    # This makes use of linked list
    # The start/top of the linked list is referenced at self.headNode
    def createResultWindows( self, allJobSizes, allJobArrivalTime, allJobRunTime, allPartitionSizes):
        global partition1
        global partition2
        global partition3
        global partition4
        global partition5
        global partitionSizes

        global osSize
        global memSize

        global size1
        global size2
        global size3
        global size4
        global size5
        global jobSizes

        global osPercentage
        global partition1Percentage
        global partition2Percentage
        global partition3Percentage
        global partition4Percentage
        global partition5Percentage
        global allPartitionPercentage
        
        self.clearNodes()
        jobSizes = allJobSizes
        #print( jobSizes )
        self.allJobArrivalTime = allJobArrivalTime
        self.allJobRunTime = allJobRunTime
        partitionSizes = allPartitionSizes
        #print( "Create Result Windows" , partitionSizes )
        self.partitionState = [ False, False, False, False, False]
        self.jobState = [ False, False, False, False, False]
        self.partitionHistory = [ [], [], [], [], [] ]
        self.time_zero = datetime.datetime.strptime('00:00', '%H:%M')
        self.allJobResults = [ [], [], [], [], [] ]
        self.patStatus1 = [ ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"]]
        self.patStatus2 = [ ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"]]
        self.allStartTime = []
        self.allFinishTime = []
        for i in range( 5 ):
            for j in range( 5 ):
                if int(partitionSizes[j]) >= int(jobSizes[i]) and self.partitionState[j] == False:
                    self.partitionState[j] = True
                    self.jobState[i] = True
                    #print( self.partitionState )
                    if len(self.partitionHistory[j]) == 0:
                        self.tempStartTime = datetime.datetime.strptime( self.allJobArrivalTime[i] , '%H:%M')
                    else:
                        self.tempStartTime = self.partitionHistory[j][-1]

                    if (self.tempStartTime - datetime.datetime.strptime( self.allJobArrivalTime[i], '%H:%M')).total_seconds() < 0:
                        self.tempCpuWait = "0:00:00"
                        self.tempStartTime = datetime.datetime.strptime( self.allJobArrivalTime[i], '%H:%M')
                    else:
                        self.tempCpuWait = self.tempStartTime - datetime.datetime.strptime( self.allJobArrivalTime[i], '%H:%M')
                        
                    self.allStartTime.append( self.tempStartTime.time() )
                    self.allJobResults[i].append( self.tempStartTime )

                    self.tempFinishTime = ( self.tempStartTime - self.time_zero + (datetime.datetime.strptime(self.allJobRunTime[i], '%H:%M')))
                    self.allFinishTime.append( self.tempFinishTime.time() )
                    self.partitionHistory[j].append( self.tempFinishTime )
                    self.allJobResults[i].append( self.tempFinishTime )

                    self.allJobResults[i].append( self.tempCpuWait )

                    self.allJobResults[i].append( j )
                    self.allJobResults[i].append( i )
                    self.allJobResults[i].append( "After" )
                    
                    self.tempIsAllocated = True
                    #print( "compare: ", int(partitionSizes[j]), int(jobSizes[i]) )
                    break
                    
        #print( self.jobState )

        for i in range( 5 ):
            if self.jobState[i] == False:
                for j in range( 5 ):
                    if int(partitionSizes[j]) >= int(jobSizes[i]):
                        self.partitionState[j] = True
                        self.jobState[i] = True
                        #print( self.partitionState )

                        if len(self.partitionHistory[j]) == 0:
                            self.tempStartTime = datetime.datetime.strptime( self.allJobArrivalTime[i] , '%H:%M')
                        else:
                            self.tempStartTime = self.partitionHistory[j][-1]

                        if (self.tempStartTime - datetime.datetime.strptime( self.allJobArrivalTime[i], '%H:%M')).total_seconds() < 0:
                            self.tempCpuWait = "0:00:00"
                            self.tempStartTime = datetime.datetime.strptime( self.allJobArrivalTime[i], '%H:%M')
                        else:
                            self.tempCpuWait = self.tempStartTime - datetime.datetime.strptime( self.allJobArrivalTime[i], '%H:%M')
                        self.allStartTime.append( self.tempStartTime.time() )
                        self.allJobResults[i].append( self.tempStartTime )

                        self.tempFinishTime = ( self.tempStartTime - self.time_zero + (datetime.datetime.strptime(self.allJobRunTime[i], '%H:%M')))
                        self.allFinishTime.append( self.tempFinishTime.time() )
                        self.partitionHistory[j].append( self.tempFinishTime )
                        self.allJobResults[i].append( self.tempFinishTime )

                        self.allJobResults[i].append( self.tempCpuWait )
                        
                        #print( "compare: ", int(partitionSizes[j]), int(jobSizes[i]) )
                        self.allJobResults[i].append( j )
                        self.allJobResults[i].append( i )
                        self.allJobResults[i].append( "After" )

                        #self.allJobResults = [ [ startTime, finishTime, cpuWait, partitionLocation, job num, before/after ] ]
                        break
        #print( self.jobState )

        # is_time_between(self, begin_time, end_time, check_time=None):


        for i in range( 5 ):
            self.tempCheckTime = self.allJobResults[i][0]
            self.tempCheckTime2 = self.allJobResults[i][1] + datetime.timedelta( seconds = 1)
            for j in range( 5 ):
                self.tempBeginTime = self.allJobResults[j][0]
                self.tempEndTime = self.allJobResults[j][1]
                
                self.tempStatus = self.is_time_between( self.tempBeginTime, self.tempEndTime, self.tempCheckTime )
                self.tempStatus2 = self.is_time_between( self.tempBeginTime, self.tempEndTime, self.tempCheckTime2 )
                if self.tempStatus == True:
                    #print ( "X", self.tempBeginTime, self.tempEndTime, self.tempCheckTime )
                    #print( self.allJobResults[j][3] , self.allJobResults[j][4] )
                    self.patStatus1[i][self.allJobResults[j][3]] = "Allocated(J{})".format(self.allJobResults[j][4] + 1)
                if self.tempStatus2 == True:
                    self.patStatus2[i][self.allJobResults[j][3]] = "Allocated(J{})".format(self.allJobResults[j][4] + 1)          
        for x in self.allJobResults:
            for xx in x:
                pass
                #print( xx )


        self.addResultNode( self.allFinishTime[4], self.patStatus2[4], "After", "J5 Terminated" )
        self.addResultNode( self.allStartTime[4], self.patStatus1[4], "At", "J5 Started" )

        self.addResultNode( self.allFinishTime[3], self.patStatus2[3], "After", "J4 Terminated" )
        self.addResultNode( self.allStartTime[3], self.patStatus1[3], "At", "J4 Started" )

        self.addResultNode( self.allFinishTime[2], self.patStatus2[2], "After", "J3 Terminated" )
        self.addResultNode( self.allStartTime[2], self.patStatus1[2], "At", "J3 Started" )

        self.addResultNode( self.allFinishTime[1], self.patStatus2[1], "After", "J2 Terminated" )
        self.addResultNode( self.allStartTime[1], self.patStatus1[1], "At", "J2 Started" )

        self.addResultNode( self.allFinishTime[0], self.patStatus2[0], "After", "J1 Terminated" )
        self.addResultNode( self.allStartTime[0], self.patStatus1[0], "At", "J1 Started" )
        
        self.mainResult1_window()


    # This function is for most of the necessary computations
    def mainInput2_computePressed( self ):
        global partition1
        global partition2
        global partition3
        global partition4
        global partition5
        global partitionSizes

        global osSize
        global memSize

        global size1
        global size2
        global size3
        global size4
        global size5
        global jobSizes

        global osPercentage
        global partition1Percentage
        global partition2Percentage
        global partition3Percentage
        global partition4Percentage
        global partition5Percentage
        global allPartitionPercentage
        if messagebox.askyesno( "Confirmation..." , " Are you sure you want to compute? " ) == True :
            size1 = self.size1ENTRY.get()
            size2 = self.size2ENTRY.get()
            size3 = self.size3ENTRY.get()
            size4 = self.size4ENTRY.get()
            size5 = self.size5ENTRY.get()

            #print ( "Main Input2" , partitionSizes )
 
            self.size1_Check = self.isNotInteger( size1 )
            self.size2_Check = self.isNotInteger( size2 )
            self.size3_Check = self.isNotInteger( size3 )
            self.size4_Check = self.isNotInteger( size4 )
            self.size5_Check = self.isNotInteger( size5 )

            self.size1_Check2 = self.cantFitInPartition( size1 )
            self.size2_Check2 = self.cantFitInPartition( size2 )
            self.size3_Check2 = self.cantFitInPartition( size3 )
            self.size4_Check2 = self.cantFitInPartition( size4 )
            self.size5_Check2 = self.cantFitInPartition( size5 )
            
            
            self.arrivalTime1 = self.arrivalTime1ENTRY.get()
            self.arrivalTime2 = self.arrivalTime2ENTRY.get()
            self.arrivalTime3 = self.arrivalTime3ENTRY.get()
            self.arrivalTime4 = self.arrivalTime4ENTRY.get()
            self.arrivalTime5 = self.arrivalTime5ENTRY.get()

            self.arrivalTime1_Check = self.isNotTimeFormat( self.arrivalTime1 )
            self.arrivalTime2_Check = self.isNotTimeFormat( self.arrivalTime2 )
            self.arrivalTime3_Check = self.isNotTimeFormat( self.arrivalTime3 )
            self.arrivalTime4_Check = self.isNotTimeFormat( self.arrivalTime4 )
            self.arrivalTime5_Check = self.isNotTimeFormat( self.arrivalTime5 )

            self.runTime1 = self.runTime1ENTRY.get()
            self.runTime2 = self.runTime2ENTRY.get()
            self.runTime3 = self.runTime3ENTRY.get()
            self.runTime4 = self.runTime4ENTRY.get()
            self.runTime5 = self.runTime5ENTRY.get()
        
            self.runTime1_Check = self.isNotTimeFormat( self.runTime1 )
            self.runTime2_Check = self.isNotTimeFormat( self.runTime2 )
            self.runTime3_Check = self.isNotTimeFormat( self.runTime3 )
            self.runTime4_Check = self.isNotTimeFormat( self.runTime4 )
            self.runTime5_Check = self.isNotTimeFormat( self.runTime5 )

            if self.size1_Check or self.size2_Check or self.size3_Check or self.size4_Check or self.size5_Check:
                #print ( "Error: Size input detected as not an integer." )
                messagebox.showinfo( "Compute Error" , "Error: Size input detected as not an integer." )
            elif self.size1_Check2:
                #print ( "Error: Size 1 input can't fit in any partition." )
                messagebox.showinfo( "Compute Error" , "Error: Size 1 input can't fit in any partition." )
            elif self.size2_Check2:
                #print ( "Error: Size 2 input can't fit in any partition." )
                messagebox.showinfo( "Compute Error" , "Error: Size 2 input can't fit in any partition." )
            elif self.size3_Check2:
                #print ( "Error: Size 3 input can't fit in any partition." )
                messagebox.showinfo( "Compute Error" , "Error: Size 3 input can't fit in any partition." )
            elif self.size4_Check2:
                #print ( "Error: Size 4 input can't fit in any partition." )
                messagebox.showinfo( "Compute Error" , "Error: Size 4 input can't fit in any partition." )
            elif self.size5_Check2:
                #print ( "Error: Size 5 input can't fit in any partition." )
                messagebox.showinfo( "Compute Error" , "Error: Size 5 input can't fit in any partition." )
            elif self.arrivalTime1_Check or self.arrivalTime2_Check or self.arrivalTime3_Check or self.arrivalTime4_Check or self.arrivalTime5_Check:
                #print ( " Error in arrival time input " )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Arrival Time Input." )
            elif self.runTime1_Check or self.runTime2_Check or self.runTime3_Check or self.runTime4_Check or self.runTime5_Check:
                #print ( "Error: Invalid Run Time Input." )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Run Time Input." )
            else:
                size1 = int(size1)
                size2 = int(size2)
                size3 = int(size3)
                size4 = int(size4)
                size5 = int(size5)
                jobSizes = [ size1, size2, size3, size4, size5 ]
                #print( jobSizes )
                self.allJobArrivalTime = [ self.arrivalTime1, self.arrivalTime2, self.arrivalTime3, self.arrivalTime4, self.arrivalTime5 ]
                self.allJobRunTime = [ self.runTime1, self.runTime2, self.runTime3, self.runTime4, self.runTime5 ]
                self.createResultWindows( jobSizes, self.allJobArrivalTime, self.allJobRunTime, partitionSizes )
                #print( "success" )


    # For taking user's input of each job's information
    def mainInput2_window ( self ):
        self.clearWidgets()
        basicWidgetList = []
        
        self.staticPartitionedBG = Label ( root , image = spa_bg, bg = "black" )
        self.staticPartitionedBG.place(x = 0, y = 0)
        basicWidgetList.append( self.staticPartitionedBG )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffc800" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffc800")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        basicWidgetList.append( self.dateLBL )
        
        self.title1LBL  =  Label( root , text = "Static First Fit"  , font = ('Times New Roman', 20),  bg = "#ffc800")
        self.title1LBL.place(x = 120, y = 20)
        basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Partitioned Allocation" , font = ('Times New Roman', 20),  bg = "#ffc800")
        self.title2LBL.place(x = 75, y = 65)
        basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Input Window" , font = ('Times New Roman', 30),  bg = "#c6e3ad")
        self.title3LBL.place(x = 355, y = 105)
        basicWidgetList.append( self.title3LBL )

        self.jobLBL  =  Label( root , text = "Job" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.jobLBL.place(x = 125, y = 160)
        basicWidgetList.append( self.jobLBL )

        self.job1LBL  =  Label( root , text = "1" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job1LBL.place(x = 135, y = 210)
        basicWidgetList.append( self.job1LBL )
        
        self.job2LBL  =  Label( root , text = "2" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job2LBL.place(x = 135, y = 260)
        basicWidgetList.append( self.job2LBL )
        
        self.job3LBL  =  Label( root , text = "3" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job3LBL.place(x = 135, y = 310)
        basicWidgetList.append( self.job3LBL )

        self.job4LBL  =  Label( root , text = "4" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job4LBL.place(x = 135, y = 360)
        basicWidgetList.append( self.job4LBL )
        
        self.job5LBL  =  Label( root , text = "5" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job5LBL.place(x = 135, y = 410)
        basicWidgetList.append( self.job5LBL )
        
        self.sizeLBL  =  Label( root , text = "Size" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.sizeLBL.place(x = 275, y = 160)
        basicWidgetList.append( self.sizeLBL )
        
        self.size1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size1ENTRY.place(x = 225, y = 210)
        basicWidgetList.append( self.size1ENTRY )
        
        self.size2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size2ENTRY.place(x = 225, y = 260)
        basicWidgetList.append( self.size2ENTRY )
        
        self.size3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size3ENTRY.place(x = 225, y = 310)
        basicWidgetList.append( self.size3ENTRY )

        self.size4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size4ENTRY.place(x = 225, y = 360)
        basicWidgetList.append( self.size4ENTRY )
        
        self.size5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size5ENTRY.place(x = 225, y = 410)
        basicWidgetList.append( self.size5ENTRY )
        
        
        self.arrivalTimeLBL  =  Label( root , text = "Arrival Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.arrivalTimeLBL.place(x = 505, y = 160)
        basicWidgetList.append( self.arrivalTimeLBL )

        self.arrivalTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime1ENTRY.place(x = 490, y = 210)
        basicWidgetList.append( self.arrivalTime1ENTRY )
        
        self.arrivalTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime2ENTRY.place(x = 490, y = 260)
        basicWidgetList.append( self.arrivalTime2ENTRY )
        
        self.arrivalTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime3ENTRY.place(x = 490, y = 310)
        basicWidgetList.append( self.arrivalTime3ENTRY )

        self.arrivalTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime4ENTRY.place(x = 490, y = 360)
        basicWidgetList.append( self.arrivalTime4ENTRY )
        
        self.arrivalTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime5ENTRY.place(x = 490, y = 410)
        basicWidgetList.append( self.arrivalTime5ENTRY )
        
        self.runTimeLBL  =  Label( root , text = "Run Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.runTimeLBL.place(x = 725, y = 160)
        basicWidgetList.append( self.runTimeLBL )
        
        self.runTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.runTime1ENTRY.place(x = 700, y = 210)
        basicWidgetList.append( self.runTime1ENTRY )
        
        self.runTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.runTime2ENTRY.place(x = 700, y = 260)
        basicWidgetList.append( self.runTime2ENTRY )
        
        self.runTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.runTime3ENTRY.place(x = 700, y = 310)
        basicWidgetList.append( self.runTime3ENTRY )

        self.runTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.runTime4ENTRY.place(x = 700, y = 360)
        basicWidgetList.append( self.runTime4ENTRY )
        
        self.runTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.runTime5ENTRY.place(x = 700, y = 410)
        basicWidgetList.append( self.runTime5ENTRY )
        
        self.computeBTN  =  Button ( root , text = 'Compute',command = self.mainInput2_computePressed , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.computeBTN.place (x = 390 ,y = 460)
        basicWidgetList.append( self.computeBTN )

        self.backBTN  =  Button ( root , text = 'Back',command = self.mainInput1_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 390 ,y = 510)
        basicWidgetList.append( self.backBTN )


    # This function points to the headNode's memMap_window
    def mainResult1_nextBTN_Pressed( self ):
        if self.headNode != None:
            self.headNode.memMap_window()


    # For displaying the summary table
    def mainResult1_window( self ):
        self.clearWidgets()
        basicWidgetList = []
        
        self.staticPartitionedBG = Label ( root , image = spa_bg, bg = "black" )
        self.staticPartitionedBG.place(x = 0, y = 0)
        basicWidgetList.append( self.staticPartitionedBG )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffc800" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffc800")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        basicWidgetList.append( self.dateLBL )
        
        self.title1LBL  =  Label( root , text = "Static First Fit"  , font = ('Times New Roman', 20),  bg = "#ffc800")
        self.title1LBL.place(x = 120, y = 20)
        basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Partitioned Allocation" , font = ('Times New Roman', 20),  bg = "#ffc800")
        self.title2LBL.place(x = 75, y = 65)
        basicWidgetList.append( self.title2LBL )

        self.jobLBL  =  Label( root , text = "Job" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.jobLBL.place(x = 112, y = 130)
        basicWidgetList.append( self.jobLBL )

        self.job1LBL  =  Label( root , text = "1" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job1LBL.place(x = 120, y = 190)
        basicWidgetList.append( self.job1LBL )
        
        self.job2LBL  =  Label( root , text = "2" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job2LBL.place(x = 120, y = 250)
        basicWidgetList.append( self.job2LBL )
        
        self.job3LBL  =  Label( root , text = "3" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job3LBL.place(x = 120, y = 310)
        basicWidgetList.append( self.job3LBL )
        
        self.job4LBL  =  Label( root , text = "4" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job4LBL.place(x = 120, y = 370)
        basicWidgetList.append( self.job4LBL )
        
        self.job5LBL  =  Label( root , text = "5" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job5LBL.place(x = 120, y = 430)
        basicWidgetList.append( self.job5LBL )
        
        self.startTimeLBL  =  Label( root , text = "Start Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.startTimeLBL.place(x = 250, y = 130)
        basicWidgetList.append( self.startTimeLBL )
        
        self.startTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.startTime1ENTRY.place(x = 225, y = 190)
        self.startTime1ENTRY.insert( 0, self.allJobResults[0][0].time() )
        self.startTime1ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.startTime1ENTRY )
        
        self.startTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.startTime2ENTRY.place(x = 225, y = 250)
        self.startTime2ENTRY.insert( 0, self.allJobResults[1][0].time() )
        self.startTime2ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.startTime2ENTRY )
        
        self.startTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.startTime3ENTRY.place(x = 225, y = 310)
        self.startTime3ENTRY.insert( 0, self.allJobResults[2][0].time() )
        self.startTime3ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.startTime3ENTRY )
        
        self.startTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.startTime4ENTRY.place(x = 225, y = 370)
        self.startTime4ENTRY.insert( 0, self.allJobResults[3][0].time() )
        self.startTime4ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.startTime4ENTRY )
        
        self.startTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.startTime5ENTRY.place(x = 225, y = 430)
        self.startTime5ENTRY.insert( 0, self.allJobResults[4][0].time() )
        self.startTime5ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.startTime5ENTRY )

        self.finishTimeLBL  =  Label( root , text = "Finish Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.finishTimeLBL.place(x = 512, y = 130)
        basicWidgetList.append( self.finishTimeLBL )

        self.finishTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.finishTime1ENTRY.place(x = 490, y = 190)
        self.finishTime1ENTRY.insert( 0, self.allJobResults[0][1].time() )
        self.finishTime1ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.finishTime1ENTRY )
        
        self.finishTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.finishTime2ENTRY.place(x = 490, y = 250)
        self.finishTime2ENTRY.insert( 0, self.allJobResults[1][1].time() )
        self.finishTime2ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.finishTime2ENTRY )
        
        self.finishTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.finishTime3ENTRY.place(x = 490, y = 310)
        self.finishTime3ENTRY.insert( 0, self.allJobResults[2][1].time() )
        self.finishTime3ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.finishTime3ENTRY )
        
        self.finishTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.finishTime4ENTRY.place(x = 490, y = 370)
        self.finishTime4ENTRY.insert( 0, self.allJobResults[3][1].time() )
        self.finishTime4ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.finishTime4ENTRY )
        
        self.finishTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.finishTime5ENTRY.place(x = 490, y = 430)
        self.finishTime5ENTRY.insert( 0, self.allJobResults[4][1].time() )
        self.finishTime5ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.finishTime5ENTRY )
        
        self.cpuWaitLBL  =  Label( root , text = "CPU Wait" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.cpuWaitLBL.place(x = 725, y = 130)
        basicWidgetList.append( self.cpuWaitLBL )
        
        self.cpuWait1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuWait1ENTRY.place(x = 700, y = 190)
        self.cpuWait1ENTRY.insert( 0, self.allJobResults[0][2] )
        self.cpuWait1ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.cpuWait1ENTRY )
        
        self.cpuWait2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuWait2ENTRY.place(x = 700, y = 250)
        self.cpuWait2ENTRY.insert( 0, self.allJobResults[1][2] )
        self.cpuWait2ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.cpuWait2ENTRY )
        
        self.cpuWait3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuWait3ENTRY.place(x = 700, y = 310)
        self.cpuWait3ENTRY.insert( 0, self.allJobResults[2][2] )
        self.cpuWait3ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.cpuWait3ENTRY )
        
        self.cpuWait4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuWait4ENTRY.place(x = 700, y = 370)
        self.cpuWait4ENTRY.insert( 0, self.allJobResults[3][2] )
        self.cpuWait4ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.cpuWait4ENTRY )
        
        self.cpuWait5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuWait5ENTRY.place(x = 700, y = 430)
        self.cpuWait5ENTRY.insert( 0, self.allJobResults[4][2] )
        self.cpuWait5ENTRY.config( state = "readonly" )
        basicWidgetList.append( self.cpuWait5ENTRY )

        self.backBTN  =  Button ( root , text = 'BACK',command = self.mainInput2_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 300 ,y = 500)
        basicWidgetList.append( self.backBTN )
        self.nextBTN  =  Button ( root , text = 'NEXT',command = self.mainResult1_nextBTN_Pressed , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.nextBTN.place (x = 480 ,y = 500)
        basicWidgetList.append( self.nextBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 550)
        basicWidgetList.append( self.exitBTN )
# END OF SPA PROGRAM: line 1340-2838


# DFF PROGRAM: Line 2847-4428
# All the back end processes are hosted in this class.
class dynamic_firstFit_backEnd:
    def __init__( self ):
        self.time_zero = datetime.datetime.strptime('00:00', '%H:%M')
        # summary table [ jobNum, startTime, finishTime, cpuWait ]
        self.summaryTable = {}
        self.allTime = []
        
        # Job Status [ allocated(True/False), finished(True/False), waiting ]
        self.jobStatus = { 1 : [ False, False, False ],
                           2 : [ False, False, False ],
                           3 : [ False, False, False ],
                           4 : [ False, False, False ],
                           5 : [ False, False, False ]}
        self.memoryResults = []
        self.memoryResults_time = []

    # for taking in the user's input into the backEnd class.
    def insert_inputs( self, memSpace, osSpace, jobDetails, memory ):
        #print( "INPUTS: " )
        #print ( "I1" , jobDetails )
        #print( "I2", memory )
        self.memSpace = int(memSpace)
        self.osSpace = int(osSpace)
        self.memSize = int( memSpace)
        self.osSpace = int( osSpace )
        self.jobDetails = deepcopy( jobDetails )
        self.memory = deepcopy( memory )

        self.summaryTable = {}
        self.allTime = []
        # generates the all time list which will contain all the time that needs a memory map, fat, and pat.
        for job in self.jobDetails:
            self.tempTime = datetime.datetime.strptime( job[2], '%H:%M')
            self.allTime.append( self.tempTime )

        # job status [ isJobAllocated, isJobFinished, isJobWaiting ]
        self.jobStatus = { 1 : [ False, False, False ],
                           2 : [ False, False, False ],
                           3 : [ False, False, False ],
                           4 : [ False, False, False ],
                           5 : [ False, False, False ]}

        # memoryResult will be used to store the data for every memory map.
        self.memoryResults = []
        # memoryResult_time will be used to store the time of every memory map.
        self.memoryResults_time = []
        return

    # returns memory list
    def get_memory( self ):
        return self.memory

    # returns summaryTable
    def get_summaryTable( self ):
        return self.summaryTable

    # returns the memoryResults
    def get_memoryResults( self ):
        return self.memoryResults

    # returns the memoryResults_time
    def get_memoryResults_time( self ):
        return self.memoryResults_time

    # for appending a certain memory list into the memory result
    def add_memoryResult( self, memory, time, timeStatus) :
        self.memoryResults.append( memory )
        self.memoryResults_time.append( [time, timeStatus] )
        return

    # sorts the list containing all the time that needs a memory result.
    def arrange_allTime( self ):
        self.allTime.sort()
        return

    # remove's the time that already have a memory result.
    def remove_time( self, time ):
        try:
            while True:
                self.allTime.remove(time)
        except ValueError:
            pass
        self.arrange_allTime()
        return

    # checks if the job fits into the available partitions.
    def check_jobFit( self, j_size ):
        # j_size: job size
        self.j_size = j_size
        # memorySpace[1]: F for free/available space and U if occupied by a certain job
        # memorySpace[0]: the size of the partition.
        for memorySpace in self.memory:
            if memorySpace[1] == "F" and memorySpace[0] > self.j_size:
                return True
        return False

    # checks a certain job's status.
    def check_jobStatus( self ):
        # checks if the jobs are already done.
        self.jobsDone = 0
        for jobNum in list(self.jobStatus):
            if self.jobStatus[jobNum][0] == True and self.jobStatus[jobNum][1]:
                self.jobsDone += 1
        if self.jobsDone == len( list(self.jobStatus) ):
            return True
        else:
            return False

    # allocates a job into a free/available partition.
    def allocate( self, memory, job ):
        # job [ job id, a/f( allocate/deallocate ), job size ]
        self.j_id = job[0]
        self.j_size = job[2]
        self.allocate_memory = memory
        # if the memory list is empty, immediately return
        if self.allocate_memory == None:
            return self.allocate_memory
        # i: id for the memory space/partition
        # m: F for free/available memory space,
        #    U for occupied memory space.
        # This loop traverses the memory list so that a job can be allocated to the 
        # first memory space which meets the needs of the job.
        for i, m in enumerate(self.allocate_memory):
            if m[1] == "F" and m[0] > self.j_size:
                self.allocate_memory.insert( i + 1, [m[0] - self.j_size, "F", -1])
                try:
                    if self.allocate_memory[i+2][1] == "F":
                        self.allocate_memory[i+1][0] += self.allocate_memory[i+2][0]
                        self.allocate_memory.pop(i+2)
                except IndexError:
                    pass

                m[0] = self.j_size
                m[1] = "U"
                m[2] = self.j_id
                return self.allocate_memory

    # for de-allocating a job out of the memory list.
    def recycle( self, memory, job ):
        self.recycle_memory = memory
        self.job = job
        # if the memory list is empty, immediately return
        if self.recycle_memory == None:
            return
        # i: id for the memory space/partition
        # m: F for free/available memory space,
        #    U for occupied memory space.
        # This loop traverses the memory list to de-allocate a job from the memory list
        # Furthermore, it also combines free memory spaces that are side by side.
        for i, m in enumerate( self.recycle_memory ):
            if m[2] == self.job[0] and m[1] == "U":
                m[1] = "F"
                m[2] = -1
                if i != 0 and self.recycle_memory[i-1][1] == "F":
                    self.recycle_memory[i-1][0] += m[0]
                    self.recycle_memory.remove(m)
                    if self.recycle_memory[i][1] == "F":
                        self.recycle_memory[i-1][0] += self.recycle_memory[i][0]
                        self.recycle_memory.pop(i)
                elif i != len(self.recycle_memory) and self.recycle_memory[i+1][1] == "F":
                    self.recycle_memory[i][0] += self.recycle_memory[i+1][0]
                    self.recycle_memory.remove( self.recycle_memory[i+1] )
        return self.recycle_memory
    
    # for generating the summary table.
    def generate_summaryTable( self ):
        self.isFinished = False
        self.arrange_allTime()
        
        while self.isFinished == False:
            # This block of code sets the needed parameters for the next process.
            # It resets the indicator 'actionTaken'. This indicator is used by the
            # program to determine if a job has been allocated/de-allocated in this iteration.
            # tempTimeStatus: contains the status of certain time periods. This could contain
            #                 job arrivals, job waiting, and job terminations.
            # currentTime: the time of a certain/this iteration.
            self.actionTaken = False
            self.tempTimeStatus = []
            try:
                self.arrange_allTime()
                self.currentTime = self.allTime[0]
            except:
                self.isFinished = True
                break

            # Checks if all the jobs are already finished. If it is, then stop the while loop.
            self.tempJobStatus = self.check_jobStatus()
            if self.tempJobStatus == True:
                self.isFinished = True
                break

            # Iterates through the job details to see what actions can be taken in this currentTime
            for job in self.jobDetails:
                self.jobFits = self.check_jobFit( job[0] )
                self.test_jobWaiting = True
                
                # If a certain job details from the self.jobDetails is deemed to waiting to be allocated
                # then, it will check if the currentTime meets the job's demand for allocation.
                if job[4] != False:
                    self.tempWaitUntil = job[4]
                    if self.currentTime == self.tempWaitUntil:
                        self.test_jobWaiting = False

                # If a certain job arrives, this nested condition will check whether the job needs to wait or is capable
                # of immediate allocation.
                if self.currentTime == datetime.datetime.strptime( job[2], '%H:%M') and self.jobStatus[job[1]][0] == False:
                    if self.jobFits == True:
                        self.tempTimeStatus.append( "Arrived(J{})".format( job[1] ) )
                    else:
                        self.tempTimeStatus.append( "Arrived/Wait(J{})".format( job[1] ) )
                        self.tempWaitUntil = self.tempFinishTime
                        job[4] = self.tempWaitUntil

                # This conditions checks if a certain actions could be taken.
                # The actions could be, the start/allocation or termination of certain job.
                if ( self.test_jobWaiting == False or self.currentTime == datetime.datetime.strptime( job[2], '%H:%M')) and self.jobStatus[job[1]][0] == False and self.jobFits == True:
                    self.memory = self.allocate( self.memory, [ job[1], "a" , job[0] ] )
                    self.jobStatus[job[1]][0] = True

                    self.tempStartTime = self.currentTime
                    if (self.tempStartTime - datetime.datetime.strptime( job[2], '%H:%M')).total_seconds() < 0:
                        self.tempCpuWait = "0:00:00"
                        self.tempStartTime = datetime.datetime.strptime( job[2], '%H:%M')
                    else:
                        self.tempCpuWait = self.tempStartTime - datetime.datetime.strptime( job[2], '%H:%M')
                    self.tempFinishTime = ( self.tempStartTime - self.time_zero + (datetime.datetime.strptime( job[3], '%H:%M')))
                    self.allTime.append( self.tempFinishTime )
                    self.summaryTable[job[1]] = [ job[1], self.tempStartTime, self.tempFinishTime, self.tempCpuWait ]

                    self.actionTaken = True
                    self.tempTimeStatus.append( "Started(J{})".format( job[1] ) )
                elif self.jobStatus[job[1]][0] == True and self.currentTime == self.summaryTable[job[1]][2]:
                    self.memory = self.recycle( self.memory, [ job[1], "f" , job[0] ] )
                    self.jobStatus[job[1]][1] = True
                    
                    self.actionTaken = True
                    self.tempTimeStatus.append( "Terminated(J{})".format( job[1] ) )
                else:
                    pass

            # copies the memory list of this currentTime
            self.memoryToAdd = deepcopy(self.memory)
            # appds the needed data into the memoryResult list.
            self.add_memoryResult( self.memoryToAdd, self.currentTime, deepcopy(self.tempTimeStatus) )

            # Checks if all the job are already finished. If not, then remove the current time from
            # the list of all time.
            self.tempJobStatus = self.check_jobStatus()
            if self.tempJobStatus == True:
                self.isFinished = True
                break
            else:
                self.remove_time( self.currentTime )


# Contains all the front end windows and functions
class dynamic_firstFit_frontEnd:
    def __init__( self ):
        self.memSpace = 640
        self.memSize = 640
        self.osSpace = 32
        self.osSize = 32
        # Job Details [ jobSize, jobNum, arrivalTime, runTime, isjobWaiting ]
        self.jobDetails = [ [ 10, 1, "9:00", "1:00", False],
                            [ 20, 2, "9:00", "1:00", False],
                            [ 30, 3, "9:00", "1:00", False],
                            [ 40, 4, "9:00", "1:00", False],
                            [ 50, 5, "9:00", "1:00", False]]

        self.memory = [[609,'F',-1]]
        
        self.firstFit_backEnd = dynamic_firstFit_backEnd()

        # insert_inputs( self, memSpace, osSpace, jobDetails, memory )
        self.firstFit_backEnd.insert_inputs( self.memSpace, self.osSpace, self.jobDetails, self.memory )
        self.firstFit_backEnd.generate_summaryTable()

        self.headNode = None

    # To clear the linked list of nodes.
    def clearNodes( self ):
        self.headNode = None
        return

    # To add a node into the linked list
    # ( self, memoryResult = None, memoryResult_time = None, osSize = None, memSize = None)
    def addResultNode( self, memoryResult, memoryResult_time, osSize, memSize ):
        memoryResult_time[0] = memoryResult_time[0].time()
        self.tempNode = dynamic_firstFitNode_frontEnd( memoryResult, memoryResult_time, osSize, memSize )

        if self.headNode == None:
            self.headNode = self.tempNode
        else:
            self.headNode.backPointer = self.tempNode
            self.tempNode.nextPointer = self.headNode

            self.headNode = self.tempNode
        return


    # For getting the current date
    def current_date( self ):
        self.dateString  =  datetime.date.today().strftime("%B %d, %Y")
        self.dateLBL.config(text = self.dateString)

    
    # This updates the clock widget
    def tick( self ):
        if self.tick_on:
            self.timeString  =  time.strftime("%H:%M:%S")
            self.clockLBL.config(text = self.timeString)
            self.clockLBL.after(200, self.tick )
        else:
            pass


    # This function returns True if timeInput is not in proper time format
    # Else, returns False if the input is in proper time format
    # Time format is HH:MM
    def isNotTimeFormat( self, timeInput):
        try:
            time.strptime( timeInput, '%H:%M')
            return False
        except ValueError:
            return True

    # This function returns True if the integerInput is not an Integer.
    # If it is an integer, return False.
    def isNotInteger( self, integerInput):
        try:
            self.intTest = int(integerInput)
            return False
        except ValueError:
            return True

    # The program has two list which contains a reference to all the program's widgets
    # And what this function does is it tries to clear/destroy all of these widgets
    # using the lists which contains the program's widgets.
    # The two lists are:
    #   - self.basicWidgetList: For most of the basic widgets
    #   - self.physicalMemWidgets: For the widgets used to display physical memory map
    def clearWidgets( self ):
        try:
            self.tick_on = False
            self.clearWidgetList( self.basicWidgetList )
            self.clearWidgetList( self.physicalMemWidgets )
        except:
            pass
        return


    # This function destroys all of the widgets inside the inputted widgetsToClear list.
    def clearWidgetList ( self, widgetsToClear):
        for widget in widgetsToClear:
            widget.destroy()

    # This function displays the necessary widgets for physical memory map.
    # To get a general gist, the program has around 50 labels which acts as the physical memory map.
    # In addition, it has a text label which marks each section of the physical memory map.
    def displayMap( self, tempPointer, tempColor, tempText, tempPercentage, tempTotalSize ):
        self.tempPointer = int(tempPointer)
        self.tempColor = tempColor
        self.tempText = tempText
        self.tempPercentage = tempPercentage
        self.tempTotalSize = tempTotalSize
        
        if self.tempPercentage != 0:
            self.tempLBL = Label( root , text = "          " * 25 , font = ('Times New Roman', 1),  bg = self.tempColor)
            self.tempLBL.place(x = 80, y = self.yCounter)
            self.yCounter += 7
            self.physicalMemWidgets.append( self.tempLBL )
            
            self.tempLBL = Label( root , text = self.tempText , font = ('Times New Roman', 10),  bg = self.tempColor)
            self.tempLBL.place(x = 350, y = self.yCounter)
            self.physicalMemWidgets.append( self.tempLBL )
        for i in range( int( self.tempPercentage / 2 ) ):
            if self.tempPointer != 0:
                self.tempLBL = Label( root , text = "          " * 25 , font = ('Times New Roman', 1),  bg = self.tempColor)
                self.tempLBL.place(x = 80, y = self.yCounter)
                self.yCounter += 7
                self.physicalMemWidgets.append( self.tempLBL )
                self.tempPointer -= 1
            else:
                pass
        if self.tempPercentage != 0:
            self.tempLBL  =  Label( root , text = tempTotalSize , font = ('Times New Roman', 10),  bg = self.tempColor)
            self.tempLBL.place(x = 50, y = self.yCounter - 15)
            self.physicalMemWidgets.append( self.tempLBL )
        return

    def mainMenuBTN_Pressed( self ):
        main.mainMenu_window()

    def aboutUsBTN_Pressed( self ):
        main.aboutUs_window()


    # function which contains widget placements
    # this also takes in the user's input.
    def input1_window( self ):
        root.title ( "Dynamic First Fit" )
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.dynamicFirstFitBG = Label ( root , image = dff_bg, bg = "black" )
        self.dynamicFirstFitBG.place(x = 0, y = 0)
        self.basicWidgetList.append( self.dynamicFirstFitBG )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffff01" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffff01")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )

        self.mainMenuBTN  =  Button ( root , image = mainMenu_btn, command = self.mainMenuBTN_Pressed , bg = "#ffff01" )
        self.mainMenuBTN.place (x = 850 ,y = 60)
        self.basicWidgetList.append( self.mainMenuBTN )

        self.aboutBTN  =  Button ( root , image = aboutUs_btn, command = self.aboutUsBTN_Pressed, bg = "#ffff01" )
        self.aboutBTN.place (x = 850 ,y = 10)
        self.basicWidgetList.append( self.aboutBTN )
        
        self.title1LBL  =  Label( root , text = "First Fit Dynamic" , font = ('Times New Roman', 20),  bg = "#ffff01")
        self.title1LBL.place(x = 100, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Partitioned Allocation" , font = ('Times New Roman', 20),  bg = "#ffff01")
        self.title2LBL.place(x = 75, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Input Window" , font = ('Times New Roman', 30),  bg = "#c6e3ad")
        self.title3LBL.place(x = 355, y = 105)
        self.basicWidgetList.append( self.title3LBL )

        self.jobLBL  =  Label( root , text = "Job" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.jobLBL.place(x = 125, y = 160)
        self.basicWidgetList.append( self.jobLBL )

        self.job1LBL  =  Label( root , text = "1" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job1LBL.place(x = 135, y = 210)
        self.basicWidgetList.append( self.job1LBL )
        
        self.job2LBL  =  Label( root , text = "2" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job2LBL.place(x = 135, y = 260)
        self.basicWidgetList.append( self.job2LBL )
        
        self.job3LBL  =  Label( root , text = "3" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job3LBL.place(x = 135, y = 310)
        self.basicWidgetList.append( self.job3LBL )

        self.job4LBL  =  Label( root , text = "4" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job4LBL.place(x = 135, y = 360)
        self.basicWidgetList.append( self.job4LBL )
        
        self.job5LBL  =  Label( root , text = "5" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job5LBL.place(x = 135, y = 410)
        self.basicWidgetList.append( self.job5LBL )
        
        self.sizeLBL  =  Label( root , text = "Size" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.sizeLBL.place(x = 275, y = 160)
        self.basicWidgetList.append( self.sizeLBL )
        
        self.size1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size1ENTRY.place(x = 225, y = 210)
        self.basicWidgetList.append( self.size1ENTRY )
        
        self.size2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size2ENTRY.place(x = 225, y = 260)
        self.basicWidgetList.append( self.size2ENTRY )
        
        self.size3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size3ENTRY.place(x = 225, y = 310)
        self.basicWidgetList.append( self.size3ENTRY )

        self.size4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size4ENTRY.place(x = 225, y = 360)
        self.basicWidgetList.append( self.size4ENTRY )
        
        self.size5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size5ENTRY.place(x = 225, y = 410)
        self.basicWidgetList.append( self.size5ENTRY )
        
        
        self.arrivalTimeLBL  =  Label( root , text = "Arrival Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.arrivalTimeLBL.place(x = 505, y = 160)
        self.basicWidgetList.append( self.arrivalTimeLBL )

        self.arrivalTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime1ENTRY.place(x = 490, y = 210)
        self.basicWidgetList.append( self.arrivalTime1ENTRY )
        
        self.arrivalTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime2ENTRY.place(x = 490, y = 260)
        self.basicWidgetList.append( self.arrivalTime2ENTRY )
        
        self.arrivalTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime3ENTRY.place(x = 490, y = 310)
        self.basicWidgetList.append( self.arrivalTime3ENTRY )

        self.arrivalTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime4ENTRY.place(x = 490, y = 360)
        self.basicWidgetList.append( self.arrivalTime4ENTRY )
        
        self.arrivalTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime5ENTRY.place(x = 490, y = 410)
        self.basicWidgetList.append( self.arrivalTime5ENTRY )
        
        self.runTimeLBL  =  Label( root , text = "Run Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.runTimeLBL.place(x = 725, y = 160)
        self.basicWidgetList.append( self.runTimeLBL )
        
        self.runTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.runTime1ENTRY.place(x = 700, y = 210)
        self.basicWidgetList.append( self.runTime1ENTRY )
        
        self.runTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.runTime2ENTRY.place(x = 700, y = 260)
        self.basicWidgetList.append( self.runTime2ENTRY )
        
        self.runTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.runTime3ENTRY.place(x = 700, y = 310)
        self.basicWidgetList.append( self.runTime3ENTRY )

        self.runTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.runTime4ENTRY.place(x = 700, y = 360)
        self.basicWidgetList.append( self.runTime4ENTRY )
        
        self.runTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.runTime5ENTRY.place(x = 700, y = 410)
        self.basicWidgetList.append( self.runTime5ENTRY )

        self.memSizeLBL  =  Label( root , text = "Memory Size" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.memSizeLBL.place(x = 150, y = 470)
        self.basicWidgetList.append( self.memSizeLBL )
        
        self.memSizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.memSizeENTRY.place(x = 130, y = 520 )
        self.basicWidgetList.append( self.memSizeENTRY )

        self.osSizeLBL  =  Label( root , text = "OS Size" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.osSizeLBL.place(x = 660, y = 470)
        self.basicWidgetList.append( self.osSizeLBL )
        
        self.osSizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.osSizeENTRY.place(x = 625, y = 520 )
        self.basicWidgetList.append( self.osSizeENTRY )
        
        self.computeBTN  =  Button ( root , text = 'Compute',command = self.input1_computeBTN_Pressed , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.computeBTN.place (x = 390 ,y = 470)
        self.basicWidgetList.append( self.computeBTN )

        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 520)
        self.basicWidgetList.append( self.exitBTN )


    # Executes once the user presses the compute button in the input1_window
    def input1_computeBTN_Pressed( self ):
        self.clearNodes()
        #print( "Head Node: " , self.headNode )
        #print ( "Input1 Compute BTN Pressed " )
        if messagebox.askyesno( "Confirmation..." , " Are you sure you want to compute? " ) == True :
            self.size1 = self.size1ENTRY.get()
            self.size2 = self.size2ENTRY.get()
            self.size3 = self.size3ENTRY.get()
            self.size4 = self.size4ENTRY.get()
            self.size5 = self.size5ENTRY.get()

            self.memSize = self.memSizeENTRY.get()
            self.osSize = self.osSizeENTRY.get()

            self.memSize_Check = self.isNotInteger( self.memSize )
            self.osSize_Check = self.isNotInteger( self.osSize )
 
            self.size1_Check = self.isNotInteger( self.size1 )
            self.size2_Check = self.isNotInteger( self.size2 )
            self.size3_Check = self.isNotInteger( self.size3 )
            self.size4_Check = self.isNotInteger( self.size4 )
            self.size5_Check = self.isNotInteger( self.size5 )
            
            
            self.arrivalTime1 = self.arrivalTime1ENTRY.get()
            self.arrivalTime2 = self.arrivalTime2ENTRY.get()
            self.arrivalTime3 = self.arrivalTime3ENTRY.get()
            self.arrivalTime4 = self.arrivalTime4ENTRY.get()
            self.arrivalTime5 = self.arrivalTime5ENTRY.get()

            self.arrivalTime1_Check = self.isNotTimeFormat( self.arrivalTime1 )
            self.arrivalTime2_Check = self.isNotTimeFormat( self.arrivalTime2 )
            self.arrivalTime3_Check = self.isNotTimeFormat( self.arrivalTime3 )
            self.arrivalTime4_Check = self.isNotTimeFormat( self.arrivalTime4 )
            self.arrivalTime5_Check = self.isNotTimeFormat( self.arrivalTime5 )

            self.runTime1 = self.runTime1ENTRY.get()
            self.runTime2 = self.runTime2ENTRY.get()
            self.runTime3 = self.runTime3ENTRY.get()
            self.runTime4 = self.runTime4ENTRY.get()
            self.runTime5 = self.runTime5ENTRY.get()
        
            self.runTime1_Check = self.isNotTimeFormat( self.runTime1 )
            self.runTime2_Check = self.isNotTimeFormat( self.runTime2 )
            self.runTime3_Check = self.isNotTimeFormat( self.runTime3 )
            self.runTime4_Check = self.isNotTimeFormat( self.runTime4 )
            self.runTime5_Check = self.isNotTimeFormat( self.runTime5 )

            # This condition checks whether the user's inputted values are acceptable.
            # If not, #print the errors.
            if self.memSize_Check or self.osSize_Check :
                #print ( "Error: Invalid Memory or OS Size input." )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Memory or OS Size input." )
            elif int(self.memSize) < int(self.osSize):
                #print ( " Error: Os Size can't exceed Memory Size. " )
                messagebox.showinfo( "Compute Error" , "Error: Os Size can't exceed Memory Size." )
            elif self.size1_Check or self.size2_Check or self.size3_Check or self.size4_Check or self.size5_Check:
                #print ( "Error: Size input detected as not an integer." )
                messagebox.showinfo( "Compute Error" , "Error: Size input detected as not an integer." )
            elif (int(self.size1) > ( int(self.memSize) - int(self.osSize))) or (int(self.size2) > ( int(self.memSize) - int(self.osSize))) or (int(self.size3) > ( int(self.memSize) - int(self.osSize))) or (int(self.size4) > ( int(self.memSize) - int(self.osSize))) or (int(self.size5) > ( int(self.memSize) - int(self.osSize))):
                #print ( "Error: Size input should not exceed ( Memory Size - OS Size )." )
                messagebox.showinfo( "Compute Error" , "Error: Size input should not exceed ( Memory Size - OS Size )." )
            elif self.arrivalTime1_Check or self.arrivalTime2_Check or self.arrivalTime3_Check or self.arrivalTime4_Check or self.arrivalTime5_Check:
                #print ( " Error in arrival time input " )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Arrival Time Input." )
            elif self.runTime1_Check or self.runTime2_Check or self.runTime3_Check or self.runTime4_Check or self.runTime5_Check:
                #print ( "Error: Invalid Run Time Input." )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Run Time Input." )
            else:
                # Job Details [ jobSize, jobNum, arrivalTime, runTime, isjobWaiting ]
                # manipulates the user's input in a format that can be understood by the backEnd class.
                self.jobDetails = [ [ int(self.size1), 1, self.arrivalTime1, self.runTime1, False],
                                    [ int(self.size2), 2, self.arrivalTime2, self.runTime2, False],
                                    [ int(self.size3), 3, self.arrivalTime3, self.runTime3, False],
                                    [ int(self.size4), 4, self.arrivalTime4, self.runTime4, False],
                                    [ int(self.size5), 5, self.arrivalTime5, self.runTime5, False]]
                # Memory [ sizeTaken, F/U( Free,Taken ), -1/jobNum ]
                self.memory = [[( int(self.memSize) - int(self.osSize) ) + 1,'F',-1]]
                # insert_inputs( self, memSpace, osSpace, jobDetails, memory )
                self.firstFit_backEnd.insert_inputs( self.memSize, self.osSize, self.jobDetails, self.memory )
                self.firstFit_backEnd.generate_summaryTable()
                self.summaryTable_window()
                #print ( " Success " )

    # the window which displays the summary table
    def summaryTable_window( self ):
        self.summaryTable = deepcopy(self.firstFit_backEnd.get_summaryTable())
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.dynamicFirstFitBG = Label ( root , image = dff_bg, bg = "black" )
        self.dynamicFirstFitBG.place(x = 0, y = 0)
        self.basicWidgetList.append( self.dynamicFirstFitBG )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffff01" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffff01")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )
        
        self.title1LBL  =  Label( root , text = "First Fit Dynamic" , font = ('Times New Roman', 20),  bg = "#ffff01")
        self.title1LBL.place(x = 100, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Partitioned Allocation" , font = ('Times New Roman', 20),  bg = "#ffff01")
        self.title2LBL.place(x = 75, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Summary Table" , font = ('Times New Roman', 30),  bg = "#c6e3ad")
        self.title3LBL.place(x = 343, y = 105)
        self.basicWidgetList.append( self.title3LBL )

        self.jobLBL  =  Label( root , text = "Job" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.jobLBL.place(x = 125, y = 160)
        self.basicWidgetList.append( self.jobLBL )

        self.job1LBL  =  Label( root , text = "1" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job1LBL.place(x = 135, y = 210)
        self.basicWidgetList.append( self.job1LBL )
        
        self.job2LBL  =  Label( root , text = "2" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job2LBL.place(x = 135, y = 260)
        self.basicWidgetList.append( self.job2LBL )
        
        self.job3LBL  =  Label( root , text = "3" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job3LBL.place(x = 135, y = 310)
        self.basicWidgetList.append( self.job3LBL )

        self.job4LBL  =  Label( root , text = "4" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job4LBL.place(x = 135, y = 360)
        self.basicWidgetList.append( self.job4LBL )
        
        self.job5LBL  =  Label( root , text = "5" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job5LBL.place(x = 135, y = 410)
        self.basicWidgetList.append( self.job5LBL )
        
        # Start Time Widgets
        self.startTimeLBL  =  Label( root , text = "Start Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.startTimeLBL.place(x = 252, y = 160)
        self.basicWidgetList.append( self.startTimeLBL )
        
        self.startTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.startTime1ENTRY.place(x = 225, y = 210)
        self.startTime1ENTRY.insert( 0, self.summaryTable[1][1].time() )
        self.startTime1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.startTime1ENTRY )
        
        self.startTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.startTime2ENTRY.place(x = 225, y = 260)
        self.startTime2ENTRY.insert( 0, self.summaryTable[2][1].time() )
        self.startTime2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.startTime2ENTRY )
        
        self.startTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.startTime3ENTRY.place(x = 225, y = 310)
        self.startTime3ENTRY.insert( 0, self.summaryTable[3][1].time() )
        self.startTime3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.startTime3ENTRY )

        self.startTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.startTime4ENTRY.place(x = 225, y = 360)
        self.startTime4ENTRY.insert( 0, self.summaryTable[4][1].time() )
        self.startTime4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.startTime4ENTRY )
        
        self.startTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.startTime5ENTRY.place(x = 225, y = 410)
        self.startTime5ENTRY.insert( 0, self.summaryTable[5][1].time() )
        self.startTime5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.startTime5ENTRY )
        
        # Finish Time Widgets
        self.finishTimeLBL  =  Label( root , text = "Finish Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.finishTimeLBL.place(x = 512, y = 160)
        self.basicWidgetList.append( self.finishTimeLBL )

        self.finishTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.finishTime1ENTRY.place(x = 490, y = 210)
        self.finishTime1ENTRY.insert( 0, self.summaryTable[1][2].time() )
        self.finishTime1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.finishTime1ENTRY )
        
        self.finishTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.finishTime2ENTRY.place(x = 490, y = 260)
        self.finishTime2ENTRY.insert( 0, self.summaryTable[2][2].time() )
        self.finishTime2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.finishTime2ENTRY )
        
        self.finishTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.finishTime3ENTRY.place(x = 490, y = 310)
        self.finishTime3ENTRY.insert( 0, self.summaryTable[3][2].time() )
        self.finishTime3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.finishTime3ENTRY )

        self.finishTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.finishTime4ENTRY.place(x = 490, y = 360)
        self.finishTime4ENTRY.insert( 0, self.summaryTable[4][2].time() )
        self.finishTime4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.finishTime4ENTRY )
        
        self.finishTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.finishTime5ENTRY.place(x = 490, y = 410)
        self.finishTime5ENTRY.insert( 0, self.summaryTable[5][2].time() )
        self.finishTime5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.finishTime5ENTRY )
        
        # CPU Wait Widgets
        self.cpuWaitLBL  =  Label( root , text = "CPU Wait" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.cpuWaitLBL.place(x = 725, y = 160)
        self.basicWidgetList.append( self.cpuWaitLBL )
        
        self.cpuWait1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuWait1ENTRY.place(x = 700, y = 210)
        self.cpuWait1ENTRY.insert( 0, self.summaryTable[1][3] )
        self.cpuWait1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.cpuWait1ENTRY )
        
        self.cpuWait2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuWait2ENTRY.place(x = 700, y = 260)
        self.cpuWait2ENTRY.insert( 0, self.summaryTable[2][3] )
        self.cpuWait2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.cpuWait2ENTRY )
        
        self.cpuWait3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuWait3ENTRY.place(x = 700, y = 310)
        self.cpuWait3ENTRY.insert( 0, self.summaryTable[3][3] )
        self.cpuWait3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.cpuWait3ENTRY )

        self.cpuWait4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuWait4ENTRY.place(x = 700, y = 360)
        self.cpuWait4ENTRY.insert( 0, self.summaryTable[4][3] )
        self.cpuWait4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.cpuWait4ENTRY )
        
        self.cpuWait5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuWait5ENTRY.place(x = 700, y = 410)
        self.cpuWait5ENTRY.insert( 0, self.summaryTable[5][3] )
        self.cpuWait5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.cpuWait5ENTRY )

        # Buttons
        self.backBTN  =  Button ( root , text = 'BACK',command = self.input1_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 200 ,y = 470)
        self.basicWidgetList.append( self.backBTN )
        self.nextBTN  =  Button ( root , text = 'NEXT',command = self.summaryTable_nextBTN_Pressed , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.nextBTN.place (x = 580 ,y = 470)
        self.basicWidgetList.append( self.nextBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 470)
        self.basicWidgetList.append( self.exitBTN )


    # This executes if the user presses the next button in the summaryTable window.
    def summaryTable_nextBTN_Pressed( self ):
        #print( "Summary Table nextBTN Pressed " )
        self.headNode = None
        self.tempMemoryResults = deepcopy(self.firstFit_backEnd.get_memoryResults())
        self.tempMemoryResults_time = deepcopy(self.firstFit_backEnd.get_memoryResults_time())
        for i in range(len( self.tempMemoryResults ) - 1, -1, -1):
            self.addResultNode( self.tempMemoryResults[i], self.tempMemoryResults_time[i], self.osSize, self.memSize )
        if self.headNode != None:
            self.headNode.memMap_window()
        

# This is a node class for the linked list
# the linked list contains the nodes which hosts the memory map, fat, and pat windows.
class dynamic_firstFitNode_frontEnd:
    def __init__ ( self, memoryResult = None, memoryResult_time = None, osSize = None, memSize = None):
        self.backPointer = None
        self.nextPointer = None
        self.patData = []
        self.fatData = []
        self.location = 0
        
        if memoryResult == None:
            self.memoryResult = [[500, "U", 1], [109, "F", -1]]
        else:
            self.memoryResult = memoryResult
                   
        if memoryResult_time == None:
            self.memoryResult_time = [ "09:00:00", ["Arrived(J1)", "Started(J1)"]]
        else:
            self.memoryResult_time = memoryResult_time

        if osSize == None:
            self.osSize = 32
        else:
            self.osSize = int(osSize)

        if memSize == None:
            self.memSize = 640
        else:
            self.memSize = int(memSize)

        self.location += int(self.osSize)
        self.tempColors = [ "#f77777", "#f7d977", "#77f7e6", "#77d5f7", "#d577f7", "#77d567", "#d5987" ]
        self.tempColorCounter = 0
        self.tempPercentage = float(( float(self.osSize) / float(self.memSize) ) * 100 )
        self.memMap_data = [ [ self.tempPercentage, "#f5f3ed", "OS Size", self.tempPercentage, self.location, self.osSize ] ]
        self.availableCounter = 1
        self.pCounter = 1
        for certainResult in self.memoryResult:
            if certainResult[1] == "U":
                if self.location+certainResult[0] > self.memSize:
                    self.patData.append( [ certainResult[0] - 1, self.location, "Allocated(J{})".format( certainResult[2] ) ] )
                else:
                    self.patData.append( [ certainResult[0], self.location, "Allocated(J{})".format( certainResult[2] ) ] )
                self.location += int(certainResult[0])
                self.tempPercentage = float(( float(certainResult[0]) / float(self.memSize) ) * 100 )
                self.memMap_data.append( [ self.tempPercentage, self.tempColors[self.tempColorCounter], "Allocated(P{})".format(self.pCounter), self.tempPercentage, self.location, certainResult[0] ])
                self.tempColorCounter += 1
                self.pCounter += 1
            else:
                if self.location+certainResult[0] > self.memSize:
                    self.fatData.append( [ certainResult[0] - 1, self.location, "Available" ] )
                    self.location += int(certainResult[0])
                    #print ( "Available Counter: ", self.availableCounter )
                    self.tempPercentage = float(( float(certainResult[0]) / float(self.memSize) ) * 100 )
                    if certainResult[0] == 1:
                        pass
                    else:
                        self.memMap_data.append( [ self.tempPercentage, self.tempColors[self.tempColorCounter], "Available(F{})".format(self.availableCounter), self.tempPercentage, self.location - 1, certainResult[0] - 1 ])
                else:
                    self.fatData.append( [ certainResult[0], self.location, "Available" ] )
                    self.location += int(certainResult[0])
                    #print ( "Available Counter: ", self.availableCounter )
                    self.tempPercentage = float(( float(certainResult[0]) / float(self.memSize) ) * 100 )
                    if certainResult[0] == 1:
                        pass
                    else:
                        self.memMap_data.append( [ self.tempPercentage, self.tempColors[self.tempColorCounter], "Available(F{})".format(self.availableCounter), self.tempPercentage, self.location, certainResult[0] ])
                    
                self.tempColorCounter += 1
                self.availableCounter += 1


        self.countPatData = len( self.patData )
        if self.countPatData != 5:
            for i in range( 5 - self.countPatData ):
                self.patData.append( ["---", "---", "---"] )
        self.countFatData = len( self.fatData )
        if self.countFatData != 5:
            for i in range( 5 - self.countFatData ):
                self.fatData.append( ["---", "---", "---"] )

        ##print( self.memMap_data )
        ##print( self.fatData )

        self.memMap_data2 = deepcopy( self.memMap_data )
        self.tempCount = len( self.memMap_data2 )
        if self.tempCount != 7:
            for i in range( 7 - self.tempCount ):
                self.memMap_data2.append([ "---", "#c6e3ad", "---", "---", "---", "---" ])
        #print( self.memMap_data2 )

        # displayMap( self, tempPointer, tempColor, tempText, tempPercentage, tempTotalSize, memSize )

        

            

    # For getting the current date
    def current_date( self ):
        self.dateString  =  datetime.date.today().strftime("%B %d, %Y")
        self.dateLBL.config(text = self.dateString)

    # This updates the clock widget
    def tick( self ):
        if self.tick_on:
            self.timeString  =  time.strftime("%H:%M:%S")
            self.clockLBL.config(text = self.timeString)
            self.clockLBL.after(200, self.tick )
        else:
            pass

    # The program has two list which contains a reference to all the program's widgets
    # And what this function does is it tries to clear/destroy all of these widgets
    # using the lists which contains the program's widgets.
    # The two lists are:
    #   - self.basicWidgetList: For most of the basic widgets
    #   - self.physicalMemWidgets: For the widgets used to display physical memory map
    def clearWidgets( self ):
        try:
            self.tick_on = False
            self.clearWidgetList( self.basicWidgetList )
            self.clearWidgetList( self.physicalMemWidgets )
        except:
            pass
        return


    # This function destroys all of the widgets inside the inputted widgetsToClear list.
    def clearWidgetList ( self, widgetsToClear):
        for widget in widgetsToClear:
            widget.destroy()

            
    # This function displays the necessary widgets for physical memory map.
    # To get a general gist, the program has around 50 labels which acts as the physical memory map.
    # In addition, it has a text label which marks each section of the physical memory map.
    def displayMap( self, tempPointer, tempColor, tempText, tempPercentage, tempTotalSize ):
        self.tempPointer = int(tempPointer)
        self.tempColor = tempColor
        self.tempText = tempText
        self.tempPercentage = tempPercentage
        self.tempTotalSize = tempTotalSize
        
        if self.tempPercentage != 0:
            self.tempLBL = Label( root , text = "          " * 25 , font = ('Times New Roman', 1),  bg = self.tempColor)
            self.tempLBL.place(x = 80, y = self.yCounter)
            self.yCounter += 7
            self.physicalMemWidgets.append( self.tempLBL )
            
            self.tempLBL = Label( root , text = self.tempText , font = ('Times New Roman', 10),  bg = self.tempColor)
            self.tempLBL.place(x = 350, y = self.yCounter)
            self.physicalMemWidgets.append( self.tempLBL )
        for i in range( int( self.tempPercentage / 2 ) ):
            if self.tempPointer != 0:
                self.tempLBL = Label( root , text = "          " * 25 , font = ('Times New Roman', 1),  bg = self.tempColor)
                self.tempLBL.place(x = 80, y = self.yCounter)
                self.yCounter += 7
                self.physicalMemWidgets.append( self.tempLBL )
                self.tempPointer -= 1
            else:
                pass
        if self.tempPercentage != 0:
            self.tempLBL  =  Label( root , text = tempTotalSize , font = ('Times New Roman', 10),  bg = "#c6e3ad")
            self.tempLBL.place(x = 50, y = self.yCounter - 15)
            self.physicalMemWidgets.append( self.tempLBL )

        return

    def memMap_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.dynamicFirstFitBG = Label ( root , image = dff_bg, bg = "black" )
        self.dynamicFirstFitBG.place(x = 0, y = 0)
        self.basicWidgetList.append( self.dynamicFirstFitBG )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffff01" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffff01")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )

        self.title1LBL  =  Label( root , text = "First Fit Dynamic" , font = ('Times New Roman', 20),  bg = "#ffff01")
        self.title1LBL.place(x = 100, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Partitioned Allocation" , font = ('Times New Roman', 20),  bg = "#ffff01")
        self.title2LBL.place(x = 75, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Memory Map Data" , font = ('Times New Roman', 20),  bg = "#c6e3ad")
        self.title3LBL.place(x = 530, y = 106)
        self.basicWidgetList.append( self.title3LBL )

        self.title4LBL  =  Label( root , text = "At {}".format( self.memoryResult_time[0] ) , font = ('Times New Roman', 12),  bg = "#c6e3ad")
        self.title4LBL.place(x = 608, y = 138)
        self.basicWidgetList.append( self.title4LBL )
        
        self.physicalMemWidgets = []
        self.yCounter = 140
        self.indexPointer = 0
        
        self.markLBL  =  Label( root , text = 0 , font = ('Times New Roman', 10),  bg = "#c6e3ad")
        self.markLBL.place(x = 60, y = self.yCounter - 20)
        self.physicalMemWidgets.append( self.markLBL )

        for tempData in self.memMap_data:
            self.displayMap( tempData[0], tempData[1], tempData[2], tempData[3], tempData[4] )

        self.partitionLBL  =  Label( root , text = "#" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.partitionLBL.place(x = 440, y = 160)
        self.basicWidgetList.append( self.partitionLBL )

        self.partition1LBL  =  Label( root , text = "1" , font = ('Times New Roman', 15),  bg = self.memMap_data2[0][1])
        self.partition1LBL.place(x = 440, y = 210)
        self.basicWidgetList.append( self.partition1LBL )
        
        self.partition2LBL  =  Label( root , text = "2" , font = ('Times New Roman', 15),  bg = self.memMap_data2[1][1])
        self.partition2LBL.place(x = 440, y = 260)
        self.basicWidgetList.append( self.partition2LBL )
        
        self.partition3LBL  =  Label( root , text = "3" , font = ('Times New Roman', 15),  bg = self.memMap_data2[2][1])
        self.partition3LBL.place(x = 440, y = 310)
        self.basicWidgetList.append( self.partition3LBL )
        
        self.partition4LBL  =  Label( root , text = "4" , font = ('Times New Roman', 15),  bg = self.memMap_data2[3][1])
        self.partition4LBL.place(x = 440, y = 360)
        self.basicWidgetList.append( self.partition4LBL )
        
        self.partition5LBL  =  Label( root , text = "5" , font = ('Times New Roman', 15),  bg = self.memMap_data2[4][1])
        self.partition5LBL.place(x = 440, y = 410)
        self.basicWidgetList.append( self.partition5LBL )

        self.partition6LBL  =  Label( root , text = "6" , font = ('Times New Roman', 15),  bg = self.memMap_data2[5][1])
        self.partition6LBL.place(x = 440, y = 460)
        self.basicWidgetList.append( self.partition6LBL )
        
        self.partition7LBL  =  Label( root , text = "7" , font = ('Times New Roman', 15),  bg = self.memMap_data2[6][1])
        self.partition7LBL.place(x = 440, y = 510)
        self.basicWidgetList.append( self.partition7LBL )


        # Size Widgets
        self.sizeLBL  =  Label( root , text = "Size" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.sizeLBL.place(x = 580, y = 160)
        self.basicWidgetList.append( self.sizeLBL )

        self.size1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size1ENTRY.place(x = 530, y = 210)
        self.size1ENTRY.insert( 0, self.memMap_data2[0][5] )
        self.size1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.size1ENTRY )
        
        self.size2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size2ENTRY.place(x = 530, y = 260)
        self.size2ENTRY.insert( 0, self.memMap_data2[1][5] )
        self.size2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.size2ENTRY )
        
        self.size3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size3ENTRY.place(x = 530, y = 310)
        self.size3ENTRY.insert( 0, self.memMap_data2[2][5] )
        self.size3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.size3ENTRY )
        
        self.size4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size4ENTRY.place(x = 530, y = 360)
        self.size4ENTRY.insert( 0, self.memMap_data2[3][5] )
        self.size4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.size4ENTRY )
        
        self.size5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size5ENTRY.place(x = 530, y = 410)
        self.size5ENTRY.insert( 0, self.memMap_data2[4][5] )
        self.size5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.size5ENTRY )

        self.size6ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size6ENTRY.place(x = 530, y = 460)
        self.size6ENTRY.insert( 0, self.memMap_data2[5][5] )
        self.size6ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.size6ENTRY )
        
        self.size7ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size7ENTRY.place(x = 530, y = 510)
        self.size7ENTRY.insert( 0, self.memMap_data2[6][5] )
        self.size7ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.size7ENTRY )


        # Status Widgets
        self.statusLBL  =  Label( root , text = "Status" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.statusLBL.place(x = 740, y = 160)
        self.basicWidgetList.append( self.statusLBL )
        
        self.status1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.status1ENTRY.place(x = 700, y = 210)
        self.status1ENTRY.insert( 0, self.memMap_data2[0][2] )
        self.status1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.status1ENTRY )
        
        self.status2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.status2ENTRY.place(x = 700, y = 260)
        self.status2ENTRY.insert( 0, self.memMap_data2[1][2] )
        self.status2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.status2ENTRY )
        
        self.status3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.status3ENTRY.place(x = 700, y = 310)
        self.status3ENTRY.insert( 0, self.memMap_data2[2][2] )
        self.status3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.status3ENTRY )
        
        self.status4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.status4ENTRY.place(x = 700, y = 360)
        self.status4ENTRY.insert( 0, self.memMap_data2[3][2] )
        self.status4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.status4ENTRY )
        
        self.status5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.status5ENTRY.place(x = 700, y = 410)
        self.status5ENTRY.insert( 0, self.memMap_data2[4][2] )
        self.status5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.status5ENTRY )

        self.status6ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.status6ENTRY.place(x = 700, y = 460)
        self.status6ENTRY.insert( 0, self.memMap_data2[5][2] )
        self.status6ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.status6ENTRY )
        
        self.status7ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.status7ENTRY.place(x = 700, y = 510)
        self.status7ENTRY.insert( 0, self.memMap_data2[6][2] )
        self.status7ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.status7ENTRY )

        self.backBTN  =  Button ( root , text = 'BACK',command = self.memMap_backBTN_Pressed , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 200 ,y = 540)
        self.basicWidgetList.append( self.backBTN )
        self.nextBTN  =  Button ( root , text = 'NEXT',command = self.pat_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.nextBTN.place (x = 580 ,y = 540)
        self.basicWidgetList.append( self.nextBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 540)
        self.basicWidgetList.append( self.exitBTN )

    def memMap_backBTN_Pressed( self ):
        #print ( "memMap_backBTN_Pressed" )
        if self.backPointer != None:
            self.backPointer.fat_window()
        else:
            dff_program.summaryTable_window()

    def pat_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.dynamicFirstFitBG = Label ( root , image = dff_bg, bg = "black" )
        self.dynamicFirstFitBG.place(x = 0, y = 0)
        self.basicWidgetList.append( self.dynamicFirstFitBG )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffff01" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffff01")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )
        
        self.title1LBL  =  Label( root , text = "First Fit Dynamic" , font = ('Times New Roman', 20),  bg = "#ffff01")
        self.title1LBL.place(x = 100, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Partitioned Allocation" , font = ('Times New Roman', 20),  bg = "#ffff01")
        self.title2LBL.place(x = 75, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Partion Allocation Table" , font = ('Times New Roman', 30),  bg = "#c6e3ad")
        self.title3LBL.place(x = 270, y = 105)
        self.basicWidgetList.append( self.title3LBL )

        self.title4LBL  =  Label( root , text = "At {}".format( self.memoryResult_time[0] ) , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.title4LBL.place(x = 425, y = 155)
        self.basicWidgetList.append( self.title4LBL )
        

        # PAT Number Widgets
        self.patNumLBL  =  Label( root , text = "Partition #" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.patNumLBL.place(x = 100, y = 180)
        self.basicWidgetList.append( self.patNumLBL )

        self.patNum1LBL  =  Label( root , text = "1" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.patNum1LBL.place(x = 135, y = 220)
        self.basicWidgetList.append( self.patNum1LBL )
        
        self.patNum2LBL  =  Label( root , text = "2" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.patNum2LBL.place(x = 135, y = 260)
        self.basicWidgetList.append( self.patNum2LBL )
        
        self.patNum3LBL  =  Label( root , text = "3" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.patNum3LBL.place(x = 135, y = 300)
        self.basicWidgetList.append( self.patNum3LBL )

        self.patNum4LBL  =  Label( root , text = "4" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.patNum4LBL.place(x = 135, y = 340)
        self.basicWidgetList.append( self.patNum4LBL )
        
        self.patNum5LBL  =  Label( root , text = "5" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.patNum5LBL.place(x = 135, y = 380)
        self.basicWidgetList.append( self.patNum5LBL )
        
        # PAT Size Widgets
        self.patSizeLBL  =  Label( root , text = "Size" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.patSizeLBL.place(x = 277, y = 180)
        self.basicWidgetList.append( self.patSizeLBL )
        
        self.patSize1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patSize1ENTRY.place(x = 225, y = 220)
        self.patSize1ENTRY.insert( 0, self.patData[0][0] )
        self.patSize1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patSize1ENTRY )
        
        self.patSize2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patSize2ENTRY.place(x = 225, y = 260)
        self.patSize2ENTRY.insert( 0, self.patData[1][0] )
        self.patSize2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patSize2ENTRY )
        
        self.patSize3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patSize3ENTRY.place(x = 225, y = 300)
        self.patSize3ENTRY.insert( 0, self.patData[2][0] )
        self.patSize3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patSize3ENTRY )

        self.patSize4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patSize4ENTRY.place(x = 225, y = 340)
        self.patSize4ENTRY.insert( 0, self.patData[3][0] )
        self.patSize4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patSize4ENTRY )
        
        self.patSize5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patSize5ENTRY.place(x = 225, y = 380)
        self.patSize5ENTRY.insert( 0, self.patData[4][0] )
        self.patSize5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patSize5ENTRY )
        
        # PAT Location Widgets
        self.patLocationLBL  =  Label( root , text = "Location" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.patLocationLBL.place(x = 522, y = 180)
        self.basicWidgetList.append( self.patLocationLBL )

        self.patLocation1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patLocation1ENTRY.place(x = 490, y = 220)
        self.patLocation1ENTRY.insert( 0, self.patData[0][1] )
        self.patLocation1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patLocation1ENTRY )
        
        self.patLocation2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patLocation2ENTRY.place(x = 490, y = 260)
        self.patLocation2ENTRY.insert( 0, self.patData[1][1] )
        self.patLocation2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patLocation2ENTRY )
        
        self.patLocation3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patLocation3ENTRY.place(x = 490, y = 300)
        self.patLocation3ENTRY.insert( 0, self.patData[2][1] )
        self.patLocation3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patLocation3ENTRY )

        self.patLocation4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patLocation4ENTRY.place(x = 490, y = 340)
        self.patLocation4ENTRY.insert( 0, self.patData[3][1] )
        self.patLocation4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patLocation4ENTRY )
        
        self.patLocation5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patLocation5ENTRY.place(x = 490, y = 380)
        self.patLocation5ENTRY.insert( 0, self.patData[4][1] )
        self.patLocation5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patLocation5ENTRY )
        
        # PAT Status Widgets
        self.patStatusLBL  =  Label( root , text = "Status" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.patStatusLBL.place(x = 740, y = 180)
        self.basicWidgetList.append( self.patStatusLBL )
        
        self.patStatus1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patStatus1ENTRY.place(x = 700, y = 220)
        self.patStatus1ENTRY.insert( 0, self.patData[0][2] )
        self.patStatus1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patStatus1ENTRY )
        
        self.patStatus2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patStatus2ENTRY.place(x = 700, y = 260)
        self.patStatus2ENTRY.insert( 0, self.patData[1][2] )
        self.patStatus2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patStatus2ENTRY )
        
        self.patStatus3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patStatus3ENTRY.place(x = 700, y = 300)
        self.patStatus3ENTRY.insert( 0, self.patData[2][2] )
        self.patStatus3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patStatus3ENTRY )

        self.patStatus4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patStatus4ENTRY.place(x = 700, y = 340)
        self.patStatus4ENTRY.insert( 0, self.patData[3][2] )
        self.patStatus4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patStatus4ENTRY )
        
        self.patStatus5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patStatus5ENTRY.place(x = 700, y = 380)
        self.patStatus5ENTRY.insert( 0, self.patData[4][2] )
        self.patStatus5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patStatus5ENTRY )

        # Listbox Widgets

        self.patListbox1 = Listbox( root, height = 6, width = 40, border = 0, justify = "center" )
        self.patListbox1.place( x = 220, y = 430 )
        self.basicWidgetList.append( self.patListbox1 )
        self.patListbox2 = Listbox( root, height = 6, width = 40, border = 0, justify = "center" )
        self.patListbox2.place( x = 480, y = 430 )
        self.basicWidgetList.append( self.patListbox2 )

        self.tempCount1 = 0
        self.tempCount2 = 0
        for allocation in self.memoryResult_time[1]:
            if allocation[0] == "A":
                self.tempCount1 += 1
                self.patListbox1.insert( self.tempCount1, allocation )
            else:
                self.tempCount2 += 1
                self.patListbox2.insert( self.tempCount2, allocation )

        # Buttons
        self.backBTN  =  Button ( root , text = 'Back',command = self.memMap_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 200 ,y = 540)
        self.basicWidgetList.append( self.backBTN )
        self.nextBTN  =  Button ( root , text = 'Next',command = self.fat_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.nextBTN.place (x = 580 ,y = 540)
        self.basicWidgetList.append( self.nextBTN )

        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 540)
        self.basicWidgetList.append( self.exitBTN )


    def fat_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.dynamicFirstFitBG = Label ( root , image = dff_bg, bg = "black" )
        self.dynamicFirstFitBG.place(x = 0, y = 0)
        self.basicWidgetList.append( self.dynamicFirstFitBG )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffff01" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffff01")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )
        
        self.title1LBL  =  Label( root , text = "First Fit Dynamic" , font = ('Times New Roman', 20),  bg = "#ffff01")
        self.title1LBL.place(x = 100, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Partitioned Allocation" , font = ('Times New Roman', 20),  bg = "#ffff01")
        self.title2LBL.place(x = 75, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "File Allocation Table" , font = ('Times New Roman', 30),  bg = "#c6e3ad")
        self.title3LBL.place(x = 305, y = 105)
        self.basicWidgetList.append( self.title3LBL )
        self.title4LBL  =  Label( root , text = "At {}".format( self.memoryResult_time[0] ) , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.title4LBL.place(x = 425, y = 155)
        self.basicWidgetList.append( self.title4LBL )

        # fat Number Widgets
        self.fatNumLBL  =  Label( root , text = "FA #" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.fatNumLBL.place(x = 123, y = 180)
        self.basicWidgetList.append( self.fatNumLBL )

        self.fatNum1LBL  =  Label( root , text = "1" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.fatNum1LBL.place(x = 135, y = 220)
        self.basicWidgetList.append( self.fatNum1LBL )
        
        self.fatNum2LBL  =  Label( root , text = "2" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.fatNum2LBL.place(x = 135, y = 260)
        self.basicWidgetList.append( self.fatNum2LBL )
        
        self.fatNum3LBL  =  Label( root , text = "3" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.fatNum3LBL.place(x = 135, y = 300)
        self.basicWidgetList.append( self.fatNum3LBL )

        self.fatNum4LBL  =  Label( root , text = "4" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.fatNum4LBL.place(x = 135, y = 340)
        self.basicWidgetList.append( self.fatNum4LBL )
        
        self.fatNum5LBL  =  Label( root , text = "5" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.fatNum5LBL.place(x = 135, y = 380)
        self.basicWidgetList.append( self.fatNum5LBL )
        
        # fat Size Widgets
        self.fatSizeLBL  =  Label( root , text = "Size" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.fatSizeLBL.place(x = 277, y = 180)
        self.basicWidgetList.append( self.fatSizeLBL )
        
        self.fatSize1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatSize1ENTRY.place(x = 225, y = 220)
        self.fatSize1ENTRY.insert( 0, self.fatData[0][0] )
        self.fatSize1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatSize1ENTRY )
        
        self.fatSize2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatSize2ENTRY.place(x = 225, y = 260)
        self.fatSize2ENTRY.insert( 0, self.fatData[1][0] )
        self.fatSize2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatSize2ENTRY )
        
        self.fatSize3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatSize3ENTRY.place(x = 225, y = 300)
        self.fatSize3ENTRY.insert( 0, self.fatData[2][0] )
        self.fatSize3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatSize3ENTRY )

        self.fatSize4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatSize4ENTRY.place(x = 225, y = 340)
        self.fatSize4ENTRY.insert( 0, self.fatData[3][0] )
        self.fatSize4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatSize4ENTRY )
        
        self.fatSize5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatSize5ENTRY.place(x = 225, y = 380)
        self.fatSize5ENTRY.insert( 0, self.fatData[4][0] )
        self.fatSize5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatSize5ENTRY )
        
        # fat Location Widgets
        self.fatLocationLBL  =  Label( root , text = "Location" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.fatLocationLBL.place(x = 522, y = 180)
        self.basicWidgetList.append( self.fatLocationLBL )

        self.fatLocation1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatLocation1ENTRY.place(x = 490, y = 220)
        self.fatLocation1ENTRY.insert( 0, self.fatData[0][1] )
        self.fatLocation1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatLocation1ENTRY )
        
        self.fatLocation2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatLocation2ENTRY.place(x = 490, y = 260)
        self.fatLocation2ENTRY.insert( 0, self.fatData[1][1] )
        self.fatLocation2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatLocation2ENTRY )
        
        self.fatLocation3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatLocation3ENTRY.place(x = 490, y = 300)
        self.fatLocation3ENTRY.insert( 0, self.fatData[2][1] )
        self.fatLocation3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatLocation3ENTRY )

        self.fatLocation4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatLocation4ENTRY.place(x = 490, y = 340)
        self.fatLocation4ENTRY.insert( 0, self.fatData[3][1] )
        self.fatLocation4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatLocation4ENTRY )
        
        self.fatLocation5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatLocation5ENTRY.place(x = 490, y = 380)
        self.fatLocation5ENTRY.insert( 0, self.fatData[4][1] )
        self.fatLocation5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatLocation5ENTRY )
        
        # fat Status Widgets
        self.fatStatusLBL  =  Label( root , text = "Status" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.fatStatusLBL.place(x = 740, y = 180)
        self.basicWidgetList.append( self.fatStatusLBL )
        
        self.fatStatus1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatStatus1ENTRY.place(x = 700, y = 220)
        self.fatStatus1ENTRY.insert( 0, self.fatData[0][2] )
        self.fatStatus1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatStatus1ENTRY )
        
        self.fatStatus2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatStatus2ENTRY.place(x = 700, y = 260)
        self.fatStatus2ENTRY.insert( 0, self.fatData[1][2] )
        self.fatStatus2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatStatus2ENTRY )
        
        self.fatStatus3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatStatus3ENTRY.place(x = 700, y = 300)
        self.fatStatus3ENTRY.insert( 0, self.fatData[2][2] )
        self.fatStatus3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatStatus3ENTRY )

        self.fatStatus4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatStatus4ENTRY.place(x = 700, y = 340)
        self.fatStatus4ENTRY.insert( 0, self.fatData[3][2] )
        self.fatStatus4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatStatus4ENTRY )
        
        self.fatStatus5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatStatus5ENTRY.place(x = 700, y = 380)
        self.fatStatus5ENTRY.insert( 0, self.fatData[4][2] )
        self.fatStatus5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatStatus5ENTRY )

        # Listbox Widgets

        self.fatListbox1 = Listbox( root, height = 6, width = 40, border = 0, justify = "center" )
        self.fatListbox1.place( x = 220, y = 430 )
        self.basicWidgetList.append( self.fatListbox1 )
        self.fatListbox2 = Listbox( root, height = 6, width = 40, border = 0, justify = "center" )
        self.fatListbox2.place( x = 480, y = 430 )
        self.basicWidgetList.append( self.fatListbox2 )

        self.tempCount1 = 0
        self.tempCount2 = 0
        for allocation in self.memoryResult_time[1]:
            if allocation[0] == "A":
                self.tempCount1 += 1
                self.fatListbox1.insert( self.tempCount1, allocation )
            else:
                self.tempCount2 += 1
                self.fatListbox2.insert( self.tempCount2, allocation )

        # Buttons
        self.backBTN  =  Button ( root , text = 'Back',command = self.pat_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 200 ,y = 540)
        self.basicWidgetList.append( self.backBTN )
        self.nextBTN  =  Button ( root , text = 'Next',command = self.fat_nextBTN_Pressed , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        if self.nextPointer == None:
            self.nextBTN.configure( text = "Try New Input", width = 13 )
        self.nextBTN.place (x = 580 ,y = 540)
        self.basicWidgetList.append( self.nextBTN )

        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 540)
        self.basicWidgetList.append( self.exitBTN )

    def fat_nextBTN_Pressed( self ):
        if self.nextPointer == None:
            dff_program.input1_window()
        else:
            self.nextPointer.memMap_window()
# END OF DFF PROGRAM: 2847-4428


# DBF PROGRAM: 4435-6027
# All the back end processes are hosted in this class.
class dynamic_bestFit_backEnd:
    def __init__( self ):
        self.time_zero = datetime.datetime.strptime('00:00', '%H:%M')
        # summary table [ jobNum, startTime, finishTime, cpuWait ]
        self.summaryTable = {}
        self.allTime = []
        
        # Job Status [ allocated(True/False), finished(True/False), waiting ]
        self.jobStatus = { 1 : [ False, False, False ],
                           2 : [ False, False, False ],
                           3 : [ False, False, False ],
                           4 : [ False, False, False ],
                           5 : [ False, False, False ]}
        self.memoryResults = []
        self.memoryResults_time = []

    # for taking in the user's input into the backEnd class.
    def insert_inputs( self, memSpace, osSpace, jobDetails, memory, compactionType ):
        #print( "INPUTS: " )
        #print ( "I1" , jobDetails )
        #print( "I2", memory )
        #print( "compactionType : ", compactionType )
        self.compactionType = compactionType
        self.memSpace = int(memSpace)
        self.osSpace = int(osSpace)
        self.memSize = int( memSpace)
        self.osSpace = int( osSpace )
        self.jobDetails = deepcopy( jobDetails )
        self.memory = deepcopy( memory )

        self.summaryTable = {}
        self.allTime = []
        # generates the all time list which will contain all the time that needs a memory map, fat, and pat.
        for job in self.jobDetails:
            self.tempTime = datetime.datetime.strptime( job[2], '%H:%M')
            self.allTime.append( self.tempTime )

        # job status [ isJobAllocated, isJobFinished, isJobWaiting ]
        self.jobStatus = { 1 : [ False, False, False ],
                           2 : [ False, False, False ],
                           3 : [ False, False, False ],
                           4 : [ False, False, False ],
                           5 : [ False, False, False ]}

        # memoryResult will be used to store the data for every memory map.
        self.memoryResults = []
        
        # memoryResult_time will be used to store the time of every memory map.
        self.memoryResults_time = []
        return

    # returns memory list
    def get_memory( self ):
        return self.memory

    # returns summaryTable
    def get_summaryTable( self ):
        return self.summaryTable

    # returns the memoryResults
    def get_memoryResults( self ):
        return self.memoryResults

    # returns the memoryResults_time
    def get_memoryResults_time( self ):
        return self.memoryResults_time

    # for appending a certain memory list into the memory result
    def add_memoryResult( self, memory, time, timeStatus) :
        self.memoryResults.append( memory )
        self.memoryResults_time.append( [time, timeStatus] )
        return

    # sorts the list containing all the time that needs a memory result.
    def arrange_allTime( self ):
        self.allTime.sort()
        return

    # remove's the time that already have a memory result.
    def remove_time( self, time ):
        try:
            while True:
                self.allTime.remove(time)
        except ValueError:
            pass
        self.arrange_allTime()
        return

    # checks if the job fits into the available partitions
    def check_jobFit( self, j_size ):
        # j_size: job size
        self.j_size = j_size
        # memorySpace[1]: F for free/available space and U if occupied by a certain job
        # memorySpace[0]: the size of the partition.
        for memorySpace in self.memory:
            if memorySpace[1] == "F" and memorySpace[0] > self.j_size:
                return True
        return False

    # checks a certain job's status.
    def check_jobStatus( self ):
        # checks if the jobs are already done.
        self.jobsDone = 0
        for jobNum in list(self.jobStatus):
            if self.jobStatus[jobNum][0] == True and self.jobStatus[jobNum][1]:
                self.jobsDone += 1
        if self.jobsDone == len( list(self.jobStatus) ):
            return True
        else:
            return False

    # allocates a job into the best fitted free/available partition.
    def allocate( self, memory, job, reverse = False ):
        # job [ job id, a/f( allocate/deallocate ), job size ]
        self.j_id = job[0]
        self.j_size = job[2]
        # if the memory list is empty, immediately return
        if memory is None:
            return
        # sorts the memory list by the memory space.
        self.m_sorted = sorted(memory, key=lambda x: x[0], reverse=reverse)
        # i: id for the memory space/partition
        # m: F for free/available memory space,
        #    U for occupied memory space.
        # This loop traverses the memory list so that a job can be allocated to the 
        # first memory space which meets the needs of the job.
        for ms in self.m_sorted:
            if ms[1] == 'F' and ms[0] > self.j_size:
                break
        for i, m in enumerate(memory):
            if m[1] == 'F' and m[0] == ms[0]:
                memory.insert(i + 1, [m[0] - self.j_size, 'F', -1])
                try:
                    if memory[i+2][1] == 'F':
                        memory[i+1][0] += memory[i+2][0]
                        memory.pop(i+2)
                except IndexError:
                    pass

                m[0] = self.j_size
                m[1] = 'U'
                m[2] = self.j_id
                return memory
        
    # for de-allocating a job out of the memory list.
    def recycle( self, memory, job ):
        self.recycle_memory = memory
        self.job = job
        # if the memory list is empty, immediately return
        if self.recycle_memory == None:
            return

        # i: id for the memory space/partition
        # m: F for free/available memory space,
        #    U for occupied memory space.
        # This loop traverses the memory list to de-allocate a job from the memory list
        # Furthermore, it also combines free memory spaces that are side by side.
        for i, m in enumerate( self.recycle_memory ):
            if m[2] == self.job[0] and m[1] == "U":
                m[1] = "F"
                m[2] = -1
                if i != 0 and self.recycle_memory[i-1][1] == "F":
                    self.recycle_memory[i-1][0] += m[0]
                    self.recycle_memory.remove(m)
                    try:
                        if self.recycle_memory[i][1] == "F":
                            self.recycle_memory[i-1][0] += self.recycle_memory[i][0]
                            self.recycle_memory.pop(i)
                    except:
                        pass
                elif i != len(self.recycle_memory) and self.recycle_memory[i+1][1] == "F":
                    self.recycle_memory[i][0] += self.recycle_memory[i+1][0]
                    self.recycle_memory.remove( self.recycle_memory[i+1] )
        return self.recycle_memory


    def recycle_withCompaction( self, memory, job ):
        self.recycle_memory = memory
        self.job = job
        # if the memory list is empty, immediately return
        if self.recycle_memory == None:
            return

        # i: id for the memory space/partition
        # m: F for free/available memory space,
        #    U for occupied memory space.
        # This loop traverses the memory list to de-allocate a job from the memory list
        # Furthermore, it also combines free memory spaces that are side by side.
        for i, m in enumerate( self.recycle_memory ):
            if m[2] == self.job[0] and m[1] == "U":
                m[1] = "F"
                m[2] = -1
                if i != 0 and self.recycle_memory[i-1][1] == "F":
                    self.recycle_memory[i-1][0] += m[0]
                    self.recycle_memory.remove(m)
                    try:
                        if self.recycle_memory[i][1] == "F":
                            self.recycle_memory[i-1][0] += self.recycle_memory[i][0]
                            self.recycle_memory.pop(i)
                    except:
                        pass
                elif i != len(self.recycle_memory) and self.recycle_memory[i+1][1] == "F":
                    self.recycle_memory[i][0] += self.recycle_memory[i+1][0]
                    self.recycle_memory.remove( self.recycle_memory[i+1] )

        if len( self.recycle_memory ) >= 3:
            for i in range( 1, len( self.recycle_memory ) ):
                try:
                    if self.recycle_memory[i-1][1] == "F" and self.recycle_memory[i][1] == "U":
                        self.tempJob = deepcopy( self.recycle_memory[i] )
                        self.tempFreeSpace = deepcopy( self.recycle_memory[i-1] )
                        self.recycle_memory[i-1] = self.tempJob
                        self.recycle_memory[i] = self.tempFreeSpace
                except:
                    pass
                    
                try:
                    if self.recycle_memory[i+1][1] == "F" and self.recycle_memory[i][1] == "F":
                        self.recycle_memory[i][0] += self.recycle_memory[i+1][0]
                        self.recycle_memory.pop( i+1 )
                except:
                    pass
        return self.recycle_memory


    # for generating the summary table.
    def generate_summaryTable( self ):
        self.isFinished = False
        self.arrange_allTime()
        
        while self.isFinished == False:
            # This block of code sets the needed parameters for the next process.
            # It resets the indicator 'actionTaken'. This indicator is used by the
            # program to determine if a job has been allocated/de-allocated in this iteration.
            # tempTimeStatus: contains the status of certain time periods. This could contain
            #                 job arrivals, job waiting, and job terminations.
            # currentTime: the time of a certain/this iteration.
            self.actionTaken = False
            self.tempTimeStatus = []
            try:
                self.arrange_allTime()
                self.currentTime = self.allTime[0]
            except:
                self.isFinished = True
                break

            # Checks if all the jobs are already finished. If it is, then stop the while loop.
            self.tempJobStatus = self.check_jobStatus()
            if self.tempJobStatus == True:
                self.isFinished = True
                break

            # Iterates through the job details to see what actions can be taken in this currentTime
            for job in self.jobDetails:
                self.jobFits = self.check_jobFit( job[0] )
                self.test_jobWaiting = True

                # If a certain job details from the self.jobDetails is deemed to waiting to be allocated
                # then, it will check if the currentTime meets the job's demand for allocation.
                if job[4] != False:
                    self.tempWaitUntil = job[4]
                    if self.currentTime == self.tempWaitUntil:
                        self.test_jobWaiting = False

                # If a certain job arrives, this nested condition will check whether the job needs to wait or is capable
                # of immediate allocation.
                if self.currentTime == datetime.datetime.strptime( job[2], '%H:%M') and self.jobStatus[job[1]][0] == False:
                    if self.jobFits == True:
                        self.tempTimeStatus.append( "Arrived(J{})".format( job[1] ) )
                    else:
                        self.tempTimeStatus.append( "Arrived/Wait(J{})".format( job[1] ) )
                        self.tempWaitUntil = self.tempFinishTime
                        job[4] = self.tempWaitUntil
                # This conditions checks if a certain actions could be taken.
                # The actions could be, the start/allocation or termination of certain job.
                if ( self.test_jobWaiting == False or self.currentTime == datetime.datetime.strptime( job[2], '%H:%M')) and self.jobStatus[job[1]][0] == False and self.jobFits == True:
                    self.memory = self.allocate( self.memory, [ job[1], "a" , job[0] ] )
                    self.jobStatus[job[1]][0] = True

                    self.tempStartTime = self.currentTime
                    if (self.tempStartTime - datetime.datetime.strptime( job[2], '%H:%M')).total_seconds() < 0:
                        self.tempCpuWait = "0:00:00"
                        self.tempStartTime = datetime.datetime.strptime( job[2], '%H:%M')
                    else:
                        self.tempCpuWait = self.tempStartTime - datetime.datetime.strptime( job[2], '%H:%M')
                    self.tempFinishTime = ( self.tempStartTime - self.time_zero + (datetime.datetime.strptime( job[3], '%H:%M')))
                    self.allTime.append( self.tempFinishTime )
                    self.summaryTable[job[1]] = [ job[1], self.tempStartTime, self.tempFinishTime, self.tempCpuWait ]

                    self.actionTaken = True
                    self.tempTimeStatus.append( "Started(J{})".format( job[1] ) )
                elif self.jobStatus[job[1]][0] == True and self.currentTime == self.summaryTable[job[1]][2]:
                    if self.compactionType == "Without Compaction":
                        self.memory = self.recycle( self.memory, [ job[1], "f" , job[0] ] )
                    else:
                        self.memory = self.recycle_withCompaction( self.memory, [ job[1], "f" , job[0] ] )
                    self.jobStatus[job[1]][1] = True
                    
                    self.actionTaken = True
                    self.tempTimeStatus.append( "Terminated(J{})".format( job[1] ) )
                else:
                    pass

            # copies the memory list of this currentTime
            self.memoryToAdd = deepcopy(self.memory)
            # appds the needed data into the memoryResult list.
            self.add_memoryResult( self.memoryToAdd, self.currentTime, deepcopy(self.tempTimeStatus) )

            # Checks if all the job are already finished. If not, then remove the current time from
            # the list of all time.
            self.tempJobStatus = self.check_jobStatus()
            if self.tempJobStatus == True:
                self.isFinished = True
                break
            else:
                self.remove_time( self.currentTime )


# Contains all the front end windows and functions
class dynamic_bestFit_frontEnd:
    def __init__( self ):
        self.memSpace = 640
        self.memSize = 640
        self.osSpace = 32
        self.osSize = 32
        # Job Details [ jobSize, jobNum, arrivalTime, runTime, isjobWaiting ]
        self.jobDetails = [ [ 200, 1, "9:00", "0:20", False],
                            [ 250, 2, "9:10", "0:25", False],
                            [ 300, 3, "9:30", "0:30", False],
                            [ 50, 4, "13:00", "1:00", False],
                            [ 50, 5, "13:00", "1:30", False]]

        self.memory = [[609,'F',-1]]
        
        self.bestFit_backEnd = dynamic_bestFit_backEnd()

        # insert_inputs( self, memSpace, osSpace, jobDetails, memory )
        self.bestFit_backEnd.insert_inputs( self.memSpace, self.osSpace, self.jobDetails, self.memory, "With Compaction" )
        self.bestFit_backEnd.generate_summaryTable()

        self.headNode = None

    # To clear the linked list of nodes.
    def clearNodes( self ):
        self.headNode = None
        return

    # To add a node into the linked list
    # ( self, memoryResult = None, memoryResult_time = None, osSize = None, memSize = None)
    def addResultNode( self, memoryResult, memoryResult_time, osSize, memSize ):
        memoryResult_time[0] = memoryResult_time[0].time()
        self.tempNode = dynamic_bestFitNode_frontEnd( memoryResult, memoryResult_time, osSize, memSize )

        if self.headNode == None:
            self.headNode = self.tempNode
        else:
            self.headNode.backPointer = self.tempNode
            self.tempNode.nextPointer = self.headNode

            self.headNode = self.tempNode
        return


    # For getting the current date
    def current_date( self ):
        self.dateString  =  datetime.date.today().strftime("%B %d, %Y")
        self.dateLBL.config(text = self.dateString)

    
    # This updates the clock widget
    def tick( self ):
        if self.tick_on:
            self.timeString  =  time.strftime("%H:%M:%S")
            self.clockLBL.config(text = self.timeString)
            self.clockLBL.after(200, self.tick )
        else:
            pass


    # This function returns True if timeInput is not in proper time format
    # Else, returns False if the input is in proper time format
    # Time format is HH:MM
    def isNotTimeFormat( self, timeInput):
        try:
            time.strptime( timeInput, '%H:%M')
            return False
        except ValueError:
            return True

    # This function returns True if the integerInput is not an Integer.
    # If it is an integer, return False.
    def isNotInteger( self, integerInput):
        try:
            self.intTest = int(integerInput)
            return False
        except ValueError:
            return True

    # The program has two list which contains a reference to all the program's widgets
    # And what this function does is it tries to clear/destroy all of these widgets
    # using the lists which contains the program's widgets.
    # The two lists are:
    #   - self.basicWidgetList: For most of the basic widgets
    #   - self.physicalMemWidgets: For the widgets used to display physical memory map
    def clearWidgets( self ):
        try:
            self.tick_on = False
            self.clearWidgetList( self.basicWidgetList )
            self.clearWidgetList( self.physicalMemWidgets )
        except:
            pass
        return


    # This function destroys all of the widgets inside the inputted widgetsToClear list.
    def clearWidgetList ( self, widgetsToClear):
        for widget in widgetsToClear:
            widget.destroy()

    # This function displays the necessary widgets for physical memory map.
    # To get a general gist, the program has around 50 labels which acts as the physical memory map.
    # In addition, it has a text label which marks each section of the physical memory map.
    def displayMap( self, tempPointer, tempColor, tempText, tempPercentage, tempTotalSize ):
        self.tempPointer = int(tempPointer)
        self.tempColor = tempColor
        self.tempText = tempText
        self.tempPercentage = tempPercentage
        self.tempTotalSize = tempTotalSize
        
        if self.tempPercentage != 0:
            self.tempLBL = Label( root , text = "          " * 25 , font = ('Times New Roman', 1),  bg = self.tempColor)
            self.tempLBL.place(x = 80, y = self.yCounter)
            self.yCounter += 7
            self.physicalMemWidgets.append( self.tempLBL )
            
            self.tempLBL = Label( root , text = self.tempText , font = ('Times New Roman', 10),  bg = self.tempColor)
            self.tempLBL.place(x = 350, y = self.yCounter)
            self.physicalMemWidgets.append( self.tempLBL )
        for i in range( int( self.tempPercentage / 2 ) ):
            if self.tempPointer != 0:
                self.tempLBL = Label( root , text = "          " * 25 , font = ('Times New Roman', 1),  bg = self.tempColor)
                self.tempLBL.place(x = 80, y = self.yCounter)
                self.yCounter += 7
                self.physicalMemWidgets.append( self.tempLBL )
                self.tempPointer -= 1
            else:
                pass
        if self.tempPercentage != 0:
            self.tempLBL  =  Label( root , text = tempTotalSize , font = ('Times New Roman', 10),  bg = "#c6e3ad")
            self.tempLBL.place(x = 50, y = self.yCounter - 15)
            self.physicalMemWidgets.append( self.tempLBL )
        return

    def mainMenuBTN_Pressed( self ):
        main.mainMenu_window()

    def aboutUsBTN_Pressed( self ):
        main.aboutUs_window()


    # function which contains widget placements
    # this also takes in the user's input.
    def input1_window( self ):
        root.title ( "Dynamic Best Fit" )
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.dynamicBestFitGB = Label ( root , image = dbf_bg, bg = "black" )
        self.dynamicBestFitGB.place(x = 0, y = 0)
        self.basicWidgetList.append( self.dynamicBestFitGB )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffff01" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffff01")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )

        self.mainMenuBTN  =  Button ( root , image = mainMenu_btn, command = self.mainMenuBTN_Pressed , bg = "#ffff01" )
        self.mainMenuBTN.place (x = 850 ,y = 60)
        self.basicWidgetList.append( self.mainMenuBTN )

        self.aboutBTN  =  Button ( root , image = aboutUs_btn, command = self.aboutUsBTN_Pressed, bg = "#ffff01" )
        self.aboutBTN.place (x = 850 ,y = 10)
        self.basicWidgetList.append( self.aboutBTN )
        
        self.title1LBL  =  Label( root , text = "Best Fit Dynamic" , font = ('Times New Roman', 20),  bg = "#ffff01")
        self.title1LBL.place(x = 100, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Partitioned Allocation" , font = ('Times New Roman', 20),  bg = "#ffff01")
        self.title2LBL.place(x = 75, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Input Window" , font = ('Times New Roman', 30),  bg = "#c6e3ad")
        self.title3LBL.place(x = 355, y = 105)
        self.basicWidgetList.append( self.title3LBL )

        self.jobLBL  =  Label( root , text = "Job" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.jobLBL.place(x = 125, y = 160)
        self.basicWidgetList.append( self.jobLBL )

        self.job1LBL  =  Label( root , text = "1" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job1LBL.place(x = 135, y = 210)
        self.basicWidgetList.append( self.job1LBL )
        
        self.job2LBL  =  Label( root , text = "2" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job2LBL.place(x = 135, y = 260)
        self.basicWidgetList.append( self.job2LBL )
        
        self.job3LBL  =  Label( root , text = "3" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job3LBL.place(x = 135, y = 310)
        self.basicWidgetList.append( self.job3LBL )

        self.job4LBL  =  Label( root , text = "4" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job4LBL.place(x = 135, y = 360)
        self.basicWidgetList.append( self.job4LBL )
        
        self.job5LBL  =  Label( root , text = "5" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job5LBL.place(x = 135, y = 410)
        self.basicWidgetList.append( self.job5LBL )
        
        self.sizeLBL  =  Label( root , text = "Size" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.sizeLBL.place(x = 275, y = 160)
        self.basicWidgetList.append( self.sizeLBL )
        
        self.size1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size1ENTRY.place(x = 225, y = 210)
        self.basicWidgetList.append( self.size1ENTRY )
        
        self.size2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size2ENTRY.place(x = 225, y = 260)
        self.basicWidgetList.append( self.size2ENTRY )
        
        self.size3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size3ENTRY.place(x = 225, y = 310)
        self.basicWidgetList.append( self.size3ENTRY )

        self.size4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size4ENTRY.place(x = 225, y = 360)
        self.basicWidgetList.append( self.size4ENTRY )
        
        self.size5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size5ENTRY.place(x = 225, y = 410)
        self.basicWidgetList.append( self.size5ENTRY )
        
        
        self.arrivalTimeLBL  =  Label( root , text = "Arrival Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.arrivalTimeLBL.place(x = 505, y = 160)
        self.basicWidgetList.append( self.arrivalTimeLBL )

        self.arrivalTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime1ENTRY.place(x = 490, y = 210)
        self.basicWidgetList.append( self.arrivalTime1ENTRY )
        
        self.arrivalTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime2ENTRY.place(x = 490, y = 260)
        self.basicWidgetList.append( self.arrivalTime2ENTRY )
        
        self.arrivalTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime3ENTRY.place(x = 490, y = 310)
        self.basicWidgetList.append( self.arrivalTime3ENTRY )

        self.arrivalTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime4ENTRY.place(x = 490, y = 360)
        self.basicWidgetList.append( self.arrivalTime4ENTRY )
        
        self.arrivalTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime5ENTRY.place(x = 490, y = 410)
        self.basicWidgetList.append( self.arrivalTime5ENTRY )
        
        self.runTimeLBL  =  Label( root , text = "Run Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.runTimeLBL.place(x = 725, y = 160)
        self.basicWidgetList.append( self.runTimeLBL )
        
        self.runTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.runTime1ENTRY.place(x = 700, y = 210)
        self.basicWidgetList.append( self.runTime1ENTRY )
        
        self.runTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.runTime2ENTRY.place(x = 700, y = 260)
        self.basicWidgetList.append( self.runTime2ENTRY )
        
        self.runTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.runTime3ENTRY.place(x = 700, y = 310)
        self.basicWidgetList.append( self.runTime3ENTRY )

        self.runTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.runTime4ENTRY.place(x = 700, y = 360)
        self.basicWidgetList.append( self.runTime4ENTRY )
        
        self.runTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.runTime5ENTRY.place(x = 700, y = 410)
        self.basicWidgetList.append( self.runTime5ENTRY )

        self.memSizeLBL  =  Label( root , text = "Memory Size" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.memSizeLBL.place(x = 150, y = 470)
        self.basicWidgetList.append( self.memSizeLBL )
        
        self.memSizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.memSizeENTRY.place(x = 130, y = 520 )
        self.basicWidgetList.append( self.memSizeENTRY )

        self.osSizeLBL  =  Label( root , text = "OS Size" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.osSizeLBL.place(x = 660, y = 470)
        self.basicWidgetList.append( self.osSizeLBL )
        
        self.osSizeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.osSizeENTRY.place(x = 625, y = 520 )
        self.basicWidgetList.append( self.osSizeENTRY )
        
        self.compactionOptions = [ "Without Compaction" , "With Compaction" ]
        self.compactionChosen = StringVar( root )
        self.compactionChosen.set( self.compactionOptions[0] )

        self.compactionMenu = OptionMenu( root, self.compactionChosen, *self.compactionOptions )
        self.compactionMenu.configure( width = 20 )
        self.compactionMenu.place( x = 390, y = 450 )
        
        self.computeBTN  =  Button ( root , text = 'Compute',command = self.input1_computeBTN_Pressed , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.computeBTN.place (x = 390 ,y = 490)
        self.basicWidgetList.append( self.computeBTN )

        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 540)
        self.basicWidgetList.append( self.exitBTN )


    # Executes once the user presses the compute button in the input1_window
    def input1_computeBTN_Pressed( self ):
        self.clearNodes()
        #print( "Head Node: " , self.headNode )
        #print ( "Input1 Compute BTN Pressed " )
        if messagebox.askyesno( "Confirmation..." , " Are you sure you want to compute? " ) == True :
            self.size1 = self.size1ENTRY.get()
            self.size2 = self.size2ENTRY.get()
            self.size3 = self.size3ENTRY.get()
            self.size4 = self.size4ENTRY.get()
            self.size5 = self.size5ENTRY.get()

            self.memSize = self.memSizeENTRY.get()
            self.osSize = self.osSizeENTRY.get()

            self.memSize_Check = self.isNotInteger( self.memSize )
            self.osSize_Check = self.isNotInteger( self.osSize )
 
            self.size1_Check = self.isNotInteger( self.size1 )
            self.size2_Check = self.isNotInteger( self.size2 )
            self.size3_Check = self.isNotInteger( self.size3 )
            self.size4_Check = self.isNotInteger( self.size4 )
            self.size5_Check = self.isNotInteger( self.size5 )
            
            
            self.arrivalTime1 = self.arrivalTime1ENTRY.get()
            self.arrivalTime2 = self.arrivalTime2ENTRY.get()
            self.arrivalTime3 = self.arrivalTime3ENTRY.get()
            self.arrivalTime4 = self.arrivalTime4ENTRY.get()
            self.arrivalTime5 = self.arrivalTime5ENTRY.get()

            self.arrivalTime1_Check = self.isNotTimeFormat( self.arrivalTime1 )
            self.arrivalTime2_Check = self.isNotTimeFormat( self.arrivalTime2 )
            self.arrivalTime3_Check = self.isNotTimeFormat( self.arrivalTime3 )
            self.arrivalTime4_Check = self.isNotTimeFormat( self.arrivalTime4 )
            self.arrivalTime5_Check = self.isNotTimeFormat( self.arrivalTime5 )

            self.runTime1 = self.runTime1ENTRY.get()
            self.runTime2 = self.runTime2ENTRY.get()
            self.runTime3 = self.runTime3ENTRY.get()
            self.runTime4 = self.runTime4ENTRY.get()
            self.runTime5 = self.runTime5ENTRY.get()
        
            self.runTime1_Check = self.isNotTimeFormat( self.runTime1 )
            self.runTime2_Check = self.isNotTimeFormat( self.runTime2 )
            self.runTime3_Check = self.isNotTimeFormat( self.runTime3 )
            self.runTime4_Check = self.isNotTimeFormat( self.runTime4 )
            self.runTime5_Check = self.isNotTimeFormat( self.runTime5 )

            self.compactionType = self.compactionChosen.get()

            # This condition checks whether the user's inputted values are acceptable.
            # If not, #print the errors.
            if self.memSize_Check or self.osSize_Check :
                #print ( "Error: Invalid Memory or OS Size input." )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Memory or OS Size input." )
            elif int(self.memSize) < int(self.osSize):
                #print ( " Error: Os Size can't exceed Memory Size. " )
                messagebox.showinfo( "Compute Error" , "Error: Os Size can't exceed Memory Size." )
            elif self.size1_Check or self.size2_Check or self.size3_Check or self.size4_Check or self.size5_Check:
                #print ( "Error: Size input detected as not an integer." )
                messagebox.showinfo( "Compute Error" , "Error: Size input detected as not an integer." )
            elif (int(self.size1) > ( int(self.memSize) - int(self.osSize))) or (int(self.size2) > ( int(self.memSize) - int(self.osSize))) or (int(self.size3) > ( int(self.memSize) - int(self.osSize))) or (int(self.size4) > ( int(self.memSize) - int(self.osSize))) or (int(self.size5) > ( int(self.memSize) - int(self.osSize))):
                #print ( "Error: Size input should not exceed ( Memory Size - OS Size )." )
                messagebox.showinfo( "Compute Error" , "Error: Size input should not exceed ( Memory Size - OS Size )." )
            elif self.arrivalTime1_Check or self.arrivalTime2_Check or self.arrivalTime3_Check or self.arrivalTime4_Check or self.arrivalTime5_Check:
                #print ( " Error in arrival time input " )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Arrival Time Input." )
            elif self.runTime1_Check or self.runTime2_Check or self.runTime3_Check or self.runTime4_Check or self.runTime5_Check:
                #print ( "Error: Invalid Run Time Input." )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Run Time Input." )
            else:
                # Job Details [ jobSize, jobNum, arrivalTime, runTime, isjobWaiting ]
                # manipulates the user's input in a format that can be understood by the backEnd class.
                self.jobDetails = [ [ int(self.size1), 1, self.arrivalTime1, self.runTime1, False],
                                    [ int(self.size2), 2, self.arrivalTime2, self.runTime2, False],
                                    [ int(self.size3), 3, self.arrivalTime3, self.runTime3, False],
                                    [ int(self.size4), 4, self.arrivalTime4, self.runTime4, False],
                                    [ int(self.size5), 5, self.arrivalTime5, self.runTime5, False]]
                # Memory [ sizeTaken, F/U( Free,Taken ), -1/jobNum ]
                self.memory = [[( int(self.memSize) - int(self.osSize) ) + 1,'F',-1]]
                # insert_inputs( self, memSpace, osSpace, jobDetails, memory )
                self.bestFit_backEnd.insert_inputs( self.memSize, self.osSize, self.jobDetails, self.memory, self.compactionType )
                self.bestFit_backEnd.generate_summaryTable()
                self.summaryTable_window()
                #print ( " Success " )

    # the window which displays the summary table
    def summaryTable_window( self ):
        self.summaryTable = deepcopy(self.bestFit_backEnd.get_summaryTable())
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.dynamicBestFitGB = Label ( root , image = dbf_bg, bg = "black" )
        self.dynamicBestFitGB.place(x = 0, y = 0)
        self.basicWidgetList.append( self.dynamicBestFitGB )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffff01" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffff01")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )
        
        self.title1LBL  =  Label( root , text = "Best Fit Dynamic" , font = ('Times New Roman', 20),  bg = "#ffff01")
        self.title1LBL.place(x = 100, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Partitioned Allocation" , font = ('Times New Roman', 20),  bg = "#ffff01")
        self.title2LBL.place(x = 75, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Summary Table" , font = ('Times New Roman', 30),  bg = "#c6e3ad")
        self.title3LBL.place(x = 343, y = 105)
        self.basicWidgetList.append( self.title3LBL )

        self.jobLBL  =  Label( root , text = "Job" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.jobLBL.place(x = 125, y = 160)
        self.basicWidgetList.append( self.jobLBL )

        self.job1LBL  =  Label( root , text = "1" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job1LBL.place(x = 135, y = 210)
        self.basicWidgetList.append( self.job1LBL )
        
        self.job2LBL  =  Label( root , text = "2" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job2LBL.place(x = 135, y = 260)
        self.basicWidgetList.append( self.job2LBL )
        
        self.job3LBL  =  Label( root , text = "3" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job3LBL.place(x = 135, y = 310)
        self.basicWidgetList.append( self.job3LBL )

        self.job4LBL  =  Label( root , text = "4" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job4LBL.place(x = 135, y = 360)
        self.basicWidgetList.append( self.job4LBL )
        
        self.job5LBL  =  Label( root , text = "5" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.job5LBL.place(x = 135, y = 410)
        self.basicWidgetList.append( self.job5LBL )
        
        # Start Time Widgets
        self.startTimeLBL  =  Label( root , text = "Start Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.startTimeLBL.place(x = 252, y = 160)
        self.basicWidgetList.append( self.startTimeLBL )
        
        self.startTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.startTime1ENTRY.place(x = 225, y = 210)
        self.startTime1ENTRY.insert( 0, self.summaryTable[1][1].time() )
        self.startTime1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.startTime1ENTRY )
        
        self.startTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.startTime2ENTRY.place(x = 225, y = 260)
        self.startTime2ENTRY.insert( 0, self.summaryTable[2][1].time() )
        self.startTime2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.startTime2ENTRY )
        
        self.startTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.startTime3ENTRY.place(x = 225, y = 310)
        self.startTime3ENTRY.insert( 0, self.summaryTable[3][1].time() )
        self.startTime3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.startTime3ENTRY )

        self.startTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.startTime4ENTRY.place(x = 225, y = 360)
        self.startTime4ENTRY.insert( 0, self.summaryTable[4][1].time() )
        self.startTime4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.startTime4ENTRY )
        
        self.startTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.startTime5ENTRY.place(x = 225, y = 410)
        self.startTime5ENTRY.insert( 0, self.summaryTable[5][1].time() )
        self.startTime5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.startTime5ENTRY )
        
        # Finish Time Widgets
        self.finishTimeLBL  =  Label( root , text = "Finish Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.finishTimeLBL.place(x = 512, y = 160)
        self.basicWidgetList.append( self.finishTimeLBL )

        self.finishTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.finishTime1ENTRY.place(x = 490, y = 210)
        self.finishTime1ENTRY.insert( 0, self.summaryTable[1][2].time() )
        self.finishTime1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.finishTime1ENTRY )
        
        self.finishTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.finishTime2ENTRY.place(x = 490, y = 260)
        self.finishTime2ENTRY.insert( 0, self.summaryTable[2][2].time() )
        self.finishTime2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.finishTime2ENTRY )
        
        self.finishTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.finishTime3ENTRY.place(x = 490, y = 310)
        self.finishTime3ENTRY.insert( 0, self.summaryTable[3][2].time() )
        self.finishTime3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.finishTime3ENTRY )

        self.finishTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.finishTime4ENTRY.place(x = 490, y = 360)
        self.finishTime4ENTRY.insert( 0, self.summaryTable[4][2].time() )
        self.finishTime4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.finishTime4ENTRY )
        
        self.finishTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.finishTime5ENTRY.place(x = 490, y = 410)
        self.finishTime5ENTRY.insert( 0, self.summaryTable[5][2].time() )
        self.finishTime5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.finishTime5ENTRY )
        
        # CPU Wait Widgets
        self.cpuWaitLBL  =  Label( root , text = "CPU Wait" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.cpuWaitLBL.place(x = 725, y = 160)
        self.basicWidgetList.append( self.cpuWaitLBL )
        
        self.cpuWait1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuWait1ENTRY.place(x = 700, y = 210)
        self.cpuWait1ENTRY.insert( 0, self.summaryTable[1][3] )
        self.cpuWait1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.cpuWait1ENTRY )
        
        self.cpuWait2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuWait2ENTRY.place(x = 700, y = 260)
        self.cpuWait2ENTRY.insert( 0, self.summaryTable[2][3] )
        self.cpuWait2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.cpuWait2ENTRY )
        
        self.cpuWait3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuWait3ENTRY.place(x = 700, y = 310)
        self.cpuWait3ENTRY.insert( 0, self.summaryTable[3][3] )
        self.cpuWait3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.cpuWait3ENTRY )

        self.cpuWait4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuWait4ENTRY.place(x = 700, y = 360)
        self.cpuWait4ENTRY.insert( 0, self.summaryTable[4][3] )
        self.cpuWait4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.cpuWait4ENTRY )
        
        self.cpuWait5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuWait5ENTRY.place(x = 700, y = 410)
        self.cpuWait5ENTRY.insert( 0, self.summaryTable[5][3] )
        self.cpuWait5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.cpuWait5ENTRY )

        # Buttons
        self.backBTN  =  Button ( root , text = 'BACK',command = self.input1_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 200 ,y = 470)
        self.basicWidgetList.append( self.backBTN )
        self.nextBTN  =  Button ( root , text = 'NEXT',command = self.summaryTable_nextBTN_Pressed , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.nextBTN.place (x = 580 ,y = 470)
        self.basicWidgetList.append( self.nextBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 470)
        self.basicWidgetList.append( self.exitBTN )

    # This executes if the user presses the next button in the summaryTable window.
    def summaryTable_nextBTN_Pressed( self ):
        self.clearNodes()
        #print( "Summary Table nextBTN Pressed " )
        self.tempMemoryResults = deepcopy(self.bestFit_backEnd.get_memoryResults())
        self.tempMemoryResults_time = deepcopy(self.bestFit_backEnd.get_memoryResults_time())
        for i in range(len( self.tempMemoryResults ) - 1, -1, -1):
            self.addResultNode( self.tempMemoryResults[i], self.tempMemoryResults_time[i], self.osSize, self.memSize )
        if self.headNode != None:
            self.headNode.memMap_window()
        

# This is a node class for the linked list
# the linked list contains the nodes which hosts the memory map, fat, and pat windows.
class dynamic_bestFitNode_frontEnd:
    def __init__ ( self, memoryResult = None, memoryResult_time = None, osSize = None, memSize = None):
        self.backPointer = None
        self.nextPointer = None
        self.patData = []
        self.fatData = []
        self.location = 0
        
        if memoryResult == None:
            self.memoryResult = [[500, "U", 1], [109, "F", -1]]
        else:
            self.memoryResult = memoryResult
                   
        if memoryResult_time == None:
            self.memoryResult_time = [ "09:00:00", ["Arrived(J1)", "Started(J1)"]]
        else:
            self.memoryResult_time = memoryResult_time

        if osSize == None:
            self.osSize = 32
        else:
            self.osSize = int(osSize)

        if memSize == None:
            self.memSize = 640
        else:
            self.memSize = int(memSize)

        self.location += int(self.osSize)
        self.tempColors = [ "#f77777", "#f7d977", "#77f7e6", "#77d5f7", "#d577f7", "#77d567", "#d5987" ]
        self.tempColorCounter = 0
        self.tempPercentage = float(( float(self.osSize) / float(self.memSize) ) * 100 )
        self.memMap_data = [ [ self.tempPercentage, "#f5f3ed", "OS Size", self.tempPercentage, self.location, self.osSize ] ]
        self.availableCounter = 1
        self.pCounter = 1
        for certainResult in self.memoryResult:
            if certainResult[1] == "U":
                if self.location+certainResult[0] > self.memSize:
                    self.patData.append( [ certainResult[0] - 1, self.location, "Allocated(J{})".format( certainResult[2] ) ] )
                else:
                    self.patData.append( [ certainResult[0], self.location, "Allocated(J{})".format( certainResult[2] ) ] )
                self.location += int(certainResult[0])
                self.tempPercentage = float(( float(certainResult[0]) / float(self.memSize) ) * 100 )
                self.memMap_data.append( [ self.tempPercentage, self.tempColors[self.tempColorCounter], "Allocated(P{})".format( self.pCounter), self.tempPercentage, self.location, certainResult[0] ])
                self.tempColorCounter += 1
                self.pCounter += 1
            else:
                if self.location+certainResult[0] > self.memSize:
                    self.fatData.append( [ certainResult[0] - 1, self.location, "Available" ] )
                    self.location += int(certainResult[0])
                    #print ( "Available Counter: ", self.availableCounter )
                    self.tempPercentage = float(( float(certainResult[0]) / float(self.memSize) ) * 100 )
                    if certainResult[0] == 1:
                        pass
                    else:
                        self.memMap_data.append( [ self.tempPercentage, self.tempColors[self.tempColorCounter], "Available(F{})".format(self.availableCounter), self.tempPercentage, self.location - 1, certainResult[0] - 1 ])
                else:
                    self.fatData.append( [ certainResult[0], self.location, "Available" ] )
                    self.location += int(certainResult[0])
                    #print ( "Available Counter: ", self.availableCounter )
                    self.tempPercentage = float(( float(certainResult[0]) / float(self.memSize) ) * 100 )
                    if certainResult[0] == 1:
                        pass
                    else:
                        self.memMap_data.append( [ self.tempPercentage, self.tempColors[self.tempColorCounter], "Available(F{})".format(self.availableCounter), self.tempPercentage, self.location, certainResult[0] ])
                    
                self.tempColorCounter += 1
                self.availableCounter += 1


        self.countPatData = len( self.patData )
        if self.countPatData != 5:
            for i in range( 5 - self.countPatData ):
                self.patData.append( ["---", "---", "---"] )
        self.countFatData = len( self.fatData )
        if self.countFatData != 5:
            for i in range( 5 - self.countFatData ):
                self.fatData.append( ["---", "---", "---"] )

        ##print( self.memMap_data )
        ##print( self.fatData )

        self.memMap_data2 = deepcopy( self.memMap_data )
        self.tempCount = len( self.memMap_data2 )
        if self.tempCount != 7:
            for i in range( 7 - self.tempCount ):
                self.memMap_data2.append([ "---", "#c6e3ad", "---", "---", "---", "---" ])
        #print( self.memMap_data2 )

        # displayMap( self, tempPointer, tempColor, tempText, tempPercentage, tempTotalSize, memSize )

        

            

    # For getting the current date
    def current_date( self ):
        self.dateString  =  datetime.date.today().strftime("%B %d, %Y")
        self.dateLBL.config(text = self.dateString)

    # This updates the clock widget
    def tick( self ):
        if self.tick_on:
            self.timeString  =  time.strftime("%H:%M:%S")
            self.clockLBL.config(text = self.timeString)
            self.clockLBL.after(200, self.tick )
        else:
            pass

    # The program has two list which contains a reference to all the program's widgets
    # And what this function does is it tries to clear/destroy all of these widgets
    # using the lists which contains the program's widgets.
    # The two lists are:
    #   - self.basicWidgetList: For most of the basic widgets
    #   - self.physicalMemWidgets: For the widgets used to display physical memory map
    def clearWidgets( self ):
        try:
            self.tick_on = False
            self.clearWidgetList( self.basicWidgetList )
            self.clearWidgetList( self.physicalMemWidgets )
        except:
            pass
        return


    # This function destroys all of the widgets inside the inputted widgetsToClear list.
    def clearWidgetList ( self, widgetsToClear):
        for widget in widgetsToClear:
            widget.destroy()

            
    # This function displays the necessary widgets for physical memory map.
    # To get a general gist, the program has around 50 labels which acts as the physical memory map.
    # In addition, it has a text label which marks each section of the physical memory map.
    def displayMap( self, tempPointer, tempColor, tempText, tempPercentage, tempTotalSize ):
        self.tempPointer = int(tempPointer)
        self.tempColor = tempColor
        self.tempText = tempText
        self.tempPercentage = tempPercentage
        self.tempTotalSize = tempTotalSize
        
        if self.tempPercentage != 0:
            self.tempLBL = Label( root , text = "          " * 25 , font = ('Times New Roman', 1),  bg = self.tempColor)
            self.tempLBL.place(x = 80, y = self.yCounter)
            self.yCounter += 7
            self.physicalMemWidgets.append( self.tempLBL )
            
            self.tempLBL = Label( root , text = self.tempText , font = ('Times New Roman', 10),  bg = self.tempColor)
            self.tempLBL.place(x = 350, y = self.yCounter)
            self.physicalMemWidgets.append( self.tempLBL )
        for i in range( int( self.tempPercentage / 2 ) ):
            if self.tempPointer != 0:
                self.tempLBL = Label( root , text = "          " * 25 , font = ('Times New Roman', 1),  bg = self.tempColor)
                self.tempLBL.place(x = 80, y = self.yCounter)
                self.yCounter += 7
                self.physicalMemWidgets.append( self.tempLBL )
                self.tempPointer -= 1
            else:
                pass
        if self.tempPercentage != 0:
            self.tempLBL  =  Label( root , text = tempTotalSize , font = ('Times New Roman', 10),  bg = "#c6e3ad")
            self.tempLBL.place(x = 50, y = self.yCounter - 15)
            self.physicalMemWidgets.append( self.tempLBL )

        return

    def memMap_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.dynamicBestFitGB = Label ( root , image = dbf_bg, bg = "black" )
        self.dynamicBestFitGB.place(x = 0, y = 0)
        self.basicWidgetList.append( self.dynamicBestFitGB )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffff01" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffff01")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )

        self.title1LBL  =  Label( root , text = "Best Fit Dynamic" , font = ('Times New Roman', 20),  bg = "#ffff01")
        self.title1LBL.place(x = 100, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Partitioned Allocation" , font = ('Times New Roman', 20),  bg = "#ffff01")
        self.title2LBL.place(x = 75, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Memory Map Data" , font = ('Times New Roman', 20),  bg = "#c6e3ad")
        self.title3LBL.place(x = 530, y = 106)
        self.basicWidgetList.append( self.title3LBL )

        self.title4LBL  =  Label( root , text = "At {}".format( self.memoryResult_time[0] ) , font = ('Times New Roman', 12),  bg = "#c6e3ad")
        self.title4LBL.place(x = 608, y = 138)
        self.basicWidgetList.append( self.title4LBL )
        
        self.physicalMemWidgets = []
        self.yCounter = 140
        self.indexPointer = 0
        
        self.markLBL  =  Label( root , text = 0 , font = ('Times New Roman', 10),  bg = "#c6e3ad")
        self.markLBL.place(x = 60, y = self.yCounter - 20)
        self.physicalMemWidgets.append( self.markLBL )

        for tempData in self.memMap_data:
            self.displayMap( tempData[0], tempData[1], tempData[2], tempData[3], tempData[4] )

        self.partitionLBL  =  Label( root , text = "#" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.partitionLBL.place(x = 440, y = 160)
        self.basicWidgetList.append( self.partitionLBL )

        self.partition1LBL  =  Label( root , text = "1" , font = ('Times New Roman', 15),  bg = self.memMap_data2[0][1])
        self.partition1LBL.place(x = 440, y = 210)
        self.basicWidgetList.append( self.partition1LBL )
        
        self.partition2LBL  =  Label( root , text = "2" , font = ('Times New Roman', 15),  bg = self.memMap_data2[1][1])
        self.partition2LBL.place(x = 440, y = 260)
        self.basicWidgetList.append( self.partition2LBL )
        
        self.partition3LBL  =  Label( root , text = "3" , font = ('Times New Roman', 15),  bg = self.memMap_data2[2][1])
        self.partition3LBL.place(x = 440, y = 310)
        self.basicWidgetList.append( self.partition3LBL )
        
        self.partition4LBL  =  Label( root , text = "4" , font = ('Times New Roman', 15),  bg = self.memMap_data2[3][1])
        self.partition4LBL.place(x = 440, y = 360)
        self.basicWidgetList.append( self.partition4LBL )
        
        self.partition5LBL  =  Label( root , text = "5" , font = ('Times New Roman', 15),  bg = self.memMap_data2[4][1])
        self.partition5LBL.place(x = 440, y = 410)
        self.basicWidgetList.append( self.partition5LBL )

        self.partition6LBL  =  Label( root , text = "6" , font = ('Times New Roman', 15),  bg = self.memMap_data2[5][1])
        self.partition6LBL.place(x = 440, y = 460)
        self.basicWidgetList.append( self.partition6LBL )
        
        self.partition7LBL  =  Label( root , text = "7" , font = ('Times New Roman', 15),  bg = self.memMap_data2[6][1])
        self.partition7LBL.place(x = 440, y = 510)
        self.basicWidgetList.append( self.partition7LBL )


        # Size Widgets
        self.sizeLBL  =  Label( root , text = "Size" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.sizeLBL.place(x = 580, y = 160)
        self.basicWidgetList.append( self.sizeLBL )

        self.size1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size1ENTRY.place(x = 530, y = 210)
        self.size1ENTRY.insert( 0, self.memMap_data2[0][5] )
        self.size1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.size1ENTRY )
        
        self.size2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size2ENTRY.place(x = 530, y = 260)
        self.size2ENTRY.insert( 0, self.memMap_data2[1][5] )
        self.size2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.size2ENTRY )
        
        self.size3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size3ENTRY.place(x = 530, y = 310)
        self.size3ENTRY.insert( 0, self.memMap_data2[2][5] )
        self.size3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.size3ENTRY )
        
        self.size4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size4ENTRY.place(x = 530, y = 360)
        self.size4ENTRY.insert( 0, self.memMap_data2[3][5] )
        self.size4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.size4ENTRY )
        
        self.size5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size5ENTRY.place(x = 530, y = 410)
        self.size5ENTRY.insert( 0, self.memMap_data2[4][5] )
        self.size5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.size5ENTRY )

        self.size6ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size6ENTRY.place(x = 530, y = 460)
        self.size6ENTRY.insert( 0, self.memMap_data2[5][5] )
        self.size6ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.size6ENTRY )
        
        self.size7ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.size7ENTRY.place(x = 530, y = 510)
        self.size7ENTRY.insert( 0, self.memMap_data2[6][5] )
        self.size7ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.size7ENTRY )


        # Status Widgets
        self.statusLBL  =  Label( root , text = "Status" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.statusLBL.place(x = 740, y = 160)
        self.basicWidgetList.append( self.statusLBL )
        
        self.status1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.status1ENTRY.place(x = 700, y = 210)
        self.status1ENTRY.insert( 0, self.memMap_data2[0][2] )
        self.status1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.status1ENTRY )
        
        self.status2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.status2ENTRY.place(x = 700, y = 260)
        self.status2ENTRY.insert( 0, self.memMap_data2[1][2] )
        self.status2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.status2ENTRY )
        
        self.status3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.status3ENTRY.place(x = 700, y = 310)
        self.status3ENTRY.insert( 0, self.memMap_data2[2][2] )
        self.status3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.status3ENTRY )
        
        self.status4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.status4ENTRY.place(x = 700, y = 360)
        self.status4ENTRY.insert( 0, self.memMap_data2[3][2] )
        self.status4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.status4ENTRY )
        
        self.status5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.status5ENTRY.place(x = 700, y = 410)
        self.status5ENTRY.insert( 0, self.memMap_data2[4][2] )
        self.status5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.status5ENTRY )

        self.status6ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.status6ENTRY.place(x = 700, y = 460)
        self.status6ENTRY.insert( 0, self.memMap_data2[5][2] )
        self.status6ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.status6ENTRY )
        
        self.status7ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.status7ENTRY.place(x = 700, y = 510)
        self.status7ENTRY.insert( 0, self.memMap_data2[6][2] )
        self.status7ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.status7ENTRY )

        self.backBTN  =  Button ( root , text = 'BACK',command = self.memMap_backBTN_Pressed , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 200 ,y = 540)
        self.basicWidgetList.append( self.backBTN )
        self.nextBTN  =  Button ( root , text = 'NEXT',command = self.pat_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.nextBTN.place (x = 580 ,y = 540)
        self.basicWidgetList.append( self.nextBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 540)
        self.basicWidgetList.append( self.exitBTN )

    def memMap_backBTN_Pressed( self ):
        #print ( "memMap_backBTN_Pressed" )
        if self.backPointer != None:
            self.backPointer.fat_window()
        else:
            dbf_program.summaryTable_window()

    def pat_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.dynamicBestFitGB = Label ( root , image = dbf_bg, bg = "black" )
        self.dynamicBestFitGB.place(x = 0, y = 0)
        self.basicWidgetList.append( self.dynamicBestFitGB )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffff01" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffff01")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )
        
        self.title1LBL  =  Label( root , text = "Best Fit Dynamic" , font = ('Times New Roman', 20),  bg = "#ffff01")
        self.title1LBL.place(x = 100, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Partitioned Allocation" , font = ('Times New Roman', 20),  bg = "#ffff01")
        self.title2LBL.place(x = 75, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Partion Allocation Table" , font = ('Times New Roman', 30),  bg = "#c6e3ad")
        self.title3LBL.place(x = 270, y = 105)
        self.basicWidgetList.append( self.title3LBL )

        self.title4LBL  =  Label( root , text = "At {}".format( self.memoryResult_time[0] ) , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.title4LBL.place(x = 425, y = 155)
        self.basicWidgetList.append( self.title4LBL )
        

        # PAT Number Widgets
        self.patNumLBL  =  Label( root , text = "Partition #" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.patNumLBL.place(x = 100, y = 180)
        self.basicWidgetList.append( self.patNumLBL )

        self.patNum1LBL  =  Label( root , text = "1" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.patNum1LBL.place(x = 135, y = 220)
        self.basicWidgetList.append( self.patNum1LBL )
        
        self.patNum2LBL  =  Label( root , text = "2" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.patNum2LBL.place(x = 135, y = 260)
        self.basicWidgetList.append( self.patNum2LBL )
        
        self.patNum3LBL  =  Label( root , text = "3" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.patNum3LBL.place(x = 135, y = 300)
        self.basicWidgetList.append( self.patNum3LBL )

        self.patNum4LBL  =  Label( root , text = "4" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.patNum4LBL.place(x = 135, y = 340)
        self.basicWidgetList.append( self.patNum4LBL )
        
        self.patNum5LBL  =  Label( root , text = "5" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.patNum5LBL.place(x = 135, y = 380)
        self.basicWidgetList.append( self.patNum5LBL )
        
        # PAT Size Widgets
        self.patSizeLBL  =  Label( root , text = "Size" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.patSizeLBL.place(x = 277, y = 180)
        self.basicWidgetList.append( self.patSizeLBL )
        
        self.patSize1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patSize1ENTRY.place(x = 225, y = 220)
        self.patSize1ENTRY.insert( 0, self.patData[0][0] )
        self.patSize1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patSize1ENTRY )
        
        self.patSize2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patSize2ENTRY.place(x = 225, y = 260)
        self.patSize2ENTRY.insert( 0, self.patData[1][0] )
        self.patSize2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patSize2ENTRY )
        
        self.patSize3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patSize3ENTRY.place(x = 225, y = 300)
        self.patSize3ENTRY.insert( 0, self.patData[2][0] )
        self.patSize3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patSize3ENTRY )

        self.patSize4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patSize4ENTRY.place(x = 225, y = 340)
        self.patSize4ENTRY.insert( 0, self.patData[3][0] )
        self.patSize4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patSize4ENTRY )
        
        self.patSize5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patSize5ENTRY.place(x = 225, y = 380)
        self.patSize5ENTRY.insert( 0, self.patData[4][0] )
        self.patSize5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patSize5ENTRY )
        
        # PAT Location Widgets
        self.patLocationLBL  =  Label( root , text = "Location" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.patLocationLBL.place(x = 522, y = 180)
        self.basicWidgetList.append( self.patLocationLBL )

        self.patLocation1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patLocation1ENTRY.place(x = 490, y = 220)
        self.patLocation1ENTRY.insert( 0, self.patData[0][1] )
        self.patLocation1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patLocation1ENTRY )
        
        self.patLocation2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patLocation2ENTRY.place(x = 490, y = 260)
        self.patLocation2ENTRY.insert( 0, self.patData[1][1] )
        self.patLocation2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patLocation2ENTRY )
        
        self.patLocation3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patLocation3ENTRY.place(x = 490, y = 300)
        self.patLocation3ENTRY.insert( 0, self.patData[2][1] )
        self.patLocation3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patLocation3ENTRY )

        self.patLocation4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patLocation4ENTRY.place(x = 490, y = 340)
        self.patLocation4ENTRY.insert( 0, self.patData[3][1] )
        self.patLocation4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patLocation4ENTRY )
        
        self.patLocation5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patLocation5ENTRY.place(x = 490, y = 380)
        self.patLocation5ENTRY.insert( 0, self.patData[4][1] )
        self.patLocation5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patLocation5ENTRY )
        
        # PAT Status Widgets
        self.patStatusLBL  =  Label( root , text = "Status" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.patStatusLBL.place(x = 740, y = 180)
        self.basicWidgetList.append( self.patStatusLBL )
        
        self.patStatus1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patStatus1ENTRY.place(x = 700, y = 220)
        self.patStatus1ENTRY.insert( 0, self.patData[0][2] )
        self.patStatus1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patStatus1ENTRY )
        
        self.patStatus2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patStatus2ENTRY.place(x = 700, y = 260)
        self.patStatus2ENTRY.insert( 0, self.patData[1][2] )
        self.patStatus2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patStatus2ENTRY )
        
        self.patStatus3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patStatus3ENTRY.place(x = 700, y = 300)
        self.patStatus3ENTRY.insert( 0, self.patData[2][2] )
        self.patStatus3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patStatus3ENTRY )

        self.patStatus4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patStatus4ENTRY.place(x = 700, y = 340)
        self.patStatus4ENTRY.insert( 0, self.patData[3][2] )
        self.patStatus4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patStatus4ENTRY )
        
        self.patStatus5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.patStatus5ENTRY.place(x = 700, y = 380)
        self.patStatus5ENTRY.insert( 0, self.patData[4][2] )
        self.patStatus5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.patStatus5ENTRY )

        # Listbox Widgets

        self.patListbox1 = Listbox( root, height = 6, width = 40, border = 0, justify = "center" )
        self.patListbox1.place( x = 220, y = 430 )
        self.basicWidgetList.append( self.patListbox1 )
        self.patListbox2 = Listbox( root, height = 6, width = 40, border = 0, justify = "center" )
        self.patListbox2.place( x = 480, y = 430 )
        self.basicWidgetList.append( self.patListbox2 )

        self.tempCount1 = 0
        self.tempCount2 = 0
        for allocation in self.memoryResult_time[1]:
            if allocation[0] == "A":
                self.tempCount1 += 1
                self.patListbox1.insert( self.tempCount1, allocation )
            else:
                self.tempCount2 += 1
                self.patListbox2.insert( self.tempCount2, allocation )

        # Buttons
        self.backBTN  =  Button ( root , text = 'Back',command = self.memMap_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 200 ,y = 540)
        self.basicWidgetList.append( self.backBTN )
        self.nextBTN  =  Button ( root , text = 'Next',command = self.fat_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.nextBTN.place (x = 580 ,y = 540)
        self.basicWidgetList.append( self.nextBTN )

        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 540)
        self.basicWidgetList.append( self.exitBTN )


    def fat_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.dynamicBestFitGB = Label ( root , image = dbf_bg, bg = "black" )
        self.dynamicBestFitGB.place(x = 0, y = 0)
        self.basicWidgetList.append( self.dynamicBestFitGB )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffff01" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#ffff01")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )
        
        self.title1LBL  =  Label( root , text = "Best Fit Dynamic" , font = ('Times New Roman', 20),  bg = "#ffff01")
        self.title1LBL.place(x = 100, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Partitioned Allocation" , font = ('Times New Roman', 20),  bg = "#ffff01")
        self.title2LBL.place(x = 75, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "File Allocation Table" , font = ('Times New Roman', 30),  bg = "#c6e3ad")
        self.title3LBL.place(x = 305, y = 105)
        self.basicWidgetList.append( self.title3LBL )
        self.title4LBL  =  Label( root , text = "At {}".format( self.memoryResult_time[0] ) , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.title4LBL.place(x = 425, y = 155)
        self.basicWidgetList.append( self.title4LBL )

        # fat Number Widgets
        self.fatNumLBL  =  Label( root , text = "FA #" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.fatNumLBL.place(x = 123, y = 180)
        self.basicWidgetList.append( self.fatNumLBL )

        self.fatNum1LBL  =  Label( root , text = "1" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.fatNum1LBL.place(x = 135, y = 220)
        self.basicWidgetList.append( self.fatNum1LBL )
        
        self.fatNum2LBL  =  Label( root , text = "2" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.fatNum2LBL.place(x = 135, y = 260)
        self.basicWidgetList.append( self.fatNum2LBL )
        
        self.fatNum3LBL  =  Label( root , text = "3" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.fatNum3LBL.place(x = 135, y = 300)
        self.basicWidgetList.append( self.fatNum3LBL )

        self.fatNum4LBL  =  Label( root , text = "4" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.fatNum4LBL.place(x = 135, y = 340)
        self.basicWidgetList.append( self.fatNum4LBL )
        
        self.fatNum5LBL  =  Label( root , text = "5" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.fatNum5LBL.place(x = 135, y = 380)
        self.basicWidgetList.append( self.fatNum5LBL )
        
        # fat Size Widgets
        self.fatSizeLBL  =  Label( root , text = "Size" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.fatSizeLBL.place(x = 277, y = 180)
        self.basicWidgetList.append( self.fatSizeLBL )
        
        self.fatSize1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatSize1ENTRY.place(x = 225, y = 220)
        self.fatSize1ENTRY.insert( 0, self.fatData[0][0] )
        self.fatSize1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatSize1ENTRY )
        
        self.fatSize2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatSize2ENTRY.place(x = 225, y = 260)
        self.fatSize2ENTRY.insert( 0, self.fatData[1][0] )
        self.fatSize2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatSize2ENTRY )
        
        self.fatSize3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatSize3ENTRY.place(x = 225, y = 300)
        self.fatSize3ENTRY.insert( 0, self.fatData[2][0] )
        self.fatSize3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatSize3ENTRY )

        self.fatSize4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatSize4ENTRY.place(x = 225, y = 340)
        self.fatSize4ENTRY.insert( 0, self.fatData[3][0] )
        self.fatSize4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatSize4ENTRY )
        
        self.fatSize5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatSize5ENTRY.place(x = 225, y = 380)
        self.fatSize5ENTRY.insert( 0, self.fatData[4][0] )
        self.fatSize5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatSize5ENTRY )
        
        # fat Location Widgets
        self.fatLocationLBL  =  Label( root , text = "Location" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.fatLocationLBL.place(x = 522, y = 180)
        self.basicWidgetList.append( self.fatLocationLBL )

        self.fatLocation1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatLocation1ENTRY.place(x = 490, y = 220)
        self.fatLocation1ENTRY.insert( 0, self.fatData[0][1] )
        self.fatLocation1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatLocation1ENTRY )
        
        self.fatLocation2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatLocation2ENTRY.place(x = 490, y = 260)
        self.fatLocation2ENTRY.insert( 0, self.fatData[1][1] )
        self.fatLocation2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatLocation2ENTRY )
        
        self.fatLocation3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatLocation3ENTRY.place(x = 490, y = 300)
        self.fatLocation3ENTRY.insert( 0, self.fatData[2][1] )
        self.fatLocation3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatLocation3ENTRY )

        self.fatLocation4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatLocation4ENTRY.place(x = 490, y = 340)
        self.fatLocation4ENTRY.insert( 0, self.fatData[3][1] )
        self.fatLocation4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatLocation4ENTRY )
        
        self.fatLocation5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatLocation5ENTRY.place(x = 490, y = 380)
        self.fatLocation5ENTRY.insert( 0, self.fatData[4][1] )
        self.fatLocation5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatLocation5ENTRY )
        
        # fat Status Widgets
        self.fatStatusLBL  =  Label( root , text = "Status" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.fatStatusLBL.place(x = 740, y = 180)
        self.basicWidgetList.append( self.fatStatusLBL )
        
        self.fatStatus1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatStatus1ENTRY.place(x = 700, y = 220)
        self.fatStatus1ENTRY.insert( 0, self.fatData[0][2] )
        self.fatStatus1ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatStatus1ENTRY )
        
        self.fatStatus2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatStatus2ENTRY.place(x = 700, y = 260)
        self.fatStatus2ENTRY.insert( 0, self.fatData[1][2] )
        self.fatStatus2ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatStatus2ENTRY )
        
        self.fatStatus3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatStatus3ENTRY.place(x = 700, y = 300)
        self.fatStatus3ENTRY.insert( 0, self.fatData[2][2] )
        self.fatStatus3ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatStatus3ENTRY )

        self.fatStatus4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatStatus4ENTRY.place(x = 700, y = 340)
        self.fatStatus4ENTRY.insert( 0, self.fatData[3][2] )
        self.fatStatus4ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatStatus4ENTRY )
        
        self.fatStatus5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.fatStatus5ENTRY.place(x = 700, y = 380)
        self.fatStatus5ENTRY.insert( 0, self.fatData[4][2] )
        self.fatStatus5ENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.fatStatus5ENTRY )

        # Listbox Widgets

        self.fatListbox1 = Listbox( root, height = 6, width = 40, border = 0, justify = "center" )
        self.fatListbox1.place( x = 220, y = 430 )
        self.basicWidgetList.append( self.fatListbox1 )
        self.fatListbox2 = Listbox( root, height = 6, width = 40, border = 0, justify = "center" )
        self.fatListbox2.place( x = 480, y = 430 )
        self.basicWidgetList.append( self.fatListbox2 )

        self.tempCount1 = 0
        self.tempCount2 = 0
        for allocation in self.memoryResult_time[1]:
            if allocation[0] == "A":
                self.tempCount1 += 1
                self.fatListbox1.insert( self.tempCount1, allocation )
            else:
                self.tempCount2 += 1
                self.fatListbox2.insert( self.tempCount2, allocation )

        # Buttons
        self.backBTN  =  Button ( root , text = 'Back',command = self.pat_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 200 ,y = 540)
        self.basicWidgetList.append( self.backBTN )
        self.nextBTN  =  Button ( root , text = 'Next',command = self.fat_nextBTN_Pressed , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        if self.nextPointer == None:
            self.nextBTN.configure( text = "Try New Input", width = 13 )
        self.nextBTN.place (x = 580 ,y = 540)
        self.basicWidgetList.append( self.nextBTN )

        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 540)
        self.basicWidgetList.append( self.exitBTN )

    def fat_nextBTN_Pressed( self ):
        if self.nextPointer == None:
            dbf_program.input1_window()
        else:
            self.nextPointer.memMap_window()
# END OF DBF PROGRAM: 4435-6027

# FCFS PROGRAM: 6101-6580

# This class contains all the back end processes/computations.
class fcfs_backEnd:
    def __init__( self ):
        # process details [ processNum, burstTime, arrivalTime ]
        self.processDetails = { 1 : [ "P1", 10, 10 ],
                                2 : [ "P2", 1, 5],
                                3 : [ "P3", 2, 8],
                                4 : [ "P4", 5, 6]}
        self.process_queue = []
        self.numOfProcess = 0
        for i in range ( 1, len( list(self.processDetails )) + 1):
            self.numOfProcess += 1
            self.process_queue.append( self.processDetails[i] )

    # For accepting in the user's input that will be utilized by the backend class.
    def insert_inputs( self, processDetails = None ):
        # process details [ processNum, burstTime, arrivalTime ]
        if processDetails == None:
            self.processDetails = { 1 : [ "P1", 7, 5 ],
                                    2 : [ "P2", 10, 0],
                                    3 : [ "P3", 5, 8] }
        else:
            self.processDetails = processDetails
        self.process_queue = []
        self.numOfProcess = 0
        for i in range ( 1, len( list(self.processDetails )) + 1):
            self.numOfProcess += 1
            self.process_queue.append( self.processDetails[i] )

    # returns the ganttChart list
    def get_ganttChart( self ):
        return self.ganttChart

    # returns the caa list which contains CPU Utilization, ATA, AWT.
    def get_caa( self ):
        return self.caa
    
    def generate_ganttChart( self ):
        # gantt chart [ start, finish, processNum, arrivalTime, burstTime, percentageprocess ]
        self.ganttChart = []
        
        # sort the process_queue by its arrival time.
        # process queue [ processNum, burstTime, arrivalTime ]
        self.process_queue = sorted( self.process_queue, key=lambda x: x[2] )
        self.completionTime = 0
        self.idleTime = 0
        self.ata = float(0)
        self.awt = float(0)
        self.tempColors = [ "#f77777", "#f7d977", "#77f7e6", "#77d5f7", "#d577f7", "#fcba03" ]
        self.tempColorsCounter = 0
        #print( len(self.process_queue) )
        
        # Traverse the process_queue list to generate the necessary computations
        for i in range( len(self.process_queue) ):
            # if there's a gap/idle period in the process queue, execute the computations for idle.
            # also, append the necessary idle data into the gantt chart.
            if self.process_queue[i][2] > 0 and (i == 0 or self.completionTime < self.process_queue[i][2]):
                #print( i )
                try:
                    self.ganttChart.append( [self.completionTime,self.process_queue[i][2], "Idle",self.completionTime , self.process_queue[i][2] - self.completionTime, "#bfbaac"] )
                except:
                    pass
                self.idleTime += (self.process_queue[i][2] - self.completionTime)
                self.completionTime = self.process_queue[i][2]
                #print(self.process_queue[i][2] - self.completionTime )
            self.ata += float((self.completionTime + self.process_queue[i][1]) - self.process_queue[i][2] )
            self.awt += float((self.completionTime) - self.process_queue[i][2] )
            # append the computations/data for a certain process in the process queue.
            try:
                self.ganttChart.append( [self.completionTime, self.completionTime + self.process_queue[i][1], self.process_queue[i][0], self.process_queue[i][2], self.process_queue[i][1], self.tempColors[self.tempColorsCounter]] )
            except:
                #print( "fail", self.process_queue[i] )
                pass
            self.completionTime += self.process_queue[i][1]
            self.tempColorsCounter += 1

        #print ( "idle time: ", self.idleTime )
        #print( "completion time: ", self.completionTime )

        # add/append the necessary data that will be used by displayChart function in the frontEnd.
        for i in range( len(self.ganttChart) ):
            self.ganttChart[i].append( float(( float(self.ganttChart[i][4]) / float(self.completionTime) ) * 100 ))

        # compute for CPU Utilization, ATA, AWT.
        self.cpuUtilization = float(( 1 - ( self.idleTime/ self.completionTime )) * 100 )
        self.ata = round(self.ata/self.numOfProcess, 2)
        self.awt = round(self.awt/self.numOfProcess, 2 )
        self.caa = [ self.cpuUtilization, self.ata, self.awt ]
        

# This contains all the necessary functions for the frontEnd.
# This mostly contains widget placements.
class fcfs_frontEnd:
    def __init__( self ):
        self.backEnd = fcfs_backEnd()
        self.backEnd.generate_ganttChart()
        self.ganttChart = self.backEnd.get_ganttChart()
        self.caa = self.backEnd.get_caa()

    # For getting the current date
    def current_date( self ):
        self.dateString  =  datetime.date.today().strftime("%B %d, %Y")
        self.dateLBL.config(text = self.dateString)

    
    # This updates the clock widget
    def tick( self ):
        if self.tick_on:
            self.timeString  =  time.strftime("%H:%M:%S")
            self.clockLBL.config(text = self.timeString)
            self.clockLBL.after(200, self.tick )
        else:
            pass

    # This function returns True if the integerInput is not an Integer.
    # If it is an integer, return False.
    def isNotInteger( self, integerInput):
        try:
            self.intTest = int(integerInput)
            return False
        except ValueError:
            return True

    # The program has two list which contains a reference to all the program's widgets
    # And what this function does is it tries to clear/destroy all of these widgets
    # using the lists which contains the program's widgets.
    # The two lists are:
    #   - self.basicWidgetList: For most of the basic widgets
    #   - self.physicalMemWidgets: For the widgets used to display physical memory map
    def clearWidgets( self ):
        try:
            self.tick_on = False
            self.clearWidgetList( self.basicWidgetList )
            self.clearWidgetList( self.physicalMemWidgets )
        except:
            pass
        return


    # This function destroys all of the widgets inside the inputted widgetsToClear list.
    def clearWidgetList ( self, widgetsToClear):
        for widget in widgetsToClear:
            widget.destroy()


    # This function displays the necessary widgets for the gantt chart.
    # To get a general gist, the program has around 50 labels which acts as the gantt chart.
    # In addition, it has a text label which marks each section of the gantt chart
    def displayChart( self, tempPointer, tempColor, tempText, tempPercentage, tempTotalSize ):
        self.tempPointer = int(tempPointer)
        self.tempColor = tempColor
        self.tempText = tempText
        self.tempPercentage = tempPercentage
        self.tempTotalSize = tempTotalSize
        
        if self.tempPercentage != 0:
            self.tempLBL = Label( root , text = " ", font = ('Times New Roman', 30),  bg = self.tempColor)
            self.tempLBL.place(x = self.xCounter, y = 250)
            self.physicalMemWidgets.append( self.tempLBL )
            
            self.tempLBL = Label( root , text = self.tempText , font = ('Times New Roman', 10),  bg = self.tempColor)
            self.tempLBL.place(x = self.xCounter, y = 220)
            self.physicalMemWidgets.append( self.tempLBL )
            self.xCounter += 10
        ##print( int( self.tempPercentage ) )
        for i in range( int( self.tempPercentage/2 ) ):
            if self.tempPointer != 0:
                ##print( i )
                self.tempLBL = Label( root , text = " " , font = ('Times New Roman', 30),  bg = self.tempColor)
                self.tempLBL.place(x = self.xCounter, y = 250)
                self.xCounter += 10
                self.physicalMemWidgets.append( self.tempLBL )
                self.tempPointer -= 1
            else:
                pass
        if self.tempPercentage != 0:
            self.tempLBL  =  Label( root , text = tempTotalSize , font = ('Times New Roman', 10),  bg = "#c6e3ad")
            self.tempLBL.place(x = self.xCounter - 5, y = 310)
            self.physicalMemWidgets.append( self.tempLBL )
        return

    def mainMenuBTN_Pressed( self ):
        main.mainMenu_window()

    def aboutUsBTN_Pressed( self ):
        main.aboutUs_window()

    # This is the input window that will take in the user's inputs.
    def input1_window( self ):
        root.title ( "First Come First Serve" )
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.fcfsBG = Label ( root , image = fcfs_bg, bg = "black" )
        self.fcfsBG.place(x = 0, y = 0)
        self.basicWidgetList.append( self.fcfsBG )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#e1ddd2" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#e1ddd2")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )

        self.mainMenuBTN  =  Button ( root , image = mainMenu_btn, command = self.mainMenuBTN_Pressed , bg = "#e1ddd2" )
        self.mainMenuBTN.place (x = 850 ,y = 60)
        self.basicWidgetList.append( self.mainMenuBTN )

        self.aboutBTN  =  Button ( root , image = aboutUs_btn, command = self.aboutUsBTN_Pressed, bg = "#e1ddd2" )
        self.aboutBTN.place (x = 850 ,y = 10)
        self.basicWidgetList.append( self.aboutBTN )
        
        self.title1LBL  =  Label( root , text = "FCFS" , font = ('Times New Roman', 20),  bg = "#e1ddd2")
        self.title1LBL.place(x = 160, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Process Management" , font = ('Times New Roman', 20),  bg = "#e1ddd2")
        self.title2LBL.place(x = 75, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Input Window" , font = ('Times New Roman', 30),  bg = "#c6e3ad")
        self.title3LBL.place(x = 350, y = 105)
        self.basicWidgetList.append( self.title3LBL )

        self.processLBL  =  Label( root , text = "Process" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.processLBL.place(x = 285, y = 160)
        self.basicWidgetList.append( self.processLBL )

        self.process1LBL  =  Label( root , text = "1" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process1LBL.place(x = 315, y = 210)
        self.basicWidgetList.append( self.process1LBL )
        
        self.process2LBL  =  Label( root , text = "2" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process2LBL.place(x = 315, y = 260)
        self.basicWidgetList.append( self.process2LBL )
        
        self.process3LBL  =  Label( root , text = "3" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process3LBL.place(x = 315, y = 310)
        self.basicWidgetList.append( self.process3LBL )

        self.process4LBL  =  Label( root , text = "4" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process4LBL.place(x = 315, y = 360)
        self.basicWidgetList.append( self.process4LBL )
        
        self.process5LBL  =  Label( root , text = "5" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process5LBL.place(x = 315, y = 410)
        self.basicWidgetList.append( self.process5LBL )
        
        self.burstTimeLBL  =  Label( root , text = "Burst Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.burstTimeLBL.place(x = 425, y = 160)
        self.basicWidgetList.append( self.burstTimeLBL )
        
        self.burstTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime1ENTRY.place(x = 400, y = 210)
        self.basicWidgetList.append( self.burstTime1ENTRY )
        
        self.burstTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime2ENTRY.place(x = 400, y = 260)
        self.basicWidgetList.append( self.burstTime2ENTRY )
        
        self.burstTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime3ENTRY.place(x = 400, y = 310)
        self.basicWidgetList.append( self.burstTime3ENTRY )

        self.burstTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime4ENTRY.place(x = 400, y = 360)
        self.basicWidgetList.append( self.burstTime4ENTRY )
        
        self.burstTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime5ENTRY.place(x = 400, y = 410)
        self.basicWidgetList.append( self.burstTime5ENTRY )
        
        
        self.arrivalTimeLBL  =  Label( root , text = "Arrival Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.arrivalTimeLBL.place(x = 585, y = 160)
        self.basicWidgetList.append( self.arrivalTimeLBL )

        self.arrivalTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime1ENTRY.place(x = 570, y = 210)
        self.basicWidgetList.append( self.arrivalTime1ENTRY )
        
        self.arrivalTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime2ENTRY.place(x = 570, y = 260)
        self.basicWidgetList.append( self.arrivalTime2ENTRY )
        
        self.arrivalTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime3ENTRY.place(x = 570, y = 310)
        self.basicWidgetList.append( self.arrivalTime3ENTRY )

        self.arrivalTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime4ENTRY.place(x = 570, y = 360)
        self.basicWidgetList.append( self.arrivalTime4ENTRY )
        
        self.arrivalTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime5ENTRY.place(x = 570, y = 410)
        self.basicWidgetList.append( self.arrivalTime5ENTRY )
        
        self.computeBTN  =  Button ( root , text = 'Compute',command = self.input1_computeBTN_Pressed , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.computeBTN.place (x = 390 ,y = 470)
        self.basicWidgetList.append( self.computeBTN )

        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 520)
        self.basicWidgetList.append( self.exitBTN )

    # Once the user wants to proceed with the computation, this function will be executed.
    def input1_computeBTN_Pressed( self ):
        #print( "input1_computeBTN_Pressed" )
        if messagebox.askyesno( "Confirmation..." , " Are you sure you want to compute? " ) == True :
            self.arrivalTime1 = self.arrivalTime1ENTRY.get()
            self.arrivalTime2 = self.arrivalTime2ENTRY.get()
            self.arrivalTime3 = self.arrivalTime3ENTRY.get()
            self.arrivalTime4 = self.arrivalTime4ENTRY.get()
            self.arrivalTime5 = self.arrivalTime5ENTRY.get()
            self.arrivalTime_list = [ self.arrivalTime1,
                                      self.arrivalTime2,
                                      self.arrivalTime3,
                                      self.arrivalTime4,
                                      self.arrivalTime5 ]

            self.arrivalError = False
            self.arrivalTests = [ self.isNotInteger( self.arrivalTime1 ),
                                  self.isNotInteger( self.arrivalTime2 ),
                                  self.isNotInteger( self.arrivalTime3 ),
                                  self.isNotInteger( self.arrivalTime4 ),
                                  self.isNotInteger( self.arrivalTime5 ) ]
            for i in range( len( self.arrivalTests ) ):
                if self.arrivalTests[i] == True:
                    if self.arrivalTime_list[i] == "x":
                        pass
                    else:
                        self.arrivalError = True
                        break

            self.burstTime1 = self.burstTime1ENTRY.get()
            self.burstTime2 = self.burstTime2ENTRY.get()
            self.burstTime3 = self.burstTime3ENTRY.get()
            self.burstTime4 = self.burstTime4ENTRY.get()
            self.burstTime5 = self.burstTime5ENTRY.get()
            self.burstTime_list = [ self.burstTime1,
                                      self.burstTime2,
                                      self.burstTime3,
                                      self.burstTime4,
                                      self.burstTime5 ]

            self.burstError = False
            self.burstTests = [ self.isNotInteger( self.burstTime1 ),
                                  self.isNotInteger( self.burstTime2 ),
                                  self.isNotInteger( self.burstTime3 ),
                                  self.isNotInteger( self.burstTime4 ),
                                  self.isNotInteger( self.burstTime5 ) ]
            
            # process details [ processNum, burstTime, arrivalTime ]
            self.processDetails = {}
            for i in range( len( self.burstTests ) ):
                if self.burstTests[i] == True:
                    if self.burstTime_list[i] == "x":
                        pass
                    else:
                        self.burstError = True
                        break
                else:
                    # process details [ processNum, burstTime, arrivalTime ]
                    self.processDetails[i+1] = [ "P{}".format( i+1 ),
                                                 int( self.burstTime_list[i] ),
                                                 int( self.arrivalTime_list[i] ) ]

            
            if self.burstError == True:
                ##print ( "Error: Invalid Burst Time input." )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Burst Time input" )
            elif self.arrivalError == True:
                ##print ( " Error: Invalid Arrival Time input." )
                messagebox.showinfo( "Compute Error" , "Invalid Arrival Time input." )
            else:
                # Send the user's inputs to the backEnd class
                self.backEnd.insert_inputs( self.processDetails )
                # Generate the gantt chart using the backEnd class
                self.backEnd.generate_ganttChart()
                # get the gantt chart data from the backEnd class
                self.ganttChart = self.backEnd.get_ganttChart()
                self.caa = self.backEnd.get_caa()
                #print ( "compute finish" )
                #print( self.ganttChart )
                #print( self.caa )
                self.result1_window()

    # This function contains and displays the result data.
    # Result includes:
    #           Gantt Chart
    #           CPU Utilization
    #           ATA
    #           AWT
    def result1_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.fcfsBG = Label ( root , image = fcfs_bg, bg = "black" )
        self.fcfsBG.place(x = 0, y = 0)
        self.basicWidgetList.append( self.fcfsBG )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#e1ddd2" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#e1ddd2")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )

        self.title1LBL  =  Label( root , text = "FCFS" , font = ('Times New Roman', 20),  bg = "#e1ddd2")
        self.title1LBL.place(x = 160, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Process Management" , font = ('Times New Roman', 20),  bg = "#e1ddd2")
        self.title2LBL.place(x = 75, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Gantt Chart" , font = ('Times New Roman', 20),  bg = "#c6e3ad")
        self.title3LBL.place(x = 410, y = 160)
        self.basicWidgetList.append( self.title3LBL )
        
        self.physicalMemWidgets = []
        self.xCounter = 210
        self.indexPointer = 0
        
        self.markLBL  =  Label( root , text = 0 , font = ('Times New Roman', 10),  bg = "#c6e3ad")
        self.markLBL.place(x = self.xCounter - 5, y = 310)
        self.physicalMemWidgets.append( self.markLBL )

        self.tempTotalSize = 0
        for tempData in self.ganttChart:
            self.tempTotalSize += tempData[4]
            self.displayChart( tempData[6], tempData[5], tempData[2], tempData[6], self.tempTotalSize )

        self.cpuUtilizationLBL  =  Label( root , text = " CPU Utilization" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.cpuUtilizationLBL.place(x = 400, y = 360)
        self.basicWidgetList.append( self.cpuUtilizationLBL )

        self.cpuUtilizationENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuUtilizationENTRY.place(x = 400, y = 405)
        self.cpuUtilizationENTRY.insert( 0, str( round(self.caa[0],2)) + "%" )
        self.cpuUtilizationENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.cpuUtilizationENTRY )

        self.ataLBL  =  Label( root , text = " ATA" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.ataLBL.place(x = 280, y = 360)
        self.basicWidgetList.append( self.ataLBL )

        self.ataENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.ataENTRY.place(x = 235, y = 405)
        self.ataENTRY.insert( 0, str(self.caa[1]) )
        self.ataENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.ataENTRY )

        self.awtLBL  =  Label( root , text = " AWT" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.awtLBL.place(x = 602, y = 360)
        self.basicWidgetList.append( self.awtLBL )

        self.awtENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.awtENTRY.place(x = 565, y = 405)
        self.awtENTRY.insert( 0, str(self.caa[2]) )
        self.awtENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.awtENTRY )


        self.backBTN  =  Button ( root , text = 'BACK',command = self.input1_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 300 ,y = 480)
        self.basicWidgetList.append( self.backBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 490 ,y = 480)
        self.basicWidgetList.append( self.exitBTN )

# END OF FCFS PROGRAM: 6101-6580


# SJF PROGRAM: 6601-7145

# This class contains all the back end processes/computations.
class sjf_backEnd:
    def __init__( self ):
        # process details [ processNum, burstTime, arrivalTime ]
        self.processDetails = { 1 : [ "P1", 10, 10 ],
                                2 : [ "P2", 1, 5],
                                3 : [ "P3", 2, 8],
                                4 : [ "P4", 5, 6]}
        self.process_queue = []
        self.numOfProcess = 0
        for i in range ( 1, len( list(self.processDetails )) + 1):
            self.numOfProcess += 1
            self.process_queue.append( self.processDetails[i] )

    # For accepting in the user's input that will be utilized by the backend class.
    def insert_inputs( self, processDetails = None ):
        # process details [ processNum, burstTime, arrivalTime ]
        if processDetails == None:
            self.processDetails = { 1 : [ "P1", 7, 5 ],
                                    2 : [ "P2", 10, 0],
                                    3 : [ "P3", 5, 8] }
        else:
            self.processDetails = processDetails
        self.process_queue = []
        self.numOfProcess = 0
        for i in range ( 1, len( list(self.processDetails )) + 1):
            self.numOfProcess += 1
            self.process_queue.append( self.processDetails[i] )

    # returns the ganttChart list
    def get_ganttChart( self ):
        return self.ganttChart

    # returns the caa list which contains CPU Utilization, ATA, AWT.
    def get_caa( self ):
        return self.caa
    
    def generate_ganttChart( self ):
        # gantt chart [ start, finish, processNum, arrivalTime, burstTime, percentageprocess ]
        self.ganttChart = []

        # sort the process_queue by its arrival time.
        # process queue, [ processNum, burstTime, arrivalTime, priorirtyNum ]
        self.process_queue = sorted( self.process_queue, key=lambda x: x[2] )
        self.tempProcess_queue = deepcopy( self.process_queue )


        self.tempProcess_queue = deepcopy( self.process_queue )
        self.currentProcess = self.tempProcess_queue[0]
        self.tempResult_queue = []
        self.tempResult_queue.append( self.currentProcess )
        self.tempProcess_queue.pop(0)
        
        self.isFinished = False
        while self.isFinished == False:
            if len( self.tempProcess_queue) == 0:
                ##print( "first" )
                self.isFinished = True
                break
            self.finishTime = self.currentProcess[1] + self.currentProcess[2]
            ##print( "finishTime", self.finishTime )
            self.waitingProcess = []
            for i in range( len( self.tempProcess_queue )):
                if self.finishTime >= self.tempProcess_queue[i][2]:
                    # waitingProcess [ index, burstTime ]
                    self.waitingProcess.append( [ i, self.tempProcess_queue[i][1] ] )
            ##print( "waiting", self.waitingProcess )
            self.waitingProcess = sorted( self.waitingProcess, key=lambda x:x[1] )
            try:
                self.currentProcess = self.tempProcess_queue[ self.waitingProcess[0][0] ]
                self.tempResult_queue.append( self.currentProcess )
                self.tempProcess_queue.pop( self.waitingProcess[0][0] )
            except:
                try:
                    self.currentProcess = self.tempProcess_queue[ 0 ]
                    self.tempResult_queue.append( self.currentProcess )
                    self.tempProcess_queue.pop( 0 )
                except:
                    ##print( "last" )
                    self.isFinished = True
                    break

        self.process_queue = deepcopy( self.tempResult_queue )
            

        """
        ##print( "process queue", self.process_queue )
        self.process_queue[0].append( 0 )
        self.priorityNum = 1
        # This loop will traverse the process queue to determine the priority level of each process.
        for i in range( 1, len( self.process_queue) ):
            self.priorityNum = self.process_queue[i-1][3] + 1
            self.prevStartTime = self.process_queue[i-1][2]
            self.prevFinishTime = self.prevStartTime + self.process_queue[i-1][1]
            self.tempWaitingList = []
            for j in range( i, len( self.process_queue)):
                if self.process_queue[j][2] >= self.prevStartTime and self.process_queue[j][2] <= self.prevFinishTime:
                    self.tempWaitingList.append( [ j, self.process_queue[j][1] ] )
            self.tempWaitingList = sorted( self.tempWaitingList, key= lambda x: x[1] )
            ##print( "test", self.tempWaitingList )
            try:
                self.process_queue[self.tempWaitingList[0][0]].append( self.priorityNum)
                self.process_queue = sorted( self.process_queue, key=len, reverse = True )
            except:
                self.process_queue[-1].append( self.priorityNum )
                self.process_queue = sorted( self.process_queue, key=len, reverse = True )
        """
        # sort the process queue by the level of priority
        #self.process_queue = sorted( self.process_queue, key=lambda x: (x[2], x[3]) )
        ##print( "process queue 3", self.process_queue )

        # Initialize the needed variables
        self.completionTime = 0
        self.idleTime = 0
        self.ata = float(0)
        self.awt = float(0)
        self.tempColors = [ "#f77777", "#f7d977", "#77f7e6", "#77d5f7", "#d577f7", "#fcba03" ]
        self.tempColorsCounter = 0

        # Traverse the process_queue list to generate the necessary computations
        for i in range( len(self.process_queue) ):
            # if there's a gap/idle period in the process queue, execute the computations for idle.
            # also, append the necessary idle data into the gantt chart.
            if self.process_queue[i][2] > 0 and (i == 0 or self.completionTime < self.process_queue[i][2]):
                ##print( i )
                try:
                    self.ganttChart.append( [self.completionTime,self.process_queue[i][2], "Idle",self.completionTime , self.process_queue[i][2] - self.completionTime, "#bfbaac"] )
                except:
                    pass
                self.idleTime += (self.process_queue[i][2] - self.completionTime)
                self.completionTime = self.process_queue[i][2]
                ##print(self.process_queue[i][2] - self.completionTime )
            self.ata += float((self.completionTime + self.process_queue[i][1]) - self.process_queue[i][2] )
            self.awt += float((self.completionTime) - self.process_queue[i][2] )

            # append the computations/data for a certain process in the process queue.
            try:
                self.ganttChart.append( [self.completionTime, self.completionTime + self.process_queue[i][1], self.process_queue[i][0], self.process_queue[i][2], self.process_queue[i][1], self.tempColors[self.tempColorsCounter]] )
            except:
                ##print( "fail", self.process_queue[i] )
                pass
            self.completionTime += self.process_queue[i][1]
            self.tempColorsCounter += 1

        ##print ( "idle time: ", self.idleTime )
        ##print( "completion time: ", self.completionTime )

        # add/append the necessary data that will be used by displayChart function in the frontEnd.
        for i in range( len(self.ganttChart) ):
            self.ganttChart[i].append( float(( float(self.ganttChart[i][4]) / float(self.completionTime) ) * 100 ))

        # compute for CPU Utilization, ATA, AWT.
        self.cpuUtilization = float(( 1 - ( self.idleTime/ self.completionTime )) * 100 )
        self.ata = round(self.ata/self.numOfProcess, 2)
        self.awt = round(self.awt/self.numOfProcess, 2 )
        self.caa = [ self.cpuUtilization, self.ata, self.awt ]
        

# This contains all the necessary functions for the frontEnd.
# This mostly contains widget placements.
class sjf_frontEnd:
    def __init__( self ):
        self.backEnd = sjf_backEnd()
        self.backEnd.generate_ganttChart()
        self.ganttChart = self.backEnd.get_ganttChart()
        self.caa = self.backEnd.get_caa()

    # For getting the current date
    def current_date( self ):
        self.dateString  =  datetime.date.today().strftime("%B %d, %Y")
        self.dateLBL.config(text = self.dateString)

    
    # This updates the clock widget
    def tick( self ):
        if self.tick_on:
            self.timeString  =  time.strftime("%H:%M:%S")
            self.clockLBL.config(text = self.timeString)
            self.clockLBL.after(200, self.tick )
        else:
            pass

    # This function returns True if the integerInput is not an Integer.
    # If it is an integer, return False.
    def isNotInteger( self, integerInput):
        try:
            self.intTest = int(integerInput)
            return False
        except ValueError:
            return True

    # The program has two list which contains a reference to all the program's widgets
    # And what this function does is it tries to clear/destroy all of these widgets
    # using the lists which contains the program's widgets.
    # The two lists are:
    #   - self.basicWidgetList: For most of the basic widgets
    #   - self.physicalMemWidgets: For the widgets used to display physical memory map
    def clearWidgets( self ):
        try:
            self.tick_on = False
            self.clearWidgetList( self.basicWidgetList )
            self.clearWidgetList( self.physicalMemWidgets )
        except:
            pass
        return


    # This function destroys all of the widgets inside the inputted widgetsToClear list.
    def clearWidgetList ( self, widgetsToClear):
        for widget in widgetsToClear:
            widget.destroy()


    # This function displays the necessary widgets for the gantt chart.
    # To get a general gist, the program has around 50 labels which acts as the gantt chart.
    # In addition, it has a text label which marks each section of the gantt chart
    def displayChart( self, tempPointer, tempColor, tempText, tempPercentage, tempTotalSize ):
        self.tempPointer = int(tempPointer)
        self.tempColor = tempColor
        self.tempText = tempText
        self.tempPercentage = tempPercentage
        self.tempTotalSize = tempTotalSize
        
        if self.tempPercentage != 0:
            self.tempLBL = Label( root , text = " ", font = ('Times New Roman', 30),  bg = self.tempColor)
            self.tempLBL.place(x = self.xCounter, y = 250)
            self.physicalMemWidgets.append( self.tempLBL )
            
            self.tempLBL = Label( root , text = self.tempText , font = ('Times New Roman', 10),  bg = self.tempColor)
            self.tempLBL.place(x = self.xCounter, y = 220)
            self.physicalMemWidgets.append( self.tempLBL )
            self.xCounter += 10
        ###print( int( self.tempPercentage ) )
        for i in range( int( self.tempPercentage/2 ) ):
            if self.tempPointer != 0:
                ###print( i )
                self.tempLBL = Label( root , text = " " , font = ('Times New Roman', 30),  bg = self.tempColor)
                self.tempLBL.place(x = self.xCounter, y = 250)
                self.xCounter += 10
                self.physicalMemWidgets.append( self.tempLBL )
                self.tempPointer -= 1
            else:
                pass
        if self.tempPercentage != 0:
            self.tempLBL  =  Label( root , text = tempTotalSize , font = ('Times New Roman', 10),  bg = "#c6e3ad")
            self.tempLBL.place(x = self.xCounter - 5, y = 310)
            self.physicalMemWidgets.append( self.tempLBL )
        return

    def mainMenuBTN_Pressed( self ):
        main.mainMenu_window()

    def aboutUsBTN_Pressed( self ):
        main.aboutUs_window()

    # This is the input window that will take in the user's inputs.
    def input1_window( self ):
        root.title ( "Shortest Job First Process Management" )
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.sjfBG = Label ( root , image = sjf_bg, bg = "black" )
        self.sjfBG.place(x = 0, y = 0)
        self.basicWidgetList.append( self.sjfBG )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#e1ddd2" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.mainMenuBTN  =  Button ( root , image = mainMenu_btn, command = self.mainMenuBTN_Pressed , bg = "#e1ddd2" )
        self.mainMenuBTN.place (x = 850 ,y = 60)
        self.basicWidgetList.append( self.mainMenuBTN )

        self.aboutBTN  =  Button ( root , image = aboutUs_btn, command = self.aboutUsBTN_Pressed, bg = "#e1ddd2" )
        self.aboutBTN.place (x = 850 ,y = 10)
        self.basicWidgetList.append( self.aboutBTN )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#e1ddd2")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )
        
        self.title1LBL  =  Label( root , text = "SJF" , font = ('Times New Roman', 20),  bg = "#e1ddd2")
        self.title1LBL.place(x = 165, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Process Management" , font = ('Times New Roman', 20),  bg = "#e1ddd2")
        self.title2LBL.place(x = 75, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Input Window" , font = ('Times New Roman', 30),  bg = "#c6e3ad")
        self.title3LBL.place(x = 370, y = 105)
        self.basicWidgetList.append( self.title3LBL )

        self.processLBL  =  Label( root , text = "Process" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.processLBL.place(x = 285, y = 160)
        self.basicWidgetList.append( self.processLBL )

        self.process1LBL  =  Label( root , text = "1" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process1LBL.place(x = 315, y = 210)
        self.basicWidgetList.append( self.process1LBL )
        
        self.process2LBL  =  Label( root , text = "2" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process2LBL.place(x = 315, y = 260)
        self.basicWidgetList.append( self.process2LBL )
        
        self.process3LBL  =  Label( root , text = "3" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process3LBL.place(x = 315, y = 310)
        self.basicWidgetList.append( self.process3LBL )

        self.process4LBL  =  Label( root , text = "4" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process4LBL.place(x = 315, y = 360)
        self.basicWidgetList.append( self.process4LBL )
        
        self.process5LBL  =  Label( root , text = "5" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process5LBL.place(x = 315, y = 410)
        self.basicWidgetList.append( self.process5LBL )
        
        self.burstTimeLBL  =  Label( root , text = "Burst Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.burstTimeLBL.place(x = 425, y = 160)
        self.basicWidgetList.append( self.burstTimeLBL )
        
        self.burstTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime1ENTRY.place(x = 400, y = 210)
        self.basicWidgetList.append( self.burstTime1ENTRY )
        
        self.burstTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime2ENTRY.place(x = 400, y = 260)
        self.basicWidgetList.append( self.burstTime2ENTRY )
        
        self.burstTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime3ENTRY.place(x = 400, y = 310)
        self.basicWidgetList.append( self.burstTime3ENTRY )

        self.burstTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime4ENTRY.place(x = 400, y = 360)
        self.basicWidgetList.append( self.burstTime4ENTRY )
        
        self.burstTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime5ENTRY.place(x = 400, y = 410)
        self.basicWidgetList.append( self.burstTime5ENTRY )
        
        
        self.arrivalTimeLBL  =  Label( root , text = "Arrival Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.arrivalTimeLBL.place(x = 585, y = 160)
        self.basicWidgetList.append( self.arrivalTimeLBL )

        self.arrivalTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime1ENTRY.place(x = 570, y = 210)
        self.basicWidgetList.append( self.arrivalTime1ENTRY )
        
        self.arrivalTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime2ENTRY.place(x = 570, y = 260)
        self.basicWidgetList.append( self.arrivalTime2ENTRY )
        
        self.arrivalTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime3ENTRY.place(x = 570, y = 310)
        self.basicWidgetList.append( self.arrivalTime3ENTRY )

        self.arrivalTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime4ENTRY.place(x = 570, y = 360)
        self.basicWidgetList.append( self.arrivalTime4ENTRY )
        
        self.arrivalTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime5ENTRY.place(x = 570, y = 410)
        self.basicWidgetList.append( self.arrivalTime5ENTRY )
        
        self.computeBTN  =  Button ( root , text = 'Compute',command = self.input1_computeBTN_Pressed , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.computeBTN.place (x = 390 ,y = 470)
        self.basicWidgetList.append( self.computeBTN )

        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 520)
        self.basicWidgetList.append( self.exitBTN )


    # Once the user wants to proceed with the computation, this function will be executed.
    def input1_computeBTN_Pressed( self ):
        ##print( "input1_computeBTN_Pressed" )
        if messagebox.askyesno( "Confirmation..." , " Are you sure you want to compute? " ) == True :
            self.arrivalTime1 = self.arrivalTime1ENTRY.get()
            self.arrivalTime2 = self.arrivalTime2ENTRY.get()
            self.arrivalTime3 = self.arrivalTime3ENTRY.get()
            self.arrivalTime4 = self.arrivalTime4ENTRY.get()
            self.arrivalTime5 = self.arrivalTime5ENTRY.get()
            self.arrivalTime_list = [ self.arrivalTime1,
                                      self.arrivalTime2,
                                      self.arrivalTime3,
                                      self.arrivalTime4,
                                      self.arrivalTime5 ]

            self.arrivalError = False
            self.arrivalTests = [ self.isNotInteger( self.arrivalTime1 ),
                                  self.isNotInteger( self.arrivalTime2 ),
                                  self.isNotInteger( self.arrivalTime3 ),
                                  self.isNotInteger( self.arrivalTime4 ),
                                  self.isNotInteger( self.arrivalTime5 ) ]
            for i in range( len( self.arrivalTests ) ):
                if self.arrivalTests[i] == True:
                    if self.arrivalTime_list[i] == "x":
                        pass
                    else:
                        self.arrivalError = True
                        break

            self.burstTime1 = self.burstTime1ENTRY.get()
            self.burstTime2 = self.burstTime2ENTRY.get()
            self.burstTime3 = self.burstTime3ENTRY.get()
            self.burstTime4 = self.burstTime4ENTRY.get()
            self.burstTime5 = self.burstTime5ENTRY.get()
            self.burstTime_list = [ self.burstTime1,
                                      self.burstTime2,
                                      self.burstTime3,
                                      self.burstTime4,
                                      self.burstTime5 ]

            self.burstError = False
            self.burstTests = [ self.isNotInteger( self.burstTime1 ),
                                  self.isNotInteger( self.burstTime2 ),
                                  self.isNotInteger( self.burstTime3 ),
                                  self.isNotInteger( self.burstTime4 ),
                                  self.isNotInteger( self.burstTime5 ) ]
            
            # process details [ processNum, burstTime, arrivalTime ]
            self.processDetails = {}
            for i in range( len( self.burstTests ) ):
                if self.burstTests[i] == True:
                    if self.burstTime_list[i] == "x":
                        pass
                    else:
                        self.burstError = True
                        break
                else:
                    self.processDetails[i+1] = [ "P{}".format( i+1 ),
                                                 int( self.burstTime_list[i] ),
                                                 int( self.arrivalTime_list[i] ) ]

            
            if self.burstError == True:
                ##print ( "Error: Invalid Burst Time input." )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Burst Time input" )
            elif self.arrivalError == True:
                ##print ( " Error: Invalid Arrival Time input." )
                messagebox.showinfo( "Compute Error" , "Invalid Arrival Time input." )
            else:
                self.backEnd.insert_inputs( self.processDetails )
                self.backEnd.generate_ganttChart()
                self.ganttChart = self.backEnd.get_ganttChart()
                self.caa = self.backEnd.get_caa()
                ##print ( "compute finish" )
                ##print( self.ganttChart )
                ##print( self.caa )
                self.result1_window()

    # This function contains and displays the result data.
    # Result includes:
    #           Gantt Chart
    #           CPU Utilization
    #           ATA
    #           AWT
    def result1_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.sjfBG = Label ( root , image = sjf_bg, bg = "black" )
        self.sjfBG.place(x = 0, y = 0)
        self.basicWidgetList.append( self.sjfBG )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#e1ddd2" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#e1ddd2")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )

        self.title1LBL  =  Label( root , text = "SJF" , font = ('Times New Roman', 20),  bg = "#e1ddd2")
        self.title1LBL.place(x = 165, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Process Management" , font = ('Times New Roman', 20),  bg = "#e1ddd2")
        self.title2LBL.place(x = 75, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Gantt Chart" , font = ('Times New Roman', 20),  bg = "#c6e3ad")
        self.title3LBL.place(x = 410, y = 160)
        self.basicWidgetList.append( self.title3LBL )
        
        self.physicalMemWidgets = []
        self.xCounter = 210
        self.indexPointer = 0
        
        self.markLBL  =  Label( root , text = 0 , font = ('Times New Roman', 10),  bg = "#c6e3ad")
        self.markLBL.place(x = self.xCounter - 5, y = 310)
        self.physicalMemWidgets.append( self.markLBL )

        self.tempTotalSize = 0
        for tempData in self.ganttChart:
            self.tempTotalSize += tempData[4]
            self.displayChart( tempData[6], tempData[5], tempData[2], tempData[6], self.tempTotalSize )

        self.cpuUtilizationLBL  =  Label( root , text = " CPU Utilization" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.cpuUtilizationLBL.place(x = 400, y = 360)
        self.basicWidgetList.append( self.cpuUtilizationLBL )

        self.cpuUtilizationENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuUtilizationENTRY.place(x = 400, y = 405)
        self.cpuUtilizationENTRY.insert( 0, str( round(self.caa[0],2)) + "%" )
        self.cpuUtilizationENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.cpuUtilizationENTRY )

        self.ataLBL  =  Label( root , text = " ATA" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.ataLBL.place(x = 280, y = 360)
        self.basicWidgetList.append( self.ataLBL )

        self.ataENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.ataENTRY.place(x = 235, y = 405)
        self.ataENTRY.insert( 0, str(self.caa[1]) )
        self.ataENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.ataENTRY )

        self.awtLBL  =  Label( root , text = " AWT" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.awtLBL.place(x = 602, y = 360)
        self.basicWidgetList.append( self.awtLBL )

        self.awtENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.awtENTRY.place(x = 565, y = 405)
        self.awtENTRY.insert( 0, str(self.caa[2]) )
        self.awtENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.awtENTRY )


        self.backBTN  =  Button ( root , text = 'BACK',command = self.input1_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 300 ,y = 480)
        self.basicWidgetList.append( self.backBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 490 ,y = 480)
        self.basicWidgetList.append( self.exitBTN )

# END OF SJF PROGRAM: 6601-7145


# START OF SRTF PROGRAM

# This class contains all the back end processes/computations.
class srtf_backEnd:
    def __init__( self ):
        # process details [ processNum, burstTime, arrivalTime, timeRemaining ]
        self.processDetails = { 1 : [ "P1", 12, 4, 12 ],
                                2 : [ "P2", 10, 5, 10],
                                3 : [ "P3", 5, 10, 5],
                                4 : [ "P4", 7, 7, 7]}

        # AWT
        self.awtInfo_dic = {}
        
        # process_queue [ processNum, burstTime, arrivalTime, timeRemaining ]
        self.process_queue = []
        self.numOfProcess = 0
        for i in range ( 1, len( list(self.processDetails )) + 1):
            self.numOfProcess += 1
            self.process_queue.append( [ self.processDetails[i][0],
                                         self.processDetails[i][1],
                                         self.processDetails[i][2],
                                         self.processDetails[i][3] ])
            self.awtInfo_dic[self.processDetails[i][0]] = [ int("-" + str(self.processDetails[i][2])) ]

    # For accepting in the user's input that will be utilized by the backend class.
    def insert_inputs( self, processDetails = None ):
            
        # process details [ processNum, burstTime, arrivalTime, timeRemaining ]
        if processDetails == None:
            self.processDetails = { 1 : [ "P1", 12, 4, 12 ],
                                    2 : [ "P2", 10, 5, 10],
                                    3 : [ "P3", 5, 10, 5],
                                    4 : [ "P4", 7, 7, 7]}
        else:
            self.processDetails = processDetails

        # AWT
        self.awtInfo_dic = {}
        
        # process_queue [ processNum, burstTime, arrivalTime, timeRemaining ]
        self.process_queue = []
        self.numOfProcess = 0
        for i in range ( 1, len( list(self.processDetails )) + 1):
            self.numOfProcess += 1
            self.process_queue.append( [ self.processDetails[i][0],
                                         self.processDetails[i][1],
                                         self.processDetails[i][2],
                                         self.processDetails[i][3] ])
            self.awtInfo_dic[self.processDetails[i][0]] = [ int("-" + str(self.processDetails[i][2])) ]
            

            

    # returns the ganttChart list
    def get_ganttChart( self ):
        return self.ganttChart

    # returns the caa list which contains CPU Utilization, ATA, AWT.
    def get_caa( self ):
        return self.caa

    def hasProcessArrived( self, processNum, time ):
        print( processNum )
        print ( self.processDetails )
        if self.processDetails[processNum][2] <= time:
            return True
        else:
            return False

    def deductTime( self, processNum ):
        try:
            self.processDetails[processNum][3] -= 1
        except:
            pass
        return

    def isProcessFinished( self, processNum ):
        #print( processNum )
        if self.processDetails[processNum][3] <= 0:
            try:
                self.waitingList.remove( processNum )
            except:
                print( "fail", processNum )
                pass
            return True
        else:
            return False
    
    def generate_ganttChart( self ):
        # gantt chart [ start, finish, processNum, arrivalTime, burstTime, percentageprocess ]
        self.ganttChart = []

        # sort the process_queue by its arrival time.
        # process_queue [ processNum, burstTime, arrivalTime, timeRemaining ]
        self.process_queue = sorted( self.process_queue, key=lambda x: x[2] )
        self.numberOfProcesses = len( self.process_queue )

        self.waitingList = []
        for i in range( len( self.process_queue ) ):
            self.waitingList.append( int(self.process_queue[i][0][1]) )
            
        self.tempProcess_queue = deepcopy( self.process_queue )
        self.tempResult_queue = []
        self.tempResult_dic = {}
        # ataInfo_dic processNum : finishTime
        self.ataInfo_dic = {}


        self.isFinished = False
        self.currentTime = 0
        while self.isFinished == False:
            # [ processNum, indexNum ]
            self.waitingList = []
            for i in range( len( self.tempProcess_queue )):
                self.tempProcessNum = int(self.tempProcess_queue[i][0][1])
                self.test = self.hasProcessArrived( self.tempProcessNum, self.currentTime )
                if self.test == True:
                    self.waitingList.append( [ self.tempProcessNum , i, self.processDetails[self.tempProcessNum][3]] )
            if len( self.waitingList  ) == 0 and len( self.tempProcess_queue ) >= 1:
                self.tempResult_dic[self.currentTime] = "Idle"
                self.currentTime += 1
            else:
                self.waitingList = sorted( self.waitingList, key=lambda x: x[2] )
                self.currentProcessNum = int(self.waitingList[0][0])
                self.deductTime( self.currentProcessNum )
                self.tempResult_dic[self.currentTime] = "P{}".format( self.currentProcessNum )
                self.currentTime += 1
                self.ataInfo_dic["P{}".format( self.currentProcessNum )] = [ self.currentTime, self.processDetails[self.currentProcessNum][2] ]
                self.test2 = self.isProcessFinished( self.currentProcessNum )
                if self.test2 == True:
                    self.tempProcess_queue.pop( self.waitingList[0][1] )
            if len(self.tempProcess_queue) == 0:
                break
        #print( "waitingList", self.waitingList )
        #print( "end", self.currentProcessNum, self.nextProcessNum )
        print( "xResult", self.tempResult_dic )

                
        #print ( self.tempResult_dic )
        print( "ataInfo", self.ataInfo_dic )
        
        self.prevProcess = "N/A"
        self.currentProcess = "N/A"
        self.tempColors = { "Idle" : "#bfbaac",
                            "P1" : "#f77777",
                            "P2" : "#f7d977",
                            "P3" : "#77f7e6",
                            "P4" : "#77d5f7",
                            "P5" : "#d577f7",
                            "EXTRA" : "#fcba03" }

        # In this block of code, we will turn the tempResult_dic into the ganttChart data        
        self.idleTime = 0
        for time in list(self.tempResult_dic):
            self.time = time
            self.currentProcess = self.tempResult_dic[time]
            if self.currentProcess == "Idle":
                self.idleTime += 1
                
            if self.prevProcess != "N/A":
                if self.currentProcess != self.prevProcess:
                    try:
                        self.ganttChart.append( [ self.startTime,
                                              self.time,
                                              self.tempResult_dic[self.time-1],
                                              self.time,
                                              self.time - self.startTime,
                                              self.tempColors[self.tempResult_dic[self.time-1]] ] )
                        if self.tempResult_dic[self.time-1] in self.awtInfo_dic:
                            self.awtInfo_dic[self.tempResult_dic[self.time-1]].append( self.startTime )
                            self.awtInfo_dic[self.tempResult_dic[self.time-1]].append( int("-" + str(self.time)) )
                    except:
                        pass
                    self.startTime = self.time
            else:
                self.startTime = self.time
                
            self.prevProcess = self.currentProcess
        else:
            self.time += 1
            self.ganttChart.append( [ self.startTime,
                                      self.time,
                                      self.tempResult_dic[self.time-1],
                                      self.time,
                                      (self.time) - self.startTime,
                                      self.tempColors[self.tempResult_dic[self.time-1]] ] )
            if self.tempResult_dic[self.time-1] in self.awtInfo_dic:
                            self.awtInfo_dic[self.tempResult_dic[self.time-1]].append( self.startTime )
                            self.awtInfo_dic[self.tempResult_dic[self.time-1]].append( int("-" + str(self.time)) )

        for i in range( len(self.ganttChart) ):
            self.ganttChart[i].append( float(( float(self.ganttChart[i][4]) / float(self.time) ) * 100 ))

        # The program will compute for the average turn around time here
        self.ata = 0.0
        for processNum in list( self.ataInfo_dic ):
            self.ata += ( self.ataInfo_dic[processNum][0] - self.ataInfo_dic[processNum][1] )

        # The program will compute for the average waiting time here
        self.awt = 0.0
        for processNum in list( self.awtInfo_dic ):
            self.tempCalc = 0.0
            if len(self.awtInfo_dic[processNum]) // 2 != 0:
                self.awtInfo_dic[processNum].pop( -1 )
            for i in range( len( self.awtInfo_dic[processNum] )):
                self.tempCalc += self.awtInfo_dic[processNum][i]
            self.awt += self.tempCalc

        # The final computations for cpuUtilization, ata, and awt
        
        self.cpuUtilization = round((( 1-(self.idleTime/self.time)) * 100 ), 2 )
        self.ata = round(( self.ata ) / len(self.ataInfo_dic), 2)
        self.awt = round(( self.awt ) / len(self.awtInfo_dic), 2)

        # Put the calculated cpuUtilization, ata, and awt into one list
        # The data inside this list will be displayed to the user.
        self.caa = [ self.cpuUtilization,
                     self.ata,
                     self.awt ]
                     
        print ( self.cpuUtilization )
        print( self.ata )
        print( self.awt )
        print( "awtInfo", self.awtInfo_dic )
        
        #self.caa = [ 0, 0, 0 ]
        
        

# This contains all the necessary functions for the frontEnd.
# This mostly contains widget placements.
class srtf_frontEnd:
    def __init__( self ):
        self.backEnd = srtf_backEnd()
        #self.backEnd.generate_ganttChart()
        #self.ganttChart = self.backEnd.get_ganttChart()
        #self.caa = self.backEnd.get_caa()
        #self.caa = self.backEnd.get_caa()

    # For getting the current date
    def current_date( self ):
        self.dateString  =  datetime.date.today().strftime("%B %d, %Y")
        self.dateLBL.config(text = self.dateString)

    
    # This updates the clock widget
    def tick( self ):
        if self.tick_on:
            self.timeString  =  time.strftime("%H:%M:%S")
            self.clockLBL.config(text = self.timeString)
            self.clockLBL.after(200, self.tick )
        else:
            pass

    # This function returns True if the integerInput is not an Integer.
    # If it is an integer, return False.
    def isNotInteger( self, integerInput):
        try:
            self.intTest = int(integerInput)
            return False
        except ValueError:
            return True

    # The program has two list which contains a reference to all the program's widgets
    # And what this function does is it tries to clear/destroy all of these widgets
    # using the lists which contains the program's widgets.
    # The two lists are:
    #   - self.basicWidgetList: For most of the basic widgets
    #   - self.physicalMemWidgets: For the widgets used to display physical memory map
    def clearWidgets( self ):
        try:
            self.tick_on = False
            self.clearWidgetList( self.basicWidgetList )
            self.clearWidgetList( self.physicalMemWidgets )
        except:
            pass
        return


    # This function destroys all of the widgets inside the inputted widgetsToClear list.
    def clearWidgetList ( self, widgetsToClear):
        for widget in widgetsToClear:
            widget.destroy()


    # This function displays the necessary widgets for the gantt chart.
    # To get a general gist, the program has around 50 labels which acts as the gantt chart.
    # In addition, it has a text label which marks each section of the gantt chart
    def displayChart( self, tempPointer, tempColor, tempText, tempPercentage, tempTotalSize ):
        self.tempPointer = int(tempPointer)
        self.tempColor = tempColor
        self.tempText = tempText
        self.tempPercentage = tempPercentage
        self.tempTotalSize = tempTotalSize
        
        if self.tempPercentage != 0:
            self.tempLBL = Label( root , text = " ", font = ('Times New Roman', 30),  bg = self.tempColor)
            self.tempLBL.place(x = self.xCounter, y = 250)
            self.physicalMemWidgets.append( self.tempLBL )
            
            self.tempLBL = Label( root , text = self.tempText , font = ('Times New Roman', 10),  bg = self.tempColor)
            self.tempLBL.place(x = self.xCounter, y = 220)
            self.physicalMemWidgets.append( self.tempLBL )
            self.xCounter += 10
        ##print( int( self.tempPercentage ) )
        for i in range( int( self.tempPercentage/2 ) ):
            if self.tempPointer != 0:
                ##print( i )
                self.tempLBL = Label( root , text = " " , font = ('Times New Roman', 30),  bg = self.tempColor)
                self.tempLBL.place(x = self.xCounter, y = 250)
                self.xCounter += 10
                self.physicalMemWidgets.append( self.tempLBL )
                self.tempPointer -= 1
            else:
                pass
        if self.tempPercentage != 0:
            self.tempLBL  =  Label( root , text = tempTotalSize , font = ('Times New Roman', 10),  bg = "#c6e3ad")
            self.tempLBL.place(x = self.xCounter - 5, y = 310)
            self.physicalMemWidgets.append( self.tempLBL )
        return

    def mainMenuBTN_Pressed( self ):
        main.mainMenu_window()

    def aboutUsBTN_Pressed( self ):
        main.aboutUs_window()

    # This is the input window that will take in the user's inputs.
    def input1_window( self ):
        root.title ( "Shortest Remaining Time First Process Management" )
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.srtfLBL = Label ( root , image = srtf_bg, bg = "black" )
        self.srtfLBL.place(x = 0, y = 0)
        self.basicWidgetList.append( self.srtfLBL )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#e1ddd2" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#e1ddd2")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )
        
        self.mainMenuBTN  =  Button ( root , image = mainMenu_btn, command = self.mainMenuBTN_Pressed , bg = "#e1ddd2" )
        self.mainMenuBTN.place (x = 850 ,y = 60)
        self.basicWidgetList.append( self.mainMenuBTN )

        self.aboutBTN  =  Button ( root , image = aboutUs_btn, command = self.aboutUsBTN_Pressed, bg = "#e1ddd2" )
        self.aboutBTN.place (x = 850 ,y = 10)
        
        self.basicWidgetList.append( self.aboutBTN )
        self.title1LBL  =  Label( root , text = "SRTF" , font = ('Times New Roman', 20),  bg = "#e1ddd2")
        self.title1LBL.place(x = 155, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Process Management" , font = ('Times New Roman', 20),  bg = "#e1ddd2")
        self.title2LBL.place(x = 75, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Input Window" , font = ('Times New Roman', 30),  bg = "#c6e3ad")
        self.title3LBL.place(x = 370, y = 105)
        self.basicWidgetList.append( self.title3LBL )

        # Process Num
        self.processLBL  =  Label( root , text = "Process" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.processLBL.place(x = 285, y = 160)
        self.basicWidgetList.append( self.processLBL )

        self.process1LBL  =  Label( root , text = "1" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process1LBL.place(x = 315, y = 210)
        self.basicWidgetList.append( self.process1LBL )
        
        self.process2LBL  =  Label( root , text = "2" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process2LBL.place(x = 315, y = 260)
        self.basicWidgetList.append( self.process2LBL )
        
        self.process3LBL  =  Label( root , text = "3" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process3LBL.place(x = 315, y = 310)
        self.basicWidgetList.append( self.process3LBL )

        self.process4LBL  =  Label( root , text = "4" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process4LBL.place(x = 315, y = 360)
        self.basicWidgetList.append( self.process4LBL )
        
        self.process5LBL  =  Label( root , text = "5" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process5LBL.place(x = 315, y = 410)
        self.basicWidgetList.append( self.process5LBL )


        # Burst Time Widgets
        self.burstTimeLBL  =  Label( root , text = "Burst Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.burstTimeLBL.place(x = 425, y = 160)
        self.basicWidgetList.append( self.burstTimeLBL )
        
        self.burstTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime1ENTRY.place(x = 400, y = 210)
        self.basicWidgetList.append( self.burstTime1ENTRY )
        
        self.burstTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime2ENTRY.place(x = 400, y = 260)
        self.basicWidgetList.append( self.burstTime2ENTRY )
        
        self.burstTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime3ENTRY.place(x = 400, y = 310)
        self.basicWidgetList.append( self.burstTime3ENTRY )

        self.burstTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime4ENTRY.place(x = 400, y = 360)
        self.basicWidgetList.append( self.burstTime4ENTRY )
        
        self.burstTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime5ENTRY.place(x = 400, y = 410)
        self.basicWidgetList.append( self.burstTime5ENTRY )
        

        # Arrival Time Widgets
        self.arrivalTimeLBL  =  Label( root , text = "Arrival Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.arrivalTimeLBL.place(x = 585, y = 160)
        self.basicWidgetList.append( self.arrivalTimeLBL )

        self.arrivalTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime1ENTRY.place(x = 570, y = 210)
        self.basicWidgetList.append( self.arrivalTime1ENTRY )
        
        self.arrivalTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime2ENTRY.place(x = 570, y = 260)
        self.basicWidgetList.append( self.arrivalTime2ENTRY )
        
        self.arrivalTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime3ENTRY.place(x = 570, y = 310)
        self.basicWidgetList.append( self.arrivalTime3ENTRY )

        self.arrivalTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime4ENTRY.place(x = 570, y = 360)
        self.basicWidgetList.append( self.arrivalTime4ENTRY )
        
        self.arrivalTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime5ENTRY.place(x = 570, y = 410)
        self.basicWidgetList.append( self.arrivalTime5ENTRY )
        
        self.computeBTN  =  Button ( root , text = 'Compute',command = self.input1_computeBTN_Pressed , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.computeBTN.place (x = 390 ,y = 480)
        self.basicWidgetList.append( self.computeBTN )

        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 530)
        self.basicWidgetList.append( self.exitBTN )


    # Once the user wants to proceed with the computation, this function will be executed.
    def input1_computeBTN_Pressed( self ):
        #print( "input1_computeBTN_Pressed" )
        if messagebox.askyesno( "Confirmation..." , " Are you sure you want to compute? " ) == True :
            self.arrivalTime1 = self.arrivalTime1ENTRY.get()
            self.arrivalTime2 = self.arrivalTime2ENTRY.get()
            self.arrivalTime3 = self.arrivalTime3ENTRY.get()
            self.arrivalTime4 = self.arrivalTime4ENTRY.get()
            self.arrivalTime5 = self.arrivalTime5ENTRY.get()
            self.arrivalTime_list = [ self.arrivalTime1,
                                      self.arrivalTime2,
                                      self.arrivalTime3,
                                      self.arrivalTime4,
                                      self.arrivalTime5 ]

            self.arrivalError = False
            self.arrivalTests = [ self.isNotInteger( self.arrivalTime1 ),
                                  self.isNotInteger( self.arrivalTime2 ),
                                  self.isNotInteger( self.arrivalTime3 ),
                                  self.isNotInteger( self.arrivalTime4 ),
                                  self.isNotInteger( self.arrivalTime5 ) ]
            for i in range( len( self.arrivalTests ) ):
                if self.arrivalTests[i] == True:
                    if self.arrivalTime_list[i] == "x":
                        pass
                    else:
                        self.arrivalError = True
                        break

            self.burstTime1 = self.burstTime1ENTRY.get()
            self.burstTime2 = self.burstTime2ENTRY.get()
            self.burstTime3 = self.burstTime3ENTRY.get()
            self.burstTime4 = self.burstTime4ENTRY.get()
            self.burstTime5 = self.burstTime5ENTRY.get()
            self.burstTime_list = [ self.burstTime1,
                                      self.burstTime2,
                                      self.burstTime3,
                                      self.burstTime4,
                                      self.burstTime5 ]

            self.burstError = False
            self.burstTests = [ self.isNotInteger( self.burstTime1 ),
                                  self.isNotInteger( self.burstTime2 ),
                                  self.isNotInteger( self.burstTime3 ),
                                  self.isNotInteger( self.burstTime4 ),
                                  self.isNotInteger( self.burstTime5 ) ]
            
            # process details [ processNum, burstTime, arrivalTime ]
            self.processDetails = {}
            for i in range( len( self.burstTests ) ):
                if self.burstTests[i] == True:
                    if self.burstTime_list[i] == "x":
                        pass
                    else:
                        self.burstError = True
                        break
                else:
                    self.processDetails[i+1] = [ "P{}".format( i+1 ),
                                                 int( self.burstTime_list[i] ),
                                                 int( self.arrivalTime_list[i]),
                                                 int( self.burstTime_list[i] ) ]

            if self.burstError == True:
                #print ( "Error: Invalid Burst Time input." )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Burst Time input" )
            elif self.arrivalError == True:
                #print ( " Error: Invalid Arrival Time input." )
                messagebox.showinfo( "Compute Error" , "Invalid Arrival Time input." )
            else:
                self.backEnd.insert_inputs( self.processDetails)
                self.backEnd.generate_ganttChart()
                self.ganttChart = self.backEnd.get_ganttChart()
                self.caa = self.backEnd.get_caa()
                self.result1_window()

    # This function contains and displays the result data.
    # Result includes:
    #           Gantt Chart
    #           CPU Utilization
    #           ATA
    #           AWT
    def result1_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.srtfLBL = Label ( root , image = srtf_bg, bg = "black" )
        self.srtfLBL.place(x = 0, y = 0)
        self.basicWidgetList.append( self.srtfLBL )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#e1ddd2" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#e1ddd2")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )

        self.title1LBL  =  Label( root , text = "SRTF" , font = ('Times New Roman', 20),  bg = "#e1ddd2")
        self.title1LBL.place(x = 155, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Process Management" , font = ('Times New Roman', 20),  bg = "#e1ddd2")
        self.title2LBL.place(x = 75, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Gantt Chart" , font = ('Times New Roman', 20),  bg = "#c6e3ad")
        self.title3LBL.place(x = 410, y = 160)
        self.basicWidgetList.append( self.title3LBL )
        
        self.physicalMemWidgets = []
        self.xCounter = 210
        self.indexPointer = 0
        
        self.markLBL  =  Label( root , text = 0 , font = ('Times New Roman', 10),  bg = "#c6e3ad")
        self.markLBL.place(x = self.xCounter - 5, y = 310)
        self.physicalMemWidgets.append( self.markLBL )

        self.tempTotalSize = 0
        for tempData in self.ganttChart:
            print( "tempData",  tempData )
            try:
                self.tempTotalSize += tempData[4]
                self.displayChart( tempData[6], tempData[5], tempData[2], tempData[6], self.tempTotalSize )
            except:
                pass

        self.cpuUtilizationLBL  =  Label( root , text = " CPU Utilization" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.cpuUtilizationLBL.place(x = 400, y = 360)
        self.basicWidgetList.append( self.cpuUtilizationLBL )

        self.cpuUtilizationENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuUtilizationENTRY.place(x = 400, y = 405)
        self.cpuUtilizationENTRY.insert( 0, str( round(self.caa[0],2)) + "%" )
        self.cpuUtilizationENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.cpuUtilizationENTRY )

        self.ataLBL  =  Label( root , text = " ATA" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.ataLBL.place(x = 280, y = 360)
        self.basicWidgetList.append( self.ataLBL )

        self.ataENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.ataENTRY.place(x = 235, y = 405)
        self.ataENTRY.insert( 0, str(self.caa[1]) )
        self.ataENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.ataENTRY )

        self.awtLBL  =  Label( root , text = " AWT" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.awtLBL.place(x = 602, y = 360)
        self.basicWidgetList.append( self.awtLBL )

        self.awtENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.awtENTRY.place(x = 565, y = 405)
        self.awtENTRY.insert( 0, str(self.caa[2]) )
        self.awtENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.awtENTRY )


        self.backBTN  =  Button ( root , text = 'BACK',command = self.input1_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 300 ,y = 480)
        self.basicWidgetList.append( self.backBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 490 ,y = 480)
        self.basicWidgetList.append( self.exitBTN )

# END OF SRTF PROGRAM

# START OF ROUND ROBIN PROGRAM

# This class contains all the back end processes/computations.
class rRobin_backEnd:
    def __init__( self ):
        self.quantumTime = 5
        # process details [ processNum, burstTime, arrivalTime, timeRemaining ]
        self.processDetails = { 1 : [ "P1", 12, 4, 12 ],
                                2 : [ "P2", 10, 5, 10],
                                3 : [ "P3", 5, 10, 5],
                                4 : [ "P4", 7, 7, 7]}

        # AWT
        self.awtInfo_dic = {}
        
        # process_queue [ processNum, burstTime, arrivalTime, timeRemaining ]
        self.process_queue = []
        self.numOfProcess = 0
        for i in range ( 1, len( list(self.processDetails )) + 1):
            self.numOfProcess += 1
            self.process_queue.append( [ self.processDetails[i][0],
                                         self.processDetails[i][1],
                                         self.processDetails[i][2],
                                         self.processDetails[i][3] ])
            self.awtInfo_dic[self.processDetails[i][0]] = [ int("-" + str(self.processDetails[i][2])) ]

    # For accepting in the user's input that will be utilized by the backend class.
    def insert_inputs( self, processDetails = None, quantumTime = None ):
        if quantumTime == None:
            self.quantumTime = 5
        else:
            self.quantumTime = quantumTime
            
        # process details [ processNum, burstTime, arrivalTime, timeRemaining ]
        if processDetails == None:
            self.processDetails = { 1 : [ "P1", 12, 4, 12 ],
                                    2 : [ "P2", 10, 5, 10],
                                    3 : [ "P3", 5, 10, 5],
                                    4 : [ "P4", 7, 7, 7]}
        else:
            self.processDetails = processDetails

        # AWT
        self.awtInfo_dic = {}
        
        # process_queue [ processNum, burstTime, arrivalTime, timeRemaining ]
        self.process_queue = []
        self.numOfProcess = 0
        for i in range ( 1, len( list(self.processDetails )) + 1):
            self.numOfProcess += 1
            self.process_queue.append( [ self.processDetails[i][0],
                                         self.processDetails[i][1],
                                         self.processDetails[i][2],
                                         self.processDetails[i][3] ])
            self.awtInfo_dic[self.processDetails[i][0]] = [ int("-" + str(self.processDetails[i][2])) ]
            

            

    # returns the ganttChart list
    def get_ganttChart( self ):
        return self.ganttChart

    # returns the caa list which contains CPU Utilization, ATA, AWT.
    def get_caa( self ):
        return self.caa


    # This function will check whether the given process number has already arrived
    def hasProcessArrived( self, processNum, time ):
        if self.processDetails[processNum][2] <= time:
            return True
        else:
            return False

    # This function will deduct 1 in the remainingTime of the given processNum
    def deductTime( self, processNum ):
        try:
            self.processDetails[processNum][3] -= 1
        except:
            pass
        return

    # This function will check whether the given processNum is already finished.
    # If it already have a remainingTime of less than or equal to 0, the processNumber will be removed from the waitingList
    def isProcessFinished( self, processNum ):
        #print( processNum )
        if self.processDetails[processNum][3] <= 0:
            try:
                self.waitingList.remove( processNum )
            except:
                print( "fail", processNum )
                pass
            return True
        else:
            return False
    
    def generate_ganttChart( self ):
        # gantt chart [ start, finish, processNum, arrivalTime, burstTime, percentageprocess ]
        self.ganttChart = []

        # sort the process_queue by its arrival time.
        # process_queue [ processNum, burstTime, arrivalTime, timeRemaining ]
        self.process_queue = sorted( self.process_queue, key=lambda x: x[2] )
        self.numberOfProcesses = len( self.process_queue )

        self.waitingList = []
        for i in range( len( self.process_queue ) ):
            self.waitingList.append( int(self.process_queue[i][0][1]) )
            
        self.tempProcess_queue = deepcopy( self.process_queue )
        self.tempResult_queue = []
        self.tempResult_dic = {}
        # ataInfo_dic processNum : finishTime
        self.ataInfo_dic = {}


        self.isFinished = False
        self.currentProcessNum = self.waitingList[0]
        self.nextProcessNum = self.waitingList[1]
        self.currentTime = 0
        self.pastProcesses = []
        while self.isFinished == False:
            self.test = self.hasProcessArrived( self.currentProcessNum, self.currentTime )
            if self.test == False:
                #print ( "XXX", self.currentTime )
                self.tempResult_dic[self.currentTime] = "Idle"
                self.currentTime += 1
            else:
                for i in range( self.quantumTime ):
                    self.deductTime( self.currentProcessNum )
                    self.tempResult_dic[self.currentTime] = "P{}".format( self.currentProcessNum )
                    self.currentTime += 1
                    self.ataInfo_dic["P{}".format( self.currentProcessNum )] = [ self.currentTime, self.processDetails[self.currentProcessNum][2] ]
                    self.test2 = self.isProcessFinished( self.currentProcessNum )
                    if self.test2 == True:
                        break
                if len(self.waitingList) == 0:
                    break
                self.currentProcessNum = self.nextProcessNum
                if self.currentProcessNum == self.waitingList[-1]:
                    self.nextProcessNum = self.waitingList[0]
                else:
                    self.tempIndex = self.waitingList.index( self.currentProcessNum )
                    self.nextProcessNum = self.waitingList[self.tempIndex+1]
            if len(self.waitingList) == 0:
                break
        #print( "waitingList", self.waitingList )
        #print( "end", self.currentProcessNum, self.nextProcessNum )
        print( "xResult", self.tempResult_dic )

                
        #print ( self.tempResult_dic )
        print( "ataInfo", self.ataInfo_dic )
        
        self.prevProcess = "N/A"
        self.currentProcess = "N/A"
        self.tempColors = { "Idle" : "#bfbaac",
                            "P1" : "#f77777",
                            "P2" : "#f7d977",
                            "P3" : "#77f7e6",
                            "P4" : "#77d5f7",
                            "P5" : "#d577f7",
                            "EXTRA" : "#fcba03" }

        # In this block of code, we will turn the tempResult_dic into the ganttChart data        
        self.idleTime = 0
        for time in list(self.tempResult_dic):
            self.time = time
            self.currentProcess = self.tempResult_dic[time]
            if self.currentProcess == "Idle":
                self.idleTime += 1
                
            if self.prevProcess != "N/A":
                if self.currentProcess != self.prevProcess:
                    try:
                        self.ganttChart.append( [ self.startTime,
                                              self.time,
                                              self.tempResult_dic[self.time-1],
                                              self.time,
                                              self.time - self.startTime,
                                              self.tempColors[self.tempResult_dic[self.time-1]] ] )
                        if self.tempResult_dic[self.time-1] in self.awtInfo_dic:
                            self.awtInfo_dic[self.tempResult_dic[self.time-1]].append( self.startTime )
                            self.awtInfo_dic[self.tempResult_dic[self.time-1]].append( int("-" + str(self.time)) )
                    except:
                        pass
                    self.startTime = self.time
            else:
                self.startTime = self.time
                
            self.prevProcess = self.currentProcess
        else:
            self.time += 1
            self.ganttChart.append( [ self.startTime,
                                      self.time,
                                      self.tempResult_dic[self.time-1],
                                      self.time,
                                      (self.time) - self.startTime,
                                      self.tempColors[self.tempResult_dic[self.time-1]] ] )
            if self.tempResult_dic[self.time-1] in self.awtInfo_dic:
                            self.awtInfo_dic[self.tempResult_dic[self.time-1]].append( self.startTime )
                            self.awtInfo_dic[self.tempResult_dic[self.time-1]].append( int("-" + str(self.time)) )

        for i in range( len(self.ganttChart) ):
            self.ganttChart[i].append( float(( float(self.ganttChart[i][4]) / float(self.time) ) * 100 ))

        # The program will compute for the average turn around time here
        self.ata = 0.0
        for processNum in list( self.ataInfo_dic ):
            self.ata += ( self.ataInfo_dic[processNum][0] - self.ataInfo_dic[processNum][1] )

        # The program will compute for the average waiting time here
        self.awt = 0.0
        for processNum in list( self.awtInfo_dic ):
            self.tempCalc = 0.0
            if len(self.awtInfo_dic[processNum]) // 2 != 0:
                self.awtInfo_dic[processNum].pop( -1 )
            for i in range( len( self.awtInfo_dic[processNum] )):
                self.tempCalc += self.awtInfo_dic[processNum][i]
            self.awt += self.tempCalc

        # The final computations for cpuUtilization, ata, and awt
        
        self.cpuUtilization = round((( 1-(self.idleTime/self.time)) * 100 ), 2 )
        self.ata = round(( self.ata ) / len(self.ataInfo_dic), 2)
        self.awt = round(( self.awt ) / len(self.awtInfo_dic), 2)

        # Put the calculated cpuUtilization, ata, and awt into one list
        # The data inside this list will be displayed to the user.
        self.caa = [ self.cpuUtilization,
                     self.ata,
                     self.awt ]
                     
        print ( self.cpuUtilization )
        print( self.ata )
        print( self.awt )
        print( "awtInfo", self.awtInfo_dic )
        
        #self.caa = [ 0, 0, 0 ]
        
        

# This contains all the necessary functions for the frontEnd.
# This mostly contains widget placements.
class rRobin_frontEnd:
    def __init__( self ):
        self.backEnd = rRobin_backEnd()
        self.backEnd.generate_ganttChart()
        self.ganttChart = self.backEnd.get_ganttChart()
        self.caa = self.backEnd.get_caa()
        #self.caa = self.backEnd.get_caa()

    # For getting the current date
    def current_date( self ):
        self.dateString  =  datetime.date.today().strftime("%B %d, %Y")
        self.dateLBL.config(text = self.dateString)

    
    # This updates the clock widget
    def tick( self ):
        if self.tick_on:
            self.timeString  =  time.strftime("%H:%M:%S")
            self.clockLBL.config(text = self.timeString)
            self.clockLBL.after(200, self.tick )
        else:
            pass

    # This function returns True if the integerInput is not an Integer.
    # If it is an integer, return False.
    def isNotInteger( self, integerInput):
        try:
            self.intTest = int(integerInput)
            return False
        except ValueError:
            return True

    # The program has two list which contains a reference to all the program's widgets
    # And what this function does is it tries to clear/destroy all of these widgets
    # using the lists which contains the program's widgets.
    # The two lists are:
    #   - self.basicWidgetList: For most of the basic widgets
    #   - self.physicalMemWidgets: For the widgets used to display physical memory map
    def clearWidgets( self ):
        try:
            self.tick_on = False
            self.clearWidgetList( self.basicWidgetList )
            self.clearWidgetList( self.physicalMemWidgets )
        except:
            pass
        return


    # This function destroys all of the widgets inside the inputted widgetsToClear list.
    def clearWidgetList ( self, widgetsToClear):
        for widget in widgetsToClear:
            widget.destroy()


    # This function displays the necessary widgets for the gantt chart.
    # To get a general gist, the program has around 50 labels which acts as the gantt chart.
    # In addition, it has a text label which marks each section of the gantt chart
    def displayChart( self, tempPointer, tempColor, tempText, tempPercentage, tempTotalSize ):
        self.tempPointer = int(tempPointer)
        self.tempColor = tempColor
        self.tempText = tempText
        self.tempPercentage = tempPercentage
        self.tempTotalSize = tempTotalSize
        
        if self.tempPercentage != 0:
            self.tempLBL = Label( root , text = " ", font = ('Times New Roman', 30),  bg = self.tempColor)
            self.tempLBL.place(x = self.xCounter, y = 250)
            self.physicalMemWidgets.append( self.tempLBL )
            
            self.tempLBL = Label( root , text = self.tempText , font = ('Times New Roman', 10),  bg = self.tempColor)
            self.tempLBL.place(x = self.xCounter, y = 220)
            self.physicalMemWidgets.append( self.tempLBL )
            self.xCounter += 10
        ##print( int( self.tempPercentage ) )
        for i in range( int( self.tempPercentage/2 ) ):
            if self.tempPointer != 0:
                ##print( i )
                self.tempLBL = Label( root , text = " " , font = ('Times New Roman', 30),  bg = self.tempColor)
                self.tempLBL.place(x = self.xCounter, y = 250)
                self.xCounter += 10
                self.physicalMemWidgets.append( self.tempLBL )
                self.tempPointer -= 1
            else:
                pass
        if self.tempPercentage != 0:
            self.tempLBL  =  Label( root , text = tempTotalSize , font = ('Times New Roman', 10),  bg = "#c6e3ad")
            self.tempLBL.place(x = self.xCounter - 5, y = 310)
            self.physicalMemWidgets.append( self.tempLBL )
        return

    def mainMenuBTN_Pressed( self ):
        main.mainMenu_window()

    def aboutUsBTN_Pressed( self ):
        main.aboutUs_window()

    # This is the input window that will take in the user's inputs.
    def input1_window( self ):
        root.title ( "Round Robin Process Management" )
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.rrLBL = Label ( root , image = rr_bg, bg = "black" )
        self.rrLBL.place(x = 0, y = 0)
        self.basicWidgetList.append( self.rrLBL )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#4ec2c2" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#4ec2c2")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )

        self.mainMenuBTN  =  Button ( root , image = mainMenu_btn, command = self.mainMenuBTN_Pressed , bg = "#4ec2c2" )
        self.mainMenuBTN.place (x = 850 ,y = 60)
        self.basicWidgetList.append( self.mainMenuBTN )

        self.aboutBTN  =  Button ( root , image = aboutUs_btn, command = self.aboutUsBTN_Pressed, bg = "#4ec2c2" )
        self.aboutBTN.place (x = 850 ,y = 10)
        self.basicWidgetList.append( self.aboutBTN )
        
        self.title1LBL  =  Label( root , text = "Round Robin" , font = ('Times New Roman', 20),  bg = "#4ec2c2")
        self.title1LBL.place(x = 120, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Process Management" , font = ('Times New Roman', 20),  bg = "#4ec2c2")
        self.title2LBL.place(x = 75, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Input Window" , font = ('Times New Roman', 30),  bg = "#c6e3ad")
        self.title3LBL.place(x = 370, y = 108)
        self.basicWidgetList.append( self.title3LBL )

        # Process Num
        self.processLBL  =  Label( root , text = "Process" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.processLBL.place(x = 285, y = 160)
        self.basicWidgetList.append( self.processLBL )

        self.process1LBL  =  Label( root , text = "1" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process1LBL.place(x = 315, y = 210)
        self.basicWidgetList.append( self.process1LBL )
        
        self.process2LBL  =  Label( root , text = "2" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process2LBL.place(x = 315, y = 260)
        self.basicWidgetList.append( self.process2LBL )
        
        self.process3LBL  =  Label( root , text = "3" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process3LBL.place(x = 315, y = 310)
        self.basicWidgetList.append( self.process3LBL )

        self.process4LBL  =  Label( root , text = "4" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process4LBL.place(x = 315, y = 360)
        self.basicWidgetList.append( self.process4LBL )
        
        self.process5LBL  =  Label( root , text = "5" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process5LBL.place(x = 315, y = 410)
        self.basicWidgetList.append( self.process5LBL )


        # Burst Time Widgets
        self.burstTimeLBL  =  Label( root , text = "Burst Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.burstTimeLBL.place(x = 425, y = 160)
        self.basicWidgetList.append( self.burstTimeLBL )
        
        self.burstTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime1ENTRY.place(x = 400, y = 210)
        self.basicWidgetList.append( self.burstTime1ENTRY )
        
        self.burstTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime2ENTRY.place(x = 400, y = 260)
        self.basicWidgetList.append( self.burstTime2ENTRY )
        
        self.burstTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime3ENTRY.place(x = 400, y = 310)
        self.basicWidgetList.append( self.burstTime3ENTRY )

        self.burstTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime4ENTRY.place(x = 400, y = 360)
        self.basicWidgetList.append( self.burstTime4ENTRY )
        
        self.burstTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime5ENTRY.place(x = 400, y = 410)
        self.basicWidgetList.append( self.burstTime5ENTRY )
        

        # Arrival Time Widgets
        self.arrivalTimeLBL  =  Label( root , text = "Arrival Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.arrivalTimeLBL.place(x = 585, y = 160)
        self.basicWidgetList.append( self.arrivalTimeLBL )

        self.arrivalTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime1ENTRY.place(x = 570, y = 210)
        self.basicWidgetList.append( self.arrivalTime1ENTRY )
        
        self.arrivalTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime2ENTRY.place(x = 570, y = 260)
        self.basicWidgetList.append( self.arrivalTime2ENTRY )
        
        self.arrivalTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime3ENTRY.place(x = 570, y = 310)
        self.basicWidgetList.append( self.arrivalTime3ENTRY )

        self.arrivalTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime4ENTRY.place(x = 570, y = 360)
        self.basicWidgetList.append( self.arrivalTime4ENTRY )
        
        self.arrivalTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime5ENTRY.place(x = 570, y = 410)
        self.basicWidgetList.append( self.arrivalTime5ENTRY )

        # Quantum Time Widgets
        self.quantumTimeLBL  =  Label( root , text = "Quantum Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.quantumTimeLBL.place(x = 350, y = 450)
        self.basicWidgetList.append( self.quantumTimeLBL )

        self.quantumTimeENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.quantumTimeENTRY.place(x = 490, y = 450)
        self.basicWidgetList.append( self.quantumTimeENTRY )
        
        self.computeBTN  =  Button ( root , text = 'Compute',command = self.input1_computeBTN_Pressed , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.computeBTN.place (x = 390 ,y = 500)
        self.basicWidgetList.append( self.computeBTN )

        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 550)
        self.basicWidgetList.append( self.exitBTN )


    # Once the user wants to proceed with the computation, this function will be executed.
    def input1_computeBTN_Pressed( self ):
        #print( "input1_computeBTN_Pressed" )
        if messagebox.askyesno( "Confirmation..." , " Are you sure you want to compute? " ) == True :
            self.arrivalTime1 = self.arrivalTime1ENTRY.get()
            self.arrivalTime2 = self.arrivalTime2ENTRY.get()
            self.arrivalTime3 = self.arrivalTime3ENTRY.get()
            self.arrivalTime4 = self.arrivalTime4ENTRY.get()
            self.arrivalTime5 = self.arrivalTime5ENTRY.get()
            self.arrivalTime_list = [ self.arrivalTime1,
                                      self.arrivalTime2,
                                      self.arrivalTime3,
                                      self.arrivalTime4,
                                      self.arrivalTime5 ]

            self.arrivalError = False
            self.arrivalTests = [ self.isNotInteger( self.arrivalTime1 ),
                                  self.isNotInteger( self.arrivalTime2 ),
                                  self.isNotInteger( self.arrivalTime3 ),
                                  self.isNotInteger( self.arrivalTime4 ),
                                  self.isNotInteger( self.arrivalTime5 ) ]
            for i in range( len( self.arrivalTests ) ):
                if self.arrivalTests[i] == True:
                    if self.arrivalTime_list[i] == "x":
                        pass
                    else:
                        self.arrivalError = True
                        break

            self.burstTime1 = self.burstTime1ENTRY.get()
            self.burstTime2 = self.burstTime2ENTRY.get()
            self.burstTime3 = self.burstTime3ENTRY.get()
            self.burstTime4 = self.burstTime4ENTRY.get()
            self.burstTime5 = self.burstTime5ENTRY.get()
            self.burstTime_list = [ self.burstTime1,
                                      self.burstTime2,
                                      self.burstTime3,
                                      self.burstTime4,
                                      self.burstTime5 ]

            self.burstError = False
            self.burstTests = [ self.isNotInteger( self.burstTime1 ),
                                  self.isNotInteger( self.burstTime2 ),
                                  self.isNotInteger( self.burstTime3 ),
                                  self.isNotInteger( self.burstTime4 ),
                                  self.isNotInteger( self.burstTime5 ) ]
            
            # process details [ processNum, burstTime, arrivalTime ]
            self.processDetails = {}
            for i in range( len( self.burstTests ) ):
                if self.burstTests[i] == True:
                    if self.burstTime_list[i] == "x":
                        pass
                    else:
                        self.burstError = True
                        break
                else:
                    self.processDetails[i+1] = [ "P{}".format( i+1 ),
                                                 int( self.burstTime_list[i] ),
                                                 int( self.arrivalTime_list[i]),
                                                 int( self.burstTime_list[i] ) ]

            self.quantumTime = self.quantumTimeENTRY.get()
            self.quantumError = self.isNotInteger( self.quantumTime )
            if self.burstError == True:
                #print ( "Error: Invalid Burst Time input." )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Burst Time input" )
            elif self.arrivalError == True:
                #print ( " Error: Invalid Arrival Time input." )
                messagebox.showinfo( "Compute Error" , "Invalid Arrival Time input." )
            elif self.quantumError == True:
                #print ( " Error: Invalid Arrival Time input." )
                messagebox.showinfo( "Compute Error" , "Invalid Quantum Time input." )
            else:
                self.backEnd.insert_inputs( self.processDetails, int(self.quantumTime) )
                self.backEnd.generate_ganttChart()
                self.ganttChart = self.backEnd.get_ganttChart()
                self.caa = self.backEnd.get_caa()
                self.result1_window()

    # This function contains and displays the result data.
    # Result includes:
    #           Gantt Chart
    #           CPU Utilization
    #           ATA
    #           AWT
    def result1_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.rrLBL = Label ( root , image = rr_bg, bg = "black" )
        self.rrLBL.place(x = 0, y = 0)
        self.basicWidgetList.append( self.rrLBL )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#4ec2c2" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#4ec2c2")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )

        self.title1LBL  =  Label( root , text = "Round Robin" , font = ('Times New Roman', 20),  bg = "#4ec2c2")
        self.title1LBL.place(x = 120, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Process Management" , font = ('Times New Roman', 20),  bg = "#4ec2c2")
        self.title2LBL.place(x = 75, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Gantt Chart" , font = ('Times New Roman', 20),  bg = "#c6e3ad")
        self.title3LBL.place(x = 410, y = 160)
        self.basicWidgetList.append( self.title3LBL )
        
        self.physicalMemWidgets = []
        self.xCounter = 210
        self.indexPointer = 0
        
        self.markLBL  =  Label( root , text = 0 , font = ('Times New Roman', 10),  bg = "#c6e3ad")
        self.markLBL.place(x = self.xCounter - 5, y = 310)
        self.physicalMemWidgets.append( self.markLBL )

        self.tempTotalSize = 0
        for tempData in self.ganttChart:
            print( "tempData",  tempData )
            try:
                self.tempTotalSize += tempData[4]
                self.displayChart( tempData[6], tempData[5], tempData[2], tempData[6], self.tempTotalSize )
            except:
                pass

        self.cpuUtilizationLBL  =  Label( root , text = " CPU Utilization" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.cpuUtilizationLBL.place(x = 400, y = 360)
        self.basicWidgetList.append( self.cpuUtilizationLBL )

        self.cpuUtilizationENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuUtilizationENTRY.place(x = 400, y = 405)
        self.cpuUtilizationENTRY.insert( 0, str( round(self.caa[0],2)) + "%" )
        self.cpuUtilizationENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.cpuUtilizationENTRY )

        self.ataLBL  =  Label( root , text = " ATA" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.ataLBL.place(x = 280, y = 360)
        self.basicWidgetList.append( self.ataLBL )

        self.ataENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.ataENTRY.place(x = 235, y = 405)
        self.ataENTRY.insert( 0, str(self.caa[1]) )
        self.ataENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.ataENTRY )

        self.awtLBL  =  Label( root , text = " AWT" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.awtLBL.place(x = 602, y = 360)
        self.basicWidgetList.append( self.awtLBL )

        self.awtENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.awtENTRY.place(x = 565, y = 405)
        self.awtENTRY.insert( 0, str(self.caa[2]) )
        self.awtENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.awtENTRY )


        self.backBTN  =  Button ( root , text = 'BACK',command = self.input1_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 300 ,y = 480)
        self.basicWidgetList.append( self.backBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 490 ,y = 480)
        self.basicWidgetList.append( self.exitBTN )

# END OF ROUND ROBIN PROGRAM


# START OF PRIORITY PROGRAM

# This class contains all the back end processes/computations.
class pty_backEnd:
    def __init__( self ):
        # process details [ processNum, burstTime, arrivalTime, priorityNum ]
        self.processDetails = { 1 : [ "P1", 12, 4, 2 ],
                                2 : [ "P2", 10, 5, 1],
                                3 : [ "P3", 5, 10, 4],
                                4 : [ "P4", 7, 7, 3]}

        # AWT
        self.awtInfo_dic = {}
        
        # process_queue [ processNum, burstTime, arrivalTime, priorityNum, timeRemaining ]
        self.process_queue = []
        self.numOfProcess = 0
        for i in range ( 1, len( list(self.processDetails )) + 1):
            self.numOfProcess += 1
            self.process_queue.append( [ self.processDetails[i][0],
                                         self.processDetails[i][1],
                                         self.processDetails[i][2],
                                         self.processDetails[i][3],
                                         self.processDetails[i][1] ])
            self.awtInfo_dic[self.processDetails[i][0]] = [ int("-" + str(self.processDetails[i][2])) ]
        print ( "awtInfo", self.awtInfo_dic )
        print( self.process_queue )

    # For accepting in the user's input that will be utilized by the backend class.
    def insert_inputs( self, processDetails = None ):
        # process details [ processNum, burstTime, arrivalTime, priorityNum ]
        if processDetails == None:
            self.processDetails = { 1 : [ "P1", 12, 4, 2 ],
                                    2 : [ "P2", 10, 5, 1],
                                    3 : [ "P3", 5, 10, 4],
                                    4 : [ "P4", 7, 7, 3]}
        else:
            self.processDetails = processDetails

        # AWT
        self.awtInfo_dic = {}
        
        # process_queue [ processNum, burstTime, arrivalTime, priorityNum, timeRemaining ]
        self.process_queue = []
        self.numOfProcess = 0
        for i in range ( 1, len( list(self.processDetails )) + 1):
            self.numOfProcess += 1
            self.process_queue.append( [ self.processDetails[i][0],
                                         self.processDetails[i][1],
                                         self.processDetails[i][2],
                                         self.processDetails[i][3],
                                         self.processDetails[i][1] ])
            self.awtInfo_dic[self.processDetails[i][0]] = [ int("-" + str(self.processDetails[i][2])) ]
            

            

    # returns the ganttChart list
    def get_ganttChart( self ):
        return self.ganttChart

    # returns the caa list which contains CPU Utilization, ATA, AWT.
    def get_caa( self ):
        return self.caa
    
    def generate_ganttChart( self ):
        # gantt chart [ start, finish, processNum, arrivalTime, burstTime, percentageprocess ]
        self.ganttChart = []

        # sort the process_queue by its arrival time.
        # process_queue [ processNum, burstTime, arrivalTime, priorityNum, timeRemaining ]
        self.process_queue = sorted( self.process_queue, key=lambda x: x[2] )

        self.tempProcess_queue = deepcopy( self.process_queue )
        self.tempResult_queue = []
        self.currentTime = 0
        self.tempResult_dic = {}
        # ataInfo_dic processNum : finishTime
        self.ataInfo_dic = {}


        self.isFinished = False
        self.prevProcess = -1
        while self.isFinished == False:
            # waitingList [ processNum, index, priorityNum ]
            self.waitingList = []
            
            # In this loop, we will be taking note of all the process that has already arrived
            for i in range( len(self.tempProcess_queue) ):
                if self.currentTime >= self.tempProcess_queue[i][2]:
                    self.waitingList.append( [ self.tempProcess_queue[i][0],
                                               i,
                                               self.tempProcess_queue[i][3] ] )

            # We will check what process should be processed during the current time
            # After knowing the process number, we will take note of it inside "self.tempResult_dic"
            try:
                # If there are no process yet to arrive, we replace the processNum into "Idle"
                if len(self.waitingList) == 0 and len(self.tempProcess_queue) != 0:
                    self.tempResult_dic[self.currentTime] = "Idle"
                    self.currentTime += 1
                else: # otherwise, the program will take note of the processNum
                    self.waitingList = sorted( self.waitingList, key= lambda x: x[2] )
                    self.currentProcess = self.waitingList[0][1]

                    self.tempProcess_queue[self.currentProcess][4] -= 1
                    self.tempResult_dic[self.currentTime] = self.tempProcess_queue[self.currentProcess][0]
                    self.currentTime += 1
                    self.ataInfo_dic[self.waitingList[0][0]] = [ self.currentTime, self.tempProcess_queue[self.currentProcess][2] ]

                    if self.tempProcess_queue[self.currentProcess][4] <= 0:
                        self.tempProcess_queue.pop( self.currentProcess )

                if len(self.tempProcess_queue) == 0:
                    break
            except:
                break
                
        #print ( self.tempResult_dic )
        print( "ataInfo", self.ataInfo_dic )
        
        self.prevProcess = "N/A"
        self.currentProcess = "N/A"
        self.tempColors = { "Idle" : "#bfbaac",
                            "P1" : "#f77777",
                            "P2" : "#f7d977",
                            "P3" : "#77f7e6",
                            "P4" : "#77d5f7",
                            "P5" : "#d577f7",
                            "EXTRA" : "#fcba03" }

        # In this block of code, we will turn the tempResult_dic into the ganttChart data        
        self.idleTime = 0
        for time in list(self.tempResult_dic):
            self.time = time
            self.currentProcess = self.tempResult_dic[time]
            if self.currentProcess == "Idle":
                self.idleTime += 1
                
            if self.prevProcess != "N/A":
                if self.currentProcess != self.prevProcess:
                    try:
                        self.ganttChart.append( [ self.startTime,
                                              self.time,
                                              self.tempResult_dic[self.time-1],
                                              self.time,
                                              self.time - self.startTime,
                                              self.tempColors[self.tempResult_dic[self.time-1]] ] )
                        if self.tempResult_dic[self.time-1] in self.awtInfo_dic:
                            self.awtInfo_dic[self.tempResult_dic[self.time-1]].append( self.startTime )
                            self.awtInfo_dic[self.tempResult_dic[self.time-1]].append( int("-" + str(self.time)) )
                    except:
                        pass
                    self.startTime = self.time
            else:
                self.startTime = self.time
                
            self.prevProcess = self.currentProcess
        else:
            self.time += 1
            self.ganttChart.append( [ self.startTime,
                                      self.time,
                                      self.tempResult_dic[self.time-1],
                                      self.time,
                                      (self.time) - self.startTime,
                                      self.tempColors[self.tempResult_dic[self.time-1]] ] )
            if self.tempResult_dic[self.time-1] in self.awtInfo_dic:
                            self.awtInfo_dic[self.tempResult_dic[self.time-1]].append( self.startTime )
                            self.awtInfo_dic[self.tempResult_dic[self.time-1]].append( int("-" + str(self.time)) )

        for i in range( len(self.ganttChart) ):
            self.ganttChart[i].append( float(( float(self.ganttChart[i][4]) / float(self.time) ) * 100 ))

        # The program will compute for the average turn around time here
        self.ata = 0.0
        for processNum in list( self.ataInfo_dic ):
            self.ata += ( self.ataInfo_dic[processNum][0] - self.ataInfo_dic[processNum][1] )

        # The program will compute for the average waiting time here
        self.awt = 0.0
        for processNum in list( self.awtInfo_dic ):
            self.tempCalc = 0.0
            if len(self.awtInfo_dic[processNum]) // 2 != 0:
                self.awtInfo_dic[processNum].pop( -1 )
            for i in range( len( self.awtInfo_dic[processNum] )):
                self.tempCalc += self.awtInfo_dic[processNum][i]
            self.awt += self.tempCalc

        # The final computations for cpuUtilization, ata, and awt
        self.cpuUtilization = round((( 1-(self.idleTime/self.time)) * 100 ), 2 )
        self.ata = round(( self.ata ) / len(self.ataInfo_dic), 2)
        self.awt = round(( self.awt ) / len(self.awtInfo_dic), 2)

        # Put the calculated cpuUtilization, ata, and awt into one list
        # The data inside this list will be displayed to the user.
        self.caa = [ self.cpuUtilization,
                     self.ata,
                     self.awt ]
        """
        print ( self.cpuUtilization )
        print( self.ata )
        print( self.awt )
        print( "awtInfo", self.awtInfo_dic )
        """
        
        

# This contains all the necessary functions for the frontEnd.
# This mostly contains widget placements.
class pty_frontEnd:
    def __init__( self ):
        self.backEnd = pty_backEnd()
        self.backEnd.generate_ganttChart()
        self.ganttChart = self.backEnd.get_ganttChart()
        self.caa = self.backEnd.get_caa()
        #self.caa = self.backEnd.get_caa()

    # For getting the current date
    def current_date( self ):
        self.dateString  =  datetime.date.today().strftime("%B %d, %Y")
        self.dateLBL.config(text = self.dateString)

    
    # This updates the clock widget
    def tick( self ):
        if self.tick_on:
            self.timeString  =  time.strftime("%H:%M:%S")
            self.clockLBL.config(text = self.timeString)
            self.clockLBL.after(200, self.tick )
        else:
            pass

    # This function returns True if the integerInput is not an Integer.
    # If it is an integer, return False.
    def isNotInteger( self, integerInput):
        try:
            self.intTest = int(integerInput)
            return False
        except ValueError:
            return True

    # The program has two list which contains a reference to all the program's widgets
    # And what this function does is it tries to clear/destroy all of these widgets
    # using the lists which contains the program's widgets.
    # The two lists are:
    #   - self.basicWidgetList: For most of the basic widgets
    #   - self.physicalMemWidgets: For the widgets used to display physical memory map
    def clearWidgets( self ):
        try:
            self.tick_on = False
            self.clearWidgetList( self.basicWidgetList )
            self.clearWidgetList( self.physicalMemWidgets )
        except:
            pass
        return


    # This function destroys all of the widgets inside the inputted widgetsToClear list.
    def clearWidgetList ( self, widgetsToClear):
        for widget in widgetsToClear:
            widget.destroy()


    # This function displays the necessary widgets for the gantt chart.
    # To get a general gist, the program has around 50 labels which acts as the gantt chart.
    # In addition, it has a text label which marks each section of the gantt chart
    def displayChart( self, tempPointer, tempColor, tempText, tempPercentage, tempTotalSize ):
        self.tempPointer = int(tempPointer)
        self.tempColor = tempColor
        self.tempText = tempText
        self.tempPercentage = tempPercentage
        self.tempTotalSize = tempTotalSize
        
        if self.tempPercentage != 0:
            self.tempLBL = Label( root , text = " ", font = ('Times New Roman', 30),  bg = self.tempColor)
            self.tempLBL.place(x = self.xCounter, y = 250)
            self.physicalMemWidgets.append( self.tempLBL )
            
            self.tempLBL = Label( root , text = self.tempText , font = ('Times New Roman', 10),  bg = self.tempColor)
            self.tempLBL.place(x = self.xCounter, y = 220)
            self.physicalMemWidgets.append( self.tempLBL )
            self.xCounter += 10
        ##print( int( self.tempPercentage ) )
        for i in range( int( self.tempPercentage/2 ) ):
            if self.tempPointer != 0:
                ##print( i )
                self.tempLBL = Label( root , text = " " , font = ('Times New Roman', 30),  bg = self.tempColor)
                self.tempLBL.place(x = self.xCounter, y = 250)
                self.xCounter += 10
                self.physicalMemWidgets.append( self.tempLBL )
                self.tempPointer -= 1
            else:
                pass
        if self.tempPercentage != 0:
            self.tempLBL  =  Label( root , text = tempTotalSize , font = ('Times New Roman', 10),  bg = "#c6e3ad")
            self.tempLBL.place(x = self.xCounter - 5, y = 310)
            self.physicalMemWidgets.append( self.tempLBL )
        return

    def mainMenuBTN_Pressed( self ):
        main.mainMenu_window()

    def aboutUsBTN_Pressed( self ):
        main.aboutUs_window()
        
    # This is the input window that will take in the user's inputs.
    def input1_window( self ):
        root.title ( "Priority Process Management" )
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.pLBL = Label ( root , image = p_bg, bg = "black" )
        self.pLBL.place(x = 0, y = 0)
        self.basicWidgetList.append( self.pLBL )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#4ec2c2" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#4ec2c2")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )

        self.mainMenuBTN  =  Button ( root , image = mainMenu_btn, command = self.mainMenuBTN_Pressed , bg = "#4ec2c2" )
        self.mainMenuBTN.place (x = 850 ,y = 60)
        self.basicWidgetList.append( self.mainMenuBTN )

        self.aboutBTN  =  Button ( root , image = aboutUs_btn, command = self.aboutUsBTN_Pressed, bg = "#4ec2c2" )
        self.aboutBTN.place (x = 850 ,y = 10)
        
        self.title1LBL  =  Label( root , text = "Priority" , font = ('Times New Roman', 20),  bg = "#4ec2c2")
        self.title1LBL.place(x = 150, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Process Management" , font = ('Times New Roman', 20),  bg = "#4ec2c2")
        self.title2LBL.place(x = 75, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Input Window" , font = ('Times New Roman', 30),  bg = "#c6e3ad")
        self.title3LBL.place(x = 370, y = 108)
        self.basicWidgetList.append( self.title3LBL )

        # Process Num
        self.processLBL  =  Label( root , text = "Process" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.processLBL.place(x = 170, y = 160)
        self.basicWidgetList.append( self.processLBL )

        self.process1LBL  =  Label( root , text = "1" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process1LBL.place(x = 190, y = 210)
        self.basicWidgetList.append( self.process1LBL )
        
        self.process2LBL  =  Label( root , text = "2" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process2LBL.place(x = 190, y = 260)
        self.basicWidgetList.append( self.process2LBL )
        
        self.process3LBL  =  Label( root , text = "3" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process3LBL.place(x = 190, y = 310)
        self.basicWidgetList.append( self.process3LBL )

        self.process4LBL  =  Label( root , text = "4" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process4LBL.place(x = 190, y = 360)
        self.basicWidgetList.append( self.process4LBL )
        
        self.process5LBL  =  Label( root , text = "5" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.process5LBL.place(x = 190, y = 410)
        self.basicWidgetList.append( self.process5LBL )

        # Burst Time
        self.burstTimeLBL  =  Label( root , text = "Burst Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.burstTimeLBL.place(x = 340, y = 160)
        self.basicWidgetList.append( self.burstTimeLBL )
        
        self.burstTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime1ENTRY.place(x = 315, y = 210)
        self.basicWidgetList.append( self.burstTime1ENTRY )
        
        self.burstTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime2ENTRY.place(x = 315, y = 260)
        self.basicWidgetList.append( self.burstTime2ENTRY )
        
        self.burstTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime3ENTRY.place(x = 315, y = 310)
        self.basicWidgetList.append( self.burstTime3ENTRY )

        self.burstTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime4ENTRY.place(x = 315, y = 360)
        self.basicWidgetList.append( self.burstTime4ENTRY )
        
        self.burstTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.burstTime5ENTRY.place(x = 315, y = 410)
        self.basicWidgetList.append( self.burstTime5ENTRY )
        
        # Arrival Time
        self.arrivalTimeLBL  =  Label( root , text = "Arrival Time" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.arrivalTimeLBL.place(x = 505, y = 160)
        self.basicWidgetList.append( self.arrivalTimeLBL )

        self.arrivalTime1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime1ENTRY.place(x = 490, y = 210)
        self.basicWidgetList.append( self.arrivalTime1ENTRY )
        
        self.arrivalTime2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime2ENTRY.place(x = 490, y = 260)
        self.basicWidgetList.append( self.arrivalTime2ENTRY )
        
        self.arrivalTime3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime3ENTRY.place(x = 490, y = 310)
        self.basicWidgetList.append( self.arrivalTime3ENTRY )

        self.arrivalTime4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime4ENTRY.place(x = 490, y = 360)
        self.basicWidgetList.append( self.arrivalTime4ENTRY )
        
        self.arrivalTime5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.arrivalTime5ENTRY.place(x = 490, y = 410)
        self.basicWidgetList.append( self.arrivalTime5ENTRY )

        # Priority Num
        self.priorityNumLBL  =  Label( root , text = "Priority #" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.priorityNumLBL.place(x = 690, y = 160)
        self.basicWidgetList.append( self.priorityNumLBL )

        self.priorityNum1ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.priorityNum1ENTRY.place(x = 665, y = 210)
        self.basicWidgetList.append( self.priorityNum1ENTRY )
        
        self.priorityNum2ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.priorityNum2ENTRY.place(x = 665, y = 260)
        self.basicWidgetList.append( self.priorityNum2ENTRY )
        
        self.priorityNum3ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.priorityNum3ENTRY.place(x = 665, y = 310)
        self.basicWidgetList.append( self.priorityNum3ENTRY )

        self.priorityNum4ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.priorityNum4ENTRY.place(x = 665, y = 360)
        self.basicWidgetList.append( self.priorityNum4ENTRY )
        
        self.priorityNum5ENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.priorityNum5ENTRY.place(x = 665, y = 410)
        self.basicWidgetList.append( self.priorityNum5ENTRY )
        
        self.computeBTN  =  Button ( root , text = 'Compute',command = self.input1_computeBTN_Pressed , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.computeBTN.place (x = 390 ,y = 470)
        self.basicWidgetList.append( self.computeBTN )

        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 520)
        self.basicWidgetList.append( self.exitBTN )


    # Once the user wants to proceed with the computation, this function will be executed.
    def input1_computeBTN_Pressed( self ):
        #print( "input1_computeBTN_Pressed" )
        if messagebox.askyesno( "Confirmation..." , " Are you sure you want to compute? " ) == True :
            self.arrivalTime1 = self.arrivalTime1ENTRY.get()
            self.arrivalTime2 = self.arrivalTime2ENTRY.get()
            self.arrivalTime3 = self.arrivalTime3ENTRY.get()
            self.arrivalTime4 = self.arrivalTime4ENTRY.get()
            self.arrivalTime5 = self.arrivalTime5ENTRY.get()
            self.arrivalTime_list = [ self.arrivalTime1,
                                      self.arrivalTime2,
                                      self.arrivalTime3,
                                      self.arrivalTime4,
                                      self.arrivalTime5 ]

            self.arrivalError = False
            self.arrivalTests = [ self.isNotInteger( self.arrivalTime1 ),
                                  self.isNotInteger( self.arrivalTime2 ),
                                  self.isNotInteger( self.arrivalTime3 ),
                                  self.isNotInteger( self.arrivalTime4 ),
                                  self.isNotInteger( self.arrivalTime5 ) ]
            for i in range( len( self.arrivalTests ) ):
                if self.arrivalTests[i] == True:
                    if self.arrivalTime_list[i] == "x":
                        pass
                    else:
                        self.arrivalError = True
                        break

            self.priorityNum1 = self.priorityNum1ENTRY.get()
            self.priorityNum2 = self.priorityNum2ENTRY.get()
            self.priorityNum3 = self.priorityNum3ENTRY.get()
            self.priorityNum4 = self.priorityNum4ENTRY.get()
            self.priorityNum5 = self.priorityNum5ENTRY.get()
            self.priorityNum_list = [ self.priorityNum1,
                                      self.priorityNum2,
                                      self.priorityNum3,
                                      self.priorityNum4,
                                      self.priorityNum5 ]

            self.priorityError = False
            self.priorityTests = [ self.isNotInteger( self.priorityNum1 ),
                                  self.isNotInteger( self.priorityNum2 ),
                                  self.isNotInteger( self.priorityNum3 ),
                                  self.isNotInteger( self.priorityNum4 ),
                                  self.isNotInteger( self.priorityNum5 ) ]
            
            # process details [ processNum, priorityNum, arrivalTime ]
            self.processDetails = {}
            for i in range( len( self.priorityTests ) ):
                if self.priorityTests[i] == True:
                    if self.priorityNum_list[i] == "x":
                        pass
                    else:
                        self.priorityError = True
                        break
                    if self.priorityNum_list[i] != "x":
                        self.count = self.priorityNum_list.count( self.priorityNum_list[i] )
                        if self.count > 1:
                            print( "tick", self.priorityNum_list[i], self.count )
                            self.priorityError = True
                            break

            self.burstTime1 = self.burstTime1ENTRY.get()
            self.burstTime2 = self.burstTime2ENTRY.get()
            self.burstTime3 = self.burstTime3ENTRY.get()
            self.burstTime4 = self.burstTime4ENTRY.get()
            self.burstTime5 = self.burstTime5ENTRY.get()
            self.burstTime_list = [ self.burstTime1,
                                      self.burstTime2,
                                      self.burstTime3,
                                      self.burstTime4,
                                      self.burstTime5 ]

            self.burstError = False
            self.burstTests = [ self.isNotInteger( self.burstTime1 ),
                                  self.isNotInteger( self.burstTime2 ),
                                  self.isNotInteger( self.burstTime3 ),
                                  self.isNotInteger( self.burstTime4 ),
                                  self.isNotInteger( self.burstTime5 ) ]
            
            # process details [ processNum, burstTime, arrivalTime ]
            self.processDetails = {}
            for i in range( len( self.burstTests ) ):
                if self.burstTests[i] == True:
                    if self.burstTime_list[i] == "x":
                        pass
                    else:
                        self.burstError = True
                        break
                else:
                    self.processDetails[i+1] = [ "P{}".format( i+1 ),
                                                 int( self.burstTime_list[i] ),
                                                 int( self.arrivalTime_list[i]),
                                                 int( self.priorityNum_list[i]) ]


            

            
            if self.burstError == True:
                #print ( "Error: Invalid Burst Time input." )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Burst Time input" )
            elif self.arrivalError == True:
                #print ( " Error: Invalid Arrival Time input." )
                messagebox.showinfo( "Compute Error" , "Invalid Arrival Time input." )
            elif self.priorityError == True:
                messagebox.showinfo( "Compute Error" , "Invalid Priority input." )
            else:
                self.backEnd.insert_inputs( self.processDetails )
                self.backEnd.generate_ganttChart()
                self.ganttChart = self.backEnd.get_ganttChart()
                self.caa = self.backEnd.get_caa()
                #print ( "compute finish" )
                #print( self.ganttChart )
                #print( self.caa )
                self.result1_window()

    # This function contains and displays the result data.
    # Result includes:
    #           Gantt Chart
    #           CPU Utilization
    #           ATA
    #           AWT
    def result1_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.pLBL = Label ( root , image = p_bg, bg = "black" )
        self.pLBL.place(x = 0, y = 0)
        self.basicWidgetList.append( self.pLBL )
        
        self.clockLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#4ec2c2" )
        self.clockLBL.place(x = 700, y = 70)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append( self.clockLBL )

        self.dateLBL  =  Label( root , font = ('Times New Roman', 17),  bg = "#4ec2c2")
        self.dateLBL.place(x = 650, y = 25)
        self.current_date()
        self.basicWidgetList.append( self.dateLBL )

        self.title1LBL  =  Label( root , text = "Priority" , font = ('Times New Roman', 20),  bg = "#4ec2c2")
        self.title1LBL.place(x = 150, y = 20)
        self.basicWidgetList.append( self.title1LBL )
        self.title2LBL  =  Label( root , text = "Process Management" , font = ('Times New Roman', 20),  bg = "#4ec2c2")
        self.title2LBL.place(x = 75, y = 65)
        self.basicWidgetList.append( self.title2LBL )

        self.title3LBL  =  Label( root , text = "Gantt Chart" , font = ('Times New Roman', 20),  bg = "#c6e3ad")
        self.title3LBL.place(x = 410, y = 160)
        self.basicWidgetList.append( self.title3LBL )
        
        self.physicalMemWidgets = []
        self.xCounter = 210
        self.indexPointer = 0
        
        self.markLBL  =  Label( root , text = 0 , font = ('Times New Roman', 10),  bg = "#c6e3ad")
        self.markLBL.place(x = self.xCounter - 5, y = 310)
        self.physicalMemWidgets.append( self.markLBL )

        self.tempTotalSize = 0
        for tempData in self.ganttChart:
            print( "tempData",  tempData )
            try:
                self.tempTotalSize += tempData[4]
                self.displayChart( tempData[6], tempData[5], tempData[2], tempData[6], self.tempTotalSize )
            except:
                pass

        self.cpuUtilizationLBL  =  Label( root , text = " CPU Utilization" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.cpuUtilizationLBL.place(x = 400, y = 360)
        self.basicWidgetList.append( self.cpuUtilizationLBL )

        self.cpuUtilizationENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.cpuUtilizationENTRY.place(x = 400, y = 405)
        self.cpuUtilizationENTRY.insert( 0, str( round(self.caa[0],2)) + "%" )
        self.cpuUtilizationENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.cpuUtilizationENTRY )

        self.ataLBL  =  Label( root , text = " ATA" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.ataLBL.place(x = 280, y = 360)
        self.basicWidgetList.append( self.ataLBL )

        self.ataENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.ataENTRY.place(x = 235, y = 405)
        self.ataENTRY.insert( 0, str(self.caa[1]) )
        self.ataENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.ataENTRY )

        self.awtLBL  =  Label( root , text = " AWT" , font = ('Times New Roman', 15),  bg = "#c6e3ad")
        self.awtLBL.place(x = 602, y = 360)
        self.basicWidgetList.append( self.awtLBL )

        self.awtENTRY = Entry( root , font = ('Poppins', 10, 'bold'), justify= "center" )
        self.awtENTRY.place(x = 565, y = 405)
        self.awtENTRY.insert( 0, str(self.caa[2]) )
        self.awtENTRY.config( state = "readonly" )
        self.basicWidgetList.append( self.awtENTRY )


        self.backBTN  =  Button ( root , text = 'BACK',command = self.input1_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 300 ,y = 480)
        self.basicWidgetList.append( self.backBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 490 ,y = 480)
        self.basicWidgetList.append( self.exitBTN )

# END OF PRIORITY PROGRAM

main = main()
scmm_program = singleContiguousProgram()
spa_program = staticPartitionedAllocation()
dff_program = dynamic_firstFit_frontEnd()
dbf_program = dynamic_bestFit_frontEnd()
fcfs_program = fcfs_frontEnd()
sjf_program = sjf_frontEnd()
srtf_program = srtf_frontEnd()
rr_program = rRobin_frontEnd()
p_program = pty_frontEnd()

main.mainMenu_window()
#main.aboutUs_window()
root.mainloop()

