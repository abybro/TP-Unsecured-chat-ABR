import msgpack
import logging
from simple_server import SimpleServer

class RogueServer(SimpleServer):
    def __init__(self, recv_port: int, broadcast_port: int) -> None:
        super().__init__(recv_port, broadcast_port)
        self._serial_function = msgpack.packb
        self._deserial_function = msgpack.unpackb
        logging.basicConfig(level=logging.DEBUG)

    def on_message(self, packet: bytes, frame: dict):
        """ Intercepte et modifie les messages avant de les renvoyer """
        if frame["nick"] not in self._clients:
            self._log.error(f"Client '{frame['nick']}' n'est pas connecté, impossible d'envoyer le message.")
            return None, self._serial_function({"response": "ko"})

        # Log des messages avant modification
        logging.info(f"Message avant modification : {frame.get('message', '')}")

        try:
            if "message" in frame:
                # Modifier le message en clair
                original_message = frame["message"]
                modified_message = " Ce message a été altéré par le serveur malveillant ! "

                # Remplacer uniquement la partie en clair du message
                frame["message"] = modified_message

            # Sérialise le message modifié sans altérer la structure binaire chiffrée
            modified_packet = self._serial_function(frame)
            logging.info(f"Message après modification : {modified_message}")
            
            return modified_packet, self._serial_function({"response": "ok"})
        
        except Exception as e:
            # Gère les erreurs et log les problèmes
            self._log.error(f"Erreur lors de la modification du message : {e}")
            return None, self._serial_function({"response": "ko"})

if __name__ == "__main__":
    server = RogueServer(6666, 6667)

    try:
        logging.info("RogueServer en marche... Attente de messages...")
        while True:
            server.update()
    except KeyboardInterrupt:
        logging.info("Extinction du serveur malveillant...")
    finally:
        server.close()
