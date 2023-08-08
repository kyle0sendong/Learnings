import twint

search_terms = [
'#MannyPacquiao',
'#Pacquiao', 
'#presidentmanny',
'#MannyLito',
'#ForGodAndCountry',
'#PanaloAngMahirap',
'#PanaloAngPilipino'
'#mptayo',
'#mannypacquiaotayo',
'#MannyPacquiaoChristianSupporter'
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
        c.Output = "raw_Manny.csv"

        twint.run.Search(c)

jobone("2022-02-08 00:00:00", "2022-03-22 23:59:00")