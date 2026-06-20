# MuscleBattle

友達を倒すための筋トレSNS。  
ランキング・バトル・ストリークで、記録するだけじゃ続かない筋トレを「競技」にする。

---

## 画面一覧

| ファイル | 画面 | 状態 |
|---|---|---|
| `frontend/pages/home.html` | ホーム / ランキング | ✅ 完成 |
| `frontend/pages/login.html` | ログイン / 新規登録 | ✅ 完成 |
| `frontend/pages/record.html` | 記録入力 | ✅ 完成 |
| `frontend/pages/battle.html` | バトル詳細 | ✅ 完成 |
| `frontend/pages/ranking.html` | ランキング全体 | ✅ 完成 |
| `frontend/pages/friends.html` | フレンド | ✅ 完成 |

## フォルダ構成

```
MuscleBattle/
├── frontend/
│   ├── pages/        # 各画面のHTML
│   ├── css/          # 共通スタイル（今後分離予定）
│   └── js/           # 共通スクリプト（今後分離予定）
├── backend/          # C# / ASP.NET Core（今後）
├── docs/             # 設計メモ
└── README.md
```

## 技術スタック

- **フロントエンド**: HTML / CSS / JavaScript
- **バックエンド**: C# / ASP.NET Core（予定）
- **DB**: SQL Server / PostgreSQL（予定）
- **バージョン管理**: Git

## デザインカラー

| 変数 | 値 | 用途 |
|---|---|---|
| `--bg` | `#18181f` | ページ背景 |
| `--bg2` | `#22222c` | カード背景 |
| `--bg3` | `#2c2c38` | 入力欄・サブ背景 |
| `--text` | `#f2f2f5` | 本文テキスト |
| `--muted` | `#a0a0b0` | サブテキスト |
| `--accent` | `#e8f000` | メインアクセント（黄緑） |
| `--accent2` | `#ff4f4f` | 警告・煽り（赤） |
| `--accent3` | `#00c9a7` | 成功・達成（緑） |
