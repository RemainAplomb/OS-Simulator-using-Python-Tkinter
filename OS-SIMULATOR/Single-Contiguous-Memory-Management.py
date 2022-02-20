"""
    Group Members:
        - Abaño, Ian Joshua
        - Conti, Ronjay
        - Dibansa, Rahmani
        - Palattao, Larry Simoun
        
    Program Description:
        - This is a program which mimics and represents the Single Contgiguous Memory Management.

    Program Algorithm:
        1. Initialize the program and create the tkinter GUI
        2. In the function mainInput1_window, ask for the user's input and proceed to step 3 once input is taken.
        3. In the function mainInput1_computeBTN_Pressed, solve for every job's needed variables.
        4. In the function mainResult1_window, display the computed startTime, finishTime, and cpuWait.
        5. In the function mainResult2_window, display the physical memory map of the job 1's startTime.
        6. In the function mainResult3_window, display the physical memory map of the job 2's startTime.
        7. In the function mainResult4_window, display the physical memory map of the job 3's startTime.
        8. In the function mainResult5_window, display the physical memory map of the job 4's startTime.
        9. In the function mainResult6_window, display the physical memory map of the job 5's startTime.
        10. Terminate program if exit button is pressed.

    General Program Flow:
        mainInput1_window -> mainInput1_computeBTN_Pressed -> mainResult1_window -> mainResult2_window
        mainResult2_window -> mainResult3_window -> mainResult4_window -> mainResult5_window -> mainResult6_window

    Miscellaneous Functions of mainUI class:
        - current_date: This function takes the current date
        - tick: This function updates the time widget
        - isNotTimeFormat: This function returns True if the input is not in time format ( Time format: HH:MM )
        - isNotInteger: This function returns True if the input is not an Integer
        - clearWidgets: This function clears all the widgets( self.basicWidgetList and self.physicalMemWidgets )
        - clearWidgetList: This function clears the inputted widget list
        - displayMap: This function is used to display the physical memory map
        - mainInput1_computeBTN_Pressed: This function is for all the necessary computations

    Window Functions of mainUI class:
        - mainInput1_window: For taking user's input
        - mainResult1_window: For displaying the summary table
        - mainResult2_window: For displaying physical memory map of job 1's start time.
        - mainResult3_window: For displaying physical memory map of job 2's start time.
        - mainResult4_window: For displaying physical memory map of job 3's start time.
        - mainResult5_window: For displaying physical memory map of job 4's start time.
        - mainResult6_window: For displaying physical memory map of job 5's start time.
        
"""


# importing modules
from tkinter import*
from tkinter import ttk
from array import*
from tkinter import messagebox
import csv
import math
import sys
import time
import datetime
import os

from PIL import Image, ImageTk

global listbox
# end of module importing


# getting current directory of the app
try:
    currentDirectory = os.getcwd()
    ###Started(currentDirectory)
except:
    print ( " Error : Cannot find the Current Directory. " )
# end of getting current directory


# creating the tkinter root that will accommodate the UI
root = Tk()
root.title ( "Single Contiguous Memory Management" )
#


# Resources
#   -> Background
bg1 = PhotoImage(file = currentDirectory + "\\resources\\background\\bg1.png" )
# *End of resources code block


# mainUI class which contains most of all the program's code.
# This contains all the window functions and miscellaneous functions
# To know each function's description, look at the documentation at the first line. ( *Ctrl + h* line 27 and 37 )
class mainUI:
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
                print ( "Error: Invalid Memory or OS Size input." )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Memory or OS Size input." )
            elif int(self.memSize) < int(self.osSize):
                print ( " Error: Os Size can't exceed Memory Size. " )
                messagebox.showinfo( "Compute Error" , "Error: Os Size can't exceed Memory Size." )
            elif self.size1_Check or self.size2_Check or self.size3_Check or self.size4_Check or self.size5_Check:
                print ( "Error: Size input detected as not an integer." )
                messagebox.showinfo( "Compute Error" , "Error: Size input detected as not an integer." )
            elif (int(self.size1) > ( int(self.memSize) - int(self.osSize))) or (int(self.size2) > ( int(self.memSize) - int(self.osSize))) or (int(self.size3) > ( int(self.memSize) - int(self.osSize))) or (int(self.size4) > ( int(self.memSize) - int(self.osSize))) or (int(self.size5) > ( int(self.memSize) - int(self.osSize))):
                print ( "Error: Size input should not exceed ( Memory Size - OS Size )." )
                messagebox.showinfo( "Compute Error" , "Error: Size input should not exceed ( Memory Size - OS Size )." )
            elif self.arrivalTime1_Check or self.arrivalTime2_Check or self.arrivalTime3_Check or self.arrivalTime4_Check or self.arrivalTime5_Check:
                print ( " Error in arrival time input " )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Arrival Time Input." )
            elif self.runTime1_Check or self.runTime2_Check or self.runTime3_Check or self.runTime4_Check or self.runTime5_Check:
                print ( "Error: Invalid Run Time Input." )
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
                self.mainResult1_window()
   

    # From here, and down to the last function are the windows/pages of the GUI.
    def mainInput1_window ( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.bg1LBL = Label ( root , image = bg1, bg = "black" )
        self.bg1LBL.place(x = 0, y = 0)
        self.basicWidgetList.append( self.bg1LBL )
        
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

        
    def mainResult1_window ( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.bg1LBL = Label ( root , image = bg1, bg = "black" )
        self.bg1LBL.place(x = 0, y = 0)
        self.basicWidgetList.append( self.bg1LBL )
        
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

        self.backBTN  =  Button ( root , text = 'BACK',command = self.mainInput1_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 300 ,y = 500)
        self.basicWidgetList.append( self.backBTN )
        
        self.nextBTN  =  Button ( root , text = 'NEXT',command = self.mainResult2_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.nextBTN.place (x = 480 ,y = 500)
        self.basicWidgetList.append( self.nextBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 550)
        self.basicWidgetList.append( self.exitBTN )


    def mainResult2_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.bg1LBL = Label ( root , image = bg1, bg = "black" )
        self.bg1LBL.place(x = 0, y = 0)
        self.basicWidgetList.append( self.bg1LBL )
        
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
        
        self.backBTN  =  Button ( root , text = 'BACK',command = self.mainResult1_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 200 ,y = 530)
        self.basicWidgetList.append( self.backBTN )
        self.nextBTN  =  Button ( root , text = 'NEXT',command = self.mainResult3_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.nextBTN.place (x = 580 ,y = 530)
        self.basicWidgetList.append( self.nextBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 530)
        self.basicWidgetList.append( self.exitBTN )

    def mainResult3_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.bg1LBL = Label ( root , image = bg1, bg = "black" )
        self.bg1LBL.place(x = 0, y = 0)
        self.basicWidgetList.append( self.bg1LBL )
        
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
        
        self.backBTN  =  Button ( root , text = 'BACK',command = self.mainResult2_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 200 ,y = 530)
        self.basicWidgetList.append( self.backBTN )
        self.nextBTN  =  Button ( root , text = 'NEXT',command = self.mainResult4_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.nextBTN.place (x = 580 ,y = 530)
        self.basicWidgetList.append( self.nextBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 530)
        self.basicWidgetList.append( self.exitBTN )


    def mainResult4_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.bg1LBL = Label ( root , image = bg1, bg = "black" )
        self.bg1LBL.place(x = 0, y = 0)
        self.basicWidgetList.append( self.bg1LBL )
        
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
        
        self.backBTN  =  Button ( root , text = 'BACK',command = self.mainResult3_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 200 ,y = 530)
        self.basicWidgetList.append( self.backBTN )
        self.nextBTN  =  Button ( root , text = 'NEXT',command = self.mainResult5_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.nextBTN.place (x = 580 ,y = 530)
        self.basicWidgetList.append( self.nextBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 530)
        self.basicWidgetList.append( self.exitBTN )


    def mainResult5_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.bg1LBL = Label ( root , image = bg1, bg = "black" )
        self.bg1LBL.place(x = 0, y = 0)
        self.basicWidgetList.append( self.bg1LBL )
        
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
        
        self.backBTN  =  Button ( root , text = 'BACK',command = self.mainResult4_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 200 ,y = 530)
        self.basicWidgetList.append( self.backBTN )
        self.nextBTN  =  Button ( root , text = 'NEXT',command = self.mainResult6_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.nextBTN.place (x = 580 ,y = 530)
        self.basicWidgetList.append( self.nextBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 530)
        self.basicWidgetList.append( self.exitBTN )


    def mainResult6_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.bg1LBL = Label ( root , image = bg1, bg = "black" )
        self.bg1LBL.place(x = 0, y = 0)
        self.basicWidgetList.append( self.bg1LBL )
        
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
        
        self.backBTN  =  Button ( root , text = 'BACK',command = self.mainResult5_window , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.backBTN.place (x = 200 ,y = 530)
        self.basicWidgetList.append( self.backBTN )
        self.nextBTN  =  Button ( root , text = 'TRY NEW INPUT',command = self.mainInput1_window , font = ('Poppins', 16, 'bold'), width  =  14, bg = "#659bdb" )
        self.nextBTN.place (x = 580 ,y = 530)
        self.basicWidgetList.append( self.nextBTN )
        
        self.exitBTN  =  Button ( root , text = 'Exit',command = root.destroy , font = ('Poppins', 16, 'bold'), width  =  12, bg = "#659bdb" )
        self.exitBTN.place (x = 390 ,y = 530)
        self.basicWidgetList.append( self.exitBTN )
    

# The Graphical User Interface's activation.
root.resizable( width = FALSE , height = FALSE )
root.geometry( "900x600" )
root.config ( background = "LIGHTBLUE" )

# Initialize the class mainUI into programStart variable.
# Display the first window of the program ( mainInput1_window )
programStart = mainUI()
programStart.mainInput1_window()
root.mainloop()

    
    
