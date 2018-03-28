def read_field(file_name):

    f = open(file_name, 'r', encoding='utf-8', errors='ignore')
    data = dict()
    row = 1
    for i in f:
        n = 1
        i = i.strip('\n')
        for symb in i:
            data[(row, n)] = symb
            n += 1
        row += 1
    return data


def has_ship(field, coordinates):

    if field[coordinates] == '*':
        return True
    return False


def ship_size(field, coordinates):
    ship_len = 0

    koor1 = coordinates[0]
    koor2 = coordinates[1]

    if field[coordinates] != " ":
        ship_len = 1
        i = 1
        while koor2 + i <= 10 and field[(koor1, koor2 + i)] != " ":
            ship_len += 1
            i += 1
        i = 1
        while koor2 - i > 0 and field[(koor1, koor2 - i)] != " ":
            ship_len += 1
            i += 1
        i = 1
        while koor1 + i <= 10 and field[(koor1 + i, koor2)] != " ":
            ship_len += 1
            i += 1
        i = 1
        while koor1 - i > 0 and field[(koor1 - i, koor2)] != " ":
            ship_len += 1
            i += 1

    return ship_len


def is_valid(field):
    one = 0
    two = 0
    three = 0
    four = 0
    for i in range(1, 11):
        for j in range(1, 11):
            if ship_size(field, (i, j)) == 1:
                one += 1
            if ship_size(field, (i, j)) == 2:
                two += 1
            if ship_size(field, (i, j)) == 3:
                three += 1
            if ship_size(field, (i, j)) == 4:
                four += 1
            if ship_size(field, (i, j)) > 4:
                return False
    if one == 4 and two == 6 and three == 6 and four == 4:
        return True
    print(one, two, three, four)

    return False


field = read_field("field")
print(has_ship(field, (4, 10)))
print(read_field("field"))

print(ship_size(field, (1, 1)))

print(is_valid(field))