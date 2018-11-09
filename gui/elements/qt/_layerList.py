from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea


class QtLayerList(QScrollArea):
    def __init__(self):
        super().__init__()

        self.setWidgetResizable(True)
        #self.setFixedWidth(315)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scrollWidget = QWidget()
        self.setWidget(scrollWidget)
        self.layersLayout = QVBoxLayout(scrollWidget)
        self.layersLayout.addStretch(1)

    def insert(self, index, layer):
        """Inserts a layer widget at a specific index
        """
        if layer._qt is not None:
            self.layersLayout.insertWidget(index, layer._qt)

    def remove(self, layer):
        """Removes a layer widget
        """
        if layer._qt is not None:
            self.layersLayout.removeWidget(layer._qt)
            layer._qt.deleteLater()
            layer._qt = None

    def reorder(self, layerList):
        """Reorders list of layer widgets by looping through all
        widgets in list sequentially removing them and inserting
        them into the correct place in final list.
        """
        for i in range(len(layerList)):
            layer = layerList[i]
            if layer._qt is not None:
                self.layersLayout.removeWidget(layer._qt)
                self.layersLayout.insertWidget(i,layer._qt)
