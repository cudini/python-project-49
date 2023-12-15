install: # установка пакета нашего проекта
	poetry install

brain-games: # запуск проекта
	poetry run brain-games

build: # сборка пакета
	poetry build

publish: # публикация пакета без отправки в индекс
	poetry publish --dry-run

package-install: # --force-reinstall для переустановки пакета
	python3 -m pip install --user dist/*.whl --force-reinstall

make lint:
	poetry run flake8 brain_games
