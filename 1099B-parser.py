import argparse
import csv
from datetime import datetime
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
dfs = tabula.read_pdf(args.input_fn, pages="all", stream=True, lattice=False)
print('converting...')
for df in dfs:
    col = df['VOID CORRECTED']
    rows = col.values.flatten().tolist()
    row_idx = 0
    for row in rows:
        if str(row).startswith('1b'):
            dates = col[row_idx + 1]
        if str(row).startswith("PAYER’S TIN"):
            prices = col[row_idx + 1]
        row_idx += 1
    dates = dates.split(' ')
    dates[0] = datetime.strptime(dates[0], '%Y-%m-%d').strftime('%m/%d/%Y')
    dates[1] = datetime.strptime(dates[1], '%Y-%m-%d').strftime('%m/%d/%Y')
    prices = prices.split(' ')
    dt_acquired, dt_sold = dates[0], dates[1]
    sale_price, cost = prices[1], prices[3]
    table.append(['T', 'TaxPayer Owned', dt_acquired, dt_sold, sale_price, cost])
print('writing ...')
with open(args.output_fn, 'w') as file:
    writer = csv.writer(file)
    writer.writerows(table)

print ('done.')
