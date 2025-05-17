from communication.websocket_client import WebSocketClient


ws = WebSocketClient("ws://localhost:4545", "haykos")
ws.commencer_connexion()



