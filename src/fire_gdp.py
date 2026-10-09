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
    pass

