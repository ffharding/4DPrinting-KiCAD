import subprocess
def autoroute_dsn(path):
    """
    Handles autorouting from Specctra DSN file to routed Specctra Session file using freerouting fork (freerouting_cli)
    Inputs:
        path (str) : path location of specctra dsn file and target location for specctra ses file
    Outputs:
        Specctra Session file (.ses) : file containing autorouted PCB information
    """
    cmd = r'java.exe -jar freerouting_cli/lib/freerouting_cli.jar -de {path}.dsn -do {path}.ses -mp 100 -dr autorouting\default.rules'.split(' ')
    cmd = [command.replace('{path}', path) for command in cmd] ## fixes error that separated file names with spaces
    subprocess.run(cmd)

