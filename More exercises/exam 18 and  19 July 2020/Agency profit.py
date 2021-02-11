company = input()
tickets_qty_adult = int(input())
tickets_qty_child = int(input())
net_price_adult = float(input())
tax_price = float(input())

net_price_child = net_price_adult * 0.30
adult_ticket_final = net_price_adult + tax_price
child_ticket_final = net_price_child + tax_price
total_price = (adult_ticket_final * tickets_qty_adult) + (child_ticket_final * tickets_qty_child)

profit = total_price * 0.20

print(f"The profit of your agency from {company} tickets is {profit:.2f} lv.")