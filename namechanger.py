import os, glob, re

name_map = {
    "uhc-skwf-bqx": "basico_interfaces_grupo_10",
    "pxr-qsrs-vjc": "basico_interfaces_grupo_06"
}

for root, dirs, files in os.walk(r"C:\Users\Dell\Downloads\skip"):
    for f in files:
        for name in name_map.keys():
            if re.search(name,f) != None:
                new_name = re.sub(name,name_map[name],f)
                try:
                    os.rename(os.path.join(root,f), os.path.join(root, new_name))
                except OSError:
                    print("No such file or directory!")
