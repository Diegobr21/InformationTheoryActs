def KMP(pattern, text):
    prefix_arr = get_prefix(pattern, len(pattern))
  
    initial_point = []
    partial_matches = []
    m = 0
    n = 0
  
    while m != len(text):
       
        if text[m] == pattern[n]:
            m += 1
            n += 1
      
        else:
            n = prefix_arr[n-1]
       
        if n == len(pattern):
            initial_point.append(m-n)
            n = prefix_arr[n-1]

        if(2 < n < len(pattern)):
            partial_matches.append(m-n)

        elif n == 0:
            m += 1
    real_partial_matches = [e for e in partial_matches if e not in initial_point]
    real_partial_matches = set(real_partial_matches)
    return initial_point, real_partial_matches


def get_prefix(pattern, length):
    prefix_arr = [0] * length
    n = 0
    m = 1
    while m != length:
        if pattern[m] == pattern[n]:
            n += 1
            prefix_arr[m] = n
            m += 1
        elif n != 0:
            n = prefix_arr[n-1]
        else:
            prefix_arr[m] = 0
            m += 1
    return prefix_arr


string = input('Enter the string or press enter if you want the default one: ')
if len(string) > 0:
    pat = input('Enter the pattern to search for in the string provided: ')
    print(f'\nString: {string}\nPattern: {pat}\n')
else:
    string = "ABABDABACDABABCABABCABAB"
    pat = "ABABCABAB"
    print(f'\nString: {string}\nPattern: {pat}\n')

result = KMP(pat, string)
indexes_ocurrence = result[0]
partial_matches = result[1]
if(len(indexes_ocurrence) > 0):
    for i in indexes_ocurrence:
        print('* Pattern is found in the string at index number: ',i)
else:
    print('* No complete match of the pattern was found')

print('\nPartial matches are considered as matching at least 3 characters\n')
if(len(partial_matches) > 0):
    for i in partial_matches:
        print('* Partial match of the pattern is found in the string at index number: ',i)
else:
    print('* No partial match of the pattern was found')
