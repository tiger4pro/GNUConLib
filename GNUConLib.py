#!/usr/bin/env python
# -*- coding: utf-8 -*-

# GNUConLib - Convertir un fichier wav en mp3
# Copyright (C) 2020 Steve Prud'Homme <sprudhom@gmail.com>
#
# Ce programme est un logiciel libre ; vous pouvez le redistribuer ou le
# modifier suivant les termes de la Licence Publique Générale GNU telle que
# publiée par la Free Software Foundation ; soit la version 3 de la
# licence, soit (à votre gré) toute version ultérieure.
#
# Ce programme est distribué dans l'espoir qu'il sera utile, mais SANS
# AUCUNE GARANTIE ; sans même la garantie implicite de COMMERCIALISABILITÉ
# ni d'ADÉQUATION À UN OBJECTIF PARTICULIER. Consultez la Licence Publique
# Générale GNU pour plus de détails.
#
# Vous devriez avoir reçu une copie de la Licence Publique Générale GNU
# avec ce programme ; si ce n'est pas le cas, consultez
# <https://www.gnu.org/licenses/>.

import argparse
import sys
from pydub import AudioSegment

# Définition des arguments de la ligne de commande
parser = argparse.ArgumentParser(
    description="Convertir un fichier wav en mp3",
    epilog="""Exemples :
    python GNUConLib.py fichier.wav fichier.mp3
    python GNUConLib.py fichier.wav fichier.mp3 --channels 1 --sample_rate 44100 --bitrate 128""",
    usage="%(prog)s [-man] fichier_entree.wav fichier_sortie.mp3 [--channels N] [--sample_rate N] [--bitrate N]",
)
parser.add_argument("-man", action="store_true", help="afficher l'aide")
parser.add_argument("fichier_entree", nargs='?', help="fichier wav à convertir")
parser.add_argument("fichier_sortie", nargs='?', help="fichier mp3 résultant")
parser.add_argument("--channels", type=int, default=2, help="nombre de canaux (1 pour mono, 2 pour stéréo)")
parser.add_argument("--sample_rate", type=int, default=44100, help="fréquence d'échantillonnage en Hz")
parser.add_argument("--bitrate", type=int, default=320, help="débit en kbps")

# Parse les arguments de la ligne de commande
args = parser.parse_args()

# Affiche l'aide si le paramètre -man est utilisé
if args.man:
    parser.print_help()
    sys.exit(0)

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
