import argparse
import csv
import tabula

"""requirements.txt
tabula-py
jpype1
"""

cli_parser = argparse.ArgumentParser("1099B-parser")
cli_parser.add_argument("input_fn", help="Path to the 1099B document")
cli_parser.add_argument("output_fn", help="Desired output filename")
args = cli_parser.parse_args()

table = []
table.append(['Owner', 'Description', 'DtAcquired', 'DtSold', 'SalesPrice', 'Cost'])

print('reading...')
dfs = tabula.read_pdf(args.input_fn, pages="1-2", stream=True, lattice=False)
print('converting...')
for df in dfs:
    col = df['VOID CORRECTED']
    dates = col[7]
    prices = col[9]
    dates = dates.split(' ')
    prices = prices.split(' ')
    dt_acquired, dt_sold = dates[0], dates[1]
    sale_price, cost = prices[1], prices[3]
    table.append(['T', 'TaxPayer Owned', dt_acquired, dt_sold, sale_price, cost])
print('writing ...')
with open(args.output_fn, 'w') as file:
    writer = csv.writer(file)
    writer.writerows(table)

print ('done.')
