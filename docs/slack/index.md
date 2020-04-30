# SLACK
  グループチャットアプリケーションSlack（スラック）に対して通知を送る機能を利用する事が可能です。

# SLACKにメッセージを送信する
```bash tab="環境変数からURLを設定する"
export SLACK_WEBHOOK_URL=[SLACK 通知用URL]
noct slack [CHANNEL] [TITLE] [USERNAME] [ICON_EMOJI]
```

```bash tab="コマンド引数からURLを設定する"
noct slack [CHANNEL] [TITLE] [USERNAME] [ICON_EMOJI] --url [SLACK 通知用URL]
```

# URL付きボタンを送信する
```bash
noct slack [チャネル名] --buttons "メッセージ:URL(https://example.com/)"
```

