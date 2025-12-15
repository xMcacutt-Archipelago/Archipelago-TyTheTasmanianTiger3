from typing import Dict

from BaseClasses import Region, Location, Entrance

ty3_levels: Dict[str, str] = {
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
}


def create_location(world, region, name: str, code: int):
    location = Location(world.player, name, code, region)
    region.locations.append(location)


def create_locations(world, region, loc_dict):
    for (key, data) in loc_dict.items():
        if data.region != region.name:
            continue
        create_location(world, region, key, data.code)


def create_region(world, name: str, loc_dict):
    region = Region(name, world.player, world.multiworld)
    create_locations(world, region, loc_dict)
    world.multiworld.regions.append(region)
    return region

def create_ty3_regions(world, location_dict):
    create_region(world, "Menu", location_dict)
    create_region(world, "The Dreaming", location_dict)
    create_region(world, "New Burramudgee - Prologue", location_dict)
    create_region(world, "New Burramudgee", location_dict)
    create_region(world, "Cassopolis", location_dict)
    create_region(world, "Cinder Canyon", location_dict)
    create_region(world, "Dead Dingo Marsh", location_dict)
    create_region(world, "Kaka Boom Island", location_dict)
    create_region(world, "Gooboo Gully", location_dict)
    create_region(world, "Mount Boom Basin", location_dict)
    create_region(world, "SR Desert", location_dict)
    create_region(world, "SR Swamp", location_dict)
    create_region(world, "Razorback Stream", location_dict)
    create_region(world, "Pippy Beach", location_dict)
    create_region(world, "Winter Woods", location_dict)
    create_region(world, "Frozen Forest", location_dict)
    create_region(world, "Backwood Blizzard", location_dict)
    create_region(world, "Quinking", location_dict)
    create_region(world, "SR Desert - Duke", location_dict)
    create_region(world, "SR Desert - Sly", location_dict)
    create_region(world, "SR Swamp - Duke", location_dict)
    create_region(world, "SR Swamp - Sly", location_dict)


def connect_regions(world, from_name: str, to_name: str, entrance_name: str, entrance_group = 0, two_way = False) -> Entrance:
    entrance_region = world.get_region(from_name)
    exit_region = world.get_region(to_name)
    entrance = entrance_region.connect(exit_region, entrance_name)
    return entrance


def connect_ty3_regions(world):
    connect_regions(world, "Menu", "The Dreaming",
                    "Start")
    connect_regions(world, "The Dreaming", "New Burramudgee - Prologue",
                    "Time Warp")
    connect_regions(world, "New Burramudgee - Prologue", "New Burramudgee",
                    "Save the General")
    connect_regions(world, "New Burramudgee", "Cassopolis",
                    "Portal")
    connect_regions(world, "New Burramudgee", "Razorback Stream",
                    "Elevator")
    connect_regions(world, "Razorback Stream", "SR Desert",
                    "Razorback Stream Crab")
    connect_regions(world, "Razorback Stream", "Cinder Canyon",
                    "Cinder Canyon Cave")
    connect_regions(world, "SR Desert", "SR Desert - Duke",
                    "Desert Duke Airship")
    connect_regions(world, "SR Desert", "SR Desert - Sly",
                    "Desert Sly Airship")
    connect_regions(world, "SR Desert - Sly", "Frozen Forest",
                    "Sly Airship - FF")
    connect_regions(world, "SR Desert - Sly", "Backwood Blizzard",
                    "Sly Airship - BB")
    connect_regions(world, "SR Desert - Duke", "Mount Boom Basin",
                    "Duke Airship - MBB")
    connect_regions(world, "SR Desert", "SR Swamp",
                    "SR Gate")
    connect_regions(world, "SR Swamp", "Dead Dingo Marsh",
                    "Dead Dingo Marsh Tunnel")
    connect_regions(world, "SR Swamp", "Cassopolis",
                    "Cassopolis Sewers")
    connect_regions(world, "SR Swamp", "Gooboo Gully",
                    "Gooboo Gully Tunnel")
    connect_regions(world, "SR Swamp", "SR Swamp - Duke",
                    "Swamp Duke Airship")
    connect_regions(world, "SR Swamp", "SR Swamp - Sly",
                    "Swamp Sly Airship")
    connect_regions(world, "SR Swamp - Sly", "Winter Woods",
                    "Sly Airship - WW")
    connect_regions(world, "SR Swamp", "Pippy Beach",
                    "Pippy Beach Parking Bay")
    connect_regions(world, "Pippy Beach", "SR Swamp - Duke",
                    "Pippy Beach Duke Airship")
    connect_regions(world, "SR Swamp - Duke", "Kaka Boom Island",
                    "Duke Airship - KBI")
    connect_regions(world, "SR Swamp", "Quinking",
                    "Airship - Quinking")