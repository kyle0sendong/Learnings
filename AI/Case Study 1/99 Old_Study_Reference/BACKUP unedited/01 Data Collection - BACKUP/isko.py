import twint

search_terms = [
'#yorme',
'#isko',
'#iskoako',
'#iskomorenodomagoso',
'#YormeIsko',
'#IskoMoreno',  
'#SwitchToIsko',
'#KayIskoPosible', 
'#KayISKOPossible', 
'#IskoSupporters',
'#PHVoteDomagoso',
'#2jointsparangMafia',
'#YORMESAPLACER',
'#TunayNaSolusyonMabilisUmaksyon',
'#IskoDocWillie2022',
'#IskoParasaPilipino',
'#ikawnaISKO2022',
'#BilisKilos',
'#IskoMorenoForPresident ',
'#Iskorganic',
'#2Joints',
'#AtrasIsko',
'#IskoDuwag',
'##IskoAtras',
'#IskoTrapo',
'#IskoTanga',
'#NoToTrapos',
'#IskoBobo',
'#IskoManloloko',
'#IskoPunk',
'#LetIskoLeadVietnam',
'#BilisKilosDaw', 
'#LetIskoLeadThePrayer',
'#IskoWithdraw',
'#WithdrawIsko']

def jobone(cStart, cEnd):
    for i in range(len(search_terms)):
        c = twint.Config()
        c.Search = search_terms[i]
        c.Lang = "en"
        c.Since = cStart
        c.Until = cEnd
        c.Limit = 2000
        c.Store_csv = True
        c.Output = "raw_Isko.csv"

        twint.run.Search(c)

jobone("2022-02-08 00:00:00", "2022-03-22 23:59:00")