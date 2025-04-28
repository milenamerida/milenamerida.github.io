def area():
    room = input("What is the room you want to calculate the area? ")
    length = int(input("Enter the length (ft): "))
    width = int(input("Enter the width (ft): "))
    height = int(input("Enter the height (ft): "))
    wallarea = 2*((length*height)+(width*height))
    floorarea = length*width
    ceilarea = length*width

    print("Wall area is {:.2f} sqft,\nFloor area is {:.2f} sqft,\nCeiling area is {:.2f} sqft.".format(wallarea,floorarea,ceilarea))
    return room, wallarea, floorarea, ceilarea

prompt = input("Do you want to run this program? (Yes/No) ").lower()

totalwall = 0
totalfloor = 0
totalceiling = 0
index = 0

rooms = []
walls = []
floors = []
ceilings = []

while prompt == 'yes':
    room, wallarea, floorarea, ceilarea = area()
    rooms.append(room)
    walls.append(wallarea)
    floors.append(floorarea)
    ceilings.append(ceilarea)
    index = index + 1
    prompt = input("Enter another room? (Yes/No) ").lower()

totalwall = sum(walls)
totalfloor = sum(floors)
totalceiling = sum(ceilings)

print(" ")
print(rooms)
print(walls)
print(floors)
print(ceilings)

print("Total wall area is {:.0f} sqft. Total gallons of paint for the walls: {:.0f}.".format(totalwall, totalwall/50))
print("Total floor area is {:.0f} sqft. Total gallons of paint for the floors: {:.0f}.".format(totalfloor, totalfloor/50))
print("Total ceiling area is {:.0f} sqft. Total gallons of paint for the ceilings: {:.0f}.".format(totalceiling, totalceiling/50))
