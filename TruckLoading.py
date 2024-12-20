class Parcel:
    def __init__(self, parcel_id, weight):
        self.id = parcel_id
        self.weight = weight  

# sort parcels by id
def sort_parcels_by_id(parcels):
    return sorted(parcels, key=lambda parcel: parcel.id, reverse=True)

def print_invoice(parcel):
    reversed_id = str(parcel.id)[::-1]
    print(f"Parcel ID (reversed): {reversed_id}, Weight: {parcel.weight} kg")

def main():
    num_parcels = int(input("Enter the number of parcels: "))
    parcels = []

    for _ in range(num_parcels):
        parcel_id = int(input("Enter Parcel ID: "))
        weight = float(input("Enter Parcel Weight (kg): "))
        parcels.append(Parcel(parcel_id, weight))

    sorted_parcels = sort_parcels_by_id(parcels)

    print("\nDelivery Plan:")
    for parcel in sorted_parcels:
        print_invoice(parcel)

if __name__ == "__main__":
    main()


