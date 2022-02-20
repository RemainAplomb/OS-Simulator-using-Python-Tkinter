"""
    Group Members:
        - Abaño, Ian Joshua
        - Conti, Ronjay
        - Dibansa, Rahmani
        - Palattao, Larry Simoun
        
    Program Description:
        - This is a program which mimics and represents the Dynamic Best Fit Partitioned Allocation.

    Program Algorithm:
        1. Initialize the program and create the tkinter GUI
        2. Ask for user input in input1_window of dynamic_bestFit_frontEnd.
        3. Once user has successfully entered an acceptable input, send the user's input to the backEnd class.
        4. Use the backEnd class to generate the summary table.
        5. Use the summaryTable_window of the frontEnd class to display the results.
        6. Create the linked linked list containing the the memory map, fat, and pat if the user clicked nextBTN of summaryTable_window.
        7. Traverse the linked list to display the certain time's memory map, fat, and pat.
        8. Terminate program if exit button is pressed.

    General Program Flow:
        input1_window -> summaryTable_window -> linked list head -> nextPointer of certain node -> ... -> input1_window( if user wants to try with new inputs )

    dynamic_bestFit_backEnd:
        print_data: for printing data
        insert_inputs: for taking in the user's input into the backEnd class.
        get_memory: returns the memory list
        get_summaryTable: returns the summary table
        get_memoryResults: returns memory results
        get_memoryResults_time: returns memory result's time.
        add_memoryResult: for appending a certain memory list into the memory result
        arrange_allTime: sorts the list containing all the time that needs a memory result.
        remove_time: remove's the time that already have a memory result.
        check_jobFit: checks if the job fits into the available partitions.
        check_jobStatus: checks a certain job's status.
        allocate: for allocating a job into the memory list.
        recycle: for de-allocating a job out of the memory list.
        generate_summaryTable: for generating the summary table.
        

    dynamic_bestFit_frontEnd:
        clearNodes: for clearing the linked list which contains the windows for memory map, fat, and pat.
        addResultNode: for adding a node into the linked list
        current_date: sets the current time into the date label.
        tick: for updating the clock label.
        isNotTimeFormat: This function returns True if timeInput is not in proper time format
        isNotInteger: This function returns True if the integerInput is not an Integer.
        clearWidgets: tries to clear/destroy all of the widgets.
        clearWidgetList: destroys a certain group of widgets.
        displayMap: This function displays the necessary widgets for physical memory map.
        input1_window: the window which takes in the user's input.
        input1_computeBTN_Pressed: executes once the user clicks the compute button.
        summaryTable_window: the window which displays the summary table.
        summaryTable_nextBTN_Pressed: this executes once the user wants to view the memory maps, fats, and pats.

    dynamic_bestFitNode_frontEnd:
        clearNodes: for clearing the linked list which contains the windows for memory map, fat, and pat.
        addResultNode: for adding a node into the linked list
        current_date: sets the current time into the date label.
        tick: for updating the clock label.
        memMap_window: the window which displays a certain time's memory map.
        memMap_backBTN_Pressed: this execute once the user clicked the back button in the memory map window.
        pat_window: the window which displays a certain time's partitioned allocation table.
        fat_window: the window which displays a certain time's FAT.
        fat_nextBTN_Pressed: this execute once the user clicked the next button in the fat window.
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

# For the backend
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
root.title ( "Dynamic Best Fit" )
#

# Resources
#   -> Background
bg4 = PhotoImage(file = currentDirectory + "\\resources\\background\\bg4.png" )
# *End of resources code block


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

    # for printing data
    def print_data( self ):
        for x in self.memoryResults:
            print ( x )
        for x in self.memoryResults_time:
            print ( x[0].time(), x[1] )
        for x in list( self.summaryTable ):
            print( self.summaryTable[x][0], self.summaryTable[x][1].time(), self.summaryTable[x][2].time(), self.summaryTable[x][3] )
        return

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
                    self.jobStatus[job[1]][0] = True # Status which indicates that the job is being processed

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
                    self.jobStatus[job[1]][1] = True # Status which indicates that the job has been processed.
                    
                    self.actionTaken = True
                    self.tempTimeStatus.append( "Terminated(J{})".format( job[1] ) )
                else:
                    pass
            #print( self.currentTime, self.memory )

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
        # a miscellaneous command used for debugging. 
        #self.print_data()


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


    # function which contains widget placements
    # this also takes in the user's input.
    def input1_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.bg4LBL = Label ( root , image = bg4, bg = "black" )
        self.bg4LBL.place(x = 0, y = 0)
        self.basicWidgetList.append( self.bg4LBL )
        
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
            # If not, print the errors.
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
        
        self.bg4LBL = Label ( root , image = bg4, bg = "black" )
        self.bg4LBL.place(x = 0, y = 0)
        self.basicWidgetList.append( self.bg4LBL )
        
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
                    self.memMap_data.append( [ self.tempPercentage, self.tempColors[self.tempColorCounter], "Available(F{})".format(self.availableCounter), self.tempPercentage, self.location - 1, certainResult[0] - 1 ])
                else:
                    self.fatData.append( [ certainResult[0], self.location, "Available" ] )
                    self.location += int(certainResult[0])
                    #print ( "Available Counter: ", self.availableCounter )
                    self.tempPercentage = float(( float(certainResult[0]) / float(self.memSize) ) * 100 )
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

        #print( self.memMap_data )
        #print( self.fatData )

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
        
        self.bg4LBL = Label ( root , image = bg4, bg = "black" )
        self.bg4LBL.place(x = 0, y = 0)
        self.basicWidgetList.append( self.bg4LBL )
        
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
            frontEnd.summaryTable_window()

    def pat_window( self ):
        self.clearWidgets()
        self.basicWidgetList = []
        
        self.bg4LBL = Label ( root , image = bg4, bg = "black" )
        self.bg4LBL.place(x = 0, y = 0)
        self.basicWidgetList.append( self.bg4LBL )
        
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
        
        self.bg4LBL = Label ( root , image = bg4, bg = "black" )
        self.bg4LBL.place(x = 0, y = 0)
        self.basicWidgetList.append( self.bg4LBL )
        
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
            frontEnd.input1_window()
        else:
            self.nextPointer.memMap_window()

                    
# The Graphical User Interface's activation.
root.resizable( width = FALSE , height = FALSE )
root.geometry( "900x600" )
root.config ( background = "LIGHTBLUE" )

frontEnd = dynamic_bestFit_frontEnd()
frontEnd.input1_window()
root.mainloop()

