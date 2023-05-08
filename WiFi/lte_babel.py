import time
import zmq
import struct
import subprocess
import decoders

high_five = struct.Struct("h")
babel = decoders.dynamic_decoder2(samples_per_chip=5)
symbols_caught = []
switch = False

print("initializing")
# time.sleep(5)  # time to initialize
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, b"")
socket.connect("tcp://localhost:2003")
proc = subprocess.Popen(["~/PATH_TO_EXECUTABLE"], shell=False)  # starts srsRAN UE
time.sleep(0.25)


while True:
    try:
        string = socket.recv()
        string = high_five.unpack(string)[0]
        symbol = babel.add_val(string)
        if symbol is not None:  # we found a symbol
            print(symbol)
            # print(test)
            symbols_caught.append(symbol[0])
            if len(symbols_caught) > 7: # full buffer and ready to check for known symbol
                symbols_caught.pop(0)
                if switch and symbols_caught == ["-4", "-4", "0", "2","4","3","-1","0"]:
                    print("protocol enacted, shutting down")
                    socket.close()
                    context.destroy()
                    proc.terminate()  # Kills the srsRAN UE
                    break
                symbols_caught.pop(0)
                                        # os.system("nmcli device wifi rescan")
                                        # with open("network_config.txt", "r") as nc:
                                        #     ssid = nc.readline().rstrip()
                                        #     password = nc.readline().rstrip()
                                        # os.system(f"nmcli dev wifi connect \"{ssid}\" password {password}")
                                        # self.scanner.stop()
                                        
        # time.sleep(1)
    except KeyboardInterrupt:
        print("\nending")

        socket.close()
        context.destroy()
        break
print("\ndone")
