import blocks

connectedClients = {}

class ClientData(object):
	"""docstring for ClientData"""
	def __init__(self, ipAddress, segaId, handle):
		self.ipAddress = ipAddress
		self.segaId = segaId
		self.handle = handle
	def getHandle(self):
		return self.handle
	def setHandle(self, handle):
		self.handle = handle

def addClient(handle):
	connectedClients[handle.playerId] = ClientData(handle.transport.getPeer().host, handle.myUsername, handle)
	print('[Clients] Registered client %s (ID:%i) in online clients' % (handle.myUsername, handle.playerId))

def removeClient(handle):
	print("[Clients] Removing client %s (ID:%i) from online clients" % (handle.myUsername, handle.playerId))
	del connectedClients[handle.playerId]

def populateData(handle):
	cData = connectedClients[handle.playerId]
	cData.handle = handle
	handle.myUsername = cData.segaId
	handle.peer.myUsername = cData.segaId
	if handle.transport.getHost().port in blocks.blockList:
		bName = blocks.blockList[handle.transport.getHost().port][1]
	else:
		bName = None
	print("[ShipProxy] %s has successfully changed blocks to %s!" % (handle.myUsername, bName))
	handle.loaded = True
