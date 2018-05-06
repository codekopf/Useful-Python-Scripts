import subprocess

def load_file(file_name):
    return tuple(open(file_name, 'r'))

def main():
    file = "packages.txt"
    lines = load_file(file)

    l = []
    for line in lines:
        if line.strip() != '':
            modul_name, modul_version = line.split(",")
            modul_version = modul_version.strip()
            l.append("{} {}".format(modul_name, modul_version))

            result = subprocess.Popen(["pip", "install", modul_name, modul_version], stdout=subprocess.PIPE)
            result.stdout
            """
            sys.stdout.write("{} {}".format(modul_name, version))
            print("{} {}".format(modul_name, version))
            """


    for a in l:
        print(a)

"""
TODO
* option for unassigned module version
* test for empty file
"""

if __name__ == "__main__":
    main()