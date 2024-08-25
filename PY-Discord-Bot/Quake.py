import aiohttp
from datetime import datetime as ds

async def Quake_info():
    
    async with aiohttp.ClientSession() as session:
        resp = "https://api.p2pquake.net/v2/history?codes=551&limit=1"
        async with session.get(resp) as resp_:
            js_l = await resp_.json()
            hypocenter = js_l[0]["earthquake"]["hypocenter"]["name"] 
            maxint = js_l[0]["earthquake"]["maxScale"]
            depth = js_l[0]["earthquake"]["hypocenter"]["depth"]
            magnitude = js_l[0]["earthquake"]["hypocenter"]["magnitude"]
            date = js_l[0]["earthquake"]["time"]
            type = js_l[0]["issue"]["type"]
            _domesticTsunami = js_l[0]['earthquake']['domesticTsunami']

            info = None #変数を初期化
            shindo = None #変数を初期化
            domesticTsunami = None #変数を初期化
            em_color = None #変数を初期化

            match (maxint):
                case -1: #最大震度が-1(不明)のとき
                    magu = '-'
                    hukasa = '-'
                    depth = "-"
                    shindo = "-"
                    shindo_text = ""
                    em_color = 0x555555 #Embed用の色情報
                case 10: #最大震度が1のとき
                    shindo__ = "1"
                    shindo = "1"
                    shindo_text = ""
                    em_color = 0x00324C #Embed用の色情報
                case 20: #最大震度が2のとき
                    shindo = "2"
                    shindo_text = ""
                    em_color = 0x558937 #Embed用の色情報
                case 30: #最大震度が3のとき
                    shindo = "3"
                    shindo_text = "地震による揺れを感じました。"
                    em_color = 0x007931 #Embed用の色情報
                case 40: #最大震度が4のとき
                    shindo = "4"
                    shindo_text = "地震によるやや強い揺れを感じました。"
                    em_color = 0xEA9201 #Embed用の色情報
                case 45: #最大震度が5弱のとき
                    shindo = "5弱"
                    shindo_text = "地震による強い揺れを感じました。"
                    em_color = 0xC21F24 #Embed用の色情報
                case 50: #最大震度が5強のとき
                    shindo = "5強"
                    shindo_text = "地震による強い揺れを感じました。"
                    em_color = 0x8E0002 #Embed用の色情報
                case 55: #最大震度が6弱のとき
                    shindo = "6弱"
                    shindo_text = "地震による非常に強い揺れを感じました。"
                    em_color = 0x640B6F #Embed用の色情報
                case 60: #最大震度が6強のとき
                    shindo = "6強"
                    shindo_text = "地震による非常に強い揺れを感じました。"
                    em_color = 0x770892 #Embed用の色情報
                case 70: #最大震度が7のとき
                    shindo = "7"
                    shindo_text = "地震による非常に強い揺れを感じました。"
                    em_color = 0x6C02A7 #Embed用の色情報

            tsunamiLevels = {
                'None': 'この地震による津波の心配はありません。',
                'Unknown': '津波の影響は不明です。',
                'Checking': '津波の影響を現在調査中です。',
                'NonEffective': '若干の海面変動が予想されますが、被害の心配はありません。',
                'Watch': 'この地震で津波注意報が発表されています。',
                'Warning': 'この地震で津波警報等（大津波警報・津波警報あるいは津波注意報）が発表されています。'
            }

            if _domesticTsunami in tsunamiLevels:
                domesticTsunami = tsunamiLevels[_domesticTsunami]

            try:
                jmaDatetime = js_l[0]['earthquake']['time']
                jmaDatetime = ds.strptime(jmaDatetime,'%Y/%m/%d %H:%M:%S')
                jmaDatetime = jmaDatetime.strftime('%d日%H時%M分')
            except:
                jmaDatetime = "--日--時--分"

            if (hypocenter == ''):
                singen = '-'
            else:
                singen = f'{hypocenter}'

            if (magnitude == -1):
                magu =  '-'
            else:
                magu = f'M{(magnitude)}'

            if (depth == -1):
                hukasa =  '-'
            else:
                hukasa = f'約{(depth)}km'


            pointsText = "> 各地の震度情報"
            points = [""] * 10
            scales = {
                -1: 9, 10: 8, 20: 7, 30: 6, 40: 5,
                45: 4, 50: 3, 55: 2, 60: 1, 70: 0
            }
            scalesText = {
                -1: '', 10: '1', 20: '2', 30: '3', 40: '4', 45: '5弱', 50: '5強', 55: '6弱', 60: '6強', 70: '7'
            }
            pointNameList = [[] for i in range(10)]

            for point in js_l[0]['points']:
                if point['scale'] in scales:
                    scale = scales[point['scale']]
                    pointName = point['pref']

                    if points[scale] == "":
                        points[scale] = points[scale] + f"\n**[震度{scalesText[point['scale']]}]**"

                    if not(pointName in pointNameList[scale]):
                        pointNameList[scale].append(pointName)
                        points[scale] = points[scale] + f"\n- {pointName}\n"

                    points[scale] = f"{points[scale]} {point['addr']} "

                else:
                    continue

            for point in points:
                pointsText = pointsText + point

            match type:
                case "ScalePrompt":
                    info = "震度速報"
                case "Destination":
                    info = "震源に関する情報"
                case "ScaleAndDestination":
                    info = "震源 ・ 震度に関する情報"
                case "DetailScale":
                    info = "各地の震度に関する情報"
                case "Foreign":
                    info = "遠地地震に関する情報"
                case _:
                    info = "その他"

            Quake_text = (f"[{info}]\n" \
                           "> 発生時刻\n" \
                          f"{jmaDatetime}\n" \
                           "> 震源地\n" \
                          f"{singen}\n" \
                           "> 規模\n" \
                          f"{magu}\n" \
                           "> 深さ\n" \
                          f"{hukasa}\n" \
                           "> 最大震度\n" \
                          f"{shindo}\n" \
                           "> 津波有無\n" \
                          f"{domesticTsunami}\n" \
                          f"{pointsText}"
            )

            return em_color, Quake_text