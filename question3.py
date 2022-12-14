class Person:
    def __init__(self,heigth,weight):
        self.heigth = heigth # meters
        self.weight = weight # kilograms

    def BMI(self):
        BMI = self.weight/(self.heigth**2)
        return round(BMI,2) # rounding two decimal

    def classif_obesity(self):
        # List with all classification
        classification = [[18.5, "Thinness", None], [24.9, "Normal", None], [29.9, "Overweight", None], [34.9, "Obesity","I"], [39.9, "Obesity", "II"], [40.0, "Obesity", "III"]]
        
        # raise error for negative values
        if self.heigth < 0 or self.weight < 0:
            raise ValueError("Heigth or Weight can't be negative!")

        # raise error for non-numeric values
        if type(self.heigth) not in [int,float]:
            raise TypeError("Heigth needs to be a number!")
        if type(self.weight) not in [int,float]:
            raise TypeError("Weight needs to be a number!")

        # iterate to find in each category BMI falls into
        for i in range(0,len(classification)): 
            if classification[i][0] < self.BMI() <  classification[i+1][0]:
                return classification[i+1][1:3]
            elif self.BMI() < classification[0][0]: # thinness exception case 
                return classification[0][1:3]
                break
            elif self.BMI() > classification[len(classification)-1][0]: # obesity III exception case
                return classification[len(classification)-1][1:3]
                break


# driver example code
user1 =  Person(1.70,65)
user1.BMI()
user1.classif_obesity()