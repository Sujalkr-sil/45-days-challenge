class UnitConverter:
    def meters_to_feet(self, meters):
        return meters * 3.28084

    def feet_to_meters(self, feet):
        return feet / 3.28084

    def centimeters_to_inches(self, cm):
        return cm * 0.393701

    def inches_to_centimeters(self, inches):
        return inches / 0.393701
    
    def kilograms_to_grams(self, kilograms):
        return kilograms * 1000

    def grams_to_kilograms(self, grams):
        return grams / 1000

converter = UnitConverter()
meters = 5
feet = converter.meters_to_feet(meters)
print(f"{meters} meters = {feet:.2f} feet")

kilograms = 5
grams = converter.kilograms_to_grams(kilograms)
print(f"{kilograms} kilograms = {grams} grams")

grams = 2000
kilograms = converter.grams_to_kilograms(grams)
print(f"{grams} grams = {kilograms:.2f} kilograms")