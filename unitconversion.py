from rich.console import Console
from rich.table import Table

console = Console()

'''---------- CONVERSION FUNCTION ----------'''

def km_to_miles(km):    return km*0.621371
def miles_to_km(miles): return miles / 0.621371

def c_to_f(c): return (c*9/5)+32
def f_to_c(f): return (f-32)*5/9

def kg_to_lbs(kg): return kg*2.20462
def lbs_to_kg(lbs): return lbs/2.20462

def liters_to_gallons(liters): return liters* 0.264172
def gallons_to_liters(gallons): return gallons/0.264172

def get_float_input(prompt):
    while True:
        try: 
            value=float(input(prompt))
            return value 
        except ValueError :
            console.print("Invalid  input !! Please enter a number .",style="bold red")
def print_history(history):
    if not history :
        console.print("No conversions yet.",style="yellow")
        return
    table=Table(title="Conversion History")
    table.add_column("Input",justify="right")
    table.add_column("Converted",justify="right")
    table.add_column("Type",justify="right")
    
    for entry in history :
        table.add_row(entry["input"],entry["converted"],entry["type"])
        console.print(table)
def main():
    history = []

    while True:
        console.print("\n [bold green]Unit Converter[/bold green]")
        console,print(  "1. Kilometers to Miles"    )
        console,print(  "2. Miles to Kilometers "   )
        console,print(  "3. Clesious to Fahrenheit" )
        console,print(  "4. Fahrenheit to Clesious" )
        console,print(  "5. Kilogram to Pounds "    )
        console,print(  "6. Pounds to Kilogram "    )
        console,print(  "7. Liters to Gallons "     )
        console,print(  "8. Gallons to Litres"      )
        console,print(  "9. View conversion History")
        console.print("0.EXIT")

        choice = input("Choose comversion (0-9):")
        if choice == "0":
            console,print(" GOODBYE !!!",style="bold green" )
            break
        elif choice == "9" :
            print_history(history)
            continue
    value = get_float_input("Enter value : ")
    if choice=="1":
        result= km_to_miles(value)
        console.print(f"{value} km = {result:2.f} miles",style="cyan")
        history.append({"input": f"{value} km ", "converted": f"{result:.2f} miles","type": "Distance"})
    elif choice == '2':
            result = miles_to_km(value)
            console.print(f"{value} miles = {result:.2f} km", style="cyan")
            history.append({"input": f"{value} miles", "converted": f"{result:.2f} km", "type": "Distance"})
    elif choice == '3':
            result = c_to_f(value)
            console.print(f"{value}°C = {result:.2f}°F", style="cyan")
            history.append({"input": f"{value}°C", "converted": f"{result:.2f}°F", "type": "Temperature"})
    elif choice == '4':
            result = f_to_c(value)
            console.print(f"{value}°F = {result:.2f}°C", style="cyan")
            history.append({"input": f"{value}°F", "converted": f"{result:.2f}°C", "type": "Temperature"})
    elif choice == '5':
            result = kg_to_lbs(value)
            console.print(f"{value} kg = {result:.2f} lbs", style="cyan")
            history.append({"input": f"{value} kg", "converted": f"{result:.2f} lbs", "type": "Weight"})
    elif choice == '6':
            result = lbs_to_kg(value)
            console.print(f"{value} lbs = {result:.2f} kg", style="cyan")
            history.append({"input": f"{value} lbs", "converted": f"{result:.2f} kg", "type": "Weight"})
    elif choice == '7':
            result = liters_to_gallons(value)
            console.print(f"{value} liters = {result:.2f} gallons", style="cyan")
            history.append({"input": f"{value} liters", "converted": f"{result:.2f} gallons", "type": "Volume"})
    elif choice == '8':
            result = gallons_to_liters(value)
            console.print(f"{value} gallons = {result:.2f} liters", style="cyan")
            history.append({"input": f"{value} gallons", "converted": f"{result:.2f} liters", "type": "Volume"})
    else:
         console.print("Invalid choice.",style="bold red")
if __name__ == "__main__":
    main()
