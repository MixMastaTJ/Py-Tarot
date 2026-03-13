import sys, math, random, logging
from PySide6 import Qt, QtCore, QtWidgets, QtGui

CardDictionary = {
	'Major01' : "I: The Magician",
	'Major02' : "II: The High Priestess",
	'Major03' : "III: The Empress",
	'Major04' : "IV: The Emperor",
	'Major05' : "V: The Hierophant",
	'Major06' : "VI: The Lovers",
	'Major07' : "VII: The Chariot",
	'Major08' : "VIII: Strength",
	'Major09' : "IX: The Hermit",
	'Major10' : "X: Wheel of Fortune",
	'Major11' : "XI: Justice",
	'Major12' : "XII: The Hanged Man",
	'Major13' : "XIII: Death",
	'Major14' : "XIV: Temperance",
	'Major15' : "XV: The Devil",
	'Major16' : "XVI: The Tower",
	'Major17' : "XVII: The Star",
	'Major18' : "XVIII: The Moon",
	'Major19' : "XIX: The Sun",
	'Major20' : "XX: Judgement",
	'Major21' : "XXI: The World",
	'Major00' : "0: The Fool",
	'Cups01' : "Ace of Cups",
	'Cups02' : "Two of Cups",
	'Cups03' : "Three of Cups",
	'Cups04' : "Four of Cups",
	'Cups05' : "Five of Cups",
	'Cups06' : "Six of Cups",
	'Cups07' : "Seven of Cups",
	'Cups08' : "Eight of Cups",
	'Cups09' : "Nine of Cups",
	'Cups10' : "Ten of Cups",
	'Cups11' : "Page of Cups",
	'Cups12' : "Knight of Cups",
	'Cups13' : "Queen of Cups",
	'Cups14' : "King of Cups",
	'Wands01': "Ace of Wands",
	'Wands02': "Two of Wands",
	'Wands03': "Three of Wands",
	'Wands04': "Four of Wands",
	'Wands05': "Five of Wands",
	'Wands06': "Six of Wands",
	'Wands07': "Seven of Wands",
	'Wands08': "Eight of Wands",
	'Wands09': "Nine of Wands",
	'Wands10': "Ten of Wands",
	'Wands11': "Page of Wands",
	'Wands12': "Knight of Wands",
	'Wands13': "Queen of Wands",
	'Wands14': "King of Wands",
	'Swords01': "Ace of Swords",
	'Swords02': "Two of Swords",
	'Swords03': "Three of Swords",
	'Swords04': "Four of Swords",
	'Swords05': "Five of Swords",
	'Swords06': "Six of Swords",
	'Swords07': "Seven of Swords",
	'Swords08': "Eight of Swords",
	'Swords09': "Nine of Swords",
	'Swords10': "Ten of Swords",
	'Swords11': "Page of Swords",
	'Swords12': "Knight of Swords",
	'Swords13': "Queen of Swords",
	'Swords14': "King of Swords",
	'Pents01' : "Ace of Pentacles",
	'Pents02' : "Two of Pentacles",
	'Pents03' : "Three of Pentacles",
	'Pents04' : "Four  of Pentacles",
	'Pents05' : "Five of Pentacles",
	'Pents06' : "Six of Pentacles",
	'Pents07' : "Seven of Pentacles",
	'Pents08' : "Eight of Pentacles",
	'Pents09' : "Nine of Pentacles",
	'Pents10' : "Ten of Pentacles",
	'Pents11' : "Page of Pentacles",
	'Pents12' : "Knight of Pentacles",
	'Pents13' : "Queen of Pentacles",
	'Pents14' : "King of Pentacles"
}

class mainWindow(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()

		self._base_size = QtCore.QSize(1280,720)
		self._current_scale = 1
		self.magicScaler = (2/9)
		self.Deck = self.addWidget(Deck())
		self.Deck.shuffle()

	def resizeEvent(self, event):
		super().resizeEvent(event)
		
		self._current_scale = event.size().height() / self._base_size.height()

		for child in self.children():
			if isinstance(child, (Card, Deck)):
				child.rescale(self._current_scale * self.magicScaler)

	def addWidget(self, widget, x=0, y=0):
		widget.setParent(self)
		if isinstance(widget, (Card, Deck)):
			widget.rescale(self._current_scale * self.magicScaler)
		widget.move(x, y)
		widget.show()
		widget.raise_()
		return widget

class Deck(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()

		self.contents = [
		'Major01', 'Major02', 'Major03', 'Major04', 'Major05',
		'Major06', 'Major07', 'Major08', 'Major09', 'Major10',
		'Major11', 'Major12', 'Major13', 'Major14', 'Major15',
		'Major16', 'Major17', 'Major18', 'Major19', 'Major20',
		'Major21', 'Major00',
		'Cups01', 'Cups02', 'Cups03', 'Cups04', 'Cups05',
		'Cups06', 'Cups07', 'Cups08', 'Cups09', 'Cups10',
		'Cups11', 'Cups12', 'Cups13', 'Cups14',
		'Wands01', 'Wands02', 'Wands03', 'Wands04', 'Wands05',
		'Wands06', 'Wands07', 'Wands08', 'Wands09', 'Wands10',
		'Wands11', 'Wands12', 'Wands13', 'Wands14',
		'Swords01', 'Swords02', 'Swords03', 'Swords04', 'Swords05',
		'Swords06', 'Swords07', 'Swords08', 'Swords09', 'Swords10',
		'Swords11', 'Swords12', 'Swords13', 'Swords14',
		'Pents01', 'Pents02', 'Pents03', 'Pents04', 'Pents05',
		'Pents06', 'Pents07', 'Pents08', 'Pents09', 'Pents10',
		'Pents11', 'Pents12', 'Pents13', 'Pents14']

		self.deckImage = QtGui.QImage("Tarot_Image/Deck.png")
		self.deckEmptyImage = QtGui.QImage("Tarot_Image/DeckEmpty.png")
		self._base_img_w = self.deckImage.width()
		self._base_img_h = self.deckImage.height()

		self._drag_start = None

	def _current_pixmap(self):
		img = self.deckImage if len(self.contents)>0 else self.deckEmptyImage
		return QtGui.QPixmap.fromImage(img).scaled(
			self._img_size,
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation,
		)

	def rescale(self, scale):

		new_w = int(self._base_img_w * scale)
		new_h = int(self._base_img_h * scale)
		self._img_size = QtCore.QSize(new_w, new_h)

		self.setFixedSize(new_w,new_h)

		#new_x = int(self.x() * scale)
		#new_y = int(self.y() * scale)
		#self.move(new_x, new_y)
		
		self.update()

	#Draw a card on double click
	def mouseDoubleClickEvent(self, event):
		if event.button() == QtCore.Qt.LeftButton:
			if len(self.contents) > 0:
				parPos =  self.mapToParent(self.pos())
				self.parentWidget().addWidget(Card(self.contents.pop(0)), self.x()+self.width(), self.y())
				self.update()
	
	#Drag deck if clicked and dragged (next 3 methods)
	def mousePressEvent(self, event):
		if event.button() == QtCore.Qt.LeftButton:
			self._drag_start = event.position().toPoint()
			self.raise_()

	def mouseMoveEvent(self, event):
		if self._drag_start is not None:
			delta = event.position().toPoint() - self._drag_start
			self.move(self.pos() + delta)

	def mouseReleaseEvent(self, event):
		if event.button() == QtCore.Qt.LeftButton:
			self._drag_start = None
		elif event.button() == QtCore.Qt.RightButton:
			self.contextMenu(event.position().toPoint())

	def replace(self, card):
	#Destroy "card" and add its value to contents
		if (card._rotation > 90 and card._rotation < 270):
			self.contents.insert(0, "!" + card.name)
		else:
			self.contents.insert(0, card.name)
		card.deleteLater()

	def shuffle(self):
	#Randomize indexing of contents
		tempList = []		
		for item in self.contents:
			i = random.randint(0, len(tempList))
			if (random.randint(0, 100) < 49):
				if item[0] == "!":
					tempList.insert(i, item[1:])
				else:
					tempList.insert(i, "!"+item)
			else:
				tempList.insert(i, item)
		self.contents = tempList

	def paintEvent(self, event):
		pixmap = self._current_pixmap()
		painter =  QtGui.QPainter(self)
		painter.setRenderHint(QtGui.QPainter.Antialiasing)
		painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform)

		cx, cy = self.width() / 2, self.height() / 2
		
		img_x = (self.width() - pixmap.width())/2
		img_y = (self.height() - pixmap.height()) / 2

		painter.drawPixmap(int(img_x), int(img_y), pixmap)

	def contextMenu(self, position):
		menu = QtWidgets.QMenu(self)
		menu.addAction("Shuffle", self.shuffle())

		selectionMenu = QtWidgets.QMenu("Pull Card", self)
		majorMenu = QtWidgets.QMenu("Major Arcana", self)
		cupsMenu = QtWidgets.QMenu("Cups", self)
		pentsMenu = QtWidgets.QMenu("Pentacles", self)
		swordsMenu = QtWidgets.QMenu("Swords", self)
		wandsMenu = QtWidgets.QMenu("Wands", self)

		cloneCont = sorted(self.contents, key=lambda x: x[1:] if x.startswith("!") else x)
		for item in cloneCont:
			if item[0] == "!":
				cleanItem = item[1:]
			else:
				cleanItem = item

			if item.find("Wands") != -1:
				wandsMenu.addAction(CardDictionary.get(cleanItem), lambda i=item:self.pullCard(i))
			elif item.find("Cups") != -1:
				cupsMenu.addAction(CardDictionary.get(cleanItem), lambda i=item:self.pullCard(i))
			elif item.find("Pents") != -1:
				pentsMenu.addAction(CardDictionary.get(cleanItem), lambda i=item:self.pullCard(i))
			elif item.find("Swords") != -1:
				swordsMenu.addAction(CardDictionary.get(cleanItem), lambda i=item:self.pullCard(i))
			else:
				majorMenu.addAction(CardDictionary.get(cleanItem), lambda i=item:self.pullCard(i))

		selectionMenu.addMenu(majorMenu)
		selectionMenu.addMenu(cupsMenu)
		selectionMenu.addMenu(pentsMenu)
		selectionMenu.addMenu(swordsMenu)
		selectionMenu.addMenu(wandsMenu)

		menu.addMenu(selectionMenu)

		menu.exec(self.mapToGlobal(position))

	#Remove specific card from contents and spawn card face up
	def pullCard(self, cardName):
		self.contents.remove(cardName)
		if cardName[0] == "!":
			cardName = cardName[1:]
		parPos =  self.mapToParent(self.pos())
		newCard = self.parentWidget().addWidget(Card(cardName), self.x()+self.width(), self.y())
		newCard.flip()
		self.update()

	#Return all cards from table to deck then shuffle
	def resetDeck(self):

		pass

class Card(QtWidgets.QWidget):
	def __init__(self, name):
		super().__init__()
		self.name = name
		if self.name[0] == "!":
			self.name = self.name[1:]
			self._rotation = 180
		else:
			self._rotation = 0

		self.backImage = QtGui.QImage("Tarot_Image/Back.png")
		self.faceImage = QtGui.QImage("Tarot_Image/" + self.name + ".png")

		self.facing = 0
		#self.setPixmap(QtGui.QPixmap.fromImage(self.backImage))

		self._drag_start = None
		self._rot_start = None
		self._previous_rotation = 0

		self._base_img_w = self.backImage.width()
		self._base_img_h = self.backImage.height()
		self._img_size = QtCore.QSize(self._base_img_w, self._base_img_h)
		diag = int(math.ceil(math.ceil(math.sqrt(self._base_img_w**2+self._base_img_h**2))))
		self.setFixedSize(diag,diag)

	def rescale(self, scale):
		new_w = int(self._base_img_w * scale)
		new_h = int(self._base_img_h * scale)
		self._img_size = QtCore.QSize(new_w, new_h)

		diag = int(math.ceil(math.sqrt(new_w**2+new_h**2)))
		self.setFixedSize(diag,diag)

		#new_x = int(self.x() * scale * (9/2))
		#new_y = int(self.y() * scale * (9/2))
		#self.move(new_x, new_y)
		
		self.update()

	def _current_pixmap(self):
		img = self.faceImage if self.facing == 1 else self.backImage
		return QtGui.QPixmap.fromImage(img).scaled(
			self._img_size,
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation,
		)
	def _point_in_card(self, pos: QtCore.QPoint) -> bool:
		#Test if mouse event is actually over this card or in transparent region
		cx, cy = self.width() / 2, self.height() / 2
		img_w, img_h = self._img_size.width(), self._img_size.height()

		#Translate pos to card-centre-relative coords, then un-rotate it
		dx = pos.x() - cx
		dy = pos.y() - cy
		rad = math.radians(-self._rotation)
		local_x = dx * math.cos(rad) - dy * math.sin(rad)
		local_y = dx * math.sin(rad) + dy * math.cos(rad)

		# Now check if it falls within the unrotated card rectangle
		return (abs(local_x) <= img_w / 2) and (abs(local_y) <= img_h / 2)

	def _forward_event_to_below(self, event):
	#Find topmost sibling udner cursor that accepts the event
		pos_in_parent = self.mapToParent(event.position().toPoint())

		for sibling in reversed(self.parent().children()):
			if sibling is self or not isinstance(sibling, QtWidgets.QWidget):
				continue
			if not sibling.isVisible():
				continue
			pos_in_sibling = sibling.mapFromParent(pos_in_parent)

			if isinstance(sibling, Card):
				if not sibling._point_in_card(pos_in_sibling):
					continue
			else:
				if not sibling.rect().contains(pos_in_sibling):
					continue

			new_event = QtGui.QMouseEvent(
				event.type(),
				QtCore.QPointF(pos_in_sibling),
				event.globalPosition(),
				event.button(),
				event.buttons(),
				event.modifiers(),
			)
			QtWidgets.QApplication.sendEvent(sibling, new_event)
			return

		event.ignore()		

	def _check_for_deck(self, event):
		pos_in_parent = self.mapToParent(event.position().toPoint())
		for sibling in reversed(self.parent().children()):
			if isinstance(sibling, Deck):
				pos_in_sibling = sibling.mapFromParent(pos_in_parent)
				if sibling.rect().contains(pos_in_sibling):
					sibling.replace(self)

	#Flip the card if doubleclicked
	def mouseDoubleClickEvent(self, event):
		if not self._point_in_card(event.position().toPoint()):
			self._forward_event_to_below(event)
			return	
		if event.button() == QtCore.Qt.LeftButton:
			self.flip()

	#Handle dragging on left click and rotation on right click (next 3 methods)
	def mousePressEvent(self, event):
		if not self._point_in_card(event.position().toPoint()):
			self._forward_event_to_below(event)
			return
		if event.button() == QtCore.Qt.LeftButton:
			self._drag_start = event.position().toPoint()
			self.raise_()
			self.grabMouse()
		elif event.button() == QtCore.Qt.RightButton:
			self._rot_start = event.position().toPoint()
			self._previous_rotation = self._rotation
			self.raise_()	
			self.grabMouse()

	def mouseMoveEvent(self, event):
		if self._drag_start is not None:
			delta = event.position().toPoint() - self._drag_start
			self.move(self.pos() + delta)
		elif self._rot_start is not None:
			center = QtCore.QPointF(self.width()/2, self.height()/2)
			line_start = QtCore.QLineF(center, self._rot_start)
			line_current = QtCore.QLineF(center, event.position())
			delta_angle = line_start.angleTo(line_current)			
			self._rotation = (self._previous_rotation - delta_angle) % 360
			self.update()
		elif not self._point_in_card(event.position().toPoint()):
			self._forward_event_to_below(event)
			return

	def mouseReleaseEvent(self, event):
		if event.button() == QtCore.Qt.LeftButton:
			self._drag_start = None
			self._check_for_deck(event)
		elif event.button() == QtCore.Qt.RightButton:
			self._rot_start = None
		self.releaseMouse()
	
	def paintEvent(self, event):
		pixmap = self._current_pixmap()
		painter =  QtGui.QPainter(self)
		painter.setRenderHint(QtGui.QPainter.Antialiasing)
		painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform)

		cx, cy = self.width() / 2, self.height() / 2
		
		img_x = (self.width() - pixmap.width())/2
		img_y = (self.height() - pixmap.height()) / 2

		painter.translate(cx, cy)
		painter.rotate(self._rotation)
		painter.translate(-cx, -cy)
		painter.drawPixmap(int(img_x), int(img_y), pixmap)

	def flip(self):
	#Alternate between face and back
		self.facing = 1 - self.facing
		self.update()

if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	
	gameWindow = mainWindow()
	
	#We will need to set the card and deck size to ~2/9 the screen height assuming oriented in landscape
	gameWindow.resize(1280,720)
	gameWindow.show()

	#

	sys.exit(app.exec())
