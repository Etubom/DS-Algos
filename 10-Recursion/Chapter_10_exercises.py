def even_numbers_between_low_and_high(low,high):
    print(low)
    if low >= high:
        return
    else:
        even_numbers_between_low_and_high(low + 2,high)

# even_numbers_between_low_and_high(0,10)


def sum(low, high):
    if high == low:
        return low
    else:
        return sum(low, high - 1) + high

# print(sum(1, 10))

nested_array_of_numbers = [1,2,3,
 [4,5,6],
 7,
 [8,
  [9,10,11,
   [12,13,14]
   ]
  ],
 [15,16,17,18,19,
  [20,21,22,
   [23,24,25,
    [26,27,29]
    ],30,31
   ],32
  ],33
]

def print_all_items(array):
    for value in array:
        if isinstance(value,list):
            print_all_items(value)
        else:
            print(value)

print_all_items(nested_array_of_numbers)