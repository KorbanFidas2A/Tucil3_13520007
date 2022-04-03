import tkinter as Tk
import numpy as np
import time
from tkinter import messagebox
import sys

#ganti dengan path dimana menyimpan algoritma branch and bound
sys.path.insert(0, 'D:\Semester4\StrategiAlgoritma\Tucil3\BnB')
from solver import BranchandBound as bb, node, prioQueue

class GUI(Tk.Frame):
    #me-nginisiasi parent
    def __init__(self,parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
    
    #menambahkan matrix yang disimpan dalam atribut matrix
    def matrixmake(self, matrix):
        self.matrix = matrix

    #melakukan change state jika user menekan tombol "next"
    def changestate(self, matindex, len_matrix):
        if(matindex < len_matrix -1):
            matindex += 1
        else:
            messagebox.showinfo("state puzzle", "Puzzle berhasil ditemukan!")
        for j in range(0,self.a.shape[0]):
            for k in range(0,self.a.shape[1]):
                root.update()
                test_integer = self.matrix[matindex]
                integer = test_integer[j][k]
                if(integer != 0): 
                    self.b = Tk.Button(self.frame, text = str(integer), height= 5, width=10, font = ('4'))
                else:
                    self.b = Tk.Button(self.frame, text = " ", height= 5, width=10, bg='blue', font = ('4'))
                self.b.grid(row=j,  column= k)
        self.btn1= Tk.Button(self.frame, text="Next" , command = lambda : self.changestate(matindex, len_matrix), font = ('Helvetica'))
        self.btn1.grid(row=4,  column=1)
        self.btn2= Tk.Button(self.frame, text="Previous", command = lambda : self.changestate2(matindex, len_matrix), font = ('Helvetica'))
        self.btn2.grid(row=4,  column=0)
    
    #melakukan change state jika user menekan tombol "previous"
    def changestate2(self, matindex, len_matrix):
        if(matindex > 1):
            matindex -= 1
        else:
            messagebox.showinfo("state puzzle", "Ini adalah state awal Puzzle!")
        for j in range(0,self.a.shape[0]):
            for k in range(0,self.a.shape[1]):
                root.update()
                test_integer = self.matrix[matindex]
                integer = test_integer[j][k]
                if(integer != 0): 
                    self.b = Tk.Button(self.frame, text = str(integer), height= 5, width=10, font = ('4'))
                else:
                    self.b = Tk.Button(self.frame, text = " ", height= 5, width=10, bg='blue', font = ('4'))
                self.b.grid(row=j,  column= k)
        self.btn1= Tk.Button(self.frame, text="Next" , command = lambda : self.changestate(matindex, len_matrix), font = ('Helvetica'))
        self.btn1.grid(row=4,  column=1)
        self.btn2= Tk.Button(self.frame, text="Previous", command = lambda : self.changestate2(matindex, len_matrix), font = ('Helvetica'))
        self.btn2.grid(row=4,  column=0)

    #untuk memulai pemrosesan pembuatan GUI    
    def initialize(self):
        '''
        Mengontrol board yang menampilkan angka
        '''
        self.parent.title("15-Puzzle Branch and Bound")       
        self.parent.grid_rowconfigure(1,weight=1)
        self.parent.grid_columnconfigure(1,weight=1)
        root.geometry("700x700")

        self.frame = Tk.Frame(self.parent)  
        self.frame.pack(fill=Tk.X, padx=1, pady=1)

        # Membuat array 4, 4
        self.a = np.zeros((4,4))
        len_matrix = len(self.matrix)
        index_matrix = 1
        for j in range(0,self.a.shape[0]):
            for k in range(0,self.a.shape[1]):
                test_integer = self.matrix[index_matrix]
                integer = test_integer[j][k]
                if(integer != 0): 
                    self.b = Tk.Button(self.frame, text = str(integer), height= 5, width=10, font = ('4'))
                else:
                    self.b = Tk.Button(self.frame, text = "  ", height= 5, width=10, bg='blue', font = ('4'))
                self.b.grid(row=j,  column= k)
        self.btn1= Tk.Button(self.frame, text="Next" , command = lambda : self.changestate(index_matrix, len_matrix), font = ('Helvetica'))
        self.btn1.grid(row=4,  column=1)
        self.btn2= Tk.Button(self.frame, text="Previous", command = lambda : self.changestate2(index_matrix, len_matrix), font = ('Helvetica'))
        self.btn2.grid(row=4,  column=0)
