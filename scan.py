import os
import platform

try:
    import requests
except ImportError:
    os.system('pip install requests')

bit = platform.architecture()[0]

if bit == "64bit":
    try:
        from VIRUS import Main
    except ImportError:
        print("The module 'VIRUS' is not available.")
else:
    try:
        from VIRUS_SCAN import Main
    except ImportError:
        print("The module 'VIRUS_SCAN' is not available.")

if 'Main' in locals():
    Main()
