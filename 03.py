# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft
mc = Minecraft .create()

import time

x,y,z = mc.player.getTilePos()
time.sleep(5)
mc.setBlock(x,y,z,20)
time.sleep(0.5)
mc.setBlock(x,y+1,z,20)
time.sleep(0.5)
mc.setBlock(x,y+2,z,20)
time.sleep(0.5)
mc.setBlock(x,y+3,z,20)
time.sleep(0.5)
mc.setBlock(x,y+4,z,20)
time.sleep(0.5)
mc.setBlock(x,y+5,z,20)
x,y,z = mc.player.getTilePos()
mc.setBlocks(x, y-1, z+1, x+2, y-1, z-1, 57)
mc.setBlock(x+1, y-1, z, 11)
