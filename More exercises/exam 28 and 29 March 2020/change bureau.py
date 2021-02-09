bitcoin = int(input())
yuan = float(input())
commission = float(input())

yuan = yuan * 0.15 * 1.76
bitcoin *= 1168
euro = (bitcoin + yuan) / 1.95
commission *= euro * 0.01
total_sum= euro - commission
print(f'{total_sum:.2f}')