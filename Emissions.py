import tkinter as tk
from tkinter import messagebox


def calculate_co2_emissions():
    try:
        battery_capacity = float(battery_entry.get())
        driving_range = float(range_entry.get())

        coal = float(coal_entry.get()) / 100
        gas = float(gas_entry.get()) / 100
        petroleum = float(petroleum_entry.get()) / 100
        hydro = float(hydro_entry.get()) / 100
        wind = float(wind_entry.get()) / 100
        solar = float(solar_entry.get()) / 100

        total_percentage = coal + gas + petroleum + hydro + wind + solar
        if total_percentage != 1:
            messagebox.showerror("Error", "The total percentage must add up to 100%.")
            return

        emissions_factors = {
            "coal": 2.31,
            "gas": 0.96,
            "petroleum": 2.46,
            "hydro": 0.0,
            "wind": 0.0,
            "solar": 0.0
        }

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

        result_label.config(
            text=f"Total CO2 emissions: {total_emissions:.2f} kg CO2\nCO2 emissions per km: {emissions_per_km:.4f} kg CO2/km")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")


# GUI Setup
root = tk.Tk()
root.title("EV Charging CO2 Emissions Calculator")

tk.Label(root, text="Battery Capacity (kWh):").grid(row=0, column=0)
battery_entry = tk.Entry(root)
battery_entry.grid(row=0, column=1)

tk.Label(root, text="Driving Range (km):").grid(row=1, column=0)
range_entry = tk.Entry(root)
range_entry.grid(row=1, column=1)

tk.Label(root, text="Coal (%):").grid(row=2, column=0)
coal_entry = tk.Entry(root)
coal_entry.grid(row=2, column=1)

tk.Label(root, text="Natural Gas (%):").grid(row=3, column=0)
gas_entry = tk.Entry(root)
gas_entry.grid(row=3, column=1)

tk.Label(root, text="Petroleum (%):").grid(row=4, column=0)
petroleum_entry = tk.Entry(root)
petroleum_entry.grid(row=4, column=1)

tk.Label(root, text="Hydropower (%):").grid(row=5, column=0)
hydro_entry = tk.Entry(root)
hydro_entry.grid(row=5, column=1)

tk.Label(root, text="Wind (%):").grid(row=6, column=0)
wind_entry = tk.Entry(root)
wind_entry.grid(row=6, column=1)

tk.Label(root, text="Solar (%):").grid(row=7, column=0)
solar_entry = tk.Entry(root)
solar_entry.grid(row=7, column=1)

tk.Button(root, text="Calculate", command=calculate_co2_emissions).grid(row=8, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=9, column=0, columnspan=2)

root.mainloop()