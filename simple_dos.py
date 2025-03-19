import zmq
import time

# Créer un contexte et un socket de type PUSH pour envoyer des messages
context = zmq.Context()
socket = context.socket(zmq.PUSH)

# Connexion au serveur
socket.connect("tcp://localhost:5555")

print("Envoi de messages pour saturation du serveur...")
while True:
    try:
        socket.send_string("Message flood")  # Envoyer un message
        time.sleep(0.01)  # Envoi rapide des messages pour saturer le serveur
    except zmq.ZMQError as e:
        print(f"Erreur ZMQ: {e}")
    except KeyboardInterrupt:
        print("Arrêt du flood.")
        break
