# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'expression_evaluation_configuration_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExpressionEvaluationConfigurationWindow(object):
    def setupUi(self, ExpressionEvaluationConfigurationWindow):
        ExpressionEvaluationConfigurationWindow.setObjectName("ExpressionEvaluationConfigurationWindow")
        ExpressionEvaluationConfigurationWindow.resize(400, 300)
        ExpressionEvaluationConfigurationWindow.setWindowTitle("Configure Expression Evaluation")
        self.verticalLayout = QtWidgets.QVBoxLayout(ExpressionEvaluationConfigurationWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.token_table_widget = QtWidgets.QTableWidget(ExpressionEvaluationConfigurationWindow)
        self.token_table_widget.setObjectName("token_table_widget")
        self.token_table_widget.setColumnCount(2)
        self.token_table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.token_table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.token_table_widget.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.token_table_widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_push_button = QtWidgets.QPushButton(ExpressionEvaluationConfigurationWindow)
        self.add_push_button.setObjectName("add_push_button")
        self.horizontalLayout.addWidget(self.add_push_button)
        self.remove_push_button = QtWidgets.QPushButton(ExpressionEvaluationConfigurationWindow)
        self.remove_push_button.setObjectName("remove_push_button")
        self.horizontalLayout.addWidget(self.remove_push_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ExpressionEvaluationConfigurationWindow)
        QtCore.QMetaObject.connectSlotsByName(ExpressionEvaluationConfigurationWindow)

    def retranslateUi(self, ExpressionEvaluationConfigurationWindow):
        _translate = QtCore.QCoreApplication.translate
        item = self.token_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("ExpressionEvaluationConfigurationWindow", "Token"))
        item = self.token_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("ExpressionEvaluationConfigurationWindow", "Expression"))
        self.add_push_button.setText(_translate("ExpressionEvaluationConfigurationWindow", "Add"))
        self.remove_push_button.setText(_translate("ExpressionEvaluationConfigurationWindow", "Remove"))