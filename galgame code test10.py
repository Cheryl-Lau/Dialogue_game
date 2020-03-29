# -*- coding: utf-8 -*-


from PIL import Image, ImageDraw, ImageTk
import tkinter as tk 
import numpy as np


player_name = 'Master'

images = []   # for storing all objects created with method create_polygon


class Scene:
    
    def __init__(self,img_name, name, content1, content2):
        
        self.img_name = img_name 
        self.name = name 
        self.content1 = content1 
        self.content2 = content2 


    def display_scene(self):
        '''
        For normal story scenes 
        '''
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=700, height=400)
        self.canvas.pack()
        
        self.image = Image.open(self.img_name,'r')
        self.image.thumbnail((704.2,390), Image.ANTIALIAS)
        self.image = self.image.convert('RGBA')
        
        tk_img = ImageTk.PhotoImage(self.image)
        
        self.canvas.create_image(0,0, image=tk_img, anchor=tk.NW)

        # dialogue box
        points_dialogue = ((117, 310), (570, 310), (570, 380), (117, 380))
        self.create_polygon(*points_dialogue, fill='blue', alpha=0.5, line_fill='white', line_width=30, line_alpha=0.7)
        self.add_text((145, 327), self.content1, fill='white', font=('Verdana', 10))
        self.add_text((145, 352), self.content2, fill='white', font=('Verdana', 10))
        
        # name box 
        points_name = ((140,288), (152+(len(self.name)*7),288) , (152+(len(self.name)*7), 313), (140,313))
        self.create_polygon(*points_name, fill='white', alpha=0.85, line_fill='white', line_width=3, line_alpha=0.8)
        self.add_text((148, 292), self.name, fill='blue', font=('Helvetica', 10, 'bold'))

        # next button 
        nxt_button_img = self.image.crop((self.image.size[0]-100,0,self.image.size[0],self.image.size[1]))
        nxt_button_image = ImageTk.PhotoImage(nxt_button_img)
        nxt_button = tk.Button(self.root, image=nxt_button_image, bd=0, command=self.close_win)
        self.canvas.create_window(self.image.size[0]-100,0, anchor=tk.NW, window=nxt_button)        
        self.root.mainloop()


    def select_option(self, op1, op2):
        '''
        For story scenes with options popping up 
        '''
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=700, height=400)
        self.canvas.pack()
        
        self.image = Image.open(self.img_name,'r')
        self.image.thumbnail((704.2,390), Image.ANTIALIAS)
        self.image = self.image.convert('RGBA')
        
        tk_img = ImageTk.PhotoImage(self.image)
        
        self.canvas.create_image(0,0, image=tk_img, anchor=tk.NW)

        # dialogue box
        points_dialogue = ((117, 310), (570, 310), (570, 380), (117, 380))
        self.create_polygon(*points_dialogue, fill='blue', alpha=0.5, line_fill='white', line_width=20, line_alpha=0.7)
        self.add_text((145, 327), self.content1, fill='white', font=('Verdana', 10))
        self.add_text((145, 352), self.content2, fill='white', font=('Verdana', 10))
        
        # name box 
        points_name = ((140,288), (152+(len(self.name)*7),288) , (152+(len(self.name)*7), 313), (140,313))
        self.create_polygon(*points_name, fill='white', alpha=0.85, line_fill='white', line_width=3, line_alpha=0.8)
        self.add_text((148, 292), self.name, fill='royalblue', font=('Helvetica', 10, 'bold'))

        self.ans = 'A'  # set default self.ans as A when no option is clicked
        
        # option box 1
        points_op1 = ((170,165), (180,150), (500,150), (510,165), (500,180), (180,180))
        self.create_polygon(*points_op1, fill='royalblue', alpha=0.8, line_fill='navy', line_width=25, line_alpha=0.7)
        self.add_text((205, 158), '>>>   A:  '+op1, fill='darkblue', font=('Verdana', 9, 'bold'))

        # option box 1 button - call optionA_callback
        button_img = ImageTk.PhotoImage(file='button_img.jpg')
        buttonA = tk.Button(self.root, image=button_img, bd=0, command=lambda: self.optionA_callback(op1, op2), height=10, width=35)
        self.canvas.create_window(201, 160, anchor=tk.NW, window=buttonA) 

        # option box 2
        points_op2 = ((170,225), (180,210), (500,210), (510,225), (500,240), (180,240))
        self.create_polygon(*points_op2, fill='royalblue', alpha=0.8, line_fill='navy', line_width=25, line_alpha=0.7)
        self.add_text((205, 218), '>>>   B:  '+op2, fill='darkblue', font=('Verdana', 9, 'bold'))
        
        # option box 2 button - call optionB_callback
        buttonB = tk.Button(self.root, image=button_img, bd=0, command=lambda: self.optionB_callback(op1, op2), height=10, width=35)
        self.canvas.create_window(201, 220, anchor=tk.NW, window=buttonB) 

        # next button 
        nxt_button_img = self.image.crop((self.image.size[0]-100,0,self.image.size[0],self.image.size[1]))
        nxt_button_image = ImageTk.PhotoImage(nxt_button_img)
        nxt_button = tk.Button(self.root, image=nxt_button_image, bd=0, command=self.close_win)
        self.canvas.create_window(self.image.size[0]-98,0, anchor=tk.NW, window=nxt_button)        
        
        self.root.mainloop()

        # self.ans returned from optionA/B_callback function 
        if self.ans == 'A':
            print(player_name+': "'+op1+'"')
        elif self.ans == 'B':
            print(player_name+': "'+op2+'"')
            
        return self.ans

        
    def optionA_callback(self, op1, op2):
        '''
        Called when option A is clicked
        '''
        # buttonA change to red 
        points_op1 = ((170,165), (180,150), (500,150), (510,165), (500,180), (180,180))
        self.create_polygon(*points_op1, fill='royalblue', alpha=0.8, line_fill='red', line_width=30, line_alpha=0.7)  
        self.add_text((205, 158), '>>>   A:  '+op1, fill='red', font=('Verdana', 9, 'bold'))
        
        # buttonB change to blue
        points_op2 = ((170,225), (180,210), (500,210), (510,225), (500,240), (180,240))
        self.create_polygon(*points_op2, fill='royalblue', alpha=0.8, line_fill='navy', line_width=25, line_alpha=0.7)
        self.add_text((205, 218), '>>>   B:  '+op2, fill='darkblue', font=('Verdana', 9, 'bold'))         
        
        self.ans = 'A'
        
        return self.ans
    
    
    def optionB_callback(self, op1, op2):
        '''
        Called when option B is clicked
        '''
        # buttonB change to red 
        points_op2 = ((170,225), (180,210), (500,210), (510,225), (500,240), (180,240))
        self.create_polygon(*points_op2, fill='royalblue', alpha=0.8, line_fill='red', line_width=30, line_alpha=0.7)
        self.add_text((205, 218), '>>>   B:  '+op2, fill='red', font=('Verdana', 9, 'bold'))        
        
        # buttonA change to blue 
        points_op1 = ((170,165), (180,150), (500,150), (510,165), (500,180), (180,180))
        self.create_polygon(*points_op1, fill='royalblue', alpha=0.8, line_fill='navy', line_width=25, line_alpha=0.7)
        self.add_text((205, 158), '>>>   A:  '+op1, fill='darkblue', font=('Verdana', 9, 'bold'))        
        
        self.ans = 'B'
        
        return self.ans


    def create_polygon(self,*points, **kwargs):
        '''
        Creates polygon object (& outline) with variable transparency
        Function Inputs:   *points_poly, fill, alpha, line_fill, line_width, line_alpha
        '''
        # extract coordinates from point arguments
        x_list = [coord[0] for coord in points]
        y_list = [coord[1] for coord in points]
    
        alpha = kwargs.pop('alpha')  # extract alpha input 
        opacity = int(255*alpha)
        fill = kwargs.pop('fill')    # extract colour input for polygon
        fill_opacity = self.root.winfo_rgb(fill) + (opacity,)
        
        line_width = kwargs.pop('line_width')
        line_alpha = kwargs.pop('line_alpha')  # extract alpha input 
        line_opacity = int(255*line_alpha)        
        line_fill = kwargs.pop('line_fill') 
        line_fill_opacity = self.root.winfo_rgb(line_fill) + (line_opacity,)
        
        # crop out a section of the bg image JUST around the polygon (+/-cut)
        min_x = min(x_list)
        max_x = max(x_list)
        min_y = min(y_list)
        max_y = max(y_list)
        cut = 6
        cropped_image = self.image.crop((min_x-cut,min_y-cut,max_x+cut,max_y+cut))
                                
        # create an overlay image (cropped background) around the polygon                        
        overlay = Image.new('RGBA', cropped_image.size , (255,255,255)+(0,))
        draw = ImageDraw.Draw(overlay) 
        
        # convert to coord of polygon relative to the cropped overlay image
        polygon_coord = [(i-(min_x-cut),j-(min_y-cut)) for (i,j) in zip(x_list,y_list)]

        # Create an enlarged polygon centered at polygon midpoint to form the outline
        midpt = ((max_x-min_x+2*cut)/2., (max_y-min_y+2*cut)/2.)
        vector_to_mid = np.subtract(np.array(polygon_coord),np.array(midpt)) # vector dir to enlarge
        unit_vector = vector_to_mid / (vector_to_mid**2).sum()**0.5
        enlarged_coord = polygon_coord + unit_vector * line_width  
        enlarged_coord = [(i,j) for i,j in enlarged_coord] # convect array back to ((x1,y1),(x2,y2),...) format
        
        # draw polygon to form outline with alpha transparency
        draw.polygon(enlarged_coord, fill=line_fill_opacity)
        
        # draw polygon on overlay with alpha transparency 
        draw.polygon(polygon_coord, fill=fill_opacity)
    
        # combine the objects with overlay 
        img = Image.alpha_composite(cropped_image, overlay) 
        img = img.convert('CMYK')
        
        images.append(ImageTk.PhotoImage(img))
        
        # paste overlay back to background image on same location where it was taken out
        self.canvas.create_image(min_x-cut,min_y-cut, image=images[-1], anchor='nw') 
        
        
    def add_text(self, position, text, **kwargs):
        '''
        Puts text onto canvas
        '''
        fill = kwargs.pop('fill')
        font = kwargs.pop('font')
        self.canvas.create_text(*position, anchor=tk.NW, fill=fill, font=font, text=text)
        
        
    def close_win(self):
        '''
        Called from next button - Close current tkinter window to run the next scene
        '''
        self.root.destroy()


## Set up content in each scene 

def scene_1():   # story
    
    img_name = 'okita_happy.jpg'
    name = 'Okita Souji'
    content1 = "I was looking for you, "+player_name+"!"
    content2 = "You look happy today wwwwwwwwww"
    print(name+': "'+content1+' '+content2+'"')
    scene1 = Scene(img_name, name, content1, content2)
    scene1.display_scene()

def scene_2():   # option 
    
    img_name = 'okita_blush.jpg'
    name = 'Okita Souji'
    content1 = 'Heyhey, '+player_name+', do I.... look any different today?'
    content2 = ''
    op1 = 'Did you buy a new sword again?'
    op2 = 'Ermmm, still fat.'
    print(name+': "'+content1+' '+content2+'"')
    scene2 = Scene(img_name, name, content1, content2)
    scene2.display_scene()
    ans2 = scene2.select_option(op1, op2)
    return ans2
    
def scene_3():   # story
    
    img_name = 'okita_sad.jpg'
    name = 'Okita Souji'
    content1 = "Is that it....? I thought you would realise the new kimono."
    content2 = "(sigh)"
    print(name+': "'+content1+' '+content2+'"')
    scene3 = Scene(img_name, name, content1, content2)
    scene3.display_scene()
    
def scene_4():   # option
    
    img_name = 'okita_yell.jpg'
    name = 'Okita Souji'
    content1 = "Shut upppp! "+player_name+" I hate you."
    content2 = ''
    op1 = '??????'
    op2 = 'Okay, my bad!'
    print(name+': "'+content1+' '+content2+'"')
    scene4 = Scene(img_name, name, content1, content2)
    scene4.display_scene()
    ans4 = scene4.select_option(op1, op2)
    return ans4

def scene_5():   # story
    
    img_name = 'okita_yell.jpg'
    name = 'Okita Souji'
    content1 = "Baka! Baka baka baka!"
    content2 = player_name+" You're a big baka!"
    print(name+': "'+content1+' '+content2+'"')
    scene5 = Scene(img_name, name, content1, content2)
    scene5.display_scene()
    
def scene_6():   # story
    
    img_name = 'okita_sad.jpg'
    name = 'Okita Souji'
    content1 = "Stop bullying me, don't do that to your own waifu."
    content2 = " "
    print(name+': "'+content1+' '+content2+'"')
    scene6 = Scene(img_name, name, content1, content2)
    scene6.display_scene()

def scene_7():   # story
    
    img_name = 'okita_happy.jpg'
    name = 'Okita Souji'
    content1 = "The shinsengumi went out yesterday, Hijikata-san bought me "
    content2 = "a kimono as present!"
    print(name+': "'+content1+' '+content2+'"')
    scene7 = Scene(img_name, name, content1, content2)
    scene7.display_scene()
    
    
def main():
    '''
    Story flow; options tree
    '''
    scene_1()
    ans2 = scene_2()    
    if ans2 == 'A':
        scene_3()   
        scene_7()
    elif ans2 == 'B':
        ans4 = scene_4() 
        if ans4 == 'A':
            scene_5()
        elif ans4 == 'B':
            scene_6()
    
    return 

    
if __name__ == '__main__':
    main()















