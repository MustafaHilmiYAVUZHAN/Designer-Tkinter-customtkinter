import customtkinter as tk,customtkinter
from PIL import Image, ImageTk,ImageDraw
#import cv2
import os
global pre_my_data,pre_element,pro_my_data,my_data,pre_root
pre_element=[""]
pre_my_data=[]
pro_my_data=[]
pre_root=["root"]
print(type(pre_element))

def cmd():
    print("")

def custom_sort(item):
    widget_type = item[2]
    print(item[0])
    if widget_type == 'frame':
        if find_index_by_value_by_value(pre_root,item[0])==None:
            pre_root.append(item[0])
        return 0
    elif widget_type == 'tabview':
        if find_index_by_value_by_value(pre_root,item[0])==None:
            pre_root.append(item[0])
        return 1
    elif widget_type == 'tab':
        if find_index_by_value_by_value(pre_root,item[0])==None:
            pre_root.append(item[0])
        return 2
    elif widget_type == 'varframe':
        if find_index_by_value_by_value(pre_root,item[0])==None:
            pre_root.append(item[0])
        return 3
    else:
        return 4

def sort():
    print(pro_my_data)
    sorted_my_data = sorted(pro_my_data, key=custom_sort)
    return sorted_my_data
    # Sonucu ekrana yazdır
def find_index_by_value(my_data, search_value):
    print("a")
    for index, sublist in enumerate(my_data):
        if sublist[0] == search_value:
            return index
    return None 
def find_index_by_value_by_value(my_data, search_value):
    print("a")
    for index, sublist in enumerate(my_data):
        if sublist == search_value:
            return index
    return None 
def my_data_get(element):
    print(element)
    print(my_data[find_index_by_value(my_data,element)][-1].get())
    return my_data[find_index_by_value(my_data,element)][-1].get()

def default_text(element_text_up):
    element=find_index_by_value(pre_my_data,element_text_up)
    entry=find_index_by_value(my_data,"entry6")  
    try:
        my_data[entry][-1].delete(0, tk.END)
    except:
        pass
    my_data[entry][-1].insert(0,str(pre_my_data[element][1][0]) )

    entry=find_index_by_value(my_data,"entry7")
    try:
        my_data[entry][-1].delete(0, tk.END)
    except:
        pass
    my_data[entry][-1].insert(0,str(pre_my_data[element][1][1]) )

    entry=find_index_by_value(my_data,"entry8")
    try:
        my_data[entry][-1].delete(0, tk.END)
    except:
        pass
    my_data[entry][-1].insert(0,str(pre_my_data[element][1][2]) )

    entry=find_index_by_value(my_data,"entry9")
    try:
        my_data[entry][-1].delete(0, tk.END)
    except:
        pass
    my_data[entry][-1].insert(0,str(pre_my_data[element][1][3]) )

    entry=find_index_by_value(my_data,"optionmenu2")
    my_data[entry][-1].set(str(pre_my_data[element][2]) )

def update(element_up):
    global my_data
    element_up=find_index_by_value(my_data,element_up)
    del my_data[element_up][-1]
    element,command,is_this_image=place_element(my_data[element_up][0],my_data[element_up][1],my_data[element_up][2],my_data[element_up][3],my_data[element_up][4],my_data[element_up][5])

    my_data[element_up].append(eval(element))
    x=element_up
    eval(command)
def update_box(element_up):
    global my_data
    element_up=find_index_by_value(my_data,element_up)
    del my_data[element_up][-1]
    element,command,is_this_image=place_element(my_data[element_up][0],my_data[element_up][1],my_data[element_up][2],my_data[element_up][3],my_data[element_up][4],my_data[element_up][5])

    my_data[element_up].append(eval(element))
    x=element_up
    eval(command[0])
    eval(command[1])

def add_my_data():
    
    if "combobox"==my_data[find_index_by_value(my_data,"optionmenu2")][-1].get() or "optionmenu"==my_data[find_index_by_value(my_data,"optionmenu2")][-1].get():
        return_my_data = [my_data[find_index_by_value(my_data,"optionmenu1")][-1].get(),[int(my_data[find_index_by_value(my_data,"entry6")][-1].get()),int(my_data[find_index_by_value(my_data,"entry7")][-1].get()),int(my_data[find_index_by_value(my_data,"entry8")][-1].get()),int(my_data[find_index_by_value(my_data,"entry9")][-1].get())],my_data[find_index_by_value(my_data,"optionmenu2")][-1].get(),[my_data[find_index_by_value(my_data,"entry10")][-1].get(),my_data[find_index_by_value(my_data,"entry11")][-1].get()],my_data[find_index_by_value(my_data,"combo")][-1].get(),my_data[find_index_by_value(my_data,"optionmenu3")][-1].get()]
    else:
        return_my_data = [my_data[find_index_by_value(my_data,"optionmenu1")][-1].get(),[int(my_data[find_index_by_value(my_data,"entry6")][-1].get()),int(my_data[find_index_by_value(my_data,"entry7")][-1].get()),int(my_data[find_index_by_value(my_data,"entry8")][-1].get()),int(my_data[find_index_by_value(my_data,"entry9")][-1].get())],my_data[find_index_by_value(my_data,"optionmenu2")][-1].get(),my_data[find_index_by_value(my_data,"entry11")][-1].get(),my_data[find_index_by_value(my_data,"combo")][-1].get(),my_data[find_index_by_value(my_data,"optionmenu3")][-1].get()]
    entry=find_index_by_value(my_data,"entry1")  
    try:
        my_data[entry][-1].delete(0, tk.END)
    except:
        pass
    entry=find_index_by_value(my_data,"entry2")  
    try:
        my_data[entry][-1].delete(0, tk.END)
    except:
        pass
    entry=find_index_by_value(my_data,"entry3")  
    try:
        my_data[entry][-1].delete(0, tk.END)
    except:
        pass
    entry=find_index_by_value(my_data,"entry4")  
    try:
        my_data[entry][-1].delete(0, tk.END)
    except:
        pass
    entry=find_index_by_value(my_data,"entry5")  
    try:
        my_data[entry][-1].delete(0, tk.END)
    except:
        pass
    return return_my_data
def update_button():
    if my_data_get("entry11")=="":
        my_data[find_index_by_value(my_data,"entry11")][-1].insert(0,"cmd")
    global pro_my_data
    if my_data[find_index_by_value(my_data,"optionmenu1")][-1].get()=="":
        pass
    elif None==find_index_by_value(pro_my_data,my_data[find_index_by_value(my_data,"optionmenu1")][-1].get()):
        pro_my_data.append(add_my_data())
    else:
        x=find_index_by_value(pro_my_data,my_data[find_index_by_value(my_data,"optionmenu1")][-1].get())
        pro_my_data[x][0],pro_my_data[x][1],pro_my_data[x][2],pro_my_data[x][3],pro_my_data[x][4],pro_my_data[x][5]=add_my_data()
    pro_my_data=sorted(pro_my_data, key=custom_sort)
    update("optionmenu3")
    try:
        update_box("Box")
    except Exception as error:
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaq")
        print(error)
    print("aaaaaaaaaa")
    print(pro_my_data)
def add_button():
    if my_data[find_index_by_value(my_data,"entry1")][-1].get()=="":
        pass
    elif None==find_index_by_value(pre_my_data,my_data[find_index_by_value(my_data,"entry1")][-1].get()):
        pre_my_data.append([my_data[find_index_by_value(my_data,"entry1")][-1].get(),[int(my_data[find_index_by_value(my_data,"entry2")][-1].get()),int(my_data[find_index_by_value(my_data,"entry3")][-1].get()),int(my_data[find_index_by_value(my_data,"entry4")][-1].get()),int(my_data[find_index_by_value(my_data,"entry5")][-1].get())],my_data[find_index_by_value(my_data,"optionmenu")][-1].get()])
        pre_element.append(my_data[find_index_by_value(my_data,"entry1")][-1].get())
        if pre_element[0]=="":
            del pre_element[0]
        update("optionmenu1")

        update("optionmenu3")
        try:
            update_box("Box")
        except Exception as error:
            print(error)
        print("aaaaaaaaaaaa")
        print(find_index_by_value(my_data,"optionmenu1"))
        print(my_data[find_index_by_value(my_data,"optionmenu1")][-1].get())
        entry=find_index_by_value(my_data,"optionmenu1")
        my_data[entry][-1].set(my_data[find_index_by_value(my_data,"entry1")][-1].get())
        default_text(my_data[find_index_by_value(my_data,"optionmenu1")][-1].get())
    # default_text()
    print(pre_my_data)    

def delete_button():
    global pre_element
    del pre_element[find_index_by_value(pre_my_data,my_data_get("optionmenu1"))]
    del pro_my_data[find_index_by_value(pro_my_data,my_data_get("optionmenu1"))]
    del pre_my_data[find_index_by_value(pre_my_data,my_data_get("optionmenu1"))]
    try:
        del pre_root[find_index_by_value_by_value(pre_root,my_data_get("optionmenu1"))]
    except Exception as error:
        print(error)
    if pre_element==[]:
        pre_element=[""]
    print(pre_element)
    update("optionmenu3")
    update("optionmenu1")
    update("Box")
def right():
    entry=find_index_by_value(my_data,"entry6")
    x=int(my_data[entry][-1].get())
    my_data[entry][-1].delete(0, tk.END)
    my_data[entry][-1].insert(0,str(x+5) )
def left():
    entry=find_index_by_value(my_data,"entry6")
    x=int(my_data[entry][-1].get())
    my_data[entry][-1].delete(0, tk.END)
    my_data[entry][-1].insert(0,str(x-5) )
def up():
    entry=find_index_by_value(my_data,"entry7")
    x=int(my_data[entry][-1].get())
    my_data[entry][-1].delete(0, tk.END)
    my_data[entry][-1].insert(0,str(x+5) )
def down():
    entry=find_index_by_value(my_data,"entry7")
    x=int(my_data[entry][-1].get())
    my_data[entry][-1].delete(0, tk.END)
    my_data[entry][-1].insert(0,str(x-5) )
def expand():
    entry=find_index_by_value(my_data,"entry8")
    x=int(my_data[entry][-1].get())
    my_data[entry][-1].delete(0, tk.END)
    my_data[entry][-1].insert(0,str(x+5) )
def collapse():
    entry=find_index_by_value(my_data,"entry8")
    x=int(my_data[entry][-1].get())
    my_data[entry][-1].delete(0, tk.END)
    my_data[entry][-1].insert(0,str(x-5) )
def elongation():
    entry=find_index_by_value(my_data,"entry9")
    x=int(my_data[entry][-1].get())
    my_data[entry][-1].delete(0, tk.END)
    my_data[entry][-1].insert(0,str(x+5) )
def shortening():
    entry=find_index_by_value(my_data,"entry9")
    x=int(my_data[entry][-1].get())
    my_data[entry][-1].delete(0, tk.END)
    my_data[entry][-1].insert(0,str(x-5) )
def aaaaa(d=None):
    if d==None:
        d="jjjjjjjjjjjj"
    print(d)
    print(my_data[find_index_by_value(my_data,"entry")][-1].get())
def pre_img(path):
    image = Image.open(path)
    return image.size, image
def pro_img(image):
    rad=7
    w, h = image.size
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255)
    alpha = Image.new('L', image.size, 255)
            
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    image.putalpha(alpha)
        ### image.show()
    return ImageTk.PhotoImage(image=image)

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

def place_element(name, coordinates, kind,command,extra,win):
    try:
        x, y, width, height=coordinates
    except:
        pass
    if type(extra)==type("a"):
        if extra=="":
            pass
        else:
            extra=","+extra

    else:
        if extra[-1]!="":
            extra[-1]=","+extra[-1]
    if win=="":
        win="root"
    else:
        try:
            print(win)
            win=find_index_by_value(my_data,win)
            print(win)
            if win==None:
                print("error")
                win="root"
            else:
                win=f"my_data[{str(win)}][-1]"
        except Exception as error:
            print(error)
            print(win)
            win="root"
    if str(kind).lower() == "entry":
        return f"tk.CTkEntry({win},width={width},height={height}{extra})",f"my_data[x][-1].place(x={x}, y={y})",""
    elif str(kind).lower() == "button":
        return f'tk.CTkButton({win},text="{name}",width={width},height={height},command={command}{extra})' ,f"my_data[x][-1].place(x={x}, y={y})",""
    elif str(kind).lower() == "frame":
        return f'tk.CTkFrame({win},width={width},height={height}{extra})' ,f"my_data[x][-1].place(x={x}, y={y})",""
    elif str(kind).lower() == "tabview":
        return f'tk.CTkTabview({win},width={width},height={height})' ,f"my_data[x][-1].place(x={x}, y={y})",""
    elif str(kind).lower() == "tab":
        return f'{win}.add("{name}")' ,"",""
    elif str(kind).lower() == "checkbox":
        return f'tk.CTkCheckBox({win},text="{name}")' ,f"my_data[x][-1].place(x={x}, y={y})",""
    elif str(kind).lower() == "label" or str(kind).lower() == "text" :
        return f'tk.CTkLabel({win},text="{command}",width={width}{extra})' ,f"my_data[x][-1].place(x={x}, y={y})",""
    elif str(kind).lower() == "radiobutton":
        varframe,value,extra=extra
        varframe=find_index_by_value(my_data,varframe)
        return f'tk.CTkRadioButton({win},text="{name}",command={command},variable=my_data[{str(varframe)}][-1],value={value}{extra})' ,f"my_data[x][-1].place(x={x}, y={y})",""
    elif str(kind).lower() == "varframe":
        return f'tk.IntVar(value=0)' ,f"my_data[x][-1]",""
    elif str(kind).lower() == "combobox":
        values,extra=extra
        try :
            values1=eval(values)
            print(type([22,22]))
            print(values1==type([22,22]))
            print(type(values1))
            if type(values1)==type([22,22]):
                return f'tk.CTkComboBox({win},width={width},height={height},command={command},values={values}{extra})' ,f"my_data[x][-1].place(x={x}, y={y})",""
            else:
                return f'tk.CTkComboBox({win},width={width},height={height},command={command},values=[{values}]{extra})' ,f"my_data[x][-1].place(x={x}, y={y})",""
        except:
            return f'tk.CTkComboBox({win},width={width},height={height},command={command},values=[{values}]{extra})' ,f"my_data[x][-1].place(x={x}, y={y})",""
    elif str(kind).lower() == "optionmenu":
        values,extra=extra
        print(values)
        if values[-1]==",":
            values=values[0:-1]
        try :
            values1=eval(values)
            print(type([22,22]))
            print(values1)
            if type(values1)==type([22,22]):
                return f'tk.CTkOptionMenu({win},width={width},height={height},command={command},values={values}{extra})' ,f"my_data[x][-1].place(x={x}, y={y})",""
            else:
                return f'tk.CTkOptionMenu({win},width={width},height={height},command={command},values=[{values}]{extra})' ,f"my_data[x][-1].place(x={x}, y={y})",""
        except:
            return f'tk.CTkOptionMenu({win},width={width},height={height},command={command},values=[{values}]{extra})' ,f"my_data[x][-1].place(x={x}, y={y})",""
    elif str(kind).lower() == "progressbar":
        return f'tk.CTkProgressBar({win},width={width},height={height}{extra})' ,f"my_data[x][-1].place(x={x}, y={y})",""
    elif str(kind).lower() == "slider":
        return f'tk.CTkSlider({win},width={width},height={height},command={command}{extra})' ,f"my_data[x][-1].place(x={x}, y={y})",""
    elif str(kind).lower() == "switch":
        return ["tk.IntVar(value=1)",f'tk.CTkSwitch({win},text="{name}",command={command},variable=my_data[x][-1],onvalue=1{extra})'] ,f"my_data[x][-1].place(x={x}, y={y})",""
    elif str(kind).lower() == "textbox":
        return f'tk.CTkTextbox({win},width={width},height={height}{extra})' ,[f"my_data[x][-1].place(x={x}, y={y})",f"my_data[x][-1].insert('0.0',{command})"],""


    else:
        extra=extra[1:]
        print(extra)
        
        (w, h) ,image= pre_img(extra)
        
    
        # Sonucu göster veya kaydet
        if kind==0:
            # Görüntüyü kırp
            image = image.crop((0, 0, width, height))
            ###new_p=[name,x,y,width,height,0,command]
        elif kind==1:
            # Görüntüyü yeniden boyutlandır
            image = image.resize((width, height))
            ###new_p=[name,x,y,width,height,1,command]
        elif kind==2:
            newH=int(float(width)/w*h)
            image = image.resize((width,newH))
            diff_y=int((newH-height)/2)

            if newH<height:
                pass
            else:
                image = image.crop((0,diff_y , width,newH-diff_y))
                del diff_y
            
        elif kind==3:
            newW=int(float(height)/h*w)
            image = image.resize((newW,height ))
            diff_x=int((newW-width)/2)
            if newW<width:
                pass
            else:
                
                image = image.crop((diff_x ,0,newW-diff_x, height ))
                del diff_x
            
            
        
        if 1:
            img = pro_img(image)

            # Görüntüyü yerleştir
            label = ""
            ###label.image = img
            try:
                ##label.place(x=x-diff_x, y=y)
                return img,f"tk.CTkLabel({win},text='', image=element)",f"my_data[x][-1].place(x={x-diff_x}, y={y})"
            except:
                try:
                    ##label.place(x=x, y=y-diff_y)
                    return img,f"tk.CTkLabel({win},text='', image=element)",f"my_data[x][-1].place(x={x}, y={y-diff_y})"
                except:
                    ##label.place(x=x, y=y)
                    return img,f"tk.CTkLabel({win},text='', image=element)",f"my_data[x][-1].place(x={x}, y={y})"  # Belirtilen x ve y konumuna yerleştir
            ##del diff_,diff_x
def find_indices_by_value(my_data, search_value):
    indices = [index for index, sublist in enumerate(my_data) if str(sublist[2]).lower() == search_value]
    return indices
def find_indices_by_value_not_entry_and_button(my_data):
    indices = [index for index, sublist in enumerate(my_data) if str(sublist[2]).lower() not in ["entry", "button","frame","tabview","tab"]]
    return indices

my_data=[["lsbel1",[210,15,30,0],"label","Design your tkinter",'font=("Arial",25)',""],
      ["label2",[455,5,30,0],'label'," with customtkinter",'text_color="#777777",font=("Arial",11)',''],
      ["label3",[430,25,30,0],'label'," By Mustafa Hilmi YAVUZHAN",'text_color="#777777",font=("Arial",11)',''],
      ["frame_1",[50,70,700,60],'frame',"",'',''],
      ["Add",[590,10,100,40],'button',"add_button",'font=("Arial",13)','frame_1'],
      ["optionmenu",[20,20,90,20],'optionmenu',"cmd",['"frame","tabview","tab","button","entry","label","switch","varframe","checkbox","textbox","radiobutton","optionmenu","combobox","progressbar","slider"',""],'frame_1'],
      ["label4",[130,16,30,0],'label',"name :",'font=("Arial",15)','frame_1'],
      ["entry1",[180,19,75,15],'entry',"",'font=("Arial",15)','frame_1'],
      ["label5",[260,16,30,0],'label',"x :",'font=("Arial",15)','frame_1'],
      ["entry2",[285,19,35,15],'entry',"",'font=("Arial",15)','frame_1'],
      ["label6",[330,16,30,0],'label',"y :",'font=("Arial",15)','frame_1'],
      ["entry3",[355,19,35,15],'entry',"",'font=("Arial",15)','frame_1'],
      ["label7",[400,16,30,0],'label',"width :",'font=("Arial",15)','frame_1'],
      ["entry4",[445,19,35,15],'entry',"",'font=("Arial",15)','frame_1'],
      ["label7",[485,16,30,0],'label',"height:",'font=("Arial",15)','frame_1'],
      ["entry5",[535,19,35,15],'entry',"",'font=("Arial",15)','frame_1'],
      ["frame_2",[50,150,700,250],'frame',"",'',''],
      ["optionmenu1",[20,20,90,20],'optionmenu',"default_text",['pre_element',""],'frame_2'],
      ["label4",[130,16,30,0],'label',"type :",'font=("Arial",15)','frame_2'],
      ["optionmenu2",[180,19,105,15],'optionmenu',"cmd",['"frame","tabview","tab","button","entry","label","switch","varframe","checkbox","textbox","radiobutton","optionmenu","combobox","progressbar","slider"',""],'frame_2'],
      ["label5",[300,36,30,0],'label',"x :",'font=("Arial",15)','frame_2'],
      ["entry6",[325,39,35,15],'entry',"",'font=("Arial",15)','frame_2'],
      ["label6",[300,151,30,0],'label',"y :",'font=("Arial",15)','frame_2'],
      ["entry7",[325,154,35,15],'entry',"",'font=("Arial",15)','frame_2'],
      ["label7",[400,36,30,0],'label',"width :",'font=("Arial",15)','frame_2'],
      ["entry8",[450,39,35,15],'entry',"",'font=("Arial",15)','frame_2'],
      ["label7",[400,151,30,0],'label',"height :",'font=("Arial",15)','frame_2'],
      ["entry9",[450,154,35,15],'entry',"",'font=("Arial",15)','frame_2'],
      ["→",[330,10,10,10],'button',"right",'font=("Arial",13)','frame_2'],
      ["←",[330,72,10,10],'button',"left",'font=("Arial",13)','frame_2'],
      ["↑",[330,125,10,10],'button',"up",'font=("Arial",13)','frame_2'],
      ["↓",[330,187,10,10],'button',"down",'font=("Arial",13)','frame_2'],
      ["←→",[450,10,10,10],'button',"expand",'font=("Arial",13)','frame_2'],
      ["→←",[450,72,10,10],'button',"collapse",'font=("Arial",13)','frame_2'],
      ["↕",[460,125,10,10],'button',"elongation",'font=("Arial",13)','frame_2'],
      ["↘↙",[455,187,10,10],'button',"shortening",'font=("Arial",13)','frame_2'],

      ["label10",[520,105,0,0],'label',"if this is combobox or optionmenu",'font=("Arial",10),text_color="#777777"','frame_2'],
      ["label8",[550,10,30,0],'label',"command :",'font=("Arial",13)','frame_2'],      
      ["entry11",[520,40,150,20],'entry',"",'font=("Arial",15)','frame_2'],
      ["label9",[570,130,30,0],'label',"list :",'font=("Arial",13)','frame_2'],
      ["entry10",[520,160,150,20],'entry',"cmd",'font=("Arial",15)','frame_2'],
      ["label11",[10,60,30,0],'label',"extra :",'font=("Arial",15)','frame_2'],
      ["combo",[80,65,205,15],'combobox',"cmd",["""'','text_color="#777777"','font=("Arial",11)'""",""],'frame_2'],
      ["label12",[10,90,30,0],'label',"root :",'font=("Arial",15)','frame_2'],  
      ["optionmenu3",[80,95,205,15],'optionmenu',"cmd",["pre_root",""],'frame_2'],
      ["Update",[10,180,275,20],'button',"update_button",'font=("Arial",13)','frame_2'],
      ["Delete",[10,150,275,20],'button',"delete_button",'font=("Arial",13),hover_color="red",fg_color="#a03333"','frame_2'],
      ["Box",[50,450,700,370],'textbox',"'my_data='+str(pro_my_data)",'font=("Arial",13)','root'],

      ]

# Çalışan python dosyasının yolunu al
current_dir = os.path.dirname(os.path.abspath(__file__))

# Dosya yolunu oluştur
"""file_path = os.path.join(current_dir, "my_data.txt")
my_data_file=open(file_path,"r", encoding="utf-8")
my_data=my_data_file.read()
my_data_file.close()
exec(my_data)"""
global my_my_data
global button_indices,entry_indices,image_indices,frame_indices
button_indices=find_indices_by_value(my_data,"button")
entry_indices=find_indices_by_value(my_data,"entry")
frame_indices=find_indices_by_value(my_data,"frame")
image_indices=find_indices_by_value_not_entry_and_button(my_data)

global root
root = tk.CTk()
root.title("Yavuzhan designer")
root.geometry("800x850")
new_p_arc=[]
for x in range(len(my_data)):
    try:
        element,command,is_this_image=place_element(my_data[x][0], my_data[x][1], my_data[x][2], my_data[x][3], my_data[x][4], my_data[x][5])
        if type(element)==type(["ü",""]):
            element,element1=element
        else:
            element1="" 
        if type(command)==type(["ü",""]):
            command,command1=command
        else:
            command1=""
        if is_this_image=="":

            
   #         a=eval(element)

            print(element)
                
            my_data[x].append(eval(element))
            print(type(my_data[x][-1]))
            if element1!="":
                print(element1)
                my_data[x].append(eval(element1))
            try:
                print(command)
                eval(command)
                
            except Exception as error:
                print(error)
                try:
                    exec(command)
                except Exception as error:
                    print(error)
            try:
                print(command1)
                eval(command1)
                
            except Exception as error:
                print(error)
                try:
                    exec(command1)
                except Exception as error:
                    print(error)
        else:
            my_data[x].append(eval(command))
            eval(is_this_image)
            


    except IndexError:
        break



    # Set the window icon
#root.iconbitmap("icon1.ico")
root.resizable(0,0)
"""
root.bind('<Motion>', which_element)
root.bind("<Button-1>",which_element) """
root.mainloop()
