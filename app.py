import streamlit as st

def length_conversion(value, from_unit, to_unit):
    # Conversion factors to meters
    length_factors = {
        'Meters': 1,
        'Kilometers': 1000,
        'Miles': 1609.34,
        'Feet': 0.3048,
        'Inches': 0.0254
    }
    
    # Convert to meters first, then to target unit
    meters = value * length_factors[from_unit]
    result = meters / length_factors[to_unit]
    return result

def weight_conversion(value, from_unit, to_unit):
    # Conversion factors to kilograms
    weight_factors = {
        'Kilograms': 1,
        'Grams': 0.001,
        'Pounds': 0.453592,
        'Ounces': 0.0283495
    }
    
    # Convert to kilograms first, then to target unit
    kilos = value * weight_factors[from_unit]
    result = kilos / weight_factors[to_unit]
    return result

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return value

def main():
    # Define units dictionary at the start of main function
    units = {
        'Length': ['Meters', 'Kilometers', 'Miles', 'Feet', 'Inches'],
        'Weight': ['Kilograms', 'Grams', 'Pounds', 'Ounces'],
        'Temperature': ['Celsius', 'Fahrenheit', 'Kelvin'],
        'Volume': ['Liters', 'Milliliters', 'Gallons', 'Cubic Meters', 'Cubic Feet'],
        'Speed': ['Meters per Second', 'Kilometers per Hour', 'Miles per Hour', 'Knots'],
        'Time': ['Seconds', 'Minutes', 'Hours', 'Days', 'Weeks'],
        'Area': ['Square Meters', 'Square Kilometers', 'Square Miles', 'Square Feet', 'Acres', 'Hectares'],
        'Pressure': ['Pascal', 'Kilopascal', 'Bar', 'PSI', 'Atmosphere'],
        'Energy': ['Joules', 'Kilojoules', 'Calories', 'Kilocalories', 'Watt Hours'],
        'Data': ['Bytes', 'Kilobytes', 'Megabytes', 'Gigabytes', 'Terabytes'],
        'Frequency': ['Hertz', 'Kilohertz', 'Megahertz', 'Gigahertz'],
        'Angle': ['Radians', 'Degrees', 'Gradians', 'Minutes', 'Seconds'],
        'Fuel Efficiency': ['Kilometers per Liter', 'Miles per Gallon', 'Liters per 100km', 'Miles per Liter'],
        'Currency': ['USD', 'EUR', 'GBP', 'JPY', 'AUD'],
        'Power': ['Watts', 'Kilowatts', 'Horsepower', 'BTU per hour', 'Megawatts'],
        'Density': ['Kilograms per Cubic Meter', 'Grams per Cubic Centimeter', 'Pounds per Cubic Foot', 'Kilograms per Liter', 'Pounds per Gallon']
    }

    with st.container():
        st.title('✨ Advanced Unit Converter ✨')
        
        # Wrap the main content in a card
        with st.container():
            st.markdown('<div class="conversion-card">', unsafe_allow_html=True)
            
            # Select conversion type with a more prominent style
            conversion_type = st.selectbox(
                '🔄 Select Conversion Type',
                ['Length', 'Weight', 'Temperature', 'Volume', 'Speed', 'Time',
                 'Area', 'Pressure', 'Energy', 'Data', 'Frequency', 'Angle',
                 'Fuel Efficiency', 'Currency', 'Power', 'Density']
            )
            
            # Input value with improved styling
            value = st.number_input('📊 Enter Value', value=0.0)
            
            # Create two columns for from/to units
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown('<div class="column">', unsafe_allow_html=True)
                from_unit = st.selectbox('📥 From', units[conversion_type])
                st.markdown('</div>', unsafe_allow_html=True)
                
            with col2:
                st.markdown('<div class="column">', unsafe_allow_html=True)
                to_unit = st.selectbox('📤 To', units[conversion_type])
                st.markdown('</div>', unsafe_allow_html=True)
            
            # Perform conversion
            if st.button('Convert'):
                if conversion_type == 'Length':
                    result = length_conversion(value, from_unit, to_unit)
                elif conversion_type == 'Weight':
                    result = weight_conversion(value, from_unit, to_unit)
                else:  # Temperature
                    result = temperature_conversion(value, from_unit, to_unit)
                    
                st.success(f'{value} {from_unit} = {result:.4f} {to_unit}')

if __name__ == '__main__':
    main()
