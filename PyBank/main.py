import csv
import os


file_path = os.path.join('Resources', 'budget_data.csv')

unique_months = set()
curr_ = None
changes = []
total = 0
max_incr_profits = {'value': 0, 'date': ''}
max_decr_profits = {'value': 0, 'date': ''}

with open(file_path, encoding='UTF-8') as f:
    csvreader = csv.reader(f, delimiter=",")
    header = next(csvreader)  # skip header

    for (date, profit_loss) in csvreader:
        unique_months.add(date)
        profit_loss = int(profit_loss)

        total += profit_loss

        if curr_ is not None:
            delta = profit_loss - curr_
            changes.append(delta)

            if max_incr_profits['value'] < delta:
                max_incr_profits['value'] = delta
                max_incr_profits['date'] = date

            if max_decr_profits['value'] > delta:
                max_decr_profits['value'] = delta
                max_decr_profits['date'] = date

        curr_ = profit_loss


avg_change = sum(changes) / len(changes)

output = f"""Financial Analysis
----------------------------
Total Months: {len(unique_months)}
Total: ${total}
Average Change: ${round(avg_change, 2)}
Greatest Increase in Profits: {max_incr_profits['date']} (${max_incr_profits['value']})
Greatest Decrease in Profits: {max_decr_profits['date']} (${max_decr_profits['value']})"""
print(output)

output_file = os.path.join('analysis', 'output.txt')

with open(output_file, "w") as f:
    f.write(output)
