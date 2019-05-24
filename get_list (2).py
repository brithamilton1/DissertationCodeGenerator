def get_list(elements, length_of_list):
    if(length_of_list == 1): 
        return elements
    else:
        all_list = [None] * len(elements) ** length_of_list

        sub_list = get_list(elements, length_of_list - 1)

        array_index = 0

        for element in elements:
            for sub_element in sub_list:
                all_list[array_index] = element + sub_element
                array_index += 1
        return all_list

options = ["U","D","R","L"];
print(len(get_list(options, 6)))