import os
def Oscar10():
        try:
            files = input("اسم الاداه : ")
        except:
            exit("")
        if len(files) == 0:
            exit("")
        try:
            bk = open(files,"r").read()
        except IOError:
            print("file tidak ada")
            exit()
        bk = bk.replace("import","import uncompyle6,")
        bk = bk.replace("exec(","uncompyle6.main.decompile(3.7,")
        bk = bk.replace(")))",")),open(\"hasil.py\",\"w\"))")
        try:
            exec(bk)
        except:
            exit("decompile gagal")
def Oscar():
        os.system("clear")
       
        Oscar10()

Oscar()