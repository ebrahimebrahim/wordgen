#!/usr/bin/python3
# -*- coding: utf-8 -*-

from wordgen import *
from english import *
from arabic import *
from qlumb import *

from sys import exit, argv

from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

btn_width=50

class wgWindow(QWidget): # main Qt window for wordgen
	def __init__(self):
		super().__init__() # calls initialiser of parent function (QWidget)
		self.initUI()
	def initUI(self): # initialises UI of main window
		self.setupWordfield()
		self.initLayout()
		self.initWindow()
	def initLayout(self): # sets up layout of the various widgets on the window
		vbox = QVBoxLayout() # a vertical "box" that will arrange the layout
		vbox.addWidget(self.wordfield) # this adds the wordfield at the top...the order in which things are added determines how they will show up
		vbox.addStretch(1) # this is a "stretch factor," which will change in size as the window is resized. putting it below the wordfield ensures the wordfield will remain at the top always
		vbox.addLayout( self.makeButtonLayout("English",self.genEnglishWord) )
		vbox.addStretch(1)
		vbox.addLayout( self.makeButtonLayout("ﻉﺮﺒﻳﺓ",self.genArabicWord) )
		vbox.addStretch(1)
		vbox.addLayout( self.makeButtonLayout("Qlumb",self.genQlumbWord) )
		hbox = QHBoxLayout() # this is a horizontal box. it will contain the entire vertical box. putting it between two stretch factors ensures that the vertical box remains horizontally centered
		hbox.addStretch(1)
		hbox.addLayout(vbox)
		hbox.addStretch(1)
		self.setLayout(hbox) # the hbox contains everything that was added in this function, and the layout is then set to it
	def makeButtonLayout(self, button_text, button_function): # sets up a button labeled by button_text with button_function as the function called when it's clicked
		""" sets up a button labeled by button_text with button_function as the function called when it's clicked
		    returns a QHBoxLayout containing the centered button """
		new_button = QPushButton(button_text)
		new_button.clicked.connect(button_function)
		new_button.setMaximumWidth(btn_width)
		new_button_layout = QHBoxLayout()
		new_button_layout.addStretch(1)
		new_button_layout.addWidget(new_button)
		new_button_layout.addStretch(1)
		return new_button_layout
	def genEnglishWord(self): # generates an english word, updating the wordfield to display the word in english and IPA displays
		word = gen_word(english)
		self.wordfield.setText(display_word(word,"english")+"\n"+display_word(word,"IPA"))
	def genArabicWord(self): # generates an arabi word, updating the wordfield to display the word in arabi and IPA displays
		word = gen_word(arabic)
		self.wordfield.setText(display_word(word,"arabic")+"\n"+display_word(word,"IPA"))
	def genQlumbWord(self):# generates a qlumb word, updating the wordfield to display the word in qlumb and IPA displays
		word = gen_word(qlumb)
		self.wordfield.setText(display_word(word,"qlumb")+"\n"+display_word(word,"IPA"))
	def setupWordfield(self): # sets up wordfield, where the generated words will be displayed
		self.wordfield = QLabel() # the wordfield is a QLabel, just a text display where the text can be updated
		self.wordfield.setTextInteractionFlags(Qt.TextSelectableByMouse) # makes the text selectable by mouse, in case someone wanted to copy a generated word
		self.wordfield.setText("To generate a word,\nchoose a language below:") # this is just the starting text
	def initWindow(self): # sets up window itself on the screen
		self.resize(self.minimumSizeHint()) # sets window to smallest possible size (given all the other widgets that were introduced)
		self.centerWindow()
		self.setWindowTitle("WordGen")
		self.show()
	def centerWindow(self): # centers window on user's desktop by determining desktop geometry
		rect = self.frameGeometry()
		centerpoint = QDesktopWidget().availableGeometry().center()
		rect.moveCenter(centerpoint)
		self.move(rect.topLeft())
		

if __name__ == "__main__":
	app = QApplication(argv)
	wgw = wgWindow()
	exit(app.exec_()) # launches QApplication while script exits so that it can return error code if necessary
