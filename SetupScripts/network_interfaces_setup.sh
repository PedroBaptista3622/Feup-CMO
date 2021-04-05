#!/bin/bash

echo 0 > /proc/sys/net/ipv6/conf/h$1-eth0/accept_ra
echo 1 > /proc/sys/net/ipv6/conf/h$1-eth0/forwarding
