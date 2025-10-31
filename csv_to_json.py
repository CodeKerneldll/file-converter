import csv, json, os

file_csv = input("Caminho do CSV: ")
file_json = input("Caminho do JSON de saída: ")

if not os.path.exists(file_csv):
    print("Arquivo CSV não existe")
    exit()

data = []
with open(file_csv, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

with open(file_json, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print(f"CSV convertido pra JSON em {file_json}")
