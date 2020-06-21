from tkinter import *
from tkinter import filedialog
from sklearn import tree
from os import listdir
import numpy as np
from os.path import isfile, join
from PIL import Image

class ocr:
    global file_path
    X = []
    y = []
    clf = tree.DecisionTreeClassifier()
    def __init__(self, master):

        topframe = Frame(master, width=600, height=150, background="purple")
        topframe.pack()
        topframe.pack_propagate(False)
        self.label = Label(topframe, text='Bengali Handwritten OCR', bg='purple', fg='white')
        self.label.config(font=("Algerian", 22))
        self.label.pack(padx=5, pady=50);

        middleframe = Frame(master, width=600, height=100, background="pink")
        middleframe.pack_propagate(False)
        middleframe.pack()

        bottomframe = Frame(master, width=600, height=150, background="purple")
        bottomframe1 = Frame(bottomframe, width=200, height=150, background="purple")
        bottomframe2 = Frame(bottomframe, width=200, height=150, background="purple")
        bottomframe3 = Frame(bottomframe, width=200, height=150, background="purple")
        self.bottomlevel1 = Label(bottomframe1, text='input')
        self.bottomlevel3 = Label(bottomframe3, text='input')

        self.training = Button(middleframe, text='Tarin Data', fg='white', bg="purple",
                               command=self.training)
        self.training.config(font=("Times New Roman", 14))
        self.training.pack(padx=75, pady=30, side='left');

        self.filechooser = Button(middleframe, text='Choose File', fg='white', bg="purple",
                                  command=lambda: self.chooseFile())

        self.filechooser.config(font=("Times New Roman", 14))
        self.filechooser.pack(padx=20, pady=30, side='left');

        self.submit = Button(middleframe, text='Submit', fg='white', bg="purple",
                             command=self.process)

        self.submit.config(font=("Times New Roman", 14))
        self.submit.pack(padx=75, pady=30, side='left');

        self.bottomlevel2  = Label(bottomframe2, text='input' ,bg='purple' ,fg='white')
        bottomframe.pack_propagate(False)
        bottomframe.pack()

        bottomframe1.pack_propagate(False)
        bottomframe2.pack_propagate(False)
        bottomframe3.pack_propagate(False)

        bottomframe1.pack(side=LEFT)
        bottomframe2.pack(side=LEFT)
        bottomframe3.pack(side=LEFT)


    def training(self):
        try:
            for i in range(172, 221):
                mypath = 'F:\\machine learning\\Data Set\\Bangla Dataset\\28X28 Dataset\\Train\\' + str(i)
                onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
                self.data_process(mypath, onlyfiles, i)

            self.clf = self.clf.fit(self.X, self.y)
            self.bottomlevel2.configure(text="Train Completed", pady=50,font=("Times New Roman", 14))
            self.bottomlevel2.pack()
        except:
            self.bottomlevel2.configure(text="Error Occure", pady=50,font=("Times New Roman", 14))
            self.bottomlevel2.pack()


    def data_process(self,mypath, onlyfiles, b):
        try:
            for k in range(0, len(onlyfiles)):
                im = Image.open(mypath + '\\' + onlyfiles[k]).convert('L')
                data = np.array(im)
                f = []
                for i in range(0, 28):
                    for j in range(0, 28):
                        f.append(data[i][j])
                self.X.append(f)
                self.y.append(b)
        except:
            self.bottomlevel2.configure(text="Error Occure", pady=50,font=("Times New Roman", 14))
            self.bottomlevel2.pack()

    def chooseFile(self):
        try:
            self.bottomlevel2.configure(text="Please choose a PNG file", pady=50, font=("Times New Roman", 14))
            self.imagefile = filedialog.askopenfilename(
                initialdir="F:\\machine learning\\Data Set\\Bangla Dataset\\28X28 Dataset\\Train",
                title="Select file", filetypes=(("PNG file", ".png"), ("All Files", ".*")))
            self.file_path = self.imagefile

            self.img = PhotoImage(file=self.imagefile)
            inn = self.img
            self.bottomlevel1.configure(image=inn)
            self.bottomlevel1.pack(pady=50)
            self.bottomlevel2.configure(text="PNG file has been Selected", pady=50, font=("Times New Roman", 14))
        except:
            self.bottomlevel2.configure(text="Error Occure", pady=50,font=("Times New Roman", 14))
            self.bottomlevel2.pack()

    def process(self):
        try:
            self.bottomlevel2.configure(text="Processing", pady=50, font=("Times New Roman", 14))
            im = Image.open(self.file_path).convert('L')
            data = np.array(im)
            test = []
            self.test1 = []
            for i in range(0, 28):
                for j in range(0, 28):
                    test.append(data[i][j])

            self.test1.append(test)
            p = self.clf.predict(self.test1)
            self.output(p[0])
        except:
            self.bottomlevel2.configure(text="Error Occure", pady=50,font=("Times New Roman", 14))
            self.bottomlevel2.pack()
    def output(self,val):
        self.bottomlevel2.configure(text="Detected Output", pady=50, font=("Times New Roman", 14))
        self.bottomlevel2.pack()
        self.imagefile1 = 'C:\\Users\\Tarequzzaman\\Dropbox\\machine Learning\\OCR\\Bangla\\' + str(val) + '.png';
        self.img1 = PhotoImage(file=self.imagefile1)
        p = self.img1;
        self.bottomlevel3.configure(image=self.img1)
        self.bottomlevel3.pack(pady=30)



root = Tk()
b = ocr(root)

root.mainloop()
