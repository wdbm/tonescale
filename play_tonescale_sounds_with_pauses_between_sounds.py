#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# play_tonescale_sounds_with_pauses_between_sounds                             #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is tonescale examples.                                          #
#                                                                              #
# copyright (C) 2017 William Breaden Madden                                    #
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

import time

import propyte
import pyprel
import tonescale

name    = "play_tonescale_sounds_with_pauses_between_sounds"
version = "2017-07-04T1100Z"
logo    = None

def main():

    print(
        "play tonescale sounds first once and then repeated three times with a "
        "pause between each play"
    )

    for sound in tonescale.sounds:
        print("\nplay sound once: {name}".format(name = sound.name()))
        propyte.pause("press key to continue")
        sound.play()
        print("play sound three times: {name}".format(name = sound.name()))
        propyte.pause("press key to continue")
        sound.repeat(number = 3)
        sound.play()

if __name__ == "__main__":
    main()
