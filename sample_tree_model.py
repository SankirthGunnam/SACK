import sys
from PyQt5.QtWidgets import QApplication, QTreeView, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QModelIndex, QAbstractItemModel

class TreeModel(QAbstractItemModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, parent=QModelIndex()):
        if not parent.isValid():
            return len(self._data)
        else:
            parent_item = parent.data()
            return len(self._data.get(parent_item, []))

    def columnCount(self, parent=QModelIndex()):
        return 1  # We will have only one column for this example

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if index.isValid():
                item = self.itemFromIndex(index)
                return item
        return None

    def itemFromIndex(self, index):
        if not index.isValid():
            return None
        item = self._data
        for i in range(index.row() + 1):
            item = item[list(item.keys())[index.row()]]
        return list(item.keys())[index.row()]

    def index(self, row, column, parent=QModelIndex()):
        if not parent.isValid():
            return self.createIndex(row, column)
        else:
            parent_item = self.itemFromIndex(parent)
            if parent_item in self._data:
                child_items = self._data[parent_item]
                if row < len(child_items):
                    return self.createIndex(row, column, child_items[row])
        return QModelIndex()

    def parent(self, index):
        if not index.isValid() or index.parent().isValid():
            return QModelIndex()

        child_item = self.itemFromIndex(index)
        for key, value in self._data.items():
            if child_item in value:
                row = value.index(child_item)
                return self.createIndex(row, 0, key)
        return QModelIndex()

class TreeViewExample(QWidget):
    def __init__(self):
        super().__init__()

        # Sample dictionary representing the hierarchical data
        self.data = {
            "Parent 1": ["Child 1-1", "Child 1-2"],
            "Parent 2": ["Child 2-1", "Child 2-2", "Child 2-3"],
            "Parent 3": []
        }

        # Create the tree view and set the model
        self.tree_view = QTreeView()
        self.model = TreeModel(self.data)
        self.tree_view.setModel(self.model)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.tree_view)
        
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TreeViewExample()
    window.setWindowTitle("QTreeView with Dictionary Example")
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec_())
