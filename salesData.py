import csv

def csvCreator():
    salesData = [
        ['date', 'price', 'product'],
        ['1404-05-15', 150000000, 'laptop'],
        ['1404-05-10', 1000000, 'case'],
        ['1404-05-13', 2000000, 'headphones'],
        ['1404-05-12', 500000, 'charging cable'],
        ['1404-05-03', 75000000, 'cellphone'],
        ['1404-05-03', 25000000, 'watch'],
    ]
    with open('salesData.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(salesData)

def csvAnalyzer(filename):
    totalSales = 0
    salesCount = 0
    dailySales = {}

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            try:
                date = row[0]
                price = int(row[1])
                totalSales += price
                salesCount += 1
                if date in dailySales:
                    dailySales[date] += price
                else:
                    dailySales[date] = price

            except (ValueError, IndexError):
                continue

    averageSales = totalSales / salesCount if salesCount > 0 else 0
    highestSalesDay = None
    maxDailySales = 0

    for date, sales in dailySales.items():
        if sales > maxDailySales:
            maxDailySales = sales
            highestSalesDay = date

    return totalSales, averageSales, highestSalesDay, maxDailySales

csvCreator()
total, average, highestDay, highestAmount = csvAnalyzer('salesData.csv')
print("Sales Analysis Report:")
print("-" * 25)
print(f"Total Sales: {total}")
print(f"Avg. Sales: {average}")
print(f"Highest Sales Date: {highestDay} with a total of {highestAmount}")