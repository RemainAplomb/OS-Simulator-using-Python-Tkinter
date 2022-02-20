"""
    Group Members:
        - Abaño, Ian Joshua
        - Conti, Ronjay
        - Dibansa, Rahmani
        - Palattao, Larry Simoun
        
    Program Description:
        - This is a program which mimics and represents the Static Partitioned Memory Allocation

    Program Algorithm:
        1. Initialize the program and create the tkinter GUI
        2. In the function mainInput1_window, ask for the user's input of partition and proceed to step 3 once input is taken.
        3. In the function mainInput2_window, ask for the user's input of the job's information and proceed to step 4 once input is taken.
        4. In the function mainInput2_computeBTN_Pressed, solve for every job's needed variables.
        5. In the function createResultWindows, generate the result windows using the help of the Node class.
        6. In the function mainResult1_window, display the summary table.
        7. Use the linked list of result window nodes to display every all the necessary physical memory maps and PAT.
        8. Terminate program if exit button is pressed.

    General Program Flow:
        mainInput1_window -> mainInput2_window -> mainInput2_computeBTN -> createResultWindows
        mainResult1 -> windows of the linked list of result window nodes.

    BackEnd Functions of mainUI class:
        - current_date: This function takes the current date
        - tick: This function updates the time widget
        - isNotTimeFormat: This function returns True if the input is not in time format ( Time format: HH:MM )
        - isNotInteger: This function returns True if the input is not an Integer
        - clearWidgets: This function clears all the widgets( basicWidgetList and self.physicalMemWidgets )
        - clearWidgetList: This function clears the inputted widget list
        - displayMap: This function is used to display the physical memory map
        - mainInput2_computeBTN_Pressed: This function is for most of the necessary computations
        - createResultWindows: Generates the result windows using the help of the Node class.

    FrontEnd Functions of mainUI class:
        - mainInput1_window: For taking user's input of partitions
        - mainInput2_window: For taking user's input of each job's information
        - mainResult1_window: For displaying the summary table

    BackEnd Functions of Node class:
        - current_date: This function takes the current date
        - tick: This function updates the time widget
        - clearWidgets: This function clears all the widgets( basicWidgetList and self.physicalMemWidgets )
        - clearWidgetList: This function clears the inputted widget list
        - displayMap: This function is used to display the physical memory map
        - memMap_backBTN_Pressed: This function points which window to go back on.
        - pat_nextBTN_Pressed: This function points which window to go next.

    FrontEnd Functions of Node class:
        - memMap_window: For displaying the physical memory map
        - pat_window: For displaying the partition allocation table.
        
"""


#importing modules
from tkinter import*
from tkinter import ttk
#from array import*
from tkinter import messagebox
#import csv
#import math
import sys
import time
import datetime
import os

from PIL import Image, ImageTk

#global listbox
# end of module importing


# getting current directory of the app
try:
    currentDirectory = os.getcwd()
except:
    print ( " Error : Cannot find the Current Directory. " )
# end of getting current directory


# creating the tkinter root that will accommodate the UI
root = Tk()
root.title ( "Static First Fit Partitioned Allocation" )
#

# Resources
#   -> Background
bg2 = PhotoImage(file = currentDirectory + "\\resources\\background\\bg2.png" )
# */ End of Resouces code block


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
            mainUI.mainResult1_window()
        else:
            self.backPointer.pat_window()


    # For displaying the physical memory map
    def memMap_window( self ):
        self.clearWidgets()
        basicWidgetList = []
        self.nextAvailable = True
        
        self.bg2LBL = Label ( root , image = bg2, bg = "black" )
        self.bg2LBL.place(x = 0, y = 0)
        basicWidgetList.append( self.bg2LBL )
        
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
            mainUI.mainInput1_window()
        else:
            self.nextPointer.memMap_window()


    # For displaying the partition allocation table.
    def pat_window( self ):
        self.clearWidgets()
        basicWidgetList = []
        
        self.bg2LBL = Label ( root , image = bg2, bg = "black" )
        self.bg2LBL.place(x = 0, y = 0)
        basicWidgetList.append( self.bg2LBL )
        
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


class mainUI:
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
            self.tempJob = int(tempJob)
            self.tempResult = True
            for i in range( len( partitionSizes) ):
                if int(partitionSizes[i]) >= self.tempJob:
                    self.tempResult = False
                    break
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
                print ( "Error: Invalid Memory or OS Size input." )
                messagebox.showinfo( "Partition Error" , "Error: Invalid Memory or OS Size input." )
            elif int(memSize) < int(osSize):
                print ( " Error: Os Size can't exceed Memory Size. " )
                messagebox.showinfo( "Partition Error" , "Error: Os Size can't exceed Memory Size." )
            elif self.partition1_Check or self.partition2_Check or self.partition3_Check or self.partition4_Check or self.partition5_Check:
                print ( "Error: Partition Size input." )
                messagebox.showinfo( "Partition Error" , "Error: Partition Size input." )
            elif int(self.totalSize) > int(memSize):
                print ( "Error: Total taken size exceeded Memory Size." )
                messagebox.showinfo( "Partition Error" , "Error: Total taken size exceeded Memory Size." )
            elif int(self.totalSize) != int(memSize):
                print ( "Error: Total taken size must be equal to Memory Size." )
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

                partition1 = int(partition1)
                partition2 = int(partition2)
                partition3 = int(partition3)
                partition4 = int(partition4)
                partition5 = int(partition5)
                partitionSizes = [ partition1, partition2, partition3, partition4, partition5 ]
                messagebox.showinfo( "Partition Success" , "The partitions has been set." )


    # This function checks if the user is eligible to continue into the next window
    def mainInput1_nextBTN_Pressed ( self ):
        if messagebox.askyesno( "Confirmation..." , " Are you sure you want to move on? " ) == True :
            if self.nextAvailable == True:
                self.mainInput2_window()
            else:
                print ( "Error: Please make sure that you've correctly set the partition." )
                messagebox.showinfo( "Partition Error" , "Error: Please make sure that you've correctly set the partition." )

    # For taking user's input of partitions
    def mainInput1_window( self ):
        self.clearWidgets()
        basicWidgetList = []
        self.nextAvailable = True
        
        self.bg2LBL = Label ( root , image = bg2, bg = "black" )
        self.bg2LBL.place(x = 0, y = 0)
        basicWidgetList.append( self.bg2LBL )
        
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
        self.allJobArrivalTime = allJobArrivalTime
        self.allJobRunTime = allJobRunTime
        partitionSizes = allPartitionSizes
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
                    break

        for i in range( 5 ):
            if self.jobState[i] == False:
                for j in range( 5 ):
                    if int(partitionSizes[j]) >= int(jobSizes[i]):
                        self.partitionState[j] = True
                        self.jobState[i] = True

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

                        #self.allJobResults = [ [ startTime, finishTime, cpuWait, partitionLocation, job num, before/after ] ]
                        break

        # is_time_between(self, begin_time, end_time, check_time=None):

        # Bookmark
        for i in range( 5 ):
            self.tempCheckTime = self.allJobResults[i][0]
            self.tempCheckTime2 = self.allJobResults[i][1]
            for j in range( 5 ):
                self.tempBeginTime = self.allJobResults[j][0]
                self.tempEndTime = self.allJobResults[j][1]
                
                self.tempStatus = self.is_time_between( self.tempBeginTime, self.tempEndTime, self.tempCheckTime )
                self.tempStatus2 = self.is_time_between( self.tempBeginTime, self.tempEndTime, self.tempCheckTime2 )
                if self.tempStatus == True:
                    self.patStatus1[i][self.allJobResults[j][3]] = "Allocated(J{})".format(self.allJobResults[j][4] + 1)
                if self.tempStatus2 == True:
                    if self.tempCheckTime2 == self.tempEndTime:
                        pass
                    else:
                        self.patStatus2[i][self.allJobResults[j][3]] = "Allocated(J{})".format(self.allJobResults[j][4] + 1)
        """
        for x in self.allJobResults:
            for xx in x:
                print( xx )
        """


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
                print ( "Error: Size input detected as not an integer." )
                messagebox.showinfo( "Compute Error" , "Error: Size input detected as not an integer." )
            elif self.size1_Check2:
                print ( "Error: Size 1 input can't fit in any partition." )
                messagebox.showinfo( "Compute Error" , "Error: Size 1 input can't fit in any partition." )
            elif self.size2_Check2:
                print ( "Error: Size 2 input can't fit in any partition." )
                messagebox.showinfo( "Compute Error" , "Error: Size 2 input can't fit in any partition." )
            elif self.size3_Check2:
                print ( "Error: Size 3 input can't fit in any partition." )
                messagebox.showinfo( "Compute Error" , "Error: Size 3 input can't fit in any partition." )
            elif self.size4_Check2:
                print ( "Error: Size 4 input can't fit in any partition." )
                messagebox.showinfo( "Compute Error" , "Error: Size 4 input can't fit in any partition." )
            elif self.size5_Check2:
                print ( "Error: Size 5 input can't fit in any partition." )
                messagebox.showinfo( "Compute Error" , "Error: Size 5 input can't fit in any partition." )
            elif self.arrivalTime1_Check or self.arrivalTime2_Check or self.arrivalTime3_Check or self.arrivalTime4_Check or self.arrivalTime5_Check:
                print ( " Error in arrival time input " )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Arrival Time Input." )
            elif self.runTime1_Check or self.runTime2_Check or self.runTime3_Check or self.runTime4_Check or self.runTime5_Check:
                print ( "Error: Invalid Run Time Input." )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Run Time Input." )
            else:
                size1 = int(size1)
                size2 = int(size2)
                size3 = int(size3)
                size4 = int(size4)
                size5 = int(size5)
                jobSizes = [ size1, size2, size3, size4, size5 ]
                self.allJobArrivalTime = [ self.arrivalTime1, self.arrivalTime2, self.arrivalTime3, self.arrivalTime4, self.arrivalTime5 ]
                self.allJobRunTime = [ self.runTime1, self.runTime2, self.runTime3, self.runTime4, self.runTime5 ]
                self.createResultWindows( jobSizes, self.allJobArrivalTime, self.allJobRunTime, partitionSizes )


    # For taking user's input of each job's information
    def mainInput2_window ( self ):
        self.clearWidgets()
        basicWidgetList = []
        
        self.bg2LBL = Label ( root , image = bg2, bg = "black" )
        self.bg2LBL.place(x = 0, y = 0)
        basicWidgetList.append( self.bg2LBL )
        
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
        
        self.bg2LBL = Label ( root , image = bg2, bg = "black" )
        self.bg2LBL.place(x = 0, y = 0)
        basicWidgetList.append( self.bg2LBL )
        
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



# The User Interface's activation.
root.resizable( width = FALSE , height = FALSE )
root.geometry( "900x600" )
root.config ( background = "LIGHTBLUE" )


# Initialize the class mainUI into mainUI variable.
# Display the first window of the program ( mainInput1_window )
mainUI = mainUI()
mainUI.mainInput1_window()
root.mainloop()
