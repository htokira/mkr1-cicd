from population_analyzer import read_population_data, calculate_population_change

def main():
    """Основна функція для запуску програми."""
    filename = "data.txt"
    
    print(f"Аналіз населення з файлу: {filename}")
    
    raw_data = read_population_data(filename)
    
    if not raw_data:
        print("Немає даних для обробки.")
        return
    
    results = calculate_population_change(raw_data)

    for country, periods in results.items():
        print(f"\nКраїна: {country}")

        if not periods:
            print("Недостатньо даних для порівняння.")
        
        for period, change in periods.items():
            sign = "+" if change > 0 else ""
            print(f"Період {period}: {sign}{change:,} осіб")

if __name__ == "__main__":
    main()