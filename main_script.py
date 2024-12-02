import pandas as pd
import os

os.chdir( '/Users/dinum-304418/code/HackatonDonn-esAlimentaires' )

# agrimer_rnm = pd.read_parquet("hf://datasets/raphael0202/FranceAgriMer-RNM/COT-MUL-prd_RNM.parquet")
# agrimer_rnm.to_parquet('FranceAgriMer-RNM__COT-MUL-prd_RNM.parquet.parquet')
# agrimer_rnm.to_csv('FranceAgriMer-RNM__COT-MUL-prd_RNM.parquet.csv')
agrimer_rnm = pd.read_parquet( 'FranceAgriMer-RNM__COT-MUL-prd_RNM.parquet.parquet' )


# open_prices = pd.read_parquet("hf://datasets/openfoodfacts/open-prices/prices.parquet")
# open_prices.to_parquet('open_prices__prices.parquet')
# open_prices.to_csv("open_prices__prices.csv")
open_prices = pd.read_parquet( "open_prices__prices.parquet" )


print(
    "Colonnes agrimer: ", agrimer_rnm.columns
)
print(
    "Colonnes open prices: ", open_prices.columns
)
