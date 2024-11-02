from datetime import datetime
from django.db import models



from multiselectfield import MultiSelectField

# Create your models here.


class Car(models.Model):

    state_choice = (
    ('Alabama', 'Alabama'),
    ('Alaska', 'Alaska'),
    ('Arizona', 'Arizona'),
    ('Arkansas', 'Arkansas'),
    ('California', 'California'),
    ('Colorado', 'Colorado'),
    ('Connecticut', 'Connecticut'),
    ('Delaware', 'Delaware'),
    ('District Of Columbia', 'District Of Columbia'),
    ('Florida', 'Florida'),
    ('Georgia', 'Georgia'),
    ('Hawaii', 'Hawaii'),
    ('Idaho', 'Idaho'),
    ('Illinois', 'Illinois'),
    ('Indiana', 'Indiana'),
    ('Iowa', 'Iowa'),
    ('Kansas', 'Kansas'),
    ('Kentucky', 'Kentucky'),
    ('Louisiana', 'Louisiana'),
    ('Maine', 'Maine'),
    ('Maryland', 'Maryland'),
    ('Massachusetts', 'Massachusetts'),
    ('Michigan', 'Michigan'),
    ('Minnesota', 'Minnesota'),
    ('Mississippi', 'Mississippi'),
    ('Missouri', 'Missouri'),
    ('Montana', 'Montana'),
    ('Nebraska', 'Nebraska'),
    ('Nevada', 'Nevada'),
    ('New Hampshire', 'New Hampshire'),
    ('New Jersey', 'New Jersey'),
    ('New Mexico', 'New Mexico'),
    ('New York', 'New York'),
    ('North Carolina', 'North Carolina'),
    ('North Dakota', 'North Dakota'),
    ('Ohio', 'Ohio'),
    ('Oklahoma', 'Oklahoma'),
    ('Oregon', 'Oregon'),
    ('Pennsylvania', 'Pennsylvania'),
    ('Rhode Island', 'Rhode Island'),
    ('South Carolina', 'South Carolina'),
    ('South Dakota', 'South Dakota'),
    ('Tennessee', 'Tennessee'),
    ('Texas', 'Texas'),
    ('Utah', 'Utah'),
    ('Vermont', 'Vermont'),
    ('Virginia', 'Virginia'),
    ('Washington', 'Washington'),
    ('West Virginia', 'West Virginia'),
    ('Wisconsin', 'Wisconsin'),
    ('Wyoming', 'Wyoming'),
    )


    

    year_choice = []

    for r in range(2000,datetime.now().year +1 ):
        year_choice.append((r,r))
    

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    city_choice = (
    ('New York City', 'New York City'),
    ('Los Angeles', 'Los Angeles'),
    ('Chicago', 'Chicago'),
    ('Houston', 'Houston'),
    ('Phoenix', 'Phoenix'),
    ('Philadelphia', 'Philadelphia'),
    ('San Antonio', 'San Antonio'),
    ('San Diego', 'San Diego'),
    ('Dallas', 'Dallas'),
    ('San Jose', 'San Jose'),
    ('Atlanta', 'Atlanta'),
    ('Miami', 'Miami'),
    ('Boston', 'Boston'),
    ('Detroit', 'Detroit'),
    ('Seattle', 'Seattle'),
    ('Denver', 'Denver'),
    ('Washington D.C.', 'Washington D.C.'),
    ('Las Vegas', 'Las Vegas'),
    ('Portland', 'Portland'),
    ('Oklahoma City', 'Oklahoma City'),
    )

    color_choice = (
        ('Black', 'Black'),
        ('White', 'White'),
        ('Gray', 'Gray'),
        ('Silver', 'Silver'),
        ('Blue', 'Blue'),
        ('Red', 'Red'),
        ('Green', 'Green'),
        ('Yellow', 'Yellow'),
        ('Orange', 'Orange'),
        ('Brown', 'Brown'),
        ('Gold', 'Gold'),
        ('Pink', 'Pink'),
        ('Purple', 'Purple'),
    )

    model_choice = (
        ('Ferrari 480 GTB', 'Ferrari 480 GTB'),
        ('Ferrari F8 Tributo', 'Ferrari F8 Tributo'),
        ('Tesla Model 3', 'Tesla Model 3'),
        ('Tesla Model Y Performance', 'Tesla Model Y Performance'),
        ('Ford Mustang', 'Ford Mustang'),
        ('Ford Ranger Raptor', 'Ford Ranger Raptor'),
        ('Toyota Camry', 'Toyota Camry'),
        ('Toyota Prius', 'Toyota Prius'),
        ('Benz CLA-Class', 'Benz CLA-Class'),
        ('Benz GLA-Class', 'Benz GLA-Class'),
        ('BMW 3 Series', 'BMW 3 Series'),
        ('BMW X5', 'BMW X5'),
        ('Honda Civic', 'Honda Civic'),
        ('Nissan Altima', 'Nissan Altima'),
        ('Volkswagen Scirocco', 'Volkswagen Scirocco'),
        ('Audi A4', 'Audi A4'),
        ('Maserati Ghibli', 'Maserati Ghibli'),
        ('Lamborghini Huracán', 'Lamborghini Huracán'),
    )

    condition_choice = (
        ('New', 'New'),
        ('Used', 'Used'),
        ('First Hand', 'First Hand'),
        ('Test Drive', 'Test Drive'),
        ('Refurbished', 'Refurbished'),
        ('Certified Pre-Owned', 'Certified Pre-Owned'),
    )

    body_style_choice = (
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Coupe', 'Coupe'),
        ('Hatchback', 'Hatchback'),
        ('Convertible', 'Convertible'),
        ('Wagon', 'Wagon'),
        ('Pickup Truck', 'Pickup Truck'),
        ('Van', 'Van'),
    )

    engine_choice = (
        ('Internal Combustion Engine', 'Internal Combustion Engine'),
        ('Electric Vehicle', 'Electric Vehicle'),
        ('Hybrid', 'Hybrid'),
        ('Diesel', 'Diesel'),
        ('Plug-in Hybrid Electric Vehicle', 'Plug-in Hybrid Electric Vehicle'),
        ('Fuel Cell Electric Vehicle', 'Fuel Cell Electric Vehicle'),
    )

    interior_choice = (
        ('Cloth', 'Cloth'),
        ('Leather', 'Leather'),
        ('Vinyl', 'Vinyl'),
        ('Suede', 'Suede'),
        ('Mixed Materials', 'Mixed Materials'),
    )

    transmission_choice = (
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
        ('Continuously Variable Transmission', 'Continuously Variable Transmission'),
        ('Dual-Clutch Transmission', 'Dual-Clutch Transmission'),
        ('Semi-Automatic', 'Semi-Automatic'),
    )

    fuel_type_choice = (
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
        ('Compressed Natural Gas', 'Compressed Natural Gas'),
        ('E85 Ethanol', 'E85 Ethanol'),
        ('Biodiesel', 'Biodiesel'),
    )




    



    car_title = models.CharField(max_length=250)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(choices=city_choice, max_length=100)
    color = models.CharField(choices=color_choice, max_length=100)
    model = models.CharField(choices=model_choice, max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(choices=condition_choice, max_length=100)
    
    price = models.IntegerField()
    
    description = models.CharField(max_length=250)

    
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/') 
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) 
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) 
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) 
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) 

    features = models.CharField(max_length=255) 
    
    body_style = models.CharField(choices=body_style_choice, max_length=100)
    engine = models.CharField(choices=engine_choice, max_length=100)   
    transmission = models.CharField(choices=transmission_choice, max_length=100)  
    interior = models.CharField(choices=interior_choice, max_length=100)   
    
    miles = models.IntegerField()   
    
    doors = models.CharField(choices=door_choices, max_length=10)    
    
    passengers = models.IntegerField()   

    vin_no = models.CharField(max_length=50) 
    
    milage = models.IntegerField()
    
    fuel_type = models.CharField(choices=fuel_type_choice, max_length=50) 
    
    no_of_owners = models.CharField(max_length=100) 
    
    is_featured = models.BooleanField(default=False) 

    for_rented = models.BooleanField(default=False) 
    
    created_at = models.DateField(default=datetime.now, blank=True) 

    def __str__(self):
        return self.car_title


class Car_at_top(models.Model):

    car_title = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    car_image_at_top = models.ImageField(upload_to='photo/top_pge/%Y/%m/%d')