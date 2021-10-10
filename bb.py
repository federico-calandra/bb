#! /usr/bin/env python3

# Versione 2.2

from PyQt5 import QtCore, QtWidgets, uic
from datetime import *
from os import mknod, listdir
import M

## Variabili usate nel programma
initTabIndex = 0
saveFileExt = '.ses'

## Classe per carica il file .ui che definisce la finestra
class Ui(QtWidgets.QWidget):
	def __init__(self, ui_file):
		super().__init__()
		uic.loadUi(ui_file, self)

## Classe che espande QListWidgetItem implementando livelli di gerarchia 
class QListItem(QtWidgets.QListWidgetItem):
	def __init__(self, strNome, widget=None, intLivello=None, strParent=None):
		self.livello = intLivello
		self.parent = strParent
		if self.livello == 0:	# l'item indica un comparto
			super().__init__(strNome, widget)
			self.setFlags(self.flags() & ~QtCore.Qt.ItemIsEnabled)
			
		if self.livello == 1:	# l'item indica un muscolo
			super().__init__(strNome, widget)
			
		if self.livello == 2:	# l'item indica un capo muscolare
			super().__init__(strNome, widget)
		
## Funzione che inizializza la finestra window, e se è una dialog la visualizza anche
def initializeWindow(w):
	if w == window1:
		# inizializzo tab1
		for comparto in M.comparti:	# aggiungo i comparti
			QListItem(':: '+comparto.capitalize()+' ::', w.tab1_listMuscoli, 0)
			for muscolo in M.muscoli:	# aggiungo i muscoli
				if muscolo.comparto == comparto:
					if muscolo.capi == []:
						QListItem('    '+muscolo.nome.capitalize(), w.tab1_listMuscoli, 1)
					else:
						QListItem('    '+muscolo.nome.capitalize(), w.tab1_listMuscoli, 1)
						for capo in muscolo.capi:
							QListItem('      - '+capo, w.tab1_listMuscoli, 2, muscolo.nome)						
						
		w.tab1_listMuscoli.setCurrentRow(1)
		refreshList(window1.tab1_listEsercizi, window1.tab1_listMuscoli)	# preparo listEsercizi
		
		# ~ #inizializzo tab2
		for obj in M.esercizi:	# aggiungo gli esercizi a listEsercizi
			w.tab2_listEsercizi.addItem(obj.nome.capitalize())
		w.tab2_listEsercizi.setCurrentRow(0)	# seleziono prima riga di listEsercizi
				
		refreshList(w.tab2_listMuscoli, w.tab2_listEsercizi)	# preparo listMuscoli
		
		w.tabWidget.setCurrentIndex(initTabIndex)	# imposto quale tab è visualizzata
		w.move(0, 178)
		w.show()
	
	if w == window2:
		w.tableSessione.setColumnWidth(0, 330)
		w.tableSessione.setColumnWidth(1, 30)
		w.tableSessione.setColumnWidth(2, 30)
		w.tableSessione.setColumnWidth(3, 100)
		w.tableSessione.setRowCount(0)
	
	if w == dialogSalva:
		w.tboxNome.clear()
		w.show()
		
	if w == dialogCarica:
		if w.isHidden() == False: return
		w.listWidget.clear()
		#considero i file che hanno estensione .ses nella cartella attuale e li aggiungo a listWidget
		ls = listdir()
		for f in ls:
			if f[-3:len(f)] == 'ses':
				w.listWidget.addItem(f[0:len(f)-len(saveFileExt)])
		w.listWidget.setCurrentRow(0)
		w.show()
		
	return w
		
## Funzione che fa popola la lista slave secondo i risultati di ricerca
def refreshList(slave, master):
	slave.clear()
	sel = master.currentItem()
	c1 = []
	c2 = []
	c3 = []
	if master == window1.tab1_listMuscoli:	# usata su tab1 per gli esercizi che allenano un muscolo
		if sel.parent is None:	# muscolo con 1 capo
			res = M.cerca(3, sel.text().lstrip(' -').casefold())
			for e in res[0]:
				for m in e.muscoli: 
					if m.nome == sel.text().lstrip(' -').casefold():
						if m.livello == 1: c1.append(QListItem(e.nome.capitalize(), intLivello=1))
						if m.livello == 2: c2.append(QListItem(e.nome.capitalize(), intLivello=1))
						if m.livello == 3: c3.append(QListItem(e.nome.capitalize(), intLivello=1))
			QListItem('Primari', slave, 0)
			for item in c1: slave.addItem(item)
			QListItem('Secondari', slave, 0)
			for item in c2: slave.addItem(item)
			QListItem('Ausiliari', slave, 0)
			for item in c3: slave.addItem(item)
		elif sel.parent is not None:	# muscolo con più capi
			res = M.cerca(4, [sel.parent, sel.text().lstrip(' -').casefold()])
			for e in res[0]:
				for m in e.muscoli:
					if m.nome == sel.parent and sel.text().lstrip(' -').casefold() in m. capi:
						if m.livello == 1: c1.append(QListItem(e.nome.capitalize(), intLivello=1))
						if m.livello == 2: c2.append(QListItem(e.nome.capitalize(), intLivello=1))
						if m.livello == 3: c3.append(QListItem(e.nome.capitalize(), intLivello=1))
			QListItem('Primari', slave, 0)
			for item in c1: slave.addItem(item)
			QListItem('Secondari', slave, 0)
			for item in c2: slave.addItem(item)
			QListItem('Ausiliari', slave, 0)
			for item in c3: slave.addItem(item)
					
	if master == window1.tab2_listEsercizi:	# usata su tab2 per i muscoli allenati da un esercizio
		res = M.cerca(1, sel.text().casefold())[0][0]	# in questo modo recupero l'oggetto esercizio
		c1 = []
		c2 = []
		c3 = []
		# questo forse può essere migliorato #
		for m in res.muscoli:	# metto ogni muscolo nella categoria in base al livello di coinvolgimento
			if m.livello == 1:
				if m.capi == []: c1.append(QListItem(m.nome.capitalize(), intLivello=1))
				else:
					for c in m.capi: c1.append(QListItem(m.nome.capitalize()+' '+c, intLivello=1))
			if m.livello == 2:
				if m.capi == []: c2.append(QListItem(m.nome.capitalize(), intLivello=1))
				else:
					for c in m.capi: c2.append(QListItem(m.nome.capitalize()+' '+c, intLivello=1))
			if m.livello == 3:
				if m.capi == []: c3.append(QListItem(m.nome.capitalize(), intLivello=1))
				else:
					for c in m.capi: c3.append(QListItem(m.nome.capitalize()+' '+c, intLivello=1))
		QListItem('Primari', slave, 0)
		for item in c1: slave.addItem(item)
		QListItem('Secondari', slave, 0)
		for item in c2: slave.addItem(item)
		QListItem('Ausiliari', slave, 0)
		for item in c3: slave.addItem(item)
		# fino a qua ma come?#
	
	slave.setCurrentRow(1)
	return slave

## Funzione che popola window2.tableSessione secondo elementi da listSessione o da file
def buildSessione(ses = None):
	initializeWindow(window2)

	if ses is None:	# costruisco la tabella a partire da listSessione
		if window1.tab1_listSessione.count() == 0: return
		for i in range(window1.tab1_listSessione.count()):
			item = window1.tab1_listSessione.item(i)
			window2.tableSessione.insertRow(i)
			window2.tableSessione.setItem(i, 0, QtWidgets.QTableWidgetItem(window1.tab1_listSessione.item(i).text()))
		window2.tableSessione.setCurrentCell(0, 0)
		
	elif ses is not None:	# costruisco la tabella per invocazione da caricaSessione
		for i in range(len(ses)):
			window2.tableSessione.insertRow(window2.tableSessione.rowCount())
			for j in range(window2.tableSessione.columnCount()):
				window2.tableSessione.setItem(i, j, QtWidgets.QTableWidgetItem(ses[i][j]))
	
	dialogCarica.hide()
	window2.show()
	return window2.tableSessione
	
## Funzione che salva tableSessione su un file .ses, in forma CSV
def salvaSessione(strNome):
	t = datetime.today()
	if t.day < 10: path = str(t.year) + '-' + str(t.month) + '-' + '0' + str(t.day)
	else: path = str(t.year) + '-' + str(t.month) + '-' + str(t.day)
	
	
	if strNome == '': path = path + saveFileExt
	else: path = path + '_' + str(strNome) + saveFileExt
	
	try : mknod(path)
	except FileExistsError: print('Errore: file già esistente')	# TO-DO implementare dialog
	with open(path, 'w') as f:
		for r in range(window2.tableSessione.rowCount()):
			for c in range(window2.tableSessione.columnCount()):
				try: f.write(window2.tableSessione.item(r, c).text() + ';')
				except: f.write(';')
			f.write('\n')
	
	dialogSalva.close()
	return 0

## Funzione che genera una list i cui elementi sono altre list. Gli elementi di queste ultime descrivono la sessione da caricare
def caricaSessione(strNome):
	with open(strNome, 'r') as f:
		lines = f.readlines()
	ses = []
	var = []
	
	for l in lines:
		for i in l.split(';'):
			if i != '\n':
				var.append(i)
		ses.append(var)
		var = []
	
	buildSessione(ses)
	return ses

## Funzione che gestisce i pulsanti +, -, Up e Dn
def tbHandler(intIndex, item = None):
	if intIndex == 0:	# aggiungi
		# ~ if item is None: return	# in questo modo evito l'eccezione se non c'è nessun elemento selezionato
		window1.tab1_listSessione.addItem(item.text())
		window1.tab1_listSessione.setCurrentRow(window1.tab1_listSessione.count()-1)
		
	if intIndex == 1:	# rimuovi
		window1.tab1_listSessione.takeItem(item)
		
	if intIndex == 2:	# sposta su
		if item == 0: return
		window1.tab1_listSessione.insertItem(item-1, window1.tab1_listSessione.takeItem(item))
		window1.tab1_listSessione.setCurrentRow(item-1)
		
	if intIndex == 3:	#sposta giù
		if item == window1.tab1_listSessione.count()-1: return
		window1.tab1_listSessione.insertItem(item+1, window1.tab1_listSessione.takeItem(item))
		window1.tab1_listSessione.setCurrentRow(item+1)

	return 0


if __name__ == "__main__":
	app = QtWidgets.QApplication([])	# necessario per mostrare le finestre
	window1 = Ui('window1.ui')
	window2 = Ui('window2.ui')
	dialogSalva = Ui('dialogSalva.ui')
	dialogCarica = Ui('dialogCarica.ui')
	
	## Inizializza window1
	initializeWindow(window1)
	
	## Connettori
	window1.tab1_listMuscoli.currentItemChanged.connect(lambda: refreshList(window1.tab1_listEsercizi, window1.tab1_listMuscoli))
	window1.tab2_listEsercizi.currentItemChanged.connect(lambda: refreshList(window1.tab2_listMuscoli, window1.tab2_listEsercizi))
	
	window1.tbPlus.clicked.connect(lambda: tbHandler(0, window1.tab1_listEsercizi.currentItem()))
	window1.tbMinus.clicked.connect(lambda: tbHandler(1, window1.tab1_listSessione.currentRow()))
	window1.tbUp.clicked.connect(lambda: tbHandler(2, window1.tab1_listSessione.currentRow()))
	window1.tbDn.clicked.connect(lambda: tbHandler(3, window1.tab1_listSessione.currentRow()))
	
	window1.pbOk.clicked.connect(lambda: buildSessione())
	window1.pbCarica.clicked.connect(lambda: initializeWindow(dialogCarica))
	
	window2.pbSalva.clicked.connect(lambda: initializeWindow(dialogSalva))
	
	dialogSalva.pbSalva.clicked.connect(lambda: salvaSessione(dialogSalva.tboxNome.text()))
	dialogCarica.pbCarica.clicked.connect(lambda: caricaSessione(dialogCarica.listWidget.currentItem().text()+saveFileExt))

input()
