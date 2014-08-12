#! /usr/bin/env python
# -*- coding: shift_jis -*-
"""
jentry.py

japanese entry

June 30, 2005
"""


import Tkinter as Tk


FONT = ('Helvetica', '12')
WIDTH = 30

class Frame(Tk.Frame):

    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        l_name = Tk.Label(self, font=FONT, text=u"お名前")
        l_address  = Tk.Label(self, font=FONT, text=u"ご住所")
        self.s1 = Tk.StringVar()
        self.s2 = Tk.StringVar()
        self.s3 = Tk.StringVar()
        e1 = Tk.Entry(self, textvariable = self.s1, width=WIDTH, font=FONT)
        e2 = Tk.Entry(self, textvariable = self.s2, width=WIDTH, font=FONT)
        e3 = Tk.Entry(self, textvariable = self.s3, width=WIDTH, font=FONT)
        self.bind_class("Entry", '<Return>', self.make_echo)

        self.s = Tk.StringVar()
        l_echo = Tk.Label(self, font=FONT, textvariable = self.s, anchor=Tk.W, justify=Tk.LEFT)

        l_name.grid(row=0, column=0, padx=5, pady=2)
        l_address.grid(row=1, column=0, padx=5, pady=2)
        e1.grid(row=0, column=1, padx=5, pady=2)
        e2.grid(row=1, column=1, padx=5, pady=2)
        e3.grid(row=2, column=1, padx=5, pady=2)
        l_echo.grid(row=3, column=0, columnspan=2, padx=30, pady=10, sticky=Tk.W + Tk.E)


    def make_echo(self, event):
        self.s.set(u'お名前：\t%s\nご住所：\t%s\n\t%s\n' % (self.s1.get(), self.s2.get(), self.s3.get()))


##------------------------------------------------

if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()