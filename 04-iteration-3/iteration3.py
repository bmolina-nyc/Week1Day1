
import math 

def med_avg_most(your_list):
    sorted_list = sorted(your_list)
    list_length = len(your_list)
    median = " "
    
    if list_length % 2 != 0:
        median = math.ceil(sorted_list/list_length)
    else:
        median = (sorted_list[list_length // 2] + sorted_list[(list_length //2) -1])//2

    most_frequent =  max(set(your_list), key=your_list.count)
    average = int(sum(your_list)/len(your_list))
    
    
    print(median)
    print(average)
    print(most_frequent)

print(med_avg_most([2, 34, 12, 29, 38, 1, 12, 8, 8, 9, 29, 38, 8, 9, 2, 3, 7, 10, 12, 8, 34, 7]
))