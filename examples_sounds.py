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

name    = "examples_sounds"
version = "2017-05-17T1932Z"
logo    = None

def main():

    propyte.pause("\ntable of sounds:\n")

    table_contents = [["name", "duration (s)"]]
    for sound in tonescale.sounds:
        table_contents.append([
                                  str(sound.name()),
                                  str(round(sound.duration(), 2))
                              ]
        )
    print(pyprel.Table(contents = table_contents))

    propyte.pause("\nexample: play sound in loop")

    sound = tonescale.access_sound(name = "199935__drzhnn__04-blip")

    for count in range(5):
        sound.play()

    propyte.pause("\nexample: repeat sound and then play sound")

    sound = tonescale.access_sound(name = "DynamicLoad_BSPNostromo_Ripley.023")
    sound.repeat(number = 2)
    sound.play()

    propyte.pause("\nexample: concatenate sounds and then play")

    sound = tonescale.Sound(name = "compose")
    sound.concatenate(
        sounds = [
                     tonescale.access_sound(name = "199935__drzhnn__04-blip"),
                     tonescale.access_sound(name = "199935__drzhnn__04-blip"),
                     tonescale.access_sound(name = "199935__drzhnn__04-blip")
                 ]
    )
    sound.play()

    propyte.pause("\nexample: add sounds and then play")

    sound_1 = tonescale.access_sound(name = "199935__drzhnn__04-blip")
    sound_2 = tonescale.access_sound(name = "199935__drzhnn__04-blip")
    sound_3 = sound_1 + sound_2
    sound_3.play()

    propyte.pause("\nexample: sum sounds and then play")

    sound_1 = tonescale.access_sound(name = "199935__drzhnn__04-blip")
    sound_2 = tonescale.access_sound(name = "199935__drzhnn__04-blip")
    sound_3 = sum([sound_1, sound_2])
    sound_3.play()

    propyte.pause("\nexample: play combined sounds by streaming, with pause\n")

    sound_1 = tonescale.access_sound(name = "ri1")
    sound_2 = tonescale.access_sound(name = "ri2")
    sound_3 = tonescale.access_sound(name = "ri4")

    sounds = [
                 sound_1, sound_2, sound_3, sound_1, sound_2, sound_3,
                 sound_1, sound_2, sound_3, sound_1, sound_2, sound_3,
                 sound_1, sound_2, sound_3, sound_1, sound_2, sound_3,
                 sound_1, sound_2, sound_3, sound_1, sound_2, sound_3,
                 sound_1, sound_2, sound_3, sound_1, sound_2, sound_3,
                 sound_1, sound_2, sound_3, sound_1, sound_2, sound_3,
                 sound_1, sound_2, sound_3, sound_1, sound_2, sound_3
             ]


    for sound in sounds[:24]:
        sound.play_stream()

    print("    pause")
    time.sleep(3)

    for sound in sounds[24:]:
        sound.play_stream()

    propyte.pause("\nexample: play all sounds in tonescale 3 times\n")

    for sound in tonescale.sounds:
        print("    play sound {name}".format(name = sound.name()))
        sound.repeat(number = 3)
        sound.play()

    propyte.pause("\nexample: save all sounds in tonescale repeated 30 times\n")

    for sound in tonescale.sounds:
        print("    save sound {name} repeated".format(name = sound.name()))
        sound.repeat(number = 3)
        sound.save_WAVE()

    print("")

if __name__ == "__main__":
    main()
