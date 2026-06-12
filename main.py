import sys
from PySide6.QtWidgets import QApplication

from main_window import Mainwindow
from display import Display
from PySide6.QtGui import QIcon
from variaveis import WINDOW_ICON_PATH
from info import Info
from styles import setupTheme
from botoes import ButtonsGrid


if __name__ == "__main__":
    app = QApplication(sys.argv)
    setupTheme(app)
    window = Mainwindow()

    # Define o ícone da janela
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info("2.0 ^ 10.0 = 1024")
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid de Botões
    grade_botoes = ButtonsGrid()
    window.vLayout.addLayout(grade_botoes)

    window.show()
    app.exec()
