class bike_management_system:
    def __init__(self):
        self.specs={ "Bullet 350cc":{"Mileage":"38 kmpl","Engine Type":"Single cylinder 4 stroke, air cooled fuel injection","Fuel Capacity":"13.5L","Price":"	₹ 1,50,893 Avg. Ex-showroom price"},
      "Bullet 500cc":{"Mileage":"30 kmpl","Engine Type":"Single Cylinder, 4-Stroke, Spark ignition","Fuel Capacity":"13.5L","Price":" ₹ 3,50,000 Avg. Ex-showroom price"},
      "Classic":{"Mileage":"41.55 kmpl","Engine Type":"349cc Air-Oil cooled single cylinder","Fuel Capacity":"13L","Price":"₹ 1,90,092 Avg. Ex-showroom price"},
      "Thunderbird":{"Mileage":"40 kmpl","Engine Type":" single cylinder, 4-stroke, OHV, SI Engine, single","Fuel Capacity":"20L","Price":"	₹ 1,90,000 Avg. Ex-showroom price"},
      "Himalayan":{"Mileage":"30 kmpl","Engine Type":"411cc, Single Cylinder, 4 Stroke, SOHC, Air Cooled","Fuel Capacity":"15L","Price":"	₹ 2,15,893 Avg. Ex-showroom price"},
      "Interceptor 650":{"Mileage":"24 kmpl","Engine Type":"	Inline twin cylinder, 4 stroke / SOHC","Fuel Capacity":"13.7L","Price":"	₹ 3,50,893 Avg. Ex-showroom price"},
      "Continental GT 650":{"Mileage":"25 kmpl","Engine Type":"Single Cylinder, 4 Stroke, Air Cooled","Fuel Capacity":"12.5L","Price":"	₹ 3,18,793 Avg. Ex-showroom price"}}
        self.bikes={1:"Bullet 350cc",
       2:"Bullet 500cc",
       3:"Classic",
       4:"Thunderbird",
       5:"Himalayan",
       6:"Interceptor 650",
       7:"Continental GT 650"}
        self.stock={"Bullet 350cc":5,
       "Bullet 500cc":5,
       "Classic":8,
       "Thunderbird":2,
       "Himalayan":20,
       "Interceptor 650":1,
       "Continental GT 650":0}
    def add_bike(self,bike,specs,stock):
        if bike in self.stock:
            self.stock[bike]+=stock
        else:
            self.bikes[len(self.bikes)+1]=bike
            self.specs[bike]=specs
            self.stock[bike]=stock
    def display(self):
        print(self.bikes)
    def displaystock(self):
        print(self.stock)
    def remove_bike(self,bike,stock):
        if bike in self.bikes:
            if self.stock[bike]>0:
                self.stock[bike]-=1
            else:
                print(" No Stock")
        else:
            print(bike+" is Not available")
manager=bike_management_system()
class customer:
    def __init__(self):
        self.customers={}
    def viewbike(self):
        manager.display()
        n=int(input("enter the number to display the bike specs"))
        print(manager.specs[bikes[n]])
    def purchase(self):
        manager.display()
        n=int(input("enter the number to purchase the bike"))
        name=input("customer name: ")
        mobile=int(input())
        address=input()
        self.customers[len(self.customers)+1)]={"name":name,"mobile":mobile,"address":address}        
obj=customer()
while True:
    obj.viewbike()
    


















"""dic={ "Bullet 350cc":{"Mileage":"38 kmpl","Engine Type":"Single cylinder 4 stroke, air cooled fuel injection","Fuel Capacity":"13.5L","Price":"	₹ 1,50,893 Avg. Ex-showroom price"},
      "Bullet 500cc":{"Mileage":"30 kmpl","Engine Type":"Single Cylinder, 4-Stroke, Spark ignition","Fuel Capacity":"13.5L","Price":" ₹ 3,50,000 Avg. Ex-showroom price"},
      "Classic":{"Mileage":"41.55 kmpl","Engine Type":"349cc Air-Oil cooled single cylinder","Fuel Capacity":"13L","Price":"₹ 1,90,092 Avg. Ex-showroom price"},
      "Thunderbird":{"Mileage":"40 kmpl","Engine Type":" single cylinder, 4-stroke, OHV, SI Engine, single","Fuel Capacity":"20L","Price":"	₹ 1,90,000 Avg. Ex-showroom price"},
      "Himalayan":{"Mileage":"30 kmpl","Engine Type":"411cc, Single Cylinder, 4 Stroke, SOHC, Air Cooled","Fuel Capacity":"15L","Price":"	₹ 2,15,893 Avg. Ex-showroom price"},
      "Interceptor 650":{"Mileage":"24 kmpl","Engine Type":"	Inline twin cylinder, 4 stroke / SOHC","Fuel Capacity":"13.7L","Price":"	₹ 3,50,893 Avg. Ex-showroom price"},
      "Continental GT 650":{"Mileage":"25 kmpl","Engine Type":"Single Cylinder, 4 Stroke, Air Cooled","Fuel Capacity":"12.5L","Price":"	₹ 3,18,793 Avg. Ex-showroom price"}}
stock={"Bullet 350cc":5,
       "Bullet 500cc":5,
       "Classic":8,
       "Thunderbird":2,
       "Himalayan":20,
       "Interceptor 650":1,
       "Continental GT 650":0}
bikes={1:"Bullet 350cc",
       2:"Bullet 500cc",
       3:"Classic",
       4:"Thunderbird",
       5:"Himalayan",
       6:"Interceptor 650",
       7:"Continental GT 650"}

cusdic={}
class :
    pass
def customer(dic,bikes):
    print(bikes)
    n=int(input("enter the number to know the details of the bike"))
    print(dic[bikes[n]])
    print("enter Y or N to see other models")
    s=input().strip()
    if s=="Y":
        customer()

def purchase(dic,stock,bikes,cusdic):
    print(bikes)
    n=int(input())
    if stock[bikes[n]]==0:
        print("un available")
    else:
        name=input("name : ")
        mobile=int(input("mobile number : "))
        address=input("address : ")
        bikename=bikes[n]
        cusdic[name]=[bikename,mobile,address]
        stock[bikes[n]]-=1
        print(bikes[n] +" is sold")
customer(dic,bikes)
print("Y Or N to purchase bike")
s=input().strip()
if s=="Y":
    purchase(dic,stock,bikes,cusdic)
print(cusdic)
print(stock)
"""
