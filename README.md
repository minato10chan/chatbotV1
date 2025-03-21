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

2. Streamlitアプリケーションを実行します。

    ```bash
    streamlit run app.py
    ```

3. OPENAIのAPIキーをstreamlitcloudで設定します。

    - streamlitcloudの設定ページに移動し、Secretsに`OPENAI_API_KEY`を追加します。