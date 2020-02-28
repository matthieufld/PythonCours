import sys

def write(fich_name):
    fichier = open(fich_name, "w+")
    fichier.write("Bonjour")
    fichier.close();

def read(fich_name):
    fichier = open(fich_name, "r")
    o = fichier.read()
    print (o)
    fichier.close();

if __name__ == "__main__":
    fich_name = input(sys.argv[0])
    write(fichier_name)
    read(fichier_name)