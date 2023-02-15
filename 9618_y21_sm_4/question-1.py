the_data = [20, 3, 4, 8, 12, 99, 4, 26, 4]

def insertion_sort(the_data):
    for i in range(0, len(the_data)):
        data_to_insert = the_data[i]
        inserted = 0
        next_value = i - 1
        while next_value >= 0 and inserted != 1:
            if data_to_insert < the_data[next_value]:
                the_data[next_value + 1] = the_data[next_value]
                next_value = next_value - 1
                the_data[next_value + 1] = data_to_insert
            else:
                inserted = 1

def output_array(the_data):
    for i in range(0, len(the_data)):
        print(the_data[i], end=" ")

def main():
    print("Data before sorting:")
    output_array(the_data)
    insertion_sort(the_data)
    print("\nData after sorting:")
    output_array(the_data)

main()