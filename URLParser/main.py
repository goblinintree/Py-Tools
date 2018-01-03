#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a hello world GUI example.'

from Tkinter import *
import urllib
import chardet

import sys
print sys.getdefaultencoding()

def check_code(s_text_str):
    if isinstance(s_text_str, unicode):
        print "check_code >> unicode"
    else:
        print "check_code >> ", chardet.detect(s_text_str)
    pass

def str_code_utf8(strings):

    return strings


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets(master)

    def do_url_unquote(self, rawurl):
        print "100000000001"
        return urllib.unquote(rawurl)

    def do_url_quote(self, rawurl):
        print "200000000001"
        return urllib.quote(rawurl)

    def do_unquote_action(self):
        s_text= self.srcText
        d_text = self.distText
        s_text_str = s_text.get('1.0',END)
        print 1111, s_text_str
        check_code(s_text_str)
        s_text_str = s_text_str.encode("UTF-8")
        check_code(s_text_str)
        d_text_str=self.do_url_unquote(s_text_str)
        d_text.delete(1.0,END)
        d_text.insert(1.0,d_text_str)
        pass

    def do_quote_action(self):
        s_text= self.srcText
        d_text = self.distText
        s_text_str = s_text.get('1.0',END)
        print 2222, s_text_str
        check_code(s_text_str)
        s_text_str = s_text_str.encode("UTF-8")
        check_code(s_text_str)

        d_text_str=self.do_url_quote(s_text_str)
        d_text.delete(1.0,END)
        d_text.insert(1.0,d_text_str)
        pass

    # def select_all_src(self):
    #     print "300000000001"
    #     d_text = self.distText
    #     # d_text.
    #     pass

    def createWidgets(self,master=None):
        # self.src_text = StringVar(value="None")
        # self.dist_text = StringVar(value="None")

        self.frame_1 = Frame(master)
        self.baseSrcLabel = Label(self.frame_1, text=u'URL源')
        self.baseSrcLabel.pack()
        self.srcText = Text(self.frame_1, height="10")
        self.srcText.pack()
        self.srcText.insert(INSERT,"src")
        self.frame_1.pack(side=TOP)

        self.frame_2 = Frame(master)
        self.decodeButton = Button(self.frame_2, text=u'解码', command = self.do_unquote_action )
        self.decodeButton.pack(side=LEFT)
        self.encodeButton = Button(self.frame_2, text=u'编码', command = self.do_quote_action )
        self.encodeButton.pack(side=LEFT)
        self.frame_2.pack(side=TOP)

        self.frame_3 = Frame(master)
        self.basedistLabel = Label(self.frame_3, text=u'URL目标')
        self.basedistLabel.pack()
        self.distText = Text(self.frame_3, height="10")
        self.distText.pack()
        self.distText.insert(INSERT,"dist")
        self.frame_3.pack(side=TOP)

        self.frame_4 = Frame(master)
        self.quitButton = Button(self.frame_4, text='Quit', command=self.quit)
        self.quitButton.pack()
        self.frame_4.pack(side=TOP)
        # self.distText.bind("<Double-Button-1>",  command = self.select_all_src)
        

app = Application()
# 窗口标题:
app.master.title(u'URL加解密工具')
# 主消息循环:
app.mainloop()