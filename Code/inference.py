import fuzzification as f


def dict(output_healthy, output_sick1, output_sick2, output_sick3, output_sick4):
    return {
        'outputsick_healthy': max(output_healthy),
        'outputsick_sick1': max(output_sick1),
        'outputsick_sick2': max(output_sick2),
        'outputsick_sick3': max(output_sick3),
        'outputsick_sick4': max(output_sick4)
    }


def inference(chest_pain, blood_pressure, cholesterol, blood_sugar, ECG, maximum_heart_rate, exercise, old_peak,
              thallium,
              sex, age):
    output_sick1, output_sick2, output_sick3, output_sick4, output_healthy = [], [], [], [], []
    # RULE 1: IF (age IS very_old) AND (chest_pain IS atypical_anginal) THEN health IS output_sick4;
    output_sick4.append(min(f.compute_fuzzy_age(age)['very_old'],
                            f.compute_fuzzy_chest_pain(chest_pain)['atypical_anginal']))
    # RULE 2: IF (maximum_heart_rate IS high) AND (age IS old) THEN health IS sick_4;
    output_sick4.append(min(f.compute_fuzzy_heartRate(maximum_heart_rate)['high'],
                            f.compute_fuzzy_age(age)['old']))
    # RULE 3: IF (sex IS male) AND (maximum_heart_rate IS medium) THEN health IS sick_3;
    output_sick3.append(min(f.compute_fuzzy_sex(sex)['male'],
                            f.compute_fuzzy_heartRate(maximum_heart_rate)['medium']))
    # RULE 4: IF (sex IS female) AND (maximum_heart_rate IS medium) THEN health IS sick_2;
    output_sick2.append(min(f.compute_fuzzy_sex(sex)['female'],
                            f.compute_fuzzy_heartRate(maximum_heart_rate)['medium']))
    # RULE 5: IF (chest_pain IS non_aginal_pain) AND (blood_pressure IS high) THEN health IS sick_3;
    output_sick3.append(min(f.compute_fuzzy_chest_pain(chest_pain)['non_aginal_pain'],
                            f.compute_fuzzy_bloodPressure(blood_pressure)['high']))
    # RULE 6: IF (chest_pain IS typical_anginal) AND (maximum_heart_rate IS medium) THEN health IS sick_2;
    output_sick2.append(min(f.compute_fuzzy_chest_pain(chest_pain)['typical_anginal'],
                            f.compute_fuzzy_heartRate(maximum_heart_rate)['medium']))
    # RULE 7: IF (blood_sugar IS true) AND (age IS mild) THEN health IS sick_3;
    output_sick3.append(min(f.compute_fuzzy_bloodSugar(blood_sugar)['true'],
                            f.compute_fuzzy_age(age)['mild']))
    # RULE 8: IF (blood_sugar IS false) AND (blood_pressure IS very_high) THEN health IS sick_2;
    output_sick2.append(min(f.compute_fuzzy_bloodSugar(blood_sugar)['false'],
                            f.compute_fuzzy_bloodPressure(blood_pressure)['very_high']))
    # RULE 9: IF (chest_pain IS asymptomatic) OR (age IS very_old) THEN health IS sick_1;
    output_sick1.append(max(f.compute_fuzzy_chest_pain(chest_pain)['asymptomatic'],
                            f.compute_fuzzy_age(age)['very_old']))
    # RULE 10: IF (blood_pressure IS high) OR (maximum_heart_rate IS low) THEN health IS sick_1;
    output_sick1.append(max(f.compute_fuzzy_bloodPressure(blood_pressure)['high'],
                            f.compute_fuzzy_heartRate(maximum_heart_rate)['low']))
    # RULE 11: IF (chest_pain IS typical_anginal) THEN health IS healthy;
    output_healthy.append(f.compute_fuzzy_chest_pain(chest_pain)['typical_anginal'])
    # RULE 12: IF (chest_pain IS atypical_anginal) THEN health IS sick_1;
    output_sick1.append(f.compute_fuzzy_chest_pain(chest_pain)['atypical_anginal'])
    # RULE 13: IF (chest_pain IS non_aginal_pain) THEN health IS sick_2;
    output_sick2.append(f.compute_fuzzy_chest_pain(chest_pain)['non_aginal_pain'])
    # RULE 14: IF (chest_pain IS asymptomatic) THEN health IS sick_3;
    output_sick3.append(f.compute_fuzzy_chest_pain(chest_pain)['asymptomatic'])
    # RULE 15: IF (chest_pain IS asymptomatic) THEN health IS sick_4;
    output_sick4.append(f.compute_fuzzy_chest_pain(chest_pain)['asymptomatic'])
    # RULE 16: IF (sex IS female) THEN health IS sick_1;
    output_sick1.append(f.compute_fuzzy_sex(sex)['female'])
    # RULE 17: IF (sex IS male) THEN health IS sick_2;
    output_sick2.append(f.compute_fuzzy_sex(sex)['male'])
    # RULE 18: IF (blood_pressure IS low) THEN health IS healthy;
    output_healthy.append(f.compute_fuzzy_bloodPressure(blood_pressure)['low'])
    # RULE 19: IF (blood_pressure IS medium) THEN health IS sick_1;
    output_sick1.append(f.compute_fuzzy_bloodPressure(blood_pressure)['medium'])
    # RULE 20: IF (blood_pressure IS high) THEN health IS sick_2;
    output_sick2.append(f.compute_fuzzy_bloodPressure(blood_pressure)['high'])
    # RULE 21: IF (blood_pressure IS high) THEN health IS sick_3;
    output_sick3.append(f.compute_fuzzy_bloodPressure(blood_pressure)['high'])
    # RULE 22: IF (blood_pressure IS very_high) THEN health IS sick_4;
    output_sick4.append(f.compute_fuzzy_bloodPressure(blood_pressure)['very_high'])
    # RULE 23: IF (cholesterol IS low) THEN health IS	healthy;
    output_healthy.append(f.compute_fuzzy_cholesterol(cholesterol)['low'])
    # RULE 24: IF (cholesterol IS medium) THEN health IS sick_1;
    output_sick1.append(f.compute_fuzzy_cholesterol(cholesterol)['medium'])
    # RULE 25: IF (cholesterol IS high) THEN health IS sick_2;
    output_sick2.append(f.compute_fuzzy_cholesterol(cholesterol)['high'])
    # RULE 26: IF (cholesterol IS high) THEN health IS sick_3;
    output_sick3.append(f.compute_fuzzy_cholesterol(cholesterol)['high'])
    # RULE 27: IF (cholesterol IS very_high) THEN health IS sick_4;
    output_sick4.append(f.compute_fuzzy_cholesterol(cholesterol)['very_high'])
    # RULE 28: IF (blood_sugar IS true) THEN health IS sick_2;
    output_sick2.append(f.compute_fuzzy_bloodSugar(blood_sugar)['true'])
    # RULE 29: IF (ECG IS normal) THEN health IS healthy;
    output_healthy.append(f.compute_fuzzy_ECG(ECG)['normal'])
    # RULE 30: IF (ECG IS normal) THEN health IS sick_1;
    output_sick1.append(f.compute_fuzzy_ECG(ECG)['normal'])
    # RULE 31: IF (ECG IS abnormal) THEN health IS sick_2;
    output_sick2.append(f.compute_fuzzy_ECG(ECG)['abnormal'])
    # RULE 32: IF (ECG IS hypertrophy) THEN health IS sick_3;
    output_sick3.append(f.compute_fuzzy_ECG(ECG)['hypertrophy'])
    # RULE 33: IF (ECG IS hypertrophy) THEN health IS sick_4;
    output_sick4.append(f.compute_fuzzy_ECG(ECG)['hypertrophy'])
    # RULE 34: IF (maximum_heart_rate IS low) THEN health IS healthy;
    output_healthy.append(f.compute_fuzzy_heartRate(maximum_heart_rate)['low'])
    # RULE 35: IF (maximum_heart_rate IS medium) THEN health IS sick_1;
    output_sick1.append(f.compute_fuzzy_heartRate(maximum_heart_rate)['medium'])
    # RULE 36: IF (maximum_heart_rate IS medium) THEN health IS sick_2;
    output_sick2.append(f.compute_fuzzy_heartRate(maximum_heart_rate)['medium'])
    # RULE 37: IF(maximum_heart_rate IS high) THEN health IS sick_3;
    output_sick3.append(f.compute_fuzzy_heartRate(maximum_heart_rate)['high'])
    # RULE 38: IF(maximum_heart_rate IS high) THEN health IS sick_4;
    output_sick4.append(f.compute_fuzzy_heartRate(maximum_heart_rate)['high'])
    # RULE 39: IF (exercise IS true) THEN health IS sick_2;
    output_sick2.append(f.compute_fuzzy_exercise(exercise)['true'])
    # RULE 40: IF (old_peak IS low) THEN health IS healthy;
    output_healthy.append(f.compute_fuzzy_oldPeak(old_peak)['low'])
    # RULE 41: IF (old_peak IS low) THEN health IS sick_1;
    output_sick1.append(f.compute_fuzzy_oldPeak(old_peak)['low'])
    # RULE 42: IF (old_peak IS terrible) THEN health IS sick_2;
    output_sick2.append(f.compute_fuzzy_oldPeak(old_peak)['terrible'])
    # RULE 43: IF (old_peak IS terrible) THEN health IS sick_3;
    output_sick3.append(f.compute_fuzzy_oldPeak(old_peak)['terrible'])
    # RULE 44: IF (old_peak IS risk) THEN health IS sick_4;
    output_sick4.append(f.compute_fuzzy_oldPeak(old_peak)['risk'])
    # RULE 45: IF (thallium IS normal) THEN health IS healthy;
    output_healthy.append(f.compute_fuzzy_thallium(thallium)['normal'])
    # RULE 46: IF (thallium IS normal) THEN health IS sick_1;
    output_sick1.append(f.compute_fuzzy_thallium(thallium)['normal'])
    # RULE 47: IF (thallium IS medium) THEN health IS sick_2;
    output_sick2.append(f.compute_fuzzy_thallium(thallium)['medium'])
    # RULE 48: IF (thallium IS high) THEN health IS sick_3;
    output_sick3.append(f.compute_fuzzy_thallium(thallium)['high'])
    # RULE 49: IF (thallium IS high) THEN health IS sick_4;
    output_sick4.append(f.compute_fuzzy_thallium(thallium)['high'])
    # RULE 50: IF (age IS young) THEN health IS healthy;
    output_healthy.append(f.compute_fuzzy_age(age)['young'])
    # RULE 51: IF (age IS mild) THEN health IS sick_1;
    output_sick1.append(f.compute_fuzzy_age(age)['mild'])
    # RULE 52: IF (age IS old) THEN health IS sick_2;
    output_sick2.append(f.compute_fuzzy_age(age)['old'])
    # RULE 53: IF (age IS old) THEN health IS sick_3;
    output_sick3.append(f.compute_fuzzy_age(age)['old'])
    # RULE 54: IF (age IS very_old) THEN health IS sick_4;
    output_sick4.append(f.compute_fuzzy_age(age)['very_old'])

    return dict(output_healthy, output_sick1, output_sick2,
                output_sick3, output_sick4)  # return the max of the output_sick1, output_sick2, output_sick3,
                                             # output_sick4
