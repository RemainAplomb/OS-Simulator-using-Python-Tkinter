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
    current_directory = os.getcwd()
    ####print(current_directory)
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

def load_image(file_path, prefix_cd=True, dim= (900, 600)):
    if prefix_cd:
        file_path = current_directory + file_path
    image = Image.open(file_path)
    image = image.resize((dim[0], dim[1]), Image.ANTIALIAS)
    photo_image = ImageTk.PhotoImage(image)
    return photo_image

# Backgrounds
main_menu_bg = load_image("\\resources\\background\\m2_bg.png")
pa_bg = load_image("\\resources\\background\\m2_bg.png")
pm_bg = load_image("\\resources\\background\\m2_bg.png")
sc_bg = load_image("\\resources\\background\\m2_bg1.png")
spa_bg = load_image("\\resources\\background\\m2_bg1.png")
dff_bg = load_image("\\resources\\background\\m2_bg1.png")
dbf_bg = load_image("\\resources\\background\\m2_bg1.png")
fcfs_bg = load_image("\\resources\\background\\m2_bg.png")
sjf_bg = load_image("\\resources\\background\\m2_bg.png")
srtf_bg = load_image("\\resources\\background\\m2_bg.png")
rr_bg = load_image("\\resources\\background\\m2_bg.png")
p_bg = load_image("\\resources\\background\\m2_bg.png")

# Buttons
main_menu_btn = load_image("\\resources\\buttons\\mainMenu.png")

class Frontend_Functions:
    def __init__(self):
        pass

    # The program has two list which contains a reference to all the program's widgets
    # And what this function does is it tries to clear/destroy all of these widgets
    # using the lists which contains the program's widgets.
    # The two lists are:
    #   - self.basic_widget_list: For most of the basic widgets
    #   - self.phys_mem_widgets: For the widgets used to display physical memory map
    def clear_widgets( self ):
        try:
            self.tick_on = False
            self.clear_widget_list( self.basic_widget_list )
            self.clear_widget_list( self.phys_mem_widgets )
        except:
            pass
        return

    # This function destroys all of the widgets inside the inputted widgets_to_clear list.
    def clear_widget_list ( self, widgets_to_clear):
        for widget in widgets_to_clear:
            widget.destroy()

    # For getting the current date
    def current_date( self ):
        self.date_string  =  datetime.date.today().strftime("%B %d, %Y")
        self.date_LBL.config(text = self.date_string)

    # This updates the clock widget
    def tick( self ):
        if self.tick_on:
            self.time_string  =  time.strftime("%H:%M:%S")
            self.clockLBL.config(text = self.time_string)
            self.clockLBL.after(200, self.tick )
        else:
            pass
    
    def create_BG(self, root_location, image_label, bg_clr="black", placement=(0, 0)):
        create_bg = Label(root_location, image=image_label, bg=bg_clr)
        create_bg.place(x=placement[0], y=placement[1])
        self.basic_widget_list.append(create_bg)
        return create_bg
    
    def create_image_BTN(self, root_location, image_for_btn, execute_cmd, bg_btn="#f4e033", placement=(840, 20)):
        create_btn = Button(root_location, image=image_for_btn, command=execute_cmd, bg=bg_btn)
        create_btn.place(x=placement[0], y=placement[1])
        self.basic_widget_list.append(create_btn)
        return create_btn
    
    def create_text_BTN(self, root_location, text_label, execute_cmd, font_label=('Consolas', 13, 'bold'), width_label=20, bg_clr="#B3B3B3", placement=(0, 0)):
        create_btn = Button(root_location, text=text_label, command=execute_cmd, font=font_label, width=width_label, bg=bg_clr)
        create_btn.place(x=placement[0], y=placement[1])
        self.basic_widget_list.append(create_btn)
        return create_btn
    
    def create_LBL(self, root_location, font_label=('Cooper Black', 14), bg_clr="#99d9ea", placement=(0, 0)):
        create_lbl = Label(root_location, font=font_label, bg=bg_clr)
        create_lbl.place(x=placement[0], y=placement[1])
        self.basic_widget_list.append(create_lbl)
        return create_lbl

    def create_text_LBL(self, root_location, lbl_text, font_label=('Cooper Black', 14), bg_clr="#99d9ea", placement=(0, 0)):
        create_lbl = Label( root_location , text = lbl_text , font = font_label,  bg = bg_clr)
        create_lbl.place(x=placement[0], y=placement[1])
        self.basic_widget_list.append(create_lbl)
        return create_lbl
    
    
    def create_ENTRY(self, root_location, font_label=('Consolas', 10, 'bold'), placement=(225, 310), justify= "center", state="normal", text=None):
        create = Entry( root , font = font_label, justify= justify)
        create.place(x=placement[0], y=placement[1])
        if text != None:
            create.insert( 0, text )
        if state == "readonly":
            create.config( state = state )
        self.basic_widget_list.append( create )
        return create

    def create_LISTBOX(self, HWB= (6, 40, 0), placement=(220, 430), justify = "center"):
        listbox = Listbox( root, height = HWB[0], width = HWB[1], border = HWB[2], justify = justify )
        listbox.place( x = placement[0], y = placement[1] )
        self.basic_widget_list.append( listbox )
        return listbox
    
    def create_clock(self, date_placement=(313, 350), clock_placement= (513, 350), bg_clr= "#99d9ea"):
        self.date_LBL = self.create_LBL(root, font_label=('Impact', 14), bg_clr=bg_clr, placement=date_placement)
        self.current_date()

        self.clockLBL = self.create_LBL(root, font_label=('Impact', 14), bg_clr=bg_clr, placement=clock_placement)
        self.tick_on = True
        self.tick()

class Frontend_Functions2:
    def __init__(self):
        pass

    # This function displays the necessary widgets for physical memory map.
    # To get a general gist, the program has around 50 labels which acts as the physical memory map.
    # In addition, it has a text label which marks each section of the physical memory map.
    def display_map( self, temp_pointer, temp_clr, temp_txt, temp_percentage, temp_total_size, label_height = 7, x_placement = 550):
        self.temp_pointer = int(temp_pointer)
        self.temp_clr = temp_clr
        self.temp_txt = temp_txt
        self.temp_percentage = temp_percentage
        self.temp_total_size = temp_total_size
        
        if self.temp_percentage != 0:
            self.temp_LBL = Label( root , text = "          " * 25 , font = ('Times New Roman', 1),  bg = self.temp_clr)
            self.temp_LBL.place(x = x_placement, y = self.y_counter)
            self.y_counter += label_height
            self.phys_mem_widgets.append( self.temp_LBL )
            
            self.temp_LBL = Label( root , text = self.temp_txt , font = ('Times New Roman', 10),  bg = self.temp_clr)
            self.temp_LBL.place(x = x_placement + 270, y = self.y_counter)
            self.phys_mem_widgets.append( self.temp_LBL )
        for i in range( int( self.temp_percentage / 2 ) ):
            if self.temp_pointer != 0:
                self.temp_LBL = Label( root , text = "          " * 25 , font = ('Times New Roman', 1),  bg = self.temp_clr)
                self.temp_LBL.place(x = x_placement, y = self.y_counter)
                self.y_counter += label_height
                self.phys_mem_widgets.append( self.temp_LBL )
                self.temp_pointer -= 1
            else:
                pass
        if self.temp_percentage != 0:
            self.temp_LBL  =  Label( root , text = temp_total_size , font = ('Times New Roman', 10),  bg = self.temp_clr)
            self.temp_LBL.place(x = x_placement - 40, y = self.y_counter - 15)
            self.phys_mem_widgets.append( self.temp_LBL )
        return

class Backend_Functions:
    def __init__(self):
        pass

    # This function returns True if time_input is not in proper time format
    # Else, returns False if the input is in proper time format
    # Time format is HH:MM
    def is_not_time_format( self, time_input):
        try:
            time.strptime( time_input, '%H:%M')
            return False
        except ValueError:
            return True

    # This function returns True if the integer_input is not an Integer.
    # If it is an integer, return False.
    def is_not_integer( self, integer_input):
        try:
            self.intTest = int(integer_input)
            return False
        except ValueError:
            return True
    
    # To clear the linked list of nodes.
    def clear_nodes( self ):
        self.head_node = None
        return
    
    # To add a node into the linked list
    def add_result_node( self, time, result_data, time_type, text_title ): # ( self, time = "9:00:00" , data = None, time_type = "At", text_title = "Jx removed" ):
        self.temp_node = Node( time, result_data, time_type, text_title )

        if self.head_node == None:
            self.head_node = self.temp_node
        else:
            self.head_node.back_pointer = self.temp_node
            self.temp_node.next_pointer = self.head_node

            self.head_node = self.temp_node
        return

    # This function checks if a certain time( check_time ) is between two time ( begin_time and end_time )
    def is_time_between(self, begin_time, end_time, check_time=None):
        # If check time is not given, default to current UTC time
        check_time = check_time or datetime.utcnow().time()
        if begin_time < end_time:
            return check_time >= begin_time and check_time <= end_time
        else: # crosses midnight
            return check_time >= begin_time or check_time <= end_time

    # This function checks if a certain job could fit into any of the partitions.
    def cant_fit_in_partition( self, temp_job ):
        try:
            ##print( partition_sizes )
            ##print ( "start" )
            self.temp_job = int(temp_job)
            self.temp_result = True
            ##print ( "2" )
            for i in range( len( partition_sizes) ):
                ##print( " partition size: " , partition_sizes[i] )
                ##print ( " temp job: " , self.temp_job )
                if int(partition_sizes[i]) >= self.temp_job:
                    ##print( "2.2" )
                    self.temp_result = False
                    break
            ##print ( "3" )
            return self.temp_result
        except:
            return True



class Main(Frontend_Functions):
    def __init__(self):
        super().__init__()
    
            
    def main_menu_window( self ):
        root.title ( "OS Simulation: Main Menu" )
        self.clear_widgets()
        self.basic_widget_list = []
        
        self.main_menu_BG = self.create_BG(root, main_menu_bg, bg_clr="black", placement=(0, 0))

        self.create_clock(date_placement= (710, 100), clock_placement= (725, 50), bg_clr= "#D3BAF4")

        self.static_LBL = self.create_text_LBL(root, lbl_text="Static", font_label=('Times New Roman', 20),
                                          bg_clr="#0096FF", placement=(100, 70))
        self.dynamic_LBL = self.create_text_LBL(root, lbl_text="Dynamic", font_label=('Times New Roman', 20),
                                          bg_clr="#0096FF", placement=(400, 70))

        self.sff_BTN  =  self.create_text_BTN(root, 'First Fit', self.static_first_fit, font_label=('Consolas', 13, 'bold'), width_label=20, bg_clr="#B3B3B3", placement=(50, 170))
        
        
        self.sbf_BTN  =  self.create_text_BTN(root, 'Best Fit', self.static_best_fit, font_label=('Consolas', 13, 'bold'), width_label=20, bg_clr="#B3B3B3", placement=(50, 270))

        self.swf_BTN  =  self.create_text_BTN(root, 'Worst Fit', self.static_worst_fit, font_label=('Consolas', 13, 'bold'), width_label=20, bg_clr="#B3B3B3", placement=(50, 370))
        
        
        self.dff_BTN  =  self.create_text_BTN(root, 'First Fit', self.dynamic_first_fit, font_label=('Consolas', 13, 'bold'), width_label=20, bg_clr="#B3B3B3", placement=(350, 170))
        
        self.dbf_BTN  =  self.create_text_BTN(root, 'Best Fit', self.dynamic_best_fit, font_label=('Consolas', 13, 'bold'), width_label=20, bg_clr="#B3B3B3", placement=(350, 270))

        self.dwf_BTN  =  self.create_text_BTN(root, 'Worst Fit', self.dynamic_worst_fit, font_label=('Consolas', 13, 'bold'), width_label=20, bg_clr="#B3B3B3", placement=(350, 370))

        self.sc_BTN  =  self.create_text_BTN(root, 'Single Contiguous', self.single_contiguous, font_label=('Consolas', 13, 'bold'), width_label=20, bg_clr="#B3B3B3", placement=(200, 500))
    
    def static_first_fit( self ):
        static_first_fit_program.main_input1_window()

    def static_best_fit( self ):
        static_best_fit_program.main_input1_window()
    
    def static_worst_fit( self ):
       static_worst_fit_program.main_input1_window()
    
    def single_contiguous( self ):
        single_contiguous_program.input1_window()

    def dynamic_first_fit( self ):
        dynamic_first_fit_program.input1_window()

    def dynamic_best_fit( self ):
        dynamic_best_fit_program.input1_window()
    
    def dynamic_worst_fit( self ):
        dynamic_worst_fit_program.input1_window()



# Single_Contiguous PROGRAM: Line 227-1337

class Single_Contiguous_Node(Frontend_Functions, Frontend_Functions2, Backend_Functions):
    def __init__(self, job_number, prev_finish_time, start_time, memory_size, os_size, job_size, cpu_wait= "0:00:00"):
        super().__init__()
        self.next_pointer = None
        self.back_pointer = None

        self.job_number = job_number
        self.prev_finish_time = prev_finish_time
        self.start_time = start_time
        self.memory_size = memory_size
        self.os_size = os_size
        self.job_size = job_size
        self.cpu_wait= cpu_wait

        self.os_percentage = float(( int(self.os_size) / int(self.memory_size) ) * 100 )
        self.jobPercentage = float(( int(self.job_size) / int(self.memory_size) ) * 100 )

        self.wasted_size = float(self.memory_size) - (int(self.os_size) + int(self.job_size))
        self.wasted_percentage = int(( int(self.wasted_size) / int(self.memory_size) ) * 100 )


    # This function points which window to go back on.
    def back_BTN_Pressed( self ):
        if self.back_pointer == None:
            single_contiguous_program.result1_window()
        else:
            self.back_pointer.result_window()
    
    # This function points which window to go on next.
    def next_BTN_Pressed( self ):
        if self.next_pointer == None:
            single_contiguous_program.input1_window()
        else:
            self.next_pointer.result_window()


    # For displaying the physical memory map
    def result_window( self):
        self.clear_widgets()
        self.basic_widget_list = []

        self.single_contigious_BG = self.create_BG(root, sc_bg, bg_clr="black", placement=(0, 0))

        self.create_clock(date_placement= (170, 50), clock_placement= (700, 50), bg_clr= "#D3BAF4")

        self.title1_LBL = self.create_text_LBL(root, lbl_text= "Single Contiguous", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(375, 20))
        self.title2_LBL = self.create_text_LBL(root, lbl_text= "Memory Management", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(355, 65))

        self.title3_LBL = self.create_text_LBL(root, lbl_text= "Physical Memory Map", font_label=('Times New Roman', 20), bg_clr="#0096FF", placement=(150, 170))
        if int(self.job_number) == 1:
            self.title4_LBL = self.create_text_LBL(root, lbl_text= f"At {str(self.start_time.time())}, Job {str(self.job_number)} Started", font_label=('Times New Roman', 12), bg_clr="#0096FF", placement=(185, 203))
        elif self.cpu_wait == "0:00:00":
            self.title4_LBL = self.create_text_LBL(root, lbl_text= f"At {str(self.start_time.time())}, Job {str(self.job_number)} Started", font_label=('Times New Roman', 12), bg_clr="#0096FF", placement=(185, 203))
            self.title5_LBL = self.create_text_LBL(root, lbl_text= f"Earlier at {str(self.prev_finish_time.time())}, Job {str(int(self.job_number) - 1)} Terminated", font_label=('Times New Roman', 12), bg_clr="#0096FF", placement=(115, 180))
        else:
            self.title4_LBL = self.create_text_LBL(root, lbl_text= f"At {str(self.start_time.time())}, Job {str(int(self.job_number) - 1 )} Terminated and Job {str(self.job_number)} Started", font_label=('Times New Roman', 12), bg_clr="#0096FF", placement=(120, 203))
            
        

        self.phys_mem_widgets = []
        self.y_counter = 140
        #self.physicalMemInfo1 = [ [ 30, "#f2f5f4", "OS Size", "" ], [ 75, "#c2c4c3", "Job Size", "312"], [ 0, "#979998", "Wasted", "412"] ]
        self.temp_clr = "#f2f5f4"
        self.index_pointer = 0
        self.temp_type_printed = False
        
        self.mark_LBL  =  self.create_text_LBL(root, lbl_text= "0", font_label=('Times New Roman', 10), bg_clr="#0096FF", placement=(530, self.y_counter - 20))

        self.temp_total_size = int(self.os_size)
        self.display_map( self.os_percentage, "#f5f3ed", "Os Size", self.os_percentage, self.temp_total_size )

        self.temp_total_size = int(self.os_size) + int(self.job_size)
        self.display_map( self.jobPercentage, "#c2c4c3", f"Job {str(self.job_number)} Size", self.jobPercentage, self.temp_total_size )

        self.temp_total_size = int(self.os_size) + int(self.job_size) + int(self.wasted_size)
        self.display_map( self.wasted_percentage, "#979998", "Wasted size", self.wasted_percentage, self.temp_total_size )


        # Widgets
        self.os_size_LBL = self.create_text_LBL(root, lbl_text= "OS Size", font_label=('Times New Roman', 15), bg_clr="#f5f3ed", placement=(100, 245))
        self.os_size_entry = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(65, 285), state="readonly", text=self.os_size)

        
        self.memory_size_LBL = self.create_text_LBL(root, lbl_text="Memory Size", font_label=('Times New Roman', 15),
                                         bg_clr="#0096FF", placement=(290, 245))
        self.memory_size_entry = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(275, 285), state="readonly", text=self.memory_size)


        self.job1size_LBL = self.create_text_LBL(root, lbl_text="Job 1 Size", font_label=('Times New Roman', 15),
                                          bg_clr="#c2c4c3", placement=(90, 345))
        self.job1SizeENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(65, 385), state="readonly", text=self.job_size)

        self.wasted_size_LBL = self.create_text_LBL(root, lbl_text="Wasted Size", font_label=('Times New Roman', 15),
                                                    bg_clr="#979998", placement=(295, 345))

        self.wasted_sizeENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                                placement=(275, 385), state="readonly", text=self.wasted_size)
        
        self.back_BTN  =  self.create_text_BTN(root, text_label= 'BACK', execute_cmd= self.back_BTN_Pressed, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(200, 530))
        if self.next_pointer == None:
            self.next_BTN  =  self.create_text_BTN(root, text_label= 'NEW INPUT', execute_cmd= self.next_BTN_Pressed, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(580, 530))
        else:
            self.next_BTN  =  self.create_text_BTN(root, text_label= 'NEXT', execute_cmd= self.next_BTN_Pressed, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(580, 530))
        self.exit_BTN  =  self.create_text_BTN(root, text_label= 'EXIT', execute_cmd= root.destroy, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(390, 530))


# single_contiguous_program class which contains most of all the program's code.
# This contains all the window functions and miscellaneous functions
# To know each function's description, look at the documentation at the first line. ( *Ctrl + h* line 27 and 37 )
class Single_Contiguous_Program(Frontend_Functions, Frontend_Functions2, Backend_Functions):
    def __init__(self):
        super().__init__()
        self.head_node = None

    # To clear the linked list of nodes.
    def clear_nodes( self ):
        self.head_node = None
        return

    # To add a node into the linked list
    def add_result_node( self, job_number, prev_finish_time, start_time, memory_size, os_size, job_size, cpu_wait = None ): 
        self.temp_node = Single_Contiguous_Node(job_number, prev_finish_time, start_time, memory_size, os_size, job_size, cpu_wait)

        if self.head_node == None:
            self.head_node = self.temp_node
        else:
            self.head_node.back_pointer = self.temp_node
            self.temp_node.next_pointer = self.head_node

            self.head_node = self.temp_node
        return

    # This functions has all the necessary computations for the computation result.
    def main1_window_compute ( self ):
        if messagebox.askyesno( "Confirmation..." , " Are you sure you want to compute? " ) == True :
            self.clear_nodes()

            self.size1 = self.size1_ENTRY.get()
            self.size2 = self.size2_ENTRY.get()
            self.size3 = self.size3_ENTRY.get()
            self.size4 = self.size4_ENTRY.get()
            self.size5 = self.size5_ENTRY.get()

            self.memory_size = self.memory_size_entry.get()
            self.os_size = self.os_size_entry.get()

            self.memory_size_CHECK = self.is_not_integer( self.memory_size )
            self.os_size_CHECK = self.is_not_integer( self.os_size )
 
            self.size1_CHECK = self.is_not_integer( self.size1 )
            #print ( self.size1_CHECK )
            self.size2_CHECK = self.is_not_integer( self.size2 )
            self.size3_CHECK = self.is_not_integer( self.size3 )
            self.size4_CHECK = self.is_not_integer( self.size4 )
            self.size5_CHECK = self.is_not_integer( self.size5 )
            
            
            self.arrival_time1 = self.arrival_time1_ENTRY.get()
            self.arrival_time2 = self.arrival_time2_ENTRY.get()
            self.arrival_time3 = self.arrival_time3_ENTRY.get()
            self.arrival_time4 = self.arrival_time4_ENTRY.get()
            self.arrival_time5 = self.arrival_time5_ENTRY.get()

            self.arrival_time1_CHECK = self.is_not_time_format( self.arrival_time1 )
            self.arrival_time2_CHECK = self.is_not_time_format( self.arrival_time2 )
            self.arrival_time3_CHECK = self.is_not_time_format( self.arrival_time3 )
            self.arrival_time4_CHECK = self.is_not_time_format( self.arrival_time4 )
            self.arrival_time5_CHECK = self.is_not_time_format( self.arrival_time5 )

            self.run_time1 = self.run_time1_ENTRY.get()
            self.run_time2 = self.run_time2_ENTRY.get()
            self.run_time3 = self.run_time3_ENTRY.get()
            self.run_time4 = self.run_time4_ENTRY.get()
            self.run_time5 = self.run_time5_ENTRY.get()
        
            self.run_time1_CHECK = self.is_not_time_format( self.run_time1 )
            self.run_time2_CHECK = self.is_not_time_format( self.run_time2 )
            self.run_time3_CHECK = self.is_not_time_format( self.run_time3 )
            self.run_time4_CHECK = self.is_not_time_format( self.run_time4 )
            self.run_time5_CHECK = self.is_not_time_format( self.run_time5 )

            if self.memory_size_CHECK or self.os_size_CHECK :
                #print ( "Error: Invalid Memory or OS Size input." )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Memory or OS Size input." )
            elif int(self.memory_size) < int(self.os_size):
                ##print ( "ting" )
                #print ( " Error: Os Size can't exceed Memory Size. " )
                messagebox.showinfo( "Compute Error" , "Error: Os Size can't exceed Memory Size." )
            elif self.size1_CHECK or self.size2_CHECK or self.size3_CHECK or self.size4_CHECK or self.size5_CHECK:
                #print ( "Error: Size input detected as not an integer." )
                messagebox.showinfo( "Compute Error" , "Error: Size input detected as not an integer." )
            elif (int(self.size1) > ( int(self.memory_size) - int(self.os_size))) or (int(self.size2) > ( int(self.memory_size) - int(self.os_size))) or (int(self.size3) > ( int(self.memory_size) - int(self.os_size))) or (int(self.size4) > ( int(self.memory_size) - int(self.os_size))) or (int(self.size5) > ( int(self.memory_size) - int(self.os_size))):
                #print ( "Error: Size input should not exceed ( Memory Size - OS Size )." )
                messagebox.showinfo( "Compute Error" , "Error: Size input should not exceed ( Memory Size - OS Size )." )
            elif self.arrival_time1_CHECK or self.arrival_time2_CHECK or self.arrival_time3_CHECK or self.arrival_time4_CHECK or self.arrival_time5_CHECK:
                #print ( " Error in arrival time input " )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Arrival Time Input." )
            elif self.run_time1_CHECK or self.run_time2_CHECK or self.run_time3_CHECK or self.run_time4_CHECK or self.run_time5_CHECK:
                #print ( "Error: Invalid Run Time Input." )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Run Time Input." )
            else:
                self.time_zero = datetime.datetime.strptime('00:00', '%H:%M')
                
                # Job 1
                self.start_time1 = datetime.datetime.strptime( self.arrival_time1, '%H:%M')
                if (self.start_time1 - datetime.datetime.strptime( self.arrival_time1, '%H:%M')).total_seconds() < 0:
                    self.cpu_wait1 = "0:00:00"
                    self.start_time1 = datetime.datetime.strptime( self.arrival_time1, '%H:%M')
                else:
                    self.cpu_wait1 = self.start_time1 - datetime.datetime.strptime( self.arrival_time1, '%H:%M')

                # Job 2
                self.finish_time1 = ( self.start_time1 - self.time_zero + (datetime.datetime.strptime(self.run_time1, '%H:%M')))
                self.start_time2 = self.finish_time1

                if (self.start_time2 - datetime.datetime.strptime( self.arrival_time2, '%H:%M')).total_seconds() < 0:
                    self.cpu_wait2 = "0:00:00"
                    self.start_time2 = datetime.datetime.strptime( self.arrival_time2, '%H:%M')
                else:
                    self.cpu_wait2 = self.start_time2 - datetime.datetime.strptime( self.arrival_time2, '%H:%M')

                # Job 3
                self.finish_time2 = ( self.start_time2 - self.time_zero + (datetime.datetime.strptime(self.run_time2, '%H:%M')))
                self.start_time3 = self.finish_time2

                if (self.start_time3 - datetime.datetime.strptime( self.arrival_time3, '%H:%M')).total_seconds() < 0:
                    self.cpu_wait3 = "0:00:00"
                    self.start_time3 = datetime.datetime.strptime( self.arrival_time3, '%H:%M')
                else:
                    self.cpu_wait3 = self.start_time3 - datetime.datetime.strptime( self.arrival_time3, '%H:%M')
                
                # Job 4
                self.finish_time3 = ( self.start_time3 - self.time_zero + (datetime.datetime.strptime(self.run_time3, '%H:%M')))
                self.start_time4 = self.finish_time3

                if (self.start_time4 - datetime.datetime.strptime( self.arrival_time4, '%H:%M')).total_seconds() < 0:
                    self.start_time4 = datetime.datetime.strptime( self.arrival_time4, '%H:%M')
                    self.cpu_wait4 = "0:00:00"
                else:
                    self.cpu_wait4 = self.start_time4 - datetime.datetime.strptime( self.arrival_time4, '%H:%M')

                # Job 5
                self.finish_time4 = ( self.start_time4 - self.time_zero + (datetime.datetime.strptime(self.run_time4, '%H:%M')))
                self.start_time5 = self.finish_time4

                if (self.start_time5 - datetime.datetime.strptime( self.arrival_time5, '%H:%M')).total_seconds() < 0:
                    self.start_time5 = datetime.datetime.strptime( self.arrival_time5, '%H:%M')
                    self.cpu_wait5 = "0:00:00"
                else:
                    self.cpu_wait5 = self.start_time5 - datetime.datetime.strptime( self.arrival_time5, '%H:%M')

                self.finish_time5 = ( self.start_time5 - self.time_zero + (datetime.datetime.strptime(self.run_time5, '%H:%M')))

                self.add_result_node( job_number = 5, prev_finish_time = self.finish_time4, start_time= self.start_time5, memory_size=self.memory_size, os_size=self.os_size, job_size=self.size5, cpu_wait = self.cpu_wait5 )
                self.add_result_node( job_number = 4, prev_finish_time = self.finish_time3, start_time= self.start_time4, memory_size=self.memory_size, os_size=self.os_size, job_size=self.size4, cpu_wait = self.cpu_wait4 )
                self.add_result_node( job_number = 3, prev_finish_time = self.finish_time2, start_time= self.start_time3, memory_size=self.memory_size, os_size=self.os_size, job_size=self.size3, cpu_wait = self.cpu_wait3 )
                self.add_result_node( job_number = 2, prev_finish_time = self.finish_time1, start_time= self.start_time2, memory_size=self.memory_size, os_size=self.os_size, job_size=self.size2, cpu_wait = self.cpu_wait2 )
                self.add_result_node( job_number = 1, prev_finish_time = None, start_time= self.start_time1, memory_size=self.memory_size, os_size=self.os_size, job_size=self.size1, cpu_wait = self.cpu_wait1 )
                
                #print( self.cpu_wait3, self.start_time3, datetime.datetime.strptime( self.arrival_time3, '%H:%M'))
                #print( self.cpu_wait4, self.start_time4, datetime.datetime.strptime( self.arrival_time4, '%H:%M'))
                #print( self.cpu_wait5, self.start_time4, datetime.datetime.strptime( self.arrival_time5, '%H:%M'))
                #print ( " Success " )
                self.result1_window()


    def main_menu_BTN_pressed( self ):
        main_program.main_menu_window()


    # From here, and down to the last function are the windows/pages of the GUI.
    def input1_window ( self ):
        root.title ( "Single Contiguous Memory Management" )
        self.clear_widgets()
        self.basic_widget_list = []

        self.single_contigious_BG = self.create_BG(root, sc_bg, bg_clr="black", placement=(0, 0))

        self.create_clock(date_placement= (170, 50), clock_placement= (700, 50), bg_clr= "#D3BAF4")

        self.title1_LBL = self.create_text_LBL(root, lbl_text= "Single Contiguous", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(375, 20))
        self.title2_LBL = self.create_text_LBL(root, lbl_text= "Memory Management", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(355, 65))

        self.job_LBL = self.create_text_LBL(root, lbl_text= "Job", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(125, 130))
        self.job1_LBL = self.create_text_LBL(root, lbl_text= "1", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(125, 190))
        self.job2_LBL = self.create_text_LBL(root, lbl_text= "2", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(125, 250))
        self.job3_LBL = self.create_text_LBL(root, lbl_text= "3", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(125, 310))
        self.job4_LBL = self.create_text_LBL(root, lbl_text= "4", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(125, 370))
        self.job5_LBL = self.create_text_LBL(root, lbl_text= "5", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(125, 430))

        self.size_LBL = self.create_text_LBL(root, lbl_text= "Size", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(275, 130))

        self.size1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(225, 190), justify="center")
        self.size2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(225, 250), justify="center")
        self.size3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(225, 310), justify="center")
        self.size4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(225, 370), justify="center")
        self.size5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(225, 430), justify="center")


        self.arrival_time_LBL  = self.create_text_LBL(root, lbl_text= "Arrival Time", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(505, 130))

        self.arrival_time1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(490, 190), justify="center")
        self.arrival_time2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(490, 250), justify="center")
        self.arrival_time3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(490, 310), justify="center")
        self.arrival_time4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(490, 370), justify="center")
        self.arrival_time5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(490, 430), justify="center")

        
        self.run_time_LBL  = self.create_text_LBL(root, lbl_text= "Run Time", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(725, 130))

        self.run_time1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(700, 190), justify="center")
        self.run_time2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(700, 250), justify="center")
        self.run_time3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(700, 310), justify="center")
        self.run_time4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(700, 370), justify="center")
        self.run_time5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(700, 430), justify="center")


        self.memory_size_LBL  = self.create_text_LBL(root, lbl_text= "Memory Size", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(300, 470))
        self.memory_size_entry = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(280, 520), justify="center")

        self.os_size_LBL  = self.create_text_LBL(root, lbl_text= "OS Size", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(510, 470))
        self.os_size_entry = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(475, 520), justify="center")

        self.exit_BTN  =  self.create_text_BTN(root, text_label= 'Exit', execute_cmd= root.destroy, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(190, 550))
        self.compute_BTN  =  self.create_text_BTN(root, text_label= 'Compute', execute_cmd= self.main1_window_compute, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(390, 550))
        self.main_menu_BTN = self.create_text_BTN(root, text_label= 'Menu', execute_cmd= self.main_menu_BTN_pressed, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(590, 550))

        
    def result1_window ( self ):
        self.clear_widgets()
        self.basic_widget_list = []
        
        self.single_contigious_BG = self.create_BG(root, sc_bg, bg_clr="black", placement=(0, 0))

        self.create_clock(date_placement= (170, 50), clock_placement= (700, 50), bg_clr= "#D3BAF4")

        self.title1_LBL = self.create_text_LBL(root, lbl_text= "Single Contiguous", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(375, 20))
        self.title2_LBL = self.create_text_LBL(root, lbl_text= "Memory Management", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(355, 65))

        self.job_LBL = self.create_text_LBL(root, lbl_text= "Job", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(125, 160))
        self.job1_LBL = self.create_text_LBL(root, lbl_text= "1", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(125, 220))
        self.job2_LBL = self.create_text_LBL(root, lbl_text= "2", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(125, 280))
        self.job3_LBL = self.create_text_LBL(root, lbl_text= "3", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(125, 340))
        self.job4_LBL = self.create_text_LBL(root, lbl_text= "4", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(125, 420))
        self.job5_LBL = self.create_text_LBL(root, lbl_text= "5", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(125, 460))

        self.start_time_LBL = self.create_text_LBL(root, lbl_text= "Start Time", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(280, 160))
        self.start_time1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(225, 220), state="readonly", text=self.start_time1.time())
        self.start_time2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(225, 280), state="readonly", text=self.start_time2.time())
        self.start_time3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(225, 340), state="readonly", text=self.start_time3.time())
        self.start_time4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(225, 400), state="readonly", text=self.start_time4.time())
        self.start_time5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(225, 460), state="readonly", text=self.start_time5.time())
        
        self.finish_time_LBL = self.create_text_LBL(root, lbl_text= "Finish Time", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(510, 160))
        self.finish_time1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(490, 220), state="readonly", text=self.finish_time1.time())
        self.finish_time2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(490, 280), state="readonly", text=self.finish_time2.time())
        self.finish_time3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(490, 340), state="readonly", text=self.finish_time3.time())
        self.finish_time4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(490, 400), state="readonly", text=self.finish_time4.time())
        self.finish_time5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(490, 460), state="readonly", text=self.finish_time5.time())

        self.cpu_wait_LBL = self.create_text_LBL(root, lbl_text= "CPU Wait", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(725, 160))
        self.cpu_wait1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(700, 220), state="readonly", text=self.cpu_wait1)
        self.cpu_wait2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(700, 280), state="readonly", text=self.cpu_wait2)
        self.cpu_wait3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(700, 340), state="readonly", text=self.cpu_wait3)
        self.cpu_wait4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(700, 400), state="readonly", text=self.cpu_wait4)
        self.cpu_wait5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(700, 460), state="readonly", text=self.cpu_wait5)
        
        self.back_BTN  =  self.create_text_BTN(root, text_label= 'BACK', execute_cmd= self.input1_window, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(190, 550))
        self.exit_BTN  =  self.create_text_BTN(root, text_label= 'EXIT', execute_cmd= root.destroy, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(390, 550))
        self.next_BTN  =  self.create_text_BTN(root, text_label= 'NEXT', execute_cmd= self.head_node.result_window, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(590, 550))
    
# END OF single_contiguous PROGRAM: Line 227-695



# SPA PROGRAM: Line 1340-2838

# Global Variables
partition1 = 8
partition2 = 32
partition3 = 32
partition4 = 120
partition5 = 520
partition_sizes = [ partition1, partition2, partition3, partition4, partition5 ]

os_size = 312
memory_size = 1024

size1 = 5
size2 = 32
size3 = 50
size4 = 130
size5 = 150

job_sizes = [ size1, size2, size3, size4, size5 ]

os_percentage = float(( float(os_size) / float(memory_size) ) * 100 )
partition1_percentage = float(( float(partition1) / float(memory_size) ) * 100 )
partition2_percentage = float(( float(partition2) / float(memory_size) ) * 100 )
partition3_percentage = float(( float(partition3) / float(memory_size) ) * 100 )
partition4_percentage = float(( float(partition4) / float(memory_size) ) * 100 )
partition5_percentage = float(( float(partition5) / float(memory_size) ) * 100 )


all_partition_percentage = [ partition1_percentage,
                           partition2_percentage,
                           partition3_percentage,
                           partition4_percentage,
                           partition5_percentage ]
# basic_widget_list = []
# phys_mem_widgets = []
# */ End of Global variable code block.



# This is a node class for the result windows ( i.e. mem_map_window, pat_window )
# Check line 41 and 52 to get the description of the Node class' functions.
class Node (Frontend_Functions, Frontend_Functions2, Backend_Functions):
    def __init__( self, time = "*:**:**" , data = None, time_type = "After", text_title = "Jx Terminated" ):
        super().__init__()
        self.back_pointer = None
        self.next_pointer = None
        self.data = data
        self.time = time
        self.time_type = time_type
        self.text_title = text_title
        if self.data == None:
            self.data = [ "Available", "Available", "Available", "Available", "Available" ]
        
        self.title1_text = "Static First Fit"
        self.title1_placement = (400, 20)

    # This function points which window to go back on.
    def mem_map_back_BTN_Pressed( self ):
        if self.back_pointer == None:
            static_first_fit_program.main_result1_window()
        else:
            self.back_pointer.pat_window()


    # For displaying the physical memory map
    def mem_map_window( self ):
        #print( partition_sizes )
        self.clear_widgets()
        self.basic_widget_list = []
        self.nextAvailable = True

        self.static_first_fit_BG = self.create_BG(root, spa_bg, bg_clr="black", placement=(0, 0))

        self.create_clock(date_placement= (170, 50), clock_placement= (700, 50), bg_clr= "#D3BAF4")

        self.title1_LBL = self.create_text_LBL(root, lbl_text= self.title1_text, font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=self.title1_placement)
        self.title2_LBL = self.create_text_LBL(root, lbl_text= "Partitioned Allocation", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(355, 65))

        self.title3_LBL = self.create_text_LBL(root, lbl_text= "Physical Memory Map", font_label=('Times New Roman', 20), bg_clr="#0096FF", placement=(150, 120))
        if self.time_type == "After":
            self.title4_LBL = self.create_text_LBL(root, lbl_text= f"{str(self.time_type)} {str(self.time)}, {str(self.text_title)}", font_label=('Times New Roman', 12), bg_clr="#0096FF", placement=(185, 153))
        else:
            self.title4_LBL = self.create_text_LBL(root, lbl_text= f"{str(self.time_type)} {str(self.time)}, {str(self.text_title)}", font_label=('Times New Roman', 12), bg_clr="#0096FF", placement=(203, 153))
        
        self.phys_mem_widgets = []
        self.y_counter = 140
        self.index_pointer = 0
        
        self.mark_LBL  =  Label( root , text = 0 , font = ('Times New Roman', 10),  bg = "#0096FF")
        self.mark_LBL.place(x = 530, y = self.y_counter - 20)
        self.phys_mem_widgets.append( self.mark_LBL )

        self.temp_total_size = int(os_size)
        self.display_map( os_percentage, "#f5f3ed", "Os Size", os_percentage, self.temp_total_size )
                
        self.temp_total_size = int(os_size) + int(partition1) 
        self.display_map( partition1_percentage, "#f77777", self.data[0], partition1_percentage, self.temp_total_size )
                
        self.temp_total_size = int(os_size) + int(partition1) + int(partition2)
        self.display_map( partition2_percentage, "#f7d977", self.data[1], partition2_percentage, self.temp_total_size )

        self.temp_total_size = int(os_size) + int(partition1) + int(partition2) + int(partition3)
        self.display_map( partition3_percentage, "#77f7e6", self.data[2], partition3_percentage, self.temp_total_size )

        self.temp_total_size = int(os_size) + int(partition1) + int(partition2) + int(partition3) + int(partition4)
        self.display_map( partition4_percentage, "#77d5f7", self.data[3], partition4_percentage, self.temp_total_size )

        self.temp_total_size = int(os_size) + int(partition1) + int(partition2) + int(partition3) + int(partition4) + int(partition5)
        self.display_map( partition5_percentage, "#d577f7", self.data[4], partition5_percentage, self.temp_total_size )

        # Partition labels
        self.partition_LBL = self.create_text_LBL(root, lbl_text= "Partition", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(50, 180))

        self.partition1_LBL = self.create_text_LBL(root, lbl_text= "1", font_label=('Times New Roman', 15), bg_clr="#f77777", placement=(70, 240))
        self.partition2_LBL = self.create_text_LBL(root, lbl_text= "2", font_label=('Times New Roman', 15), bg_clr="#f7d977", placement=(70, 300))
        self.partition3_LBL = self.create_text_LBL(root, lbl_text= "3", font_label=('Times New Roman', 15), bg_clr="#77f7e6", placement=(70, 360))
        self.partition4_LBL = self.create_text_LBL(root, lbl_text= "4", font_label=('Times New Roman', 15), bg_clr="#77d5f7", placement=(70, 420))
        self.partition5_LBL = self.create_text_LBL(root, lbl_text= "5", font_label=('Times New Roman', 15), bg_clr="#d577f7", placement=(70, 480))

        # Fragmentation labels
        self.all_fragmentation = []

        for i in range( len(self.data) ):
            if self.data[i] != "Available":
                self.temp_job_numberum = int(self.data[i][11]) - 1
                self.all_fragmentation.append( int(partition_sizes[i]) - int(job_sizes[self.temp_job_numberum]) )
            else:
                self.all_fragmentation.append( "--" )
        
        self.fragmentation_LBL = self.create_text_LBL(root, lbl_text= "Internal Fragmentation", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(140, 180))

        self.fragmentation1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(160, 240), state="readonly", text=self.all_fragmentation[0])
        self.fragmentation2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(160, 300), state="readonly", text=self.all_fragmentation[1])
        self.fragmentation3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(160, 360), state="readonly", text=self.all_fragmentation[2])
        self.fragmentation4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(160, 420), state="readonly", text=self.all_fragmentation[3])
        self.fragmentation5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(160, 480), state="readonly", text=self.all_fragmentation[4])
        

        # Status labels
        self.statusLBL = self.create_text_LBL(root, lbl_text= "Status", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(370, 180))

        self.status1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(330, 240), state="readonly", text=self.data[0])
        self.status2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(330, 300), state="readonly", text=self.data[1])
        self.status3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(330, 360), state="readonly", text=self.data[2])
        self.status4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(330, 420), state="readonly", text=self.data[3])
        self.status5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(330, 480), state="readonly", text=self.data[4])
        
        # Buttons
        self.back_BTN  =  self.create_text_BTN(root, text_label= 'BACK', execute_cmd= self.mem_map_back_BTN_Pressed, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(200, 530))
        self.next_BTN  =  self.create_text_BTN(root, text_label= 'NEXT', execute_cmd= self.pat_window, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(580, 530))
        self.exit_BTN  =  self.create_text_BTN(root, text_label= 'EXIT', execute_cmd= root.destroy, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(390, 530))


    # This function points which window to go next.
    def pat_next_BTN_Pressed( self ):
        if self.next_pointer == None:
            static_first_fit_program.main_input1_window()
        else:
            self.next_pointer.mem_map_window()


    # For displaying the partition allocation table.
    def pat_window( self ):
        self.clear_widgets()
        self.basic_widget_list = []

        self.static_first_fit_BG = self.create_BG(root, spa_bg, bg_clr="black", placement=(0, 0))

        self.create_clock(date_placement= (170, 50), clock_placement= (700, 50), bg_clr= "#D3BAF4")

        self.title1_LBL = self.create_text_LBL(root, lbl_text= self.title1_text, font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=self.title1_placement)
        self.title2_LBL = self.create_text_LBL(root, lbl_text= "Partitioned Allocation", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(355, 65))
        self.title3_LBL = self.create_text_LBL(root, lbl_text= "Partition Allocation Table", font_label=('Times New Roman', 20), bg_clr="#0096FF", placement=(345, 120))
        

        if self.time_type == "After":
            self.title4_LBL = self.create_text_LBL(root, lbl_text= f"{str(self.time_type)} {str(self.time)}, {str(self.text_title)}", font_label=('Times New Roman', 12), bg_clr="#0096FF", placement=(392, 150))
        else:
            self.title4_LBL = self.create_text_LBL(root, lbl_text= f"{str(self.time_type)} {str(self.time)}, {str(self.text_title)}", font_label=('Times New Roman', 12), bg_clr="#0096FF", placement=(417, 150))
        
        # Partition labels
        self.partition_LBL = self.create_text_LBL(root, lbl_text= "Partition", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(90, 180))

        self.partition1_LBL = self.create_text_LBL(root, lbl_text= "1", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(120, 240))
        self.partition2_LBL = self.create_text_LBL(root, lbl_text= "2", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(120, 300))
        self.partition3_LBL = self.create_text_LBL(root, lbl_text= "3", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(120, 360))
        self.partition4_LBL = self.create_text_LBL(root, lbl_text= "4", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(120, 420))
        self.partition5_LBL = self.create_text_LBL(root, lbl_text= "5", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(120, 480))

        # Partition Size Entries
        self.partition_size_LBL = self.create_text_LBL(root, lbl_text= "Partition Size", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(235, 180))

        self.partition_size1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(225, 240), state="readonly", text=partition1 )
        self.partition_size2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(225, 300), state="readonly", text=partition2 )
        self.partition_size3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(225, 360), state="readonly", text=partition3 )
        self.partition_size4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(225, 420), state="readonly", text=partition4 )
        self.partition_size5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(225, 480), state="readonly", text=partition5 )

        # Location Entries
        self.location_LBL = self.create_text_LBL(root, lbl_text= "Location", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(520, 180))

        self.location1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(490, 240), state="readonly", text=int(os_size) )
        self.location2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(490, 300), state="readonly", text=int(os_size) + int(partition1) )
        self.location3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(490, 360), state="readonly", text=int(os_size) + int(partition1) + int(partition2) )
        self.location4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(490, 420), state="readonly", text=int(os_size) + int(partition1) + int(partition2) + int(partition3) )
        self.location5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(490, 480), state="readonly", text=int(os_size) + int(partition1) + int(partition2) + int(partition3) + int(partition4) )

        # Status Entries
        self.statusLBL = self.create_text_LBL(root, lbl_text= "Status", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(740, 180))

        self.status1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(700, 240), state="readonly", text=self.data[0] )
        self.status2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(700, 300), state="readonly", text=self.data[1] )
        self.status3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(700, 360), state="readonly", text=self.data[2] )
        self.status4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(700, 420), state="readonly", text=self.data[3] )
        self.status5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(700, 480), state="readonly", text=self.data[4] )
        
        # Buttons
        self.back_BTN  =  self.create_text_BTN(root, text_label= 'BACK', execute_cmd= self.mem_map_window, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(200, 530))

        if self.next_pointer == None:
            self.next_BTN  =  self.create_text_BTN(root, text_label= 'TRY NEW INPUT', execute_cmd= self.pat_next_BTN_Pressed, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(580, 530))
        else:
            self.next_BTN  =  self.create_text_BTN(root, text_label= 'NEXT', execute_cmd= self.pat_next_BTN_Pressed, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(580, 530))
        
        self.exit_BTN  =  self.create_text_BTN(root, text_label= 'EXIT', execute_cmd= root.destroy, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(390, 530))
        #self.all_job_results = [ [ start_time, finish_time, cpu_wait, partition_location ] ]


class Static_First_Fit(Frontend_Functions, Frontend_Functions2, Backend_Functions):
    def __init__ ( self ):
        super().__init__()
        self.head_node = None

        self.title1_text = "Static First Fit"
        self.title1_placement = (400, 20)


    # This function is for setting partitions
    def main_input1_set_partition_BTN_Pressed ( self ):

        global partition1
        global partition2
        global partition3
        global partition4
        global partition5
        global partition_sizes

        global os_size
        global memory_size

        global size1
        global size2
        global size3
        global size4
        global size5
        global job_sizes

        global os_percentage
        global partition1_percentage
        global partition2_percentage
        global partition3_percentage
        global partition4_percentage
        global partition5_percentage
        global all_partition_percentage
        if messagebox.askyesno( "Confirmation..." , " Are you sure you want to set partition? " ) == True :
            #self.nextAvailable = False
            partition1 = self.partition1_ENTRY.get()
            partition2 = self.partition2_ENTRY.get()
            partition3 = self.partition3_ENTRY.get()
            partition4 = self.partition4_ENTRY.get()
            partition5 = self.partition5_ENTRY.get()

            self.partition1_CHECK = self.is_not_integer( partition1 )
            self.partition2_CHECK = self.is_not_integer( partition2 )
            self.partition3_CHECK = self.is_not_integer( partition3 )
            self.partition4_CHECK = self.is_not_integer( partition4 )
            self.partition5_CHECK = self.is_not_integer( partition5 )

            memory_size = self.memory_size_entry.get()
            os_size = self.os_size_entry.get()

            self.memory_size_CHECK = self.is_not_integer( memory_size )
            self.os_size_CHECK = self.is_not_integer( os_size )

            self.totalSize = 0

            try:
                self.totalSize = int(partition1) + int(partition2) + int(partition3) + int(partition4) + int(partition5) + int(os_size)
            except:
                pass

            if self.memory_size_CHECK or self.os_size_CHECK :
                #print ( "Error: Invalid Memory or OS Size input." )
                messagebox.showinfo( "Partition Error" , "Error: Invalid Memory or OS Size input." )
            elif int(memory_size) < int(os_size):
                ##print ( "ting" )
                #print ( " Error: Os Size can't exceed Memory Size. " )
                messagebox.showinfo( "Partition Error" , "Error: Os Size can't exceed Memory Size." )
            elif self.partition1_CHECK or self.partition2_CHECK or self.partition3_CHECK or self.partition4_CHECK or self.partition5_CHECK:
                #print ( "Error: Partition Size input." )
                messagebox.showinfo( "Partition Error" , "Error: Partition Size input." )
            elif int(self.totalSize) > int(memory_size):
                #print ( "Error: Total taken size exceeded Memory Size." )
                messagebox.showinfo( "Partition Error" , "Error: Total taken size exceeded Memory Size." )
            elif int(self.totalSize) != int(memory_size):
                #print ( "Error: Total taken size must be equal to Memory Size." )
                messagebox.showinfo( "Partition Error" , "Error: Total taken size must be equal to Memory Size." )
            else:
                self.clear_widget_list( self.phys_mem_widgets )
                self.phys_mem_widgets = []
                
                os_percentage = float(( float(os_size) / float(memory_size) ) * 100 )
                partition1_percentage = float(( float(partition1) / float(memory_size) ) * 100 )
                partition2_percentage = float(( float(partition2) / float(memory_size) ) * 100 )
                partition3_percentage = float(( float(partition3) / float(memory_size) ) * 100 )
                partition4_percentage = float(( float(partition4) / float(memory_size) ) * 100 )
                partition5_percentage = float(( float(partition5) / float(memory_size) ) * 100 )


                all_partition_percentage = [ partition1_percentage,
                                           partition2_percentage,
                                           partition3_percentage,
                                           partition4_percentage,
                                           partition5_percentage ]

                self.y_counter = 160
                self.index_pointer = 0
        
                self.mark_LBL  =  Label( root , text = 0 , font = ('Times New Roman', 10),  bg = "#0096FF")
                self.mark_LBL.place(x = 60, y = self.y_counter - 20)
                self.phys_mem_widgets.append( self.mark_LBL )

                self.temp_total_size = int(os_size)
                self.display_map( os_percentage, "#f5f3ed", "Os Size", os_percentage, self.temp_total_size )
                
                self.temp_total_size = int(os_size) + int(partition1) 
                self.display_map( partition1_percentage, "#f77777", "Partition 1", partition1_percentage, self.temp_total_size )
                
                self.temp_total_size = int(os_size) + int(partition1) + int(partition2)
                self.display_map( partition2_percentage, "#f7d977", "Partition 2", partition2_percentage, self.temp_total_size )

                self.temp_total_size = int(os_size) + int(partition1) + int(partition2) + int(partition3)
                self.display_map( partition3_percentage, "#77f7e6", "Partition 3", partition3_percentage, self.temp_total_size )

                self.temp_total_size = int(os_size) + int(partition1) + int(partition2) + int(partition3) + int(partition4)
                self.display_map( partition4_percentage, "#77d5f7", "Partition 4", partition4_percentage, self.temp_total_size )

                self.temp_total_size = int(os_size) + int(partition1) + int(partition2) + int(partition3) + int(partition4) + int(partition5)
                self.display_map( partition5_percentage, "#d577f7", "Partition 5", partition5_percentage, self.temp_total_size )

                #self.nextAvailable = True
                partition1 = int(partition1)
                partition2 = int(partition2)
                partition3 = int(partition3)
                partition4 = int(partition4)
                partition5 = int(partition5)
                partition_sizes = [ partition1, partition2, partition3, partition4, partition5 ]
                ##print( partition_sizes )
                messagebox.showinfo( "Partition Success" , "The partitions has been set." )


    # This function checks if the user is eligible to continue into the next window
    def main_input1_next_BTN_Pressed ( self ):
        if messagebox.askyesno( "Confirmation..." , " Are you sure you want to move on? " ) == True :
            if self.nextAvailable == True:
                self.main_input2_window()
            else:
                #print ( "Error: Please make sure that you've correctly set the partition." )
                messagebox.showinfo( "Partition Error" , "Error: Please make sure that you've correctly set the partition." )

    def main_menu_BTN_pressed( self ):
        main_program.main_menu_window()

        

    # For taking user's input of partitions
    def main_input1_window( self ):
        root.title ( "Static First Fit Partitioned Allocation" )
        self.clear_widgets()
        self.basic_widget_list = []
        self.nextAvailable = True

        self.single_contigious_BG = self.create_BG(root, spa_bg, bg_clr="black", placement=(0, 0))

        self.create_clock(date_placement= (170, 50), clock_placement= (700, 50), bg_clr= "#D3BAF4")

        self.title1_LBL = self.create_text_LBL(root, lbl_text= self.title1_text, font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=self.title1_placement)
        self.title2_LBL = self.create_text_LBL(root, lbl_text= "Partitioned Allocation", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(355, 65))
        self.title3_LBL = self.create_text_LBL(root, lbl_text= "Partition Set", font_label=('Times New Roman', 20), bg_clr="#0096FF", placement=(140, 135))
        
        ##
        self.phys_mem_widgets = []
        self.y_counter = 160
        self.index_pointer = 0
        
        self.mark_LBL = self.create_text_LBL(root, lbl_text= "0", font_label=('Times New Roman', 10), bg_clr="#0096FF", placement=(530, self.y_counter - 20))

        self.temp_total_size = int(os_size)
        self.display_map( os_percentage, "#f5f3ed", "Os Size", os_percentage, self.temp_total_size )
                
        self.temp_total_size = int(os_size) + int(partition1) 
        self.display_map( partition1_percentage, "#f77777", "Partition 1", partition1_percentage, self.temp_total_size, label_height = 5)
                
        self.temp_total_size = int(os_size) + int(partition1) + int(partition2)
        self.display_map( partition2_percentage, "#f7d977", "Partition 2", partition2_percentage, self.temp_total_size, label_height = 5 )

        self.temp_total_size = int(os_size) + int(partition1) + int(partition2) + int(partition3)
        self.display_map( partition3_percentage, "#77f7e6", "Partition 3", partition3_percentage, self.temp_total_size, label_height = 5 )

        self.temp_total_size = int(os_size) + int(partition1) + int(partition2) + int(partition3) + int(partition4)
        self.display_map( partition4_percentage, "#77d5f7", "Partition 4", partition4_percentage, self.temp_total_size, label_height = 5 )

        self.temp_total_size = int(os_size) + int(partition1) + int(partition2) + int(partition3) + int(partition4) + int(partition5)
        self.display_map( partition5_percentage, "#d577f7", "Partition 5", partition5_percentage, self.temp_total_size, label_height = 5 )
        
        ##
        self.os_size_LBL = self.create_text_LBL(root, lbl_text= "OS Size", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(310, 450))
        self.os_size_entry = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                             placement=(270, 490), state="normal", text=312)

        
        self.memory_size_LBL = self.create_text_LBL(root, lbl_text="Memory Size", font_label=('Times New Roman', 15),
                                         bg_clr="#0096FF", placement=(90, 450))
        self.memory_size_entry = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(70, 490), state="normal", text=1024)

        self.partition1_LBL = self.create_text_LBL(root, lbl_text= "Parition 1", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(70, 200))
        self.partition1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(200, 202), state="normal", text=8)

        self.partition2_LBL = self.create_text_LBL(root, lbl_text= "Parition 2", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(70, 240))
        self.partition2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(200, 242), state="normal", text=32)
        
        self.partition3_LBL = self.create_text_LBL(root, lbl_text= "Parition 3", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(70, 280))
        self.partition3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(200, 282), state="normal", text=32)

        self.partition4_LBL = self.create_text_LBL(root, lbl_text= "Parition 4", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(70, 320))
        self.partition4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(200, 322), state="normal", text=120)

        self.partition5_LBL = self.create_text_LBL(root, lbl_text= "Parition 5", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(70, 360))
        self.partition5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(200, 362), state="normal", text=520)

        self.set_partition_BTN  =  self.create_text_BTN(root, text_label= 'Set Partition', execute_cmd= self.main_input1_set_partition_BTN_Pressed, font_label=('Consolas', 10, 'bold'), width_label=13, bg_clr="#B3B3B3", placement=(200, 405))
        self.next_BTN  =  self.create_text_BTN(root, text_label= 'Next', execute_cmd= self.main_input1_next_BTN_Pressed, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(390, 550))
        self.exit_BTN  =  self.create_text_BTN(root, text_label= 'Exit', execute_cmd= root.destroy, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(190, 550))
        self.main_menu_BTN = self.create_text_BTN(root, text_label= 'Menu', execute_cmd= self.main_menu_BTN_pressed, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(590, 550))


    # Generates the result windows using the help of the Node class.
    # This makes use of linked list
    # The start/top of the linked list is referenced at self.head_node
    def create_result_windows( self, all_job_sizes, all_job_arrival_time, all_job_run_time, all_partition_sizes):
        global partition1
        global partition2
        global partition3
        global partition4
        global partition5
        global partition_sizes

        global os_size
        global memory_size

        global size1
        global size2
        global size3
        global size4
        global size5
        global job_sizes

        global os_percentage
        global partition1_percentage
        global partition2_percentage
        global partition3_percentage
        global partition4_percentage
        global partition5_percentage
        global all_partition_percentage
        
        self.clear_nodes()
        job_sizes = all_job_sizes
        #print( job_sizes )
        self.all_job_arrival_time = all_job_arrival_time
        self.all_job_run_time = all_job_run_time
        partition_sizes = all_partition_sizes
        #print( "Create Result Windows" , partition_sizes )
        self.partitionState = [ False, False, False, False, False]
        self.job_state = [ False, False, False, False, False]
        self.partition_history = [ [], [], [], [], [] ]
        self.time_zero = datetime.datetime.strptime('00:00', '%H:%M')
        self.all_job_results = [ [], [], [], [], [] ]
        self.pat_status1 = [ ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"]]
        self.pat_status2 = [ ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"]]
        self.all_start_time = []
        self.all_finish_time = []

        # Allocate jobs to partitions using First Fit
        for i in range( 5 ):
            for j in range( 5 ):
                if int(partition_sizes[j]) >= int(job_sizes[i]) and self.partitionState[j] == False:
                    # Allocate job to partition
                    self.partitionState[j] = True
                    self.job_state[i] = True

                    # Calculate start time based on previous partition history
                    if len(self.partition_history[j]) == 0:
                        self.temp_start_time = datetime.datetime.strptime( self.all_job_arrival_time[i] , '%H:%M')
                    else:
                        self.temp_start_time = self.partition_history[j][-1]

                    # Calculate CPU wait time
                    if (self.temp_start_time - datetime.datetime.strptime( self.all_job_arrival_time[i], '%H:%M')).total_seconds() < 0:
                        self.temp_cpu_wait = "0:00:00"
                        self.temp_start_time = datetime.datetime.strptime( self.all_job_arrival_time[i], '%H:%M')
                    else:
                        self.temp_cpu_wait = self.temp_start_time - datetime.datetime.strptime( self.all_job_arrival_time[i], '%H:%M')
                    
                    # Store start time and other details in job results
                    self.all_start_time.append( self.temp_start_time.time() )
                    self.all_job_results[i].append( self.temp_start_time )

                     # Calculate finish time and store in job results and partition history
                    self.temp_finish_time = ( self.temp_start_time - self.time_zero + (datetime.datetime.strptime(self.all_job_run_time[i], '%H:%M')))
                    self.all_finish_time.append( self.temp_finish_time.time() )
                    self.partition_history[j].append( self.temp_finish_time )
                    self.all_job_results[i].append( self.temp_finish_time )

                    # Store CPU wait time and other details in job results
                    self.all_job_results[i].append( self.temp_cpu_wait )

                    self.all_job_results[i].append( j )
                    self.all_job_results[i].append( i )
                    self.all_job_results[i].append( "After" )
                    
                    # Mark as allocated and break inner loop
                    self.tempIsAllocated = True
                    #print( "compare: ", int(partition_sizes[j]), int(job_sizes[i]) )
                    break
                    
        # If a job couldn't be allocated using First Fit, try allocating it to any partition
        for i in range( 5 ):
            if self.job_state[i] == False:
                for j in range( 5 ):
                    if int(partition_sizes[j]) >= int(job_sizes[i]):
                        self.partitionState[j] = True
                        self.job_state[i] = True
                        #print( self.partitionState )

                        if len(self.partition_history[j]) == 0:
                            self.temp_start_time = datetime.datetime.strptime( self.all_job_arrival_time[i] , '%H:%M')
                        else:
                            self.temp_start_time = self.partition_history[j][-1]

                        if (self.temp_start_time - datetime.datetime.strptime( self.all_job_arrival_time[i], '%H:%M')).total_seconds() < 0:
                            self.temp_cpu_wait = "0:00:00"
                            self.temp_start_time = datetime.datetime.strptime( self.all_job_arrival_time[i], '%H:%M')
                        else:
                            self.temp_cpu_wait = self.temp_start_time - datetime.datetime.strptime( self.all_job_arrival_time[i], '%H:%M')
                        self.all_start_time.append( self.temp_start_time.time() )
                        self.all_job_results[i].append( self.temp_start_time )

                        self.temp_finish_time = ( self.temp_start_time - self.time_zero + (datetime.datetime.strptime(self.all_job_run_time[i], '%H:%M')))
                        self.all_finish_time.append( self.temp_finish_time.time() )
                        self.partition_history[j].append( self.temp_finish_time )
                        self.all_job_results[i].append( self.temp_finish_time )

                        self.all_job_results[i].append( self.temp_cpu_wait )
                        
                        #print( "compare: ", int(partition_sizes[j]), int(job_sizes[i]) )
                        self.all_job_results[i].append( j )
                        self.all_job_results[i].append( i )
                        self.all_job_results[i].append( "After" )

                        #self.all_job_results = [ [ start_time, finish_time, cpu_wait, partition_location, job num, before/after ] ]
                        break
        #print( self.job_state )

        # is_time_between(self, begin_time, end_time, check_time=None):


        for i in range( 5 ):
            self.temp_check_time = self.all_job_results[i][0]
            self.temp_check_time2 = self.all_job_results[i][1] + datetime.timedelta( seconds = 1)
            for j in range( 5 ):
                self.temp_begin_time = self.all_job_results[j][0]
                self.temp_end_time = self.all_job_results[j][1]
                
                self.temp_status = self.is_time_between( self.temp_begin_time, self.temp_end_time, self.temp_check_time )
                self.temp_status2 = self.is_time_between( self.temp_begin_time, self.temp_end_time, self.temp_check_time2 )
                if self.temp_status == True:
                    #print ( "X", self.temp_begin_time, self.temp_end_time, self.temp_check_time )
                    #print( self.all_job_results[j][3] , self.all_job_results[j][4] )
                    self.pat_status1[i][self.all_job_results[j][3]] = "Allocated(J{})".format(self.all_job_results[j][4] + 1)
                if self.temp_status2 == True:
                    self.pat_status2[i][self.all_job_results[j][3]] = "Allocated(J{})".format(self.all_job_results[j][4] + 1)          
        for x in self.all_job_results:
            for xx in x:
                pass
                #print( xx )


        self.add_result_node( self.all_finish_time[4], self.pat_status2[4], "After", "J5 Terminated" )
        self.add_result_node( self.all_start_time[4], self.pat_status1[4], "At", "J5 Started" )

        self.add_result_node( self.all_finish_time[3], self.pat_status2[3], "After", "J4 Terminated" )
        self.add_result_node( self.all_start_time[3], self.pat_status1[3], "At", "J4 Started" )

        self.add_result_node( self.all_finish_time[2], self.pat_status2[2], "After", "J3 Terminated" )
        self.add_result_node( self.all_start_time[2], self.pat_status1[2], "At", "J3 Started" )

        self.add_result_node( self.all_finish_time[1], self.pat_status2[1], "After", "J2 Terminated" )
        self.add_result_node( self.all_start_time[1], self.pat_status1[1], "At", "J2 Started" )

        self.add_result_node( self.all_finish_time[0], self.pat_status2[0], "After", "J1 Terminated" )
        self.add_result_node( self.all_start_time[0], self.pat_status1[0], "At", "J1 Started" )
        
        self.main_result1_window()


    # This function is for most of the necessary computations
    def main_input2_computePressed( self ):
        global partition1
        global partition2
        global partition3
        global partition4
        global partition5
        global partition_sizes

        global os_size
        global memory_size

        global size1
        global size2
        global size3
        global size4
        global size5
        global job_sizes

        global os_percentage
        global partition1_percentage
        global partition2_percentage
        global partition3_percentage
        global partition4_percentage
        global partition5_percentage
        global all_partition_percentage
        if messagebox.askyesno( "Confirmation..." , " Are you sure you want to compute? " ) == True :
            size1 = self.size1_ENTRY.get()
            size2 = self.size2_ENTRY.get()
            size3 = self.size3_ENTRY.get()
            size4 = self.size4_ENTRY.get()
            size5 = self.size5_ENTRY.get()

            #print ( "Main Input2" , partition_sizes )
 
            self.size1_CHECK = self.is_not_integer( size1 )
            self.size2_CHECK = self.is_not_integer( size2 )
            self.size3_CHECK = self.is_not_integer( size3 )
            self.size4_CHECK = self.is_not_integer( size4 )
            self.size5_CHECK = self.is_not_integer( size5 )

            self.size1_CHECK2 = self.cant_fit_in_partition( size1 )
            self.size2_CHECK2 = self.cant_fit_in_partition( size2 )
            self.size3_CHECK2 = self.cant_fit_in_partition( size3 )
            self.size4_CHECK2 = self.cant_fit_in_partition( size4 )
            self.size5_CHECK2 = self.cant_fit_in_partition( size5 )
            
            
            self.arrival_time1 = self.arrival_time1_ENTRY.get()
            self.arrival_time2 = self.arrival_time2_ENTRY.get()
            self.arrival_time3 = self.arrival_time3_ENTRY.get()
            self.arrival_time4 = self.arrival_time4_ENTRY.get()
            self.arrival_time5 = self.arrival_time5_ENTRY.get()

            self.arrival_time1_CHECK = self.is_not_time_format( self.arrival_time1 )
            self.arrival_time2_CHECK = self.is_not_time_format( self.arrival_time2 )
            self.arrival_time3_CHECK = self.is_not_time_format( self.arrival_time3 )
            self.arrival_time4_CHECK = self.is_not_time_format( self.arrival_time4 )
            self.arrival_time5_CHECK = self.is_not_time_format( self.arrival_time5 )

            self.run_time1 = self.run_time1_ENTRY.get()
            self.run_time2 = self.run_time2_ENTRY.get()
            self.run_time3 = self.run_time3_ENTRY.get()
            self.run_time4 = self.run_time4_ENTRY.get()
            self.run_time5 = self.run_time5_ENTRY.get()
        
            self.run_time1_CHECK = self.is_not_time_format( self.run_time1 )
            self.run_time2_CHECK = self.is_not_time_format( self.run_time2 )
            self.run_time3_CHECK = self.is_not_time_format( self.run_time3 )
            self.run_time4_CHECK = self.is_not_time_format( self.run_time4 )
            self.run_time5_CHECK = self.is_not_time_format( self.run_time5 )

            if self.size1_CHECK or self.size2_CHECK or self.size3_CHECK or self.size4_CHECK or self.size5_CHECK:
                #print ( "Error: Size input detected as not an integer." )
                messagebox.showinfo( "Compute Error" , "Error: Size input detected as not an integer." )
            elif self.size1_CHECK2:
                #print ( "Error: Size 1 input can't fit in any partition." )
                messagebox.showinfo( "Compute Error" , "Error: Size 1 input can't fit in any partition." )
            elif self.size2_CHECK2:
                #print ( "Error: Size 2 input can't fit in any partition." )
                messagebox.showinfo( "Compute Error" , "Error: Size 2 input can't fit in any partition." )
            elif self.size3_CHECK2:
                #print ( "Error: Size 3 input can't fit in any partition." )
                messagebox.showinfo( "Compute Error" , "Error: Size 3 input can't fit in any partition." )
            elif self.size4_CHECK2:
                #print ( "Error: Size 4 input can't fit in any partition." )
                messagebox.showinfo( "Compute Error" , "Error: Size 4 input can't fit in any partition." )
            elif self.size5_CHECK2:
                #print ( "Error: Size 5 input can't fit in any partition." )
                messagebox.showinfo( "Compute Error" , "Error: Size 5 input can't fit in any partition." )
            elif self.arrival_time1_CHECK or self.arrival_time2_CHECK or self.arrival_time3_CHECK or self.arrival_time4_CHECK or self.arrival_time5_CHECK:
                #print ( " Error in arrival time input " )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Arrival Time Input." )
            elif self.run_time1_CHECK or self.run_time2_CHECK or self.run_time3_CHECK or self.run_time4_CHECK or self.run_time5_CHECK:
                #print ( "Error: Invalid Run Time Input." )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Run Time Input." )
            else:
                size1 = int(size1)
                size2 = int(size2)
                size3 = int(size3)
                size4 = int(size4)
                size5 = int(size5)
                job_sizes = [ size1, size2, size3, size4, size5 ]
                #print( job_sizes )
                self.all_job_arrival_time = [ self.arrival_time1, self.arrival_time2, self.arrival_time3, self.arrival_time4, self.arrival_time5 ]
                self.all_job_run_time = [ self.run_time1, self.run_time2, self.run_time3, self.run_time4, self.run_time5 ]
                self.create_result_windows( job_sizes, self.all_job_arrival_time, self.all_job_run_time, partition_sizes )
                #print( "success" )


    # For taking user's input of each job's information
    def main_input2_window ( self ):
        self.clear_widgets()
        self.basic_widget_list = []

        self.static_first_fit_BG = self.create_BG(root, spa_bg, bg_clr="black", placement=(0, 0))
        self.create_clock(date_placement= (170, 50), clock_placement= (700, 50), bg_clr= "#D3BAF4")

        self.title1_LBL = self.create_text_LBL(root, lbl_text= self.title1_text, font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=self.title1_placement)
        self.title2_LBL = self.create_text_LBL(root, lbl_text= "Partitioned Allocation", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(355, 65))
        self.title3_LBL = self.create_text_LBL(root, lbl_text= "Input Window", font_label=('Times New Roman', 30), bg_clr="#0096FF", placement=(355, 155))

        self.job_LBL = self.create_text_LBL(root, lbl_text= "Job", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(125, 210))
        self.job1_LBL = self.create_text_LBL(root, lbl_text= "1", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 260))
        self.job2_LBL = self.create_text_LBL(root, lbl_text= "2", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 310))
        self.job3_LBL = self.create_text_LBL(root, lbl_text= "3", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 360))
        self.job4_LBL = self.create_text_LBL(root, lbl_text= "4", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 410))
        self.job5_LBL = self.create_text_LBL(root, lbl_text= "5", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 460))

        self.size_LBL = self.create_text_LBL(root, lbl_text= "Size", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(275, 210))
        self.size1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(225, 260), justify="center")
        self.size2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(225, 310), justify="center")
        self.size3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(225, 360), justify="center")
        self.size4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(225, 410), justify="center")
        self.size5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(225, 460), justify="center")

        self.arrival_time_LBL  = self.create_text_LBL(root, lbl_text= "Arrival Time", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(505, 210))
        self.arrival_time1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(490, 260), justify="center")
        self.arrival_time2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(490, 310), justify="center")
        self.arrival_time3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(490, 360), justify="center")
        self.arrival_time4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(490, 410), justify="center")
        self.arrival_time5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(490, 460), justify="center")

        self.run_time_LBL  = self.create_text_LBL(root, lbl_text= "Run Time", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(725, 210))
        self.run_time1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(700, 260), justify="center")
        self.run_time2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(700, 310), justify="center")
        self.run_time3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(700, 360), justify="center")
        self.run_time4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(700, 410), justify="center")
        self.run_time5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(700, 460), justify="center")

        self.exit_BTN  =  self.create_text_BTN(root, text_label= 'Exit', execute_cmd= root.destroy, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(190, 510))
        self.compute_BTN  =  self.create_text_BTN(root, text_label= 'Compute', execute_cmd= self.main_input2_computePressed, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(390, 510))
        self.back_BTN  =  self.create_text_BTN(root, text_label= 'Back', execute_cmd= self.main_input1_window, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(590, 510))


    # This function points to the head_node's mem_map_window
    def main_result1_next_BTN_Pressed( self ):
        if self.head_node != None:
            self.head_node.mem_map_window()


    # For displaying the summary table
    def main_result1_window( self ):
        self.clear_widgets()
        self.basic_widget_list = []

        self.static_first_fit_BG = self.create_BG(root, spa_bg, bg_clr="black", placement=(0, 0))
        
        self.create_clock(date_placement= (170, 50), clock_placement= (700, 50), bg_clr= "#D3BAF4")

        self.title1_LBL = self.create_text_LBL(root, lbl_text= self.title1_text, font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=self.title1_placement)
        self.title2_LBL = self.create_text_LBL(root, lbl_text= "Partitioned Allocation", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(355, 65))
        
        # Job labels
        self.job_LBL = self.create_text_LBL(root, lbl_text= "Job", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(112, 130))
        self.job1_LBL = self.create_text_LBL(root, lbl_text= "1", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(120, 190))
        self.job2_LBL = self.create_text_LBL(root, lbl_text= "2", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(120, 250))
        self.job3_LBL = self.create_text_LBL(root, lbl_text= "3", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(120, 310))
        self.job4_LBL = self.create_text_LBL(root, lbl_text= "4", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(120, 370))
        self.job5_LBL = self.create_text_LBL(root, lbl_text= "5", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(120, 430))

        # Start Time Entries
        self.start_time_LBL = self.create_text_LBL(root, lbl_text= "Start Time", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(250, 130))
        self.start_time1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 190), state="readonly", text=self.all_job_results[0][0].time())
        self.start_time2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 250), state="readonly", text=self.all_job_results[1][0].time())
        self.start_time3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 310), state="readonly", text=self.all_job_results[2][0].time())
        self.start_time4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 370), state="readonly", text=self.all_job_results[3][0].time())
        self.start_time5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 430), state="readonly", text=self.all_job_results[4][0].time())

        # Finish Time Entries
        self.finish_time_LBL = self.create_text_LBL(root, lbl_text= "Finish Time", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(512, 130))
        self.finish_time1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 190), state="readonly", text=self.all_job_results[0][1].time())
        self.finish_time2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 250), state="readonly", text=self.all_job_results[1][1].time())
        self.finish_time3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 310), state="readonly", text=self.all_job_results[2][1].time())
        self.finish_time4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 370), state="readonly", text=self.all_job_results[3][1].time())
        self.finish_time5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 430), state="readonly", text=self.all_job_results[4][1].time())

        # CPU Wait Entries
        self.cpu_wait_LBL = self.create_text_LBL(root, lbl_text= "CPU Wait", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(725, 130))
        self.cpu_wait1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 190), state="readonly", text=self.all_job_results[0][2])
        self.cpu_wait2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 250), state="readonly", text=self.all_job_results[1][2])
        self.cpu_wait3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 310), state="readonly", text=self.all_job_results[2][2])
        self.cpu_wait4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 370), state="readonly", text=self.all_job_results[3][2])
        self.cpu_wait5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 430), state="readonly", text=self.all_job_results[4][2])

        self.back_BTN  =  self.create_text_BTN(root, text_label= 'Back', execute_cmd= self.main_input2_window, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(190, 510))
        self.exit_BTN  =  self.create_text_BTN(root, text_label= 'Exit', execute_cmd= root.destroy, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(390, 510))
        self.next_BTN  =  self.create_text_BTN(root, text_label= 'Next', execute_cmd= self.main_result1_next_BTN_Pressed, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(590, 510))
# END OF SPA PROGRAM: line 1340-2838


# DFF PROGRAM: Line 2847-4428
# All the back end processes are hosted in this class.
class Dynamic_First_Fit_Backend:
    def __init__( self ):
        self.time_zero = datetime.datetime.strptime('00:00', '%H:%M')
        # summary table [ job_numberum, start_time, finish_time, cpu_wait ]
        self.summary_table = {}
        self.all_time = []
        
        # Job Status [ allocated(True/False), finished(True/False), waiting ]
        self.job_status = { 1 : [ False, False, False ],
                           2 : [ False, False, False ],
                           3 : [ False, False, False ],
                           4 : [ False, False, False ],
                           5 : [ False, False, False ]}
        self.memory_results = []
        self.memory_results_time = []

    # for taking in the user's input into the Backend class.
    def insert_inputs( self, mem_space, os_space, job_details, memory ):
        #print( "INPUTS: " )
        #print ( "I1" , job_details )
        #print( "I2", memory )
        self.mem_space = int(mem_space)
        self.os_space = int(os_space)
        self.memory_size = int( mem_space)
        self.os_space = int( os_space )
        self.job_details = deepcopy( job_details )
        self.memory = deepcopy( memory )

        self.summary_table = {}
        self.all_time = []
        # generates the all time list which will contain all the time that needs a memory map, fat, and pat.
        for job in self.job_details:
            self.tempTime = datetime.datetime.strptime( job[2], '%H:%M')
            self.all_time.append( self.tempTime )

        # job status [ isJobAllocated, isJobFinished, isjob_waiting ]
        self.job_status = { 1 : [ False, False, False ],
                           2 : [ False, False, False ],
                           3 : [ False, False, False ],
                           4 : [ False, False, False ],
                           5 : [ False, False, False ]}

        # memory_result will be used to store the data for every memory map.
        self.memory_results = []
        # memory_result_time will be used to store the time of every memory map.
        self.memory_results_time = []
        return

    # returns memory list
    def get_memory( self ):
        return self.memory

    # returns summary_table
    def get_summary_table( self ):
        return self.summary_table

    # returns the memory_results
    def get_memory_results( self ):
        return self.memory_results

    # returns the memory_results_time
    def get_memory_results_time( self ):
        return self.memory_results_time

    # for appending a certain memory list into the memory result
    def add_memory_result( self, memory, time, time_status) :
        self.memory_results.append( memory )
        self.memory_results_time.append( [time, time_status] )
        return

    # sorts the list containing all the time that needs a memory result.
    def arrange_all_time( self ):
        self.all_time.sort()
        return

    # remove's the time that already have a memory result.
    def remove_time( self, time ):
        try:
            while True:
                self.all_time.remove(time)
        except ValueError:
            pass
        self.arrange_all_time()
        return

    # checks if the job fits into the available partitions.
    def check_job_fit( self, j_size ):
        # j_size: job size
        self.j_size = j_size
        # memorySpace[1]: F for free/available space and U if occupied by a certain job
        # memorySpace[0]: the size of the partition.
        for memorySpace in self.memory:
            if memorySpace[1] == "F" and memorySpace[0] > self.j_size:
                return True
        return False

    # checks a certain job's status.
    def check_job_status( self ):
        # checks if the jobs are already done.
        self.jobsDone = 0
        for job_numberum in list(self.job_status):
            if self.job_status[job_numberum][0] == True and self.job_status[job_numberum][1]:
                self.jobsDone += 1
        if self.jobsDone == len( list(self.job_status) ):
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
    def generate_summary_table( self ):
        self.is_finished = False
        self.arrange_all_time()
        
        while self.is_finished == False:
            # This block of code sets the needed parameters for the next process.
            # It resets the indicator 'action_taken'. This indicator is used by the
            # program to determine if a job has been allocated/de-allocated in this iteration.
            # temp_time_status: contains the status of certain time periods. This could contain
            #                 job arrivals, job waiting, and job terminations.
            # current_time: the time of a certain/this iteration.
            self.action_taken = False
            self.temp_time_status = []
            try:
                self.arrange_all_time()
                self.current_time = self.all_time[0]
            except:
                self.is_finished = True
                break

            # Checks if all the jobs are already finished. If it is, then stop the while loop.
            self.temp_job_status = self.check_job_status()
            if self.temp_job_status == True:
                self.is_finished = True
                break

            # Iterates through the job details to see what actions can be taken in this current_time
            for job in self.job_details:
                self.job_fits = self.check_job_fit( job[0] )
                self.test_job_waiting = True
                
                # If a certain job details from the self.job_details is deemed to waiting to be allocated
                # then, it will check if the current_time meets the job's demand for allocation.
                if job[4] != False:
                    self.temp_wait_until = job[4]
                    if self.current_time == self.temp_wait_until:
                        self.test_job_waiting = False

                # If a certain job arrives, this nested condition will check whether the job needs to wait or is capable
                # of immediate allocation.
                if self.current_time == datetime.datetime.strptime( job[2], '%H:%M') and self.job_status[job[1]][0] == False:
                    if self.job_fits == True:
                        self.temp_time_status.append( "Arrived(J{})".format( job[1] ) )
                    else:
                        self.temp_time_status.append( "Arrived/Wait(J{})".format( job[1] ) )
                        self.temp_wait_until = self.temp_finish_time
                        job[4] = self.temp_wait_until

                # This conditions checks if a certain actions could be taken.
                # The actions could be, the start/allocation or termination of certain job.
                if ( self.test_job_waiting == False or self.current_time == datetime.datetime.strptime( job[2], '%H:%M')) and self.job_status[job[1]][0] == False and self.job_fits == True:
                    self.memory = self.allocate( self.memory, [ job[1], "a" , job[0] ] )
                    self.job_status[job[1]][0] = True

                    self.temp_start_time = self.current_time
                    if (self.temp_start_time - datetime.datetime.strptime( job[2], '%H:%M')).total_seconds() < 0:
                        self.temp_cpu_wait = "0:00:00"
                        self.temp_start_time = datetime.datetime.strptime( job[2], '%H:%M')
                    else:
                        self.temp_cpu_wait = self.temp_start_time - datetime.datetime.strptime( job[2], '%H:%M')
                    self.temp_finish_time = ( self.temp_start_time - self.time_zero + (datetime.datetime.strptime( job[3], '%H:%M')))
                    self.all_time.append( self.temp_finish_time )
                    self.summary_table[job[1]] = [ job[1], self.temp_start_time, self.temp_finish_time, self.temp_cpu_wait ]

                    self.action_taken = True
                    self.temp_time_status.append( "Started(J{})".format( job[1] ) )
                elif self.job_status[job[1]][0] == True and self.current_time == self.summary_table[job[1]][2]:
                    self.memory = self.recycle( self.memory, [ job[1], "f" , job[0] ] )
                    self.job_status[job[1]][1] = True
                    
                    self.action_taken = True
                    self.temp_time_status.append( "Terminated(J{})".format( job[1] ) )
                else:
                    pass

            # copies the memory list of this current_time
            self.memory_to_add = deepcopy(self.memory)
            # appds the needed data into the memory_result list.
            self.add_memory_result( self.memory_to_add, self.current_time, deepcopy(self.temp_time_status) )

            # Checks if all the job are already finished. If not, then remove the current time from
            # the list of all time.
            self.temp_job_status = self.check_job_status()
            if self.temp_job_status == True:
                self.is_finished = True
                break
            else:
                self.remove_time( self.current_time )


# Contains all the front end windows and functions
class Dynamic_First_Fit_Frontend(Frontend_Functions, Frontend_Functions2, Backend_Functions):
    def __init__( self ):
        super().__init__()
        self.mem_space = 640
        self.memory_size = 640
        self.os_space = 32
        self.os_size = 32
        # Job Details [ job_size, job_numberum, arrival_time, run_time, isjob_waiting ]
        self.job_details = [ [ 10, 1, "9:00", "1:00", False],
                            [ 20, 2, "9:00", "1:00", False],
                            [ 30, 3, "9:00", "1:00", False],
                            [ 40, 4, "9:00", "1:00", False],
                            [ 50, 5, "9:00", "1:00", False]]

        self.memory = [[609,'F',-1]]
        
        self.dynamic_first_fit_backend = Dynamic_First_Fit_Backend()

        # insert_inputs( self, mem_space, os_space, job_details, memory )
        self.dynamic_first_fit_backend.insert_inputs( self.mem_space, self.os_space, self.job_details, self.memory )
        self.dynamic_first_fit_backend.generate_summary_table()

        self.head_node = None


    # To add a node into the linked list
    # ( self, memory_result = None, memory_result_time = None, os_size = None, memory_size = None)
    def add_result_node( self, memory_result, memory_result_time, os_size, memory_size ):
        memory_result_time[0] = memory_result_time[0].time()
        self.temp_node = Dynamic_First_Fit_Node( memory_result, memory_result_time, os_size, memory_size )

        if self.head_node == None:
            self.head_node = self.temp_node
        else:
            self.head_node.back_pointer = self.temp_node
            self.temp_node.next_pointer = self.head_node

            self.head_node = self.temp_node
        return

    def main_menu_BTN_pressed( self ):
        main_program.main_menu_window()



    # function which contains widget placements
    # this also takes in the user's input.
    def input1_window( self ):
        root.title ( "Dynamic First Fit" )
        self.clear_widgets()
        self.basic_widget_list = []

        self.dynamicFirstFitBG = self.create_BG(root, dff_bg, bg_clr="black", placement=(0, 0))

        self.create_clock(date_placement= (170, 50), clock_placement= (700, 50), bg_clr= "#D3BAF4")

        self.title1_LBL = self.create_text_LBL(root, lbl_text= "First Fit Dynamic", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(375, 20))
        self.title2_LBL = self.create_text_LBL(root, lbl_text= "Partitioned Allocation", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(345, 65))
        self.title3_LBL = self.create_text_LBL(root, lbl_text= "Input Window", font_label=('Times New Roman', 30), bg_clr="#0096FF", placement=(355, 135))

        # Job labels
        self.job_LBL = self.create_text_LBL(root, lbl_text= "Job", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(125, 180))
        self.job1_LBL = self.create_text_LBL(root, lbl_text= "1", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 230))
        self.job2_LBL = self.create_text_LBL(root, lbl_text= "2", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 280))
        self.job3_LBL = self.create_text_LBL(root, lbl_text= "3", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 330))
        self.job4_LBL = self.create_text_LBL(root, lbl_text= "4", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 380))
        self.job5_LBL = self.create_text_LBL(root, lbl_text= "5", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 440))

        # Size Entries
        self.size_LBL = self.create_text_LBL(root, lbl_text= "Size", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(275, 180))
        self.size1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(225, 230), justify="center")
        self.size2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(225, 280), justify="center")
        self.size3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(225, 330), justify="center")
        self.size4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(225, 380), justify="center")
        self.size5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(225, 440), justify="center")

        # Arrival Time Entries
        self.arrival_time_LBL  = self.create_text_LBL(root, lbl_text= "Arrival Time", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(505, 180))
        self.arrival_time1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(490, 230), justify="center")
        self.arrival_time2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(490, 280), justify="center")
        self.arrival_time3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(490, 330), justify="center")
        self.arrival_time4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(490, 380), justify="center")
        self.arrival_time5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(490, 440), justify="center")

        # Run Time Entries
        self.run_time_LBL  = self.create_text_LBL(root, lbl_text= "Run Time", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(725, 180))
        self.run_time1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(700, 230), justify="center")
        self.run_time2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(700, 280), justify="center")
        self.run_time3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(700, 330), justify="center")
        self.run_time4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(700, 380), justify="center")
        self.run_time5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(700, 440), justify="center")

        # Memory Size Entry
        self.memory_size_LBL  = self.create_text_LBL(root, lbl_text= "Memory Size", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(300, 470))
        self.memory_size_entry = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(280, 520), justify="center")

        # OS Size Entry
        self.os_size_LBL  = self.create_text_LBL(root, lbl_text= "OS Size", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(510, 470))
        self.os_size_entry = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(475, 520), justify="center")

        # Buttons
        self.exit_BTN  =  self.create_text_BTN(root, text_label= 'Exit', execute_cmd= root.destroy, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(190, 550))
        self.compute_BTN  =  self.create_text_BTN(root, text_label= 'Compute', execute_cmd= self.input1_compute_BTN_Pressed, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(390, 550))
        self.main_menu_BTN = self.create_text_BTN(root, text_label= 'Menu', execute_cmd= self.main_menu_BTN_pressed, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(590, 550))


    # Executes once the user presses the compute button in the input1_window
    def input1_compute_BTN_Pressed( self ):
        self.clear_nodes()
        #print( "Head Node: " , self.head_node )
        #print ( "Input1 Compute BTN Pressed " )
        if messagebox.askyesno( "Confirmation..." , " Are you sure you want to compute? " ) == True :
            self.size1 = self.size1_ENTRY.get()
            self.size2 = self.size2_ENTRY.get()
            self.size3 = self.size3_ENTRY.get()
            self.size4 = self.size4_ENTRY.get()
            self.size5 = self.size5_ENTRY.get()

            self.memory_size = self.memory_size_entry.get()
            self.os_size = self.os_size_entry.get()

            self.memory_size_CHECK = self.is_not_integer( self.memory_size )
            self.os_size_CHECK = self.is_not_integer( self.os_size )
 
            self.size1_CHECK = self.is_not_integer( self.size1 )
            self.size2_CHECK = self.is_not_integer( self.size2 )
            self.size3_CHECK = self.is_not_integer( self.size3 )
            self.size4_CHECK = self.is_not_integer( self.size4 )
            self.size5_CHECK = self.is_not_integer( self.size5 )
            
            
            self.arrival_time1 = self.arrival_time1_ENTRY.get()
            self.arrival_time2 = self.arrival_time2_ENTRY.get()
            self.arrival_time3 = self.arrival_time3_ENTRY.get()
            self.arrival_time4 = self.arrival_time4_ENTRY.get()
            self.arrival_time5 = self.arrival_time5_ENTRY.get()

            self.arrival_time1_CHECK = self.is_not_time_format( self.arrival_time1 )
            self.arrival_time2_CHECK = self.is_not_time_format( self.arrival_time2 )
            self.arrival_time3_CHECK = self.is_not_time_format( self.arrival_time3 )
            self.arrival_time4_CHECK = self.is_not_time_format( self.arrival_time4 )
            self.arrival_time5_CHECK = self.is_not_time_format( self.arrival_time5 )

            self.run_time1 = self.run_time1_ENTRY.get()
            self.run_time2 = self.run_time2_ENTRY.get()
            self.run_time3 = self.run_time3_ENTRY.get()
            self.run_time4 = self.run_time4_ENTRY.get()
            self.run_time5 = self.run_time5_ENTRY.get()
        
            self.run_time1_CHECK = self.is_not_time_format( self.run_time1 )
            self.run_time2_CHECK = self.is_not_time_format( self.run_time2 )
            self.run_time3_CHECK = self.is_not_time_format( self.run_time3 )
            self.run_time4_CHECK = self.is_not_time_format( self.run_time4 )
            self.run_time5_CHECK = self.is_not_time_format( self.run_time5 )

            # This condition checks whether the user's inputted values are acceptable.
            # If not, #print the errors.
            if self.memory_size_CHECK or self.os_size_CHECK :
                #print ( "Error: Invalid Memory or OS Size input." )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Memory or OS Size input." )
            elif int(self.memory_size) < int(self.os_size):
                #print ( " Error: Os Size can't exceed Memory Size. " )
                messagebox.showinfo( "Compute Error" , "Error: Os Size can't exceed Memory Size." )
            elif self.size1_CHECK or self.size2_CHECK or self.size3_CHECK or self.size4_CHECK or self.size5_CHECK:
                #print ( "Error: Size input detected as not an integer." )
                messagebox.showinfo( "Compute Error" , "Error: Size input detected as not an integer." )
            elif (int(self.size1) > ( int(self.memory_size) - int(self.os_size))) or (int(self.size2) > ( int(self.memory_size) - int(self.os_size))) or (int(self.size3) > ( int(self.memory_size) - int(self.os_size))) or (int(self.size4) > ( int(self.memory_size) - int(self.os_size))) or (int(self.size5) > ( int(self.memory_size) - int(self.os_size))):
                #print ( "Error: Size input should not exceed ( Memory Size - OS Size )." )
                messagebox.showinfo( "Compute Error" , "Error: Size input should not exceed ( Memory Size - OS Size )." )
            elif self.arrival_time1_CHECK or self.arrival_time2_CHECK or self.arrival_time3_CHECK or self.arrival_time4_CHECK or self.arrival_time5_CHECK:
                #print ( " Error in arrival time input " )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Arrival Time Input." )
            elif self.run_time1_CHECK or self.run_time2_CHECK or self.run_time3_CHECK or self.run_time4_CHECK or self.run_time5_CHECK:
                #print ( "Error: Invalid Run Time Input." )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Run Time Input." )
            else:
                # Job Details [ job_size, job_numberum, arrival_time, run_time, isjob_waiting ]
                # manipulates the user's input in a format that can be understood by the Backend class.
                self.job_details = [ [ int(self.size1), 1, self.arrival_time1, self.run_time1, False],
                                    [ int(self.size2), 2, self.arrival_time2, self.run_time2, False],
                                    [ int(self.size3), 3, self.arrival_time3, self.run_time3, False],
                                    [ int(self.size4), 4, self.arrival_time4, self.run_time4, False],
                                    [ int(self.size5), 5, self.arrival_time5, self.run_time5, False]]
                # Memory [ sizeTaken, F/U( Free,Taken ), -1/job_numberum ]
                self.memory = [[( int(self.memory_size) - int(self.os_size) ) + 1,'F',-1]]
                # insert_inputs( self, mem_space, os_space, job_details, memory )
                self.dynamic_first_fit_backend.insert_inputs( self.memory_size, self.os_size, self.job_details, self.memory )
                self.dynamic_first_fit_backend.generate_summary_table()
                self.summary_table_window()
                #print ( " Success " )

    # the window which displays the summary table
    def summary_table_window( self ):
        self.summary_table = deepcopy(self.dynamic_first_fit_backend.get_summary_table())
        self.clear_widgets()
        self.basic_widget_list = []

        self.dynamicFirstFitBG = self.create_BG(root, dff_bg, bg_clr="black", placement=(0, 0))

        self.create_clock(date_placement= (170, 50), clock_placement= (700, 50), bg_clr= "#D3BAF4")

        self.title1_LBL = self.create_text_LBL(root, lbl_text= "First Fit Dynamic", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(375, 20))
        self.title2_LBL = self.create_text_LBL(root, lbl_text= "Partitioned Allocation", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(345, 65))
        self.title3_LBL = self.create_text_LBL(root, lbl_text= "Summary Table", font_label=('Times New Roman', 30), bg_clr="#0096FF", placement=(343, 155))

        # Job Labels
        self.job_LBL = self.create_text_LBL(root, lbl_text= "Job", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(125, 210))
        self.job1_LBL = self.create_text_LBL(root, lbl_text= "1", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 260))
        self.job2_LBL = self.create_text_LBL(root, lbl_text= "2", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 310))
        self.job3_LBL = self.create_text_LBL(root, lbl_text= "3", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 360))
        self.job4_LBL = self.create_text_LBL(root, lbl_text= "4", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 410))
        self.job5_LBL = self.create_text_LBL(root, lbl_text= "5", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 460))
        
        # Start Time Entries
        self.start_time_LBL = self.create_text_LBL(root, lbl_text= "Start Time", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(252, 210))
        self.start_time1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 260), state="readonly", text=self.summary_table[1][1].time())
        self.start_time2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 310), state="readonly", text=self.summary_table[2][1].time())
        self.start_time3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 360), state="readonly", text=self.summary_table[3][1].time())
        self.start_time4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 410), state="readonly", text=self.summary_table[4][1].time())
        self.start_time5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 460), state="readonly", text=self.summary_table[5][1].time())
        
        # Finish Time Entries
        self.finish_time_LBL = self.create_text_LBL(root, lbl_text= "Finish Time", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(512, 210))
        self.finish_time1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 260), state="readonly", text=self.summary_table[1][2].time())
        self.finish_time2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 310), state="readonly", text=self.summary_table[2][2].time())
        self.finish_time3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 360), state="readonly", text=self.summary_table[3][2].time())
        self.finish_time4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 410), state="readonly", text=self.summary_table[4][2].time())
        self.finish_time5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 460), state="readonly", text=self.summary_table[5][2].time())
        
        # CPU Wait Entries
        self.cpu_wait_LBL = self.create_text_LBL(root, lbl_text= "CPU Wait", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(725, 210))
        self.cpu_wait1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 260), state="readonly", text=self.summary_table[1][3])
        self.cpu_wait2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 310), state="readonly", text=self.summary_table[2][3])
        self.cpu_wait3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 360), state="readonly", text=self.summary_table[3][3])
        self.cpu_wait4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 410), state="readonly", text=self.summary_table[4][3])
        self.cpu_wait5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 460), state="readonly", text=self.summary_table[5][3])

        # Buttons
        self.back_BTN  =  self.create_text_BTN(root, text_label= 'BACK', execute_cmd= self.input1_window, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(200, 510))
        self.next_BTN  =  self.create_text_BTN(root, text_label= 'NEXT', execute_cmd= self.summary_table_next_BTN_Pressed, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(580, 510))
        self.exit_BTN  =  self.create_text_BTN(root, text_label= 'Exit', execute_cmd= root.destroy, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(390, 510))

    # This executes if the user presses the next button in the summary_table window.
    def summary_table_next_BTN_Pressed( self ):
        #print( "Summary Table next_BTN Pressed " )
        self.head_node = None
        self.tempMemoryResults = deepcopy(self.dynamic_first_fit_backend.get_memory_results())
        self.tempMemoryResults_time = deepcopy(self.dynamic_first_fit_backend.get_memory_results_time())
        for i in range(len( self.tempMemoryResults ) - 1, -1, -1):
            self.add_result_node( self.tempMemoryResults[i], self.tempMemoryResults_time[i], self.os_size, self.memory_size )
        if self.head_node != None:
            self.head_node.mem_map_window()
        

# This is a node class for the linked list
# the linked list contains the nodes which hosts the memory map, fat, and pat windows.
class Dynamic_First_Fit_Node(Frontend_Functions, Frontend_Functions2, Backend_Functions):
    def __init__ ( self, memory_result = None, memory_result_time = None, os_size = None, memory_size = None):
        super().__init__()
        self.back_pointer = None
        self.next_pointer = None
        self.patData = []
        self.fatData = []
        self.location = 0
        
        if memory_result == None:
            self.memory_result = [[500, "U", 1], [109, "F", -1]]
        else:
            self.memory_result = memory_result
                   
        if memory_result_time == None:
            self.memory_result_time = [ "09:00:00", ["Arrived(J1)", "Started(J1)"]]
        else:
            self.memory_result_time = memory_result_time

        if os_size == None:
            self.os_size = 32
        else:
            self.os_size = int(os_size)

        if memory_size == None:
            self.memory_size = 640
        else:
            self.memory_size = int(memory_size)

        self.location += int(self.os_size)
        self.temp_clrs = [ "#f77777", "#f7d977", "#77f7e6", "#77d5f7", "#d577f7", "#77d567", "#d5987" ]
        self.temp_clrCounter = 0
        self.temp_percentage = float(( float(self.os_size) / float(self.memory_size) ) * 100 )
        self.mem_map_data = [ [ self.temp_percentage, "#f5f3ed", "OS Size", self.temp_percentage, self.location, self.os_size ] ]
        self.availableCounter = 1
        self.pCounter = 1
        for certainResult in self.memory_result:
            if certainResult[1] == "U":
                if self.location+certainResult[0] > self.memory_size:
                    self.patData.append( [ certainResult[0] - 1, self.location, "Allocated(J{})".format( certainResult[2] ) ] )
                else:
                    self.patData.append( [ certainResult[0], self.location, "Allocated(J{})".format( certainResult[2] ) ] )
                self.location += int(certainResult[0])
                self.temp_percentage = float(( float(certainResult[0]) / float(self.memory_size) ) * 100 )
                self.mem_map_data.append( [ self.temp_percentage, self.temp_clrs[self.temp_clrCounter], "Allocated(P{})".format(self.pCounter), self.temp_percentage, self.location, certainResult[0] ])
                self.temp_clrCounter += 1
                self.pCounter += 1
            else:
                if self.location+certainResult[0] > self.memory_size:
                    self.fatData.append( [ certainResult[0] - 1, self.location, "Available" ] )
                    self.location += int(certainResult[0])
                    #print ( "Available Counter: ", self.availableCounter )
                    self.temp_percentage = float(( float(certainResult[0]) / float(self.memory_size) ) * 100 )
                    if certainResult[0] == 1:
                        pass
                    else:
                        self.mem_map_data.append( [ self.temp_percentage, self.temp_clrs[self.temp_clrCounter], "Available(F{})".format(self.availableCounter), self.temp_percentage, self.location - 1, certainResult[0] - 1 ])
                else:
                    self.fatData.append( [ certainResult[0], self.location, "Available" ] )
                    self.location += int(certainResult[0])
                    #print ( "Available Counter: ", self.availableCounter )
                    self.temp_percentage = float(( float(certainResult[0]) / float(self.memory_size) ) * 100 )
                    if certainResult[0] == 1:
                        pass
                    else:
                        self.mem_map_data.append( [ self.temp_percentage, self.temp_clrs[self.temp_clrCounter], "Available(F{})".format(self.availableCounter), self.temp_percentage, self.location, certainResult[0] ])
                    
                self.temp_clrCounter += 1
                self.availableCounter += 1


        self.countPatData = len( self.patData )
        if self.countPatData != 5:
            for i in range( 5 - self.countPatData ):
                self.patData.append( ["---", "---", "---"] )
        self.countFatData = len( self.fatData )
        if self.countFatData != 5:
            for i in range( 5 - self.countFatData ):
                self.fatData.append( ["---", "---", "---"] )

        ##print( self.mem_map_data )
        ##print( self.fatData )

        self.mem_map_data2 = deepcopy( self.mem_map_data )
        self.temp_count = len( self.mem_map_data2 )
        if self.temp_count != 7:
            for i in range( 7 - self.temp_count ):
                self.mem_map_data2.append([ "---", "#0096FF", "---", "---", "---", "---" ])
        #print( self.mem_map_data2 )

        # display_map( self, temp_pointer, temp_clr, temp_txt, temp_percentage, temp_total_size, memory_size )

    def mem_map_window( self ):
        self.clear_widgets()
        self.basic_widget_list = []

        self.dynamicFirstFitBG = self.create_BG(root, dff_bg, bg_clr="black", placement=(0, 0))
        
        self.create_clock(date_placement= (170, 50), clock_placement= (700, 50), bg_clr= "#D3BAF4")

        self.title1_LBL = self.create_text_LBL(root, lbl_text= "First Fit Dynamic", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(375, 20))
        self.title2_LBL = self.create_text_LBL(root, lbl_text= "Partitioned Allocation", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(345, 65))
        self.title3_LBL = self.create_text_LBL(root, lbl_text= "Memory Map Data", font_label=('Times New Roman', 20), bg_clr="#0096FF", placement=(170, 126))
        self.title4_LBL = self.create_text_LBL(root, lbl_text= f"At {self.memory_result_time[0]}", font_label=('Times New Roman', 12), bg_clr="#0096FF", placement=(228, 158))

        self.phys_mem_widgets = []
        self.y_counter = 140
        self.index_pointer = 0

        self.mark_LBL = self.create_text_LBL(root, lbl_text= "0", font_label=('Times New Roman', 10), bg_clr="#0096FF", placement=(530, self.y_counter - 20))

        for temp_data in self.mem_map_data:
            self.display_map( temp_data[0], temp_data[1], temp_data[2], temp_data[3], temp_data[4] )
        
        # Partition Labels
        self.partition_LBL = self.create_text_LBL(root, lbl_text= "#", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(80, 180))
        self.partition1_LBL = self.create_text_LBL(root, lbl_text= "1", font_label=('Times New Roman', 15), bg_clr=self.mem_map_data2[0][1], placement=(80, 230))
        self.partition2_LBL = self.create_text_LBL(root, lbl_text= "2", font_label=('Times New Roman', 15), bg_clr=self.mem_map_data2[1][1], placement=(80, 275))
        self.partition3_LBL = self.create_text_LBL(root, lbl_text= "3", font_label=('Times New Roman', 15), bg_clr=self.mem_map_data2[2][1], placement=(80, 320))
        self.partition4_LBL = self.create_text_LBL(root, lbl_text= "4", font_label=('Times New Roman', 15), bg_clr=self.mem_map_data2[3][1], placement=(80, 365))
        self.partition5_LBL = self.create_text_LBL(root, lbl_text= "5", font_label=('Times New Roman', 15), bg_clr=self.mem_map_data2[4][1], placement=(80, 410))
        self.partition6_LBL = self.create_text_LBL(root, lbl_text= "6", font_label=('Times New Roman', 15), bg_clr=self.mem_map_data2[5][1], placement=(80, 455))
        self.partition7_LBL = self.create_text_LBL(root, lbl_text= "7", font_label=('Times New Roman', 15), bg_clr=self.mem_map_data2[6][1], placement=(80, 500))

        # Size Entries
        self.size_LBL = self.create_text_LBL(root, lbl_text= "Size", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(220, 180))
        self.size1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(170, 230), state="readonly", text=self.mem_map_data2[0][5])
        self.size2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(170, 275), state="readonly", text=self.mem_map_data2[1][5])
        self.size3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(170, 320), state="readonly", text=self.mem_map_data2[2][5])
        self.size4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(170, 365), state="readonly", text=self.mem_map_data2[3][5])
        self.size5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(170, 410), state="readonly", text=self.mem_map_data2[4][5])
        self.size6_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(170, 455), state="readonly", text=self.mem_map_data2[5][5])
        self.size7_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(170, 500), state="readonly", text=self.mem_map_data2[6][5])


        # Status Entries
        self.statusLBL = self.create_text_LBL(root, lbl_text= "Status", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(380, 180))
        self.status1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(340, 230), state="readonly", text=self.mem_map_data2[0][2])
        self.status2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(340, 275), state="readonly", text=self.mem_map_data2[1][2])
        self.status3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(340, 320), state="readonly", text=self.mem_map_data2[2][2])
        self.status4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(340, 365), state="readonly", text=self.mem_map_data2[3][2])
        self.status5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(340, 410), state="readonly", text=self.mem_map_data2[4][2])
        self.status6_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(340, 455), state="readonly", text=self.mem_map_data2[5][2])
        self.status7_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(340, 500), state="readonly", text=self.mem_map_data2[6][2])

        # Buttons
        self.back_BTN  =  self.create_text_BTN(root, text_label= 'BACK', execute_cmd= self.mem_map_back_BTN_Pressed, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(200, 550))
        self.next_BTN  =  self.create_text_BTN(root, text_label= 'NEXT', execute_cmd= self.pat_window, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(580, 550))
        self.exit_BTN  =  self.create_text_BTN(root, text_label= 'Exit', execute_cmd= root.destroy, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(390, 550))

    def mem_map_back_BTN_Pressed( self ):
        #print ( "mem_map_back_BTN_Pressed" )
        if self.back_pointer != None:
            self.back_pointer.fat_window()
        else:
            dynamic_first_fit_program.summary_table_window()

    def pat_window( self ):
        self.clear_widgets()
        self.basic_widget_list = []

        self.dynamicFirstFitBG = self.create_BG(root, dff_bg, bg_clr="black", placement=(0, 0))
        
        self.create_clock(date_placement= (170, 50), clock_placement= (700, 50), bg_clr= "#D3BAF4")

        self.title1_LBL = self.create_text_LBL(root, lbl_text= "First Fit Dynamic", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(375, 20))
        self.title2_LBL = self.create_text_LBL(root, lbl_text= "Partitioned Allocation", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(345, 65))

        self.title3_LBL = self.create_text_LBL(root, lbl_text= "Partion Allocation Table", font_label=('Times New Roman', 30), bg_clr="#0096FF", placement=(270, 126))
        self.title4_LBL = self.create_text_LBL(root, lbl_text= f"At {self.memory_result_time[0]}", font_label=('Times New Roman', 12), bg_clr="#0096FF", placement=(425, 178))

        # PAT Number Widgets
        self.pat_num_LBL = self.create_text_LBL(root, lbl_text= "Partition #", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(100, 200))
        self.pat_num1_LBL = self.create_text_LBL(root, lbl_text= "1", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 240))
        self.pat_num2_LBL = self.create_text_LBL(root, lbl_text= "2", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 280))
        self.pat_num3_LBL = self.create_text_LBL(root, lbl_text= "3", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 320))
        self.pat_num4_LBL = self.create_text_LBL(root, lbl_text= "4", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 360))
        self.pat_num5_LBL = self.create_text_LBL(root, lbl_text= "5", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 400))

        # PAT Size Entries
        self.pat_size_LBL = self.create_text_LBL(root, lbl_text= "Size", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(277, 200))
        self.pat_size1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 240), state="readonly", text=self.patData[0][0])
        self.pat_size2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 280), state="readonly", text=self.patData[1][0])
        self.pat_size3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 320), state="readonly", text=self.patData[2][0])
        self.pat_size4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 360), state="readonly", text=self.patData[3][0])
        self.pat_size5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 400), state="readonly", text=self.patData[4][0])

        # PAT Location Widgets
        self.pat_location_LBL = self.create_text_LBL(root, lbl_text= "Location", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(522, 200))
        self.pat_location1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 240), state="readonly", text=self.patData[0][1])
        self.pat_location2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 280), state="readonly", text=self.patData[1][1])
        self.pat_location3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 320), state="readonly", text=self.patData[2][1])
        self.pat_location4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 360), state="readonly", text=self.patData[3][1])
        self.pat_location5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 400), state="readonly", text=self.patData[4][1])
        
        # PAT Status Widgets
        self.pat_statusLBL = self.create_text_LBL(root, lbl_text= "Status", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(740, 200))
        self.pat_status1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 240), state="readonly", text=self.patData[0][2])
        self.pat_status2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 280), state="readonly", text=self.patData[1][2])
        self.pat_status3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 320), state="readonly", text=self.patData[2][2])
        self.pat_status4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 360), state="readonly", text=self.patData[3][2])
        self.pat_status5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 400), state="readonly", text=self.patData[4][2])

        # Listbox Widgets
        self.pat_listbox1 = self.create_LISTBOX(HWB= (5, 40, 0), placement=(220, 450), justify = "center")
        self.pat_listbox2 = self.create_LISTBOX(HWB= (5, 40, 0), placement=(480, 450), justify = "center")

        self.temp_count1 = 0
        self.temp_count2 = 0
        for allocation in self.memory_result_time[1]:
            if allocation[0] == "A":
                self.temp_count1 += 1
                self.pat_listbox1.insert( self.temp_count1, allocation )
            else:
                self.temp_count2 += 1
                self.pat_listbox2.insert( self.temp_count2, allocation )
        
        # Buttons
        self.back_BTN  =  self.create_text_BTN(root, text_label= 'BACK', execute_cmd= self.mem_map_window, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(200, 550))
        self.next_BTN  =  self.create_text_BTN(root, text_label= 'NEXT', execute_cmd= self.fat_window, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(580, 550))
        self.exit_BTN  =  self.create_text_BTN(root, text_label= 'Exit', execute_cmd= root.destroy, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(390, 550))


    def fat_window( self ):
        self.clear_widgets()
        self.basic_widget_list = []

        self.dynamicFirstFitBG = self.create_BG(root, dff_bg, bg_clr="black", placement=(0, 0))
        
        self.create_clock(date_placement= (170, 50), clock_placement= (700, 50), bg_clr= "#D3BAF4")

        self.title1_LBL = self.create_text_LBL(root, lbl_text= "First Fit Dynamic", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(375, 20))
        self.title2_LBL = self.create_text_LBL(root, lbl_text= "Partitioned Allocation", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(345, 65))

        self.title3_LBL = self.create_text_LBL(root, lbl_text= "File Allocation Table", font_label=('Times New Roman', 30), bg_clr="#0096FF", placement=(305, 126))
        self.title4_LBL = self.create_text_LBL(root, lbl_text= f"At {self.memory_result_time[0]}", font_label=('Times New Roman', 12), bg_clr="#0096FF", placement=(425, 178))

        # FAT Number Widgets
        self.fat_num_LBL = self.create_text_LBL(root, lbl_text= "Partition #", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(100, 200))
        self.fat_num1_LBL = self.create_text_LBL(root, lbl_text= "1", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 240))
        self.fat_num2_LBL = self.create_text_LBL(root, lbl_text= "2", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 280))
        self.fat_num3_LBL = self.create_text_LBL(root, lbl_text= "3", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 320))
        self.fat_num4_LBL = self.create_text_LBL(root, lbl_text= "4", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 360))
        self.fat_num5_LBL = self.create_text_LBL(root, lbl_text= "5", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 400))

        # FAT Size Entries
        self.fat_size_LBL = self.create_text_LBL(root, lbl_text= "Size", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(277, 200))
        self.fat_size1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 240), state="readonly", text=self.fatData[0][0])
        self.fat_size2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 280), state="readonly", text=self.fatData[1][0])
        self.fat_size3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 320), state="readonly", text=self.fatData[2][0])
        self.fat_size4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 360), state="readonly", text=self.fatData[3][0])
        self.fat_size5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 400), state="readonly", text=self.fatData[4][0])

        # FAT Location Widgets
        self.fat_location_LBL = self.create_text_LBL(root, lbl_text= "Location", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(522, 200))
        self.fat_location1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 240), state="readonly", text=self.fatData[0][1])
        self.fat_location2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 280), state="readonly", text=self.fatData[1][1])
        self.fat_location3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 320), state="readonly", text=self.fatData[2][1])
        self.fat_location4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 360), state="readonly", text=self.fatData[3][1])
        self.fat_location5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 400), state="readonly", text=self.fatData[4][1])
        
        # FAT Status Widgets
        self.fat_statusLBL = self.create_text_LBL(root, lbl_text= "Status", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(740, 200))
        self.fat_status1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 240), state="readonly", text=self.fatData[0][2])
        self.fat_status2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 280), state="readonly", text=self.fatData[1][2])
        self.fat_status3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 320), state="readonly", text=self.fatData[2][2])
        self.fat_status4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 360), state="readonly", text=self.fatData[3][2])
        self.fat_status5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 400), state="readonly", text=self.fatData[4][2])

        # Listbox Widgets
        self.fat_listbox1 = self.create_LISTBOX(HWB= (5, 40, 0), placement=(220, 450), justify = "center")
        self.fat_listbox2 = self.create_LISTBOX(HWB= (5, 40, 0), placement=(480, 450), justify = "center")

        self.temp_count1 = 0
        self.temp_count2 = 0
        for allocation in self.memory_result_time[1]:
            if allocation[0] == "A":
                self.temp_count1 += 1
                self.fat_listbox1.insert( self.temp_count1, allocation )
            else:
                self.temp_count2 += 1
                self.fat_listbox2.insert( self.temp_count2, allocation )

        # Buttons
        self.back_BTN  =  self.create_text_BTN(root, text_label= 'BACK', execute_cmd= self.pat_window, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(200, 550))
        if self.next_pointer == None:
            self.next_BTN  =  self.create_text_BTN(root, text_label= 'Try New Input', execute_cmd= self.fat_next_BTN_Pressed, font_label=('Consolas', 16, 'bold'), width_label=13, bg_clr="#B3B3B3", placement=(580, 550))
        else:
            self.next_BTN  =  self.create_text_BTN(root, text_label= 'Next', execute_cmd= self.fat_next_BTN_Pressed, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(580, 550))
        self.exit_BTN  =  self.create_text_BTN(root, text_label= 'Exit', execute_cmd= root.destroy, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(390, 550))

    def fat_next_BTN_Pressed( self ):
        if self.next_pointer == None:
            dynamic_first_fit_program.input1_window()
        else:
            self.next_pointer.mem_map_window()
# END OF DFF PROGRAM: 2847-4428


# DBF PROGRAM: 4435-6027
# All the back end processes are hosted in this class.
class Dynamic_Best_Fit_Backend:
    def __init__( self ):
        self.time_zero = datetime.datetime.strptime('00:00', '%H:%M')
        # summary table [ job_numberum, start_time, finish_time, cpu_wait ]
        self.summary_table = {}
        self.all_time = []
        
        # Job Status [ allocated(True/False), finished(True/False), waiting ]
        self.job_status = { 1 : [ False, False, False ],
                           2 : [ False, False, False ],
                           3 : [ False, False, False ],
                           4 : [ False, False, False ],
                           5 : [ False, False, False ]}
        self.memory_results = []
        self.memory_results_time = []

    # for taking in the user's input into the Backend class.
    def insert_inputs( self, mem_space, os_space, job_details, memory, compaction_type ):
        #print( "INPUTS: " )
        #print ( "I1" , job_details )
        #print( "I2", memory )
        #print( "compaction_type : ", compaction_type )
        self.compaction_type = compaction_type
        self.mem_space = int(mem_space)
        self.os_space = int(os_space)
        self.memory_size = int( mem_space)
        self.os_space = int( os_space )
        self.job_details = deepcopy( job_details )
        self.memory = deepcopy( memory )

        self.summary_table = {}
        self.all_time = []
        # generates the all time list which will contain all the time that needs a memory map, fat, and pat.
        for job in self.job_details:
            self.tempTime = datetime.datetime.strptime( job[2], '%H:%M')
            self.all_time.append( self.tempTime )

        # job status [ isJobAllocated, isJobFinished, isjob_waiting ]
        self.job_status = { 1 : [ False, False, False ],
                           2 : [ False, False, False ],
                           3 : [ False, False, False ],
                           4 : [ False, False, False ],
                           5 : [ False, False, False ]}

        # memory_result will be used to store the data for every memory map.
        self.memory_results = []
        
        # memory_result_time will be used to store the time of every memory map.
        self.memory_results_time = []
        return

    # returns memory list
    def get_memory( self ):
        return self.memory

    # returns summary_table
    def get_summary_table( self ):
        return self.summary_table

    # returns the memory_results
    def get_memory_results( self ):
        return self.memory_results

    # returns the memory_results_time
    def get_memory_results_time( self ):
        return self.memory_results_time

    # for appending a certain memory list into the memory result
    def add_memory_result( self, memory, time, time_status) :
        self.memory_results.append( memory )
        self.memory_results_time.append( [time, time_status] )
        return

    # sorts the list containing all the time that needs a memory result.
    def arrange_all_time( self ):
        self.all_time.sort()
        return

    # remove's the time that already have a memory result.
    def remove_time( self, time ):
        try:
            while True:
                self.all_time.remove(time)
        except ValueError:
            pass
        self.arrange_all_time()
        return

    # checks if the job fits into the available partitions
    def check_job_fit( self, j_size ):
        # j_size: job size
        self.j_size = j_size
        # memorySpace[1]: F for free/available space and U if occupied by a certain job
        # memorySpace[0]: the size of the partition.
        for memorySpace in self.memory:
            if memorySpace[1] == "F" and memorySpace[0] > self.j_size:
                return True
        return False

    # checks a certain job's status.
    def check_job_status( self ):
        # checks if the jobs are already done.
        self.jobsDone = 0
        for job_numberum in list(self.job_status):
            if self.job_status[job_numberum][0] == True and self.job_status[job_numberum][1]:
                self.jobsDone += 1
        if self.jobsDone == len( list(self.job_status) ):
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


    def recycle_with_compaction( self, memory, job ):
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
                        self.temp_job = deepcopy( self.recycle_memory[i] )
                        self.tempFreeSpace = deepcopy( self.recycle_memory[i-1] )
                        self.recycle_memory[i-1] = self.temp_job
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
    def generate_summary_table( self ):
        self.is_finished = False
        self.arrange_all_time()
        
        while self.is_finished == False:
            # This block of code sets the needed parameters for the next process.
            # It resets the indicator 'action_taken'. This indicator is used by the
            # program to determine if a job has been allocated/de-allocated in this iteration.
            # temp_time_status: contains the status of certain time periods. This could contain
            #                 job arrivals, job waiting, and job terminations.
            # current_time: the time of a certain/this iteration.
            self.action_taken = False
            self.temp_time_status = []
            try:
                self.arrange_all_time()
                self.current_time = self.all_time[0]
            except:
                self.is_finished = True
                break

            # Checks if all the jobs are already finished. If it is, then stop the while loop.
            self.temp_job_status = self.check_job_status()
            if self.temp_job_status == True:
                self.is_finished = True
                break

            # Iterates through the job details to see what actions can be taken in this current_time
            for job in self.job_details:
                self.job_fits = self.check_job_fit( job[0] )
                self.test_job_waiting = True

                # If a certain job details from the self.job_details is deemed to waiting to be allocated
                # then, it will check if the current_time meets the job's demand for allocation.
                if job[4] != False:
                    self.temp_wait_until = job[4]
                    if self.current_time == self.temp_wait_until:
                        self.test_job_waiting = False

                # If a certain job arrives, this nested condition will check whether the job needs to wait or is capable
                # of immediate allocation.
                if self.current_time == datetime.datetime.strptime( job[2], '%H:%M') and self.job_status[job[1]][0] == False:
                    if self.job_fits == True:
                        self.temp_time_status.append( "Arrived(J{})".format( job[1] ) )
                    else:
                        self.temp_time_status.append( "Arrived/Wait(J{})".format( job[1] ) )
                        self.temp_wait_until = self.temp_finish_time
                        job[4] = self.temp_wait_until
                # This conditions checks if a certain actions could be taken.
                # The actions could be, the start/allocation or termination of certain job.
                if ( self.test_job_waiting == False or self.current_time == datetime.datetime.strptime( job[2], '%H:%M')) and self.job_status[job[1]][0] == False and self.job_fits == True:
                    self.memory = self.allocate( self.memory, [ job[1], "a" , job[0] ] )
                    self.job_status[job[1]][0] = True

                    self.temp_start_time = self.current_time
                    if (self.temp_start_time - datetime.datetime.strptime( job[2], '%H:%M')).total_seconds() < 0:
                        self.temp_cpu_wait = "0:00:00"
                        self.temp_start_time = datetime.datetime.strptime( job[2], '%H:%M')
                    else:
                        self.temp_cpu_wait = self.temp_start_time - datetime.datetime.strptime( job[2], '%H:%M')
                    self.temp_finish_time = ( self.temp_start_time - self.time_zero + (datetime.datetime.strptime( job[3], '%H:%M')))
                    self.all_time.append( self.temp_finish_time )
                    self.summary_table[job[1]] = [ job[1], self.temp_start_time, self.temp_finish_time, self.temp_cpu_wait ]

                    self.action_taken = True
                    self.temp_time_status.append( "Started(J{})".format( job[1] ) )
                elif self.job_status[job[1]][0] == True and self.current_time == self.summary_table[job[1]][2]:
                    if self.compaction_type == "Without Compaction":
                        self.memory = self.recycle( self.memory, [ job[1], "f" , job[0] ] )
                    else:
                        self.memory = self.recycle_with_compaction( self.memory, [ job[1], "f" , job[0] ] )
                    self.job_status[job[1]][1] = True
                    
                    self.action_taken = True
                    self.temp_time_status.append( "Terminated(J{})".format( job[1] ) )
                else:
                    pass

            # copies the memory list of this current_time
            self.memory_to_add = deepcopy(self.memory)
            # appds the needed data into the memory_result list.
            self.add_memory_result( self.memory_to_add, self.current_time, deepcopy(self.temp_time_status) )

            # Checks if all the job are already finished. If not, then remove the current time from
            # the list of all time.
            self.temp_job_status = self.check_job_status()
            if self.temp_job_status == True:
                self.is_finished = True
                break
            else:
                self.remove_time( self.current_time )


# Contains all the front end windows and functions
class Dynamic_Best_Fit_Frontend(Frontend_Functions, Frontend_Functions2, Backend_Functions):
    def __init__( self ):
        super().__init__()
        self.mem_space = 640
        self.memory_size = 640
        self.os_space = 32
        self.os_size = 32
        # Job Details [ job_size, job_numberum, arrival_time, run_time, isjob_waiting ]
        self.job_details = [ [ 200, 1, "9:00", "0:20", False],
                            [ 250, 2, "9:10", "0:25", False],
                            [ 300, 3, "9:30", "0:30", False],
                            [ 50, 4, "13:00", "1:00", False],
                            [ 50, 5, "13:00", "1:30", False]]

        self.memory = [[609,'F',-1]]

        self.title1_text = "Dynamic Best Fit"
        self.title1_placement = (375, 20)
        
        self.backend = Dynamic_Best_Fit_Backend()

        # insert_inputs( self, mem_space, os_space, job_details, memory )
        self.backend.insert_inputs( self.mem_space, self.os_space, self.job_details, self.memory, "With Compaction" )
        self.backend.generate_summary_table()

        self.head_node = None

    # To add a node into the linked list
    # ( self, memory_result = None, memory_result_time = None, os_size = None, memory_size = None)
    def add_result_node( self, memory_result, memory_result_time, os_size, memory_size ):
        memory_result_time[0] = memory_result_time[0].time()
        self.temp_node = Dynamic_Best_Fit_Node( memory_result, memory_result_time, os_size, memory_size )

        if self.head_node == None:
            self.head_node = self.temp_node
        else:
            self.head_node.back_pointer = self.temp_node
            self.temp_node.next_pointer = self.head_node

            self.head_node = self.temp_node
        return

    def main_menu_BTN_pressed( self ):
        main_program.main_menu_window()

    # function which contains widget placements
    # this also takes in the user's input.
    def input1_window( self ):
        root.title ( "Dynamic Best Fit" )
        self.clear_widgets()
        self.basic_widget_list = []

        self.dynamicBestFitGB = self.create_BG(root, dbf_bg, bg_clr="black", placement=(0, 0))
        
        self.create_clock(date_placement= (170, 50), clock_placement= (700, 50), bg_clr= "#D3BAF4")

        self.title1_LBL = self.create_text_LBL(root, lbl_text= self.title1_text, font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=self.title1_placement)
        self.title2_LBL = self.create_text_LBL(root, lbl_text= "Partitioned Allocation", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(345, 65))
        self.title3_LBL = self.create_text_LBL(root, lbl_text= "Input Window", font_label=('Times New Roman', 30), bg_clr="#0096FF", placement=(355, 135))

        # Job labels
        self.job_LBL = self.create_text_LBL(root, lbl_text= "Job", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(125, 180))
        self.job1_LBL = self.create_text_LBL(root, lbl_text= "1", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 230))
        self.job2_LBL = self.create_text_LBL(root, lbl_text= "2", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 280))
        self.job3_LBL = self.create_text_LBL(root, lbl_text= "3", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 330))
        self.job4_LBL = self.create_text_LBL(root, lbl_text= "4", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 380))
        self.job5_LBL = self.create_text_LBL(root, lbl_text= "5", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 440))

        # Size Entries
        self.size_LBL = self.create_text_LBL(root, lbl_text= "Size", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(275, 180))
        self.size1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(225, 230), justify="center")
        self.size2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(225, 280), justify="center")
        self.size3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(225, 330), justify="center")
        self.size4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(225, 380), justify="center")
        self.size5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(225, 440), justify="center")

        # Arrival Time Entries
        self.arrival_time_LBL  = self.create_text_LBL(root, lbl_text= "Arrival Time", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(505, 180))
        self.arrival_time1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(490, 230), justify="center")
        self.arrival_time2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(490, 280), justify="center")
        self.arrival_time3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(490, 330), justify="center")
        self.arrival_time4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(490, 380), justify="center")
        self.arrival_time5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(490, 440), justify="center")

        # Run Time Entries
        self.run_time_LBL  = self.create_text_LBL(root, lbl_text= "Run Time", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(725, 180))
        self.run_time1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(700, 230), justify="center")
        self.run_time2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(700, 280), justify="center")
        self.run_time3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(700, 330), justify="center")
        self.run_time4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(700, 380), justify="center")
        self.run_time5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(700, 440), justify="center")

        # Memory Size Entry
        self.memory_size_LBL  = self.create_text_LBL(root, lbl_text= "Memory Size", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(240, 470))
        self.memory_size_entry = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(220, 520), justify="center")

        # OS Size Entry
        self.os_size_LBL  = self.create_text_LBL(root, lbl_text= "OS Size", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(560, 470))
        self.os_size_entry = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), placement=(525, 520), justify="center")
        
        self.compaction_options = [ "Without Compaction" , "With Compaction" ]
        self.compaction_chosen = StringVar( root )
        self.compaction_chosen.set( self.compaction_options[0] )

        self.compaction_menu = OptionMenu( root, self.compaction_chosen, *self.compaction_options )
        self.compaction_menu.configure( width = 20 )
        self.compaction_menu.place( x = 380, y = 470 )

        # Buttons
        self.exit_BTN  =  self.create_text_BTN(root, text_label= 'Exit', execute_cmd= root.destroy, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(190, 550))
        self.compute_BTN  =  self.create_text_BTN(root, text_label= 'Compute', execute_cmd= self.input1_compute_BTN_Pressed, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(390, 550))
        self.main_menu_BTN = self.create_text_BTN(root, text_label= 'Menu', execute_cmd= self.main_menu_BTN_pressed, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(590, 550))


    # Executes once the user presses the compute button in the input1_window
    def input1_compute_BTN_Pressed( self ):
        self.clear_nodes()
        #print( "Head Node: " , self.head_node )
        #print ( "Input1 Compute BTN Pressed " )
        if messagebox.askyesno( "Confirmation..." , " Are you sure you want to compute? " ) == True :
            self.size1 = self.size1_ENTRY.get()
            self.size2 = self.size2_ENTRY.get()
            self.size3 = self.size3_ENTRY.get()
            self.size4 = self.size4_ENTRY.get()
            self.size5 = self.size5_ENTRY.get()

            self.memory_size = self.memory_size_entry.get()
            self.os_size = self.os_size_entry.get()

            self.memory_size_CHECK = self.is_not_integer( self.memory_size )
            self.os_size_CHECK = self.is_not_integer( self.os_size )
 
            self.size1_CHECK = self.is_not_integer( self.size1 )
            self.size2_CHECK = self.is_not_integer( self.size2 )
            self.size3_CHECK = self.is_not_integer( self.size3 )
            self.size4_CHECK = self.is_not_integer( self.size4 )
            self.size5_CHECK = self.is_not_integer( self.size5 )
            
            
            self.arrival_time1 = self.arrival_time1_ENTRY.get()
            self.arrival_time2 = self.arrival_time2_ENTRY.get()
            self.arrival_time3 = self.arrival_time3_ENTRY.get()
            self.arrival_time4 = self.arrival_time4_ENTRY.get()
            self.arrival_time5 = self.arrival_time5_ENTRY.get()

            self.arrival_time1_CHECK = self.is_not_time_format( self.arrival_time1 )
            self.arrival_time2_CHECK = self.is_not_time_format( self.arrival_time2 )
            self.arrival_time3_CHECK = self.is_not_time_format( self.arrival_time3 )
            self.arrival_time4_CHECK = self.is_not_time_format( self.arrival_time4 )
            self.arrival_time5_CHECK = self.is_not_time_format( self.arrival_time5 )

            self.run_time1 = self.run_time1_ENTRY.get()
            self.run_time2 = self.run_time2_ENTRY.get()
            self.run_time3 = self.run_time3_ENTRY.get()
            self.run_time4 = self.run_time4_ENTRY.get()
            self.run_time5 = self.run_time5_ENTRY.get()
        
            self.run_time1_CHECK = self.is_not_time_format( self.run_time1 )
            self.run_time2_CHECK = self.is_not_time_format( self.run_time2 )
            self.run_time3_CHECK = self.is_not_time_format( self.run_time3 )
            self.run_time4_CHECK = self.is_not_time_format( self.run_time4 )
            self.run_time5_CHECK = self.is_not_time_format( self.run_time5 )

            self.compaction_type = self.compaction_chosen.get()

            # This condition checks whether the user's inputted values are acceptable.
            # If not, #print the errors.
            if self.memory_size_CHECK or self.os_size_CHECK :
                #print ( "Error: Invalid Memory or OS Size input." )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Memory or OS Size input." )
            elif int(self.memory_size) < int(self.os_size):
                #print ( " Error: Os Size can't exceed Memory Size. " )
                messagebox.showinfo( "Compute Error" , "Error: Os Size can't exceed Memory Size." )
            elif self.size1_CHECK or self.size2_CHECK or self.size3_CHECK or self.size4_CHECK or self.size5_CHECK:
                #print ( "Error: Size input detected as not an integer." )
                messagebox.showinfo( "Compute Error" , "Error: Size input detected as not an integer." )
            elif (int(self.size1) > ( int(self.memory_size) - int(self.os_size))) or (int(self.size2) > ( int(self.memory_size) - int(self.os_size))) or (int(self.size3) > ( int(self.memory_size) - int(self.os_size))) or (int(self.size4) > ( int(self.memory_size) - int(self.os_size))) or (int(self.size5) > ( int(self.memory_size) - int(self.os_size))):
                #print ( "Error: Size input should not exceed ( Memory Size - OS Size )." )
                messagebox.showinfo( "Compute Error" , "Error: Size input should not exceed ( Memory Size - OS Size )." )
            elif self.arrival_time1_CHECK or self.arrival_time2_CHECK or self.arrival_time3_CHECK or self.arrival_time4_CHECK or self.arrival_time5_CHECK:
                #print ( " Error in arrival time input " )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Arrival Time Input." )
            elif self.run_time1_CHECK or self.run_time2_CHECK or self.run_time3_CHECK or self.run_time4_CHECK or self.run_time5_CHECK:
                #print ( "Error: Invalid Run Time Input." )
                messagebox.showinfo( "Compute Error" , "Error: Invalid Run Time Input." )
            else:
                # Job Details [ job_size, job_numberum, arrival_time, run_time, isjob_waiting ]
                # manipulates the user's input in a format that can be understood by the Backend class.
                self.job_details = [ [ int(self.size1), 1, self.arrival_time1, self.run_time1, False],
                                    [ int(self.size2), 2, self.arrival_time2, self.run_time2, False],
                                    [ int(self.size3), 3, self.arrival_time3, self.run_time3, False],
                                    [ int(self.size4), 4, self.arrival_time4, self.run_time4, False],
                                    [ int(self.size5), 5, self.arrival_time5, self.run_time5, False]]
                # Memory [ sizeTaken, F/U( Free,Taken ), -1/job_numberum ]
                self.memory = [[( int(self.memory_size) - int(self.os_size) ) + 1,'F',-1]]
                # insert_inputs( self, mem_space, os_space, job_details, memory )
                self.backend.insert_inputs( self.memory_size, self.os_size, self.job_details, self.memory, self.compaction_type )
                self.backend.generate_summary_table()
                self.summary_table_window()
                #print ( " Success " )

    # the window which displays the summary table
    def summary_table_window( self ):
        self.summary_table = deepcopy(self.backend.get_summary_table())
        self.clear_widgets()
        self.basic_widget_list = []

        self.dynamicBestFitGB = self.create_BG(root, dbf_bg, bg_clr="black", placement=(0, 0))
        
        self.create_clock(date_placement= (170, 50), clock_placement= (700, 50), bg_clr= "#D3BAF4")

        self.title1_LBL = self.create_text_LBL(root, lbl_text= self.title1_text, font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=self.title1_placement)
        self.title2_LBL = self.create_text_LBL(root, lbl_text= "Partitioned Allocation", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(345, 65))
        self.title3_LBL = self.create_text_LBL(root, lbl_text= "Summary Table", font_label=('Times New Roman', 30), bg_clr="#0096FF", placement=(343, 155))

        # Job Labels
        self.job_LBL = self.create_text_LBL(root, lbl_text= "Job", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(125, 210))
        self.job1_LBL = self.create_text_LBL(root, lbl_text= "1", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 260))
        self.job2_LBL = self.create_text_LBL(root, lbl_text= "2", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 310))
        self.job3_LBL = self.create_text_LBL(root, lbl_text= "3", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 360))
        self.job4_LBL = self.create_text_LBL(root, lbl_text= "4", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 410))
        self.job5_LBL = self.create_text_LBL(root, lbl_text= "5", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 460))
        
        # Start Time Entries
        self.start_time_LBL = self.create_text_LBL(root, lbl_text= "Start Time", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(252, 210))
        self.start_time1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 260), state="readonly", text=self.summary_table[1][1].time())
        self.start_time2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 310), state="readonly", text=self.summary_table[2][1].time())
        self.start_time3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 360), state="readonly", text=self.summary_table[3][1].time())
        self.start_time4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 410), state="readonly", text=self.summary_table[4][1].time())
        self.start_time5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 460), state="readonly", text=self.summary_table[5][1].time())
        
        # Finish Time Entries
        self.finish_time_LBL = self.create_text_LBL(root, lbl_text= "Finish Time", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(512, 210))
        self.finish_time1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 260), state="readonly", text=self.summary_table[1][2].time())
        self.finish_time2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 310), state="readonly", text=self.summary_table[2][2].time())
        self.finish_time3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 360), state="readonly", text=self.summary_table[3][2].time())
        self.finish_time4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 410), state="readonly", text=self.summary_table[4][2].time())
        self.finish_time5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 460), state="readonly", text=self.summary_table[5][2].time())
        
        # CPU Wait Entries
        self.cpu_wait_LBL = self.create_text_LBL(root, lbl_text= "CPU Wait", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(725, 210))
        self.cpu_wait1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 260), state="readonly", text=self.summary_table[1][3])
        self.cpu_wait2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 310), state="readonly", text=self.summary_table[2][3])
        self.cpu_wait3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 360), state="readonly", text=self.summary_table[3][3])
        self.cpu_wait4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 410), state="readonly", text=self.summary_table[4][3])
        self.cpu_wait5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 460), state="readonly", text=self.summary_table[5][3])

        # Buttons
        self.back_BTN  =  self.create_text_BTN(root, text_label= 'BACK', execute_cmd= self.input1_window, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(200, 510))
        self.next_BTN  =  self.create_text_BTN(root, text_label= 'NEXT', execute_cmd= self.summary_table_next_BTN_Pressed, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(580, 510))
        self.exit_BTN  =  self.create_text_BTN(root, text_label= 'Exit', execute_cmd= root.destroy, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(390, 510))

    # This executes if the user presses the next button in the summary_table window.
    def summary_table_next_BTN_Pressed( self ):
        self.clear_nodes()
        #print( "Summary Table next_BTN Pressed " )
        self.tempMemoryResults = deepcopy(self.backend.get_memory_results())
        self.tempMemoryResults_time = deepcopy(self.backend.get_memory_results_time())
        for i in range(len( self.tempMemoryResults ) - 1, -1, -1):
            self.add_result_node( self.tempMemoryResults[i], self.tempMemoryResults_time[i], self.os_size, self.memory_size )
        if self.head_node != None:
            self.head_node.mem_map_window()
        

# This is a node class for the linked list
# the linked list contains the nodes which hosts the memory map, fat, and pat windows.
class Dynamic_Best_Fit_Node(Frontend_Functions, Frontend_Functions2, Backend_Functions):
    def __init__ ( self, memory_result = None, memory_result_time = None, os_size = None, memory_size = None):
        super().__init__()
        self.back_pointer = None
        self.next_pointer = None
        self.patData = []
        self.fatData = []
        self.location = 0

        self.title1_text = "Dynamic Best Fit"
        self.title1_placement = (375, 20)
        
        if memory_result == None:
            self.memory_result = [[500, "U", 1], [109, "F", -1]]
        else:
            self.memory_result = memory_result
                   
        if memory_result_time == None:
            self.memory_result_time = [ "09:00:00", ["Arrived(J1)", "Started(J1)"]]
        else:
            self.memory_result_time = memory_result_time

        if os_size == None:
            self.os_size = 32
        else:
            self.os_size = int(os_size)

        if memory_size == None:
            self.memory_size = 640
        else:
            self.memory_size = int(memory_size)

        self.location += int(self.os_size)
        self.temp_clrs = [ "#f77777", "#f7d977", "#77f7e6", "#77d5f7", "#d577f7", "#77d567", "#d5987" ]
        self.temp_clrCounter = 0
        self.temp_percentage = float(( float(self.os_size) / float(self.memory_size) ) * 100 )
        self.mem_map_data = [ [ self.temp_percentage, "#f5f3ed", "OS Size", self.temp_percentage, self.location, self.os_size ] ]
        self.availableCounter = 1
        self.pCounter = 1
        for certainResult in self.memory_result:
            if certainResult[1] == "U":
                if self.location+certainResult[0] > self.memory_size:
                    self.patData.append( [ certainResult[0] - 1, self.location, "Allocated(J{})".format( certainResult[2] ) ] )
                else:
                    self.patData.append( [ certainResult[0], self.location, "Allocated(J{})".format( certainResult[2] ) ] )
                self.location += int(certainResult[0])
                self.temp_percentage = float(( float(certainResult[0]) / float(self.memory_size) ) * 100 )
                self.mem_map_data.append( [ self.temp_percentage, self.temp_clrs[self.temp_clrCounter], "Allocated(P{})".format( self.pCounter), self.temp_percentage, self.location, certainResult[0] ])
                self.temp_clrCounter += 1
                self.pCounter += 1
            else:
                if self.location+certainResult[0] > self.memory_size:
                    self.fatData.append( [ certainResult[0] - 1, self.location, "Available" ] )
                    self.location += int(certainResult[0])
                    #print ( "Available Counter: ", self.availableCounter )
                    self.temp_percentage = float(( float(certainResult[0]) / float(self.memory_size) ) * 100 )
                    if certainResult[0] == 1:
                        pass
                    else:
                        self.mem_map_data.append( [ self.temp_percentage, self.temp_clrs[self.temp_clrCounter], "Available(F{})".format(self.availableCounter), self.temp_percentage, self.location - 1, certainResult[0] - 1 ])
                else:
                    self.fatData.append( [ certainResult[0], self.location, "Available" ] )
                    self.location += int(certainResult[0])
                    #print ( "Available Counter: ", self.availableCounter )
                    self.temp_percentage = float(( float(certainResult[0]) / float(self.memory_size) ) * 100 )
                    if certainResult[0] == 1:
                        pass
                    else:
                        self.mem_map_data.append( [ self.temp_percentage, self.temp_clrs[self.temp_clrCounter], "Available(F{})".format(self.availableCounter), self.temp_percentage, self.location, certainResult[0] ])
                    
                self.temp_clrCounter += 1
                self.availableCounter += 1


        self.countPatData = len( self.patData )
        if self.countPatData != 5:
            for i in range( 5 - self.countPatData ):
                self.patData.append( ["---", "---", "---"] )
        self.countFatData = len( self.fatData )
        if self.countFatData != 5:
            for i in range( 5 - self.countFatData ):
                self.fatData.append( ["---", "---", "---"] )

        ##print( self.mem_map_data )
        ##print( self.fatData )

        self.mem_map_data2 = deepcopy( self.mem_map_data )
        self.temp_count = len( self.mem_map_data2 )
        if self.temp_count != 7:
            for i in range( 7 - self.temp_count ):
                self.mem_map_data2.append([ "---", "#0096FF", "---", "---", "---", "---" ])
        #print( self.mem_map_data2 )

        # display_map( self, temp_pointer, temp_clr, temp_txt, temp_percentage, temp_total_size, memory_size )


    def mem_map_window( self ):
        self.clear_widgets()
        self.basic_widget_list = []

        self.dynamicBestFitGB = self.create_BG(root, dbf_bg, bg_clr="black", placement=(0, 0))
        
        self.create_clock(date_placement= (170, 50), clock_placement= (700, 50), bg_clr= "#D3BAF4")

        self.title1_LBL = self.create_text_LBL(root, lbl_text= self.title1_text, font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=self.title1_placement)
        self.title2_LBL = self.create_text_LBL(root, lbl_text= "Partitioned Allocation", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(345, 65))
        self.title3_LBL = self.create_text_LBL(root, lbl_text= "Memory Map Data", font_label=('Times New Roman', 20), bg_clr="#0096FF", placement=(170, 126))
        self.title4_LBL = self.create_text_LBL(root, lbl_text= f"At {self.memory_result_time[0]}", font_label=('Times New Roman', 12), bg_clr="#0096FF", placement=(228, 158))

        
        self.phys_mem_widgets = []
        self.y_counter = 140
        self.index_pointer = 0

        self.mark_LBL = self.create_text_LBL(root, lbl_text= "0", font_label=('Times New Roman', 10), bg_clr="#0096FF", placement=(530, self.y_counter - 20))

        for temp_data in self.mem_map_data:
            self.display_map( temp_data[0], temp_data[1], temp_data[2], temp_data[3], temp_data[4] )
        
        # Partition Labels
        self.partition_LBL = self.create_text_LBL(root, lbl_text= "#", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(80, 180))
        self.partition1_LBL = self.create_text_LBL(root, lbl_text= "1", font_label=('Times New Roman', 15), bg_clr=self.mem_map_data2[0][1], placement=(80, 230))
        self.partition2_LBL = self.create_text_LBL(root, lbl_text= "2", font_label=('Times New Roman', 15), bg_clr=self.mem_map_data2[1][1], placement=(80, 275))
        self.partition3_LBL = self.create_text_LBL(root, lbl_text= "3", font_label=('Times New Roman', 15), bg_clr=self.mem_map_data2[2][1], placement=(80, 320))
        self.partition4_LBL = self.create_text_LBL(root, lbl_text= "4", font_label=('Times New Roman', 15), bg_clr=self.mem_map_data2[3][1], placement=(80, 365))
        self.partition5_LBL = self.create_text_LBL(root, lbl_text= "5", font_label=('Times New Roman', 15), bg_clr=self.mem_map_data2[4][1], placement=(80, 410))
        self.partition6_LBL = self.create_text_LBL(root, lbl_text= "6", font_label=('Times New Roman', 15), bg_clr=self.mem_map_data2[5][1], placement=(80, 455))
        self.partition7_LBL = self.create_text_LBL(root, lbl_text= "7", font_label=('Times New Roman', 15), bg_clr=self.mem_map_data2[6][1], placement=(80, 500))

        # Size Entries
        self.size_LBL = self.create_text_LBL(root, lbl_text= "Size", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(220, 180))
        self.size1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(170, 230), state="readonly", text=self.mem_map_data2[0][5])
        self.size2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(170, 275), state="readonly", text=self.mem_map_data2[1][5])
        self.size3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(170, 320), state="readonly", text=self.mem_map_data2[2][5])
        self.size4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(170, 365), state="readonly", text=self.mem_map_data2[3][5])
        self.size5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(170, 410), state="readonly", text=self.mem_map_data2[4][5])
        self.size6_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(170, 455), state="readonly", text=self.mem_map_data2[5][5])
        self.size7_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(170, 500), state="readonly", text=self.mem_map_data2[6][5])


        # Status Entries
        self.statusLBL = self.create_text_LBL(root, lbl_text= "Status", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(380, 180))
        self.status1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(340, 230), state="readonly", text=self.mem_map_data2[0][2])
        self.status2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(340, 275), state="readonly", text=self.mem_map_data2[1][2])
        self.status3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(340, 320), state="readonly", text=self.mem_map_data2[2][2])
        self.status4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(340, 365), state="readonly", text=self.mem_map_data2[3][2])
        self.status5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(340, 410), state="readonly", text=self.mem_map_data2[4][2])
        self.status6_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(340, 455), state="readonly", text=self.mem_map_data2[5][2])
        self.status7_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(340, 500), state="readonly", text=self.mem_map_data2[6][2])

        # Buttons
        self.back_BTN  =  self.create_text_BTN(root, text_label= 'BACK', execute_cmd= self.mem_map_back_BTN_Pressed, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(200, 550))
        self.next_BTN  =  self.create_text_BTN(root, text_label= 'NEXT', execute_cmd= self.pat_window, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(580, 550))
        self.exit_BTN  =  self.create_text_BTN(root, text_label= 'Exit', execute_cmd= root.destroy, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(390, 550))

    def mem_map_back_BTN_Pressed( self ):
        #print ( "mem_map_back_BTN_Pressed" )
        if self.back_pointer != None:
            self.back_pointer.fat_window()
        else:
            dynamic_best_fit_program.summary_table_window()

    def pat_window( self ):
        self.clear_widgets()
        self.basic_widget_list = []

        self.dynamicBestFitGB = self.create_BG(root, dbf_bg, bg_clr="black", placement=(0, 0))
        
        self.create_clock(date_placement= (170, 50), clock_placement= (700, 50), bg_clr= "#D3BAF4")

        self.title1_LBL = self.create_text_LBL(root, lbl_text= self.title1_text, font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=self.title1_placement)
        self.title2_LBL = self.create_text_LBL(root, lbl_text= "Partitioned Allocation", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(345, 65))

        self.title3_LBL = self.create_text_LBL(root, lbl_text= "Partion Allocation Table", font_label=('Times New Roman', 30), bg_clr="#0096FF", placement=(270, 126))
        self.title4_LBL = self.create_text_LBL(root, lbl_text= f"At {self.memory_result_time[0]}", font_label=('Times New Roman', 12), bg_clr="#0096FF", placement=(425, 178))

        # PAT Number Widgets
        self.pat_num_LBL = self.create_text_LBL(root, lbl_text= "Partition #", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(100, 200))
        self.pat_num1_LBL = self.create_text_LBL(root, lbl_text= "1", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 240))
        self.pat_num2_LBL = self.create_text_LBL(root, lbl_text= "2", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 280))
        self.pat_num3_LBL = self.create_text_LBL(root, lbl_text= "3", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 320))
        self.pat_num4_LBL = self.create_text_LBL(root, lbl_text= "4", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 360))
        self.pat_num5_LBL = self.create_text_LBL(root, lbl_text= "5", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 400))

        # PAT Size Entries
        self.pat_size_LBL = self.create_text_LBL(root, lbl_text= "Size", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(277, 200))
        self.pat_size1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 240), state="readonly", text=self.patData[0][0])
        self.pat_size2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 280), state="readonly", text=self.patData[1][0])
        self.pat_size3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 320), state="readonly", text=self.patData[2][0])
        self.pat_size4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 360), state="readonly", text=self.patData[3][0])
        self.pat_size5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 400), state="readonly", text=self.patData[4][0])

        # PAT Location Widgets
        self.pat_location_LBL = self.create_text_LBL(root, lbl_text= "Location", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(522, 200))
        self.pat_location1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 240), state="readonly", text=self.patData[0][1])
        self.pat_location2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 280), state="readonly", text=self.patData[1][1])
        self.pat_location3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 320), state="readonly", text=self.patData[2][1])
        self.pat_location4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 360), state="readonly", text=self.patData[3][1])
        self.pat_location5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 400), state="readonly", text=self.patData[4][1])
        
        # PAT Status Widgets
        self.pat_statusLBL = self.create_text_LBL(root, lbl_text= "Status", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(740, 200))
        self.pat_status1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 240), state="readonly", text=self.patData[0][2])
        self.pat_status2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 280), state="readonly", text=self.patData[1][2])
        self.pat_status3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 320), state="readonly", text=self.patData[2][2])
        self.pat_status4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 360), state="readonly", text=self.patData[3][2])
        self.pat_status5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 400), state="readonly", text=self.patData[4][2])

        # Listbox Widgets
        self.pat_listbox1 = self.create_LISTBOX(HWB= (5, 40, 0), placement=(220, 450), justify = "center")
        self.pat_listbox2 = self.create_LISTBOX(HWB= (5, 40, 0), placement=(480, 450), justify = "center")

        self.temp_count1 = 0
        self.temp_count2 = 0
        for allocation in self.memory_result_time[1]:
            if allocation[0] == "A":
                self.temp_count1 += 1
                self.pat_listbox1.insert( self.temp_count1, allocation )
            else:
                self.temp_count2 += 1
                self.pat_listbox2.insert( self.temp_count2, allocation )
        
        # Buttons
        self.back_BTN  =  self.create_text_BTN(root, text_label= 'BACK', execute_cmd= self.mem_map_window, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(200, 550))
        self.next_BTN  =  self.create_text_BTN(root, text_label= 'NEXT', execute_cmd= self.fat_window, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(580, 550))
        self.exit_BTN  =  self.create_text_BTN(root, text_label= 'Exit', execute_cmd= root.destroy, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(390, 550))


    def fat_window( self ):
        self.clear_widgets()
        self.basic_widget_list = []

        self.dynamicBestFitGB = self.create_BG(root, dbf_bg, bg_clr="black", placement=(0, 0))
        
        self.create_clock(date_placement= (170, 50), clock_placement= (700, 50), bg_clr= "#D3BAF4")

        self.title1_LBL = self.create_text_LBL(root, lbl_text= self.title1_text, font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=self.title1_placement)
        self.title2_LBL = self.create_text_LBL(root, lbl_text= "Partitioned Allocation", font_label=('Times New Roman', 20), bg_clr="#D3BAF4", placement=(345, 65))

        self.title3_LBL = self.create_text_LBL(root, lbl_text= "File Allocation Table", font_label=('Times New Roman', 30), bg_clr="#0096FF", placement=(305, 126))
        self.title4_LBL = self.create_text_LBL(root, lbl_text= f"At {self.memory_result_time[0]}", font_label=('Times New Roman', 12), bg_clr="#0096FF", placement=(425, 178))

        # FAT Number Widgets
        self.fat_num_LBL = self.create_text_LBL(root, lbl_text= "Partition #", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(100, 200))
        self.fat_num1_LBL = self.create_text_LBL(root, lbl_text= "1", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 240))
        self.fat_num2_LBL = self.create_text_LBL(root, lbl_text= "2", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 280))
        self.fat_num3_LBL = self.create_text_LBL(root, lbl_text= "3", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 320))
        self.fat_num4_LBL = self.create_text_LBL(root, lbl_text= "4", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 360))
        self.fat_num5_LBL = self.create_text_LBL(root, lbl_text= "5", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(135, 400))

        # FAT Size Entries
        self.fat_size_LBL = self.create_text_LBL(root, lbl_text= "Size", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(277, 200))
        self.fat_size1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 240), state="readonly", text=self.fatData[0][0])
        self.fat_size2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 280), state="readonly", text=self.fatData[1][0])
        self.fat_size3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 320), state="readonly", text=self.fatData[2][0])
        self.fat_size4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 360), state="readonly", text=self.fatData[3][0])
        self.fat_size5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(225, 400), state="readonly", text=self.fatData[4][0])

        # FAT Location Widgets
        self.fat_location_LBL = self.create_text_LBL(root, lbl_text= "Location", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(522, 200))
        self.fat_location1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 240), state="readonly", text=self.fatData[0][1])
        self.fat_location2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 280), state="readonly", text=self.fatData[1][1])
        self.fat_location3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 320), state="readonly", text=self.fatData[2][1])
        self.fat_location4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 360), state="readonly", text=self.fatData[3][1])
        self.fat_location5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(490, 400), state="readonly", text=self.fatData[4][1])
        
        # FAT Status Widgets
        self.fat_statusLBL = self.create_text_LBL(root, lbl_text= "Status", font_label=('Times New Roman', 15), bg_clr="#0096FF", placement=(740, 200))
        self.fat_status1_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 240), state="readonly", text=self.fatData[0][2])
        self.fat_status2_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 280), state="readonly", text=self.fatData[1][2])
        self.fat_status3_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 320), state="readonly", text=self.fatData[2][2])
        self.fat_status4_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 360), state="readonly", text=self.fatData[3][2])
        self.fat_status5_ENTRY = self.create_ENTRY(root, font_label=('Consolas', 10, 'bold'), justify="center",
                                            placement=(700, 400), state="readonly", text=self.fatData[4][2])

        # Listbox Widgets
        self.fat_listbox1 = self.create_LISTBOX(HWB= (5, 40, 0), placement=(220, 450), justify = "center")
        self.fat_listbox2 = self.create_LISTBOX(HWB= (5, 40, 0), placement=(480, 450), justify = "center")

        self.temp_count1 = 0
        self.temp_count2 = 0
        for allocation in self.memory_result_time[1]:
            if allocation[0] == "A":
                self.temp_count1 += 1
                self.fat_listbox1.insert( self.temp_count1, allocation )
            else:
                self.temp_count2 += 1
                self.fat_listbox2.insert( self.temp_count2, allocation )

        # Buttons
        self.back_BTN  =  self.create_text_BTN(root, text_label= 'BACK', execute_cmd= self.pat_window, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(200, 550))
        if self.next_pointer == None:
            self.next_BTN  =  self.create_text_BTN(root, text_label= 'Try New Input', execute_cmd= self.fat_next_BTN_Pressed, font_label=('Consolas', 16, 'bold'), width_label=13, bg_clr="#B3B3B3", placement=(580, 550))
        else:
            self.next_BTN  =  self.create_text_BTN(root, text_label= 'Next', execute_cmd= self.fat_next_BTN_Pressed, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(580, 550))
        self.exit_BTN  =  self.create_text_BTN(root, text_label= 'Exit', execute_cmd= root.destroy, font_label=('Consolas', 16, 'bold'), width_label=12, bg_clr="#B3B3B3", placement=(390, 550))

    def fat_next_BTN_Pressed( self ):
        if self.next_pointer == None:
            dynamic_best_fit_program.input1_window()
        else:
            self.next_pointer.mem_map_window()
# END OF DBF PROGRAM: 4435-6027

# START OF DWF PROGRAM
class Dynamic_Worst_Fit_Backend (Dynamic_Best_Fit_Backend):
    def __init__( self ):
        super().__init__()
    
    def allocate(self, memory, job):
        # job [ job id, a/f( allocate/deallocate ), job size ]
        self.j_id = job[0]
        self.j_size = job[2]
        # if the memory list is empty, immediately return
        if memory is None:
            return
        # sorts the memory list by the memory space in descending order.
        self.m_sorted = sorted(memory, key=lambda x: x[0], reverse=True)
        # i: id for the memory space/partition
        # m: F for free/available memory space,
        #    U for occupied memory space.
        # This loop traverses the memory list so that a job can be allocated to the 
        # worst memory space which meets the needs of the job.
        for ms in reversed(self.m_sorted):
            if ms[1] == 'F' and ms[0] >= self.j_size:
                break
        for i, m in enumerate(memory):
            if m[1] == 'F' and m[0] == ms[0]:
                memory.insert(i + 1, [m[0] - self.j_size, 'F', -1])
                try:
                    if memory[i + 2][1] == 'F':
                        memory[i + 1][0] += memory[i + 2][0]
                        memory.pop(i + 2)
                except IndexError:
                    pass

                m[0] = self.j_size
                m[1] = 'U'
                m[2] = self.j_id
                return memory


class Dynamic_Worst_Fit_Frontend(Dynamic_Best_Fit_Frontend):
    def __init__( self ):
        super().__init__()
        self.title1_text = "Dynamic Worst Fit"
        self.title1_placement = (363, 20)
        
        self.backend = Dynamic_Worst_Fit_Backend()

class Dynamic_Worst_Fit_Node(Dynamic_Best_Fit_Node):
    def __init__ ( self, memory_result = None, memory_result_time = None, os_size = None, memory_size = None):
        super().__init__()
        self.back_pointer = None
        self.next_pointer = None
        self.patData = []
        self.fatData = []
        self.location = 0

        self.title1_text = "Dynamic Worst Fit"
        self.title1_placement = (363, 20)
# END OF DWF PROGRAM

# START OF STATIC BEST FIT (SBF) PROGRAM
class SBF_Node (Node):
    def __init__( self, time = "*:**:**" , data = None, time_type = "After", text_title = "Jx Terminated" ):
        super().__init__()
        self.back_pointer = None
        self.next_pointer = None
        self.data = data
        self.time = time
        self.time_type = time_type
        self.text_title = text_title
        if self.data == None:
            self.data = [ "Available", "Available", "Available", "Available", "Available" ]
        
        self.title1_text = "Static Best Fit"
        self.title1_placement = (400, 20)
    
    # This function points which window to go back on.
    def mem_map_back_BTN_Pressed( self ):
        if self.back_pointer == None:
            static_best_fit_program.main_result1_window()
        else:
            self.back_pointer.pat_window()
    
    # This function points which window to go next.
    def pat_next_BTN_Pressed( self ):
        if self.next_pointer == None:
            static_best_fit_program.main_input1_window()
        else:
            self.next_pointer.mem_map_window()
    

class Static_Best_Fit(Static_First_Fit):
    def __init__ ( self ):
        super().__init__()

        self.title1_text = "Static Best Fit"
        self.title1_placement = (400, 20)
    
    def add_result_node( self, time, result_data, time_type, text_title ): # ( self, time = "9:00:00" , data = None, time_type = "At", text_title = "Jx removed" ):
        print( time, result_data, time_type, text_title )
        self.temp_node = SBF_Node( time, result_data, time_type, text_title )

        if self.head_node == None:
            self.head_node = self.temp_node
        else:
            self.head_node.back_pointer = self.temp_node
            self.temp_node.next_pointer = self.head_node

            self.head_node = self.temp_node
        return
    
    def create_result_windows( self, all_job_sizes, all_job_arrival_time, all_job_run_time, all_partition_sizes):
        global partition1
        global partition2
        global partition3
        global partition4
        global partition5
        global partition_sizes

        global os_size
        global memory_size

        global size1
        global size2
        global size3
        global size4
        global size5
        global job_sizes

        global os_percentage
        global partition1_percentage
        global partition2_percentage
        global partition3_percentage
        global partition4_percentage
        global partition5_percentage
        global all_partition_percentage
        
        self.clear_nodes()
        
        job_sizes = all_job_sizes
        self.all_job_arrival_time = all_job_arrival_time
        self.all_job_run_time = all_job_run_time
        partition_sizes = all_partition_sizes
        self.partitionState = [False, False, False, False, False]
        self.job_state = [False, False, False, False, False]
        self.partition_history = [[], [], [], [], []]
        self.time_zero = datetime.datetime.strptime('00:00', '%H:%M')
        self.all_job_results = [[], [], [], [], []]
        self.pat_status1 = [["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"]]
        self.pat_status2 = [["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"]]
        self.all_start_time = []
        self.all_finish_time = []
        waiting_list = [] 

        def find_best_fit_partition(size, job_num=None):
            best_fit_index = -1
            for i in range(len(partition_sizes)):
                if int(partition_sizes[i]) >= int(size) and self.partitionState[i] == False:
                    if best_fit_index == -1 or int(partition_sizes[i]) < int(partition_sizes[best_fit_index]):
                        best_fit_index = i
            if best_fit_index == -1 and job_num != None:
                # No suitable partition found, add job to waiting list
                waiting_list.append(job_num)
            return best_fit_index

        i = 0
        while i < 5 or waiting_list:
            if i < 5:
                best_fit_index = find_best_fit_partition(job_sizes[i], i)
                if best_fit_index != -1:
                    self.partitionState[best_fit_index] = True
                    self.job_state[i] = True

                    if len(self.partition_history[best_fit_index]) == 0:
                        self.temp_start_time = datetime.datetime.strptime(self.all_job_arrival_time[i], '%H:%M')
                    else:
                        self.temp_start_time = self.partition_history[best_fit_index][-1]

                    if (self.temp_start_time - datetime.datetime.strptime(self.all_job_arrival_time[i], '%H:%M')).total_seconds() < 0:
                        self.temp_cpu_wait = "0:00:00"
                        self.temp_start_time = datetime.datetime.strptime(self.all_job_arrival_time[i], '%H:%M')
                    else:
                        self.temp_cpu_wait = self.temp_start_time - datetime.datetime.strptime(self.all_job_arrival_time[i], '%H:%M')

                    self.all_start_time.append(self.temp_start_time.time())
                    self.all_job_results[i].append(self.temp_start_time)

                    self.temp_finish_time = (self.temp_start_time - self.time_zero + (datetime.datetime.strptime(self.all_job_run_time[i], '%H:%M')))
                    self.all_finish_time.append(self.temp_finish_time.time())
                    self.partition_history[best_fit_index].append(self.temp_finish_time)
                    self.all_job_results[i].append(self.temp_finish_time)

                    self.all_job_results[i].append(self.temp_cpu_wait)
                    self.all_job_results[i].append(best_fit_index)
                    self.all_job_results[i].append(i)
                    self.all_job_results[i].append("After")
                i += 1
            else:
                # Process jobs from waiting list
                for job in waiting_list:
                    best_fit_index = find_best_fit_partition(job_sizes[job])
                    if best_fit_index != -1:
                        self.partitionState[best_fit_index] = True
                        self.job_state[job] = True

                        if len(self.partition_history[best_fit_index]) == 0:
                            self.temp_start_time = datetime.datetime.strptime(self.all_job_arrival_time[job], '%H:%M')
                        else:
                            self.temp_start_time = self.partition_history[best_fit_index][-1]

                        if (self.temp_start_time - datetime.datetime.strptime(self.all_job_arrival_time[job], '%H:%M')).total_seconds() < 0:
                            self.temp_cpu_wait = "0:00:00"
                            self.temp_start_time = datetime.datetime.strptime(self.all_job_arrival_time[job], '%H:%M')
                        else:
                            self.temp_cpu_wait = self.temp_start_time - datetime.datetime.strptime(self.all_job_arrival_time[job], '%H:%M')

                        self.all_start_time.append(self.temp_start_time.time())
                        self.all_job_results[job].append(self.temp_start_time)

                        self.temp_finish_time = (self.temp_start_time - self.time_zero + (datetime.datetime.strptime(self.all_job_run_time[job], '%H:%M')))
                        self.all_finish_time.append(self.temp_finish_time.time())
                        self.partition_history[best_fit_index].append(self.temp_finish_time)
                        self.all_job_results[job].append(self.temp_finish_time)

                        self.all_job_results[job].append(self.temp_cpu_wait)
                        self.all_job_results[job].append(best_fit_index)
                        self.all_job_results[job].append(i)
                        self.all_job_results[job].append("After")

                        waiting_list.remove(job)
                    # Clear the waiting list if it is empty after processing
                    if not waiting_list:
                        break
    

        for i in range(5):
            self.temp_check_time = self.all_job_results[i][0]
            self.temp_check_time2 = self.all_job_results[i][1] + datetime.timedelta(seconds=1)
            for j in range(5):
                self.temp_begin_time = self.all_job_results[j][0]
                self.temp_end_time = self.all_job_results[j][1]

                self.temp_status = self.is_time_between(self.temp_begin_time, self.temp_end_time, self.temp_check_time)
                self.temp_status2 = self.is_time_between(self.temp_begin_time, self.temp_end_time, self.temp_check_time2)
                if self.temp_status == True:
                    self.pat_status1[i][self.all_job_results[j][3]] = "Allocated(J{})".format(self.all_job_results[j][4] + 1)
                if self.temp_status2 == True:
                    self.pat_status2[i][self.all_job_results[j][3]] = "Allocated(J{})".format(self.all_job_results[j][4] + 1)

        self.add_result_node(self.all_finish_time[4], self.pat_status2[4], "After", "J5 Terminated")
        self.add_result_node(self.all_start_time[4], self.pat_status1[4], "At", "J5 Started")

        self.add_result_node(self.all_finish_time[3], self.pat_status2[3], "After", "J4 Terminated")
        self.add_result_node(self.all_start_time[3], self.pat_status1[3], "At", "J4 Started")

        self.add_result_node(self.all_finish_time[2], self.pat_status2[2], "After", "J3 Terminated")
        self.add_result_node(self.all_start_time[2], self.pat_status1[2], "At", "J3 Started")

        self.add_result_node(self.all_finish_time[1], self.pat_status2[1], "After", "J2 Terminated")
        self.add_result_node(self.all_start_time[1], self.pat_status1[1], "At", "J2 Started")

        self.add_result_node(self.all_finish_time[0], self.pat_status2[0], "After", "J1 Terminated")
        self.add_result_node(self.all_start_time[0], self.pat_status1[0], "At", "J1 Started")

        self.main_result1_window()
# END OF STATIC BEST FIT

# START OF STATIC WORST FIT
class SWF_Node (Node):
    def __init__( self, time = "*:**:**" , data = None, time_type = "After", text_title = "Jx Terminated" ):
        super().__init__()
        self.back_pointer = None
        self.next_pointer = None
        self.data = data
        self.time = time
        self.time_type = time_type
        self.text_title = text_title
        if self.data == None:
            self.data = [ "Available", "Available", "Available", "Available", "Available" ]
        
        self.title1_text = "Static Worst Fit"
        self.title1_placement = (400, 20)
    
    # This function points which window to go back on.
    def mem_map_back_BTN_Pressed( self ):
        if self.back_pointer == None:
            static_worst_fit_program.main_result1_window()
        else:
            self.back_pointer.pat_window()
    
    # This function points which window to go next.
    def pat_next_BTN_Pressed( self ):
        if self.next_pointer == None:
            static_worst_fit_program.main_input1_window()
        else:
            self.next_pointer.mem_map_window()
    

class Static_Worst_Fit(Static_First_Fit):
    def __init__ ( self ):
        super().__init__()

        self.title1_text = "Static Worst Fit"
        self.title1_placement = (400, 20)
    
    def add_result_node( self, time, result_data, time_type, text_title ): # ( self, time = "9:00:00" , data = None, time_type = "At", text_title = "Jx removed" ):
        print( time, result_data, time_type, text_title )
        self.temp_node = SWF_Node( time, result_data, time_type, text_title )

        if self.head_node == None:
            self.head_node = self.temp_node
        else:
            self.head_node.back_pointer = self.temp_node
            self.temp_node.next_pointer = self.head_node

            self.head_node = self.temp_node
        return
    
    def create_result_windows( self, all_job_sizes, all_job_arrival_time, all_job_run_time, all_partition_sizes):
        global partition1
        global partition2
        global partition3
        global partition4
        global partition5
        global partition_sizes

        global os_size
        global memory_size

        global size1
        global size2
        global size3
        global size4
        global size5
        global job_sizes

        global os_percentage
        global partition1_percentage
        global partition2_percentage
        global partition3_percentage
        global partition4_percentage
        global partition5_percentage
        global all_partition_percentage
        
        self.clear_nodes()
        
        job_sizes = all_job_sizes
        self.all_job_arrival_time = all_job_arrival_time
        self.all_job_run_time = all_job_run_time
        partition_sizes = all_partition_sizes
        self.partitionState = [False, False, False, False, False]
        self.job_state = [False, False, False, False, False]
        self.partition_history = [[], [], [], [], []]
        self.time_zero = datetime.datetime.strptime('00:00', '%H:%M')
        self.all_job_results = [[], [], [], [], []]
        self.pat_status1 = [["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"]]
        self.pat_status2 = [["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"],
                            ["Available", "Available", "Available", "Available", "Available"]]
        self.all_start_time = []
        self.all_finish_time = []

        def find_best_fit_partition(size):
            best_fit_index = -1
            for i in range(len(partition_sizes)):
                if int(partition_sizes[i]) >= int(size) and self.partitionState[i] == False:
                    if best_fit_index == -1 or int(partition_sizes[i]) < int(partition_sizes[best_fit_index]):
                        best_fit_index = i
            return best_fit_index

        for i in range(5):
            best_fit_index = find_best_fit_partition(job_sizes[i])
            if best_fit_index != -1:
                self.partitionState[best_fit_index] = True
                self.job_state[i] = True

                if len(self.partition_history[best_fit_index]) == 0:
                    self.temp_start_time = datetime.datetime.strptime(self.all_job_arrival_time[i], '%H:%M')
                else:
                    self.temp_start_time = self.partition_history[best_fit_index][-1]

                if (self.temp_start_time - datetime.datetime.strptime(self.all_job_arrival_time[i], '%H:%M')).total_seconds() < 0:
                    self.temp_cpu_wait = "0:00:00"
                    self.temp_start_time = datetime.datetime.strptime(self.all_job_arrival_time[i], '%H:%M')
                else:
                    self.temp_cpu_wait = self.temp_start_time - datetime.datetime.strptime(self.all_job_arrival_time[i], '%H:%M')

                self.all_start_time.append(self.temp_start_time.time())
                self.all_job_results[i].append(self.temp_start_time)

                self.temp_finish_time = (self.temp_start_time - self.time_zero + (datetime.datetime.strptime(self.all_job_run_time[i], '%H:%M')))
                self.all_finish_time.append(self.temp_finish_time.time())
                self.partition_history[best_fit_index].append(self.temp_finish_time)
                self.all_job_results[i].append(self.temp_finish_time)

                self.all_job_results[i].append(self.temp_cpu_wait)
                self.all_job_results[i].append(best_fit_index)
                self.all_job_results[i].append(i)
                self.all_job_results[i].append("After")

        for i in range(5):
            self.temp_check_time = self.all_job_results[i][0]
            self.temp_check_time2 = self.all_job_results[i][1] + datetime.timedelta(seconds=1)
            for j in range(5):
                self.temp_begin_time = self.all_job_results[j][0]
                self.temp_end_time = self.all_job_results[j][1]

                self.temp_status = self.is_time_between(self.temp_begin_time, self.temp_end_time, self.temp_check_time)
                self.temp_status2 = self.is_time_between(self.temp_begin_time, self.temp_end_time, self.temp_check_time2)
                if self.temp_status == True:
                    self.pat_status1[i][self.all_job_results[j][3]] = "Allocated(J{})".format(self.all_job_results[j][4] + 1)
                if self.temp_status2 == True:
                    self.pat_status2[i][self.all_job_results[j][3]] = "Allocated(J{})".format(self.all_job_results[j][4] + 1)

        self.add_result_node(self.all_finish_time[4], self.pat_status2[4], "After", "J5 Terminated")
        self.add_result_node(self.all_start_time[4], self.pat_status1[4], "At", "J5 Started")

        self.add_result_node(self.all_finish_time[3], self.pat_status2[3], "After", "J4 Terminated")
        self.add_result_node(self.all_start_time[3], self.pat_status1[3], "At", "J4 Started")

        self.add_result_node(self.all_finish_time[2], self.pat_status2[2], "After", "J3 Terminated")
        self.add_result_node(self.all_start_time[2], self.pat_status1[2], "At", "J3 Started")

        self.add_result_node(self.all_finish_time[1], self.pat_status2[1], "After", "J2 Terminated")
        self.add_result_node(self.all_start_time[1], self.pat_status1[1], "At", "J2 Started")

        self.add_result_node(self.all_finish_time[0], self.pat_status2[0], "After", "J1 Terminated")
        self.add_result_node(self.all_start_time[0], self.pat_status1[0], "At", "J1 Started")

        self.main_result1_window()

# END OF STATIC WORST FIT



main_program = Main()
single_contiguous_program = Single_Contiguous_Program()

static_first_fit_program = Static_First_Fit()
static_best_fit_program = Static_Best_Fit()
static_worst_fit_program = Static_Worst_Fit()

dynamic_first_fit_program = Dynamic_First_Fit_Frontend()
dynamic_best_fit_program = Dynamic_Best_Fit_Frontend()
dynamic_worst_fit_program = Dynamic_Worst_Fit_Frontend()

main_program.main_menu_window()
root.mainloop()