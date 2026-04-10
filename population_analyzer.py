def read_population_data(filepath: str) -> dict:
    data = {}

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            parts = line.split(',')
            if len(parts) == 3:
                country = parts[0].strip()
                year = int(parts[1].strip())
                population = int(parts[2].strip())
                
                if country not in data:
                    data[country] = {}
                data[country][year] = population
                
    return data
