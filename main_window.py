from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class Mainwindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # configurando o Layout Básico
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        # Título da Janela
        self.setWindowTitle("Calculadora")

    def adjustFixedSize(self):
        # ultima cois a ser feita
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
