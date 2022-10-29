from asyncio.windows_events import NULL
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication,QSizePolicy, QMainWindow, QSpacerItem,QFileDialog, QLineEdit, QLabel, QPushButton, QBoxLayout, QVBoxLayout, QHBoxLayout, QWidget, QComboBox, QCheckBox, QTextEdit, QSpinBox
import sys
import os
from datetime import datetime, timedelta
from PySide6.QtCore import Qt
from MyWidget import MyWidget

#JC
from PySide6.QtWidgets import QMessageBox

from getResults import getResults
from models import models
import shutil

#JC
import pandas as pd
import numpy as np
import time
from datetime import datetime
from dateutil.parser import parse
from dateutil.tz import gettz

import ResultData

class Main(QMainWindow): 
    def showResult(self):
        getdata=getResults()
        data = getdata.read_data("output.csv")

        wid=MyWidget(data)
        wid.setMinimumWidth(600)
        graphs=QHBoxLayout()
        graphs.addWidget(wid)
        if self.Hlayout.count()>1:
            self.Hlayout.takeAt(1)
        
        self.Hlayout.addLayout(graphs)


    def __init__(self):
        #Initializes window
        super(Main, self).__init__()

        #Intializes model
        self.model = models()
       
        #Embedded CSS Styling
        #Add group tag in widget constructor eg self.boldTextLbl = QLabel(self, objectName="bold")
        self.setStyleSheet("""
            QLabel#rowLbl {
                font-weight: bold;
                font-size:13px;
            }
            QLabel#warningLbl {
                font-weight: bold;
                font-size:14px;
                color:red;
                text-align:center;
            }
            QPushButton#submit {
                background-color: #0078d4;
                font-weight: bold;
                font-size:13px;
                padding: 12px 28px;
                border-radius: 5px;
            }
            QPushButton#submit:hover {
                color: white;
            }
        """)

        self.initUI()
        self.setWindowTitle("Sentiment Analysis")


    def initUI(self):
        #Creates all widgets
        #Included a widget to apply layout to
        widget = QWidget(self)

        self.nlpLbl = QLabel(self, objectName="rowLbl")
        self.nlpLbl.setText("Select NLP Model")
        self.nlpLbl.setMinimumSize(110, 40)

        self.nlpModel = QComboBox(self)
        self.nlpModel.addItems(["Nlptown", "Finiteautomata", "Cardiffnlp", "Seethal"])

        self.fileLoadLbl = QLabel(self, objectName="rowLbl")
        self.fileLoadLbl.setText("Load Data From")
        self.fileLoadLbl.setMinimumSize(110, 40)

        self.fileLbl = QLabel(self)
        self.fileLbl.setText(".csv, .hsv, .xlsx, .xls")
        self.fileLbl.setMaximumWidth(250)

        self.fileBtn = QPushButton(self)
        self.fileBtn.setText("Select File")
        self.fileBtn.clicked.connect(self.getFile)
        self.fileBtn.setMinimumSize(110,30)

        self.timeLbl = QLabel(self, objectName="rowLbl")
        self.timeLbl.setText('Time Period')
        self.timeLbl.setMinimumSize(110, 40)

        self.timeText = QSpinBox(self)
        self.timeText.setMaximum(999)
        self.timeText.setMinimumWidth(110)
        self.timeText.setAlignment(Qt.AlignCenter)

        self.timePeriod = QComboBox(self)
        self.timePeriod.addItems(["Days", "Weeks", "Months", "Years"])
        self.timePeriod.setMinimumWidth(110)

        self.date1Lbl = QLabel(self, objectName="rowLbl")
        self.date1Lbl.setText('Date Range')
        self.date1Lbl.setMinimumSize(110, 40)

        self.date1Text = QLineEdit(self)
        self.date1Text.setInputMask("99/99/99;")
        self.date1Text.setText("01/04/09;")
        self.date1Text.setMaximumWidth(110)

        self.date2Lbl = QLabel(self)
        self.date2Lbl.setText('to')

        self.date2Text = QLineEdit(self)
        self.date2Text.setInputMask("99/99/99;")
        self.date2Text.setText("01/07/09;")
        self.date2Text.setMaximumWidth(95)

        self.filterLbl = QLabel(self, objectName="rowLbl")
        self.filterLbl.setText('Filter Words')
        self.filterLbl.setMinimumSize(110, 40)

        self.filterLblWhite = QLabel(self)
        self.filterLblWhite.setText('Include')
        self.filterLblWhite.setAlignment(Qt.AlignVCenter)

        self.filterLblBlack = QLabel(self)
        self.filterLblBlack.setText('Exclude')
        self.filterLblBlack.setAlignment(Qt.AlignVCenter)

        self.filterCheckInclude = QCheckBox(self)

        self.filterCheckExclude = QCheckBox(self)
        self.filterCheckExclude.setContentsMargins(0,0,0,0)

        self.includeText = QTextEdit(self)
        self.includeText.setPlaceholderText("Seperate, different, words, using, commas,                       Comment must include one of these words")
        self.includeText.setMaximumSize(160, 80)

        self.excludeText = QTextEdit(self)
        self.excludeText.setPlaceholderText("Comment cannot include any of these words")
        self.excludeText.setMaximumSize(160, 80)

        self.warningLbl = QLabel(self, objectName="warningLbl")
        self.warningLbl.setText(" ")
        self.warningLbl.setMinimumSize(140, 50)
        self.warningLbl.setAlignment(Qt.AlignCenter)

        self.generateBtn = QPushButton(self, objectName="submit")
        self.generateBtn.setText("Generate")
        self.generateBtn.clicked.connect(self.generate)

        self.downloadBtn = QPushButton(self, objectName="submit")
        self.downloadBtn.setText("Download Results")
        self.downloadBtn.clicked.connect(self.saveFile)

        #Layout setup
        self.setCentralWidget(widget)        
        self.Hlayout= QHBoxLayout()
        self.vLayout = QVBoxLayout()

        #First row NLP
        self.row1 = QHBoxLayout()
        self.row1.addWidget(self.nlpLbl)
        self.row1.addWidget(self.nlpModel)
        self.row1.addStretch()

        #Second row file select
        self.row2 = QHBoxLayout()
        self.row2.addWidget(self.fileLoadLbl)
        self.row2.addWidget(self.fileBtn)
        self.row2.addWidget(self.fileLbl)
        self.row2.addStretch()

        #Third row time period
        self.row3 = QHBoxLayout()
        self.row3.addWidget(self.timeLbl)
        self.row3.addWidget(self.timeText)
        self.row3.addWidget(self.timePeriod)
        self.row3.addStretch()
        
        #Fourth row date range
        self.row4 = QHBoxLayout()
        self.row4.addWidget(self.date1Lbl)
        self.row4.addWidget(self.date1Text)
        self.row4.addWidget(self.date2Lbl)
        self.row4.addWidget(self.date2Text)
        self.row4.addStretch()

        #Fifth row filter
        self.row5 = QHBoxLayout()
        self.row5.addWidget(self.filterLbl)

        self.checkboxes = QVBoxLayout()
        self.checkInclude = QHBoxLayout()
        self.checkInclude.addWidget(self.filterCheckInclude)
        self.checkInclude.addWidget(self.filterLblWhite)
        self.checkInclude.addWidget(self.includeText)
        self.checkInclude.addStretch()
        self.checkboxes.addLayout(self.checkInclude)

        self.checkExclude = QHBoxLayout()
        self.checkExclude.addWidget(self.filterCheckExclude)
        self.checkExclude.addWidget(self.filterLblBlack)
        self.checkExclude.addWidget(self.excludeText)
        self.checkExclude.addStretch()
        self.checkboxes.addLayout(self.checkExclude)

        self.row5.addLayout(self.checkboxes)

        #Sixth row warning
        self.row6 = QHBoxLayout()
        self.row6.addWidget(self.warningLbl)

        #Seventh row buttons
        self.row7 = QHBoxLayout()
        self.row7.addWidget(self.generateBtn)
        self.row7.addStretch()
        self.row7.addWidget(self.downloadBtn)

        #Adding rows to column
        self.vLayout.addLayout(self.row1)
        self.vLayout.addLayout(self.row2)
        self.vLayout.addLayout(self.row3)
        self.vLayout.addLayout(self.row4)
        self.vLayout.addLayout(self.row5)
        self.vLayout.addLayout(self.row6)
        self.vLayout.addLayout(self.row7)
        self.Hlayout.addLayout(self.vLayout)
        
        #JC
        self.row8 = QHBoxLayout()
        self.totalRowCount = QLabel(self)
        self.row8.addWidget(self.totalRowCount)
        self.totalRowCount.setText('')
        self.row8.addStretch()
        self.vLayout.addLayout(self.row8)

        self.row9 = QHBoxLayout()
        self.actualResult = QLabel(self)
        self.row9.addWidget(self.actualResult)
        self.actualResult.setText('')
        self.row9.addStretch()
        self.vLayout.addLayout(self.row9)

        self.row10 = QHBoxLayout()
        self.predictedResult = QLabel(self)
        self.row10.addWidget(self.predictedResult)
        self.predictedResult.setText('')
        self.row10.addStretch()
        self.vLayout.addLayout(self.row10)

        self.row11 = QHBoxLayout()
        self.vLayout.addLayout(self.row11)

        #JC
        self.vLayout.addLayout(self.row7)

        self.Hlayout.addLayout(self.vLayout)
        widget.setLayout(self.Hlayout)

    #JC
    def showSentimentAnalysisResult(self,myresult):
        print('showSentimentAnalysisResult called')
        self.totalRowCount.setText('Total Row Processed: {0} '.format(myresult.totalRow))
        self.actualResult.setText('Original Dataset -- Positive: {0}  Negative: {1}'.format( myresult.truePositive,myresult.trueNegative))
        self.predictedResult.setText('Processed Dataset -- Positive: {0}  Negative: {1}  Neutral: {2}'.format( myresult.predictedPositive,myresult.predictedNegative,myresult.predictedNeutral))
        

    def getFile(self):
        fileFilter = 'Comma Seperated Values (*.csv);;Hash Seperated Values (*.hsv);; Excel File (*.xlsx, *xls)'
        #Filedeets is tuple. [0] is filename and [1] is file type
        self.fileDeets = QFileDialog.getOpenFileName(
            parent = self,
            caption = 'Select a Data Set',
            dir = os.getcwd(),
            filter = fileFilter,
            selectedFilter = 'Comma Seperated Values (*.csv)')
        self.fileLbl.setText(self.fileDeets[0])
        self.fileLbl.adjustSize()

    def saveFile(self):
        local = os.getcwd()
        fileDeets = QFileDialog()
        fileDeets.setFileMode(QFileDialog.AnyFile);
        dest = fileDeets.getSaveFileName(
            parent = self,
            caption = 'Save File...',
            dir = local)
        shutil.copy(local + "\\output.csv", dest[0])

    
    #JC
    def showdialog(self, text):
       msg = QMessageBox()
       msg.setIcon(QMessageBox.Warning)

       msg.setText(text)
       msg.setWindowTitle("Warning")
       msg.setStandardButtons(QMessageBox.Ok)
       retval = msg.exec_()
       print("value of pressed message box button:", retval)
    
        
    #JC
    def convertDate(self,t):
        tzInfo = {"PDT": gettz("US/Pacific")}
        return parse(t, tzinfos=tzInfo)

    #JC
    def getStartDate(self):
        column_name = ["Scale", "TweetID", "Date", "Query", "User", "Comments"]
        if hasattr(self, 'fileDeets') == False:
            print("fileDeet is not set")
            self.showdialog('Please Select a file first')
            return NULL
        df=pd.read_csv(self.fileDeets[0],names=column_name, encoding='latin-1')
        df=df['Date'].copy()
        dates=df.to_numpy()
        applyall = np.vectorize(self.convertDate)
        dates = applyall(dates)
        startDate=dates.min()
        print('startDate found=', startDate)
        return startDate.date()


    def generate(self):
        #If time needed, remove .date()
        #Gets the calender dates
        if self.timeText.text() == "0":
            if len(self.date1Text.text()) < 8:
                self.warningLbl.setText("Please include leading 0s in the dates")
            elif int(self.date1Text.text()[0:2]) > 31 or int(self.date1Text.text()[0:2]) == 00:
                self.warningLbl.setText("Invalid day for starting date")
                return False
            elif int(self.date1Text.text()[3:5]) > 12 or int(self.date1Text.text()[3:5]) == 00:
                self.warningLbl.setText("Invalid day for starting month")
                return False
            elif int(self.date2Text.text()[0:2]) > 31 or int(self.date2Text.text()[0:2]) == 00:
                self.warningLbl.setText("Invalid day for ending date")
                return False
            elif int(self.date2Text.text()[3:5]) > 12 or int(self.date2Text.text()[3:5]) == 00:
                self.warningLbl.setText("Invalid day for ending month")
                return False
            #Extra cases for feb
            else:
                fromDate = datetime.strptime(self.date1Text.text(), "%d/%m/%y").date()
                endDate = datetime.strptime(self.date2Text.text(), "%d/%m/%y").date()
        #Or converts time period to a date
        else:
            #JC

            fromDate=self.getStartDate()

            if fromDate==NULL:
                raise Exception("Pick a file first")
            
            #endDate = datetime.today().date()
            timeNum = int(self.timeText.text())
            if self.timePeriod.currentText() == "Days":
                dateGap = timedelta(days=timeNum)
            elif self.timePeriod.currentText() == "Weeks":
                dateGap = timedelta(weeks=timeNum)
            elif self.timePeriod.currentText() == "Months":
                #Date math only goes up to weeks so used multiplication workaround
                timeNum  = timeNum*4
                dateGap = timedelta(weeks=timeNum)
            elif self.timePeriod.currentText() == "Years":
                timeNum  = timeNum*52
                dateGap = timedelta(weeks=timeNum)

            #JC
            #fromDate = (endDate - dateGap)
            endDate=(fromDate+dateGap)
        try:
            #if startdate less than end date throw exception
            #JC
            print('File Process is ', self.fileDeets[0], '\n')

            if endDate < fromDate:
                self.warningLbl.setText("The starting date cannot be later than the end date")
            #TODO: Data processing here? convert Include/Exclude to one variable, 
            else:
                self.warningLbl.setText(" ")
                #Model (Can get text or index)  , File tuple    ,start date,end date, Include filter? (True/False)     , Exclude filter? (True/False)    , include words,   exclude words       
                print(self.nlpModel.currentText(), self.fileDeets, fromDate, endDate, self.filterCheckInclude.isChecked(), self.filterCheckExclude.isChecked(),  self.includeText.toPlainText(), self.excludeText.toPlainText())

                #JC
                self.myresult=ResultData


                #self.model.run(self.nlpModel.currentText(), self.fileDeets, fromDate, endDate, self.filterCheckInclude.isChecked(), self.filterCheckExclude.isChecked(),  self.includeText.toPlainText(),self.excludeText.toPlainText())
                #JC
                self.model.run(self.nlpModel.currentText(), self.fileDeets, fromDate, endDate, self.filterCheckInclude.isChecked(), self.filterCheckExclude.isChecked(),  self.includeText.toPlainText(),self.excludeText.toPlainText(),self.myresult)
                self.showResult()
               
                #JC
                print('TRUE POSITIVE=',self.myresult.truePositive)
                self.showSentimentAnalysisResult(self.myresult)

        except AttributeError as e:
            print(e)
            self.warningLbl.setText("Please select a dataset to use")



