from json import dump

with open('text_7.txt', 'r', encoding='utf-8') as text7:
    r_list = []
    d_profit = {}
    d_losses = {}
    d_average = {'average_profit': 0.}
    content = text7.readlines()
    for el in content:
        t_list = el.split()
        profit = float(t_list[-2]) - float(t_list[-1])
        if profit >= 0:
            d_profit[t_list[0]] = profit
            d_average['average_profit'] = sum(d_average.values()) + profit
        else:
            d_losses[t_list[0]] = profit
    d_average['average_profit'] = d_average['average_profit'] / len(d_profit.keys())
    d_profit.update(d_losses)
    del d_losses
    r_list.append(d_profit)
    r_list.append(d_average)
print(r_list)

with open('text_7.json', 'w', encoding='utf-8') as text7j:
    dump(r_list, text7j, indent=4, ensure_ascii=False)
