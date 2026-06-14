from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variaveis import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty
from display import Display


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        self.setCheckable(True)


class ButtonsGrid(QGridLayout):
    def __init__(self, display: Display, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.display = display
        self._gridMask = [
            ["C", "<", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["", "0", ".", "="],
        ]

        self._makeGrid()

    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, button_txt in enumerate(row):
                botao = Button(button_txt)

                if not isNumOrDot(button_txt) and not isEmpty(button_txt):
                    botao.setProperty("cssClass", "specialButton")
                    botao.style().unpolish(botao)
                    botao.style().polish(botao)

                self.addWidget(botao, i, j)

                botaoSlot = self._makeButtonDisplaySlot(
                    self._insertButtonTextToDisplay, botao
                )
                botao.clicked.connect(botaoSlot)

    def _makeButtonDisplaySlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)

        return realSlot

    def _insertButtonTextToDisplay(self, botao):
        botao_texto = botao.text()
        self.display.insert(botao_texto)
