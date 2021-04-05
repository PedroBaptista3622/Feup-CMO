#!/bin/bash

sudo ifconfig h5-eth0 inet6 add 3000::254/64
sudo route -A inet6 add 2021:0:0::/64 gw 3000::
