# Task 1: Start

temperature_fahrenheit = input('Enter today\'s temperature in Fahrenheit: ')


# Task 2: Temperature Conversion

def convert_to_celsius(temperature):
    try:
        temperature_celsius = round((int(temperature) - 32) * 5/9, 2)
    except ValueError:
        print('Please enter a valid numeric value.')

    # Task 3: User Experience
    else:
        print(f'{temperature}°F converted to Celsius is {temperature_celsius}°C.')
    
    # Task 4: Finally
    finally:
        print(f'Thank you for using the weather forecast application!')
convert_to_celsius(temperature_fahrenheit)