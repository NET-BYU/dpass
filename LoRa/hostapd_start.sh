#!/bin/bash
echo "killing still open hostapd processes"
sudo pkill hostapd
echo "killing wpa_supplicant process"
sudo pkill wpa_supplicant
echo "configure wlp2s0 interface"
sudo ifconfig wlp2s0 up
sudo ifconfig wlp2s0 10.0.0.1 netmask 255.255.255.0
echo "restarting dnsmasq service"
sudo systemctl restart dnsmasq
echo "starting soft ap"
sudo hostapd /etc/hostapd/hostapd.conf
