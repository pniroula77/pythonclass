def int_to_roman(num):
    mapping_list = [
        (1000,'M'),
        (900,'CM'),
        (500,'D'),
        (400,'CD'),
        (100,'C'),
        (90,'XC'),
        (50,'L'),
        (40,'XL'),
        (10,'X'),
        (9,'IX'),
        (5,'V'),
        (4,'IV'),
        (1,'I'),

    ]

    roman_list = []

    for i, number in mapping_list:
        while num >= i:
            num -= i 
            roman_list.append(number)
    return "".join(roman_list)


a = int_to_roman(902)

print(a)