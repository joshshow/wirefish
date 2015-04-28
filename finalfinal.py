#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 on Tue Apr 28 15:23:51 2015
#

import wx
import socket, sys
from struct import *
from scapy.all import *
from StringIO import StringIO
# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    packetNum = 5
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("Wirefish"), style=wx.ALIGN_CENTRE)
        self.startButton = wx.Button(self, wx.ID_ANY, _("Start"))
        self.label_2 = wx.StaticText(self, wx.ID_ANY, _("Choose Number \nof Captures"), style=wx.ALIGN_CENTRE)
        self.captureNum = wx.TextCtrl(self, wx.ID_ANY, "")
        self.captureList = wx.ListBox(self, wx.ID_ANY, choices=[])

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.startAnalyzer, self.startButton)
        self.Bind(wx.EVT_TEXT_ENTER, self.getTextEnter, self.captureNum)
        self.Bind(wx.EVT_TEXT, self.getText, self.captureNum)
        self.Bind(wx.EVT_LISTBOX, self.listboxShow, self.captureList)
        self.captureList.Append("Welcome to the Network Protocol Analyzer")
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle(_("frame_1"))
        self.SetSize((872, 482))
        self.label_1.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.startButton.SetBackgroundColour(wx.Colour(100, 255, 116))
        self.startButton.SetForegroundColour(wx.Colour(0, 1, 0))
        self.startButton.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.label_2.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.captureList.SetMinSize((852, 250))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_2 = wx.GridSizer(2, 1, 0, 0)
        sizer_1.Add(self.label_1, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 10)
        grid_sizer_1.Add(self.startButton, 0, wx.ALL | wx.EXPAND, 10)
        grid_sizer_2.Add(self.label_2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_2.Add(self.captureNum, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        sizer_1.Add(self.captureList, 0, wx.ALL | wx.EXPAND, 10)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def startAnalyzer(self, event):  # wxGlade: MyFrame.<event_handler>
        self.captureList.Append("\nCapturing packets...")
	print(self.packetNum)        
	string = sniff(prn=lambda x: x.summary(),count=int(self.packetNum))
        capture = StringIO()
        save_stdout = sys.stdout
        sys.stdout = capture
        string.show()
        sys.stdout = save_stdout
        self.captureList.Append(capture.getvalue())
        self.captureList.Append(' ')
            

    def getTextEnter(self, event):  # wxGlade: MyFrame.<event_handler>
        self.captureList.Append("\nCapturing packets...")
               
        string = sniff(prn=lambda x: x.summary(),count=int(self.packetNum))
        capture = StringIO()
        save_stdout = sys.stdout
        sys.stdout = capture
        string.show()
        sys.stdout = save_stdout
        self.captureList.Append(capture.getvalue())
        self.captureList.Append(' ')
    def getText(self, event):  # wxGlade: MyFrame.<event_handler>
        self.packetNum = self.captureNum.GetLineText(0)
	print(self.packetNum)
        

    def listboxShow(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler 'listboxShow' not implemented!"
        event.Skip()

# end of class MyFrame
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, wx.ID_ANY, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
