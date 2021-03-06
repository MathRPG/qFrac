import logging

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTableWidgetItem

from gui.ui_symbol_configuration_window import Ui_SymbolConfigurationWindow


class SymbolConfigurationWindow(QtWidgets.QWidget, Ui_SymbolConfigurationWindow):
    # added = QtCore.pyqtSignal(str, str)
    # removed = QtCore.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    @QtCore.pyqtSlot(dict)
    def display_symbol_dict(self, symbol_dict=None):
        symbol_dict = symbol_dict or {}

        self.symbol_table_widget.setRowCount(len(symbol_dict))

        for i, (symbol, value) in enumerate(symbol_dict.items()):
            value = repr(value)
            logging.info(f'[{i}] Token {symbol} is binded to expression {value}')
            self.symbol_table_widget.setItem(i, 0, QTableWidgetItem(symbol))
            self.symbol_table_widget.setItem(i, 1, QTableWidgetItem(value))
