#!/bin/bash

sudo rm /var/run/olsrd-ipv6.lock
sudo olsrd -f /etc/olsrd/olsrd$1.conf 
