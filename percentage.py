# Created by: Younes Elfeitori
# Created on: Nov 2017
# Created for: ICS3U
# This program converts marks that are in level form to percentage

import ui

def calculate_level_to_percentage_button(level):
    
    if level == "4+":
        return "95%"
        
    elif level == "4":
        return "90%"
        
    elif level == "4-":
        return "85%"
        
    elif level == "3+":
        return "80%"
        
    elif level == "3":
        return "75%"
        
    elif level == "3-":
        return "70%"
        
    elif level == "2+":
        return "65%"
        
    elif level == "2":
        return "60%"
        
    elif level == "2-":
        return "55%"
        
    elif level == "1+":
        return "50%"
        
    elif level == "1":
        return "45%"
        
    elif level == "1-":
        return "40%"
        
    elif level == "R":
        return "30%"
        
    elif level == "NE":
        return "0%"
    
    else :
        return "-1"
    
    

def convert_level_to_percentage_button_touch_up_inside(sender):

    level = view['level_textfield'].text
    
    percentage = calculate_level_to_percentage_button (level)
    
    view['percentage_label'].text = percentage


view = ui.load_view()
view.present('full_screen')
