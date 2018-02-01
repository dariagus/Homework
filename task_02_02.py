def bubble_sort(lst)
    n = len(lst) # нахожу кол-во элементов в списке для определения границ
    x = n - 1 
    while x > 0;
        for i in range(x):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        m -= 1
    return list(lst)

