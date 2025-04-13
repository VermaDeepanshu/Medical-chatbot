import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO , format='[%(asctime)s]:%(message)s:')

lists_of_files =[
    "src/__init__.py ",  # constructor file
    "src/helper.py",   # all functionality of installation
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb"   #jupyter notebook
]
#loopig in files to setup them
for filepath in lists_of_files:
    filepath = Path(filepath)  # automatically take care of forward slash
    filedir,filename = os.path.split(filepath)  # split folder and file name

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory ; {filedir} for the files: {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file : {filepath}")

    else:
        logging.info(f"{filepath} is already exists")

