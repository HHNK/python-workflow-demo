# %%
"""Ruff format en lint de code. Uncomment onderstaande en sla op het bestand op.
Mits de Ruff extensie is geinstalleerd.
# TODO Todo Tree highlights TODO's, # FIXME, as long as there's a # in front of it
"""

import os  # Warning unused import
from logging.handlers import RotatingFileHandler
from pathlib import Path
import sys

from hhnk_research_tools.gis.interactive_map import create_interactive_map
import hhnk_research_tools

print( 'example of bad format'    )     #hi
print("This line is 119 characters", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
print("This line is longer than 119 characters", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
