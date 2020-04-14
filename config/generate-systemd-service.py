# -*- coding: utf-8 -*-
"""."""
import sys
from pathlib import PurePath, Path

BASE_DIR = PurePath(__file__)
PROJECT_DIR = BASE_DIR.parents[1]

for settings_dir in Path(PROJECT_DIR).rglob('settings.py'):
    app = settings_dir.parts[-2]

description = ''
user = ''
group = ''
working_directory = PROJECT_DIR
pid = PROJECT_DIR.joinpath('pid', f'{app}.pid')
access_logfile = PROJECT_DIR.joinpath('logs', 'gunicorn-access.log')
error_logfile = PROJECT_DIR.joinpath('logs', 'gunicorn-error.log')

template = f'''[Unit]
Description = {description}
After = network.target

[Service]
User = {user}
Group = {group}
WorkingDirectory = {working_directory}
ExecStart = /usr/local/bin/pipenv run gunicorn \\
--pid {pid} \\
--access-logfile {access_logfile} \\
--error-logfile {error_logfile} \\
--workers 2 \\
--bind 0.0.0.0:8000 \\
{app}.wsgi:application

[Install]
WantedBy = multi-user.target
'''

print(template)
# SYSTEMD_FILE = Path(BASE_DIR.with_name(f'{app}.service'))
# SYSTEMD_FILE.write_text(data=template)
