def persistence(n, n_steps=0, print_steps=False):
    if print_steps:
        print(n_steps, n)
    if n < 10:
        return n_steps
    else:
        new_n = 1
        while n > 0:
            new_n *= n % 10
            n //= 10
        return persistence(new_n, n_steps+1, print_steps)
        
def check_persistence_in_range (start, end, print_steps=False, print_all_persistence=False, print_new_persistence=False):
    i = start
    largest_persistence = 0
    smallest_n_with_largest_persistence = 0
    while (i <= end):
        p = persistence(i, print_steps=print_steps)
        if p > largest_persistence:
            largest_persistence = p
            smallest_n_with_largest_persistence = i
            if print_new_persistence:
                print(i, p)
        if print_all_persistence:
            print(i, p)
        i = i+1
    return (smallest_n_with_largest_persistence, largest_persistence)
