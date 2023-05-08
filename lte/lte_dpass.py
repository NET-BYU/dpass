from reprlib import recursive_repr
import time
import zmq
import struct
import subprocess
import decoders
from psutil import Process

high_five = struct.Struct("h")
upss = decoders.dynamic_decoder2(samples_per_chip=5)
symbols_caught = []
switch = True

print("Initializing")
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, b"")
socket.connect("tcp://localhost:2003")
proc = subprocess.Popen(["sudo", "/home/jonbackman/srsRAN/build/srsue/src/srsue", "/home/jonbackman/.config/srsran/ue.conf"],
                        shell=False)  # starts srsRAN UE
time.sleep(0.25)


while True:
    try:
        string = socket.recv()
        string = high_five.unpack(string)[0]
        symbol = upss.add_val(string)
        if symbol is not None:  # we found a symbol
            print(symbol)
            symbols_caught.append(symbol[0])
            if len(symbols_caught) > 7:  # full buffer and ready to check for known symbol
                if switch and symbols_caught == ["-4", "-4", "0", "2", "4", "3", "-1", "0"]:
                    print("protocol enacted, shutting down")
                    socket.close()
                    context.destroy()
                    parent = Process(proc.pid)
                    for child in parent.children(recursive=True):
                        child.kill()
                    parent.kill()
                    break
                symbols_caught.pop(0)

    except KeyboardInterrupt:
        print("\nending")

        socket.close()
        context.destroy()
        break
print("\ndone")
