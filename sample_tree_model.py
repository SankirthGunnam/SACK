from PySide6.QtWidgets import QApplication, QTreeView
from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt

class TreeModel(QAbstractItemModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.data_dict = data
        self.keys = list(self.data_dict.keys())
    
    def index(self, row, column, parent=QModelIndex()):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()
        
        if not parent.isValid():
            key = self.keys[row]
            return self.createIndex(row, column, key)
        
        parent_key = parent.internalPointer()
        parent_value = self.data_dict.get(parent_key, {})
        if isinstance(parent_value, dict):
            child_keys = list(parent_value.keys())
            return self.createIndex(row, column, child_keys[row])
        
        return QModelIndex()
    
    def parent(self, index):
        if not index.isValid():
            return QModelIndex()
        
        child_key = index.internalPointer()
        for key, value in self.data_dict.items():
            if isinstance(value, dict) and child_key in value:
                return self.createIndex(self.keys.index(key), 0, key)
        
        return QModelIndex()
    
    def rowCount(self, parent=QModelIndex()):
        if not parent.isValid():
            return len(self.keys)
        
        parent_key = parent.internalPointer()
        parent_value = self.data_dict.get(parent_key, {})
        return len(parent_value) if isinstance(parent_value, dict) else 0
    
    def columnCount(self, parent=QModelIndex()):
        return 2  # Key and Value
    
    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or role != Qt.DisplayRole:
            return None
        
        key = index.internalPointer()
        if index.column() == 0:
            return key
        elif index.column() == 1:
            value = self.data_dict.get(key, "")
            return str(value) if not isinstance(value, dict) else ""
        return None
    
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return "Key" if section == 0 else "Value"
        return None

if __name__ == "__main__":
    import sys

    data = {
        "Person": {
            "Name": "John",
            "Age": 30,
            "Address": {
                "Street": "123 Main St",
                "City": "New York"
            }
        },
        "Job": {
            "Title": "Software Engineer",
            "Company": "Tech Corp"
        }
    }
    
    app = QApplication(sys.argv)
    tree_view = QTreeView()
    model = TreeModel(data)
    tree_view.setModel(model)
    tree_view.setWindowTitle("Dictionary Tree View")
    tree_view.resize(400, 300)
    tree_view.show()
    sys.exit(app.exec())
