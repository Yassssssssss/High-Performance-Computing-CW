import pandas as pd
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
        if line[0] in grouped_list:
            # append the new number to the existing array at this slot
            grouped_list[float(line[0])].append(float(line[2]))
        else:
            # create a new array in this slot
            grouped_list[float(line[0])] = [float(line[2])]
    return grouped_list
    
def average(lst):
    return sum(lst) / len(lst)

def calc_Average(list):
    averaged_list = {}
    for line in list:
        averaged_list[line[0]] = average(line[1])
    return averaged_list



def main():
    x = calc_Average(group(filter_zeros(datContent)))
    print(x)

main()
    

