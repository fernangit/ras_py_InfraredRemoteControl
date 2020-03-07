#!/bin/sh
python3 ir_control.py send prj1/ch0.data
sleep 1
python3 ir_control.py send prj1/ch1.data
sleep 1
python3 ir_control.py send prj1/ch1.data
sleep 1
python3 ir_control.py send prj1/ch2.data