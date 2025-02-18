def cut_cake(number_of_friends, number_of_slices):
    # Cut cake in half
    number_of_slices = number_of_slices * 2
    # Check if there are enough slices for everybody

    if (number_of_slices >= number_of_friends):
        return number_of_slices

    else:
        return cut_cake(number_of_friends, number_of_slices)


print(cut_cake(5, 1))
