# AGE
def age_young(x):
    if x <= 29:
        return 1
    elif 29 < x < 38:
        y = -(1 / 9) * x + (38 / 9)  # (y = ax + b)
        return y
    else:
        return 0


def age_mild(x):
    if x <= 33 or x >= 45:
        return 0
    elif 33 < x <= 38:
        y = (1 / 5) * x - (33 / 5)
        return y
    else:
        y = -(1 / 7) * x + (45 / 7)
        return y


def age_old(x):
    if x <= 40 or x >= 58:
        return 0
    elif 40 < x <= 48:
        y = (1 / 8) * x - (40 / 8)
        return y
    else:
        y = -(1 / 10) * x + (58 / 10)
        return y


def age_veryold(x):  # red plot
    if x <= 52:
        return 0
    if 52 < x < 60:
        y = (1 / 8) * x - (52 / 8)
        return y
    else:
        return 1


def compute_fuzzy_age(age):
    res = {'young': age_young(age),
           'mild': age_mild(age),
           'old': age_old(age),
           'very_old': age_veryold(age)}
    return res


# BLOOD PRESSURE
def bloodPressure_low(x):
    if 0 <= x < 111:
        return 1
    elif 111 <= x <= 134:
        y = -(1 / 23) * x + (134 / 23)
        return y
    else:
        return 0


def bloodPressure_medium(x):
    if x <= 127 or x >= 153:
        return 0
    elif 127 < x <= 139:
        y = (1 / 12) * x - (127 / 12)
        return y
    else:
        y = -(1 / 14) * x + (153 / 14)
        return y


def bloodPressure_high(x):
    if x <= 142 or x >= 172:
        return 0
    elif 142 < x <= 157:
        y = (1 / 15) * x - (142 / 15)
        return y
    else:
        y = -(1 / 15) * x + (172 / 15)
        return y


def bloodPressure_veryhigh(x):
    if 0 <= x <= 154:
        return 0
    if 154 < x < 171:
        y = (1 / 17) * x - (154 / 17)
        return y
    else:
        return 1


def compute_fuzzy_bloodPressure(bloodPressure):
    res = {'low': bloodPressure_low(bloodPressure),
           'medium': bloodPressure_medium(bloodPressure),
           'high': bloodPressure_high(bloodPressure),
           'very_high': bloodPressure_veryhigh(bloodPressure)}
    return res


# cholesterol
def low(x):
    if 0 <= x <= 151:
        return 1
    elif 151 < x < 197:
        y = -(1 / 46) * x + (197 / 46)
        return y
    else:
        return 0


def medium(x):
    if x <= 188 or x >= 250:
        return 0
    elif 188 < x <= 215:
        y = (1 / 27) * x - (188 / 27)
        return y
    else:
        return (-1 / 35) * x + (250 / 35)


def high(x):
    if 217 >= x >= 307:
        return 0
    elif 217 < x <= 263:
        y = (1 / 46) * x - (217 / 46)
        return y
    else:
        y = -(1 / 44) * x + (307 / 44)
        return y


def very_high(x):
    if 0 <= x < 281:
        return 0
    elif 281 <= x < 347:
        y = (1 / 66) * x - (281 / 66)
        return y
    else:
        return 1


def compute_fuzzy_cholesterol(x):
    res = {'low': low(x),
           'medium': medium(x),
           'high': high(x),
           'very_high': very_high(x)}
    return res


# heart_rate
def low(x):
    if 0 <= x <= 100:
        return 1
    elif 100 < x <= 141:
        y = -(1 / 41) * x + (141 / 41)
        return y
    else:
        return 0


def medium(x):
    if x <= 111 or x >= 194:
        return 0
    elif 111 < x <= 152:
        y = (1 / 41) * x - (111 / 41)
        return y
    else:
        y = (-1 / 42) * x + (194 / 42)
        return y


def high(x):
    if 0 < x <= 152:
        return 0
    elif 152 < x <= 210:
        y = (1 / 58) * x - (152 / 58)
        return y
    else:
        return 1


def compute_fuzzy_heartRate(heartRate):
    res = {'low': low(heartRate),
           'medium': medium(heartRate),
           'high': high(heartRate)}
    return res


# ECG
def ECG_normal(x):
    if -0.5 <= x <= 0:
        return 1
    elif 0 < x <= 0.4:
        y = -(1 / 0.4) * x + 1
        return y
    else:
        return 0


def ECG_abnormal(x):
    if x <= 0.2 or x >= 1.8:
        return 0
    elif 0.2 < x <= 1:
        y = 1.250 * x - (1 / 4)
        return y
    else:
        y = - (1 / 0.8) * x + (1 / 4)
        return y


def ECG_hypertrophy(x):
    if x <= 1.4:
        return 0
    if 1.4 < x <= 1.9:
        y = (1 / 0.5) * x - (1.4 / 0.5)
        return y
    else:
        return 1


def compute_fuzzy_ECG(ECG):
    res = {'normal': ECG_normal(ECG),
           'abnormal': ECG_abnormal(ECG),
           'hypertrophy': ECG_hypertrophy(ECG)}
    return res


# OLD PEAK
def oldPeak_low(x):
    if 0 <= x <= 1:
        return 1
    elif 1 < x < 2:
        y = -1 * x + 2
        return y
    else:
        return 0


def oldPeak_risk(x):
    if x <= 1.5 or x >= 4.2:
        return 0
    elif 1.5 < x <= 2.8:
        y = (1 / 1.3) * x - (1.5 / 1.3)
        return y
    else:
        y = (-1 / 1.4) * x + (4.2 / 1.4)
        return y


def oldPeak_terrible(x):
    if x <= 2.5:
        return 0
    elif 2.5 < x < 4:
        y = (1 / 1.5) * x - (2.5 / 1.5)
        return y
    else:
        return 1


def compute_fuzzy_oldPeak(oldPeak):
    res = {'low': oldPeak_low(oldPeak),
           'risk': oldPeak_risk(oldPeak),
           'terrible': oldPeak_terrible(oldPeak)}
    return res


# BLOOD SUGAR
def bloodSugar_veryhigh(x):
    if 105 <= x:
        return 0
    elif 105 < x <= 120:
        y = (1 / 15) * x - (105 / 15)
        return y
    else:
        return 1


def compute_fuzzy_bloodSugar(bloodSugar):
    res = {'true': bloodSugar_veryhigh(bloodSugar),
           'false': bloodSugar_veryhigh(bloodSugar)}
    return res


# OUTPUTTING
def outputsick_healthy(x):
    if 0 <= x <= 0.25:
        return 1
    elif 0.25 < x < 1:
        y = -1.333 * x + 1.333
        return y
    else:
        return 0


def outputsick_sick1(x):
    if x <= 0 or x >= 2:
        return 0
    elif 0 < x <= 1:
        y = x
        return y
    else:
        y = -1.000 * x + 2.000
        return y


def outputsick_sick2(x):
    if x <= 1 or x >= 3:
        return 0
    elif 1 < x <= 2:
        y = 1.000 * x - 1.000
        return y
    else:
        y = -1.000 * x + 3.000
        return y


def outputsick_sick3(x):
    if x <= 2 or x >= 4:
        return 0
    elif 2 < x <= 3:
        y = 1.000 * x - 2
        return y
    else:
        y = -1.000 * x + 4.000
        return y


def outputsick_sick4(x):
    if 0 <= x <= 3:
        return 0
    if 3 < x <= 3.75:
        y = (1 / 0.75) * x - 4.000
        return y
    else:
        return 1


def compute_outputsick(num):
    res = {
        'sick_1': outputsick_sick1(num),
        'sick_2': outputsick_sick2(num),
        'sick_3': outputsick_sick3(num),
        'sick_4': outputsick_sick4(num),
        'healthy': outputsick_healthy(num)
    }
    return res


# chest_pain
def typical_angina(x):
    if x == 1:
        return 1
    else:
        return 0


def atypical_angina(x):
    if x == 2:
        return 1
    else:
        return 0


def non_anginal_pain(x):
    if x == 3:
        return 1
    else:
        return 0


def asymptomatic(x):
    if x == 4:
        return 1
    else:
        return 0


def compute_fuzzy_chest_pain(num):
    res = {'typical_anginal': typical_angina(num),
           'atypical_anginal': atypical_angina(num),
           'non_aginal_pain': non_anginal_pain(num),
           'asymptomatic': asymptomatic(num)}
    return res


# emtiaziii
# exercise
def suitable(x):
    if x == 1:
        return 1

    else:
        return 0


def unsuitable(x):
    if x == 0:
        return 1

    else:
        return 0


def compute_fuzzy_exercise(num):
    res = {'true': suitable(num),
           'false': unsuitable(num)}
    return res


# emtiaziii
# thallium
def normal(x):
    if x == 3:
        return 1
    else:
        return 0


def medium(x):
    if x == 6:
        return 1
    else:
        return 0


def high(x):
    if x == 7:
        return 1
    else:
        return 0


def compute_fuzzy_thallium(num):
    res = {'normal': normal(num),
           'medium': medium(num),
           'high': high(num)}
    return res


# SEX
def male(x):
    if x == 0:
        return 1

    else:
        return 0


def female(x):
    if x == 1:
        return 1

    else:
        return 0


def compute_fuzzy_sex(num):
    res = {'male': male(num),
           'female': female(num)}
    return res
