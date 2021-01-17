skumria = float(input())
caca = float(input())
palamud = float(input())
safrid = float(input())
midi = float(input())

palamud_price = skumria + skumria * (60 / 100)
safrid_price = caca + caca * (80 / 100)
midi_price = 7.50

sum_midi = midi_price * midi
sum_safrid = safrid_price * safrid
sum_palamud = palamud_price * palamud

total_bill = sum_midi + sum_palamud + sum_safrid
print(f"{total_bill:.2f}")
