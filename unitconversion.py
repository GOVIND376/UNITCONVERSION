from rich.console import Console
from rich.table import Table

console = Console()

'''---------- CONVERSION FUNCTION ----------'''

def km_to_miles(km):    return km*0.621371
def miles_to_km(miles): return miles / 0.621371

def c_to_f(c): return (c*9/5)+32
def f_to_c(f): return (f-32)*5/9

def kg_to_lbs(kg): return kg*2.20462
def labs_to_kg(lbs): return lbs/2.20462

def litres_to_gallon(liters): return liters* 0.264172
def gallon_to_liters(gallon): return gallon/0.264172

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