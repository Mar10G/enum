import csv
import getpass
import grp
import os
import pwd
from datetime import date


class bcolors:
    OK = '\033[35m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR
    Black = '\033[0;30m'  # Black
    Red = '\033[0;31m'  # Red
    Green = '\033[0;32m'  # Green
    Yellow = '\033[0;33m'  # Yellow
    Blue = '\033[0;34m'  # Blue
    Purple = '\033[0;35m'  # Purple
    Cyan = '\033[0;36m'  # Cyan
    White = '\033[0;37m'  # White


def myCMD(cmd):
    print(f'\t ')
    print(f"{bcolors.OK}About to run {cmd}")
    os.system(cmd)
    print(f"End of cmd {bcolors.RESET}")
    print(f'\t ')


def createDirectory(myDir):
   # print(f'\t =======================================')
    print(f'Checking ' + myDir + ' ------> ' + bcolors.Green, end='')

    if os.path.isdir(myDir):
        print(f'Directory already exist')
    else:
        os.mkdir(myDir)
        uid = pwd.getpwnam(user).pw_uid
        gid = grp.getgrnam(user).gr_gid
        os.chown(myDir, uid, gid)
        print(f'Directory created')

    print(bcolors.RESET)
    # print(f'\t =======================================')


def checkIPs(fl):
    print(f'Checking ' + fl + ' ------> ' + bcolors.Green, end='')

    if os.path.isfile(fl):
        print(f'IP file exist', end='')
        count = len(open(fl).readlines())
        print(f'   ' + bcolors.Blue + 'lines = ' + str(count))
    else:
        # os.mkdir(dir)
        print(f'\t not there')
        open(fl, "w")
        uid = pwd.getpwnam(user).pw_uid
        gid = grp.getgrnam(user).gr_gid
        os.chown(fl, uid, gid)
        quit()

    print(bcolors.RESET)


def doNmapScan():
    print(f'\t =======================================')
    print(f'\t Start nmap scan')

    working_directory = base_directory + 'enum/nmap/'
    createDirectory(working_directory)
    # nmap_command = 'sudo nmap -iL ' + ip_file + ' -sSVC -Pn -O -p- -v -T3 -oA ' + working_directory + client
    nmap_command = 'sudo nmap -iL ' + ip_file + ' -sS -p 80,139,443,445 -T4 -oA ' + working_directory + client
    print(f'\t nmap_command = ' + nmap_command)
    os.system(nmap_command)

    print(f'\t End nmap scan')
    print(f'\t =======================================')


def doEyewitness():
    print(f'\t =======================================')
    print(f'\t Start eyewitness')

    print(f'\t End eyewitness')
    print(f'\t =======================================')


def doEnum4Linux():
    print(f'\t =======================================')
    print(f'\t Start enum4linux')

    print(f'\t End enum4linux')
    print(f'\t =======================================')


def doNmapParse():
    print(f'\t =======================================')
    print(f'\t Start nmap parse')

    myDir = '/opt/tools/ultimate-nmap-parser/'
    if os.path.isdir(myDir):
        print(f'\t ultimate-nmap-parser already exist in /opt/tools')
    else:
        myCMD('sudo git clone https://github.com/Shifty0g/ultimate-nmap-parser/ /opt/tools/ultimate-nmap-parser')
        myCMD('sudo chmod +x /opt/tools/ultimate-nmap-parser/ultimate-nmap-parser.sh')

    working_directory = base_directory + 'enum/nmap/'
    myCMD('sudo /opt/tools/ultimate-nmap-parser/ultimate-nmap-parser.sh ' + working_directory + client + '.gnmap --all')

    cwd = os.getcwd()
    myCMD('sudo mv ' + cwd + '/parse/ ' + base_directory + 'enum/nmap/')
    myCMD('sudo chown ' + user + ' ' + base_directory + 'enum/nmap/parse/')
    myCMD('sudo chown ' + user + ' ' + base_directory + 'enum/nmap/parse/*.*')

    print(f'\t End nmap parse')
    print(f'\t =======================================')


client = 'Home'
nmap_switches = '-sSVC -Pn -O  --top-ports 10  -v -T3'
working_directory = ' '
scan_directory = 'port-scan'
nmap_command = ' '
user = getpass.getuser()
year = date.today().year
base_directory = '/home/' + user + '/client-data/' + str(year) + '/' + client + '/'
ip_file = base_directory + 'ips.txt'

# print(f'\t Checking ' + user)
# print(f'\t Checking ' + os.getlogin() )
# print(f'\t --- ' + base_directory)

print(f'\t ')

createDirectory(base_directory)
checkIPs(ip_file)

createDirectory(base_directory + 'enum/')

doNmapScan()

quit()


doNmapParse()
# doEyewitness()
# doEnum4Linux()

quit()


