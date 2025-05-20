gyujt = input("Adja meg mire szeretne gyűjteni: ")
kutyadb= int(input("Add meg hány kutyát sétáltatsz a hétvégén: "))
ora = (kutyadb * 20)//60
perc= (kutyadb * 20)%60
penzossz= kutyadb*700
if penzossz > 5000:
    print(f"Anna {kutyadb} kutyát sétáltatott {ora}ó:{perc}p alatt, ezért {penzossz} Ft-ot kapott. Ez már elég a {gyujt}-re.")
else:
    print(f"Anna {kutyadb} kutyát sétáltatott {ora}ó:{perc}p alatt, ezért {penzossz} Ft-ot kapott. Ez még nem elég a {gyujt}-ra/re.")