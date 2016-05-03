#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# guy.py
#
###########################################################################
# Main GUI
###########################################################################

import wx
import wx.xrc
import EnhancedStatusBar as ESB

###########################################################################
# Class Frame
###########################################################################


class Frame(wx.Frame):
    def __init__(self, parent):
        style_noresize = wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Millum Catalog Uploader", pos=wx.DefaultPosition,
                          size=wx.Size(540, 390), style=style_noresize | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        vbox = wx.BoxSizer(wx.VERTICAL)

        self.label1 = wx.StaticText(self, wx.ID_ANY, u"1 - Select a Catalog File", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        self.label1.Wrap(-1)
        self.label1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        vbox.Add(self.label1, 0, wx.ALL | wx.EXPAND, 5)

        self.catalog_file_select = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a Catalog File",
                                                     u"XML File (*.XML) |*.XML", wx.DefaultPosition, wx.DefaultSize,
                                                     wx.FLP_DEFAULT_STYLE)
        vbox.Add(self.catalog_file_select, 0, wx.ALL | wx.EXPAND, 5)

        vbox.AddSpacer((0, 25), 0, 0, 1)

        self.label2 = wx.StaticText(self, wx.ID_ANY, u"2 - Select a Discount file", wx.DefaultPosition, wx.DefaultSize,
                                    wx.ALIGN_LEFT)
        self.label2.Wrap(-1)
        self.label2.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        vbox.Add(self.label2, 0, wx.ALL | wx.EXPAND, 5)

        self.discount_file_select = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a Discount File",
                                                      u"XML File (*.XML) |*.XML", wx.DefaultPosition, wx.DefaultSize,
                                                      wx.FLP_DEFAULT_STYLE)
        self.discount_file_select.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.discount_file_select.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        vbox.Add(self.discount_file_select, 0, wx.ALL | wx.EXPAND, 5)

        self.label3 = wx.StaticText(self, wx.ID_ANY,
                                    u"3 - When ready press Run to apply  the discounts to the catalog and upload them to Millum FTP ",
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.label3.Wrap(-1)
        self.label3.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        vbox.Add(self.label3, 1, wx.ALL, 5)

        bsizer = wx.BoxSizer(wx.HORIZONTAL)

        bsizer.AddSpacer((0, 0), 1, 0, 5)

        self.run_button = wx.Button(self, wx.ID_ANY, u"Run", wx.DefaultPosition, wx.DefaultSize, 0)
        bsizer.Add(self.run_button, 0, wx.ALL, 5)

        self.quit_button = wx.Button(self, wx.ID_ANY, u"Quit", wx.DefaultPosition, wx.DefaultSize, 0)
        bsizer.Add(self.quit_button, 0, wx.ALL, 5)

        vbox.Add(bsizer, 0, wx.EXPAND | wx.TOP, 15)

        self.SetSizer(vbox)
        self.Layout()
        self.statusbar = ESB.EnhancedStatusBar(self, -1)
        self.statusbar.SetSize((-1, 23))
        self.statusbar.SetFieldsCount(2)
        self.SetStatusBar(self.statusbar)

        self.progress = wx.Gauge(self.statusbar, -1, range=100, size=(250, 25))
        self.statusbar.AddWidget(self.progress, ESB.ESB_EXACT_FIT, pos=1)

        self.Centre(wx.BOTH)

        # Connect Events
        self.catalog_file_select.Bind(wx.EVT_FILEPICKER_CHANGED, self.pickCatalogFile)
        self.discount_file_select.Bind(wx.EVT_FILEPICKER_CHANGED, self.pickDiscountFile)
        self.run_button.Bind(wx.EVT_BUTTON, self.onRun)
        self.quit_button.Bind(wx.EVT_BUTTON, self.onQuit)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def pickCatalogFile(self, event):
        event.Skip()

    def pickDiscountFile(self, event):
        event.Skip()

    def onRun(self, event):
        event.Skip()

    def onQuit(self, event):
        event.Skip()
