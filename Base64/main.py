#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a hello world GUI example.'

from Tkinter import *
import base64
import chardet

import sys
print sys.getdefaultencoding()

def decode_base64(data):
            """Decode base64, padding being optional.
            :param data: Base64 data as an ASCII byte string
            :returns: The decoded byte string.
            {'confidence': 0.0, 'language': None, 'encoding': None}
            """
            missing_padding = 4 - len(data) % 4
            if missing_padding:
                data += b'='* missing_padding
            return base64.decodestring(data)

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

    def do_decode(self, src_str):
        print "100000000001"
        return decode_base64(src_str)

    def do_encode(self, src_str):
        print "200000000001"
        return base64.b64encode(src_str)

    def do_encode_action(self):
        s_text= self.srcText
        d_text = self.distText
        s_text_str = s_text.get('1.0',END)
        print 1111, s_text_str
        check_code(s_text_str)
        s_text_str = s_text_str.encode("UTF-8")
        check_code(s_text_str)
        d_text_str=self.do_encode(s_text_str)
        d_text.delete(1.0,END)
        d_text.insert(1.0,d_text_str)
        pass

    def do_decode_action(self):
        s_text= self.srcText
        d_text = self.distText
        s_text_str = s_text.get('1.0',END)
        print 2222, s_text_str
        check_code(s_text_str)
        s_text_str = s_text_str.encode("UTF-8")
        check_code(s_text_str)

        d_text_str=self.do_decode(s_text_str)
        d_text.delete(1.0,END)
        d_text.insert(1.0,d_text_str)
        pass

    def createWidgets(self,master=None):
        # self.src_text = StringVar(value="None")
        # self.dist_text = StringVar(value="None")

        self.frame_1 = Frame(master)
        self.baseSrcLabel = Label(self.frame_1, text=u'Base64源')
        self.baseSrcLabel.pack()
        self.srcText = Text(self.frame_1, height="10")
        self.srcText.pack()
        self.srcText.insert(INSERT,"src")
        self.frame_1.pack(side=TOP)

        self.frame_2 = Frame(master)
        self.decodeButton = Button(self.frame_2, text=u'解码', command = self.do_decode_action )
        self.decodeButton.pack(side=LEFT)
        self.encodeButton = Button(self.frame_2, text=u'编码', command = self.do_encode_action )
        self.encodeButton.pack(side=LEFT)
        self.frame_2.pack(side=TOP)

        self.frame_3 = Frame(master)
        self.basedistLabel = Label(self.frame_3, text=u'Base64目标')
        self.basedistLabel.pack()
        self.distText = Text(self.frame_3, height="10")
        self.distText.pack()
        self.distText.insert(INSERT,"dist")
        self.frame_3.pack(side=TOP)

        self.frame_4 = Frame(master)
        self.quitButton = Button(self.frame_4, text='Quit', command=self.quit)
        self.quitButton.pack()
        self.frame_4.pack(side=TOP)


app = Application()
# 窗口标题:
app.master.title(u'base64工具')
# 主消息循环:
app.mainloop()