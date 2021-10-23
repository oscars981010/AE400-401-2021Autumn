# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 11:16:36 2021

@author: 10105711
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
wicdth=10
height=5
length=6
mc.setBlocks(x,y,z,x+wicdth,y+height,z+length,19)
mc.setBlocks(x+1,y+1,z+1,x+wicdth-1,y+height-1,z+length-1,0)


e






