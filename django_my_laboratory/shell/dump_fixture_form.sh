#!/bin/bash
cd ..
poetry run python manage.py dumpdata form.department > form/fixtures/fixture_department.json
poetry run python manage.py dumpdata form.position > form/fixtures/fixture_position.json
poetry run python manage.py dumpdata form.skillcategory > form/fixtures/fixture_skillcategory.json
poetry run python manage.py dumpdata form.skill > form/fixtures/fixture_skill.json
poetry run python manage.py dumpdata form.employee > form/fixtures/fixture_employee.json