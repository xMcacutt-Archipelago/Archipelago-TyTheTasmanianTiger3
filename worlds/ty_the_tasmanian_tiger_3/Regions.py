from typing import Dict

from BaseClasses import Region, Location, Entrance

ty1_levels: Dict[str, str] = {
    "M1": "The Dreaming",
    "T1": "New Burramudgee",
    "T2": "Cassopolis",
    "M3": "Cinder Canyon",
    "M13": "Dead Dingo Marsh",
    "M14": "Kaka Boom Island",
    "M23": "Gooboo Gully",
    "M24": "Mount Boom Basin",
    "01": "SR Desert",
    "02": "SR Swamp",
    "01B": "Razorback Stream",
    "02D": "Pippy Beach",
    "M34": "Quinking",
    # "c3": "Dinky Dino Saurus",
    #"c4": "Buster the Nanobot Boss",
    #"e1": "Cass' Run",
    #"e4": "Final Battle",

    #"m2": "Explosive Cargo",
    # "m8": "Surfing Safari",
    #"m12": "Canopy Capers",
    #"m13": "Croc Stock Pile",
    #"m14": "Fire Fight",
    #"m15": "Pirate Panic",
    #"m27": "Ripper Rita",
    #"m28": "Sheep Dip",
    #"m33": "Dennis Freeway",
    #"m40": "Sea Lab",
    #"m49": "Chopper Challenge",
    #"m50": "Robot Bug Battle",
    #"m64": "Deep Sea Scare",
    #"m69": "Surf's Up",

    #"m35": "Up The Creek",
    #"m52": "Oil Rig Fire",
    #"m56": "Attack of the RoboCrabs",

}

def create_location(world, region, name: str, code: int):
    location = Location(world.player, name, code, region)
    region.locations.append(location)

def create_locations(world, region, loc_dict):
    for (key, data) in loc_dict.items():
        if data.region != region.name:
            continue
        create_location(world, region, key, data.code)




def create_region(world, name: str, location_dict):
    region = Region(name, world.player, world.multiworld)
    create_locations(world, region, location_dict)
    world.multiworld.regions.append(region)
    return region

def create_ty3_regions(world, location_dict):
    create_region(world, "Menu", location_dict)
    create_region(world, "Burramudgee HQ", location_dict)
    create_region(world, "Burramudgee HQ - Crates", location_dict)
    create_region(world, "Currawong", location_dict)
    create_region(world, "Burramudgee HQ - Infra", location_dict)
    create_region(world, "Burramudgee Town", location_dict)
    create_region(world, "Burramudgee Town - Infra", location_dict)
    create_region(world, "SR - Burramudgee Town", location_dict)
    create_region(world, "SR - Outback Oasis", location_dict)
    create_region(world, "Outback Oasis", location_dict)
    create_region(world, "Outback Oasis - Infra", location_dict)
    create_region(world, "SR - Never Never", location_dict)
    create_region(world, "Never Never", location_dict)
    create_region(world, "Never Never - Infra", location_dict)
    create_region(world, "SR - Faire Dinkum", location_dict)
    create_region(world, "Faire Dinkum", location_dict)
    create_region(world, "Faire Dinkum - Infra", location_dict)
    create_region(world, "Sulphur Rocks", location_dict)
    create_region(world, "Sulphur Rocks - Infra", location_dict)
    create_region(world, "SR - Wetlands", location_dict)
    create_region(world, "Wetlands", location_dict)
    create_region(world, "Wetlands Tree", location_dict)
    create_region(world, "Wetlands - Infra", location_dict)
    create_region(world, "Fluffy's Fortress", location_dict)
    create_region(world, "SR - Fluffy's Fortress", location_dict)
    create_region(world, "Buster the Nanobot Boss", location_dict)
    create_region(world, "Cass' Run", location_dict)
    create_region(world, "Southern Rivers - Prawn", location_dict)
    create_region(world, "Southern Rivers - Pineapple", location_dict)
    create_region(world, "Southern Rivers - Banana", location_dict)
    create_region(world, "Southern Rivers - Pie", location_dict)
    create_region(world, "Southern Rivers - Burramudgee", location_dict)
    create_region(world, "Southern Rivers - Sly", location_dict)
    create_region(world, "SR - Min Min Plains", location_dict)
    create_region(world, "SR - Freeway Training Grounds", location_dict)
    create_region(world, "Freeway Training Grounds", location_dict)
    create_region(world, "SR - Dennis Freeway", location_dict)
    create_region(world, "Dennis Freeway", location_dict)
    create_region(world, "SR - Muddy Bottom", location_dict)
    create_region(world, "Muddy Bottom", location_dict)
    create_region(world, "SR - Ripper Nipper", location_dict)
    create_region(world, "SR - Beach Training Grounds", location_dict)
    create_region(world, "Beach Training Grounds", location_dict)
    create_region(world, "SR - Oil Rig", location_dict)
    create_region(world, "Oil Rig", location_dict)
    create_region(world, "SR - Wobbygon Bay", location_dict)
    create_region(world, "Beach Sub", location_dict)
    create_region(world, "Deep Sea Scare", location_dict)
    create_region(world, "SR - Lava Falls Race", location_dict)
    create_region(world, "SR - MountBoom End", location_dict)
    create_region(world, "MountBoom", location_dict)
    create_region(world, "MountBoom -> Infra", location_dict)
    create_region(world, "SR - MountBoom Start", location_dict)
    create_region(world, "MountBoom Start", location_dict)
    create_region(world, "MountBoom End", location_dict)
    create_region(world, "SR - Frill Neck Forest", location_dict)
    create_region(world, "Frill Neck Forest", location_dict)
    create_region(world, "Frill Neck Forest - Infra", location_dict)
    create_region(world, "SR - Old Stony Creek", location_dict)
    create_region(world, "Old Stony Creek", location_dict)
    create_region(world, "SR - Camping", location_dict)
    create_region(world, "SR - Refinery Run", location_dict)
    create_region(world, "SR - Fire Fight", location_dict)
    create_region(world, "Fire Fight", location_dict)
    create_region(world, "SR - Sly Shack", location_dict)
    create_region(world, "SR - Outback Dash", location_dict)
    create_region(world, "SR - Truck Tragedy", location_dict)
    create_region(world, "SR - Never Never Road", location_dict)
    create_region(world, "SR - Plutonium Panic", location_dict)
    create_region(world, "SR - 50 Foot Squeaver", location_dict)
    create_region(world, "SR - Min Min Mining", location_dict)
    create_region(world, "SR - Turbo Track", location_dict)
    create_region(world, "SR - Patchy", location_dict)
    create_region(world, "Patchy", location_dict)
    create_region(world, "SR - Lake Burramudgee", location_dict) #m2
    create_region(world, "Lake Burramudgee", location_dict)
    create_region(world, "SR - Bush Fire", location_dict)
    create_region(world, "Bush Fire", location_dict)
    create_region(world, "SR - Sulphur Rocks", location_dict)
    create_region(world, "SR - King Squeaver", location_dict)
    create_region(world, "SR - Hearty Beach", location_dict)
    create_region(world, "SR - Truck Stop", location_dict)
    create_region(world, "SR - Dusty Barrows", location_dict)


def connect_regions(world, from_name: str, to_name: str, entrance_name: str, entrance_group = 0, two_way = False) -> Entrance:
    entrance_region = world.get_region(from_name)
    exit_region = world.get_region(to_name)
    entrance = entrance_region.connect(exit_region, entrance_name)
    entrance.randomization_group = entrance_group
    # if entrance.randomization_group == 0:
    #     world.disconnect_entrance_for_randomization(entrance)
    return entrance

def connect_ty3_regions(world):
    connect_regions(world, "Southern Rivers - Burramudgee", "Southern Rivers - Sly","Patchy Barriers West", 1)
    connect_regions(world, "Southern Rivers - Burramudgee", "Southern Rivers - Prawn","Patchy Barriers South", 1)
    connect_regions(world, "Southern Rivers - Sly", "Southern Rivers - Pineapple","Fluffy Barriers South", 1)
    connect_regions(world, "Southern Rivers - Burramudgee", "Southern Rivers - Banana","Fluffy Barriers North", 1)
    connect_regions(world, "Southern Rivers - Pineapple", "Southern Rivers - Banana","Truck Stop Clear", 1)
    connect_regions(world, "Southern Rivers - Burramudgee", "Southern Rivers - Pie","Buster Barriers West", 1)
    connect_regions(world, "Southern Rivers - Prawn", "Southern Rivers - Pie","Buster Barriers East", 1)

    #Burra
    connect_regions(world, "Menu", "Burramudgee HQ",
                    "Start", 3)
    connect_regions(world, "Burramudgee HQ", "Cass' Run",
                    "Bush Rescue Plane", 1)
    connect_regions(world, "Burramudgee HQ", "Currawong",
                    "Picture", 1)
    connect_regions(world, "Burramudgee HQ", "Burramudgee HQ - Infra",
                    "Burramudgee HQ -> Infra", 1)
    connect_regions(world, "Burramudgee HQ", "Burramudgee HQ - Crates",
                    "Burramudgee HQ -> Crates", 1)
    connect_regions(world, "Burramudgee HQ", "Burramudgee Town",
                    "Burramudgee Tunnel")
    connect_regions(world, "Burramudgee Town", "Burramudgee Town - Infra",
                    "Burramudgee Town -> Infra", 1)
    connect_regions(world, "Burramudgee Town", "SR - Burramudgee Town",
                    "Burramudgee Connector")
    connect_regions(world, "SR - Burramudgee Town", "Southern Rivers - Burramudgee",
                    "Burramudgee ParkingBay", 1)
    connect_regions(world, "Southern Rivers - Burramudgee", "SR - Min Min Plains",
                    "Min Min Plains ParkingBay", 1) #3689
    connect_regions(world, "Southern Rivers - Burramudgee", "SR - Outback Oasis",
                    "Outback Oasis ParkingBay", 1)  # 3685
    connect_regions(world, "SR - Outback Oasis", "Outback Oasis",
                    "Outback Oasis Connector")
    connect_regions(world, "Outback Oasis", "Outback Oasis - Infra",
                    "Outback Oasis -> Infra")
    connect_regions(world, "Southern Rivers - Burramudgee", "SR - Refinery Run",
                    "Refinery Run ParkingBay", 1)  # 3687
    connect_regions(world, "Southern Rivers - Burramudgee", "SR - Turbo Track",
                    "Turbo Track ParkingBay", 1)  # 3300
    connect_regions(world, "Southern Rivers - Burramudgee", "SR - Patchy",
                    "Patchy ParkingBay", 1)  # 3951
    connect_regions(world, "SR - Patchy", "Patchy",
                    "Patchy Connector")
    connect_regions(world, "Southern Rivers - Burramudgee", "SR - Lake Burramudgee",
                    "Lake Burramudgee ParkingBay", 1)  # 3686
    connect_regions(world, "SR - Lake Burramudgee", "Lake Burramudgee",
                    "Lake Burramudgee Connector")
    connect_regions(world, "Southern Rivers - Burramudgee", "SR - Dusty Barrows",
                    "Dusty Barrows ParkingBay")

    #Prawn
    connect_regions(world, "Southern Rivers - Prawn", "SR - Freeway Training Grounds",
                    "Freeway Training Grounds ParkingBay", 1) #3688
    connect_regions(world, "SR - Freeway Training Grounds", "Freeway Training Grounds",
                    "Freeway Training Grounds Connector")
    connect_regions(world, "Southern Rivers - Prawn", "SR - Dennis Freeway",
                    "Dennis Freeway ParkingBay", 1) #3692
    connect_regions(world, "SR - Dennis Freeway", "Dennis Freeway",
                    "Dennis Freeway Connector")
    connect_regions(world, "Southern Rivers - Prawn", "SR - Muddy Bottom",
                    "Muddy Bottom ParkingBay", 1) #3692
    connect_regions(world, "SR - Muddy Bottom", "Muddy Bottom",
                    "Muddy Bottom Connector")
    connect_regions(world, "Southern Rivers - Prawn", "SR - Ripper Nipper",
                    "Ripper Nipper ParkingBay", 1)
    connect_regions(world, "Southern Rivers - Prawn", "SR - Beach Training Grounds",
                    "Beach Training Grounds ParkingBay", 1)  # 4092
    connect_regions(world, "SR - Beach Training Grounds", "Beach Training Grounds",
                    "Beach Training Grounds Connector")
    connect_regions(world, "Southern Rivers - Prawn", "SR - Oil Rig",
                    "Oil Rig ParkingBay", 1)  # 3285
    connect_regions(world, "SR - Oil Rig", "Oil Rig",
                    "Oil Rig Connector")
    connect_regions(world, "Oil Rig", "Buster the Nanobot Boss",
                    "Oil Rig Button", 2)
    connect_regions(world, "Southern Rivers - Prawn", "SR - Wobbygon Bay",
                    "Wobbygon Bay ParkingBay", 1)  # 3287
    connect_regions(world, "SR - Wobbygon Bay", "Beach Sub",
                    "Wobbygon Bay Mission Sub Connector")
    connect_regions(world, "SR - Wobbygon Bay", "Deep Sea Scare",
                    "Deep Sea Scare Connector")
    connect_regions(world, "SR - MountBoom End", "Southern Rivers - Prawn",
                    "MountBoom End ParkingBay", 1)  # 3735
    connect_regions(world, "MountBoom End", "SR - MountBoom End",
                    "MountBoom End Connector")
    connect_regions(world, "Southern Rivers - Prawn", "SR - MountBoom Start",
                    "MountBoom Start ParkingBay", 1)  # 3694
    connect_regions(world, "SR - MountBoom Start", "MountBoom Start",
                    "MountBoom Start Connector")
    connect_regions(world, "MountBoom Start", "MountBoom",
                    "MountBoom Start Lava")
    connect_regions(world, "MountBoom", "MountBoom End",
                    "MountBoom End Lava")
    connect_regions(world, "MountBoom", "MountBoom -> Infra",
                    "MountBoom -> Infra")
    connect_regions(world, "Southern Rivers - Prawn", "SR - Frill Neck Forest",
                    "Frill Neck Forest ParkingBay", 1)  # 3693
    connect_regions(world, "SR - Frill Neck Forest", "Frill Neck Forest",
                    "Frill Neck Forest Load Zone")
    connect_regions(world, "Frill Neck Forest", "Frill Neck Forest - Infra",
                    "Frill Neck Forest -> Infra")
    connect_regions(world, "Southern Rivers - Prawn", "SR - Old Stony Creek",
                    "Old Stony Creek ParkingBay", 1)  # 3292
    connect_regions(world, "SR - Old Stony Creek", "Old Stony Creek",
                    "Old Stony Creek Connector")
    connect_regions(world, "Southern Rivers - Prawn", "SR - Camping",
                    "Camping ParkingBay", 1)  # 4130
    connect_regions(world, "Southern Rivers - Prawn", "SR - Hearty Beach",
                    "Hearty Beach ParkingBay")

    #Sly
    connect_regions(world, "Southern Rivers - Sly", "SR - Fire Fight",
                    "Fire Fight ParkingBay", 1)  # 3983
    connect_regions(world, "SR - Fire Fight", "Fire Fight",
                    "Fire Fight Connector")
    connect_regions(world, "Southern Rivers - Sly", "SR - Sly Shack",
                    "Sly ParkingBay", 1)  # 3244

    #Pie
    connect_regions(world, "Southern Rivers - Pie", "SR - Bush Fire",
                    "Bush Fire ParkingBay", 1)  # 3733
    connect_regions(world, "SR - Bush Fire", "Bush Fire",
                    "Bush Fire Connector")
    connect_regions(world, "Southern Rivers - Pie", "SR - Sulphur Rocks",
                    "Sulphur Rocks ParkingBay", 1)  # 3967
    connect_regions(world, "SR - Sulphur Rocks", "Sulphur Rocks",
                    "Sulphur Rocks Connector")
    connect_regions(world, "Sulphur Rocks", "Sulphur Rocks - Infra",
                    "Sulphur Rocks -> Infra")
    connect_regions(world, "Southern Rivers - Pie", "SR - King Squeaver",
                    "King Squeaver ParkingBay", 1)  # 3690 # King Squeaver and Birrel Hood
    connect_regions(world, "Southern Rivers - Pie", "SR - Faire Dinkum",
                    "Faire Dinkum ParkingBay", 1)  # 3277
    connect_regions(world, "SR - Faire Dinkum", "Faire Dinkum",
                    "Faire Dinkum Connector")
    connect_regions(world, "Faire Dinkum", "Faire Dinkum - Infra",
                    "Faire Dinkum -> Infra")
    connect_regions(world, "Southern Rivers - Pie", "SR - Wetlands",
                    "Wetlands ParkingBay", 1)
    connect_regions(world, "SR - Wetlands", "Wetlands",
                    "Wetlands Connector")
    connect_regions(world, "Wetlands", "Wetlands Tree",
                    "Wetlands Teleport", 2)
    connect_regions(world, "Wetlands", "Wetlands - Infra",
                    "Wetlands -> Infra")
    connect_regions(world, "Southern Rivers - Pie", "SR - Fluffy's Fortress",
                    "Fluffy ParkingBay")
    connect_regions(world, "SR - Fluffy's Fortress", "Fluffy's Fortress",
                    "Fluffy Connector")

    #Banana
    connect_regions(world, "Southern Rivers - Banana", "SR - Lava Falls Race",
                    "Lava Falls Race ParkingBay", 1)  # 3712
    connect_regions(world, "Southern Rivers - Banana", "SR - Plutonium Panic",
                    "Plutonium Panic ParkingBay", 1)  # 3284
    connect_regions(world, "Southern Rivers - Banana", "SR - 50 Foot Squeaver",
                    "50 Foot Squeaver ParkingBay", 1)  # 3709
    connect_regions(world, "Southern Rivers - Banana", "SR - Never Never",
                    "Never Never ParkingBay", 1)  # 3710
    connect_regions(world, "SR - Never Never", "Never Never",
                    "Never Never Connector")
    connect_regions(world, "Never Never", "Never Never - Infra",
                    "Never Never -> Infra")
    connect_regions(world, "Southern Rivers - Banana", "SR - Min Min Mining",
                    "Min Min Mining ParkingBay", 1)  # 4035
    connect_regions(world, "Southern Rivers - Banana", "SR - Truck Stop",
                    "Truck Stop ParkingBay North")

    #Pineapple
    connect_regions(world, "Southern Rivers - Pineapple", "SR - Outback Dash",
                    "Outback Dash ParkingBay", 1)  # 3714
    connect_regions(world, "Southern Rivers - Pineapple", "SR - Truck Tragedy",
                    "Truck Tragedy ParkingBay", 1)   # north 3708  #south 3732
    connect_regions(world, "Southern Rivers - Pineapple", "SR - Never Never Road",
                    "Never Never Road ParkingBay", 1)  # 3713
    connect_regions(world, "Southern Rivers - Pineapple", "SR - Truck Stop",
                    "Truck Stop ParkingBay South")






