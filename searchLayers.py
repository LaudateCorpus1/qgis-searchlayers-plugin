from PyQt4.QtCore import QUrl
from PyQt4.QtGui import QIcon, QAction

import os
import webbrowser

from .searchDialog import LayerSearchDialog

class SearchLayers:
    def __init__(self, iface):
        self.iface = iface
        self.searchDialog = None

    def initGui(self):
        # Create the menu items in the Plugin menu and attach the icon to the toolbar
        icon = QIcon(os.path.dirname(__file__) + "/icon.png")
        self.searchAction = QAction(icon, "Search Layers", self.iface.mainWindow())
        self.searchAction.triggered.connect(self.showSearchDialog)
        self.iface.addToolBarIcon(self.searchAction)
        self.iface.addPluginToMenu("Search Layers", self.searchAction)

        # Help
        icon = QIcon(os.path.dirname(__file__) + '/help.png')
        self.helpAction = QAction(icon, "Help", self.iface.mainWindow())
        self.helpAction.triggered.connect(self.help)
        self.iface.addPluginToMenu('Search Layers', self.helpAction)

    def unload(self):
        self.iface.removePluginMenu('Search Layers', self.searchAction)
        self.iface.removePluginMenu('Search Layers', self.helpAction)
        self.iface.removeToolBarIcon(self.searchAction)
    
    def showSearchDialog(self):
        if self.searchDialog is None:
            # All the work is done in the LayerSearchDialog
            self.searchDialog = LayerSearchDialog(self.iface, self.iface.mainWindow())
        self.searchDialog.show()
        
    def help(self):
        '''Display a help page'''
        url = QUrl.fromLocalFile(os.path.dirname(__file__) + "/index.html").toString()
        webbrowser.open(url, new=2)
        