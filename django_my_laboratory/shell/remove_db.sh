#!/bin/bash
cd ..
find ./form -path "*/migrations/*.py" -not -name "__init__.py" -delete
find ./form -path "*/migrations/*.pyc" -delete
find ./ -path "*/db.sqlite3" -delete