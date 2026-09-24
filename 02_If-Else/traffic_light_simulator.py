# Traffic Light Simulator Program

light_color = input('what color is the traffic light? (red/yellow/green): ').lower()

if light_color == 'red':
    print('Stop! do not cross')
    
elif light_color == 'yellow':
    print('Slow down and prepare to stop!')

elif light_color == 'green':
    print('Go ahead safely!')

else:
    print("Invalid color! That traffic light is broken.")