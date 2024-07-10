from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image, ImageDraw
import re, math, ctypes
from images import *


def upload_image(args):
    fileTypes = [("Image files", "*.png")]
    path = filedialog.askopenfilename(filetypes=fileTypes, title=('Open file with Light' if  args == 'wLight' else 'Open file without Light' ))

    if len(path):
        img = Image.open(path).convert('RGBA')

        background = Image.new('RGBA', img.size, (34, 34, 34, 255))
        
        img = Image.alpha_composite(background, img)

        if args == "wLight":
            label_1_size['text'] = f'size: {img.width} x {img.height} (px)'
            global Light
            Light = img
            global size_wLight
            size_wLight = img.size
        else:
            label_2_size['text'] = f'size: {img.width} x {img.height} (px)'
            global noLight
            noLight = img
            global size_woLight
            size_woLight = img.size

        delta_x = 0
        delta_y = 0

        if img.width > img.height:
            img = img.resize((200, round(img.height / img.width * 200) ))
            delta_y = round(200 - img.height) / 2
        elif img.width < img.height:
            img = img.resize(( round(img.width / img.height * 200) , 200))
            delta_x = round(200 - img.width) / 2
        else:
            img = img.resize((200, 200))

        pic = ImageTk.PhotoImage(img)

        global xL
        global yL
        global xnL
        global ynL

        if args == "wLight":
            xL, yL = 374, 71
            
            if delta_y + delta_x != 0:
                xL += delta_x
                yL += delta_y
            
            image_wLight.place(x=xL, y=yL)

            image_wLight.config(image=pic)
            image_wLight.image = pic
        else:
            xnL, ynL = 616, 71

            if delta_y + delta_x != 0:
                xnL += delta_x
                ynL += delta_y

            image_woLight.place(x=xnL, y=ynL)

            image_woLight.config(image=pic)
            image_woLight.image = pic


def check_errors():
    report_message = 'Correct the Errors:\n'
    is_show_message = False

    if Light == 0:
        print(type(Light))
        report_message += "- You don't set the image with light\n"
        is_show_message = True
    if noLight == 0:
        report_message += "- You don't set the image without light\n"
        is_show_message = True
    if Light != 0 and noLight != 0 and Light.size != noLight.size:
        report_message += "- The size of image with light and image without light are not equal\n"
        is_show_message = True

    if is_show_message:
        messagebox.showerror(title='Error...', message=report_message)
        return False
    else:
        return True


def find_pixel_color(base, result):

    if base[0] != 255:
        a_r = (255 * (result[0] - base[0]) ) / (255 - base[0])
    else: a_r = 0
    if base[1] != 255:
        a_g = (255 * (result[1] - base[1]) ) / (255 - base[1])
    else: a_g = 0
    if base[2] != 255:
        a_b = (255 * (result[2] - base[2]) ) / (255 - base[2])
    else: a_b = 0

    a = max(a_r, a_g, a_b)

    if base == result or a == 0:
        return (0, 0, 0, 0)

    r = (255 * (result[0] - base[0])) / a + base[0]
    g = (255 * (result[1] - base[1])) / a + base[1]
    b = (255 * (result[2] - base[2])) / a + base[2]

    return (int(math.ceil(r)), int(math.ceil(g)), int(math.ceil(b)), int(a))


def render():
    check_errors()

    result = Image.new("RGBA", Light.size, (0, 0, 0, 0))    # Создаем новое изобр. на котором будем рисовать

    Light_pixels = Light.load()
    noLight_pixels = noLight.load()
    idraw = ImageDraw.Draw(result)

    for x in range(Light.width):
        for y in range(Light.height):
            idraw.point((x, y), find_pixel_color([noLight_pixels[x, y][0], noLight_pixels[x, y][1], noLight_pixels[x, y][2]], [Light_pixels[x, y][0], Light_pixels[x, y][1], Light_pixels[x, y][2]]) )

    fileTypes = [("Image files", "*.png")]
    path = filedialog.asksaveasfilename(filetypes=fileTypes, title='Save')

    if len(path):
        result.save(path + '.png')
        messagebox.showinfo(title='Info...', message="Image is saved!")


xL, yL = 374, 71
Light = 0

xnL, ynL = 616, 71
noLight = 0

main_font = ("Helvetica", 12)
label_font = ("Helvetica", 14, 'bold')

if __name__ == "__main__":

    root = Tk()

    root.title("Light Cutter")
    root.geometry("848x327")
    root.resizable(width=False, height=False)
    root['bg'] = '#222'

    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    pic_icon = icon_data
    icon_img = PhotoImage(data=pic_icon)
    root.iconphoto(False, icon_img)

    # LEFT FRAME

    panel = Label(root, border=0)
    panel.place(x=30, y=30)

    pic = logo_data
    render_img = PhotoImage(data=pic)
    panel.config(image=render_img)

    uploadButton_light = Button(root, text="Upload Image with Light" , font=main_font, bg='#b8b8b8', width=22, command=lambda: upload_image('wLight'))
    uploadButton_light.place(x=75, y=181)

    uploadButton_no_light = Button(root, text="Upload Image without Light" , font=main_font, bg='#b8b8b8', width=22, command=lambda: upload_image('woLight'))
    uploadButton_no_light.place(x=75, y=223)

    uploadButton_no_light = Button(root, text="Render and save" , font=main_font, bg='#fff', width=22, command=render)
    uploadButton_no_light.place(x=75, y=265)



    # RIGHT FRAME

    label_1 = Label(root, text="Image with Light:", bg='#222', fg='#fff', font=label_font)
    label_1.place(x=391, y=36)

    panel_1 = Label(root, border=0)
    panel_1.place(x=371, y=68)

    pic_1 = test_image_wLight_data
    render_img_1 = PhotoImage(data=pic_1)
    panel_1.config(image=render_img_1)

    image_wLight = Label(root, border=0, bg='#222')
    image_wLight.place(x=xL, y=yL)

    label_1_size = Label(root, text="size: 0 x 0 (px)", bg='#222', fg='#fff', font=("Helvetica", 10), width=25, anchor="e")
    label_1_size.place(x=371, y=274)



    label_2 = Label(root, text="Image without Light:", bg='#222', fg='#fff', font=label_font)
    label_2.place(x=620, y=36)

    panel_2 = Label(root, border=0)
    panel_2.place(x=613, y=68)

    pic_2 = test_image_woLight_data
    render_img_2 = PhotoImage(data=pic_2)
    panel_2.config(image=render_img_2)

    image_woLight = Label(root, border=0, bg='#222')
    image_woLight.place(x=xnL, y=ynL)

    label_2_size = Label(root, text="size: 0 x 0 (px)", bg='#222', fg='#fff', font=("Helvetica", 10), width=25, anchor="e")
    label_2_size.place(x=613, y=274)

    root.mainloop()
