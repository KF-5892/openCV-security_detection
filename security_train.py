import cv2
import os, glob
import joblib
from sklearn.model_selection import train_test_split
from sklearn import datasets, metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# 画像の学習サイズやパスを指定
image_size = (64, 32)
path = os.path.dirname(os.path.abspath(__file__))
path_fish = path + '/face'
path_nofish = path + '/noface'
x = [] # 画像データ
y = [] # ラベルデータ

# 画像データを読み込んで配列に追加 --- (*1)
def read_dir(path, label):
    files = glob.glob(path + "/*.jpg")
    for f in files:
        img = cv2.imread(f)
        img = cv2.resize(img, image_size)
        img_data = img.reshape(-1, ) # 一次元に展開
        x.append(img_data)
        y.append(label)

# 画像データを読み込む
read_dir(path_nofish, 0)
read_dir(path_fish, 1)

# データを学習用とテスト用に分割する
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# データを学習 
clf = RandomForestClassifier()
clf.fit(x_train, y_train)

# 精度の確認 
y_pred = clf.predict(x_test)
print(accuracy_score(y_test, y_pred))

# データを保存 
joblib.dump(clf, 'security.pkl')
