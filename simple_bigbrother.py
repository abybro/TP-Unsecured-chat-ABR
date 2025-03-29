import pickle
import zmq
from threading import Thread

class BigBrother:
    def __init__(self, host="localhost", ports=(6666, 6667)):
        self.context = zmq.Context()
        self.sub = self.context.socket(zmq.SUB)
        self.sub.connect(f"tcp://{host}:{ports[1]}")
        self.sub.setsockopt_string(zmq.SUBSCRIBE, "")
        self.req = self.context.socket(zmq.REQ)
        self.req.connect(f"tcp://{host}:{ports[0]}")
        self.running = True

    def monitor(self):
        def spy_broadcast():
            while self.running:
                try:
                    msg = pickle.loads(self.sub.recv())
                    if msg["type"] == "message":
                        print(f"[SPY] {msg['nick']}: {msg['message']}")
                except: pass

        def spy_commands():
            while self.running:
                self.req.send(pickle.dumps({"type":"list"}))
                users = pickle.loads(self.req.recv())["response"]
                print(f"[USERS] {', '.join(users)}" if users != "ko" else "")
                __import__('time').sleep(5)

        Thread(target=spy_broadcast).start()
        Thread(target=spy_commands).start()

    def run(self):
        print("Ctrl+C to stop")
        self.monitor()
        try:
            while self.running: __import__('time').sleep(1)
        except KeyboardInterrupt: 
            self.running = False
            self.context.destroy()

if __name__ == "__main__":
    BigBrother().run()
