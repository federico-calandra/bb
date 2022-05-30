class Muscolo:
	def __init__(self, strComparto, strNome, lstCapi, intEngage = None):
		self.comparto = strComparto
		self.nome = strNome
		self.capi = lstCapi
		self.livello = intEngage
		
class Esercizio:
	def __init__(self, strNome, lstMuscoli):
		self.nome = strNome
		self.muscoli = []
		for m in lstMuscoli:
			self.muscoli.append(m)

comparti = ['spalle', 'torso', 'braccia', 'dorso', 'addome', 'gambe']

## Funzione che data una stringa restituisce gli oggetti nella lista target i cui nomi la contengono
def cerca(intMode, strExp):
	res = [[], []]
	if intMode == 0:	# restituisce i muscoli il cui nome contine strExp
		for m in muscoli:
			if strExp in m.nome:
				res[0].append(m)
				res[1].append(m.nome)
	if intMode == 1:	# restituisce gli esercizi il cui nome contiene strExp
		for e in esercizi:
			if strExp in e.nome:
				res[0].append(e)
				res[1].append(e.nome)	
	if intMode == 2:	# restituisce i muscoli del comparto strExp
		for m in muscoli:
			if strExp == m.comparto:
				res[0].append(m)
				res[1].append(m.nome)	
	if intMode == 3:	# restituisce gli esercizi che allenano il muscolo strExp
		for e in esercizi:
			for m in e.muscoli:
				if strExp == m.nome:
					res[0].append(e)
					res[1].append(e.nome)
	if intMode == 4:	# restituisce gli esercizi che allenano il capo strExp
		for e in esercizi:
			for m in e.muscoli:
				if m.nome == strExp[0]:
					for c in m.capi:
						if strExp[1] == c:
							res[0].append(e)
							res[1].append(e.nome)
		
	return res

def creaMuscoli():
	muscoli = []
	muscoli.append(Muscolo('spalle', 'deltoide', ['anteriore', 'laterale', 'posteriore']))
	muscoli.append(Muscolo('spalle', 'rotondo grande', []))
	muscoli.append(Muscolo('torso', 'pettorale', ['clavicolare', 'sternale', 'addominale']))
	muscoli.append(Muscolo('dorso', 'dorsale', ['vertebrale', 'scapolare', 'iliaco', 'costale']))
	muscoli.append(Muscolo('dorso', 'trapezio', ['discendente', 'trasverso', 'ascendente']))
	muscoli.append(Muscolo('braccia', 'bicipite brachiale', ['lungo', 'breve']))
	muscoli.append(Muscolo('braccia', 'brachiale', []))
	muscoli.append(Muscolo('braccia', 'brachioradiale', []))
	muscoli.append(Muscolo('braccia', 'tricipite brachiale', ['lungo', 'laterale', 'mediale']))
	muscoli.append(Muscolo('addome', 'obliquo', []))
	muscoli.append(Muscolo('addome', 'retto addominale', []))
	muscoli.append(Muscolo('gambe', 'gluteo grande', []))
	muscoli.append(Muscolo('gambe', 'gastrocnemio', ['mediale', 'laterale']))
	muscoli.append(Muscolo('gambe', 'quadricipite femorale', ['femorale', 'laterale', 'intermedio', 'mediale']))
	muscoli.append(Muscolo('gambe', 'tensore fascia lata', []))
	muscoli.append(Muscolo('gambe', 'bicipite femorale', ['lungo', 'breve']))
	muscoli.append(Muscolo('gambe', 'semimembranoso', []))
	muscoli.append(Muscolo('gambe', 'semitendinoso', []))
	return muscoli

def creaEsercizi():
	esercizi = []
	esercizi.append(Esercizio('affondo con manubri', [Muscolo('gambe', 'quadricipite', ['femorale', 'laterale'], 1), Muscolo('gambe', 'gluteo grande', [], 1)]))
	esercizi.append(Esercizio('affondo alternato', [Muscolo('gambe', 'gluteo grande', [], 1), Muscolo('gambe', 'quadricipite', ['femorale', 'laterale', 'mediale'], 1)]))
	esercizi.append(Esercizio('alzata frontale', [Muscolo('spalle', 'deltoide', ['anteriore'], 1), Muscolo('torso', 'pettorale', ['clavicolare'], 1)]))
	esercizi.append(Esercizio('alzata frontale con bilanciere', [Muscolo('spalle', 'deltoide', ['anteriore'], 1), Muscolo('torso', 'pettorale', ['clavicolare'], 1)]))
	esercizi.append(Esercizio('alzata laterale', [Muscolo('spalle', 'deltoide', ['laterale'], 1), Muscolo('dorso', 'trapezio', ['discendente'], 2)]))
	esercizi.append(Esercizio('alzata di spalle', [Muscolo('dorso', 'trapezio', ['discendente'], 1)]))
	esercizi.append(Esercizio('croce panca piana', [Muscolo('torso', 'pettorale', ['clavicolare', 'sternale', 'addominale'], 1)]))
	esercizi.append(Esercizio('croce panca inclinata', [Muscolo('torso', 'pettorale', ['clavicolare'], 1), Muscolo('spalle', 'deltoide', ['anteriore'], 1)]))
	esercizi.append(Esercizio('crunch addominale', [Muscolo('addome', 'retto addominale', [], 1), Muscolo('gambe', 'tensore fascia lata', [], 2), Muscolo('gambe', 'quadricipite', ['femorale'], 2)]))
	esercizi.append(Esercizio('crunch addominale alternato', [Muscolo('addome', 'retto addominale', [], 1), Muscolo('addome', 'obliquo', [], 1), Muscolo('gambe', 'tensore fascia lata', [], 2), Muscolo('gambe', 'quadricipite', ['femorale'], 2)]))
	esercizi.append(Esercizio('curl avambraccio, presa neutra', [Muscolo('braccia', 'brachioradiale', [], 1), Muscolo('braccia', 'brachiale', [], 2), Muscolo('braccia', 'bicipite', ['lungo', 'breve'], 2)]))
	esercizi.append(Esercizio('curl avambraccio con rotazione polso, presa neutra', [Muscolo('braccia', 'bicipite brachiale', ['lungo', 'breve'], 1), Muscolo('braccia', 'brachioradiale', [], 2), Muscolo('braccia', 'brachiale', [], 2), Muscolo('spalle', 'deltoide', ['anteriore'], 3), Muscolo('torso', 'pettorale', ['clavicolare'], 3)]))
	esercizi.append(Esercizio('curl avambraccio, presa prona', [Muscolo('braccia', 'brachiale', [], 1), Muscolo('braccia', 'bicipite brachiale', ['lungo', 'breve'], 2)]))
	esercizi.append(Esercizio('curl avambraccio, presa supina', [Muscolo('braccia', 'brachiale', [], 1), Muscolo('braccia', 'brachioradiale', [], 2)]))
	# approfondire diretto e inverso #
	esercizi.append(Esercizio('dip', [Muscolo('torso', 'pettorale', ['addominale']), Muscolo('braccia', 'tricipite brachiale', ['lungo', 'laterale', 'mediale']), Muscolo('spalle', 'deltoide', ['anteriore'])]))
	esercizi.append(Esercizio('dip inverso', [Muscolo('braccia', 'tricipite brachiale', ['lungo', 'laterale', 'mediale']), Muscolo('torso', 'pettorale', ['clavicolare', 'sternale', 'addominale']), Muscolo('spalle', 'deltoide', ['anteriore'])]))
	esercizi.append(Esercizio('distensione panca piana', [Muscolo('torso', 'pettorale', ['clavicolare', 'sternale', 'addominale'], 1), Muscolo('braccia', 'tricipite brachiale', ['lungo', 'mediale'], 2), Muscolo('spalle', 'deltoide', ['anteriore'], 2)]))
	esercizi.append(Esercizio('distensione panca inclinata', [Muscolo('torso', 'pettorale', ['clavicolare'], 1), Muscolo('braccia', 'tricipite brachiale', ['lungo', 'mediale'], 2), Muscolo('spalle', 'deltoide', ['anteriore'], 2)]))
	esercizi.append(Esercizio('distensione panca reclinata', [Muscolo('torso', 'pettorale', ['addominale'], 1), Muscolo('braccia', 'tricipite brachiale', ['lungo', 'mediale'], 2), Muscolo('spalle', 'deltoide', ['anteriore'], 2)]))
	esercizi.append(Esercizio('estensione avambraccio in alto', [Muscolo('braccia', 'tricipite brachiale', ['lungo', 'laterale'], 1)]))
	esercizi.append(Esercizio('estensione avambraccio in alto, a due mani', [Muscolo('braccia', 'tricipite brachiale', ['lungo', 'laterale', 'mediale'], 1)]))
	esercizi.append(Esercizio('flessione laterale busto', [Muscolo('addome', 'obliquo', [], 1), Muscolo('addome', 'retto addominale', [], 2)]))
	esercizi.append(Esercizio('kick back', [Muscolo('braccia', 'tricipite brachiale', ['laterale', 'lungo'], 1)]))
	# ~ esercizi.append(Esercizio('lat machine avanti, presa prona', [Muscolo('dorso', 'dorsale', ['vertebrale', 'scapolare'], 1), Muscolo('dorso', 'rotondo grande', [], 1), Muscolo('dorso', 'trapezio', ['trasversale', 'ascendente'], 2), Muscolo('braccia', 'bicipite brachiale', ['lungo', 'breve'], 2), Muscolo('braccia', 'brachiale', [], 2), Muscolo('torso', 'pettorale', ['clavicolare', 'sternale', 'addominale'], 3)]))
	esercizi.append(Esercizio('lat machine avanti, presa prona larga', [Muscolo('dorso', 'dorsale', ['iliaco', 'costale'], 1), Muscolo('dorso', 'rotondo grande', [], 1), Muscolo('dorso', 'trapezio', ['trasversale', 'ascendente'], 2), Muscolo('braccia', 'bicipite brachiale', ['lungo', 'breve'], 2), Muscolo('braccia', 'brachiale', [], 2), Muscolo('torso', 'pettorale', ['clavicolare', 'sternale', 'addominale'], 3)]))
	# ~ esercizi.append(Esercizio('lat machine avanti, presa prona stretta', [Muscolo('dorso', 'dorsale', ['vertebrale', 'scapolare'], 1), Muscolo('dorso', 'rotondo grande', [], 1), Muscolo('dorso', 'trapezio', ['trasversale', 'ascendente'], 2), Muscolo('braccia', 'bicipite brachiale', ['lungo', 'breve'], 2), Muscolo('braccia', 'brachiale', [], 2), Muscolo('torso', 'pettorale', ['clavicolare', 'sternale', 'addominale'], 3)]))
	esercizi.append(Esercizio('lat machine avanti, presa supina', [Muscolo('dorso', 'dorsale', ['vertebrale', 'scapolare'], 1), Muscolo('dorso', 'rotondo grande', [], 1), Muscolo('dorso', 'trapezio', ['trasversale', 'ascendente'], 2), Muscolo('braccia', 'bicipite brachiale', ['lungo', 'breve'], 2), Muscolo('braccia', 'brachiale', [], 2), Muscolo('torso', 'pettorale', ['clavicolare', 'sternale', 'addominale'], 3)]))
	esercizi.append(Esercizio('lat machine dietro', [Muscolo('dorso', 'dorsale', ['iliaco', 'costale'], 1), Muscolo('spalle', 'rotondo grande', [], 1), Muscolo('dorso', 'trapezio', ['ascendente'], 2), Muscolo('braccia', 'bicipite brachiale', ['lungo', 'breve'], 2), Muscolo('braccia', 'brachiale', [], 2), Muscolo('braccia', 'brachioradiale', [], 2)]))
	esercizi.append(Esercizio('lat machine a braccia tese', [Muscolo('dorso', 'dorsale', ['vertebrale', 'scapolare', 'iliaco', 'costale'], 1), Muscolo('spalle', 'rotondo grande', [], 2), Muscolo('braccia', 'tricipite brachiale', ['lungo'], 2)]))
	esercizi.append(Esercizio('lat tricipite, presa prona', [Muscolo('braccia', 'tricipite brachiale', ['laterale', 'lungo', 'mediale'], 1)]))
	esercizi.append(Esercizio('lat tricipite, presa prona, di spalle', [ Muscolo('braccia', 'tricipite brachiale', ['lungo'], 1)]))
	esercizi.append(Esercizio('lat tricipite, presa supina', [Muscolo('braccia', 'tricipite brachiale', ['mediale'], 1)]))
	esercizi.append(Esercizio('lento avanti', [Muscolo('spalle', 'deltoide', ['anteriore', 'laterale'], 1), Muscolo('torso', 'pettorale', ['clavicolare'], 1), Muscolo('dorso', 'trapezio', ['discendente', 'trasverso', 'ascendente'], 2), Muscolo('braccia', 'tricipite brachiale', ['lungo', 'mediale'], 2)]))
	esercizi.append(Esercizio('lento dietro', [Muscolo('spalle', 'deltoide', ['laterale', 'posteriore'], 1), Muscolo('dorso', 'trapezio', ['discendente', 'trasverso', 'ascendente'], 2), Muscolo('braccia', 'tricipite brachiale', ['laterale', 'lungo', 'mediale'], 2)]))
	esercizi.append(Esercizio('piegamento sulle braccia', [Muscolo('torso', 'pettorale', ['clavicolare', 'sternale', 'addominale'], 1), Muscolo('braccia', 'tricipite brachiale', ['laterale', 'lungo', 'mediale'], 1), Muscolo('spalle', 'deltoide', ['anteriore'], 2)]))
	esercizi.append(Esercizio('piegamento sulle braccia, mani rialzate', [Muscolo('torso', 'pettorale', ['addominale'], 1), Muscolo('braccia', 'tricipite brachiale', ['laterale', 'lungo', 'mediale'], 1), Muscolo('spalle', 'deltoide', ['anteriore'], 2)]))
	esercizi.append(Esercizio('piegamento sulle braccia, piedi rialzati', [Muscolo('torso', 'pettorale', ['clavicolare'], 1), Muscolo('braccia', 'tricipite brachiale', ['laterale', 'lungo', 'mediale'], 1), Muscolo('spalle', 'deltoide', ['anteriore'], 2)]))
	esercizi.append(Esercizio('pullover manubrio', [Muscolo('torso', 'pettorale', ['clavicolare', 'sternale', 'addominale'], 1), Muscolo('braccia', 'tricipite brachiale', ['lungo'], 1), Muscolo('spalle', 'rotondo grande', [], 1), Muscolo('dorso', 'dorsale', ['vertebrale', 'scapolare', 'iliaco', 'costale'], 1)]))
	# approfondire varie impugnature #
	esercizi.append(Esercizio('rematore con bilanciere', [Muscolo('dorso', 'dorsale', ['vertebrale', 'scapolare', 'iliaco', 'costale'], 1), Muscolo('dorso', 'rotondo grande', [], 1), Muscolo('spalle', 'deltoide', ['posteriore'], 1), Muscolo('dorso', 'trapezio', ['discendente', 'trasversale', 'ascendente'], 1)]))
	esercizi.append(Esercizio('rematore verticale', [Muscolo('dorso', 'trapezio', ['discendente', 'trasversale', 'ascendente'], 1), Muscolo('spalle', 'deltoide', ['anteriore', 'laterale', 'posteriore'], 1), Muscolo('braccia', 'bicipite brachiale', ['lungo', 'breve'], 1), Muscolo('braccia', 'brachioradiale', [], 2)]))
	esercizi.append(Esercizio('sollevamento busto da terra', [Muscolo('addome', 'retto addominale', [], 1), Muscolo('addome', 'obliquo', [], 2)]))
	esercizi.append(Esercizio('sollevamento gambe da terra', [Muscolo('addome', 'retto addominale', [], 1), Muscolo('addome', 'obliquo', [], 2), Muscolo('gambe', 'tensore fascia lata', [], 3), Muscolo('gambe', 'quadricipite', ['femorale'], 3)]))
	esercizi.append(Esercizio('squat', [Muscolo('gambe', 'quadricipite femorale', ['femorale', 'laterale', 'intermedio', 'mediale'], 1), Muscolo('gambe', 'gluteo grande', [], 1)]))
	# approfondire differenze fra avanti e dietro #
	esercizi.append(Esercizio('trazione sbarra avanti, presa prona', [Muscolo('dorso', 'dorsale', ['vertebrale', 'scapolare'], 1), Muscolo('dorso', 'rotondo grande', [], 1), Muscolo('dorso', 'trapezio', ['ascendente'], 1), Muscolo('braccia', 'bicipite brachiale', ['lungo', 'breve'], 2), Muscolo('braccia', 'brachiale', [], 2), Muscolo('braccia', 'brachioradiale', [], 2), Muscolo('torso', 'pettorale', ['clavicolare', 'trasversale', 'addominale'], 3)]))
	esercizi.append(Esercizio('trazione sbarra avanti, presa supina', [Muscolo('dorso', 'dorsale', ['vertebrale', 'scapolare', 'iliaco', 'costale'], 1), Muscolo('dorso', 'rotondo grande', [], 1), Muscolo('braccia', 'bicipite brachiale', ['lungo', 'breve'], 1), Muscolo('braccia', 'brachiale', [], 1), Muscolo('braccia', 'brachioradiale', [], 1), Muscolo('dorso', 'trapezio', ['trasverale', 'ascendente'], 2), Muscolo('torso', 'pettorale', ['clavicolare', 'trasversale', 'addominale'], 3)]))
	esercizi.append(Esercizio('trazione sbarra dietro', [Muscolo('dorso', 'dorsale', ['iliaco', 'costale'], 1), Muscolo('spalle', 'rotondo grande', [], 1), Muscolo('dorso', 'trapezio', ['ascendente'], 1), Muscolo('braccia', 'bicipite brachiale', ['lungo', 'breve'], 2), Muscolo('braccia', 'brachiale', [], 2), Muscolo('braccia', 'brachioradiale', [], 2), Muscolo('torso', 'pettorale', ['clavicolare', 'trasversale', 'addominale'], 3)]))
	return esercizi

muscoli = creaMuscoli()
esercizi = creaEsercizi()
