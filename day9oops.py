class vehicle:
    def __init__ (car, brand, model):
        car.brand = brand  # self likhna best practice hai car ke bajaye
        car.model = model
    
    def display(car):
        print(f'Brand: {car.brand} Model: {car.model}')
    
s1 = vehicle("bmw", "S2")
s1.display()