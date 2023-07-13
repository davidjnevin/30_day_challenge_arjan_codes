import pandas as pd


def celcuis_to_kelvin(temperature: float) -> float:
    return temperature + 273.15

def convert_humidity_to_scale_0_1(humidity: float) -> float:
    return humidity / 100

def compensate_co2_bias(value: float, bias: float = 23) -> float:
    return value + bias

def process_data(data: pd.DataFrame, option: str) -> pd.DataFrame:
    processed_data: list[pd.DataFrame] = []
    if option in ("Temperature", "Humidity", "CO2"):
        data = data.loc[data["Sensor"] == option]

    for _, row in data.iterrows():
        processed_row = process_row(row)
        processed_data.append(processed_row)

    return pd.DataFrame(data=processed_data)

def process_row(row: pd.DataFrame) -> pd.DataFrame:
    sensor: str = row["Sensor"]
    value: float = row["Value"]
    processing_function = {
        "Temperature": celcuis_to_kelvin,
        "Humidity": convert_humidity_to_scale_0_1,
        "CO2": compensate_co2_bias,
    }
    row["Value"] = processing_function[sensor](value)
    return row

def main() -> None:
    raw_data = pd.read_csv("sensor_data.csv")
    processed_data = process_data(data=raw_data, option="ALL")
    print(processed_data)


if __name__ == "__main__":
    main()
