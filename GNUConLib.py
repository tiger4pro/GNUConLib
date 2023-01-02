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

import argparse
import sys
from pydub import AudioSegment

# Définition des arguments de la ligne de commande
parser = argparse.ArgumentParser(description="Convertir un fichier wav en mp3")
parser.add_argument("fichier_entree", help="fichier wav à convertir")
parser.add_argument("fichier_sortie", help="fichier mp3 résultant")
parser.add_argument("--channels", type=int, default=2, help="nombre de canaux (1 pour mono, 2 pour stéréo)")
parser.add_argument("--sample_rate", type=int, default=44100, help="fréquence d'échantillonnage en Hz")
parser.add_argument("--bitrate", type=int, default=320, help="débit en kbps")

# Parse les arguments de la ligne de commande
args = parser.parse_args()

# Récupère le nom des fichiers d'entrée et de sortie
fichier_entree = args.fichier_entree

# Récupère le nom des fichiers d'entrée et de sortie
fichier_entree = args.fichier_entree
fichier_sortie = args.fichier_sortie

# Vérifie que les fichiers ont l'extension attendue
if not fichier_entree.endswith(".wav"):
    print("Le fichier d'entrée doit avoir l'extension .wav")
    sys.exit(1)

if not fichier_sortie.endswith(".mp3"):
    print("Le fichier de sortie doit avoir l'extension .mp3")
    sys.exit(1)

# Charge le fichier wav et le convertis en mp3
son = AudioSegment.from_wav(fichier_entree)
son = son.set_channels(args.channels)
son = son.set_frame_rate(args.sample_rate)
son.export(fichier_sortie, format="mp3", bitrate=f"{args.bitrate}k")

print("Conversion terminée !")
