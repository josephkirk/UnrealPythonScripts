#!/usr/bin/python3
#import ueqt
import unreal_engine as ue
import os
from re import compile, match
from functools import partial
import sys
#from .. import unreal_libs as ul
from PySide2 import QtCore, QtGui, QtWidgets

# Event Process
import unreal.QWidgets as uQtWidgets
# app = QtWidgets.QApplication(sys.argv)

# def ticker_loop(delta_time):
#     app.processEvents()
#     return True

# ticker = ue.add_ticker(ticker_loop)



class MainUI(uQtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(parent = uQtWidgets.get_main_window())
        self._exportFolder = "D:/temp"

        grp = QtWidgets.QGroupBox("Export Directory: ")
        layout = QtWidgets.QVBoxLayout()
        exportDirLayout = QtWidgets.QHBoxLayout()
        self.dirPathEdit = QtWidgets.QLineEdit(self._exportFolder)
        browsePathButton = QtWidgets.QPushButton()
        browsePathButton.clicked.connect(self.changeRootPath)
        exportDirLayout.addWidget( self.dirPathEdit)
        exportDirLayout.addWidget( browsePathButton)
        grp.setLayout(exportDirLayout)
        layout.addWidget(grp)


        button = QtWidgets.QPushButton("Export All")
        button.clicked.connect(self.exportAll)
        layout.addWidget(button)

        button = QtWidgets.QPushButton("Export Selected")
        button.clicked.connect(self.exportSelected)
        layout.addWidget(button)

        layout.addWidget(QtWidgets.QLabel("Folders Contain Static Meshes:"))
        self.listView = QtWidgets.QListWidget()
        rootDir = ue.get_content_dir()
        data = self.getStaticFolderMeshData(rootDir)
        for folder, meshes in data:
            item = QtWidgets.QListWidgetItem(os.path.relpath(folder, rootDir))
            item.setData(QtCore.Qt.ItemDataRole.UserRole, meshes)
            self.listView.addItem(item)
        self.listView.itemDoubleClicked.connect(self.exportFolder)
        self.listView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        layout.addWidget(self.listView)

        self.setLayout(layout)
        #print("Open")

    def getStaticFolderMeshData(self, rootDir):
        matchType = compile(r'\.uasset\Z')
        allstaticmeshes = ue.get_assets_by_class("StaticMesh")
        uassetfolders = ((root,files) for root, subdirs, files in os.walk(rootDir)
            if any(matchType.search(file) for file in files))
        filterstaticmeshfolder = ((folder, list(
                staticmesh for staticmesh in allstaticmeshes
                if any(match("^{}".format(staticmesh.get_name()), ufile) for ufile in ufiles )))
            for folder, ufiles in uassetfolders)
        return ((folder, files) for folder, files in filterstaticmeshfolder if files)

    def changeRootPath(self):
        exportdir = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose Export Folder", self._exportFolder)
        if exportdir:
            self._exportFolder = exportdir
            self.dirPathEdit.setText(exportdir)

    def exportAll(self):
        self.export(ue.get_assets_by_class("StaticMesh"), self._exportFolder)

    def exportSelected(self):
        exportObs = []
        for item in self.listView.selectedItems():
            exportObs.extend(item.data(QtCore.Qt.ItemDataRole.UserRole))
        print(exportObs)
        self.export(exportObs, self._exportFolder)

    def exportFolder(self, ListItem):
        exportMeshes = ListItem.data(QtCore.Qt.ItemDataRole.UserRole)
        self.export(exportMeshes, self._exportFolder)

    def export(self, uobjects, exportdir):
        ue.export_assets(uobjects, exportdir)
        msg = "Export {} objects to {}".format(len(uobjects), exportdir)
        QtWidgets.QMessageBox.information(self, "Export Infos", msg)
        #print(msg)

widget = MainUI()
widget.setGeometry(200,200,400, 600)
widget.setWindowTitle("Export Static Meshes")
widget.show()