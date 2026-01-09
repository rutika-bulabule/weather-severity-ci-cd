# weather_severity.py

import os
import sys

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
    # Read from command-line arguments if provided
    if len(sys.argv) == 6:
        location = sys.argv[1]
        date = sys.argv[2]
        readings = [int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])]
    else:
        # fallback to environment variables
        location = os.getenv("LOCATION", "Unknown")
        date = os.getenv("DATE", "Unknown")
        readings = [
            int(os.getenv("WEATHER1", 0)),
            int(os.getenv("WEATHER2", 0)),
            int(os.getenv("WEATHER3", 0))
        ]

    avg, level = analyze_severity(readings)

    print("\n--- Weather Report ---")
    print("Location:", location)
    print("Date:", date)
    print("Average Index:", avg)
    print("Severity Level:", level)

if __name__ == "__main__":
    main()
