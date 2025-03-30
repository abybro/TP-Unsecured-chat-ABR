import msgpack  # msgpack pour encoder et décoder les données
import logging
from simple_server import SimpleServer

class AEServer(SimpleServer):
    def __init__(self, recv_port: int, broadcast_port: int) -> None:
        super().__init__(recv_port, broadcast_port)  # Initialisation avec les bons ports
        
        # Définition des fonctions de sérialisation et de désérialisation
        self._serial_function = msgpack.packb  # Transforme les objets en format binaire compact
        self._deserial_function = msgpack.unpackb  # Restaure les objets depuis le format bianire

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)  # Activation des logs en mode debug
    server = AEServer(6666, 6667)  # Lance le serveur
    try:
        while True:
            server.update()  #Maintient le serveur en fonctionnement
    except KeyboardInterrupt:
        logging.info("Arrêt du serveur...")
    finally:
        server.close()  # Ferme proprement le serveur