import pandas as pd

def read_data(data) -> pd.DataFrame:
    return pd.read_csv(data)

def check_option(option) -> bool:
    if option not in ("All", "Temperature", "Humidity", "CO2"):
        print(f'Option not valid, should be ("All", "Temperature", "Humidity", "CO2") {option} given!')
        return False
    return True

def filter_data(data: pd.DataFrame, option: str) -> pd.DataFrame:
    if check_option(option):
        if option in ("Temperature", "Humidity", "CO2"):
            return data.loc[data["Sensor"] == option]
    return data

def process_data(data: pd.DataFrame):
    processed_data = []
    for _, row in data.iterrows():
        sensor = row["Sensor"]
        if sensor == "Temperature":
            row["Value"] += 273.15  # Convert to Kelvin
            processed_data.append(row)
        elif sensor == "Humidity":
            row["Value"] /= 100  # Convert to scale 0-1
            processed_data.append(row)
        elif sensor == "CO2":
            row["Value"] += 23  # Compensating for sensor bias
            processed_data.append(row)
    return processed_data

def main() -> None:
    option = "All"  # choose between "All", "Temperature", "Humidity", "CO2"
    data = read_data("sensor_data.csv")
    data = filter_data(data, option)
    processed_data = process_data(data)
    processed_data_single = pd.DataFrame(data=processed_data)
    print(processed_data_single)


if __name__ == "__main__":
    main()
