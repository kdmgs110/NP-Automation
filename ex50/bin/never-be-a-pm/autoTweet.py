# -*- coding: utf-8 -*-
import tweepy 
import random # ランダムでツイートを選ぶときに使う
"""
Procedure
* Sign in Twitter Accout
* Make list object that contains tweet content
* Randomly select one tweet content, and tweet
* automate tweeting 
"""
# First, sign in to Twitter API 

# 各種キーをセット
CONSUMER_KEY = 'psWut2vFh9e1dX0gCV5ICj5rk'
CONSUMER_SECRET = '5MXkpqqEe00Kn5ue1Ie6esBpQa8ocNub7gBCSGXqc4ylNmiMFp'
ACCESS_TOKEN = '718015800133586944-owT6LAObdpEesmHiWbsv80P3acRsmeI'
ACCESS_SECRET = 'sIPWThSDgTB2pp8l3f5d1Na7w7KXkk6sjI4Dww1g0HwFj'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

#APIインスタンスを作成

api = tweepy.API(auth)

#ツイートをリストに格納

tweets = [
      #''' 1'''  
              "【Python初心者向け】データの取得・操作・結合・グラフ化をStep by Stepでやってみる - pandas, matplotlib - #はてなブログ" #1 
              + "{}".format("http://review-of-my-life.blogspot.com/2017/09/python-data-analyse.html"),

      #''' 2'''  
              "【R】テキストマイニングを利用して、東京ちんこ倶楽部と暇な女子大生を分析する　#はてなブログ" #2
              + "{}".format("http://review-of-my-life.blogspot.com/2017/08/r-text-mining.html"),
        
      #''' 3'''  
              "【ノンプログラマでも5分でできる】面倒な情報収集はGoogle Spreadsheetに自動でやらせよう　#はてなブログ" #3
              + "{}".format("http://review-of-my-life.blogspot.com/2017/07/google-spreadsheet-information.html"),
              
      #''' 4'''  
              "次に私は小論文を書くことを教えようとしました。でもそれはまず不可能だとわかりました。学生たちは単に押し付けられた考え方に従うだけだったのです。#はてなブログ " #4
              + "{}".format("http://review-of-my-life.blogspot.jp/2017/06/python-cloud9-automatically-execute-python-program.html"),
              
      #''' 5'''  
              "【Pythonで定期処理】 Cloud9を利用して、Seleniumでherokuから定期実行する　#はてなブログ" #5
              + "{}".format("http://review-of-my-life.blogspot.jp/2017/06/python-cloud9-automatically-execute-python-program.html"),

      #''' 6'''  
              "PythonでTinder APIを使ってネトストとサイバーナンパ師やってみた　#はてなブログ" #6
              + "{}".format("http://review-of-my-life.blogspot.jp/2017/06/pythontinder-api-cyber-hockup.html"),
        
      #''' 7'''  
              "PythonでTinderのAPIをいじる　#はてなブログ" #7
              + "{}".format("http://review-of-my-life.blogspot.jp/2017/06/get-tinder-api-by-python.html"),
              
      #''' 8'''  
              "『Pythonによるスクレイピング&機械学習 開発テクニック』レビュー #はてなブログ" #4
              + "{}".format("http://review-of-my-life.blogspot.com/2017/09/python-scraping.html"),
      
      #''' 9'''  
              "金がないのにFacebook広告を無駄に運用してみた  #はてなブログ" #5
              + "{}".format("http://review-of-my-life.blogspot.jp/2017/09/facebook-pr-for-individual-blog.html"),

      #''' 10'''  
              
            "『無敵の思考 ---誰でも得する人になれるコスパ最強のルール21』ひろゆきの書評を書いてみた  #はてなブログ" #6
              + "{}".format("http://review-of-my-life.blogspot.com/2017/08/hiroyuki-book.html"),
        
      #''' 11'''  
              "スマホで読書しない人生なんて絶対にもったいない！！ #はてなブログ" #7
              + "{}".format("http://review-of-my-life.blogspot.com/2017/07/kindle-on-mobile-is-way-better.html"),
              
      #''' 12'''  
              "就活して最後の最後に気付いた、誰も教えてくれなかった3つのこと" #4
              + "{}".format("http://review-of-my-life.blogspot.jp/2017/07/3-things-no-one-told-me-.html"),

      #''' 13'''  
              "【学校不要論】頭いい人にとって義務教育はいらないという真実 #はてなブログ" #5
              + "{}".format("http://review-of-my-life.blogspot.com/2017/03/noHighSchool.html"),

      #''' 14'''  
              "【保存版】相関分析・重回帰分析・クロス集計の結果を、英語でレポートするためのテンプレート  #はてなブログ" #6
              + "{}".format("http://review-of-my-life.blogspot.jp/2017/01/howToReportStats.html") ,
              
                  
      #''' 15'''  
              "脚本から興行収入を事前に予測できる？『機械脳の時代』（加藤エルテス）を読んでみました  #はてなブログ" #7
              + "{}".format("http://review-of-my-life.blogspot.jp/2017/09/machine-brain.html"),
              
      #''' 16'''  
              "企業内保育の何がすごいのか  #はてなブログ" #4
              + "{}".format("http://review-of-my-life.blogspot.jp/2017/08/kindergarten-in-company.html"),

      #''' 17'''  
              "【本屋の社会学】専門書を安く買いたければ、教育所得水準の高い地域の本屋へ行こう #はてなブログ" #5
              + "{}".format("http://review-of-my-life.blogspot.jp/2017/06/go-bookstore-and-you-can-see-educational-and-income-level.html"),

      #''' 18'''  
              "英語を学ぶべきたった一つの理由" #6
              + "{}".format("http://review-of-my-life.blogspot.com/2017/05/the-reason-why-we-should-learn-english.html"),
              
      #''' 19'''  
              "【データで見る】性的少数者（LGBT）がどれだけ差別されているか調べてみた  #はてなブログ" #7
              + "{}".format("http://review-of-my-life.blogspot.jp/2017/04/lgbt-is-difficult.html"),
              
      #''' 20'''  
              "【歴史でひも解く】なぜ日本の義務教育は画一的なのか  #はてなブログ" #4
              + "{}".format("http://review-of-my-life.blogspot.jp/2017/04/WhyEducationIsSoUniform.html"),

      #''' 21'''  
              "【英語を話せる外国から学ぶ】なぜ日本人は英語を話せないのか #はてなブログ" #5
              + "{}".format("http://review-of-my-life.blogspot.jp/2017/04/JapaneseDonotLearnEnglish.html"),

      #''' 22'''  
              "【顔面格差】イケメンとブサメンの年収格差がやばい件について" #6
              + "{}".format("http://review-of-my-life.blogspot.jp/2017/04/goodLookingEarnMore.html"),
              
      #''' 22'''  
              "【データで見る】性的少数者（LGBT）がどれだけ差別されているか調べてみた  #はてなブログ" #7
              + "{}".format("http://review-of-my-life.blogspot.jp/2017/03/isRecruitmentByAcademicCredentialValid.html"),
              
      #''' 23'''  
              "学歴フィルターは差別なのか考えてみた  #はてなブログ" #4
              + "{}".format("http://review-of-my-life.blogspot.jp/2017/04/WhyEducationIsSoUniform.html"),

      #''' 24'''  
              "【マシュマロテスト・ペリー幼稚園・GRIT】教育学全般の面白い研究まとめ(心理学・社会学・経済学領域） #はてなブログ" #5
              + "{}".format("http://review-of-my-life.blogspot.jp/2017/01/interestingStudyOnEducation.html"),

      #''' 25'''  
              "東大生もハーバード生も、親の年収が頭おかしい件について" #6
              + "{}".format("http://review-of-my-life.blogspot.jp/2016/12/UniversityOfTokyoVsHarvard.html"),
              
      #''' 26'''  
              "教育格差の再生産：人生は想像以上にただの課金ゲーだった話 #はてなブログ" #4
              + "{}".format("http://review-of-my-life.blogspot.jp/2017/04/WhyEducationIsSoUniform.html"),

      #''' 27'''  
              "【大学4年間を振り返る】そもそも、大学に行く意味はあるのか？大学に行く2つのメリット #はてなブログ" #5
              + "{}".format("http://review-of-my-life.blogspot.jp/2016/05/4.html"),

      #''' 22'''  
              "【顔面格差】イケメンとブサメンの年収格差がやばい件について" #6
              + "{}".format("http://review-of-my-life.blogspot.jp/2016/12/educationismoney.htmll"),
              
      #''' 22'''  
              "【データで見る】性的少数者（LGBT）がどれだけ差別されているか調べてみた  #はてなブログ" #7
              + "{}".format("http://review-of-my-life.blogspot.jp/2017/03/isRecruitmentByAcademicCredentialValid.html"),
              
      #''' 23'''  
              "学歴フィルターは差別なのか考えてみた  #はてなブログ" #4
              + "{}".format("http://review-of-my-life.blogspot.jp/2017/04/WhyEducationIsSoUniform.html"),

      #''' 24'''  
              "【マシュマロテスト・ペリー幼稚園・GRIT】教育学全般の面白い研究まとめ(心理学・社会学・経済学領域） #はてなブログ" #5
              + "{}".format("http://review-of-my-life.blogspot.jp/2017/01/interestingStudyOnEducation.html"),

      #''' 25'''  
              "東大生もハーバード生も、親の年収が頭おかしい件について" #6
              + "{}".format("http://review-of-my-life.blogspot.jp/2016/12/UniversityOfTokyoVsHarvard.html"),
              
        
      
        ]

try:
    tweet = random.choice(tweets) 
    print("以下のツイートを取得しました。ツイートを開始します。：　{}:".format(tweet))
    api.update_status(tweet)
    print("成功しました！")  
except Exception as e:
    print("ツイートに失敗しました:{}".format(e))
