import sys
from PySide6.QtWidgets import QApplication

from main_window import Mainwindow
from display import Display
from PySide6.QtGui import QIcon
from variaveis import WINDOW_ICON_PATH


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()

    # Define o ícone da janela
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Display
    display = Display()
    window.addToVLayout(display)

    window.show()
    app.exec()
