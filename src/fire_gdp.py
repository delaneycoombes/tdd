import csv


def get_data(file_name,
             query_column=None,
             query_value=None,
             return_header=False):
    rows = []
    with open(file_name, 'r', newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if query_column is None or row[query_column] == query_value:
                rows.append(row)
    if return_header:
        return header, rows
    return rows


def get_column_index(header, column_name):
    try:
        return header.index(column_name)
    except ValueError:
        return None


def get_fire_gdp_year_data(co2_file, gdp_file, country):
    co2_header, co2_rows = get_data(co2_file, 0, country, True)
    gdp_header, gdp_rows = get_data(gdp_file, 0, country, True)

    if len(gdp_rows) == 0:
        return []
    gdp_row = gdp_rows[0]

    fire_index = get_column_index(co2_header, 'Forest fires')

    result = []
    for row in co2_rows:
        year = row[1]
        gdp_index = get_column_index(gdp_header, year)
        if gdp_index is None:
            continue
        fire = row[fire_index]
        gdp = gdp_row[gdp_index]
        if fire == '' or gdp == '':
            continue
        result.append([int(year), float(fire), float(gdp)])
    return result

