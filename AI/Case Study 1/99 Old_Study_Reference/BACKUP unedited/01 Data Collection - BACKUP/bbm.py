import twint

search_terms = [
    '#BBMismypresident',
    '#BringBackMarcos',
    '#Solidbbm',
    '#SolidLBM',
    '#LabanMarcos',
    '#labanBBM',
    '#DIKAMIBAYAD',
    '#ayawnaminsafakenews',
    '#notobbm',
    '#notouniteam',
    '#notobbmsara',
    '#BBM',
    '#FerdinandMarcosJr.',
    '#Bongbong',
    '#uniteamBbmsara',
    '#bbmsapagbabago',
    '#BBMSARAlangSAKALAM',
    '#BBMPARASAPAGBABAGO',
    '#BBMSaraUNITEAM',
    '#BBMSaraUNITEAM2022',
    '#BongbongForPresident',
    '#BongbongForPresident2022',
    '#BongbongmarcosForPresident'
    '#BBMSARA2022',
    '#bongbongmarcos2022',
    '#bongbongmarcos',
    '#BBMForPresident',
    '#BBMForPresident2022',
    '#UniTeam',
    '#MarcosDuwag',
    '#MarcosMagnanakaw']


def jobone(cStart, cEnd):
    for i in range(len(search_terms)):
        c = twint.Config()
        c.Search = search_terms[i]
        c.Lang = "en"
        c.Since = cStart
        c.Until = cEnd
        c.Limit = 2000
        c.Store_csv = True
        c.Output = "aa.csv"

        twint.run.Search(c)

jobone("2022-03-22 00:00:00", "2022-03-22 23:59:00")
