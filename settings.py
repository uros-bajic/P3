"""Project configuration settings (PROJECT_DIR, format strings, etc.).
"""

from pathlib import Path

PREFERRED_DATE_FORMAT = '%b %d, %Y'

# print(__file__) # folder projekta
# print(Path(__file__)) # objekat tipa Path
PROJECT_DIR = Path(__file__).parent # roditeljski direktorijum

# import os

# print(__file__)
# print(os.path.abspath(__file__))
# print(os.path.dirname(__file__))

# PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
# print(PROJECT_DIR)


from pathlib import Path
