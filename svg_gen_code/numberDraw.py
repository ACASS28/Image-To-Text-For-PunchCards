import svgwrite

def draw_numbers(number,right_xoffset,left_xoffset,yoffset,objects,diagram):
    
     if(number<10):
          
          draw_single_numbers(number,right_xoffset,left_xoffset,yoffset,objects,diagram)
          
     elif(number<100):
        
          first_digit = int(str(number)[0])  
          second_digit = int(str(number)[1])  
          draw_left_numbers(second_digit,3.5/2,right_xoffset,yoffset,objects,diagram)
          draw_right_numbers(first_digit,right_xoffset-(3.5/2),yoffset,objects,diagram)
     else:
          first_digit = int(str(number)[0])  
          second_digit = int(str(number)[1]) 
          third_digit =  int(str(number)[2]) 
          draw_left_numbers(third_digit,3.5/2,right_xoffset+(3.5/2),yoffset,objects,diagram)
          draw_left_numbers(second_digit,3.5/2,right_xoffset,yoffset,objects,diagram)
          draw_right_numbers(first_digit,right_xoffset-((3.5/2)),yoffset,objects,diagram)
          
'''
numbers less then 9
'''
def draw_single_numbers(number,right_xoffset,left_xoffset,yoffset,objects,diagram):
        diameter = 3.5
        numberOffset = diameter/2
        if(number == 1):
            objects.append(diagram.line(
                start=(right_xoffset + diameter, yoffset + diameter-numberOffset),  # Start of the base
                end=(left_xoffset - diameter, yoffset + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
       # Draw the vertical line (main stem)
            objects.append(diagram.line(
            start=(right_xoffset, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset, yoffset + diameter-.5-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))

        # Optional: Draw the base line (bottom of the "1")
            objects.append(diagram.line(
                start=(right_xoffset - diameter / 4, yoffset-.5 + diameter-numberOffset),  # Start of the base
                end=(right_xoffset + diameter / 4, yoffset-.5 + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))

        # Optional: Draw a small horizontal line at the top for a stylized "1"
            objects.append(diagram.line(
                start=(right_xoffset - diameter / 6, yoffset + diameter / 4-numberOffset),  # Start of the top line
                end=(right_xoffset , yoffset-numberOffset),  # End of the top line
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
        elif(number == 2):
            #top line
            objects.append(diagram.line(
                start=(right_xoffset - diameter / 4, yoffset-numberOffset),  # Start of the base
                end=(right_xoffset + diameter / 4, yoffset-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #middle line
            objects.append(diagram.line(
                start=(right_xoffset - diameter / 4, yoffset + diameter/2-numberOffset),  # Start of the base
                end=(right_xoffset + diameter / 4, yoffset + diameter/2-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))

         #bottom line
            objects.append(diagram.line(
                start=(right_xoffset - diameter / 4, yoffset + diameter-numberOffset),  # Start of the base
                end=(right_xoffset + diameter / 4, yoffset + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))

            objects.append(diagram.line(
            start=(right_xoffset+ diameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset+ diameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))

            objects.append(diagram.line(
            start=(right_xoffset- diameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset- diameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))

        elif(number == 3):
            objects.append(diagram.line(
                start=(right_xoffset - diameter / 4, yoffset-numberOffset),  # Start of the base
                end=(right_xoffset + diameter / 4, yoffset-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #middle line
            objects.append(diagram.line(
                start=(right_xoffset - diameter / 4, yoffset + diameter/2-numberOffset),  # Start of the base
                end=(right_xoffset + diameter / 4, yoffset + diameter/2-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))

         #bottom line
            objects.append(diagram.line(
                start=(right_xoffset - diameter / 4, yoffset + diameter-numberOffset),  # Start of the base
                end=(right_xoffset + diameter / 4, yoffset + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #left top vertical
            objects.append(diagram.line(
            start=(right_xoffset+ diameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset+ diameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
            #left bottom vertical
            objects.append(diagram.line(
            start=(right_xoffset+ diameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset+ diameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))

        elif(number == 4):
             objects.append(diagram.line(
            start=(right_xoffset+ diameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset+ diameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             
             objects.append(diagram.line(
            start=(right_xoffset- diameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset- diameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             
             objects.append(diagram.line(
                start=(right_xoffset - diameter / 4, yoffset + diameter/2-numberOffset),  # Start of the base
                end=(right_xoffset + diameter / 4, yoffset + diameter/2-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
             
             objects.append(diagram.line(
            start=(right_xoffset+ diameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset+ diameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
        elif(number == 5):
            objects.append(diagram.line(
                start=(right_xoffset - diameter / 4, yoffset-numberOffset),  # Start of the base
                end=(right_xoffset + diameter / 4, yoffset-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #middle line
            objects.append(diagram.line(
                start=(right_xoffset - diameter / 4, yoffset + diameter/2-numberOffset),  # Start of the base
                end=(right_xoffset + diameter / 4, yoffset + diameter/2-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))

         #bottom line
            objects.append(diagram.line(
                start=(right_xoffset - diameter / 4, yoffset + diameter-numberOffset),  # Start of the base
                end=(right_xoffset + diameter / 4, yoffset + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #right top vertical
            objects.append(diagram.line(
            start=(right_xoffset- diameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset- diameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
            #left bottom vertical
            objects.append(diagram.line(
            start=(right_xoffset+ diameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset+ diameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
        elif(number == 6):
             objects.append(diagram.line(
                start=(right_xoffset - diameter / 4, yoffset-numberOffset),  # Start of the base
                end=(right_xoffset + diameter / 4, yoffset-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #middle line
             objects.append(diagram.line(
                start=(right_xoffset - diameter / 4, yoffset + diameter/2-numberOffset),  # Start of the base
                end=(right_xoffset + diameter / 4, yoffset + diameter/2-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))

         #bottom line
             objects.append(diagram.line(
                start=(right_xoffset - diameter / 4, yoffset + diameter-numberOffset),  # Start of the base
                end=(right_xoffset + diameter / 4, yoffset + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #right top vertical
             objects.append(diagram.line(
            start=(right_xoffset- diameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset- diameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             
            #left bottom vertical
             objects.append(diagram.line(
            start=(right_xoffset+ diameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset+ diameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             #right bottom vertical
             objects.append(diagram.line(
            start=(right_xoffset- diameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset- diameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
        elif(number == 7):
           objects.append(diagram.line(
                start=(right_xoffset - diameter / 4, yoffset-numberOffset),  # Start of the base
                end=(right_xoffset + diameter / 4, yoffset-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
           objects.append(diagram.line(
            start=(right_xoffset+ diameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset- diameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
           ))
        elif(number == 8):
             objects.append(diagram.line(
                start=(right_xoffset - diameter / 4, yoffset-numberOffset),  # Start of the base
                end=(right_xoffset + diameter / 4, yoffset-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #middle line
             objects.append(diagram.line(
                start=(right_xoffset - diameter / 4, yoffset + diameter/2-numberOffset),  # Start of the base
                end=(right_xoffset + diameter / 4, yoffset + diameter/2-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))

         #bottom line
             objects.append(diagram.line(
                start=(right_xoffset - diameter / 4, yoffset + diameter-numberOffset),  # Start of the base
                end=(right_xoffset + diameter / 4, yoffset + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #right top vertical
             objects.append(diagram.line(
            start=(right_xoffset- diameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset- diameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             #left top vertical
             objects.append(diagram.line(
            start=(right_xoffset +diameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset+ diameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             
            #left bottom vertical
             objects.append(diagram.line(
            start=(right_xoffset+ diameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset+ diameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             #right bottom vertical
             objects.append(diagram.line(
            start=(right_xoffset- diameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset- diameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
        elif(number == 9):
             objects.append(diagram.line(
                start=(right_xoffset - diameter / 4, yoffset-numberOffset),  # Start of the base
                end=(right_xoffset + diameter / 4, yoffset-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #middle line
             objects.append(diagram.line(
                start=(right_xoffset - diameter / 4, yoffset + diameter/2-numberOffset),  # Start of the base
                end=(right_xoffset + diameter / 4, yoffset + diameter/2-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))

         #bottom line
             objects.append(diagram.line(
                start=(right_xoffset - diameter / 4, yoffset + diameter-numberOffset),  # Start of the base
                end=(right_xoffset + diameter / 4, yoffset + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #right top vertical
             objects.append(diagram.line(
            start=(right_xoffset- diameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset- diameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             #left top vertical
             objects.append(diagram.line(
            start=(right_xoffset +diameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset+ diameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             
             #right bottom vertical
             objects.append(diagram.line(
            start=(right_xoffset+ diameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset+ diameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
        elif(number == 0):
             objects.append(diagram.line(
                start=(right_xoffset - diameter / 4, yoffset-numberOffset),  # Start of the base
                end=(right_xoffset + diameter / 4, yoffset-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
           

         #bottom line
             objects.append(diagram.line(
                start=(right_xoffset - diameter / 4, yoffset + diameter-numberOffset),  # Start of the base
                end=(right_xoffset + diameter / 4, yoffset + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #right  vertical
             objects.append(diagram.line(
            start=(right_xoffset- diameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset- diameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             #left  vertical
             objects.append(diagram.line(
            start=(right_xoffset +diameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset+ diameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             objects.append(diagram.line(
            start=(right_xoffset- diameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset+ diameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
           ))
             
            

        # Optional: Draw a small horizontal line at the top for a stylized "1"
            

'''
numbers that are greater then 9 on the left
'''
def draw_left_numbers(number,doubleDiameter,right_xoffset,yoffset,objects,diagram):
        diameter = 3.5
        numberOffset = diameter/2
        doubleDiameter = diameter/2

        if(number == 1):
       # Draw the vertical line (main stem)
            objects.append(diagram.line(
            start=(right_xoffset, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))

        # Optional: Draw the base line (bottom of the "1")
            objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset + diameter-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))

        # Optional: Draw a small horizontal line at the top for a stylized "1"
            objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 6, yoffset + diameter / 4-numberOffset),  # Start of the top line
                end=(right_xoffset , yoffset-numberOffset),  # End of the top line
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
        elif(number == 2):
            #top line
            objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #middle line
            objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))

         #bottom line
            objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset + diameter-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))

            objects.append(diagram.line(
            start=(right_xoffset+ doubleDiameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))

            objects.append(diagram.line(
            start=(right_xoffset- doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset- doubleDiameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))

        elif(number == 3):
            objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #middle line
            objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))

         #bottom line
            objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset + diameter-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #left top vertical
            objects.append(diagram.line(
            start=(right_xoffset+ doubleDiameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
            #left bottom vertical
            objects.append(diagram.line(
            start=(right_xoffset+ doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))

        elif(number == 4):
             objects.append(diagram.line(
            start=(right_xoffset+ doubleDiameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             
             objects.append(diagram.line(
            start=(right_xoffset- doubleDiameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset- doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             
             objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
             
             objects.append(diagram.line(
            start=(right_xoffset+ doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
        elif(number == 5):
            objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #middle line
            objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))

         #bottom line
            objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset + diameter-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #right top vertical
            objects.append(diagram.line(
            start=(right_xoffset- doubleDiameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset- doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
            #left bottom vertical
            objects.append(diagram.line(
            start=(right_xoffset+ doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
        elif(number == 6):
             objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #middle line
             objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))

         #bottom line
             objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset + diameter-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #right top vertical
             objects.append(diagram.line(
            start=(right_xoffset- doubleDiameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset- doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             
            #left bottom vertical
             objects.append(diagram.line(
            start=(right_xoffset+ doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             #right bottom vertical
             objects.append(diagram.line(
            start=(right_xoffset- doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset- doubleDiameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
        elif(number == 7):
           objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset-numberOffset),  # Start of the base
                end=(right_xoffset +doubleDiameter / 4, yoffset-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
           objects.append(diagram.line(
            start=(right_xoffset+ doubleDiameter/ 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset- doubleDiameter/ 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
           ))
        elif(number == 8):
             objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #middle line
             objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter/ 4, yoffset + diameter/2-numberOffset),  # Start of the base
                end=(right_xoffset +doubleDiameter/ 4, yoffset + diameter/2-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))

         #bottom line
             objects.append(diagram.line(
                start=(right_xoffset -doubleDiameter / 4, yoffset + diameter-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #right top vertical
             objects.append(diagram.line(
            start=(right_xoffset- doubleDiameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset- doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             #left top vertical
             objects.append(diagram.line(
            start=(right_xoffset +doubleDiameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             
            #left bottom vertical
             objects.append(diagram.line(
            start=(right_xoffset+ doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             #right bottom vertical
             objects.append(diagram.line(
            start=(right_xoffset- doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset- doubleDiameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
        elif(number == 9):
             objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #middle line
             objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Start of the base
                end=(right_xoffset +doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))

         #bottom line
             objects.append(diagram.line(
                start=(right_xoffset -doubleDiameter / 4, yoffset + diameter-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter/ 4, yoffset + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #right top vertical
             objects.append(diagram.line(
            start=(right_xoffset- doubleDiameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset- doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             #left top vertical
             objects.append(diagram.line(
            start=(right_xoffset +doubleDiameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             
             #right bottom vertical
             objects.append(diagram.line(
            start=(right_xoffset+ doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
        elif(number == 0):
             objects.append(diagram.line(
                start=(right_xoffset -doubleDiameter / 4, yoffset-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
           

         #bottom line
             objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset + diameter-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #right  vertical
             objects.append(diagram.line(
            start=(right_xoffset- doubleDiameter/ 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset- doubleDiameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             #left  vertical
             objects.append(diagram.line(
            start=(right_xoffset +doubleDiameter/ 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             objects.append(diagram.line(
            start=(right_xoffset- doubleDiameter/ 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter/ 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
           ))


'''
numbers that are greater then 9 on the left
'''   
def draw_right_numbers(number,right_xoffset,yoffset,objects,diagram):
        diameter = 3.5
        numberOffset = diameter/2
        doubleDiameter = diameter/2
        

        if(number == 1):
       # Draw the vertical line (main stem)
            objects.append(diagram.line(
            start=(right_xoffset, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))

        # Optional: Draw the base line (bottom of the "1")
            objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset + diameter-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))

        # Optional: Draw a small horizontal line at the top for a stylized "1"
            objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 6, yoffset + diameter / 4-numberOffset),  # Start of the top line
                end=(right_xoffset , yoffset-numberOffset),  # End of the top line
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
        elif(number == 2):
            #top line
            objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #middle line
            objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))

         #bottom line
            objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset + diameter-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))

            objects.append(diagram.line(
            start=(right_xoffset+ doubleDiameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))

            objects.append(diagram.line(
            start=(right_xoffset- doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset- doubleDiameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))

        elif(number == 3):
            objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #middle line
            objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))

         #bottom line
            objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset + diameter-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #left top vertical
            objects.append(diagram.line(
            start=(right_xoffset+ doubleDiameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
            #left bottom vertical
            objects.append(diagram.line(
            start=(right_xoffset+ doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))

        elif(number == 4):
             objects.append(diagram.line(
            start=(right_xoffset+ doubleDiameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             
             objects.append(diagram.line(
            start=(right_xoffset- doubleDiameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset- doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             
             objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
             
             objects.append(diagram.line(
            start=(right_xoffset+ doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
        elif(number == 5):
            objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #middle line
            objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))

         #bottom line
            objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset + diameter-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #right top vertical
            objects.append(diagram.line(
            start=(right_xoffset- doubleDiameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset- doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
            #left bottom vertical
            objects.append(diagram.line(
            start=(right_xoffset+ doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
        elif(number == 6):
             objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #middle line
             objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))

         #bottom line
             objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset + diameter-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #right top vertical
             objects.append(diagram.line(
            start=(right_xoffset- doubleDiameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset- doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             
            #left bottom vertical
             objects.append(diagram.line(
            start=(right_xoffset+ doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             #right bottom vertical
             objects.append(diagram.line(
            start=(right_xoffset- doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset- doubleDiameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
        elif(number == 7):
           objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset-numberOffset),  # Start of the base
                end=(right_xoffset +doubleDiameter / 4, yoffset-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
           objects.append(diagram.line(
            start=(right_xoffset+ doubleDiameter/ 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset- doubleDiameter/ 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
           ))
        elif(number == 8):
             objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #middle line
             objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter/ 4, yoffset + diameter/2-numberOffset),  # Start of the base
                end=(right_xoffset +doubleDiameter/ 4, yoffset + diameter/2-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))

         #bottom line
             objects.append(diagram.line(
                start=(right_xoffset -doubleDiameter / 4, yoffset + diameter-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #right top vertical
             objects.append(diagram.line(
            start=(right_xoffset- doubleDiameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset- doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             #left top vertical
             objects.append(diagram.line(
            start=(right_xoffset +doubleDiameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             
            #left bottom vertical
             objects.append(diagram.line(
            start=(right_xoffset+ doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             #right bottom vertical
             objects.append(diagram.line(
            start=(right_xoffset- doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset- doubleDiameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
        elif(number == 9):
             objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #middle line
             objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Start of the base
                end=(right_xoffset +doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))

         #bottom line
             objects.append(diagram.line(
                start=(right_xoffset -doubleDiameter / 4, yoffset + diameter-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter/ 4, yoffset + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #right top vertical
             objects.append(diagram.line(
            start=(right_xoffset- doubleDiameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset- doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             #left top vertical
             objects.append(diagram.line(
            start=(right_xoffset +doubleDiameter / 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             
             #right bottom vertical
             objects.append(diagram.line(
            start=(right_xoffset+ doubleDiameter / 4, yoffset + diameter/2-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
        elif(number == 0):
             objects.append(diagram.line(
                start=(right_xoffset -doubleDiameter / 4, yoffset-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
           

         #bottom line
             objects.append(diagram.line(
                start=(right_xoffset - doubleDiameter / 4, yoffset + diameter-numberOffset),  # Start of the base
                end=(right_xoffset + doubleDiameter / 4, yoffset + diameter-numberOffset),  # End of the base
                stroke='black',  # Outline (stroke) color
                stroke_width=.1  # Outline (stroke) width
            ))
            #right  vertical
             objects.append(diagram.line(
            start=(right_xoffset- doubleDiameter/ 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset- doubleDiameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             #left  vertical
             objects.append(diagram.line(
            start=(right_xoffset +doubleDiameter/ 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter / 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
            ))
             objects.append(diagram.line(
            start=(right_xoffset- doubleDiameter/ 4, yoffset-numberOffset),  # Top of the "1"
            end=(right_xoffset+ doubleDiameter/ 4, yoffset + diameter-numberOffset),  # Bottom of the "1"
            stroke='black',  # Outline (stroke) color
            stroke_width=.1  # Outline (stroke) width
           ))