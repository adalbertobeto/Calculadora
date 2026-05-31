import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
)

from main_window import Mainwindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()

    txt = QLabel("O meu TEXTO")
    txt.setStyleSheet("font-size: 150px;")
    window.v_layout.addWidget(txt)
    window.adjustFixedSize()

    window.show()
    app.exec()
