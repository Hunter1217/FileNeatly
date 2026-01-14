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

    
    def pop_branches(self, paths, parent_item: QTreeWidgetItem):

        print("Path:", paths)
        try:
            for path in paths:
                path = Path(path)
                sub_dirs, sub_files = get_files.get_sub_dirs(path)

                for sub_dir in sub_dirs:
                    dir_item = QTreeWidgetItem([sub_dir.name, "Folder"])
                    parent_item.addChild(dir_item)
                    sub_dir = Path(sub_dir)
                    self.pop_branches(sub_dir, dir_item)

                for f in sub_files:
                    file_item = QTreeWidgetItem([f.name])
                    dir_item.addChild(file_item)
        except Exception as e:
            print("Exception: ", e)
        

    def pop_tree(self):
        self.tree.clear()

        current_dir = Path.home() / "OneDrive"

        # current_dir = Path("C:\Users\hunte\OneDrive")
        # current_dir = get_files.get_home_dir()

        root = QTreeWidgetItem([current_dir.name])
        self.tree.addTopLevelItem(root)

        current_items = []

        sub_dirs, _ = get_files.get_sub_dirs(current_dir)

        for each_dir in sub_dirs:
            print(f"Current Directory: {each_dir.name}")
    
            dir_item = QTreeWidgetItem([each_dir.name, "Folder"])
            root.addChild(dir_item)

            new_sub_dirs, new_files = get_files.get_sub_dirs(each_dir)

            if new_sub_dirs:
                self.pop_branches(new_sub_dirs, root)

            for f in new_files:
                file_item = QTreeWidgetItem([f.name])
                dir_item.addChild(file_item)
        
        root.setExpanded(True)

        
# key = directory in or other directorys
# value = files or directorys inside that one
