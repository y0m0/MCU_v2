#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  millum_catalog_uploader.py
#  

import os
import wx
import gui
import clean_catalog
import apply_discounts
from ftplib import FTP


class GuiFrame(gui.Frame):
    def __init__(self, parent):
        gui.Frame.__init__(self, parent)

    def pickDiscountFile(self, event):
        return self.discount_file_select.GetPath()

    def pickCatalogFile(self, event):
        return self.catalog_file_select.GetPath()

    def onRun(self, event):
        cat_file = self.pickCatalogFile(event)
        disc_file = self.pickDiscountFile(event)

        # Check if both the needed files have been selected
        if cat_file != '' and disc_file != '':

            # clean the catalog file from unwanted products
            clean_catalog.clean(cat_file)
            self.progress.SetValue(20)
            self.statusbar.SetStatusText('Catalog Cleaned!')

            # apply the discount to the catalog
            apply_discounts.twelve_percent(open(cat_file).read(), open('Standard_Catalog.xml', 'w'))
            self.progress.SetValue(40)
            apply_discounts.custom(open(cat_file).read(), open(disc_file).read(), open('Villa_Catalog.xml', 'w'))
            self.progress.SetValue(60)
            self.statusbar.SetStatusText('Catalogs Generated!')


            # Connect to Millim FTP
            ftp = FTP('ftp.millum.no')
            ftp.login('*USERNAME*', '*PASSWORD*')
            self.progress.SetValue(70)
            self.statusbar.SetStatusText('Connected to Millum FTP')
            # Change working directory to /In/Catalog
            ftp.cwd('/villaimport/In/catalog')
            # Upload the Standard Catalog
            ftp.storbinary('STOR Standard_Catalog.xml', open('Standard_Catalog.xml', 'rb'))
            self.progress.SetValue(80)
            self.statusbar.SetStatusText('Standard Catalog Uploaded!')
            # Upload the Villa Catalog
            ftp.storbinary('STOR Villa_Catalog.xml', open('Villa_Catalog.xml', 'rb'))
            self.progress.SetValue(90)
            self.statusbar.SetStatusText('Villa Catalog Uploaded!')
            # Close the FTP session
            ftp.close()
            self.progress.SetValue(100)
            self.statusbar.SetStatusText('Done!')

        else:
            if cat_file == '' and disc_file != '':
                self.statusbar.SetStatusText('Please Select a Catalog File!')
            elif disc_file == '' and cat_file != '':
                self.statusbar.SetStatusText('Please Select a Discount File!')
            else:
                self.statusbar.SetStatusText('Please Select a Catalog and a Discount File!')


    def onQuit(self, event):
        try:
            os.remove('Standard_Catalog.xml')
            os.remove('Villa_Catalog.xml')
        except:
            pass
        self.Close()


def main():
    app = wx.App()
    frame = GuiFrame(None)
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
