#!/bin/bash
find ../form -path "*/migrations/*.py" -not -name "__init__.py" -delete
find ../form -path "*/migrations/*.pyc" -delete
find ../../django_my_laboratory -path "*/db.sqlite3" -delete