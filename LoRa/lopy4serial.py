import serial
from decoders import dynamic_decoder

if __name__ == "__main__":
    decoder = dynamic_decoder()

    # f = np.fromfile(open("./onpc_remake_live/rx_test_5801_long.f32"), dtype=np.float32)

    # print(len(f))
    # symbols = []
    # stt = t.time()
    # for element in range(len(f)):
    #     symbols.append(decoder.add_val(int(f[element]), element))
    # end = t.time()
    # print(end - stt)

    ser = serial.Serial(port="/dev/ttyUSB0", baudrate=115200)

    while True:
        line = ser.readline()
        try:
            val = int(line)
            decoder.add_val(val, 0)
            # if val > -90:
            #     print(val)
        except:
            print("Error detected. Passing",line)
        # print(val)
