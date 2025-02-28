import streamlit as st


def convert_length(value:float, from_unit:str, to_unit:str) -> float:
    length_units:dict[str, float] = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'miles': 1609.34,
        'yards': 0.9144,
        'feet': 0.3048,
        'inches': 0.0254
    }
    return value * length_units[from_unit] / length_units[to_unit]

def convert_area(value:float, from_unit:str, to_unit:str) -> float:
    area_units:dict[str, float] = {
        'square meters': 1.0,
        'square kilometers': 1e6,
        'square centimeters': 0.0001,
        'square millimeters': 1e-6,
        'square miles': 2.59e6,
        'acres': 4046.86,
        'hectares': 10000.0
    }
    return value * area_units[from_unit] / area_units[to_unit]

def convert_volume(value:float, from_unit:str, to_unit:str) -> float:
    volume_units = {
        'liters': 1.0,
        'milliliters': 0.001,
        'cubic meters': 1000.0,
        'cubic centimeters': 0.001,
        'cubic inches': 0.0163871,
        'cubic feet': 28.3168,
        'gallons': 3.78541
    }
    return value * volume_units[from_unit] / volume_units[to_unit]

def convert_mass(value:float, from_unit:str, to_unit:str) -> float:
    mass_units:dict[str, float] = {
        'kilograms': 1.0,
        'grams': 0.001,
        'milligrams': 1e-6,
        'pounds': 0.453592,
        'ounces': 0.0283495
    }
    return value * mass_units[from_unit] / mass_units[to_unit]

def convert_time(value, from_unit, to_unit):
    time_units = {
        'seconds': 1.0,
        'minutes': 60.0,
        'hours': 3600.0,
        'days': 86400.0
    }
    return value * time_units[from_unit] / time_units[to_unit]

def convert_temperature(value:float, from_unit:str, to_unit:str) -> float:
    if from_unit == to_unit:
        return value
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return value * 9/5 + 32
    if from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    if from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273.15
    if from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273.15
    if from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        return (value - 32) * 5/9 + 273.15
    if from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        return (value - 273.15) * 9/5 + 32

def convert_power(value:float, from_unit:str, to_unit:str) -> float:
    power_units:dict[str, float] = {
        'watts': 1.0,
        'kilowatts': 1000.0,
        'horsepower': 745.7
    }
    return value * power_units[from_unit] / power_units[to_unit]


st.title(":red[Unit] Converter")
st.markdown("Convert any unit to another unit")
st.divider()

conversion_type:str = st.selectbox("Select conversion type", ["Length", "Area", "Volume", "Mass", "Time", "Temperature", "Power"])

if conversion_type == "Length":
    units = ['meters', 'kilometers', 'centimeters', 'millimeters', 'miles', 'yards', 'feet', 'inches']
    convert_function = convert_length
elif conversion_type == "Area":
    units = ['square meters', 'square kilometers', 'square centimeters', 'square millimeters', 'square miles', 'acres', 'hectares']
    convert_function = convert_area
elif conversion_type == "Volume":
    units = ['liters', 'milliliters', 'cubic meters', 'cubic centimeters', 'cubic inches', 'cubic feet', 'gallons']
    convert_function = convert_volume
elif conversion_type == "Mass":
    units = ['kilograms', 'grams', 'milligrams', 'pounds', 'ounces']
    convert_function = convert_mass
elif conversion_type == "Time":
    units = ['seconds', 'minutes', 'hours', 'days']
    convert_function = convert_time
elif conversion_type == "Temperature":
    units = ['Celsius', 'Fahrenheit', 'Kelvin']
    convert_function = convert_temperature
elif conversion_type == "Power":
    units = ['watts', 'kilowatts', 'horsepower']
    convert_function = convert_power

from_unit:str = st.selectbox("From unit", units)
to_unit:str = st.selectbox("To unit", units)
value:float = st.number_input("Enter value", value=0.0)

if st.button("Convert"):
    result:float = convert_function(value, from_unit, to_unit)
    container=st.container(border=True)
    container.write(f":red[{value:.3f}] {from_unit} is equal to :blue[{result:.3f}] {to_unit}")
    st.toast("Conversion successful")

st.html(
    """ 
    <style>
        .container {
            border: 1px solid red;
            width: 50%;
            margin: 0 auto;
            padding:2px;
            text-align: center;
            background-color:#A52A2A;
            color:white;
            border-radius:10px;
        }
    </style>
  <div class="container">
   <h1>Developed by Alyan Ali</h1>
 </div>

    """
)