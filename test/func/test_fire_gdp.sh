test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

file_name=fire_gdp_test.png
rm -f $file_name

run test_plot_runs python src/plot_fire_gdp.py \
    --co2_file test/data/co2_small.csv \
    --gdp_file test/data/gdp_small.csv \
    --countries Brazil Chile \
    --out_file $file_name
assert_exit_code 0
assert_equal $file_name $( ls $file_name )

run test_unknown_country python src/plot_fire_gdp.py \
    --co2_file test/data/co2_small.csv \
    --gdp_file test/data/gdp_small.csv \
    --countries Atlantis \
    --out_file unused.png
assert_exit_code 1

rm -f $file_name unused.png
