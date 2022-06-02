# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'continued_fraction_calculator_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ContinuedFractionCalculatorMainWindow(object):
    def setupUi(self, ContinuedFractionCalculatorMainWindow):
        ContinuedFractionCalculatorMainWindow.setObjectName("ContinuedFractionCalculatorMainWindow")
        ContinuedFractionCalculatorMainWindow.resize(650, 313)
        font = QtGui.QFont()
        font.setPointSize(10)
        ContinuedFractionCalculatorMainWindow.setFont(font)
        ContinuedFractionCalculatorMainWindow.setWindowTitle("Continued Fraction Calculator")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(ContinuedFractionCalculatorMainWindow)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(ContinuedFractionCalculatorMainWindow)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.line_2 = QtWidgets.QFrame(ContinuedFractionCalculatorMainWindow)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(ContinuedFractionCalculatorMainWindow)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.expression_line_edit = QtWidgets.QLineEdit(ContinuedFractionCalculatorMainWindow)
        self.expression_line_edit.setObjectName("expression_line_edit")
        self.horizontalLayout_4.addWidget(self.expression_line_edit)
        self.expression_configure_tool_button = QtWidgets.QToolButton(ContinuedFractionCalculatorMainWindow)
        self.expression_configure_tool_button.setToolTip("Configure Expression Parser")
        self.expression_configure_tool_button.setToolTipDuration(-1)
        self.expression_configure_tool_button.setObjectName("expression_configure_tool_button")
        self.horizontalLayout_4.addWidget(self.expression_configure_tool_button)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_2 = QtWidgets.QLabel(ContinuedFractionCalculatorMainWindow)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.depth_slider = QtWidgets.QSlider(ContinuedFractionCalculatorMainWindow)
        self.depth_slider.setMaximum(40)
        self.depth_slider.setProperty("value", 5)
        self.depth_slider.setOrientation(QtCore.Qt.Horizontal)
        self.depth_slider.setInvertedAppearance(False)
        self.depth_slider.setInvertedControls(False)
        self.depth_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.depth_slider.setTickInterval(5)
        self.depth_slider.setObjectName("depth_slider")
        self.horizontalLayout_3.addWidget(self.depth_slider)
        self.depth_spin_box = QtWidgets.QSpinBox(ContinuedFractionCalculatorMainWindow)
        self.depth_spin_box.setMaximum(40)
        self.depth_spin_box.setProperty("value", 5)
        self.depth_spin_box.setObjectName("depth_spin_box")
        self.horizontalLayout_3.addWidget(self.depth_spin_box)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(ContinuedFractionCalculatorMainWindow)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.numerators_simple_radio_button = QtWidgets.QRadioButton(ContinuedFractionCalculatorMainWindow)
        self.numerators_simple_radio_button.setChecked(True)
        self.numerators_simple_radio_button.setObjectName("numerators_simple_radio_button")
        self.verticalLayout.addWidget(self.numerators_simple_radio_button)
        self.numerators_customized_radio_button = QtWidgets.QRadioButton(ContinuedFractionCalculatorMainWindow)
        self.numerators_customized_radio_button.setObjectName("numerators_customized_radio_button")
        self.verticalLayout.addWidget(self.numerators_customized_radio_button)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.numerator_customized_option_group = QtWidgets.QGroupBox(ContinuedFractionCalculatorMainWindow)
        self.numerator_customized_option_group.setEnabled(False)
        self.numerator_customized_option_group.setObjectName("numerator_customized_option_group")
        self.formLayout = QtWidgets.QFormLayout(self.numerator_customized_option_group)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.numerator_customized_option_group)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.numerators_sequence_line_edit = QtWidgets.QLineEdit(self.numerator_customized_option_group)
        self.numerators_sequence_line_edit.setObjectName("numerators_sequence_line_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.numerators_sequence_line_edit)
        self.label_5 = QtWidgets.QLabel(self.numerator_customized_option_group)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.numerators_cycle_line_edit = QtWidgets.QLineEdit(self.numerator_customized_option_group)
        self.numerators_cycle_line_edit.setObjectName("numerators_cycle_line_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.numerators_cycle_line_edit)
        self.horizontalLayout_2.addWidget(self.numerator_customized_option_group)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(ContinuedFractionCalculatorMainWindow)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.display_format_combo_box = QtWidgets.QComboBox(ContinuedFractionCalculatorMainWindow)
        self.display_format_combo_box.setObjectName("display_format_combo_box")
        self.display_format_combo_box.addItem("")
        self.display_format_combo_box.setItemText(0, "nested")
        self.display_format_combo_box.addItem("")
        self.display_format_combo_box.setItemText(1, "flat")
        self.horizontalLayout.addWidget(self.display_format_combo_box)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.calculate_push_button = QtWidgets.QPushButton(ContinuedFractionCalculatorMainWindow)
        self.calculate_push_button.setObjectName("calculate_push_button")
        self.verticalLayout_3.addWidget(self.calculate_push_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.line = QtWidgets.QFrame(ContinuedFractionCalculatorMainWindow)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_5.addWidget(self.line)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_8 = QtWidgets.QLabel(ContinuedFractionCalculatorMainWindow)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.result_render_area = QtWidgets.QLabel(ContinuedFractionCalculatorMainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_render_area.sizePolicy().hasHeightForWidth())
        self.result_render_area.setSizePolicy(sizePolicy)
        self.result_render_area.setFrameShape(QtWidgets.QFrame.Box)
        self.result_render_area.setFrameShadow(QtWidgets.QFrame.Plain)
        self.result_render_area.setAlignment(QtCore.Qt.AlignCenter)
        self.result_render_area.setObjectName("result_render_area")
        self.verticalLayout_4.addWidget(self.result_render_area)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.retranslateUi(ContinuedFractionCalculatorMainWindow)
        self.depth_slider.valueChanged['int'].connect(self.depth_spin_box.setValue)
        self.depth_spin_box.valueChanged['int'].connect(self.depth_slider.setValue)
        self.numerators_customized_radio_button.toggled['bool'].connect(self.numerator_customized_option_group.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(ContinuedFractionCalculatorMainWindow)

    def retranslateUi(self, ContinuedFractionCalculatorMainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_7.setText(_translate("ContinuedFractionCalculatorMainWindow", "Configurations"))
        self.label.setText(_translate("ContinuedFractionCalculatorMainWindow", "Expression"))
        self.expression_configure_tool_button.setText(_translate("ContinuedFractionCalculatorMainWindow", "..."))
        self.label_2.setText(_translate("ContinuedFractionCalculatorMainWindow", "Depth"))
        self.label_3.setText(_translate("ContinuedFractionCalculatorMainWindow", "Numerators"))
        self.numerators_simple_radio_button.setText(_translate("ContinuedFractionCalculatorMainWindow", "Simple"))
        self.numerators_customized_radio_button.setText(_translate("ContinuedFractionCalculatorMainWindow", "Customized"))
        self.label_4.setText(_translate("ContinuedFractionCalculatorMainWindow", "Sequence"))
        self.label_5.setText(_translate("ContinuedFractionCalculatorMainWindow", "Cycle"))
        self.label_6.setText(_translate("ContinuedFractionCalculatorMainWindow", "Display Format"))
        self.calculate_push_button.setText(_translate("ContinuedFractionCalculatorMainWindow", "Calculate"))
        self.label_8.setText(_translate("ContinuedFractionCalculatorMainWindow", "Result"))
        self.result_render_area.setText(_translate("ContinuedFractionCalculatorMainWindow", "Result Fraction will be rendered here"))
