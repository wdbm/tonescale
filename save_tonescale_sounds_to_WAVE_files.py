#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# save_tonescale_sounds_to_WAVE_files                                          #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program saves tonescale sounds to WAVE files.                           #
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

name    = "save_tonescale_sounds_to_WAVE_files"
version = "2017-07-04T1052Z"
logo    = None

def main():

    for sound in tonescale.sounds:
        print("save sound {name}".format(name = sound.name()))
        sound.save_WAVE()

if __name__ == "__main__":
    main()
