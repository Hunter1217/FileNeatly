from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QMainWindow, QTreeWidget, QTreeWidgetItem, QWidget, QVBoxLayout, QInputDialog, QLineEdit, QPushButton
from pathlib import Path
from collections import deque
import services.get_files as get_files
import random

class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("FileNeatly")
        self.resize(900, 700)
        central = QWidget(self)
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        self.tree = QTreeWidget(central)

        layout.addWidget(self.tree)

        self.tree.setColumnCount(1)
        self.tree.setHeaderLabels(["Name"])
        self.pop_tree()

        self.btn = QPushButton('Change Directory', self)
        self.btn.clicked.connect(self.get_input)
        layout.addWidget(self.btn)

        self.text_edit = QLineEdit(self)
        layout.addWidget(self.text_edit)
        self.get_input()

    def get_input(self):
        text, ok = QInputDialog().getText(self, "QInputDialog().getText()",
                                            "Command: ", QLineEdit.Normal)
        
        if ok and text:
            self.text_edit.setText(text)

    def pop_branches(self, directory: Path, parent_item: QTreeWidgetItem):

        directory = Path(directory)


        try:
            sub_dirs, sub_files = get_files.get_sub_dirs(directory)

            for sub_dir in sub_dirs:
                sub_dir = Path(sub_dir)
                dir_item = QTreeWidgetItem([sub_dir.name, "Folder"])
                parent_item.addChild(dir_item)
                
                self.pop_branches(sub_dir, dir_item)


            for f in sub_files:
                f = Path(f)
                file_item = QTreeWidgetItem([f.name])
                dir_item.addChild(file_item)

        except Exception as e:
            print("Exception: ", e)
        
    def pop_tree(self):
        self.tree.clear()

        # current_dir = Path.home() / "OneDrive"
        current_dir = Path.home()
        root = QTreeWidgetItem([current_dir.name, "Folder"])
        self.tree.addTopLevelItem(root)

        self.pop_branches(current_dir, root)

        root.setExpanded(True)

# key = directory in or other directorys
# value = files or directorys inside that one
