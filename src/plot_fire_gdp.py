import argparse
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import fire_gdp  # noqa: E402


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Plot forest fire emissions against GDP, one panel '
                    'per country.')
    parser.add_argument('--co2_file', required=True,
                        help='Agrofood CO2 emission CSV file')
    parser.add_argument('--gdp_file', required=True,
                        help='IMF GDP CSV file')
    parser.add_argument('--countries', nargs='+', required=True,
                        help='One or more country names')
    parser.add_argument('--out_file', required=True,
                        help='Output image file (e.g. fire_gdp.png)')
    return parser.parse_args()


def get_correlation(x_values, y_values):
    """Return the Pearson correlation, or None if it is undefined."""
    if len(x_values) < 2:
        return None
    if np.std(x_values) == 0 or np.std(y_values) == 0:
        return None
    return float(np.corrcoef(x_values, y_values)[0, 1])


def plot_countries(co2_file, gdp_file, countries, out_file):
    """Save a figure with one fire-vs-GDP scatter plot per country."""
    fig, axes = plt.subplots(1, len(countries),
                             figsize=(5 * len(countries), 4),
                             squeeze=False)
    for ax, country in zip(axes[0], countries):
        data = fire_gdp.get_fire_gdp_year_data(co2_file, gdp_file, country)
        if len(data) == 0:
            print('No data found for ' + country, file=sys.stderr)
            sys.exit(1)
        fire = [row[1] for row in data]
        gdp = [row[2] for row in data]
        corr = get_correlation(gdp, fire)
        title = country
        if corr is not None:
            title += ' (r = {:.2f})'.format(corr)
            print('{}\tn={}\tr={:.3f}'.format(country, len(data), corr))
        ax.scatter(gdp, fire)
        ax.set_title(title)
        ax.set_xlabel('GDP (millions, local currency)')
        ax.set_ylabel('Forest fire emissions')
    fig.tight_layout()
    fig.savefig(out_file)
    plt.close(fig)


def main():
    """Parse arguments and make the plot."""
    args = parse_args()
    plot_countries(args.co2_file, args.gdp_file, args.countries,
                   args.out_file)


if __name__ == '__main__':
    main()
