# Home Backup Tool

A lightweight Python backup utility that monitors and uploads files from the top level of your Linux home directory (or any configured base directory). It tracks file changes using SHA-256 hashes and only uploads new or modified files.

---

## Features

- Skips non-file entries safely
- Stores local hash database for incremental backups
- Simple, dependency-light design

---

## How to use

git clone https://github.com/josephtesting97-source/BackupTool.git 
cd BackupTool
pip install -r requirements.txt
mv Backup.py /../../Backup.py
python3  /../../backup.py
---
