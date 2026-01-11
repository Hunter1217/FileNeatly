from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QMainWindow, QTreeWidget, QTreeWidgetItem, QWidget, QVBoxLayout
from pathlib import Path
import services.get_files as get_files
import random

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FileNeatly")
        self.resize(900, 600)

        central = QWidget(self)
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        self.tree = QTreeWidget(central)

        layout.addWidget(self.tree)

        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(["Name", "Type"])
        self.pop_tree()
        # self.tree.show()
        
    #     self.layout = QtWidgets.QVBoxLayout(self)
    #     self.layout.addWidget(self.text)
    #     self.layout.addWidget(self.button)

    #     self.button.clicked.connect(self.magic)

    # @QtCore.Slot()
    # def magic(self):
    #     self.text.setText(random.choice(self.hello))

    def pop_tree(self):
        self.tree.clear()

        current_dir = get_files.get_home_dir()
        root = QTreeWidgetItem([current_dir.name])
        self.tree.addTopLevelItem(root)

        sub_dirs, _ = get_files.get_sub_dirs(current_dir)
        for each_dir in sub_dirs:
            dir_item = QTreeWidgetItem([each_dir.name, "Folder"])
            root.addChild(dir_item)

            _, new_files = get_files.get_sub_dirs(each_dir)
            for f in new_files:
                ext = f.suffix.upper().lstrip(".")
                file_item = QTreeWidgetItem([f.name, ext])
                dir_item.addChild(file_item)
        
        root.setExpanded(True)
        
# key = directory in or other directorys
# value = files or directorys inside that one
