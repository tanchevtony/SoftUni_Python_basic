easter_bread_qty = int(input())
eggs_pack = int(input())
cookies_kg = int(input())

easter_bread = easter_bread_qty * 3.2  # for one
eggs = eggs_pack * 4.35  # pack 12 eggs
cookies = cookies_kg * 5.4
paint_for_eggs = eggs_pack *( 12 * 0.15)

total = easter_bread + eggs + cookies + paint_for_eggs
print(f"{total:.2f}")