from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QMainWindow, QTreeWidget, QTreeWidgetItem, QWidget, QVBoxLayout, QInputDialog, QLineEdit, QPushButton
from PySide6.QtCore import Qt
from pathlib import Path
import services.get_files as get_files
import random
import time

class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.tree.itemExpanded.connect(self.on_item_expanded)
        self.setup_tree()

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


    def setup_tree(self):
        self.pop_tree()

    def on_item_expanded(self, item):
        if item.childCount() == 0:
            self.populate_children(item)
            
    def populate_children(self, item):
        try:
            dir_path = item.data(0, Qt.UserRole)
            sub_dirs, sub_files = get_files.get_sub_dirs(dir_path)

            for sub_dir in sub_dirs:
                dir_item = QTreeWidgetItem([sub_dir.name, "Folder"])
                dir_item.setData(0, Qt.UserRole, sub_dir)
                dir_item.setChildIndicatorPolicy(QTreeWidgetItem.ShowIndicator)
                item.addChild(dir_item)

            for f in sub_files:
                file_item = QTreeWidgetItem([f.name])
                dir_item.addChild(file_item)

        except Exception as e:
            print("Exception: ", e)
        
    def pop_tree(self):
        start = time.perf_counter()
        self.tree.clear()

        current_dir = Path.home()
        root_item = QTreeWidgetItem([current_dir.name, "Folder"])
        root_item.setData(0, Qt.UserRole, current_dir)
        root_item.setChildIndicatorPolicy(QTreeWidgetItem.ShowIndicator)

        self.tree.addTopLevelItem(root_item)
        root_item.setExpanded(True)

        end = time.perf_counter()
        print(f"Elapsed time: {end - start}")


# key = directory in or other directorys
# value = files or directorys inside that one
