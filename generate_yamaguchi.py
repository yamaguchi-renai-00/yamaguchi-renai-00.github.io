import json

with open('/Users/yakushiji/Documents/SITE構築ワークスペース/yamaguchi-lady/index.html', 'r') as f:
    html = f.read()

new_html = """<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="XobACse9XaHFFnl0Vgy35clkNvxYdwOlj73VS5KQYPg" />

    <!-- ===============================
        ★ Meta Description（検索意図に最適化）
    ================================== -->
    <meta name="description"
        content="山口県で真剣な出会いを探している女性向けに、山口在住者限定アプリ「GooDMee(グーミー)」等の人気マッチングアプリ比較・恋活＆婚活のコツ・体験談・初デートにおすすめの山口観光スポットを紹介。山口市・下関・防府など県内の広域な出会い事情や、公的婚活支援サービスも徹底解説！【2026年最新版】">

    <!-- ===============================
        ★ Title（SEO最適化）
    ================================== -->
    <title>山口・女性向け｜恋活・婚活アプリ徹底比較＆体験談【2026年最新版】</title>

    <!-- ===============================
        ★ Keywords
    ================================== -->
    <meta name="keywords" content="山口 婚活, 山口 マッチングアプリ, 山口 出会い, 山口市 出会い, 下関 婚活, 山口県 婚活イベント">

    <!-- ===============================
        ★ OGP（SNSシェア最適化）
    ================================== -->
    <meta property="og:title" content="山口・女性向け｜恋活・婚活アプリ徹底比較【2026年最新版】">
    <meta property="og:description" content="山口県の女性向けに、恋活・婚活アプリ比較、体験談、初デートおすすめスポット、公的支援まで徹底紹介。">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://yamaguchi-renai-site.github.io/">
    <meta property="og:image" content="https://yamaguchi-renai-site.github.io/images/ogp_main.jpg">
    <meta property="og:locale" content="ja_JP">

    <!-- ===============================
        ★ Twitter Card（X対応）
    ================================== -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="山口・女性向け｜恋活・婚活アプリ徹底比較">
    <meta name="twitter:description" content="山口県で出会いを探す女性に向けて、人気アプリ比較・体験談・デートスポットを紹介。">
    <meta name="twitter:image" content="https://yamaguchi-renai-site.github.io/images/ogp_main.jpg">

    <!-- ===============================
        ★ Canonical（重複URL対策）
    ================================== -->
    <link rel="canonical" href="https://yamaguchi-renai-site.github.io/">

    <!-- ===============================
        ★ CSS（高速読み込み）
    ================================== -->
    <link rel="preload" href="style.css" as="style">
    <link rel="stylesheet" href="style.css">

    <!-- ===============================
        ★ 構造化データ
    ================================== -->
    <script type="application/ld+json">
    [
        {
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": "山口女性向けマッチングアプリガイド",
            "url": "https://yamaguchi-renai-site.github.io/"
        },
        {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": "山口・女性向け｜恋活・婚活アプリ徹底比較＆体験談【2026年最新版】",
            "description": "山口県で真剣な出会いを探している女性向けに、山口在住者限定アプリ「GooDMee」やPairsなどの人気マッチングアプリ比較・恋活＆婚活のコツ・体験談・初デートにおすすめの山口観光スポットを紹介。",
            "image": "https://yamaguchi-renai-site.github.io/images/ogp_main.jpg",
            "datePublished": "2026-01-23",
            "dateModified": "2026-01-23",
            "author": {
                "@type": "Organization",
                "name": "山口恋活・婚活サポートガイド"
            }
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [{
                "@type": "ListItem",
                "position": 1,
                "name": "ホーム",
                "item": "https://yamaguchi-renai-site.github.io/"
            }]
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [{
                    "@type": "Question",
                    "name": "山口でもマッチングアプリで本当に出会えるの？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "はい、出会えます！生活圏が広域に分かれやすい山口だからこそ、県内限定アプリなどを活用することで相性の良い相手を探すことができます。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "山口限定アプリのメリットは？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "最大のメリットは「県内在住者に限定できること」です。近隣の生活圏同士でマッチングしやすく、安心感があります。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "県公式の婚活支援と民間アプリ、どう使い分ける？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "公的支援は「相談できる安心感」と「結婚への真剣度」が強み。民間アプリは「圧倒的な母数」と「スピード感」が魅力です。併用がおすすめです。"
                    }
                }
            ]
        },
        {
            "@context": "https://schema.org",
            "@type": "TouristAttraction",
            "name": "角島大橋",
            "description": "エメラルドグリーンの海を渡るドライブデートの聖地。",
            "url": "https://www.google.com/maps/search/?api=1&query=角島大橋"
        },
        {
            "@context": "https://schema.org",
            "@type": "TouristAttraction",
            "name": "瑠璃光寺五重塔",
            "description": "国宝。NYタイムズ選出スポット。夜のライトアップがロマンチック。",
            "url": "https://www.google.com/maps/search/?api=1&query=瑠璃光寺五重塔"
        },
        {
            "@context": "https://schema.org",
            "@type": "TouristAttraction",
            "name": "下関市立しものせき水族館 海響館",
            "description": "関門海峡を背景にしたイルカショーやペンギン展示が人気。",
            "url": "https://www.google.com/maps/search/?api=1&query=海響館"
        },
        {
            "@context": "https://schema.org",
            "@type": "TouristAttraction",
            "name": "秋芳洞",
            "description": "日本最大級の鍾乳洞。天候や季節に左右されないアクティブデート。",
            "url": "https://www.google.com/maps/search/?api=1&query=秋芳洞"
        },
        {
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "name": "LOG COFFEE ROASTERS",
            "address": "山口県山口市",
            "image": "https://placehold.co/400x300/png?text=LOG+COFFEE+ROASTERS"
        },
        {
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "name": "庵 心月",
            "address": "山口県山口市",
            "image": "https://placehold.co/400x300/png?text=Iori+Shingetsu"
        },
        {
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "name": "TAGLINE",
            "address": "山口県下関市",
            "image": "https://placehold.co/400x300/png?text=TAGLINE"
        },
        {
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "name": "晴ル家（ハレルヤ）",
            "address": "山口県下関市",
            "image": "https://placehold.co/400x300/png?text=Hareruya"
        },
        {
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "name": "Migliore Coffee Roasters",
            "address": "山口県防府市",
            "image": "https://placehold.co/400x300/png?text=Migliore"
        },
        {
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "name": "884coffee",
            "address": "山口県周南市",
            "image": "https://placehold.co/400x300/png?text=884coffee"
        }
    ]
    </script>
</head>

<body>
    <header>
        <p class="update-date">更新日：2026年01月23日</p>
    </header>

    <main>
        <!-- ヒーロー画像プレースホルダー -->
        <div class="hero-image-placeholder">
            <img src="images/hero_main.png" alt="山口で出会いを探す女性のイメージ"
                style="width: 100%; height: auto; border-radius: 8px;">
        </div>

        <h1>山口で素敵な出会いを探しているあなたへ</h1>

        <div class="intro">
            <p>仕事や趣味に打ち込む毎日。ふと「そろそろ真剣な恋がしたい」と思うこと、ありませんか？</p>
            <p>山口県は生活圏が「下関・北九州」「山口・防府」「岩国・広島」などに分かれやすく、“自然な出会い”が増えにくいという声も。</p>
            <p>そこで今、山口でもマッチングアプリ活用が現実的な選択肢になっています。</p>
            <p><strong>「まずは無料でスタート」</strong>して、安心・安全を重視しつつ、生活圏に合う出会い方を選びましょう。</p>
        </div>

        <nav id="mokuji" class="toc">
            <h2>目次</h2>
            <ul>
                <li><a href="#featured-app">期待のアプリ（山口限定）</a></li>
                <li><a href="#yamaguchi-jijyo">山口県の出会い事情と攻略法</a></li>
                <li><a href="#ranking">山口の恋活・婚活アプリ人気ランキング</a></li>
                <li><a href="#interview">山口女子の体験談（例）</a></li>
                <li><a href="#public-support">山口県の公的婚活支援サービス</a></li>
                <li><a href="#date-spot">山口版｜初デートにおすすめスポット</a></li>
                <li><a href="#faq">よくある質問（FAQ）</a></li>
                <li><a href="#summary">まとめ</a></li>
            </ul>
        </nav>

        <section id="featured-app" class="section">
            <h2>期待のアプリ（山口限定）</h2>
            <div class="app-ranking">
                <article class="app-item app-item-recommend">
                    <div class="recommend-badge">👑 山口限定</div>
                    <div class="app-header">
                        <h3><a href="https://goodmee.jp/" target="_blank" rel="noopener">GooDMee（グーミー）</a></h3>
                        <p class="app-subtitle">山口県在住者限定の地域密着型マッチングアプリ</p>
                    </div>
                    <div class="app-image-placeholder">
                        <img src="images/goodmee.png" alt="GooDMeeアプリ"
                            style="width: 100%; max-width: 400px; height: auto; border-radius: 8px;">
                    </div>
                    <div class="app-details">
                        <table class="app-table">
                            <tr>
                                <th>ポジショニング</th>
                                <td>山口県在住者限定のマッチングサービス</td>
                            </tr>
                            <tr>
                                <th>ポイント</th>
                                <td>
                                    ・圧倒的な近さ：県内限定マッチング<br>
                                    ・プライバシー：写真公開設定を細かく調整可能<br>
                                    ・MYエッセンス機能：相性を数値で可視化
                                </td>
                            </tr>
                            <tr>
                                <th>特徴</th>
                                <td>生活圏が近い相手と出会える安心感が特徴。</td>
                            </tr>
                        </table>
                    </div>
                    <div class="app-recommend">
                        <h4>上位にランクインする理由</h4>
                        <ul>
                            <li>✨ <strong>山口限定だからこそ安心</strong>：県民限定のため、地元での出会いに集中できます。</li>
                            <li>🔒 <strong>身バレ配慮</strong>：写真公開設定などをきめ細かに調整できるプライバシー保護機能。</li>
                            <li>💡 <strong>相性可視化</strong>：MYエッセンス機能により、あらかじめ相性を数値で確認可能。</li>
                        </ul>
                    </div>
                    <p><a href="https://goodmee.jp/" target="_blank" rel="noopener"
                            class="btn">GooDMee公式サイトはこちら→</a></p>
                </article>
            </div>
            <p class="back-to-toc"><a href="#mokuji">目次に戻る↑</a></p>
        </section>

        <section id="yamaguchi-jijyo" class="section">
            <h2>山口県の出会い事情と攻略法</h2>
            <h3>広域な車社会・生活圏が分かれるからこそのアプローチ</h3>
            <p>山口県での出会い探しにおいて、以下の点がカギとなります。</p>
            <ul>
                <li><strong>生活圏の分断：</strong>「下関・北九州」「山口・防府」「岩国・広島」など、各エリアで生活圏が大きく分かれる広域な車社会です</li>
                <li><strong>真面目・保守的な県民性：</strong>誠実で慎重な層が多いため、プロフィールの充実や真剣なコミュニケーションが好まれます</li>
                <li>このため、中間地点を活用したスマートな待ち合わせや、事前にオンラインでしっかり相互理解を深めることが重要です</li>
            </ul>
            <div class="regional-hubs">
                <h4>主な出会いのエリア</h4>
                <p>下関市、山口市、防府市、周南市、岩国市、宇部市</p>
            </div>
            <p>距離の問題は、県内限定である「GooDMee」などを利用することで、同じ生活圏の人を効率よく探すメリットに変わります。また、NYタイムズにも選出された話題のスポットなど、県内の魅力的な名所をデートの話題や目的地に活用するのもおすすめです。
            </p>
            <p class="back-to-toc"><a href="#mokuji">目次に戻る↑</a></p>
        </section>

        <section id="ranking" class="section">
            <h2>山口の恋活・婚活アプリ人気ランキング</h2>
            <p class="section-note">山口では「地元密着（県内限定）」×「全国規模（母数）」の併用が最強のスタイルです。</p>
            <p>まずは県内限定で安全に始めたいならGooDMee、母数重視でたくさんの人を見たいなら全国アプリ、という使い分けがおすすめです。</p>

            <div class="app-ranking">
                <!-- Rank 1: GooDMee -->
                <article class="app-item">
                    <div class="app-header">
                        <h3><a href="https://goodmee.jp/" target="_blank" rel="noopener">1位：GooDMee（グーミー）</a></h3>
                        <p class="app-subtitle">山口県在住者専用！安心・安全の地元アプリ</p>
                    </div>
                    <div class="app-image-placeholder">
                        <img src="images/goodmee.png" alt="GooDMee アプリ"
                            style="width: 100%; max-width: 400px; height: auto; border-radius: 8px;">
                    </div>
                    <div class="app-details">
                        <table class="app-table">
                            <tr>
                                <th>目的</th>
                                <td>恋活・婚活</td>
                            </tr>
                            <tr>
                                <th>料金</th>
                                <td>女性基本無料</td>
                            </tr>
                            <tr>
                                <th>理由</th>
                                <td>山口在住者限定で、生活圏のミスマッチが起きにくい。<br>写真公開設定の調整などプライバシー配慮が徹底。<br>MYエッセンス機能を用いた相性重視の出会い。</td>
                            </tr>
                        </table>
                    </div>
                    <p><a href="https://goodmee.jp/" target="_blank" rel="noopener" class="btn">GooDMee公式サイトへ→</a>
                    </p>
                </article>

                <!-- Rank 2: Pairs -->
                <article class="app-item">
                    <div class="app-header">
                        <h3>2位：Pairs（ペアーズ）</h3>
                        <p class="app-subtitle">圧倒的な会員数で地方でも出会いやすい</p>
                    </div>
                    <div class="app-image-placeholder">
                        <img src="images/pairs_top.webp" alt="Pairs アプリ"
                            style="width: 100%; max-width: 400px; height: auto; border-radius: 8px;">
                    </div>
                    <div class="app-details">
                        <table class="app-table">
                            <tr>
                                <th>目的</th>
                                <td>恋活・婚活</td>
                            </tr>
                            <tr>
                                <th>料金</th>
                                <td>女性無料（男性有料）</td>
                            </tr>
                            <tr>
                                <th>理由</th>
                                <td>母数が多く、地方でも相手が見つかりやすい。<br>検索・コミュニティ機能で価値観が合う人を探しやすい。</td>
                            </tr>
                        </table>
                    </div>
                </article>

                <!-- Rank 3: Omiai -->
                <article class="app-item">
                    <div class="app-header">
                        <h3>3位：Omiai（オミアイ）</h3>
                        <p class="app-subtitle">真剣な婚活向け</p>
                    </div>
                    <div class="app-image-placeholder">
                        <img src="images/omiai_top.jpg" alt="Omiai アプリ"
                            style="width: 100%; max-width: 400px; height: auto; border-radius: 8px;">
                    </div>
                    <div class="app-details">
                        <table class="app-table">
                            <tr>
                                <th>目的</th>
                                <td>婚活寄り</td>
                            </tr>
                            <tr>
                                <th>料金</th>
                                <td>女性無料（男性有料）</td>
                            </tr>
                            <tr>
                                <th>理由</th>
                                <td>真剣度が高めで、結婚を意識した出会いに向きやすい。<br>プロフィール設計が比較的“婚活”寄り。</td>
                            </tr>
                        </table>
                    </div>
                </article>

                <!-- Rank 4: with -->
                <article class="app-item">
                    <div class="app-header">
                        <h3>4位：with（ウィズ）</h3>
                        <p class="app-subtitle">性格診断・価値観マッチング</p>
                    </div>
                    <div class="app-image-placeholder">
                        <img src="images/with-1.jpg" alt="with アプリ"
                            style="width: 100%; max-width: 400px; height: auto; border-radius: 8px;">
                    </div>
                    <div class="app-details">
                        <table class="app-table">
                            <tr>
                                <th>目的</th>
                                <td>恋活</td>
                            </tr>
                            <tr>
                                <th>料金</th>
                                <td>女性無料（男性有料）</td>
                            </tr>
                            <tr>
                                <th>理由</th>
                                <td>価値観・相性軸でのマッチに強い。<br>会話のきっかけが作りやすい。</td>
                            </tr>
                        </table>
                    </div>
                </article>

                <!-- Rank 5: tapple -->
                <article class="app-item">
                    <div class="app-header">
                        <h3>5位：tapple（タップル）</h3>
                        <p class="app-subtitle">気軽な恋活・趣味でつながる</p>
                    </div>
                    <div class="app-image-placeholder">
                        <img src="images/tapple-1.jpg" alt="tapple アプリ"
                            style="width: 100%; max-width: 400px; height: auto; border-radius: 8px;">
                    </div>
                    <div class="app-details">
                        <table class="app-table">
                            <tr>
                                <th>目的</th>
                                <td>恋活</td>
                            </tr>
                            <tr>
                                <th>料金</th>
                                <td>女性無料（男性有料）</td>
                            </tr>
                            <tr>
                                <th>理由</th>
                                <td>テンポよくやりとりが進みやすい。<br>ライトな恋活〜真剣寄りまで幅広い。</td>
                            </tr>
                        </table>
                    </div>
                </article>
            </div>
            <p class="back-to-toc"><a href="#mokuji">目次に戻る↑</a></p>
        </section>

        <section id="interview" class="section interview-section">
            <div class="section-illustration">
                <img src="images/Interview_2women.png" alt="カフェでの会話イメージ"
                    style="width: 100%; max-width: 600px; height: auto; border-radius: 8px; margin: 0 auto;">
            </div>
            <h2>山口女子の体験談（例）</h2>

            <article class="interview">
                <h3>【山口市 / 30代】NYタイムズ話題デートを満喫♪</h3>
                <div class="interview-content">
                    <p>最近は職場と家の往復ばかりで出会いがありませんでしたが、アプリを利用して同年代の方とマッチング。初回のデートは、NYタイムズでも選出されて話題の「瑠璃光寺五重塔」を案内してもらいました。とてもロマンチックで、山口の良さを再発見しながら話も弾みました！</p>
                </div>
            </article>

            <article class="interview">
                <h3>【20代後半】身バレ防止機能を活用した安心の活動</h3>
                <div class="interview-content">
                    <p>地元でのアプリ利用は知り合いにバレないか不安でしたが、GooDMeeのように写真の公開設定を細かく調整できる機能があるおかげで安心して活動できました。自分のペースで本当に会いたいと思える人にだけ顔を見てもらえるので、精神的な負担が少なかったです。</p>
                </div>
            </article>

            <article class="interview">
                <h3>【下関市 / 30代】広域山口でのスマートな待ち合わせ</h3>
                <div class="interview-content">
                    <p>相手は防府市にお住まいの方でしたが、事前に「中間地点のカフェで会いましょう」とスマートに提案してくれました。お互いの生活圏に配慮してドライブがてら向かったことで、道中の景色も話題になり、初対面でもスムーズに会話を楽しむことができました。</p>
                </div>
            </article>

            <p class="back-to-toc"><a href="#mokuji">目次に戻る↑</a></p>
        </section>

        <section id="public-support" class="section">
            <div class="section-illustration">
                <img src="images/public_support.png" alt="公的支援イメージ"
                    style="width: 100%; max-width: 600px; height: auto; border-radius: 8px; margin: 0 auto;">
            </div>
            <h2>山口県の公的婚活支援サービス</h2>
            <article class="support-item">
                <h3>出逢いませ山口（やまぐち結婚応縁センター）</h3>
                <p class="support-url"><a
                        href="https://www.yamaguchi-kekkon.com/"
                        target="_blank" rel="noopener">https://www.yamaguchi-kekkon.com/</a></p>
                <div class="support-content">
                    <p>山口県運営の安心サービスで、AIマッチングシステムの導入や、県内各所での対面サポートを行っています。</p>
                    <p>さらに、2025年4月から入会金が完全無料化されるため、公的支援の「真剣度」と民間アプリの「気軽さ」を併用して本格的な婚活を進めやすくなっています。</p>
                </div>
                <p><a href="https://www.yamaguchi-kekkon.com/" target="_blank" rel="noopener" class="btn">「出逢いませ山口」公式サイトへ→</a>
                </p>
            </article>
            <p class="back-to-toc"><a href="#mokuji">目次に戻る↑</a></p>
        </section>

        <section id="date-spot" class="section">
            <h2>山口版｜初デートにおすすめスポット</h2>
            <p>山口のデートスポットは、「絶景」「歴史遺産」「レジャー」がキーワード。</p>

            <div class="cafe-list">
                <article class="cafe-item">
                    <h3>角島大橋（下関市）</h3>
                    <p class="cafe-url"><a href="https://www.google.com/maps/search/?api=1&query=角島大橋" target="_blank"
                            rel="noopener">Googleマップで見る</a></p>
                    <div class="map-container">
                        <iframe width="100%" height="250" style="border:0;" loading="lazy" allowfullscreen
                            referrerpolicy="no-referrer-when-downgrade"
                            src="https://maps.google.com/maps?q=角島大橋&output=embed">
                        </iframe>
                    </div>
                    <p>エメラルドグリーンの海を渡るドライブデートの聖地。</p>
                </article>

                <article class="cafe-item">
                    <h3>瑠璃光寺五重塔（山口市）</h3>
                    <p class="cafe-url"><a href="https://www.google.com/maps/search/?api=1&query=瑠璃光寺五重塔" target="_blank"
                            rel="noopener">Googleマップで見る</a></p>
                    <div class="map-container">
                        <iframe width="100%" height="250" style="border:0;" loading="lazy" allowfullscreen
                            referrerpolicy="no-referrer-when-downgrade"
                            src="https://maps.google.com/maps?q=瑠璃光寺五重塔&output=embed">
                        </iframe>
                    </div>
                    <p>国宝。NYタイムズ選出スポット。夜のライトアップがロマンチック。</p>
                </article>

                <article class="cafe-item">
                    <h3>下関市立しものせき水族館 海響館（下関市）</h3>
                    <p class="cafe-url"><a href="https://www.google.com/maps/search/?api=1&query=海響館" target="_blank"
                            rel="noopener">Googleマップで見る</a></p>
                    <div class="map-container">
                        <iframe width="100%" height="250" style="border:0;" loading="lazy" allowfullscreen
                            referrerpolicy="no-referrer-when-downgrade"
                            src="https://maps.google.com/maps?q=海響館&output=embed">
                        </iframe>
                    </div>
                    <p>関門海峡を背景にしたイルカショーやペンギン展示が人気。</p>
                </article>

                <article class="cafe-item">
                    <h3>秋芳洞（美祢市）</h3>
                    <p class="cafe-url"><a href="https://www.google.com/maps/search/?api=1&query=秋芳洞" target="_blank"
                            rel="noopener">Googleマップで見る</a></p>
                    <div class="map-container">
                        <iframe width="100%" height="250" style="border:0;" loading="lazy" allowfullscreen
                            referrerpolicy="no-referrer-when-downgrade"
                            src="https://maps.google.com/maps?q=秋芳洞&output=embed">
                        </iframe>
                    </div>
                    <p>日本最大級の鍾乳洞。天候や季節に左右されないアクティブデート。</p>
                </article>

                <h3 class="area-header">☕ 山口エリアのおすすめカフェ</h3>

                <article class="cafe-item">
                    <h3>LOG COFFEE ROASTERS（山口市）</h3>
                    <p class="cafe-url"><a href="https://www.google.com/maps/search/?api=1&query=LOG+COFFEE+ROASTERS" target="_blank" rel="noopener">Googleマップで見る</a></p>
                    <div class="map-container">
                        <iframe width="100%" height="250" style="border:0;" loading="lazy" allowfullscreen
                            referrerpolicy="no-referrer-when-downgrade"
                            src="https://maps.google.com/maps?q=LOG+COFFEE+ROASTERS+山口&output=embed">
                        </iframe>
                    </div>
                    <div class="cafe-details">
                        <p>本格派コーヒーを楽しめる洗練された空間。</p>
                    </div>
                </article>

                <article class="cafe-item">
                    <h3>庵 心月（山口市）</h3>
                    <p class="cafe-url"><a href="https://www.google.com/maps/search/?api=1&query=庵+心月" target="_blank" rel="noopener">Googleマップで見る</a></p>
                    <div class="map-container">
                        <iframe width="100%" height="250" style="border:0;" loading="lazy" allowfullscreen
                            referrerpolicy="no-referrer-when-downgrade"
                            src="https://maps.google.com/maps?q=庵+心月+山口&output=embed">
                        </iframe>
                    </div>
                    <div class="cafe-details">
                        <p>古民家をリノベーションした隠れ家的な癒やしカフェ。</p>
                    </div>
                </article>

                <article class="cafe-item">
                    <h3>TAGLINE（下関市）</h3>
                    <p class="cafe-url"><a href="https://www.google.com/maps/search/?api=1&query=TAGLINE+下関" target="_blank" rel="noopener">Googleマップで見る</a></p>
                    <div class="map-container">
                        <iframe width="100%" height="250" style="border:0;" loading="lazy" allowfullscreen
                            referrerpolicy="no-referrer-when-downgrade"
                            src="https://maps.google.com/maps?q=TAGLINE+下関&output=embed">
                        </iframe>
                    </div>
                    <div class="cafe-details">
                        <p>モダンな内装と開放的な広場に面したカフェ。</p>
                    </div>
                </article>

                <article class="cafe-item">
                    <h3>晴ル家（ハレルヤ）（下関市）</h3>
                    <p class="cafe-url"><a href="https://www.google.com/maps/search/?api=1&query=晴ル家+下関" target="_blank" rel="noopener">Googleマップで見る</a></p>
                    <div class="map-container">
                        <iframe width="100%" height="250" style="border:0;" loading="lazy" allowfullscreen
                            referrerpolicy="no-referrer-when-downgrade"
                            src="https://maps.google.com/maps?q=晴ル家+下関&output=embed">
                        </iframe>
                    </div>
                    <div class="cafe-details">
                        <p>角島大橋を一望できる絶景テラス席が魅力。</p>
                    </div>
                </article>

                <article class="cafe-item">
                    <h3>Migliore Coffee Roasters（防府市）</h3>
                    <p class="cafe-url"><a href="https://www.google.com/maps/search/?api=1&query=Migliore+Coffee+Roasters" target="_blank" rel="noopener">Googleマップで見る</a></p>
                    <div class="map-container">
                        <iframe width="100%" height="250" style="border:0;" loading="lazy" allowfullscreen
                            referrerpolicy="no-referrer-when-downgrade"
                            src="https://maps.google.com/maps?q=Migliore+Coffee+Roasters+防府&output=embed">
                        </iframe>
                    </div>
                    <div class="cafe-details">
                        <p>落ち着いた雰囲気の自家焙煎コーヒー専門店。</p>
                    </div>
                </article>

                <article class="cafe-item">
                    <h3>884coffee（周南市）</h3>
                    <p class="cafe-url"><a href="https://www.google.com/maps/search/?api=1&query=884coffee" target="_blank" rel="noopener">Googleマップで見る</a></p>
                    <div class="map-container">
                        <iframe width="100%" height="250" style="border:0;" loading="lazy" allowfullscreen
                            referrerpolicy="no-referrer-when-downgrade"
                            src="https://maps.google.com/maps?q=884coffee+周南&output=embed">
                        </iframe>
                    </div>
                    <div class="cafe-details">
                        <p>木の温もりが心地よい、ドライブ途中に最適なスポット。</p>
                    </div>
                </article>
            </div>
            <p class="back-to-toc"><a href="#mokuji">目次に戻る↑</a></p>
        </section>

        <section id="faq" class="section">
            <div class="section-illustration">
                <img src="images/faq_main.png" alt="FAQイメージ"
                    style="width: 100%; max-width: 600px; height: auto; border-radius: 8px; margin: 0 auto;">
            </div>
            <h2>よくある質問（FAQ）</h2>
            <div class="faq-list">
                <article class="faq-item">
                    <h3>Q. 山口でもマッチングアプリで本当に出会えるの？</h3>
                    <div class="faq-answer">
                        <p>A.
                            はい、出会えます！生活圏が広範囲に分かれやすい山口だからこそ、県内限定アプリなどを利用して自身の活動エリアに近い方を探すことが有効です。
                        </p>
                    </div>
                </article>
                <article class="faq-item">
                    <h3>Q. 山口限定アプリのメリットは？</h3>
                    <div class="faq-answer">
                        <p>A.
                            最大のメリットは「県内在住者に限定できること」です。これにより、物理的な距離のミスマッチが減り、実際に会いやすくなります。また身バレ防止機能などが充実しており安全性が高いのもポイントです。
                        </p>
                    </div>
                </article>
                <article class="faq-item">
                    <h3>Q. 県公式の婚活支援と民間アプリ、どう使い分ける？</h3>
                    <div class="faq-answer">
                        <p>A.
                            公的支援は「相談できる安心感」と「結婚への真剣度」が強み。民間アプリは「気軽さ」と「スピード感」が魅力です。どちらか一つではなく、目的に合わせて併用するのが最も効率的でおすすめです。2025年4月からはやまぐち結婚応縁センターが無料化されるなど、公的支援もより利用しやすくなっています。
                        </p>
                    </div>
                </article>
            </div>
            <p class="back-to-toc"><a href="#mokuji">目次に戻る↑</a></p>
        </section>

        <section id="summary" class="section">
            <h2>まとめ｜山口でもアプリでの出会いは十分アリ！</h2>
            <p>生活圏が分かれやすい広域な山口では、“会える距離”や“中間地点の活用”による出会い方が非常に有効です。</p>
            <ul>
                <li>✅ 安心機能（年齢確認、プライバシー管理等）を重視して選ぶ</li>
                <li>✅ まずは山口限定の<strong><a href="https://goodmee.jp/">GooDMee</a></strong>などで安全に始めつつ、全国アプリややまぐち結婚応縁センターの公的支援を併用して母数を補う</li>
            </ul>
            <div class="final-cta">
                <h3>まずは試してみよう</h3>
                <p>あなたの山口での素敵な出会いを応援しています。<br>まずは地域密着アプリから、一歩を踏み出してみませんか？</p>
                <p><a href="https://goodmee.jp/" target="_blank" rel="noopener"
                        class="btn btn-large">GooDMee（グーミー）公式をチェック →</a></p>
            </div>
            <p class="back-to-toc"><a href="#mokuji">目次に戻る↑</a></p>
        </section>

    </main>

    <footer>
        <p>&copy; 2026 山口恋活・婚活サポートガイド. All rights reserved.</p>
        <p class="footer-note">※このサイトは山口県の婚活支援情報などを参考にして作成したメディアです</p>
    </footer>

    <script src="script.js"></script>
</body>

</html>
"""

with open('/Users/yakushiji/Documents/SITE構築ワークスペース/yamaguchi-lady/index.html', 'w') as f:
    f.write(new_html)

print("Updated index.html successfully.")
