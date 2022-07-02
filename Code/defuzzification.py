def integral1(x, a, b):  # x is the value of the health variable
    return x * (a * x + b)  # a and b are the constants of the function


def integral2(x, a, b):  # x is the value of the health variable
    return a * x + b  # a and b are the constants of the function


def health_defuzzy(point):  # point is the value of the health variable
    dx = 0.0001
    a, b = - 1 / 0.75, 1 / 0.75
    numerator1, denominator1, numerator2, denominator2 = 0.0, 0.0, 0.0, 0.0

    if point != 1:
        x = 0
        while x < (point - b) / a:
            numerator1 = numerator1 + integral1(x, 0, point) * dx
            denominator1 = denominator1 + integral2(x, 0, point) * dx
            x = x + dx
            
        y = (point - b) / a
        while y < 1:
            numerator2 = numerator2 + integral1(y, a, b) * dx
            denominator2 = denominator2 + integral2(y, a, b) * dx
            y = y + dx
        # numerator and denominator of the second integral process
        # numerator and denominator of the whole integral process
        res = (numerator1 + numerator2), (denominator1 + denominator2)
    else:
        x = 0
        while x < 0.25:
            numerator1 = numerator1 + integral1(x, 0, 1) * dx
            denominator1 = denominator1 + integral2(x, 0, 1) * dx
            x = x + dx

        y = 0.25
        while y < 1:
            numerator2 = numerator2 + integral1(y, a, b) * dx
            denominator2 = denominator2 + integral2(y, a, b) * dx
            y = y + dx
        # numerator and denominator of the whole integral process
        res = (numerator1 + numerator2), (denominator1 + denominator2)

    return res  # return the numerator and denominator of the whole integral process


def sick1_defuzzy(point):  # point is the value of the health variable
    dx = 0.0001
    a_1, a_2, b_1, b_2 = 1, -1, 0, 2
    numerator1, denominator1, numerator2, denominator2, numerator3, denominator3 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

    if point != 1:
        x = 0
        while x < (point - b_1) / a_1:
            numerator1 = numerator1 + integral1(x, a_1, b_1) * dx
            denominator1 = denominator1 + integral2(x, a_1, b_1) * dx
            x = x + dx

        y = (point - b_2) / a_2
        while y < 2:
            numerator2 = numerator2 + integral1(y, a_2, b_2) * dx
            denominator2 = denominator2 + integral2(y, a_2, b_2) * dx
            y = y + dx

        z = (point - b_1) / a_1
        while z < (point - b_2) / a_2:
            numerator3 = numerator3 + integral1(y, 0, point) * dx
            denominator3 = denominator3 + integral2(y, 0, point) * dx
            z = z + dx
        res = (numerator1 + numerator2 + numerator3), (denominator1 + denominator2 + denominator3)
    else:
        x = 0
        while x < 1:
            numerator1 = numerator1 + integral1(x, a_1, b_1) * dx
            denominator1 = denominator1 + integral2(x, a_1, b_1) * dx
            x = x + dx

        y = 1
        while y < 2:
            numerator2 = numerator2 + integral1(y, a_2, b_2) * dx
            denominator2 = denominator2 + integral2(y, a_2, b_2) * dx
            y = y + dx
        # numerator and denominator of the whole integral process
        res = (numerator1 + numerator2), (denominator1 + denominator2)
    return res


def sick2_defuzzy(point):
    dx = 0.0001
    # calculate the point a and b from point equation
    a_1, a_2, b_1, b_2 = 1, -1, -1, 3
    numerator1, denominator1, numerator2, denominator2, numerator3, denominator3 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    if point != 1:
        x = 1
        while x < (point - b_1) / a_1:
            numerator1 = numerator1 + integral1(x, a_1, b_1) * dx
            denominator1 = denominator1 + integral2(x, a_1, b_1) * dx
            x = x + dx

        y = (point - b_2) / a_2
        while y < 3:
            numerator2 = numerator2 + integral1(y, a_2, b_2) * dx
            denominator2 = denominator2 + integral2(y, a_2, b_2) * dx
            y = y + dx

        z = (point - b_1) / a_2
        while z < (point - b_2) / a_2:
            numerator3 = numerator3 + integral1(y, 0, point) * dx
            denominator3 = denominator3 + integral2(y, 0, point) * dx
            z = z + dx
        res = (numerator1 + numerator2 + numerator3), (denominator1 + denominator2 + denominator3)
    else:
        x = 0
        while x < 1:
            numerator1 = numerator1 + integral1(x, a_1, b_1) * dx
            denominator1 = denominator1 + integral2(x, a_1, b_1) * dx
            x = x + dx

        y = 1
        while y < 2:
            numerator2 = numerator2 + integral1(y, a_2, b_2) * dx
            denominator2 = denominator2 + integral2(y, a_2, b_2) * dx
            y = y + dx
        # numerator and denominator of the whole integral process
        res = (numerator1 + numerator2), (denominator1 + denominator2)
    return res


def sick3_defuzzy(point):
    dx = 0.0001
    a_1, a_2, b_1, b_2 = 1, -1, -2, 4
    numerator1, denominator1, numerator2, denominator2, numerator3, denominator3 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    if point != 1:
        x = 2
        while x < (point - b_1) / a_1:
            numerator1 = numerator1 + integral1(x, a_1, b_1) * dx
            denominator1 = denominator1 + integral2(x, a_1, b_1) * dx
            x = x + dx

        y = (point - b_2) / a_2
        while y < 4:
            numerator2 = numerator2 + integral1(y, a_2, b_2) * dx
            denominator2 = denominator2 + integral2(y, a_2, b_2) * dx
            y = y + dx

        z = (point - b_1) / a_1
        while z < (point - b_2) / a_2:
            numerator3 = numerator3 + integral1(y, 0, point) * dx
            denominator3 = denominator3 + integral2(y, 0, point) * dx
            z = z + dx
        res = (numerator1 + numerator2 + numerator3), (denominator1 + denominator2 + denominator3)
    else:
        x = 0
        while x < 1:
            numerator1 = numerator1 + integral1(x, a_1, b_1) * dx
            denominator1 = denominator1 + integral2(x, a_1, b_1) * dx
            x = x + dx

        y = 1
        while y < 2:
            numerator2 = numerator2 + integral1(y, a_2, b_2) * dx
            denominator2 = denominator2 + integral2(y, a_2, b_2) * dx
            y = y + dx
        # numerator and denominator of the whole integral process
        res = (numerator1 + numerator2), (denominator1 + denominator2)
    return res


def sick4_defuzzy(point):  # point is the value of the health variable
    a, b = 1 / 0.75, -4
    dx = 0.0001
    numerator1, denominator1, numerator2, denominator2 = 0.0, 0.0, 0.0, 0.0
    if point != 1:
        x = (point - b) / a
        while x < 4:
            numerator1 = numerator1 + integral1(x, 0, point) * dx
            denominator1 = denominator1 + integral2(x, 0, point) * dx
            x = x + dx

        y = 3
        while y < (point - b) / a:
            numerator2 = numerator2 + integral1(y, a, b) * dx
            denominator2 = denominator2 + integral2(y, a, b) * dx
            y = y + dx
        # numerator and denominator of the second integral process
        # numerator and denominator of the whole integral process
        res = (numerator1 + numerator2), (denominator1 + denominator2)
    else:
        x = 3.75
        while x < 4:
            numerator1 = numerator1 + integral1(x, 0, 1) * dx
            denominator1 = denominator1 + integral2(x, 0, 1) * dx
            x = x + dx

        y = 3
        while y < 3.75:
            numerator2 = numerator2 + integral1(y, a, b) * dx
            denominator2 = denominator2 + integral2(y, a, b) * dx
            y = y + dx

        res = (numerator1 + numerator2), (denominator1 + denominator2)
    return res  # return the numerator and denominator of the whole integral process


def defuzzification(output_dict):
    total_res = ''  # total_res is the result of the defuzzification process
    res = []  # res is the list of the output values of the defuzzyfication process
    numerator = 0  # numerator of the whole integral process
    denominator = 0  # denominator of the whole integral process

    if output_dict['outputsick_healthy'] > 0:  # if the output of the fuzzy system is 1, the output is healthy
        # healthy is the numerator and denominator of the health defuzzyfication process
        healthy = health_defuzzy(output_dict['outputsick_healthy'])
        # numerator is the list of the numerator of the integral process and
        # add the numerator of the health defuzzyfication process
        numerator = numerator + healthy[0]
        # add the numerator and denominator of the health defuzzyfication process to
        # the numerator and denominator of the whole integral process
        denominator = denominator + healthy[1]
    if output_dict['outputsick_sick1'] > 0:
        sick_1 = sick1_defuzzy(output_dict['outputsick_sick1'])
        numerator = numerator + sick_1[0]
        denominator = denominator + sick_1[1]
    if output_dict['outputsick_sick2'] > 0:
        sick_2 = sick2_defuzzy(output_dict['outputsick_sick2'])
        numerator = numerator + sick_2[0]
        denominator = denominator + sick_2[1]
    if output_dict['outputsick_sick3'] > 0:
        sick_3 = sick3_defuzzy(output_dict['outputsick_sick3'])
        numerator = numerator + sick_3[0]
        denominator = denominator + sick_3[1]
    if output_dict['outputsick_sick4'] > 0:
        sick_4 = sick4_defuzzy(output_dict['outputsick_sick4'])
        numerator = numerator + sick_4[0]
        denominator = denominator + sick_4[1]

    try:  # try to calculate the center of gravity of the output variable (center of gravity)
        centerOfGravity = (numerator / denominator)  # center of gravity = sum_numerator / sum_denominator
    except ZeroDivisionError:  # if the denominator is 0, the center of gravity is 0 (the output variable is 0)
        centerOfGravity = 0.0  # center of gravity = 0.0

    # if the center of gravity is less than 1.78, the output variable is 0 (the output variable is 0)
    if centerOfGravity < 1.78:
        res.append('healthy')  # add the output variable to the list of the output values of the defuzzyfication process
    if 1 <= centerOfGravity < 2.51:
        # if the list of the output values of the defuzzyfication process is not empty,
        # the output variable is 0 (the output variable is 0)
        if len(res) != 0:
            res.append(' & ')
            res.append('sick1')
        else:
            res.append('sick1')
    if 1.78 <= centerOfGravity < 3.25:
        if len(res) != 0:
            res.append(' & ')
            res.append('sick2')
        else:
            res.append('sick1')
    if 1.5 <= centerOfGravity < 4.5:
        if len(res) != 0:
            res.append(' & ')
            res.append('sick3')
        else:
            res.append('sick3')
    if 3.25 <= centerOfGravity:
        if len(res) != 0:
            res.append(' & ')
            res.append('sick4')
        else:
            res.append('sick4')

    res.append(' : ')  # add the string ' : ' to the list of the output values of the defuzzyfication process
    # add the center of gravity to the list of the output values of the defuzzyfication process
    # (round the center of gravity to 4 decimal places)
    res.append(str(round(centerOfGravity, 3)))

    for string in res:  # for each element in the list of the output values of the defuzzyfication process
        # add the element to the list of the numerator and denominator of the whole integral process
        total_res = total_res + string

    return total_res  # return the list of the numerator and denominator of the whole integral process
