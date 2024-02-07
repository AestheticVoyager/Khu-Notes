# Mahan Fallah - 4023131508
def get_prob(input_data, array):
    n_class1 = 0
    n_class2 = 0
    for i in range(len(input_data)):
        for j in range(len(input_data[i])):
            if input_data[i][j] == "'recurrence-events'":
                n_class1 += 1
            if input_data[i][j] == "'no-recurrence-events'":
                n_class2 += 1

    for col_dict in array:
        for key, value in col_dict.items():
            value[0] = round(value[0] / n_class1, 2)
            value[1] = round(value[1] / n_class2, 2)

    prob_class1 = n_class1 / (n_class1 + n_class2)
    prob_class2 = n_class2 / (n_class1 + n_class2)

    return array, prob_class1, prob_class2

def set_array(input_data):
    array = []
    col = len(input_data[0])
    for i in range(col):
        col_dict = {}
        for j in range(len(input_data)):
            if input_data[j][i] not in col_dict:
                col_dict[input_data[j][i]] = [0, 0]
            if input_data[j][i] in col_dict:
                if input_data[j][-1] == "'recurrence-events'":
                    col_dict[input_data[j][i]][0] += 1
                else:
                    col_dict[input_data[j][i]][1] += 1

        array.append(col_dict)
    array.pop()
    return array

def test(data, array, p_class1, p_class2):
    true = 0
    for i in range(len(data)):
        col_dict = {}
        factor = 1
        factor_2 = 1
        for j in range(len(data[i]) - 1):
            for col_dict in array:
                if data[i][j] in col_dict:
                    col_dict[data[i][j]] = col_dict[data[i][j]]

        for key, value in col_dict.items():
            factor *= value[0]
        factor *= p_class1

        for key, value in col_dict.items():
            factor_2 *= value[1]
        factor_2 *= p_class2

        if factor > factor_2:
            main_class = "'recurrence-events'"
        else:
            main_class = "'no-recurrence-events'"

        if main_class == data[i][-1]:
            true += 1

    return true / len(data) * 100

with open("Breast_Cancer_dataset_2.txt", "r") as file:
    lines = file.readlines()
    l = [0 for i in range(len(lines))]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            l[i] = lines[i].strip().split(",")

input_data = l[0:167]
input_test = l[167:]
a_new = set_array(input_data)
print(a_new)
f_arr, prob1, prob2 = get_prob(input_data, a_new)
print(f_arr)
print(prob1)
print(prob2)
print(test(input_test, f_arr, prob1, prob2))

