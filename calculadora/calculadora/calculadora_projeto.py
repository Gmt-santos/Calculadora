from PySide6.QtWidgets import (QMainWindow,QLayout,QVBoxLayout,QLabel,QApplication,QDialog,QWidget,QGridLayout,
                               QLineEdit,QPushButton,QGroupBox)
import sys
from PySide6.QtGui import QKeyEvent,QIcon,QWindow
from PySide6.QtCore import Slot
app = QApplication(sys.argv)  
class main(QWidget):
    
    def __init__(self):
        super().__init__()
        self.operacao_ativa=False
        main_layout=QGridLayout()
        button_layout= QGridLayout()
        design_button="font-size:30px;color:white"
        design_button_equal="font-size:40px;background-color:blue;color:black"
        design_button_focus="font-size:25px;background-color:#e6e6e6;color:black"

        self.lista_historico_espaco=[]
        self.historico_espaco=QLabel("")
        self.historico_espaco.setStyleSheet("font-size:20px;color:gray")
        

        self.lista_campo_atual=[]
        self.campo_atual_espaco=QLineEdit(*self.lista_campo_atual)
        self.campo_atual_espaco.setReadOnly(True)
        self.campo_atual_espaco.setStyleSheet("font-size:40px;color:white")

        '''''
        Criação dos botões
        '''''
        self.button_add=QPushButton()
        self.button_add.setText("+")
        self.button_add.setStyleSheet(design_button)
        self.button_add.clicked.connect(self.verificar_operacao_ativa(self.inicio_adicao,self.fim_adicao))
       

        self.button_sub=QPushButton()
        self.button_sub.setText("-")
        self.button_sub.setStyleSheet(design_button)
        self.button_sub.clicked.connect(self.verificar_operacao_ativa(self.inicio_sub,self.fim_sub))

        self.button_x=QPushButton()
        self.button_x.setText("x")
        self.button_x.setStyleSheet(design_button)
        self.button_x.clicked.connect(self.verificar_operacao_ativa(self.inicio_x,self.fim_x))
      
        self.button_div=QPushButton()
        self.button_div.setText("%")
        self.button_div.setStyleSheet(design_button)
        self.button_div.clicked.connect(self.verificar_operacao_ativa(self.inicio_div,self.fim_div))


        self.button_eq=QPushButton()
        self.button_eq.setText("=")
        self.button_eq.setStyleSheet(design_button_equal)
        self.button_eq.clicked.connect(self.verificar_operacao_especifica())

        self.button_1=QPushButton()
        self.button_1.setText("1")
        self.button_1.setStyleSheet(design_button)
        self.button_1.clicked.connect(self.botao_pressionado("1"))

        self.button_2=QPushButton()
        self.button_2.setText("2")
        self.button_2.setStyleSheet(design_button)
        self.button_2.clicked.connect(self.botao_pressionado("2"))

        self.button_3=QPushButton()
        self.button_3.setText("3")
        self.button_3.setStyleSheet(design_button)
        self.button_3.clicked.connect(self.botao_pressionado("3"))

        self.button_4=QPushButton()
        self.button_4.setText("4")
        self.button_4.setStyleSheet(design_button)
        self.button_4.clicked.connect(self.botao_pressionado("4"))

        self.button_5=QPushButton()
        self.button_5.setText("5")
        self.button_5.setStyleSheet(design_button)
        self.button_5.clicked.connect(self.botao_pressionado("5"))

        self.button_6=QPushButton()
        self.button_6.setText("6")
        self.button_6.setStyleSheet(design_button)
        self.button_6.clicked.connect(self.botao_pressionado("6"))

        self.button_7=QPushButton()
        self.button_7.setText("7")
        self.button_7.setStyleSheet(design_button)
        self.button_7.clicked.connect(self.botao_pressionado("7"))

        self.button_8=QPushButton()
        self.button_8.setText("8")
        self.button_8.setStyleSheet(design_button)
        self.button_8.clicked.connect(self.botao_pressionado("8"))

        self.button_9=QPushButton()
        self.button_9.setText("9")
        self.button_9.setStyleSheet(design_button)
        self.button_9.clicked.connect(self.botao_pressionado("9"))

        self.button_0=QPushButton()
        self.button_0.setText("0")
        self.button_0.setStyleSheet(design_button)
        self.button_0.clicked.connect(self.botao_pressionado("0"))
      

        self.button_clear=QPushButton()
        self.button_clear.setText("C")
        self.button_clear.setStyleSheet(design_button_equal)
        self.button_clear.clicked.connect(self.clear())

        '''
        O botão "Focus" serve para o usuário clicar e conseguir focar na página da aplicação,
        de modo que permita digitar no teclado e o programa "ler" o que foi digitado
        '''
        self.button_focus=QPushButton()
        self.button_focus.setText("Focus")
        self.button_focus.setStyleSheet(design_button_focus)



        '''
        Criação do Grid de botões
        '''
        self.grid_botoes=QGroupBox()
        
        
        

        button_layout.addWidget(self.button_add,1,4)
        button_layout.addWidget(self.button_sub,2,4)
        button_layout.addWidget(self.button_x,3,4)
        button_layout.addWidget(self.button_div,4,4)
        button_layout.addWidget(self.button_eq,5,1,2,4)
        button_layout.addWidget(self.button_clear,4,1)
        button_layout.addWidget(self.button_focus,4,3)
        button_layout.addWidget(self.button_1,3,1)
        button_layout.addWidget(self.button_2,3,2)
        button_layout.addWidget(self.button_3,3,3)
        button_layout.addWidget(self.button_4,2,1)
        button_layout.addWidget(self.button_5,2,2)
        button_layout.addWidget(self.button_6,2,3)
        button_layout.addWidget(self.button_7,1,1)
        button_layout.addWidget(self.button_8,1,2)
        button_layout.addWidget(self.button_9,1,3)
        button_layout.addWidget(self.button_0,4,2)

        self.grid_botoes.setLayout(button_layout)

        '''
        Criação do layout
        '''
        main_layout.addWidget(self.historico_espaco)
        main_layout.addWidget(self.campo_atual_espaco)
        main_layout.addWidget(self.grid_botoes)
        
        self.setLayout(main_layout)
    '''
    Funções específicas
    '''
    def verificar_operacao_especifica(self):
        def inner():
            _text=self.historico_espaco.text()
            self.historico_espaco.setText("")
            
            if "+" in _text:
                if "=" in _text:
                    
                    _lista_dps_sinal=self.empacotar_lista_numeros_dps_sinal(_text)
                    _lista_entre_sinal=self.empacotar_lista_numeros_entre_sinais(_text)
                    _resultado=float(self.desempacotar_lista(_lista_dps_sinal)) + float(self.desempacotar_lista(self.empacotar_lista_numeros_entre_sinais(_text)))
                    self.historico_espaco.setText(self.desempacotar_lista(_lista_dps_sinal)+"+"+self.desempacotar_lista(_lista_entre_sinal)+"="+str(_resultado))
                    self.campo_atual_espaco.setText(str(_resultado))
                else:
                    _lista=self.empacotar_lista_numeros(_text)
                    _resultado=float(self.campo_atual_espaco.text())+float("".join(_lista))
                    self.historico_espaco.setText("".join(_lista)+"+"+self.campo_atual_espaco.text()+"=" + str(_resultado))
                    self.campo_atual_espaco.setText(str(_resultado))
                    
                    
                
               
            elif "-" in _text:
                if "=" in _text:
                   
                    _lista_dps_sinal=self.empacotar_lista_numeros_dps_sinal(_text)
                    _lista_entre_sinal=self.empacotar_lista_numeros_entre_sinais(_text)
                    _resultado=float(self.desempacotar_lista(_lista_dps_sinal)) - float(self.desempacotar_lista(self.empacotar_lista_numeros_entre_sinais(_text)))
                    self.historico_espaco.setText(self.desempacotar_lista(_lista_dps_sinal)+"-"+self.desempacotar_lista(_lista_entre_sinal)+"="+str(_resultado))
                    self.campo_atual_espaco.setText(str(_resultado))
                else:
                    _lista=self.empacotar_lista_numeros(_text)
                    _resultado=float("".join(_lista))-float(self.campo_atual_espaco.text())
                    self.historico_espaco.setText("".join(_lista)+"-"+self.campo_atual_espaco.text()+"=" + str(_resultado))
                self.button_eq.clicked.disconnect(self.verificar_operacao_especifica)
                self.campo_atual_espaco.setText(str(_resultado))
            elif "x" in _text:
                if "=" in _text:
                    
                    _lista_dps_sinal=self.empacotar_lista_numeros_dps_sinal(_text)
                    _lista_entre_sinal=self.empacotar_lista_numeros_entre_sinais(_text)
                    _resultado=float(self.desempacotar_lista(_lista_dps_sinal)) * float(self.desempacotar_lista(self.empacotar_lista_numeros_entre_sinais(_text)))
                    self.historico_espaco.setText(self.desempacotar_lista(_lista_dps_sinal)+"x"+self.desempacotar_lista(_lista_entre_sinal)+"="+str(_resultado))
                    self.campo_atual_espaco.setText(str(_resultado))
                else:
                    _lista=self.empacotar_lista_numeros(_text)
                    _resultado=float(self.campo_atual_espaco.text())*float("".join(_lista))
                    self.historico_espaco.setText("".join(_lista)+"x"+self.campo_atual_espaco.text()+"=" + str(_resultado))
                    self.campo_atual_espaco.setText(str(_resultado))

            elif "÷" in _text:
                if "=" in _text:
                   
                    _lista_dps_sinal=self.empacotar_lista_numeros_dps_sinal(_text)
                    _lista_entre_sinal=self.empacotar_lista_numeros_entre_sinais(_text)
                    _resultado=float(self.desempacotar_lista(_lista_dps_sinal)) / float(self.desempacotar_lista(self.empacotar_lista_numeros_entre_sinais(_text)))
                    self.historico_espaco.setText(self.desempacotar_lista(_lista_dps_sinal)+"÷"+self.desempacotar_lista(_lista_entre_sinal)+"="+str(_resultado))
                    self.campo_atual_espaco.setText(str(_resultado))
                else:
                    _lista=self.empacotar_lista_numeros(_text)
                    _resultado=float("".join(_lista))/float(self.campo_atual_espaco.text())
                    self.historico_espaco.setText("".join(_lista)+"÷"+self.campo_atual_espaco.text()+"=" + str(_resultado))
                self.button_eq.clicked.disconnect(self.verificar_operacao_especifica)
                self.campo_atual_espaco.setText(str(_resultado))


                
        
        return inner
    


    def inicio_adicao(self):
        if self.campo_atual_espaco.text():
            self.historico_espaco.setText(self.campo_atual_espaco.text()+"+")
            self.lista_campo_atual=[]
            self.campo_atual_espaco.setText("")
            self.operacao_ativa=True
            self.button_add.clicked.disconnect(self.inicio_adicao)
            self.button_add.clicked.connect(self.verificar_operacao_ativa(self.inicio_adicao,self.fim_adicao))

    
    def fim_adicao(self):
        self.lista_historico_espaco=[]
        self.lista_campo_atual=[]
        if "=" not in self.historico_espaco.text():
            self.lista_historico_espaco=self.empacotar_lista_numeros(self.historico_espaco.text())
            self.lista_historico_espaco="".join(self.lista_historico_espaco)
            _resultado=float(self.lista_historico_espaco) + float(self.campo_atual_espaco.text())
            _resultado = str(_resultado)
            self.historico_espaco.setText(_resultado+"+")
            self.button_add.clicked.disconnect(self.fim_adicao)
            self.button_add.clicked.connect(self.verificar_operacao_ativa(self.inicio_adicao,self.fim_adicao))
        else:
            
            self.historico_espaco.setText(self.campo_atual_espaco.text()+"+")


    def inicio_sub(self):
        self.lista_campo_atual=[]
        self.historico_espaco.setText(self.campo_atual_espaco.text()+"-")
        self.campo_atual_espaco.setText("")
        self.operacao_ativa =True
        self.button_sub.clicked.disconnect(self.inicio_sub)
        self.button_sub.clicked.connect(self.verificar_operacao_ativa(self.inicio_sub,self.fim_sub))

    def fim_sub(self):
       self.lista_campo_atual=[]
       if "=" not in self.historico_espaco.text():
            self.lista_historico_espaco=self.empacotar_lista_numeros(self.historico_espaco.text())
            self.lista_historico_espaco="".join(self.lista_historico_espaco)
            _resultado=float(self.lista_historico_espaco) - float(self.campo_atual_espaco.text())
            _resultado = str(_resultado)
            self.historico_espaco.setText(_resultado+"-")
            self.button_sub.clicked.disconnect(self.fim_sub)
            self.button_sub.clicked.connect(self.verificar_operacao_ativa(self.inicio_sub,self.fim_sub))
       else:
            
            self.historico_espaco.setText(self.campo_atual_espaco.text()+"-")

    def inicio_x(self):
        self.lista_campo_atual=[]
        self.historico_espaco.setText(self.campo_atual_espaco.text() + "x")
        self.campo_atual_espaco.setText("")
        
        self.operacao_ativa=True
        self.button_x.clicked.disconnect(self.inicio_x)
        self.button_x.clicked.connect(self.verificar_operacao_ativa(self.inicio_x,self.fim_x))
        
    def fim_x(self):
        self.lista_campo_atual=[]
        if "=" not in self.historico_espaco.text(): 
            self.lista_historico_espaco=self.empacotar_lista_numeros(self.historico_espaco.text())
            self.lista_historico_espaco="".join(self.lista_historico_espaco)
            _resultado=float(self.lista_historico_espaco) * float(self.campo_atual_espaco.text())
            _resultado = str(_resultado)
            self.historico_espaco.setText(_resultado+"x")
            self.button_x.clicked.disconnect(self.fim_x)
            self.button_x.clicked.connect(self.verificar_operacao_ativa(self.inicio_x,self.fim_x))
        else:
            self.historico_espaco.setText(self.campo_atual_espaco.text()+"x")

    def inicio_div(self):
        self.lista_campo_atual=[]
        self.historico_espaco.setText(self.campo_atual_espaco.text()+"÷")
        self.campo_atual_espaco.setText("")
        self.operacao_ativa =True
        self.button_div.clicked.disconnect(self.inicio_div)
        self.button_div.clicked.connect(self.verificar_operacao_ativa(self.inicio_div,self.fim_div))

    def fim_div(self):
       self.lista_campo_atual=[]
       if "=" not in self.historico_espaco.text():
            self.lista_historico_espaco=self.empacotar_lista_numeros(self.historico_espaco.text())
            self.lista_historico_espaco="".join(self.lista_historico_espaco)
            _resultado=float(self.lista_historico_espaco) / float(self.campo_atual_espaco.text())
            _resultado = str(_resultado)
            self.historico_espaco.setText(_resultado+"÷")
            self.button_div.clicked.disconnect(self.inicio_div)
            self.button_div.clicked.connect(self.verificar_operacao_ativa(self.inicio_div,self.fim_div))
       else:
            
            self.historico_espaco.setText(self.campo_atual_espaco.text()+"÷")
        

            
        
    
        
    

    
    '''
    Funções gerais
    '''

    def clear(self):
        def inner():
            
            self.lista_campo_atual=[]
            self.lista_historico_espaco=[]
            self.operacao_ativa=False
            self.campo_atual_espaco.setText("")
            self.historico_espaco.setText("")
            self.button_add.clicked.connect(self.verificar_operacao_ativa(self.inicio_adicao,self.fim_adicao))
            self.button_sub.clicked.connect(self.verificar_operacao_ativa(self.inicio_sub,self.fim_sub))
        return inner
   
    def verificar_operacao_ativa(self,inicio,fim):
        if self.operacao_ativa == False:
                return inicio
        elif self.operacao_ativa == True:
                return fim
      
    @Slot(str)
    def botao_pressionado(self,char):
       
        def inner():
            self.lista_campo_atual.append(char)
            self.campo_atual_espaco.setText(self.desempacotar_lista(self.lista_campo_atual))
        
        return inner
         
    def desempacotar_lista(self,lista):
        string_lista_desempacotada=""
        for char in lista:
            string_lista_desempacotada+= char
        return string_lista_desempacotada
    
    def verificar_decimal(self,lista):
        for char in lista:
             if char == ".":
                 return False
        return True
    
    def empacotar_lista_numeros(self,texto):
        lista=[]
        for n in texto:
            if n in "1234567890.":
                lista.append(n)
            else:
                break
        return lista
    
    def empacotar_lista_numeros_entre_sinais(self,texto):
        lista=[]
        permissao=False
        for n in texto:
            if n in "+-/x÷":
               permissao=True
            if n in "=":
                permissao=False
            if permissao == True and n not in "+-/x÷":
                lista.append(n)
           
        return lista
    
    def empacotar_lista_numeros_dps_sinal(self,texto):
        lista=[]
        permissao=False
        for n in texto:
            if n in "=":
               permissao=True
            if permissao == True and n != "=":
                lista.append(n)
           
        return lista
    '''
    Teclas pressionadas def
    '''
    def keyPressEvent(self,event:QKeyEvent):
        print(event.__repr__())
        if str(event.text()) in "1234567890":
            self.lista_campo_atual.append(event.text())
            self.campo_atual_espaco.setText(self.desempacotar_lista(self.lista_campo_atual))
            # self.campo_atual_espaco.setText(self.campo_atual_espaco.text() + str(event.text()))

        elif str(event.text()) == "\b" and self.lista_campo_atual:

            self.lista_campo_atual.pop()
            self.campo_atual_espaco.setText(self.desempacotar_lista(self.lista_campo_atual))
        
        elif str(event.text()) == "." and self.lista_campo_atual and self.verificar_decimal(self.lista_campo_atual):
            self.lista_campo_atual.append(event.text())
            self.campo_atual_espaco.setText(self.desempacotar_lista(self.lista_campo_atual))

        elif str(event.text()) =="\r":
            self.button_eq.click()

        
        elif str(event.text()) == "-" and self.lista_campo_atual:
            if self.operacao_ativa ==  False:
                self.inicio_sub()
            else:
                self.fim_sub()
            
                 

        elif str(event.text()) == "+" and self.lista_campo_atual:
            if self.operacao_ativa ==  False:
                self.inicio_adicao()
            else:
                self.fim_adicao()
        
            


'''
Inicialização do programa
'''
main_=main()
icone=QIcon()
icone.addFile(r"pyside_aulas\calculadora\calculadora_icon.png")
window=QMainWindow()
window.setCentralWidget(main_)
window.setWindowIcon(icone)
window.setWindowTitle("Calculadora")
window.show()
app.exec()









