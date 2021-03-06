def giveFormula(option, budget):
    budget_list = ({
        'name': 'gen1',
        'cpu': 0.35,
        'motherboard': 0.14,
        'memory': 0.15,
        'gpu': 0,
        'storage': 0.15,
        'psu': 0.09,
        'case': 0.12
    },
        {
        'name': 'gen2',
        'cpu': 0.35,
        'motherboard': 0.12,
        'memory': 0.15,
        'gpu': 0,
        'storage': 0.20,
        'psu': 0.08,
        'case': 0.10
    },
        {
        'name': 'game1',
        'cpu': 0.25,
        'motherboard': 0.12,
        'memory': 0.12,
        'gpu': 0.25,
        'storage': 0.10,
        'psu': 0.08,
        'case': 0.08
    },
        {
        'name': 'game2',
        'cpu': 0.22,
        'motherboard': 0.11,
        'memory': 0.12,
        'gpu': 0.28,
        'storage': 0.10,
        'psu': 0.07,
        'case': 0.10
    },
        {
        'name': 'game3',
        'cpu': 0.25,
        'motherboard': 0.11,
        'memory': 0.10,
        'gpu': 0.30,
        'storage': 0.09,
        'psu': 0.07,
        'case': 0.08
    },
        {
        'name': 'game4',
        'cpu': 0.22,
        'motherboard': 0.09,
        'memory': 0.08,
        'gpu': 0.39,
        'storage': 0.09,
        'psu': 0.05,
        'case': 0.08
    },
        {
        'name': 'ws1',
        'cpu': 0.30,
        'motherboard': 0.11,
        'memory': 0.12,
        'gpu': 0.20,
        'storage': 0.10,
        'psu': 0.07,
        'case': 0.10
    },
        {
        'name': 'ws2',
        'cpu': 0.28,
        'motherboard': 0.08,
        'memory': 0.175,
        'gpu': 0.225,
        'storage': 0.09,
        'psu': 0.07,
        'case': 0.08
    },
        {
        'name': 'ws3',
        'cpu': 0.25,
        'motherboard': 0.09,
        'memory': 0.14,
        'gpu': 0.30,
        'storage': 0.11,
        'psu': 0.05,
        'case': 0.06
    },
        {
        'name': 'game_ult',
        'cpu': 0.23,
        'motherboard': 0.08,
        'memory': 0.13,
        'gpu': 0.35,
        'storage': 0.10,
        'psu': 0.05,
        'case': 0.06
    })
    typeList = ["gen", "game", "ws"]
    type = typeList[int(option) - 1]
    for set in budget_list:
        for item in set:
            if set[item] != set['name']:
                set[item] = round(set[item] * budget, 2)

    if type == 'gen':
        if 750 > budget >= 500:
            return budget_list[0]
        elif 1200 > budget >= 750:
            return budget_list[1]
        elif 2000 > budget >= 1200:
            return budget_list[6]
        elif 2000 > budget >= 1500:
            return budget_list[7]
        elif 3000 >= budget >= 2000:
            return budget_list[8]
        elif budget > 3000:
            return budget_list[9]
    elif type == 'game':
        if 1000 > budget >= 700:
            return budget_list[2]
        elif 1500 > budget >= 1000:
            return budget_list[3]
        elif 2000 > budget >= 1500:
            return budget_list[4]
        elif 3000 >= budget >= 2000:
            return budget_list[5]
        elif budget > 3000:
            return budget_list[9]
    elif type == 'ws':
        if 1500 > budget >= 1000:
            return budget_list[6]
        elif 2000 > budget >= 1500:
            return budget_list[7]
        elif 3000 >= budget >= 2000:
            return budget_list[8]
        elif budget > 3000:
            return budget_list[9]
