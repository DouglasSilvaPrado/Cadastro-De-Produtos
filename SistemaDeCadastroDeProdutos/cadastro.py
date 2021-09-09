from PyQt5 import uic, QtWidgets
from BancoDeDados.BaseCreate import*
from reportlab.pdfgen import canvas


class SistemaDeCadastro:
    def CadastrarPruduto(self):
        codigo = janela_principal.inputCodigo.text()
        nome = janela_principal.inputNome.text()
        preco = janela_principal.inputPreco.text().replace(',', '.')
        categoria = ""

        if janela_principal.rdbAlimentos.isChecked():
            categoria = "Alimentos"
        elif janela_principal.rdbEletronicos.isChecked():
            categoria = "Eletronicos"
        elif janela_principal.rdbInformatica.isChecked():
            categoria = "Informatica"
        else:
            print('Houve um erro ao selecionar a Categoria')

        inseridados(codigo, nome, preco, categoria)

        codigo = janela_principal.inputCodigo.setText("")
        nome = janela_principal.inputNome.setText("")
        preco = janela_principal.inputPreco.setText("")

    def MenuVisualizarDados(self):
        janela_visualizar.show()
        janela_principal.close()

        visualizarDados()
        dados_lidos = visualizarDados()
        
        janela_visualizar.tableWidget.setRowCount(len(dados_lidos))
        janela_visualizar.tableWidget.setColumnCount(5)

        for linha in range(0, len(dados_lidos)):
            for coluna in range(0, 5):
                janela_visualizar.tableWidget.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados_lidos[linha][coluna])))

    def MenuCadastrarDados(self):
        janela_principal.show()
        janela_visualizar.close()

    def GerarPDF(self):
        visualizarDados()
        dados_lidos = visualizarDados()
        y = 0
        pdf = canvas.Canvas("CadastroDeProdutos.pdf")
        pdf.setFont("Times-Bold", 25)
        pdf.drawString(100,800, "Produtos Cadastrados:")
        pdf.setFont("Times-Bold", 18)

        pdf.drawString(10,750, "ID")
        pdf.drawString(80,750, "CODIGO")
        pdf.drawString(200,750, "NOME")
        pdf.drawString(350,750, "PREÇO")
        pdf.drawString(450,750, "CATEGORIA")

        for i in range(0, len(dados_lidos)):
            y = y + 50
            pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
            pdf.drawString(80,750 - y, str(dados_lidos[i][1]))
            pdf.drawString(200,750 - y, str(dados_lidos[i][2]))
            pdf.drawString(350,750 - y, str(dados_lidos[i][3]))
            pdf.drawString(450,750 - y, str(dados_lidos[i][4]))
        pdf.save()
        print('PDF Gerado')

    def ExcluirDado(self):
        banco = conectar_base()

        linha = janela_visualizar.tableWidget.currentRow()
        janela_visualizar.tableWidget.removeRow(linha)
        cursor = banco.cursor()      
        cursor.execute("SELECT id FROM produtos;")
        dados_lidos = cursor.fetchall()
        valor_id = dados_lidos[linha][0]
        cursor.execute("DELETE FROM produtos WHERE id="+ str(valor_id))
        banco.commit()

    def EditarDados(self):
        global numero_id

        banco = conectar_base()
        
        linha = janela_visualizar.tableWidget.currentRow()
        
        cursor = banco.cursor()      
        cursor.execute("SELECT id FROM produtos;")
        dados_lidos = cursor.fetchall()
        valor_id = dados_lidos[linha][0]
        cursor.execute("SELECT * FROM produtos WHERE id="+ str(valor_id))
        produto = cursor.fetchall()
        janela_editar_dados.inputID.setText(str(produto[0][0]))
        janela_editar_dados.inputCodigo.setText(str(produto[0][1]))
        janela_editar_dados.inputNome.setText(str(produto[0][2]))
        janela_editar_dados.inputPreco.setText(str(produto[0][3]))
        janela_editar_dados.inputCategoria.setText(str(produto[0][4]))
        numero_id = valor_id

        janela_editar_dados.show()

    def SalvarDadosEditados(self):
        global numero_id
        banco = conectar_base()


        codigo = janela_editar_dados.inputCodigo.text()
        nome = janela_editar_dados.inputNome.text()
        preco= janela_editar_dados.inputPreco.text()
        categoria = janela_editar_dados.inputCategoria.text()
        # print(f'Codigo: {codigo} Nome: {nome} Preço: {preco} Categoria: {categoria}')
        
        cursor = banco.cursor()
        cursor.execute("UPDATE produtos SET codigo = '{}', nome = '{}', preço = '{}', categoria ='{}' WHERE id = {}".format(codigo,nome,preco,categoria,numero_id))
        banco.commit()

        janela_editar_dados.close()
        janela_visualizar.close()
        cadastro.MenuVisualizarDados()


if __name__ == "__main__":
    numero_id = 0

    criarDatabase(nome_database='cadastrodeprodutos')
    criartable(nome_database='cadastrodeprodutos', nome_table='produtos')

    cadastro = SistemaDeCadastro()

    app = QtWidgets.QApplication([])
    
    janela_principal = uic.loadUi('interfaces/interface.ui')
    janela_visualizar = uic.loadUi('interfaces/VisualizarDados.ui')
    janela_editar_dados = uic.loadUi('interfaces/EditarDados.ui')

    janela_principal.btnCadastrar.clicked.connect(cadastro.CadastrarPruduto)
    janela_principal.actionVisualizar.triggered.connect(cadastro.MenuVisualizarDados)


    janela_visualizar.actionCadastrar.triggered.connect(cadastro.MenuCadastrarDados)
    janela_visualizar.btnPDF.clicked.connect(cadastro.GerarPDF)
    janela_visualizar.btnExcluir.clicked.connect(cadastro.ExcluirDado)
    janela_visualizar.btnEditar.clicked.connect(cadastro.EditarDados)


    janela_editar_dados.btnSalvar.clicked.connect(cadastro.SalvarDadosEditados)


    janela_principal.show()
    app.exec()