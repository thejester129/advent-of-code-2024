from functools import reduce

rules = []
updates = []

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
    for line in lines:
        if line == "":
            continue
        if line.__contains__("|"):
            rule = line.split("|")
            rules.append(list(map(int, rule)))
        else:
            update = line.split(",")
            updates.append(list(map(int, update)))

def is_valid_update(update):
    val_pos = 0
    for val in update:
        rules_for_val = [rule for rule in rules if val in rule]
        for rule in rules_for_val:
            val_index = rule.index(val)
            comp_value = None
            if val_index == 0:
                # val < comp_value
                comp_value = rule[1]
                if comp_value in update:
                    if update.index(comp_value) < val_pos:
                        return False
            elif val_index == 1:
                # val > comp_value
                comp_value = rule[0]
                if comp_value in update:
                    if update.index(comp_value) > val_pos:
                        return False
        val_pos += 1
    return True

valid_updates = [update for update in updates if is_valid_update(update)]

def middle_of_list(x):
    return x[int((len(x) - 1) / 2)]

numbers = list(map(middle_of_list, valid_updates))

total = reduce(lambda x,y: x+y, numbers)    

print("part 1: " + str(total))

def order_update(update:list[str]) -> list[str]:
    val_pos = 0
    for val in update:
        rules_for_val = [rule for rule in rules if val in rule]
        for rule in rules_for_val:
            val_index = rule.index(val)
            comp_val = None
            if val_index == 0:
                # val < comp_val
                comp_val = rule[1]
                if comp_val in update:
                    if update.index(comp_val) < val_pos:
                        update.remove(comp_val)
                        update.insert(val_pos, comp_val)
                        return order_update(update)
            elif val_index == 1:
                # comp_val < val
                comp_val = rule[0]
                if comp_val in update:
                    if update.index(comp_val) > val_pos:
                        update.remove(comp_val)
                        update.insert(val_pos, comp_val)
                        return order_update(update)

        val_pos += 1
    return update

invalid_updates = [update for update in updates if not is_valid_update(update)]

fixed_updates = list(map(order_update, invalid_updates))

numbers = list(map(middle_of_list, fixed_updates))

total = reduce(lambda x,y: x+y, numbers)    

print("part 2: " + str(total))

