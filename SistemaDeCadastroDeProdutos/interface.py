# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JanelaPrincipal(object):
    def setupUi(self, JanelaPrincipal):
        JanelaPrincipal.setObjectName("JanelaPrincipal")
        JanelaPrincipal.resize(572, 585)
        JanelaPrincipal.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.centralwidget = QtWidgets.QWidget(JanelaPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.lbTitulo = QtWidgets.QLabel(self.centralwidget)
        self.lbTitulo.setGeometry(QtCore.QRect(130, 30, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbTitulo.setFont(font)
        self.lbTitulo.setObjectName("lbTitulo")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 120, 491, 154))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.LayoutProdutos = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.LayoutProdutos.setContentsMargins(0, 0, 0, 0)
        self.LayoutProdutos.setHorizontalSpacing(6)
        self.LayoutProdutos.setVerticalSpacing(20)
        self.LayoutProdutos.setObjectName("LayoutProdutos")
        self.lbCodigo = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lbCodigo.setFont(font)
        self.lbCodigo.setObjectName("lbCodigo")
        self.LayoutProdutos.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbCodigo)
        self.inputCodigo = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.inputCodigo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputCodigo.setObjectName("inputCodigo")
        self.LayoutProdutos.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.inputCodigo)
        self.lbNome = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lbNome.setFont(font)
        self.lbNome.setObjectName("lbNome")
        self.LayoutProdutos.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbNome)
        self.inputNome = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.inputNome.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputNome.setObjectName("inputNome")
        self.LayoutProdutos.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.inputNome)
        self.lbPreco = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lbPreco.setFont(font)
        self.lbPreco.setObjectName("lbPreco")
        self.LayoutProdutos.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbPreco)
        self.inputPreco = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.inputPreco.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputPreco.setObjectName("inputPreco")
        self.LayoutProdutos.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.inputPreco)
        self.lbCategorias = QtWidgets.QLabel(self.centralwidget)
        self.lbCategorias.setGeometry(QtCore.QRect(210, 300, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lbCategorias.setFont(font)
        self.lbCategorias.setObjectName("lbCategorias")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(370, 290, 131, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutRadios = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayoutRadios.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutRadios.setObjectName("verticalLayoutRadios")
        self.rdbAlimentos = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rdbAlimentos.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rdbAlimentos.setFont(font)
        self.rdbAlimentos.setObjectName("rdbAlimentos")
        self.verticalLayoutRadios.addWidget(self.rdbAlimentos)
        self.rdbEletronicos = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rdbEletronicos.setFont(font)
        self.rdbEletronicos.setObjectName("rdbEletronicos")
        self.verticalLayoutRadios.addWidget(self.rdbEletronicos)
        self.rdbInformatica = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rdbInformatica.setFont(font)
        self.rdbInformatica.setObjectName("rdbInformatica")
        self.verticalLayoutRadios.addWidget(self.rdbInformatica)
        self.btnCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadastrar.setGeometry(QtCore.QRect(220, 470, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnCadastrar.setFont(font)
        self.btnCadastrar.setStyleSheet("background-color: rgb(175, 255, 137);")
        self.btnCadastrar.setObjectName("btnCadastrar")
        JanelaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(JanelaPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 572, 21))
        self.menubar.setObjectName("menubar")
        self.menuCadastro = QtWidgets.QMenu(self.menubar)
        self.menuCadastro.setObjectName("menuCadastro")
        JanelaPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(JanelaPrincipal)
        self.statusbar.setObjectName("statusbar")
        JanelaPrincipal.setStatusBar(self.statusbar)
        self.actionCadastrar = QtWidgets.QAction(JanelaPrincipal)
        self.actionCadastrar.setObjectName("actionCadastrar")
        self.actionVisualizar = QtWidgets.QAction(JanelaPrincipal)
        self.actionVisualizar.setObjectName("actionVisualizar")
        self.menuCadastro.addAction(self.actionCadastrar)
        self.menuCadastro.addAction(self.actionVisualizar)
        self.menubar.addAction(self.menuCadastro.menuAction())

        self.retranslateUi(JanelaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(JanelaPrincipal)

    def retranslateUi(self, JanelaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        JanelaPrincipal.setWindowTitle(_translate("JanelaPrincipal", "MainWindow"))
        self.lbTitulo.setText(_translate("JanelaPrincipal", "Cadastro de Produtos"))
        self.lbCodigo.setText(_translate("JanelaPrincipal", "Codigo:"))
        self.lbNome.setText(_translate("JanelaPrincipal", "Nome:"))
        self.lbPreco.setText(_translate("JanelaPrincipal", "Preço:"))
        self.lbCategorias.setText(_translate("JanelaPrincipal", "Categorias :"))
        self.rdbAlimentos.setText(_translate("JanelaPrincipal", "Alimentos"))
        self.rdbEletronicos.setText(_translate("JanelaPrincipal", "Eletronicos"))
        self.rdbInformatica.setText(_translate("JanelaPrincipal", "Informatica"))
        self.btnCadastrar.setText(_translate("JanelaPrincipal", "Cadastrar"))
        self.menuCadastro.setTitle(_translate("JanelaPrincipal", "Menu"))
        self.actionCadastrar.setText(_translate("JanelaPrincipal", "Cadastrar"))
        self.actionVisualizar.setText(_translate("JanelaPrincipal", "Visualizar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JanelaPrincipal = QtWidgets.QMainWindow()
    ui = Ui_JanelaPrincipal()
    ui.setupUi(JanelaPrincipal)
    JanelaPrincipal.show()
    sys.exit(app.exec_())
