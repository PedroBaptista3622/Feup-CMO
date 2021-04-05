#!/bin/bash

sudo ifconfig h$1-eth0 inet6 add 2021::$1/128
