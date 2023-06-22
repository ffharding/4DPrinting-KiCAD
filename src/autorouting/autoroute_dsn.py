import subprocess
def autoroute_dsn(path):
    cmd = r'java.exe -jar freerouting_cli/lib/freerouting_cli.jar -de {path}.dsn -do {path}.ses -mp 100 -dr autorouting\default.rules'.split(' ')
    cmd = [command.replace('{path}', path) for command in cmd] ## fixes error that separated file names with spaces
    subprocess.run(cmd)

