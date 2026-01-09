# weather_severity.py

def analyze_severity(readings):
    avg = sum(readings) / len(readings)

    if avg >= 90:
        return avg, "Extreme"
    elif avg >= 80:
        return avg, "Severe"
    elif avg >= 65:
        return avg, "Moderate"
    elif avg >= 50:
        return avg, "Mild"
    elif avg >= 40:
        return avg, "Low"
    else:
        return avg, "Normal"


def main():
    location = input("Enter Location: ")
    date = input("Enter Date: ")

    readings = []
    for i in range(1, 4):
        readings.append(int(input(f"Enter weather index {i}: ")))

    avg, level = analyze_severity(readings)

    print("\n--- Weather Report ---")
    print("Location:", location)
    print("Date:", date)
    print("Average Index:", avg)
    print("Severity Level:", level)


if __name__ == "__main__":
    main()