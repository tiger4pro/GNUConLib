#!/usr/bin/env python
# -*- coding: utf-8 -*-

# GNUConLib - Convertir un fichier wav en mp3
# Copyright (C) 2020 Steve Prud'Homme <sprudhom@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
from pydub import AudioSegment

# Vérifie que le nombre de paramètres est correct
if len(sys.argv) != 3:
    print("Usage : GNUConLib fichier_entree.wav fichier_sortie.mp3")
    sys.exit(1)

# Récupère le nom des fichiers d'entrée et de sortie
fichier_entree = sys.argv[1]
fichier_sortie = sys.argv[2]

# Vérifie que les fichiers ont l'extension attendue
if not fichier_entree.endswith(".wav"):
    print("Le fichier d'entrée doit avoir l'extension .wav")
    sys.exit(1)

if not fichier_sortie.endswith(".mp3"):
    print("Le fichier de sortie doit avoir l'extension .mp3")
    sys.exit(1)

# Charge le fichier wav et le convertis en mp3
son = AudioSegment.from_wav(fichier_entree)
son = son.set_channels(2)
son = son.set_frame_rate(44100)
son.export(fichier_sortie, format="mp3", bitrate="320k")

print("Conversion terminée !")

