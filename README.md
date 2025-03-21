# chatbotV1

このプロジェクトは、streamlitcloudベースのlangchainを使ったチャットアプリケーションです。以下の機能を提供します。

- テキストファイルのアップロード
- アップロードされたテキストファイルをベクトル化して、chromadbへ保存
- chromadbから情報を抽出して回答するチャットボット
- ログ管理
- OPENAIのAPIキーをstreamlitcloudで設定して認証

## セットアップ

1. 必要なPythonパッケージをインストールします。

    ```bash
    pip install -r requirements.txt
    ```

2. SQLiteのバージョンをアップグレードします。

    ```bash
    tar xvfz sqlite-autoconf-3490100.tar.gz
    cd sqlite-autoconf-3490100
    ./configure --prefix=/usr/local
    make
    sudo make install
    ```

3. chromadbのベクトルデータを保存するフォルダを作成します。

    ```bash
    mkdir -p data/chromadb
    ```

4. Streamlitアプリケーションを実行します。

    ```bash
    streamlit run app.py
    ```

5. OPENAIのAPIキーをstreamlitcloudで設定します。

    - streamlitcloudの設定ページに移動し、Secretsに`OPENAI_API_KEY`を追加します。