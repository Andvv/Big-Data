# Llamadas Etl Fabian
import pandas as pd

import os
from pathlib import Path

root_dir = Path(".").resolve().parent 
filename= 'llamadas123_julio_2022.csv'

file_path = os.path.join(root_dir,"data","raw",filename)
file_path

df = pd.read_csv(file_path, sep =";", encoding="latin-1")

df.head()