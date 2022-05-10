from PIL import Image as ImagePil, ImageTk
from tkinter import filedialog as fd
from tkinter import *
from tkinter import ttk


def createImage(filename, imagename):
    with open(filename, "r") as f:
        img = ImagePil.new("RGB", (100, 100))
        k = 0
        j = 0
        pixels = f.read()
        for i in pixels:
            if int(i) == 0:
                img.putpixel((k, j), (255, 255, 255))
            else:
                img.putpixel((k, j), (0, 0, 0))
            j += 1
            if j == 100:
                k += 1
                j = 0
        img.save(imagename)

def get_filename():
    filename = fd.askopenfilename()

    #Создание черно-белой картинки 100х100
    createImage(filename, 'Klyuchnikov_D_S_BVT-191/Crypto/LR2/myImage1.jpg')

    #Отображение картинки
    image = ImagePil.open('Klyuchnikov_D_S_BVT-191/Crypto/LR2/myImage1.jpg')
    photo = ImageTk.PhotoImage(image)
    photo = photo._PhotoImage__photo.zoom(5)
    image_label = ttk.Label(root, image=photo)
    image_label.place(x=150, y=50)

    #Сжатие алгоритмом RLE
    with open(filename, "r") as f2:
        array = f2.read()
        counter = 0
        zipF = []
        prev_cymbol = array[0]
        for i in array:
            if i == prev_cymbol:
                counter += 1
            else:
                zipF.append(counter)
                zipF.append(prev_cymbol)
                zipF.append(",")
                counter = 1
                prev_cymbol = i
        zipF.append(counter)
        zipF.append(prev_cymbol)

    with open('Klyuchnikov_D_S_BVT-191/Crypto/LR2/2.txt', "w") as f3:
        for i in zipF:
            f3.write(str(i))

    #Декомпрессия
    with open('Klyuchnikov_D_S_BVT-191/Crypto/LR2/2.txt', "r") as fr:
        zip_str = fr.read()
        data = zip_str.split(",")
        real_value = []
        for i in range(0, len(data)):
            for j in range(int(data[i][0:-1])):
                real_value.append(data[i][-1])

    print("Cтепень сжатия:", round((1 - len(zip_str) / len(array)) * 100), "%")

    with open('Klyuchnikov_D_S_BVT-191/Crypto/LR2/3.txt', "w") as f6:
        for i in real_value:
            f6.write(str(i))

    #Создание черно-белой картинки 100х100
    createImage('Klyuchnikov_D_S_BVT-191/Crypto/LR2/3.txt', 'Klyuchnikov_D_S_BVT-191/Crypto/LR2/myImage2.jpg')

    # Отображение картинки после сжатия и декомпрессии
    image2 = ImagePil.open('Klyuchnikov_D_S_BVT-191/Crypto/LR2/myImage2.jpg')
    photo2 = ImageTk.PhotoImage(image2)
    photo2 = photo2._PhotoImage__photo.zoom(5)
    image_label = ttk.Label(root, image=photo2)
    image_label.place(x=750, y=50)
    root.mainloop()

root = Tk()
root.geometry("1500x700")

b1 = Button(text="Открыть", command=get_filename)
b1.grid(row=5, sticky=E)

root.mainloop()