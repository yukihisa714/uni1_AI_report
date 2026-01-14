import streamlit as st
from openai import OpenAI


try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except FileNotFoundError:
    st.error("APIキーが見つかりません。")
    st.stop()


st.title("生徒現状報告書ジェネレーター")


st.markdown("---")


courses = {"6月": "春期講習", "11月": "夏期講習", "2月": "冬期講習"}

ui_name, ui_grade, ui_subject, ui_season = st.columns(4)
with ui_name:
    name = st.text_input("生徒のイニシャル", placeholder="例：AI")
with ui_grade:
    grade = st.selectbox("学年", ["小1", "小2", "小3", "小4", "小5", "小6", "中1", "中2", "中3", "高1", "高2", "高3"])
with ui_subject:
    subject = st.selectbox("科目", ["国語", "数学", "英語", "理科", "社会"])
with ui_season:
    season = st.selectbox("時期", courses.keys())


st.markdown("---")


st.header("学習状況および指導計画")

latest_course = courses[season]


st.subheader("直近の講習の振り返り")

ui_units_learned_in_the_course = st.text_input(f"{latest_course}で重点的に学習した単元・課題", placeholder="例：一次関数")

ui_before_growth_in_the_course = st.text_input("その単元・課題のはじめの状況", placeholder="例：関数の基礎があいまい")

ui_after_growth_in_the_course = st.text_input("その単元・課題の終わりの状況", placeholder="例：関数の基礎問題がスラスラ解けるようになった")

ui_units_developing = st.text_input("改善されたが完全に定着はしていない単元・課題", placeholder="例：図形の証明")


st.subheader("克服課題")

ui_overcome1, ui_overcome1_comprehension, ui_overcome1_proficiency, ui_overcome1_place = st.columns(4)
with ui_overcome1:
    overcome1 = st.text_input("克服単元1", placeholder="例：平方根")
with ui_overcome1_comprehension:
    overcome1_comprehension = st.text_input("克服単元1の理解度", placeholder="例：90%")
with ui_overcome1_proficiency:
    overcome1_proficiency = st.text_input("克服単元1の定着度", placeholder="例：80%")
with ui_overcome1_place:
    overcome1_place = st.text_input("克服単元1の指導場所", placeholder="例：家庭学習")


ui_overcome2, ui_overcome2_comprehension, ui_overcome2_proficiency, ui_overcome2_place = st.columns(4)
with ui_overcome2:
    overcome2 = st.text_input("克服単元2", placeholder="例：三角比")
with ui_overcome2_comprehension:
    overcome2_comprehension = st.text_input("克服単元2の理解度", placeholder="例：85%")
with ui_overcome2_proficiency:
    overcome2_proficiency = st.text_input("克服単元2の定着度", placeholder="例：75%")
with ui_overcome2_place:
    overcome2_place = st.text_input("克服単元2の指導場所", placeholder="例：通常授業")


st.subheader("学ぶチカラ")

power_of_learning = {
    "正答率について": {
        "数学": {"計算の正確さを70%⇒90%にする": ["満点トライアル（１問でも間違えたら始めから）"]},
        "英語": {"単語テストを70%⇒100%覚えきる": ["70%⇒100%に基準を上げる"]},
        "理科": {"用語を70%⇒100%覚えきる": ["70%⇒100%に基準を上げる"]},
        "社会": {"用語を70%⇒100%覚えきる": ["70%⇒100%に基準を上げる"]},
        "国語": {"漢字・語いを70%⇒100%覚えきる": ["70%⇒100%に基準を上げる"]},
    }[subject],
    "集中力について": {
        # "授業中の集中力を30分⇒45分に伸ばす": "",
        "家庭学習の集中力を高める": ["やり終えたら好きなことをする", "学習時間を決める"],
    },
    "本番力について": {
        "テスト本番力を身につける": ["普段から時間を計って解く。模試の活用", "テスト形式に取り組む", "緊張をほぐす言葉を使う"],
    },
    "丸つけ・解き直しについて": {
        "間違えた問題はその日と翌日に必ず解き直しをする": ["家庭学習での徹底", "毎回の授業で解き直しをする", "復習用ノートを活用する"],
        "丸つけの間違いをなくす": ["授業中にも確認する"],
    },
    "ノート力について": {
        "何がどこに書いているかをわかるようにする": ["ページや問題番号を左枠に書く"],
        "途中式を省かず書く": ["毎回授業で徹底する"],
        "途中式を縦に書いていく": ["毎回授業で徹底する"],
        "何をやっているのか分からない（課題）": ["式だけでなく、言葉も書いていく"],
    },
    "習慣力について": {
        "家庭学習習慣をつける": ["取り組む時間を決める", "学習計画表に予定と実行を記す", "塾に毎日自習に来る"],
    },
    "学校の授業について": {
        "学校の授業を聞く": ["塾で予習する", "冷たいようですが○○さん次第です"],
        "学校の授業時間を活用する": ["授業中に自分で教科書と問題集を進める\n↑これは、高校生だけにしてくださいね（^^;\n 中学生には、内申が大切ですから。"],
    },
}

st.markdown("**学ぶチカラA**")
ui_power_of_learning_category1, ui_power_of_learning_issue1, ui_power_of_learning_plan1 = st.columns(3)
with ui_power_of_learning_category1:
    power_of_learning_category1 = st.selectbox("カテゴリー", list(power_of_learning.keys()), key="category1", index=0)
with ui_power_of_learning_issue1:
    power_of_learning_issue1 = st.selectbox("課題", list(power_of_learning[power_of_learning_category1].keys()), key="issue1")
with ui_power_of_learning_plan1:
    power_of_learning_plan1 = st.selectbox("指導案", power_of_learning[power_of_learning_category1][power_of_learning_issue1], key="plan1")

st.markdown("**学ぶチカラB**")
ui_power_of_learning_category2, ui_power_of_learning_issue2, ui_power_of_learning_plan2 = st.columns(3)
with ui_power_of_learning_category2:
    power_of_learning_category2 = st.selectbox("カテゴリー", list(power_of_learning.keys()), key="category2", index=1)
with ui_power_of_learning_issue2:
    power_of_learning_issue2 = st.selectbox("課題", list(power_of_learning[power_of_learning_category2].keys()), key="issue2")
with ui_power_of_learning_plan2:
    power_of_learning_plan2 = st.selectbox("指導案", power_of_learning[power_of_learning_category2][power_of_learning_issue2], key="plan2")

st.markdown("**学ぶチカラC**")
ui_power_of_learning_category3, ui_power_of_learning_issue3, ui_power_of_learning_plan3 = st.columns(3)
with ui_power_of_learning_category3:
    power_of_learning_category3 = st.selectbox("カテゴリー", list(power_of_learning.keys()), key="category3", index=2)
with ui_power_of_learning_issue3:
    power_of_learning_issue3 = st.selectbox("課題", list(power_of_learning[power_of_learning_category3].keys()), key="issue3")
with ui_power_of_learning_plan3:
    power_of_learning_plan3 = st.selectbox("指導案", power_of_learning[power_of_learning_category3][power_of_learning_issue3], key="plan3")


st.subheader("進度状況とスケジュール")

ui_class_status, ui_class_progress = st.columns(2)
with ui_class_status:
    class_status = st.text_input("現在の授業状況", placeholder="例：学校の予習")
with ui_class_progress:
    class_progress = st.selectbox("授業の進み具合", ["概ね順調", "やや遅れている"])

if (class_progress == "やや遅れている"):
    ui_reason_for_delay = st.text_input("遅れの理由", placeholder="例：学校行事が多かったため")
else:
    ui_reason_for_delay = "特になし"

ui_schedule_end_date = st.text_input("カリキュラム終了予定時期", placeholder="例：12月末～1月上旬")

ui_next_phase, ui_next_phase_teaching_material = st.columns(2)
with ui_next_phase:
    next_phase = st.text_input("今後の方針", placeholder="例：入試対策")
with ui_next_phase_teaching_material:
    next_phase_teaching_material = st.text_input("使用予定の教材（ある場合）", placeholder="例：入試過去問")



def generate_situation_and_plan():
    
    # 季節のマッピングを明確化（AIへの指示用）
    season_mapping = {
        "夏": "6月面談用（春期講習の振り返り）",
        "冬": "11月面談用（夏期講習の振り返り）",
        "春": "2月面談用（冬期講習の振り返り）"
    }
    target_template = season_mapping.get(season, "汎用テンプレート")

    # システムプロンプト：役割とテンプレート定義
    system_prompt = f"""
あなたは学習塾のベテラン講師です。保護者面談用の「生徒現状報告書」を作成してください。
以下の指示とテンプレートに従い、丁寧で論理的、かつ保護者が安心できるトーンで文章を生成してください。
冒頭の挨拶（「保護者様」「お世話になっております」など）は一切書かないでください。
末尾の結び（「よろしくお願いいたします」「敬具」など）も一切書かないでください。

## 全体ルール
- 文体は「です・ます」調で統一する。
- 記号（●や【】）の形式はテンプレートを厳守する。
- LaTeX形式の数式は使わず、一般的なテキスト表記にする。

## テンプレート選択指示
現在の設定時期は「{season}」です。したがって、「{target_template}」の構成を使用してください。

---
### テンプレートA：6月面談用（時期：夏 / 振り返り：春期講習）
【現在の学習状況および克服課題】
●春期講習では【入力された単元】を学びました。はじめは～（Before）だったのが、～（After）までできるようになりました。ここで学んだことは、現在の学習につながっています。●【改善中の単元】は改善傾向ですが、まだ定着には至っていないため、時期をおいて復習する予定です。●克服単元としては、【克服単元1】（理解度、定着度）、【克服単元2】などが挙げられます。また、今後高めていく学習力として「A：【学ぶチカラ課題1】」「B：【学ぶチカラ課題2】」「C：【学ぶチカラ課題3】」が挙げられます。●現在、授業は【授業状況】で進めていて、【進捗】です。（遅れている場合は理由も記述）

【今後の指導計画および目標】
●テスト後、通常授業では予習を進めていきます。【カリキュラム終了時期】に終わる予定です。●克服課題の【克服単元1】などは家庭学習や【克服場所】で反復していきます。●学習力については、「A：【学ぶチカラ指導案1】」「B：【学ぶチカラ指導案2】」「C：【学ぶチカラ指導案3】」に取り組んでいきましょう。●【今後の方針】として【使用教材】などに取り組んでいきます。

---
### テンプレートB：11月面談用（時期：冬 / 振り返り：夏期講習）
【現在の学習状況および克服課題】
●夏期講習では【入力された単元】を学びました。はじめは～（Before）だったのが、～（After）までできるようになりました。これは～という成果につながりました。●【改善中の単元】は改善されましたが、入試に向けて復習が必要です。●克服単元としては、【克服単元1】（理解度、定着度）などが挙げられます。また、今後高めていく学ぶチカラとして「A：【学ぶチカラ課題1】」「B：【学ぶチカラ課題2】」「C：【学ぶチカラ課題3】」が挙げられます。●現在、【授業状況】で進めていて、【進捗】です。（遅れている場合は理由も記述）

【今後の指導計画および目標】
●後期中間テスト後、通常授業では予習を進めていきます。内容は【カリキュラム終了時期】に終わる予定です。その後は【今後の方針】に入ります。●克服課題の【克服単元1】などは【克服場所】で、冬期講習などで復習し、入試レベルまで引き上げます。●学ぶチカラについては、「A：【学ぶチカラ指導案1】」「B：【学ぶチカラ指導案2】」「C：【学ぶチカラ指導案3】」に取り組んでいきましょう。●【使用教材】などにも取り組んでいきます。

---
### テンプレートC：2月面談用（時期：春 / 振り返り：冬期講習）
【現在の学習状況および克服課題】
●冬期講習では【入力された単元】の理解を深め、～（After）の状態になりました。（Beforeにも触れる）。●課題として【改善中の単元】などが残っています。●それ以外の克服課題として、【克服単元1】（理解度、定着度）などが挙げられます。また、今後高めていく学ぶチカラとして「A：【学ぶチカラ課題1】」「B：【学ぶチカラ課題2】」「C：【学ぶチカラ課題3】」が挙げられます。●現在、【授業状況】で進めていて、【進捗】です。（遅れている場合は理由も記述）

【今後の指導計画および目標】
●完全な受験体制/進級準備に入るため、学校内容を扱う時間は調整し、【今後の方針】を中心に行います。●【使用教材】などを使用予定です。●克服課題の【克服単元1】は【克服場所】で、【克服単元2】は春期講習で復習していきましょう。●学ぶチカラについては「A：【学ぶチカラ指導案1】」「B：【学ぶチカラ指導案2】」「C：【学ぶチカラ指導案3】」に取り組んでいきましょう。●次学年になる前に、自覚と生活習慣を確立することを目指します。
"""

    # ユーザープロンプト：変数の注入
    user_prompt = f"""
以下の生徒情報を元に、テンプレートを埋めて報告書を作成してください。

# 生徒情報
- 生徒名: {name}
- 学年: {grade}
- 科目: {subject}
- 時期設定: {season} ({latest_course}の振り返り)

# 1. 講習の振り返り
- 重点単元: {ui_units_learned_in_the_course}
- Before: {ui_before_growth_in_the_course}
- After: {ui_after_growth_in_the_course}
- 改善中・未定着: {ui_units_developing}

# 2. 克服課題
- 単元1: {overcome1} (理解: {overcome1_comprehension}, 定着: {overcome1_proficiency}) -> 指導場所: {overcome1_place}
- 単元2: {overcome2} (理解: {overcome2_comprehension}, 定着: {overcome2_proficiency}) -> 指導場所: {overcome2_place}

# 3. 学ぶチカラ（以下の文言をそのまま使用すること）
- A:
    課題: {power_of_learning_issue1}
    対策: {power_of_learning_plan1}
- B:
    課題: {power_of_learning_issue2}
    対策: {power_of_learning_plan2}
- C:
    課題: {power_of_learning_issue3}
    対策: {power_of_learning_plan3}

# 4. 進度・スケジュール
- 授業状況: {class_status}
- 進み具合: {class_progress}
- 遅れの理由: {ui_reason_for_delay}(やや遅れている場合のみ)
- 終了予定: {ui_schedule_end_date}
- 今後の方針: {next_phase}
- 使用教材: {next_phase_teaching_material}
"""

    return system_prompt, user_prompt


# --- 実行部分のイメージ ---
# --- 生成ボタンと処理 ---
st.markdown("---")

button_situation_and_plan = st.button("学習状況および指導計画を生成", type="primary")

if button_situation_and_plan:
    # 1. 入力チェック（バリデーション）
    # 必須項目のリスト（変数名と表示名をペアにする）
    required_fields = [
        (name, "生徒のイニシャル"),
        (ui_units_learned_in_the_course, f"{latest_course}で重点的に学習した単元"),
        (ui_before_growth_in_the_course, "はじめの状況"),
        (ui_after_growth_in_the_course, "終わりの状況"),
        (ui_units_developing, "改善されたが完全に定着はしていない単元"),
        (overcome1, "克服単元1"),
        (overcome1_comprehension, "克服単元1の理解度"),
        (overcome1_proficiency, "克服単元1の定着度"),
        (overcome1_place, "克服単元1の指導場所"),
        (overcome2, "克服単元2"),
        (overcome2_comprehension, "克服単元2の理解度"),
        (overcome2_proficiency, "克服単元2の定着度"),
        (overcome2_place, "克服単元2の指導場所"),
        (class_status, "現在の授業状況"),
        (ui_schedule_end_date, "カリキュラム終了予定時期"),
        (next_phase, "今後の方針")
    ]
    
    # 未入力の項目を探す
    missing_items = [label for value, label in required_fields if not value]

    if missing_items:
        # 未入力がある場合、警告を出して処理を止める
        st.error(f"以下の必須項目が入力されていません：\n\n- " + "\n- ".join(missing_items))
    else:
        # 2. 処理実行（スピナー表示）
        with st.spinner("学習状況および指導計画を生成中..."):
            
            # プロンプト作成関数の呼び出し（前のステップで作成した関数）
            sys_msg, usr_msg = generate_situation_and_plan()

            # OpenAI APIの呼び出し
            try:
                # client = openai.OpenAI() # APIキーは環境変数等で設定済みとする
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": sys_msg},
                        {"role": "user", "content": usr_msg}
                    ],
                    temperature=0.7
                )
                generated_text = response.choices[0].message.content
                
                # 成功メッセージと結果の表示
                st.success("作成が完了しました！")
                st.markdown("### 生成された報告書")
                st.text_area("コピー用", generated_text, height=500)
                
            except Exception as e:
                st.error(f"エラーが発生しました: {e}")



st.markdown("---")

st.header("生徒へのメッセージ")

ui_message = st.text_area("生徒へのメッセージ・強み（箇条書き推奨）", height=150, placeholder="・集中力が高く、最後まで頑張る力がある\n・質問が積極的")


def generate_message():
    # システムプロンプト：役割とテンプレート定義
    system_message = """
あなたは生徒のやる気を引き出すプロの塾講師です。以下の #手順 を忠実に守って、前向きで励ましの言葉を使いながら、生徒が自信を持てるような生徒現状報告書のメッセージを書いてください。

#手順
・出力する前に、何文字になったかをカウントしてください。
・カウントした結果、#文字数 の条件を満たしていることが確認できた場合に限ってタスクを終了してください。
・カウントした結果、#文字数 の条件を満たしていない場合は、#文字数 の条件を満たせるまで文字を追加したり削除して処理を繰り返してください。

＃文字数
・下限：330字
・上限：370字
"""

    # ユーザープロンプト：変数の注入
    user_message = f"""
以下の情報を元に、生徒へのメッセージを作成してください。

# 生徒情報
- 生徒名: {name}
- 学年: {grade}
- 科目: {subject}
- 時期設定: {season} ({latest_course}の振り返り)

# 1. 生徒へのメッセージ・強み
- {ui_message}
"""

    return system_message, user_message


button_message = st.button("生徒へのメッセージを生成", type="primary")

if button_message:
    required_fields = [
        (name, "生徒のイニシャル"),
        (ui_message, "生徒へのメッセージ・強み"),
    ]
    missing_items = [label for value, label in required_fields if not value]
    if missing_items:
        st.error(f"以下の必須項目が入力されていません：\n\n- " + "\n- ".join(missing_items))
    else:
        sys_msg, usr_msg = generate_message()

        with st.spinner("メッセージを生成中..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": sys_msg},
                        {"role": "user", "content": usr_msg}
                    ],
                    temperature=0.7
                )

                result = response.choices[0].message.content
                st.success("作成が完了しました！")
                st.markdown("### 生成されたメッセージ")
                st.text_area("コピー用", result, height=300)

            except Exception as e:
                st.error(f"エラー: {e}")
