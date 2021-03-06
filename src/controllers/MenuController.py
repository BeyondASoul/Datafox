from PyQt5.QtWidgets import QFileDialog,QMessageBox,QMessageBox
from PyQt5.QtGui import QKeySequence
from model import DataAdapter
from pandas.errors import ParserError
from .MyWorker import MyWorker
from PyQt5.QtCore import QThread
from views import LoadingScreen
class MenuController:
    def __init__(self,view,model):
        self.view=view
        self.model=model
        self.carga=0
        self.read_thread=None
        self.read_worker=None
        self.loading_screen=LoadingScreen(self.view)
        self.bind_signals()

    def bind_signals(self):
        self.view.buttonAbrir.clicked.connect(self.openFile)
        self.view.buttonAbrir.setShortcut(QKeySequence("Ctrl+o"))

        self.view.buttonCerrar.clicked.connect(self.closeFile)
        self.view.buttonCerrar.setShortcut(QKeySequence("Ctrl+w"))

    def aumentar_carga(self,valor):
        self.carga=self.carga+valor
        # self.view.progress_bar.setProperty("value",self.carga)
        self.loading_screen.loading_bar.setProperty("value",self.carga)
        if self.carga==100:
            self.view.load_screen.hide()
            self.view.tabWidget.show()
            self.loading_screen.close()
            self.carga=0
            # self.view.progress_bar.setProperty("value",self.carga)
            self.loading_screen.loading_bar.setProperty("value",self.carga)

    def openFile(self):
        file = QFileDialog.getOpenFileName(self.view,
            "Abrir archivo", "../datasets","Archivo de datos (*.csv)"
        )[0]
        if len(file)>0:
            
            has_header=QMessageBox.question(self.view,"Abrir","¿Tu conjunto de datos cuenta con una cabecera?")
            if has_header==QMessageBox.Yes:
                print("El archivo seleccionado sí tiene cabecera")
                has_header=True
            elif has_header==QMessageBox.No:
                print("El archivo seleccionado no tiene cabecera")
                has_header=False

            self.view.tabWidget.hide()
            self.view.load_screen.show()
            self.loading_screen.open()
            # Cambiando el titulo de la ventana
            file_name=file.split('/')[-1]
            try:
                self.view.setWindowTitle(f"Datafox - {file_name}")
                print("Comenzando carga de archivo")
                self.read_thread=QThread()
                self.read_worker=MyWorker(self.model)
                self.read_worker.moveToThread(self.read_thread)
                self.read_worker.set_file(file,has_header=has_header)
                self.read_worker.complete.connect(self.read_thread.quit)
                self.read_worker.complete.connect(self.read_worker.deleteLater)
                self.read_thread.finished.connect(self.read_thread.deleteLater)

                self.read_thread.started.connect(self.read_worker.read_file)
                self.read_worker.complete.connect(self.model.notify_observers)
                self.read_thread.start()
                
            except FileNotFoundError:
                self.show_error_popup("No se ha encontrado el archivo")
                return
            except (ParserError,IndexError):
                self.show_error_popup("No se pudieron extraer los datos del archivo")
                return
            except PermissionError:
                self.show_error_popup("No se tienen permisos para abrir el archivo")
                return
        else:
            pass

    def closeFile(self):
        self.file=None
        self.datos=None
        self.view.tabWidget.hide()
        self.view.load_screen.show()
        self.view.setWindowTitle("Datafox")
        QMessageBox.warning(self.view,"Cerrar","Se cerró el archivo CSV...")

    def exit(self):
        self.view.close()

    def show_error_popup(self,message):
        self.model.file=None
        self.view.setWindowTitle("Datafox")
        error_message=QMessageBox()
        error_message.critical(self.view,"Error",message)
        error_message.setFixedSize(500,200)
