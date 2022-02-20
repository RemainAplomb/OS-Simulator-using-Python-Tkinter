"""
    Group Members:
        - Abaño, Ian Joshua
        - Conti, Ronjay
        - Dibansa, Rahmani
        - Palattao, Larry Simoun
        
    Program Description:
        - This is a program which mimics and represents the Shortest Job First.

    Program Algorithm:
        1. Initialize the program and create the tkinter GUI
        2. Ask for user input in input1_window of sjf_frontEnd.
        3. Once user has successfully entered an acceptable input, send the user's input to the backEnd class.
        4. Use the backEnd class to generate the data for gantt chart. In addition, compute for ATA, AWT, and CPU Utilization.
        5. Use the ganttChart_window of the frontEnd class to display the results.
        6. Terminate program if exit button is pressed.

    General Program Flow:
        input1_window -> generate gantt chart using backEnd class -> display results

    sjf_backEnd:
        insert_inputs: for taking in the user's input into the backEnd class.
        get_ganttChart: returns the list containing the data for gantt chart.
        get_caa: returns the list containing CPU Utilization, ATA, AWT.
        generate_ganttChart: for generating the data for gantt chart.
        

    sjf_frontEnd:
        clearNodes: for clearing the linked list which contains the windows for memory map, fat, and pat.
        addResultNode: for adding a node into the linked list
        current_date: sets the current time into the date label.
        tick: for updating the clock label.
        isNotInteger: This function returns True if the integerInput is not an Integer.
        clearWidgets: tries to clear/destroy all of the widgets.
        clearWidgetList: destroys a certain group of widgets.
        displayChart: This function displays the necessary widgets for gantt chart.
        input1_window: the window which takes in the user's input.
        input1_computeBTN_Pressed: executes once the user clicks the compute button.
        result1_window: the window which displays the gantt chart.
"""

# importing modules
from tkinter import*
from tkinter import ttk
from array import*
from tkinter import messagebox
import csv
import math
import sys
import os

from PIL import Image, ImageTk

global listbox
# end of module importing

# For the backEnd
import datetime
import time
from copy import deepcopy

# getting current directory of the app
try:
    currentDirectory = os.getcwd()
    ###Started(currentDirectory)
except:
    pass
    #print ( " Error : Cannot find the Current Directory. " )
# end of getting current directory


# creating the tkinter root that will accommodate the UI
root = Tk()
root.title ( "Shortest Job First Process Management" )
#

# Resources
#   -> Background
bg6 = PhotoImage(file = currentDirectory + "\\resources\\background\\bg6.png" )
# *End of resources code block


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
                self.isFinished = True
                break
            self.finishTime = self.currentProcess[1] + self.currentProcess[2]
            self.waitingProcess = []
            for i in range( len( self.tempProcess_queue )):
                if self.finishTime >= self.tempProcess_queue[i][2]:
                    self.waitingProcess.append( [ i, self.tempProcess_queue[i][1] ] )
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
                    self.isFinished = True
                    break

        self.process_queue = deepcopy( self.tempResult_queue )

        # sort the process queue by the level of priority
        #self.process_queue = sorted( self.process_queue, key=lambda x: (x[2], x[3]) )
        #print( "process queue 3", self.process_queue )

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
                try:
                    self.ganttChart.append( [self.completionTime,self.process_queue[i][2], "Idle",self.completionTime , self.process_queue[i][2] - self.completionTime, "#bfbaac"] )
                except:
                    pass
                self.idleTime += (self.process_queue[i][2] - self.completionTime)
                self.completionTime = self.process_queue[i][2]
            self.ata += float((self.completionTime + self.process_queue[i][1]) - self.process_queue[i][2] )
            self.awt += float((self.completionTime) - self.process_queue[i][2] )

            # append the computations/data for a certain process in the process queue.
            try:
                self.ganttChart.append( [self.completionTime, self.completionTime + self.process_queue[i][1], self.process_queue[i][0], self.process_queue[i][2], self.process_queue[i][1], self.tempColors[self.tempColorsCounter]] )
            except:
                pass
            self.completionTime += self.process_queue[i][1]
            self.tempColorsCounter += 1

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
        for i in range( int( self.tempPercentage/2 ) ):
            if self.tempPointer != 0:
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

    # This is the input window that will take in the user's inputs.
    def input1_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.bg6LBL = Label ( root , image = bg6, bg = "black" )
        self.bg6LBL.place(x = 0, y = 0)
        self.basicWidgetList.append( self.bg6LBL )
        
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
                #print ( "Error: Invalid Burst Time input." )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Burst Time input" )
            elif self.arrivalError == True:
                #print ( " Error: Invalid Arrival Time input." )
                messagebox.showinfo( "Compute Error" , "Invalid Arrival Time input." )
            else:
                self.backEnd.insert_inputs( self.processDetails )
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
        
        self.bg6LBL = Label ( root , image = bg6, bg = "black" )
        self.bg6LBL.place(x = 0, y = 0)
        self.basicWidgetList.append( self.bg6LBL )
        
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

# The Graphical User Interface's activation.
root.resizable( width = FALSE , height = FALSE )
root.geometry( "900x600" )
root.config ( background = "LIGHTBLUE" )


program1 = sjf_frontEnd()
program1.input1_window()
root.mainloop()

            
