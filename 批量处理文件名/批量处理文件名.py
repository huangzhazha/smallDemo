#coding:utf-8
import os
name = os.listdir('./')
for temp in name:
    new_name = temp[-22:]
    os.rename('./'+temp,'./'+new_name)