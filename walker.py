import csv
# adjacency matrix  

# items in the grid
ikea_items = ['Billy Bookcase', 'Kallax Shelf Unit', 'Malm Bed Frame', 'Lack Coffee Table', 'Poäng Armchair', 'Brusali Wardrobe', 'Hemnes Daybed', 'Ektorp Sofa', 'Norraker Table', 'Vittsjo Shelving Unit', 'Fjallbo TV Stand', 'Linnmon Desk', 'Henriksdal Chair', 'Söderhamn Sectional', 'Alex Drawer Unit', 'Brimnes Bed Frame', 'Flisat Children’s Table', 'Stefan Chair', 'Kungsbacka Kitchen Cabinets', 'Raskog Cart', 'Tarva Bed Frame', 'Sultan Lien Bed Frame', 'Luroy Slatted Bed Base', 'Nordli Bed Frame']

# create a subarray of all picks
with open('historic_picks.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader) # skip the first row
    picks = []
    for row in reader:
        subarray = []
        for item in row:
            subarray.append(item)
        picks.append(subarray)

# generate an initial layout
layout = {}
# for count, node in enumerate(graph):
#     layout.update({node: ikea_items[count - 1]})


# def get_key_by_value(value):
#     for k, v in layout.items():
#         if v == value:
#             return k
#     return None

# for pick in picks:
#     for article in pick:
#         print(get_key_by_value(article))

