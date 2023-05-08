#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.9.2.0

from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio import zeromq
import numpy as np
import pdu_utils




class onpc_trans(gr.top_block):

    def __init__(self,chip_length):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)

        ##################################################
        # Variables
        ##################################################
        # self.symbol_len = symbol_len = 5000e-6
        self.symbol_len = symbol_len = chip_length
        self.samp_rate = samp_rate = 10e6
        self.samp_per_symbol = samp_per_symbol = int(samp_rate*symbol_len)
        self.metadata = metadata = {"pdu_num": 0,"time_type": "uhd_time_tuple","burst_time": (0,.0),}
        self.gain = gain = .8
        self.center_freq = center_freq = 2437e6

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_sub_msg_source_0_0 = zeromq.sub_msg_source('tcp://127.0.0.1:5557', 100, False)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
            ",".join(('addr=192.168.0.11', '')),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
            '',
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        # No synchronization enforced.

        self.uhd_usrp_sink_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        # self.uhd_usrp_sink_0.set_normalized_gain(gain, 0)
        self.uhd_usrp_sink_0.set_gain(gain,0)
        self.rational_resampler_xxx_1_0 = filter.rational_resampler_fff(
                interpolation=int(samp_per_symbol),
                decimation=1,
                taps=firdes.low_pass(1, samp_rate, 25000,1e6),
                fractional_bw=0)
        self.pdu_utils_pdu_to_bursts_X_0 = pdu_utils.pdu_to_bursts_b(pdu_utils.EARLY_BURST_BEHAVIOR__APPEND, 64)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_moving_average_xx_1 = blocks.moving_average_ff(int(samp_per_symbol), 1, 10000, 1)
        self.blocks_message_debug_0 = blocks.message_debug(True)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.zeromq_sub_msg_source_0_0, 'out'), (self.blocks_message_debug_0, 'print'))
        self.msg_connect((self.zeromq_sub_msg_source_0_0, 'out'), (self.pdu_utils_pdu_to_bursts_X_0, 'bursts'))
        self.connect((self.blocks_float_to_complex_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.blocks_moving_average_xx_1, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.rational_resampler_xxx_1_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_uchar_to_float_0, 0))
        self.connect((self.pdu_utils_pdu_to_bursts_X_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.blocks_moving_average_xx_1, 0))


    def get_symbol_len(self):
        return self.symbol_len

    def set_symbol_len(self, symbol_len):
        self.symbol_len = symbol_len
        self.set_samp_per_symbol(int(self.samp_rate*self.symbol_len))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samp_per_symbol(int(self.samp_rate*self.symbol_len))
        self.rational_resampler_xxx_1_0.set_taps(firdes.low_pass(1, self.samp_rate, 25000,1e6))
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

    def get_samp_per_symbol(self):
        return self.samp_per_symbol

    def set_samp_per_symbol(self, samp_per_symbol):
        self.samp_per_symbol = samp_per_symbol
        self.blocks_moving_average_xx_1.set_length_and_scale(int(self.samp_per_symbol), 1)

    def get_metadata(self):
        return self.metadata

    def set_metadata(self, metadata):
        self.metadata = metadata

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.uhd_usrp_sink_0.set_gain(self.gain, 0)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.uhd_usrp_sink_0.set_center_freq(self.center_freq, 0)




def main(top_block_cls=onpc_trans, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
