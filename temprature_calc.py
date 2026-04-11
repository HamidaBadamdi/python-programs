'''
5. Create a Temperature class. Create 2 methods named convertFarenheit() 
and convertCelsius(). 
'''

class Temperature:
    
    # Convert Celsius to Fahrenheit
    def convertFahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        print("\nTemperature in Fahrenheit:", fahrenheit)
    
    # Convert Fahrenheit to Celsius
    def convertCelsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        print("\nTemperature in Celsius:", celsius)

t = Temperature()

# Call methods
t.convertFahrenheit(25)   # Celsius to Fahrenheit
t.convertCelsius(77)      # Fahrenheit to Celsius
