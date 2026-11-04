## modul für zugriff auf Dateisystem
from pathlib import Path
## modul für zugriff auf zip- Dateityp
import zipfile

# Ziel dieses Scripts ist, ein zip-file auszuwählen, zu entpacken und die Inhalte als liste auf der Shell anzuzeigen.


## Es müssen Parameter akzeptiert werden, um einen Dateinamen im Prompt angeben zu können


aa_Filename = "testfiles/Archiv.zip"
aa_DirName = "testfiles/Archiv"

## This is information only
print(Path.cwd())


## This displays the contents of aa_Filename
## Remember: always close your files
with zipfile.ZipFile(aa_Filename, "r") as zip_file:
    print(zip_file.namelist())
    zip_file.close()




