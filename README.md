# tdd

```
curl -L "https://docs.google.com/uc?export=download&id=1AsXP_OGs1O_TDeXiZjk3fYV1SrG4vwXF" -o data/Agrofood_co2_emission.csv
curl -L "https://docs.google.com/uc?export=download&id=19YEPysdnK7VCXuAe9Og9pwYkNT5CbQzr" -o data/IMF_GDP.csv
```

# intro
The project looked into if yearly forest fire emissions are related to GDP in Brazil, Canada, Australia, and Indonesia. The GDP is reported in the respective country's currency, so they are analyzed individually.


# Results
Each panel shows one country, with one point per year. The Pearson
correlations between GDP and forest fire emissions were weak overall:
Brazil r = -0.189 (n = 25), Canada r = -0.349 (n = 31), Australia
r = 0.006 (n = 31) and Indonesia r = 0.086 (n = 13). Canada has the
strongest relationship, and it is moderately negative: years with higher
GDP tended to have lower fire emissions. Brazil is weakly negative, and
Australia and Indonesia show essentially no linear relationship. Indonesia
also has the fewest years of data, so its estimate is the least reliable.
Because GDP generally rises over time, these correlations may partly
reflect a time trend, and fire emissions are likely driven mostly by
climate and land use rather than GDP. These results show correlation,
not causation.

## Methods
Data came from `Agrofood_co2_emission.csv` (forest fire emissions by
country and year) and `IMF_GDP.csv` (GDP in millions of local currency),
downloaded into a `data/` folder that is not committed. For each country,
the two files were matched by year. Years with a missing fire or GDP value,
or a year not in the GDP file, were skipped. Pearson correlations were
computed separately for each country.

To make the plots from the downloaded data:

    mkdir -p data figures
    python src/plot_fire_gdp.py \
        --co2_file data/Agrofood_co2_emission.csv \
        --gdp_file data/IMF_GDP.csv \
        --countries Brazil Canada Australia Indonesia \
        --out_file figures/fire_gdp.png

To run the tests:

    PYTHONPATH=src python -m unittest discover -s test/unit -v
    bash test/func/test_fire_gdp.sh