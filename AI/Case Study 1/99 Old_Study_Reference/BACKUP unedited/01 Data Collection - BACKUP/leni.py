import twint

search_terms = [
'#leni',
'#LetLeniLead',
'labanleni',
'#labanleni2022', 
'#LetLeniLead2022',
'labanleni',
'#lenikiko',
'#LeniKiko2022',
'#KulayRosasAngBukas',
'#PasigisPink',
'#PasigLaban',
'#LeniRobredo',
'#DapatSiLeni',
'#Kakampink',
'#pasiglaban',
'#LeniAngatBuhayLahat',
'#Lenisupporters',
'#LeniLugaw',
'#BakitSiLeni',
'#LeniMatapang',
'#LeniFakeVP',
'#Lenilutang',
'#lenimagnanakawngboto',
'#leniwalangkonsensya',
'#lenihalangangkaluluwa',
'#fakevprobredo',
'#pinklawan',
'#lenlen']

def jobone(cStart, cEnd):
    for i in range(len(search_terms)):
        c = twint.Config()
        c.Search = search_terms[i]
        c.Lang = "en"
        c.Since = cStart
        c.Until = cEnd
        c.Limit = 2000
        c.Store_csv = True
        c.Output = "rawleni.csv"

        twint.run.Search(c)

jobone("2022-02-08 00:00:00", "2022-03-22 23:59:00")