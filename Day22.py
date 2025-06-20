# Build a temperature converter CLI tool
import argparse 
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32 
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9  

def main():
    parser = argparse.ArgumentParser(description="Temperature Converter CLI Tool")
    parser.add_argument("temperature", type=float, help="Temperature value to convert")
    parser.add_argument("--to", choices=["celsius", "fahrenheit"], required=True, help="Convert to Celsius or Fahrenheit")
    args = parser.parse_args()

    if args.to == "celsius":
        converted_temp = fahrenheit_to_celsius(args.temperature)
        print(f"{args.temperature}F is {converted_temp:.2f}C")
    elif args.to == "fahrenheit":
        converted_temp = celsius_to_fahrenheit(args.temperature)
        print(f"{args.temperature}C is {converted_temp:.2f}F")
if __name__ == "__main__":
    main()