# 外食先を決めるルーレット

# 命名："ランダムグルメ"

## 概要

- 入力
    - 価格設定
    - アレルギーなど
    - 場所
    - 人数

- 出力
    - お店が三つ出てくる

## ポイント
1. 情報の更新頻度
2. ログイン機能
3. 機械学習機能
    - どこかでいれたい。。
    
 
## 残りやること
1. ~料金での絞り込みを出来るようにする~
    2. **done**
3. ~時間での絞り込みが出来るようにするか、考える~
    4.  むりぽ。。。。
5. フロントをどのように修飾するか調べる
6. 位置情報APIを調べる
    7.  予想より簡単そう。緯度経度を取得して現在地から300mでランダム指定などもできそう。
    8.  https://zenn.dev/sweflo/articles/8c34c081cb764c




## データの流れ
1. 値段、人数の閾値を受け取る
    - ボタン入力時の時刻もサーバーに送る
2. 条件をif文などで書き、APIを使用して主な情報(店名、住所、url、画像など)を取得する
    - 絞り込み
        - 場所での絞り込み
            - APIのmiddle_areaをリスト形式で保持し、ドロップダウンのリストに出力した
        - 料金での絞り込み
            - 場所での絞り込みと同様に行う予定。
        - 時間での絞り込み
            - **難しい**。APIの表記がバラバラである
                - 下記のようにフォーマットが整っていない。
                    - `月～金、祝前日：11:00~14:30 料理L.O.14:00 ドリンクL.O. 13:30) 17:00~22:00 ......`
        
3. 2.絞り込みを行ったうえで、乱数を使用しランダムに飲食店を提示する
    - Flaskのjinjaテンプレートに備わっていたrandom関数を実行した
    
4. ユーザーの現在地から飲食店までの道のりを提示する
    - Googleマップへの誘導を行う？



## やること整理(重要順

- 営業時間を正規表現を用いて整形を試みる
- 茨城県つくば市版も追加する
- googleの位置情報apiを使用する




## 参考
- https://tat-pytone.hatenablog.com/entry/2022/05/04/123755
- https://zenn.dev/kohhee/articles/d4f96624b82e50
- https://www.youtube.com/watch?v=_YeN69XoqqU
- https://zenn.dev/sweflo/articles/8c34c081cb764c
