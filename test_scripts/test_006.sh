#!/bin/bash
cd ..
cd src/python
sqlite3 airwaves.db ".read db_update_6.sql"
python3 -i main.py