import random  # 1

def get_answer(answer_number):  # 2
    if answer_number == 1:  # 3
        return 'たしかにそうだ'
    elif answer_number == 2:
        return '間違いなくそうだ'
    elif answer_number == 3:
        return 'はい'
    elif answer_number == 4:
        return 'なんとも。もういちどやってみて'
    elif answer_number == 5:
        return 'あとでもう一度きいてみて'
    elif answer_number == 6:
        return '集中してもう一度きいてみて'
    elif answer_number == 7:
        return '私の答えはノーです'
    elif answer_number == 8:
        return '見通しはそれほどよくない'
    elif answer_number == 9:
        return 'とても疑わしい'

r = random.randint(1, 9)  # 4
fortune = get_answer(r)  # 5
print(fortune)  # 6

# print(get_answer(random.randint(1. 9)))