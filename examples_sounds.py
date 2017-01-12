#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# examples_sounds                                                              #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is tonescale examples.                                          #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################
"""

name    = "examples_sounds"
version = "2017-01-12T2239Z"
logo    = None

import tonescale
import time

def main():

    print("\nexample: play sound in loop")

    sound = tonescale.access_sound(name = "199935__drzhnn__04-blip")

    for count in range(5):
        sound.play()

    print("\nexample: repeat sound and then play sound")

    sound = tonescale.access_sound(name = "DynamicLoad_BSPNostromo_Ripley.023")
    sound.repeat(number = 2)
    sound.play()

if __name__ == "__main__":
    main()
