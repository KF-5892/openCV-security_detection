# 監視カメラから動体検知

## 概要

openCVを使用して、監視カメラから動きがあった部分を検出。

また、人物が映った箇所のみ抜き出して画像出力。

参考書籍：すぐに使える! 業務で実践できる! Pythonによる AI・機械学習・深層学習アプリのつくり方

### 環境

Google colaboratory

macOS Catalina

使用する動画はこちら　https://pixabay.com/ja/videos/%E6%B3%A5%E6%A3%92-%E3%83%90%E3%83%83%E3%82%B0-%E8%BB%8A-%E7%9B%97%E3%82%80-%E5%88%91%E4%BA%8B-3582/

今回はこちらの動画を「thief.mp4」という名前で使用する。

## カメラ映像から、動きがあった部分を検出

### ターミナルから実行する場合

ターミナルを起動。任意の作業フォルダに移動し、以下を起動

```
git clone -r
pip install -r  requirements.txt
python camera_check.py 
```

実行すると、動画で動きがあった部分に緑の枠線が表示される。

もし、パソコンのWebカメラで実行したい場合は、「camera_check.py」のソースを変更する。カメラから実行した場合、Enterキーで終了する。

```
＃ 動画から取得
cap = cv2.VideoCapture("thief.mp4")
# Webカメラから取得
cap = cv2.VideoCapture(0)
```

## 動きがあった部分を、画像として保存

### googlecolabより実行する場合

googleDrive上で「security_image.ipynb」を実行。以下はファイル内で説明。

### ターミナルから実行する場合

作業フォルダ内で以下を実行

```
python security_image.py
```

実行すると、フォルダ内に「img」フォルダが生成され、内部には動きを検出した画像が保存されている。



## 人物が映った部分のみ保存

画像の中には、フードの画像など、人物以外も含まれているので、人物のみを保存するよう学習させる。

### 準備

#### 訓練データ準備

「img」フォルダ内の画像を人物と、それ以外に振り分ける。

ここでは、作業フォルダ内に「face」「noface」の２つのフォルダを作成。

- 「face」 人物画像
- 「noface」それ以外

上記の分類で振り分ける。

作業フォルダ内に

- face
- noface
- security_train.py(colabの場合は.ipynb)

があれば、準備完了

### 訓練開始

#### googleColaboratoryの場合

security_train.ipynbを実行、以下はファイル内で説明。

#### ターミナルの場合

作業フォルダ内で以下を実行

```
python security_train.py
```

実行すると、学習結果であるsecurity.pklが生成される。

### テスト開始

以下を実行

```
python find_person.py
```

実行すると、「result」フォルダが生成され、人物が映った部分のみが画像として出力される。
