# pythonが無い場合は先にpythonインストール
# poetryインストール
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -

# 自動で `~/.profile` に `export PATH="$HOME/.poetry/bin:$PATH"` が追加される
# （$PATHにpoetry実行ファイルのディレクトリが追加される）
# sourceコマンドで再ログインせずに反映させる
source ~/.profile

# 依存関係インストール（django等）
poetry install

# プロジェクトを作成する場合、以下で<PROJECTNAME>ディレクトリを作成する
# poetry run django-admin startproject <PROJECTNAME>