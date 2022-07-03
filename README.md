# Diagnosis Heart Disease

In this project, our goal is to design a fuzzy expert system to detect whether a person has heart disease.
# Run
```$ app.py```

![Uploading Screen Shot 1401-04-12 at 10.43.44.png…]()

# Fuzzification
To solve the problem with the help of fuzzy logic, it is necessary to convert our values from absolute to fuzzy (imprecise, relative). This is called fuzzification. For this purpose, fuzzy sets should be defined and according to the Fuzzification function, the degree of belonging of each value to the set should be calculated. For this purpose, the membership functions of the required sets are shown in the following figures: (For inputs such as sports activity, gender, and thallium, as explained above, since they only have crisp values, the graph is not given, but they must be included in the project.)

# Inference
In the next step, it is necessary to check the obtained fuzzy values in the existing rules to solve the problem.

# defuzzification
At this stage, we return to the world of absolute values with the help of repeated deductions to obtain the answer in the form of an absolute value. There are various methods for dephasing, one of the most important and widely used of which is the center of mass method.
