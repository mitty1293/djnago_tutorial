# プロジェクト作成
カレントディレクトリ直下に最低限必要なファイルを含めた`<project_name>`ディレクトリが作成される。
```
django-admin startproject <project_name> .
```
# アプリケーション作成
必要なファイルを含めた`<appname>`ディレクトリが作成される。
```
python manage.py startapp <appname>
```
# アプリ作成後の大まかな初期設定の流れ
1. プロジェクトの`settings.py` にて `TEMPLATES` の `DIRS` を設定
    * 例：`"DIRS": [BASE_DIR / "templates"],`
2. プロジェクトの`settings.py` にて `INSTALLED_APPS` にアプリを登録
    * 例：
        ```
        INSTALLED_APPS = [
        ..... 
            "someapp.apps.SomeappConfig",
        ]
        ```
3. プロジェクトの`urls.py`にてアプリの`urls.py`を呼び出す設定
    * 例：
        ```
        from django.contrib import admin
        from django.urls import include, path

        urlpatterns = [
            path("admin/", admin.site.urls),
            path("", include("someapp.urls")),
        ]
        ```
4. アプリの`urls.py`を作成しルーティング設定
# 開発用サーバ起動
プロジェクトのルートディレクトリ（`manage.py`がある）で以下を実行すると開発用サーバが立ち上がる。  
表示の通り`http://127.0.0.1:8000/`にアクセスすると開発用サーバに繋がる。  
```
python manage.py runserver
....
Django version 4.0.4, using settings 'helloworldproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
デフォルトのポートは`8000`だが変えたい時は以下のように引数でポート番号を渡す。
```
python manage.py runserver 8080
```
サーバのIP指定も可能。全IPからのリクエストを受け付けるには`0.0.0.0` or `0`を指定。
```
python manage.py runserver 0:8080
```
# ALLOWED_HOSTSとrunserverについて
* `runserver`はデフォルトでは`runserver 127.0.0.1:8000`であるため、自身が動作しているサーバ内からのアクセスしか受け付けない。
  * ローカルループバックアドレス（`127.0.0.1`）のインターフェースにバインドされる感じ。
  * つまり「WSL上コンテナ内のdjango」に「WSLのホストPC」からアクセスする場合、別端末からのアクセスとなるので`runserver 0.0.0.0:8000`等しないとアクセスできない。
* `ALLOWED_HOSTS`は配信するドメイン名やホスト名、IPアドレスをリストで指定する。
  * クライアントからのHTTPリクエストのホストヘッダー部分に、指定したドメイン名等が含まれている場合のみ、webサービスが配信される。
  * `DEBUG=True`かつ`ALLOWED_HOSTS=[]`の場合、`localhost, 127.0.0.1, [::1]`が自動で有効になる。
# djangoのプロジェクトとアプリの関係
![django_project_app](https://github.sakura.codes/k-furumichi/learning_django/blob/main/udemy_django-3app/img/django_prj_app.png)
# djangoのファイル構成
参考：https://just-python.com/document/django/introduction/directory
## プロジェクト関連（startprojectで作成されるファイル群）
```
sample_project
├── db.sqlite3          // データベース
├── sample_project
│   ├── __init__.py     // pythonのパッケージとかを示すあれ。django特有の何かではない。
│   ├── asgi.py         // asgi用のエントリポイント
│   ├── settings.py     // django全体の設定ファイル
│   ├── urls.py         // URLとviewを紐づける。ルーティングするところ。
│   └── wsgi.py         // wsgi用のエントリポイント
└── manage.py           // djangoのコマンドラインユーティリティ。色々できるよ。

※views.pyをsample_projectディレクトリ内に作成したりすることもある。一般的にプロジェクト全体に関わるviewを書く。アプリ側は各アプリ内でviews.pyを実装する。
```
## アプリケーション関連（startappで作成されるファイル群）
```
sample_app
├── __init__.py
├── admin.py            // 管理画面を制御する
├── apps.py             // アプリの設定を記載。内容をプロジェクトのsettings.pyで読み込む。ほぼ触らない。
├── models.py           // modelを書くところ
├── tests.py            // テストコードを書くところ
└── views.py            // viewを書くところ

※一般的にはsample_appディレクトリ内にurls.pyを作成してアプリ内のルーティングをする。
```
# settings.pyの各項目について
以下参照  
https://www.tohoho-web.com/django/settings.html  
https://just-python.com/document/django/project-setting/settings
# urls.py
* pathは上から順に合致するか照合させていく。合致したらそこより下は無視。
* ルーティング構築時は、追加した各appにurls.pyを手動で追加、そのファイルをプロジェクト内のurls.pyで読み込むのが一般的。
  * そうすることでアプリとプロジェクトが繋がる。
  ```
  # https://example.com/news/price というリクエストが来たとして

  # プロジェクトのurls.py
  urlpatterns [
      ("news/", include("アプリ.urls"))
  ]

  # アプリのurls.py
  urlpatterns [
      ("price/", some_view)
  ]
  ```
# views.py
* urls.pyで合致したルーティングに従ってリクエストオブジェクトがurls.pyからvies.pyに渡され、vies.pyからレスポンスオブジェクトを返す。
* djangoのviewは関数ベース（def）とクラスベース（class）の2種類存在する。
## function based view
* 関数で記述するview
* リクエストオブジェクトを引数にした関数を作成し、返り値でレンダリングしたりする
```
# 例
def index(request):
    if request.method == 'GET':
        print('GETリクエスト')
        return HttpResponse(200)
    if request.method == 'POST':
        print('POSTリクエスト')
        return HttpResponse(200)
```
## class based view
* classで記述するview
* djangoが用意している様々な汎用viewをインポートして継承してviewを作成していく。
```
# 例
from django.views import View
class IndexView(View):
    def get(self, request):
        print('GETリクエスト')
        return HttpResponse(200)
    def post(self, request):
        print('POSTリクエスト')
        return HttpResponse(200)
```
* 使うときには`as_view()`というクラスメソッドからviewオブジェクトを生成して使う。
```
path("helloworld/", HelloWorldClass.as_view())
```
### as_viewとは
* viewオブジェクトを生成するメソッド
* class based viewを元にfunction based viewを生成してよしなにしてくれる
## viewの継承
* classの引数にviewを示すclassを指定するとviewを継承することができる。
* 要はpythonにおけるclassの継承
```
# 例：TemplateViewクラスを継承している
from django.views.generic import TemplateView
class HelloWorldClass(TemplateView):
    ....
```
## 主要な汎用ViewとCRUDの対応
* C: CreateView
* R: ListView, DetailView
* U: UpdateView
* D: DeleteView
## ListView
* 複数データをリストのように（クエリセット）扱うview
* データが存在しなくてもエラーにならない。
* template上では`{{ object_list }}`でデータ取得できる。
## DetailView
* 単体データ（オブジェクト）を扱うview
* template上では`{{ object }}`でデータ取得でき、`{{ object.some_field1 }}`,`{{ object.some_field2 }}`のようにクラス変数を取得できる。
* `urls.py`にてオブジェクトを指定するフィールドをURLに付ける必要がある
    ```
    # DBのprimary keyを指定する
    path("detail/<int:pk>", SomeDetailView.as_view()),
    # URLスラッグを使う
    ```
# models.py
* djangoではclassでモデル（DBのレイアウト）を表現する。
* 1つのモデルは1つのclassで表現され1つのテーブルと対応する。
* 各クラス変数（フィールド）がDBのカラムを表す。
## モデル定義からDBへの反映までの流れ
1. `models.py`にモデルを定義
2. `python manage.py makemigrations <app_name>`でマイグレーションファイルを生成
    djangoに対してモデルに変更があったことを伝え、変更をマイグレーションファイルとして保存する  
    (0001_initial.py, 0002_initial.py, ...)  
    ファイルによって希望通りの構造になっているか確認ができる。  
    `<app_name>`で対象アプリの名前を指定すると指定アプリについてのみマイグレーションファイルが生成される。  
    省略することも可能だが、全アプリに対して動作するため複数人での開発時は指定した方がベター。
3. `python manage.py migrate`でマイグレーションファイルからSQLを発行、テーブルを生成
    マイグレーションファイルに記入された変更がDBに反映される。
4. `admin.py`にて`admin.site.register(Model)`を記載し管理画面にモデルを登録する。
# 管理者サイト用スーパーユーザ作成
管理者サイト用のスーパーユーザが作成される。  
管理者サイトでは各ユーザのパーミッション設定等が可能。
```
python manage.py createsuperuser
```
# admin.py
* 管理画面で何をどのように管理するのか設定する。
* 例えばモデルは作成しただけでは管理画面に反映されないため、`admin.py`にて`admin.site.register(Model)`を記載し管理画面にモデルの登録を行う必要がある。
# template
* djangoのtemplateでは変数やタグを見つけて置換しレンダリングすることができる。
    * `{{ 変数 }}`
    * `{% タグ %}`
* includeやblockタグを使って他テンプレートを継承したり読み込んだりも可能
# memo
## sec12
### 139
* CreateView
* reverse_lazy
    * reverseメソッドは、通常の流れであるurlからviewを呼び出す、ではなくurlの名前(name)からviewを呼び出す。
* {{ form.as_p }}
* models.CharField(max_length=50, choices=SOME_CHOICE)
### 140
* DeleteView
### 141
* UpdateView
### 142
* urlタグ
    * urlタグはビューとオプションの引数を指定して、これとマッチする絶対パスへの参照 ( ドメイン部分を除いた URL ) を返します。
    * `{% url 'viewname' %}` で指定されたnameとマッチするviewのURLを返す。
## sec13
### 147
* render
### 149
* request.method
### 150
* django.contrib.auth.models.User
* SomeModel.objects.get
    * Modelから指定したキーワード引数をキーにオブジェクトを取り出す
* SomeModel.objects.all
    * 全オブジェクトを取り出す
### 151
* request.POST
* django.contrib.auth.models.User
    * User.objects.create_user
### 152
* django.db.IntegrityError
### 153
* django.contrib.auth.authenticate
* django.contrib.auth.login
### 154
* redirect
    * `urls.py`で指定したpathのnameをredirectで指定する。指定されたpathに飛びviewを呼び出す。
### 156
* django.db.models.ImageField(upload_to="")
    * `upload_to`: 画像の保存場所を指定。`settings.py`で指定したディレクトリ配下の場所を指定する
    * `settings.py`で指定した場所で良ければ`uploas_to=""`として置けば問題ない。
### 158
* `settings.py`
    * MEDIA_ROOT
        * 画像ファイル等メディアファイル格納ディレクトリ
    * MEDIA_URL
        * URLと画像ファイルを結び付ける変数
* static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    * プロジェクトの`urls.py`に上記を追記する
    * 画像はプロジェクトの`settings.py`で定義したMEDIA_ROOTに保存されるため、個別アプリに関係が無く、プロジェクト全体で管理するものとなる。よってプロジェクトの`urls.py`に記載をする。
    * MEDIA_URLで指定したURLを受け取ると、MEDIA_ROOTで指定したディレクトリから対象画像を持ってくる、という流れ
### 159
* https://qiita.com/saira/items/a1c565c4a2eace268a07
* `settings.py`
    * STATIC_URL
        * URLと静的ファイルを結び付ける変数
    * STATIC_ROOT = BASE_DIR / "staticfiles"
        * 本番環境用の静的ファイル格納ディレクトリ
        * 本番環境ではアプリ毎ではなく、1個のディレクトリで全アプリの静的ファイルを管理した方が効率的らしい。
        * `python manage.py collectstatic`で`STATICFILES_DIRS`から`STATIC_ROOT`に静的ファイルを集めることができる。
    * STATICFILES_DIRS = [str(BASE_DIR / "static")]
        * 開発環境用の静的ファイル格納ディレクトリ
        * リストに複数書くことで、アプリ毎の静的ファイル格納ディレクトリを設定できる。
* {% load static %}
### 160
* ログイン状態を判定するには以下の2つの方法がある
    * login_required デコレータ
        * https://docs.djangoproject.com/ja/4.0/topics/auth/default/#the-login-required-decorator
        * settings.LOGIN_URL
            * `urls.py`で指定したpathのnameをLOGIN_URLで指定する。指定されたpathに飛びviewを呼び出す。
        * function based viewには設定できるが、classには設定できないので、その際は以下を使う事。
    * {% if user.is_authenticated %}
### 161
* django.contrib.auth.logout
### 162
* django.shortcuts.get_object_or_404(Model, **kwargs)
    * `Model.objects.get(arg=value)` でも似たようなことはできる。
    * 要はModelから指定したキーワード引数をキーにオブジェクトを取り出す、という処理。
    * 404の方は、オブジェクトが存在しないときにHttp404を返す。
### 163
* object.save
### 164
* request.user.get_username()
### 165, 166
* CreateView
    * {{ user.username }}
    * models.SomeField(null=True, blank=True, default="")
