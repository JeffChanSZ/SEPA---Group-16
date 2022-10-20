import argparse
from socket import TCP_NODELAY
import sys
from tkinter import messagebox
import pandas as pd
from MyWidget import MyWidget
from PySide6.QtCore import QDateTime, QTimeZone

#JC
from PySide6.QtWidgets import QMessageBox

from PySide6.QtWidgets import QApplication 
from datetime import datetime
from dateutil.parser import parse
from dateutil.tz import gettz

class getResults(object):
    """description of class"""
    def __init__(self):
        pass
    def date(self, utc):
        d=utc[0:10]
        utc_fmt = "yyyy-MM-dd"

        new_date = QDateTime().fromString(d, utc_fmt)
        tes=new_date.toString()
        return new_date    

    #JC
    def showdialog(self, text):
       msg = QMessageBox()
       msg.setIcon(QMessageBox.Warning)

       msg.setText(text)
       msg.setWindowTitle("Warning")
       msg.setStandardButtons(QMessageBox.Ok)
       retval = msg.exec_()
       print("value of pressed message box button:", retval)

   
    def read_data(self, fname):
        # Read the CSV content
        df = pd.read_csv(fname)
        
        #JCC
        if df.empty :
            print('Warning! DataFrame is Empty\n')
            self.showdialog('DataFrame Empty!')
            return ([],[])


        # Remove wrong magnitudes
        df['date'] = df['date'].str[:10]
        df= df.groupby('date', as_index=False).mean()
        dates = df["date"].apply(lambda x: self.date(x))
        sentiment=df["scale"].apply(lambda x: round(x,3))
        # My local timezone

        # Get timestamp transformed to our timezone

        return dates, sentiment