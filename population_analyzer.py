def read_population_data(filepath: str) -> dict:
    """Зчитує дані про населення з текстового файлу."""
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


def calculate_population_change(data: dict) -> dict:
    """Обчислює щорічну зміну населення для кожної країни."""
    changes = {}

    for country, yearly_data in data.items():
        sorted_years = sorted(yearly_data.keys())
        changes[country] = {}

        for i in range(1, len(sorted_years)):
            prev_year = sorted_years[i-1]
            curr_year = sorted_years[i]

            change = yearly_data[curr_year] - yearly_data[prev_year]
            period = f"{prev_year}-{curr_year}"
            changes[country][period] = change

    return changes
