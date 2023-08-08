import twint

search_terms = [
    '#pinglacson',
    '#lacson',
    '#PingLacsonForPresident',
    '#PingLacsonForPresident2022',
    '#5PresidentePingLacson',
    '#PingLacson2022',
    '#PingGaling',
    '#PingGaling2022',
    '#PingDigmaan', 
    '#PingDigmaan2022', 
    '#WeNeedALeader',
    '#SinongPangGiyeraMo',
    '#SinongPangGiyeraMo2022',
    '#TeamLacsonSotto'
    '#TeamLacsonSotto2022'
    '#LacsonSottoPanaloTayo',
    '#LacsonSottoTayo',
    '#TuloyAngLaban'
    ]


def jobone(cStart, cEnd):
    for i in range(len(search_terms)):
        c = twint.Config()
        c.Search = search_terms[i]
        c.Lang = "en"
        c.Since = cStart
        c.Until = cEnd
        c.Limit = 2000
        c.Store_csv = True
        c.Output = "raw_Lacson.csv"

        twint.run.Search(c)

jobone("2022-02-08 00:00:00", "2022-03-22 23:59:00")
