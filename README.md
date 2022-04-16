# django_tutorial
[djangoの公式チュートリアル](https://docs.djangoproject.com/ja/4.0/intro/)をやってみる
>Django アプリケーションを作成するときの典型的なワークフローは、 モデルを作成し、 admin サイトを組み上げてできるだけ早期に立ち上げ、スタッフ (や顧客) がデータを投入できるようにしておいてから、データを公開するための方法を開発してゆくというものです。
## Setup
`poetry`を用いて依存関係の管理をしています。  
`poetry`がインストールされていない場合はインストールしてください。  
`poetry`の準備後、`poetry install`コマンドで`pyproject.toml`, `poetry.lock`を基に`django`等の依存関係をインストールします。
## Referenses
* https://rasulkireev.com/managing-django-with-poetry/
* https://docs.djangoproject.com/ja/4.0/intro/install/