import onpc_trans

import zmq, signal, sys, time, pmt
import numpy as np


transmitter = onpc_trans.onpc_trans()


def sig_handler(sig=None, frame=None):
    transmitter.stop()
    transmitter.wait()
    sys.exit(0)


signal.signal(signal.SIGINT, sig_handler)
signal.signal(signal.SIGTERM, sig_handler)

transmitter.start()
print("initializing")
# time.sleep(5)  # time to initialize
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:5557")
time.sleep(0.25)  # time for socket to initialize


    
    
    
    
    

# send_msgs = ["0x7E,0xD1,0x0B,0x2A,0x4F,0x06,0xE6,0x3A",]
send_msgs = [
    "0x7e,0xac,0xdd,0xa4,0xe2,0xf2,0x8c,0x20",
    "0x7e,0x08,0x62,0x9e,0x8e,0x4b,0x76,0x6a",
    "0x7E,0xD1,0x0B,0x2A,0x4F,0x06,0xE6,0x3A",
    "0x7e,0xb8,0xce,0xc1,0xe4,0xa9,0xa1,0x16",
    "0x7e,0x83,0x84,0x8d,0x96,0xbb,0xcc,0x54",
    "0x7e,0x54,0x67,0xba,0xd3,0x62,0x43,0x82",
    "0x01,0xab,0x98,0x45,0x2c,0x9d,0xbc,0x54",
    "0x01,0x7c,0x7b,0x72,0x69,0x44,0x33,0xab",
    "0x01,0x47,0x31,0x3e,0x1b,0x56,0x5e,0xe9",
    "0x01,0x2e,0xf4,0xd5,0xb0,0xf9,0x19,0xc5",
    "0x01,0xf7,0x9d,0x61,0x71,0xb4,0x89,0x95",
    "0x01,0x53,0x22,0x5b,0x1d,0x0d,0x73,0xdf",
    ]
new_send_msg_lst = [[int(x, 16) for x in msg.split(",")] for msg in send_msgs]
metadata = {
    "pdu_num": 0,
    "time_type": "uhd_time_tuple",
    "burst_time": (0, 0.0),
}
pdu_lst = [
    pmt.serialize_str(
        pmt.cons(
            pmt.to_pmt(metadata),
            pmt.to_pmt(
                np.array(
                    msg,
                    dtype=np.uint8,
                )
            ),
        )
    )
    for msg in new_send_msg_lst
]
def serializer(numbers):
    msg = []
    print(numbers)
    for n in numbers:
        if "-" in n:
            n = int(n) - 1
        else:
            n = int(n)
        print(n)
        msg += new_send_msg_lst[n]
    return pmt.serialize_str(
        pmt.cons(
            pmt.to_pmt(metadata),
            pmt.to_pmt(
                np.array(
                    msg,
                    dtype=np.uint8,
                )
            ),
        )
    )
# pdu = pmt.cons(
#     pmt.to_pmt(metadata),
#     pmt.to_pmt(
#         np.array(
#             new_send_msg,
#             dtype=np.uint8,
#         )
#     ),
# )
# pdu_str = pmt.serialize_str(pdu)
try:
    # print("Enter a number between 0-5 or (-0 - -5 for inverse symbols) for which symbol to send (q to quit) or a space delimited list of symbols, b to rapid fire all the symbols: ")
    print("Frequency:iterations:pause \"space demlimited symbol sequence\"")
    print("Example: 2437:2:1 -5 -5 0 2 4 4 1")
    num = input().split(" ")
    while "q" not in num:
        # Process frequency number to send and spacing first
        actions = num.pop(0).split(":")
        transmitter.set_center_freq(int(actions[0])*(1000000))
        print("transmitting "+actions[1]+" at an interval of "+actions[2]+" on "+str(transmitter.get_center_freq())+"Hz")
        for i in range(int(actions[1])):
            socket.send(serializer(num))
            time.sleep(int(actions[2]))
        # if "b" in num:
        #     print("sending burst")
        #     for packet in pdu_lst:
        #         socket.send(packet)
        #         time.sleep(.4)
        # else:
            # print("sending", send_msgs[int(num)])
            # for i in num:
            #     if "-" in i:
            #         i = int(i)-1
                # socket.send(pdu_lst[int(i)])
            # socket.send(serializer(num))
        # print("Enter a number between 0-5 or (-0 - -5 for inverse symbols) for which symbol to send (q to quit) or a space delimited list of symbols, b to rapid fire all the symbols: ")
        print("Frequency:iterations:pause \"space demlimited symbol sequence\"")
        num = input().split(" ")
except:
    print("wrong command, exiting")
finally:
    time.sleep(0.25)
    print("shutting down transmitter")
    transmitter.stop()
    transmitter.wait()
