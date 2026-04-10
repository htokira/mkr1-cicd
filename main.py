from population_analyzer import read_population_data

def main():
    """Основна функція для запуску програми."""
    filename = "data.txt"
    
    print(f"Аналіз населення з файлу: {filename}")
    
    raw_data = read_population_data(filename)
    
    if not raw_data:
        print("Немає даних для обробки.")
        return
    
    print(raw_data)

if __name__ == "__main__":
    main()