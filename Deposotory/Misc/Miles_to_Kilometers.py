import time
def convert(miles):
    return 1.6*miles
while True:
    try:
        miles = float(input("How many miles?:"))
        time.sleep(0.5)
        km = convert(miles)
        float(km)
        print(km)
    except:
        print("Please enter an integer or a decimal number")
