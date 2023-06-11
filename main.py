import multiprocessing
import json
import websocket
import profit
import time

with open ('list_chains.txt', 'r') as list_ch:
    _list = json.load (list_ch)

with open ('dict.txt', 'r') as a:
    _dict = json.load (a)

def transfer (_dict):
    global queue_flag, queue_dict
    queue_flag.get ()
    queue_dict.put (_dict)


def on_data(wsapp, message, data_type, flag):
    message = json.loads(message)
    if message['s'] in _dict:
        _dict[message['s']] = [message['a'], message['b'], message ['A'], message['B']]  
    if queue_flag.qsize () != 0:
        transfer (_dict)

def on_ping(wsapp, message):
        print("Got a ping! A pong reply has already been automatically sent.")

def on_pong(wsapp, message):
        print("Got a pong! No need to respond")

def on_error(wsapp, error):
        print(error)

def on_close(wsapp, close_status_code, close_msg):
        print("### closed ###", close_status_code, ' ', close_msg)
        global _dict
        for key in _dict:
            _dict[key] = [-1,-1]

def run():     
    #try:
    wsapp = websocket.WebSocketApp("wss://stream.binance.com:9443/ws/!bookTicker",
                                    on_ping=on_ping,
                                    on_data=on_data,
                                    on_error=on_error,
                                    on_close=on_close)

    
    wsapp.run_forever()




if __name__ == "__main__":
    queue_flag = multiprocessing.Queue(1)
    queue_dict = multiprocessing.Queue (1)
    web_process = multiprocessing.Process(target=profit.run, args=(queue_flag, queue_dict,))
    web_process.start()
    run ()



