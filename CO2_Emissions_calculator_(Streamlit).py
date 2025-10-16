import streamlit as st

# Τίτλος
st.title("EV Charging CO₂ Calculator")

st.markdown("""
Υπολόγισε τις εκπομπές CO₂ για τη φόρτιση ενός ηλεκτρικού οχήματος
ανάλογα με τη χωρητικότητα μπαταρίας, την αυτονομία και το μείγμα ηλεκτροπαραγωγής.
""")

# Εισαγωγή δεδομένων
battery_capacity = st.number_input("Battery Capacity (kWh):", min_value=1.0, value=50.0)
driving_range = st.number_input("Driving Range (km):", min_value=1.0, value=400.0)

st.markdown("### Electricity Mix (%) - πρέπει να αθροίζουν 100%")
coal = st.number_input("Coal", min_value=0.0, max_value=100.0, value=0.0) / 100
gas = st.number_input("Natural Gas", min_value=0.0, max_value=100.0, value=0.0) / 100
petroleum = st.number_input("Petroleum", min_value=0.0, max_value=100.0, value=0.0) / 100
hydro = st.number_input("Hydropower", min_value=0.0, max_value=100.0, value=0.0) / 100
wind = st.number_input("Wind", min_value=0.0, max_value=100.0, value=0.0) / 100
solar = st.number_input("Solar", min_value=0.0, max_value=100.0, value=0.0) / 100

# Έλεγχος συνολικού ποσοστού
total_percentage = coal + gas + petroleum + hydro + wind + solar
if abs(total_percentage - 1.0) > 0.001:
    st.error("⚠️ Total percentage must add up to 100%")
else:
    # Συντελεστές εκπομπών (kg CO₂/kWh)
    emissions_factors = {
        "coal": 3.26,
        "gas": 0.185,
        "petroleum": 2.96,
        "hydro": 0.0,
        "wind": 0.0,
        "solar": 0.0
    }

    # Υπολογισμός εκπομπών
    emissions_per_kwh = (
        coal * emissions_factors["coal"] +
        gas * emissions_factors["gas"] +
        petroleum * emissions_factors["petroleum"] +
        hydro * emissions_factors["hydro"] +
        wind * emissions_factors["wind"] +
        solar * emissions_factors["solar"]
    )

    total_emissions = battery_capacity * emissions_per_kwh
    emissions_per_km = total_emissions / driving_range

    # Εμφάνιση αποτελεσμάτων
    st.subheader("Results")
    st.write(f"**Total CO₂ emissions:** {total_emissions:.2f} kg CO₂")
    st.write(f"**CO₂ emissions per km:** {emissions_per_km:.4f} kg CO₂/km")
