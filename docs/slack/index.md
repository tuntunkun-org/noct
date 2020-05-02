# SLACK
## はじめに
  グループチャットアプリケーションSlack（スラック）に対して通知を送る機能を利用する事が可能です。

## 事前準備
- 「Incoming WebHooks」アプリの有効化

## SLACKにメッセージを送信する
  SLACKにメッセージを送信する際には、環境変数として渡す方法、オプションとして渡す方法があります。

```bash tab="環境変数からURLを設定する"
export SLACK_WEBHOOK_URL=[SLACK 通知用URL]
noct slack [CHANNEL] [TITLE] [USERNAME] [ICON_EMOJI]
```

```bash tab="コマンド引数からURLを設定する"
noct slack [CHANNEL] [TITLE] [USERNAME] [ICON_EMOJI] --url [SLACK 通知用URL]
```

### コマンド引数
  SLACKにメッセージを送信した際には以下のようにSLACK側に通知メッセージが送信されます。

![SLACKへの通知メッセージ送信](./images/slack_command_example.jpeg)

|    | コマンド引数 | 説明                      |
|----|--------------|---------------------------|
|    | CHANNEL      | 送信するSLACKのチャネル名 |
| ①  | TITLE        | タイトル名                |
| ②  | USERNAME     | 表示名                    |
| ③  | ICON_EMOJI   | アイコン                  |

### オプション
#### URL付きボタンを送信する
```bash
noct slack [チャネル名] --buttons "メッセージ:URL(https://example.com/)"
```

