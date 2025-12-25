import re    
import csv    
import urllib.request 
url = "https://msk.spravker.ru/avtoservisy-avtotehcentry/"
response = urllib.request.urlopen(url)
html_content = response.read().decode()

name_pattern = r"class=\"org-widget-header__title-link\"[^>]*>\s*(?P<names>[^<]+)"
street_pattern = r"<span[^>]*class=\"[^\"]*(?:street|address|location|meta-location|geo)[^\"]*\"[^>]*>\s*(?P<street>[^<\n\r]+)"
num_pattern  = r"<dd class=[^>]+>(?P<numbers>(?:\+|7|8)[^<]+)"
raspi_pattern = r"<dd class=\"spec__value\">(?P<raspi>[^<]*?\d{1,2}:\d{2}[^<]*)"

names = re.findall(name_pattern, html_content)
streets = re.findall(street_pattern, html_content, re.IGNORECASE)
numbers = re.findall(num_pattern, html_content)
raspi = re.findall(raspi_pattern, html_content)

with open('MyParctice.csv', 'w', encoding="utf-8-sig" , newline='') as s:
    writer = csv.writer(s)
    writer.writerow(['Название', 'Адрес', 'Телефон', 'Время работы'])
    max_len = max(len(names), len(streets), len(numbers), len(raspi))
    for i in range(max_len):
        row = [
            names[i] if i < len(names) else '',
            streets[i] if i < len(streets) else '',
            numbers[i] if i < len(numbers) else '',
            raspi[i] if i < len(raspi) else ''
        ]
        writer.writerow(row)
