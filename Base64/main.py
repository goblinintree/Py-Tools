#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a hello world GUI example.'

from Tkinter import *
import base64

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets(master)

    def do_decode(src_str):
        if not isinstance(src_str, unicode):
            t = type(src_str)
            src_str = unicode(src_str, t)
        return base64.b64decode(src_str)

    def do_encode(src_str):
        if not isinstance(src_str, unicode):
            t = type(src_str)
            src_str = unicode(src_str, t)
        return base64.b64encode(src_str)

    def createWidgets(self,master=None):
        self.frame_1 = Frame(master)
        self.baseSrcLabel = Label(self.frame_1, text=u'Base64源')
        self.baseSrcLabel.pack()
        self.srcText = Text(self.frame_1, height="10")
        self.srcText.pack()
        self.frame_1.pack(side=TOP)

        self.frame_2 = Frame(master)
        self.decodeButton = Button(self.frame_2, text='解码')
        self.decodeButton.pack(side=LEFT)
        self.encodeButton = Button(self.frame_2, text='编码')
        self.encodeButton.pack(side=LEFT)
        self.frame_2.pack(side=TOP)

        self.frame_3 = Frame(master)
        self.basedistLabel = Label(self.frame_3, text=u'Base64目标')
        self.basedistLabel.pack()
        self.srcText = Text(self.frame_3, height="10")
        self.srcText.pack()
        self.frame_3.pack(side=TOP)

        self.frame_4 = Frame(master)
        self.quitButton = Button(self.frame_4, text='Quit', command=self.quit)
        self.quitButton.pack()
        self.frame_4.pack(side=TOP)


app = Application()
# 窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()