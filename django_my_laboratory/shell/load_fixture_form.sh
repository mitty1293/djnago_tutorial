#!/bin/bash
cd ..
poetry run python manage.py loaddata form/fixtures/fixture_department.json
poetry run python manage.py loaddata form/fixtures/fixture_position.json
poetry run python manage.py loaddata form/fixtures/fixture_skillcategory.json
poetry run python manage.py loaddata form/fixtures/fixture_skill.json
poetry run python manage.py loaddata form/fixtures/fixture_employee.json