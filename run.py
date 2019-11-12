from threading import Thread

from compute import worker1, worker2

from parking_state import Settings

Global = Settings()


if __name__ == '__main__':
    # Register Workers & Spawn

    Thread(target=worker1.worker1).start()
    Thread(target=worker2.worker2).start()


    print(Global.device.state)






