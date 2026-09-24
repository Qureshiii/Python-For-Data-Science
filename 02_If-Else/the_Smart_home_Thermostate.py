
# The smart home thermostate System.

temprature = int(input("What is the current temprature in celcius? "))
is_raining = input('is it raining outside? (yes/no): ').lower() == 'yes'


if temprature < 18 and is_raining:
    print('Action: turn on the heater and close the electric window. ')
    
elif temprature < 18 and not is_raining:
    print('Action: turn on the heater but keep windows open for fresh air. ')
    
elif temprature >= 30 or (temprature >= 25 and is_raining):
    print('Action: turn on the Air Conditionor (AC). ')
    
else:
    print('Action: Keep everything turned off. Perfect weather. ')           
