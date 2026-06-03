import sys
from PySide6.QtWidgets import QApplication, QLabel

from main_window import Mainwindow
from PySide6.QtGui import QIcon
from variaveis import WINDOW_ICON_PATH


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()

    # Define o ícone da janela
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    txt = QLabel("O meu TEXTO")
    txt.setStyleSheet("font-size: 150px;")
    window.addWidgetToVLayout(txt)
    window.adjustFixedSize()

    window.show()
    app.exec()
