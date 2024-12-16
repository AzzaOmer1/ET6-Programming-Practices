#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Stopping a Program

You can stop a program at any time when you are in the debugger.
        - just press the red box!
        
"""
while True:
    print("...")
    user_input = input("Type 'stop' to exit: ") #add this line ad down until break
    if user_input.lower() == 'stop':
        print("Program stopped.")
        break
    
"""
To stop a program from running you can press Ctrl + c 
if it is running continuously without stopping
"""
