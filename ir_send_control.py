#!/usr/bin/python3

import adrsir
import ir_control
import os, sys, time
import argparse
import fcntl

BASE_DIR = os.path.dirname(__file__)
IR_DATA_DIR = os.path.join(BASE_DIR, 'ir_data/')
LOCK_FILE = os.path.join(BASE_DIR, 'ir_control.lock')

def send(file, num):

    if os.path.isfile(LOCK_FILE) == False:
        with open(LOCK_FILE, 'w'): pass

    ifp = open(LOCK_FILE, 'r')
    fcntl.flock(ifp.fileno(), fcntl.LOCK_EX)

    filepath = IR_DATA_DIR + file
    print('[*] send {} {} time(s)'.format(filepath, num))
    if not os.path.isfile(filepath):
        print('[!] {} does not exist'.format(filepath))
        return

    with open(filepath, 'r') as fp:
        data = fp.read()

    for i in range(num):
        adrsir.trans(data)
        time.sleep(0.5)

    fcntl.flock(ifp.fileno(), fcntl.LOCK_UN)
    ifp.close()

def main():
    args = sys.argv
    for arg in args:
        print(arg)
        if arg != 'ir_send_control.py':
            send(arg, 1)

    return

if __name__ == '__main__':
    main()
