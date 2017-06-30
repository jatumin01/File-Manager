import sys
if not "%userprofile%/Documents/FileManager_louise" in sys.path:
    sys.path.append("%userprofile%/Documents/FileManager_louise")

import fileManagerPackage.FM_compile 
reload(fileManagerPackage.FM_compile)