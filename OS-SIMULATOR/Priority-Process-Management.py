"""
    Group Members:
        - Abaño, Ian Joshua
        - Conti, Ronjay
        - Dibansa, Rahmani
        - Palattao, Larry Simoun
        
    Program Description:
        - This is a program which mimics and represents the Priority Process Management.

    Program Algorithm:
        1. Initialize the program and create the tkinter GUI
        2. Ask for user input in input1_window of pty_frontEnd.
        3. Once user has successfully entered an acceptable input, send the user's input to the backEnd class.
        4. Use the backEnd class to generate the data for gantt chart. In addition, compute for ATA, AWT, and CPU Utilization.
        5. Use the ganttChart_window of the frontEnd class to display the results.
        6. Terminate program if exit button is pressed.

    General Program Flow:
        input1_window -> generate gantt chart using backEnd class -> display results

    pty_backEnd:
        insert_inputs: for taking in the user's input into the backEnd class.
        get_ganttChart: returns the list containing the data for gantt chart.
        get_caa: returns the list containing CPU Utilization, ATA, AWT.
        generate_ganttChart: for generating the data for gantt chart.
        

    pty_frontEnd:
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
    print ( " Error : Cannot find the Current Directory. " )
# end of getting current directory


# creating the tkinter root that will accommodate the UI
root = Tk()
root.title ( "Priority Process Management" )
#

# Resources
#   -> Background
bg9 = PhotoImage(file = currentDirectory + "\\resources\\background\\bg9.png" )
# *End of resources code block


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
        
        self.bg9LBL = Label ( root , image = bg9, bg = "black" )
        self.bg9LBL.place(x = 0, y = 0)
        self.basicWidgetList.append( self.bg9LBL )
        
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
                messagebox.showinfo( "Compute Error" , "Error: Invalid Burst Time input" )
            elif self.arrivalError == True:
                messagebox.showinfo( "Compute Error" , "Invalid Arrival Time input." )
            elif self.priorityError == True:
                messagebox.showinfo( "Compute Error" , "Invalid Priority input." )
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
        
        self.bg9LBL = Label ( root , image = bg9, bg = "black" )
        self.bg9LBL.place(x = 0, y = 0)
        self.basicWidgetList.append( self.bg9LBL )
        
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

# The Graphical User Interface's activation.
root.resizable( width = FALSE , height = FALSE )
root.geometry( "900x600" )
root.config ( background = "LIGHTBLUE" )

#program = pty_backEnd()
#program.generate_ganttChart()

program1 = pty_frontEnd()
#program1.result1_window()
program1.input1_window()
root.mainloop()



            
