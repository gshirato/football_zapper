import streamlit as st

st.audio('https://sports-con.xyz/wp-content/uploads/2025/03/20250319-football-zapper-jleague-bundesliga.wav')

st.markdown("""
## 市民社会から見るJリーグの理念の意義と課題 - ブンデスリーガの事例を分析の視点として 2022年

Jリーグとドイツのブンデスリーガの違いについて、市民社会の視点から分析した記事の要約。

### 日本プロスポーツの原型 - 企業主導型の発展

日本のプロ野球は、1936年に企業（新聞社と鉄道会社）によって「上からの制度化」が行われました。この企業主導の組織形態は、親会社の経営不振によってチームが消滅するなど、営利という企業の目的に従属する形で組織されてきました。

日本のプロスポーツは、営利目的の企業によって制度化され、企業の論理に取り込まれる「上からのプロ化」が特徴となっています。観客も「市民（citizen）」としてではなく、「消費者」としてプロスポーツの経済秩序に取り込まれてきました。

### Jリーグの誕生 - 新たな理念の提案

1992年に設立されたJリーグは、企業主導のプロスポーツ組織形態を変えようとしました。設立の中心人物であった川淵三郎と木之本興三は、ドイツをモデルとし、豊かなスポーツ環境を日本で実現させることを目指しました。

川淵三郎によれば、「百年構想」の原点は彼のドイツでの実体験にありました。ドイツのスポーツ施設の充実ぶりと日本のスポーツ環境の差に衝撃を受け、「単にプロサッカーの興行を行うことが目的ではない」という理念を掲げました。

Jリーグは「地域＋愛称」でチーム名を表現するなど、企業中心の組織形態からの脱却を図りましたが、川淵は「企業中心の組織形態を百八十度変えるのは無理がある」と考え、強制することはしませんでした。

### ドイツのプロスポーツモデル - 非営利法人と市民参加

ドイツでは、スポーツクラブは「フェアアイン（非営利法人）」と呼ばれる組織によって運営されています。これらの非営利法人は、地域住民の声を集約し代表することで、企業や行政と対等に交渉する役割を担っています。

ブンデスリーガでは、「50+1ルール」と「クラブ・ライセンス制度」によって、プロサッカークラブの議決権はクラブ会員（実質的には地域住民）に残され、企業が経営破綻してもクラブは存続できる仕組みが構築されています。

例えば、SV ヴェルダー・ブレーメンでは、運営企業がチーム名の使用料として非営利法人に年間約1億円のネーミングライツを支払い、その収入は地域スポーツクラブに還元されます。

### Jリーグの取り組みと日本の社会システム

Jリーグは「シャレン」と呼ばれる社会連携事業を通じて、「地域の人・企業や団体・自治体・学校などとJリーグ・Jクラブが連携して社会課題に取り組む活動」を推進しています。

しかし、日本の社会システムでは、ドイツのように非営利組織が地域住民の意見を集約・代表する位置づけにはなく、NPO法人は地域住民とは別の存在とみなされています。

川淵は企業依存からの脱却のために「地域住民、行政、企業の相互協力」を強調し、株を複数の所有者に分散させ、特に行政の株式所有を理想視していました。これはドイツのモデルとは異なるアプローチです。

### 横浜FCの試み - 日独の法人体系の違い

フリューゲルスの消滅後、サポーターたちは「市民クラブ」づくりに動き始めましたが、日本の法制度ではドイツのような非営利法人による運営が難しく、結局は株式会社形態を選択せざるを得ませんでした。

この「市民の、市民による、市民のためのチーム」を作る試みは、各組織間の意見調整の困難さや制度に対する理解不足などにより空中分解してしまいました。

### 結論 - Jリーグ理念の意義と課題

Jリーグの理念には市民社会との接続の契機が含まれていますが、行政と企業の連携が実現される一方で、市民や非営利組織がプロスポーツクラブの運営にどう関わるかは具体化されてきませんでした。

その背景には、日独の社会システムや法人格を規定する法人体系の違い、そしてドイツの法人体系や社会システムに関する日本での理解不足があります。

## Reference
- [市民社会から見るJリーグの理念の意義と課題－ブンデスリーガの事例を分析の視点として－](https://doi.org/10.9772/jpspe.44.2_69)
""")

# 各トピックを分けるタブを作成
tabs = st.tabs(["日本のプロスポーツ発展", "Jリーグの理念", "ドイツモデル", "日本の課題"])

with tabs[0]:
    st.markdown("""
    ## 日本のプロスポーツ発展の歴史

    ### 「上からの制度化」によるプロスポーツの誕生
    日本のプロ野球は1936年、日本職業野球連盟創立総会において新聞社と鉄道会社によるリーグの編成によって成立しました。菊が「上からの制度化」と表現するように、野球界の外部に存在する企業によって主導されることで、日本のプロ野球は誕生しました。

    ### 企業主導の影響
    - 新聞社：野球を自社の宣伝と販売部数の拡大手段として利用
    - 鉄道会社：自社の宣伝と同時に、沿線にスタジアムを建設し観客を輸送することで利益獲得

    ### 観客の位置づけ
    観客は「市民（citizen）」としてではなく、「消費者」としてプロスポーツの経済秩序に取り込まれました。日本では、ドイツのような非営利法人にみられるような政治的な意識は育まれませんでした。

    ### 市民球団の試み
    「市民球団」と呼ばれた広島東洋カープの設立当初は、運営資金の寄付者に株券が発行され、その株券を持った地域住民によって組織された後援会が強い影響力を持っていました。しかし、東洋工業株式会社の主導により後援会は解散し、地域住民の関与は失われていきました。
    """)

with tabs[1]:
    st.markdown("""
    ## Jリーグの理念とその展開

    ### 設立の背景
    1985年のメキシコW杯予選での韓国との惨敗を機に、日本でもプロリーグを結成しようとする気運が高まりました。その中心的な人物となったのが、川淵三郎と木之本興三という日本サッカーリーグの経験者たちでした。

    ### 百年構想
    川淵によれば、百年構想の原点には彼のドイツでの実体験がありました。ドイツのスポーツ施設の充実ぶりと日本の環境の大きな差を痛感し、「単にプロサッカーの興行を行うことが我々の目的ではない」という理念を掲げました。

    ### 企業名の扱い
    Jリーグはチーム名から企業名を外し、地域名を入れることを提案しました。これは、親会社の名称を入れることで赤字を宣伝広告費として補填してきたプロ野球のシステムからの脱却を図るものでした。

    ### 三位一体の経営構想
    川淵は、企業依存からの脱却のために「地域住民、行政、企業の相互協力が必要不可欠」と強調し、株を複数の所有者に分散させ、特に行政の株式所有を理想視していました。

    ### シャレンの取り組み
    現在のJリーグは「シャレン」と呼ばれる社会連携事業を通じて、「地域の人・企業や団体・自治体・学校などとJリーグ・Jクラブが連携して社会課題に取り組む活動」を推進しています。
    """)

with tabs[2]:
    st.markdown("""
    ## ドイツのスポーツクラブモデル

    ### フェアアイン（非営利法人）の役割
    ドイツでは、地域の非営利組織「フェアアイン」がスポーツクラブを運営しています。これらの非営利法人は、地域住民の声を集約し代表することで、企業や行政と対等に交渉する役割を担っています。

    ### 非営利法人の特徴
    - 会費による運営という自己負担の原則
    - 国家から自立した集団・結社の自由を獲得
    - 公益目的と会員の選挙・総会による議決が法的義務
    - 優遇税制などの制度的支援

    ### 50+1ルールとクラブ・ライセンス制度
    ブンデスリーガでは、1990年代の商業主義化を背景に、営利企業にもクラブ運営が認められるようになりましたが、以下の規制が設けられました：

    - **50+1ルール**：ひとつの企業やオーナーがクラブの議決権の過半数を持つことを禁止
    - **クラブ・ライセンス制度**：議決権を非営利法人が保持するクラブにのみライセンスを付与

    ### 収益の循環システム
    例えば、SV ヴェルダー・ブレーメンでは、運営企業がチーム名の使用料として非営利法人に年間約1億円のネーミングライツを支払い、その収入は地域スポーツクラブに還元されます。この仕組みにより、企業が経営破綻してもクラブは存続できます。
    """)

with tabs[3]:
    st.markdown("""
    ## 日本における課題と横浜FCの事例

    ### 非営利組織の違い
    日本の社会システムでは、ドイツと異なり、非営利組織（NPO法人）が地域住民とは別の存在とみなされています。非営利組織が地域住民の意見を集約・代表する位置づけにはありません。

    ### 法人体系の違い
    日本の非営利法人制度はドイツと大きく異なります。現在のNPO法人法においても優遇税制が認められているのは「認定特定非営利法人」のみであり、その法人格の取得には厳しい条件があります。

    ### 横浜FCの試み
    1998年、フリューゲルスの合併問題後、サポーターたちは「市民クラブ」づくりに挑戦しました。しかし、日本の法制度ではドイツのような非営利法人による運営が難しく、結局は株式会社形態を選択せざるを得ませんでした。

    ### 試みの挫折
    この「市民の、市民による、市民のためのチーム」を作る試みは、以下の理由により挫折しました：

    - ソシオ制度の理念と日本の現実の乖離
    - 運営メンバーの制度理解不足
    - 多様なステークホルダーをひとつの制度に埋め込む中核組織の不在

    ### J.リーグの対応
    合併問題を機に、J.リーグはクラブ・ライセンス制度を導入しましたが、ドイツと異なり「市民の議決権」ではなく「企業の経営破綻からクラブを守る」ことに主眼が置かれました。
    """)
