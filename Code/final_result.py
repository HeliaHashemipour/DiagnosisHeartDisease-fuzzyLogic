import fuzzification
import defuzzification as df
import inference as inf


class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:
        return df.defuzzification(inf.inference(float(input_dict['chest_pain']),
                                                float(input_dict['blood_pressure']),
                                                float(input_dict['cholestrol']),
                                                float(input_dict['blood_sugar']),
                                                float(input_dict['ecg']),
                                                float(input_dict['heart_rate']),
                                                float(input_dict['exercise']),
                                                float(input_dict['old_peak']),
                                                float(input_dict['thallium_scan']),
                                                float(input_dict['sex']),
                                                float(input_dict['age'])))
