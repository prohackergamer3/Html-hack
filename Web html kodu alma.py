import requests as r

sita = input(("Html kodunu almak istediğiniz sitenin adresini girin?\n"))
rt  = r.get("%s"% sita)

code = rt.text

print(code)
