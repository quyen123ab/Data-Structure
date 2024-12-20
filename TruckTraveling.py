class Parcel:
    def __init__(self, parcel_id, weight, destination):
        self.id = parcel_id
        self.weight = weight
        self.destination = destination 

def sort_parcels_by_id(parcels):
    return sorted(parcels, key=lambda parcel: parcel.id, reverse=True)

def group_parcels_by_destination(parcels):
    grouped_parcels = {}
    
    for parcel in parcels:
        if parcel.destination not in grouped_parcels:
            grouped_parcels[parcel.destination] = []
        grouped_parcels[parcel.destination].append(parcel)
    
    return grouped_parcels

def print_invoice(parcel):
    reversed_id = str(parcel.id)[::-1]
    print(f"Parcel ID: {reversed_id}, Destination: {parcel.destination}")

def main():
    num_parcels = int(input("Number of parcels: "))
    parcels = []

    for _ in range(num_parcels):
        parcel_id = int(input("Parcel ID: "))
        weight = float(input("Parcel Weight (kg): "))
        destination = input("Parcel Destination: ")
        parcels.append(Parcel(parcel_id, weight, destination))

    grouped_parcels = group_parcels_by_destination(parcels)

    for destination, group in grouped_parcels.items():
        print(f"\nDelivery Plan for {destination}:")
        sorted_group = sort_parcels_by_id(group)
        for parcel in sorted_group:
            print_invoice(parcel)

if __name__ == "__main__":
    main()
