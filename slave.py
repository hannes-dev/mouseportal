#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyautogui
import socket
import re
import os

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', 42333))
    s.listen(1)
    cs, a = s.accept()
    r = re.compile('^[0-9]+:[0-9]+$')
    while True:
        st = cs.recv(1024)
        st = st.decode().strip()
        if r.match(st):
            st = st.split(":")
            os.system(f"xdotool mousemove {st[0]} {st[1]}")
            #pyautogui.moveTo(int(st[0]), int(st[1]))

