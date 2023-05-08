import tkinter as tk

from numpy import pad

import onpc_trans

import zmq, signal, sys, time, pmt
import numpy as np

class GUI:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Babel Protocol Transmitter")
        # self.window.resizable(width=False, height=False)

        self.frm_protocol = tk.Frame(master=self.window)
        self.frm_send = tk.Frame(master=self.window)
        self.frm_actual_send = tk.Frame(master=self.window)
        self.frm_protocol.grid(row=0)
        self.frm_send.grid(row=1)
        self.frm_actual_send.grid(row=2)
        self.lbl_center_freq = tk.Label(master=self.frm_protocol,text="Center frequency (MHz)")
        self.lbl_chip_length = tk.Label(master=self.frm_protocol, text="Chip Length (ms)")
        self.lbl_duration = tk.Label(master=self.frm_send, text="Duration (Hrs)")
        self.lbl_bandwidth = tk.Label(master=self.frm_send, text="Bandwidth (MHz)")
        self.lbl_freq = tk.Label(master=self.frm_send, text="Freqency (GHz)")
        self.lbl_decimal = tk.Label(master=self.frm_send, text=".")
        self.lbl_iterations = tk.Label(master=self.frm_actual_send, text="Iterations")
        self.lbl_itraspace = tk.Label(master=self.frm_actual_send, text="Intra symbol spacing")
        self.lbl_time_between = tk.Label(master=self.frm_actual_send, text="Time Between (ms)")
        self.lbl_tx_gain = tk.Label(master=self.frm_protocol,text="TX Gain")

        
        self.ent_tx_gain = tk.Entry(master=self.frm_protocol,width=6)
        self.ent_tx_gain.insert(0,"28")
        self.ent_center_freq = tk.Entry(master=self.frm_protocol, width=6)
        self.ent_center_freq.insert(0,"2437")
        self.opt_chip_length = ["1","2","3","4","5","6","7","8","9","10"]
        self.opt_duration = ["0.5","1","2","3","4","5","6","8","12","18","24"]
        self.opt_freq_first = ["0","1","2","3","4","5","6","7","8","9","10"]
        self.opt_freq = ["0","1","2","3","4","5","6","7","8","9"]
        self.opt_bandwith = ["10","20","40","80","160"]
        self.dict_bandwidth = {"10":"0","20":"1","40":"2","80":"3","160":"4"}
        self.dict_duration = {"0.5":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"-0","8":"-1","12":"-2","18":"-3","24":"-5"}
        self.dict_freq = {"0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"-0","7":"-1","8":"-2","9":"-3","10":"-5"}
        self.stv_chip_length = tk.StringVar(self.frm_protocol,self.opt_chip_length[4])
        self.stv_duration = tk.StringVar(self.frm_send, self.opt_duration[0])
        self.strv_bandwidth = tk.StringVar(self.frm_send, self.opt_bandwith[0])
        self.strv_freq_first = tk.StringVar(self.frm_send,self.opt_freq_first[2])
        self.strv_freq_second = tk.StringVar(self.frm_send, self.opt_freq[4])
        self.strv_freq_third = tk.StringVar(self.frm_send, self.opt_freq[3])
        self.strv_freq_fourth = tk.StringVar(self.frm_send, self.opt_freq[7])
        self.optm_chip_length = tk.OptionMenu(self.frm_protocol,self.stv_chip_length, *self.opt_chip_length)
        self.optm_duration = tk.OptionMenu(self.frm_send, self.stv_duration, *self.opt_duration)
        self.optm_bandwidth = tk.OptionMenu(self.frm_send, self.strv_bandwidth, *self.opt_bandwith)
        self.optm_freq_first = tk.OptionMenu(self.frm_send, self.strv_freq_first, *self.opt_freq_first)
        self.optm_freq_second = tk.OptionMenu(self.frm_send, self.strv_freq_second, *self.opt_freq)
        self.optm_freq_third = tk.OptionMenu(self.frm_send, self.strv_freq_third, *self.opt_freq)
        self.optm_freq_fourth = tk.OptionMenu(self.frm_send, self.strv_freq_fourth, *self.opt_freq)


        self.btn_gnuradio_toggle = tk.Button(self.frm_protocol, text="Start Radio", command=self.start_stop_transmitter)
        self.btn_send = tk.Button(self.frm_actual_send, text="SEND", command=self.send_protocol)

        self.ent_intraspacing = tk.Entry(master=self.frm_actual_send,width=6)
        self.ent_iterations = tk.Entry(master=self.frm_actual_send, width=4)
        self.ent_time_between = tk.Entry(master=self.frm_actual_send, width=6)
        self.ent_iterations.insert(0,"1")
        self.ent_time_between.insert(0,"0")
        self.ent_intraspacing.insert(0,"0")
        
        self.lbl_center_freq.grid(row=0, column=0)
        self.ent_center_freq.grid(row=0,column=1,padx=10)
        self.lbl_chip_length.grid(row=0,column=2)
        self.optm_chip_length.grid(row=0,column=3,padx=10)
        self.lbl_tx_gain.grid(row=0,column=4)
        self.ent_tx_gain.grid(row=0, column=5, padx=10)
        self.btn_gnuradio_toggle.grid(row=0,column=6)

        self.lbl_duration.grid(row=0,column=0)
        self.optm_duration.grid(row=0,column=1,padx=5)
        self.lbl_freq.grid(row=0,column=2)
        self.optm_freq_first.grid(row=0,column=3)
        self.lbl_decimal.grid(row=0,column=4)
        self.optm_freq_second.grid(row=0,column=5)
        self.optm_freq_third.grid(row=0,column=6)
        self.optm_freq_fourth.grid(row=0,column=7,padx=10)
        self.lbl_bandwidth.grid(row=0,column=8)
        self.optm_bandwidth.grid(row=0,column=9)

        self.lbl_iterations.grid(row=0, column=0)
        self.ent_iterations.grid(row=0,column=1, padx=10)
        self.lbl_itraspace.grid(row=0, column=2)
        self.ent_intraspacing.grid(row=0, column=3, padx=10)
        self.lbl_time_between.grid(row=0, column=4)
        self.ent_time_between.grid(row=0,column=5, padx=10)
        self.btn_send.grid(row=0, column=6)

        
        self.transmitter = None
        self.context = None
        self.socket = None
        self.send_msgs = [
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
        self.new_send_msg_lst = [[int(x, 16) for x in msg.split(",")] for msg in self.send_msgs]
        self.metadata = {
            "pdu_num": 0,
            "time_type": "uhd_time_tuple",
            "burst_time": (0, 0.0),
        }
        self.pdu_lst = [
            pmt.serialize_str(
                pmt.cons(
                    pmt.to_pmt(self.metadata),
                    pmt.to_pmt(
                        np.array(
                            msg,
                            dtype=np.uint8,
                        )
                    ),
                )
            )
            for msg in self.new_send_msg_lst
        ]

    def serializer(self, numbers):
        msg = []
        print(numbers)
        for n in numbers:
            if "-" in n:
                n = int(n) - 1
            else:
                n = int(n)
            print(n)
            msg += self.new_send_msg_lst[n]
        return pmt.serialize_str(
            pmt.cons(
                pmt.to_pmt(self.metadata),
                pmt.to_pmt(
                    np.array(
                        msg,
                        dtype=np.uint8,
                    )
                ),
            )
        )

    def start_stop_transmitter(self):
        if self.socket is None:
            self.btn_gnuradio_toggle["text"] = "Stop Radio"
            self.transmitter = onpc_trans.onpc_trans(int(self.stv_chip_length.get())*0.001)
            self.transmitter.set_gain(float(self.ent_tx_gain.get()))
            self.transmitter.set_center_freq(int(self.ent_center_freq.get())*1000000)
            self.transmitter.start()
            self.context = zmq.Context()
            self.socket = self.context.socket(zmq.PUB)
            self.socket.bind("tcp://127.0.0.1:5557")
        else:
            self.btn_gnuradio_toggle["text"] = "Start Radio"
            self.transmitter.stop()
            self.transmitter.wait()
            self.transmitter = None
            self.socket.close()
            self.context.destroy()
            self.socket = None
            self.context = None
    
    def send_protocol(self):
        # Get the protocol information from GUI
        number_of_times = int(self.ent_iterations.get())
        time_to_sleep = float(self.ent_time_between.get())*.001
        intra = int(self.ent_intraspacing.get())*.001
        nums = ["-4", "-4", self.dict_duration[self.stv_duration.get()], self.dict_freq[self.strv_freq_first.get()], self.dict_freq[self.strv_freq_second.get()], self.dict_freq[self.strv_freq_third.get()], self.dict_freq[self.strv_freq_fourth.get()], self.dict_bandwidth[self.strv_bandwidth.get()] ]
        if intra > 0:
            # do individual sends, else do the bulk send
            for i in range(number_of_times):
                for j in range(8): # packet size -- 2 pilots and 6 for information
                    self.socket.send(self.pdu_lst[int(nums[j]) if "-" not in nums[j] else int(nums[j]) - 1])
                    time.sleep(intra)  # Intra symbol sleeping
                time.sleep(time_to_sleep)  # Inter packet sleeping
            return

        # Serialize the protocol
        packet = self.serializer(nums)

        # Send the packet x number of times from the GUI
        for i in range(number_of_times):
            self.socket.send(packet)
            time.sleep(time_to_sleep)
        return

    def start(self):
        self.window.mainloop()

def main():
    gui = GUI()
    gui.start()

if __name__ == "__main__":
    main()