import pickle
import zmq
from threading import Thread

class BigBrother:
    def __init__(self, host="localhost", ports=(6666, 6667)):
         # Initialisation des objets nécessaires pour la communication ZeroMQ
        self.context = zmq.Context()
        self.sub = self.context.socket(zmq.SUB)
        self.sub.connect(f"tcp://{host}:{ports[1]}")
        self.sub.setsockopt_string(zmq.SUBSCRIBE, "")
        self.req = self.context.socket(zmq.REQ)
        self.req.connect(f"tcp://{host}:{ports[0]}")
        self.running = True

    def monitor(self):
    # Fonction principale qui gère l'espionnage des messages et des commandes    
        def spy_broadcast():
            while self.running:
                try:
                    # Recevoir un message et tenter de le désérialiser avec pickle
                    msg = pickle.loads(self.sub.recv())
                    if msg["type"] == "message":
                        print(f"[SPY] {msg['nick']}: {msg['message']}")
                except: pass

        def spy_commands():
                # Envoie une requête "list" pour obtenir la liste des utilisateurs            
            while self.running:
                self.req.send(pickle.dumps({"type":"list"}))
                users = pickle.loads(self.req.recv())["response"]
                print(f"[USERS] {', '.join(users)}" if users != "ko" else "")
                __import__('time').sleep(5)
        # Crée et lance deux threads pour espionner les messages et les commandes simultanément
        Thread(target=spy_broadcast).start()
        Thread(target=spy_commands).start()

    def run(self):
        print("Ctrl+C to stop")
        self.monitor()
        try:
        # Boucle infinie pour maintenir l'application en fonctionnement jusqu'à ce que l'utilisateur interrompt 
            while self.running: __import__('time').sleep(1)
        except KeyboardInterrupt: 
            self.running = False
            self.context.destroy()

if __name__ == "__main__":
    BigBrother().run()
