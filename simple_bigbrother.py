import zmq

# Créer un contexte et un socket de type SUB (abonnement)
context = zmq.Context()
socket = context.socket(zmq.SUB)

# Connecter au serveur (adresse et port à adapter)
socket.connect("tcp://localhost:5555")

# S'abonner à tous les messages (vide signifie tout écouter)
socket.setsockopt_string(zmq.SUBSCRIBE, '')

print("Écoute des messages...")
while True:
    try:
        message = socket.recv_string()  # Recevoir un message
        print(f"Message intercepté: {message}")  # Afficher le message reçu
    except zmq.ZMQError as e:
        print(f"Erreur ZMQ: {e}")
    except KeyboardInterrupt:
        print("Arrêt du programme.")
        break
