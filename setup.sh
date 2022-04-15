# pythonが無い場合は先にpythonインストール
# poetryインストール
echo "-----Install poetry-----"
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -

# 上記のインストール時に自動で `~/.profile` に `export PATH="$HOME/.poetry/bin:$PATH"` が追加される
# （$PATHにpoetry実行ファイルのディレクトリが追加される）
# 再ログインせずに有効化するためにsourceコマンドで反映させる
echo "-----Reflect ~/.profile-----"
source ~/.profile

# 依存関係インストール（django等）
echo "-----Installing dependencies-----"
poetry install

# vscodeがpoetryの仮想環境を認識できるようにする
echo "-----poetry config virtualenvs.in-project true-----"
poetry config virtualenvs.in-project true

# プロジェクトを作成する場合、以下で<PROJECTNAME>ディレクトリを作成する
# poetry run django-admin startproject <PROJECTNAME>
