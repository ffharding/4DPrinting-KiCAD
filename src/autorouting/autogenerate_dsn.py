import subprocess

def autoroute_dsn(filename):
    cmd = f'java.exe -jar freerouting_cli/lib/freerouting_cli.jar -de {filename}.dsn -do {filename}.ses -mp 100 -dr {filename}.rules'.split(' ')
    subprocess.run(cmd)
