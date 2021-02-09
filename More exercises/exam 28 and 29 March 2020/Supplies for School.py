pen_qty = int(input())
marker_qty = int(input())
detersive_liter = float(input())
discount = int(input())

pack_of_pen = 5.80 * pen_qty
pack_of_marker = 7.20 * marker_qty
detersive_per_liter = 1.20 * detersive_liter
total = pack_of_pen + pack_of_marker + detersive_per_liter
total_sum = total - ((total * discount) / 100)
print(f'{total_sum:.3f}')