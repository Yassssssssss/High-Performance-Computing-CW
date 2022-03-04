import matplotlib.pyplot as plt

datContent = [i.strip().split() for i in open("./final.dat").readlines()]


def filter_zeros(file):
    list =[]
    for x in file:
        if x[2] == "0":
            continue
        else:
            list.append(x)
    return list


def group(list):
    grouped_list = {}
    for line in list:
        if float(line[0]) in grouped_list:
            grouped_list[float(line[0])].append(float(line[2]))
        else:
            grouped_list[float(line[0])] = [float(line[2])]
    return grouped_list
    

def average(lst):
    return sum(lst) / len(lst)


def calc_Average(list):
    averaged_list = {}
    for line in list:
        averaged_list[line] = average(list[line])
    return averaged_list


def main():
    y = calc_Average(group(filter_zeros(datContent)))
    values = list(y.values())
    keys = list(y.keys())
    
    plt.plot(keys, values)
    plt.xlabel('X')
    plt.ylabel('u(x)(y)')
    plt.savefig('line_plot.png') 
    



main()
    

