import copy
from dataclasses import dataclass
from typing import Dict

from BaseClasses import ItemClassification, Item
from typing import Optional

from worlds.ty_the_tasmanian_tiger_3.Locations import get_mission_complete_events


class Ty3Item(Item):
    game: str = "Ty the Tasmanian Tiger 3"


@dataclass
class ItemData:
    code: int
    classification: ItemClassification
    amount: Optional[int] = 1

def get_junk_item_names(rand, k: int) -> str:
    junk = rand.choices(
        list(junk_weights.keys()),
        weights=list(junk_weights.values()),
        k=k)
    return junk

def create_item(world, name: str, classification: ItemClassification, amount: Optional[int] = 1):
    for i in range(amount):
        world.itempool.append(Item(name, classification, world.item_name_to_id[name], world.player))


def create_ty3_items(world):
    starting_items = ["Burramudgee Town ParkingBay"]

    total_location_count = len(world.multiworld.get_unfilled_locations(world.player))
    print(total_location_count)
    total_location_count -= add_mission_complete_events(world)
    print(total_location_count)
    for item_name, item_data in get_rangs(world).items():
        create_item(world, item_name, item_data.classification, item_data.amount)
    for item_name, item_data in item_dict.items():
        if world.options.start_with_maps.value and item_name in (
        "Missing Persons Map", "Cog Map", "Mysterious Anomalies Map"):
            continue
        create_item(world, item_name, item_data.classification, item_data.amount)
    for item_name, item_data in get_collectable_currencies(world).items():
        create_item(world, item_name, item_data.classification, item_data.amount)
    for item_name, item_data in get_parking_pads(world).items():
        if item_name in starting_items:
            continue
        create_item(world, item_name, item_data.classification, item_data.amount)
    if world.options.gate_unlock.value == 1:
        for item_name, item_data in barriers.items():
            create_item(world, item_name, item_data.classification, item_data.amount)

    #print(len(world.itempool))

    remaining_locations: int = total_location_count - len(world.itempool)
    # trap_count: int = round(remaining_locations * options.trap_fill_percentage / 100)
    junk_count: int = remaining_locations - 1 #trap_count
    junk = get_junk_item_names(world.random, junk_count)
    for name in junk:
        create_item(world, name, ItemClassification.filler)
    # traps = get_trap_item_names(world.worlds[player], world.random, trap_count)
    # for name in traps:
    #     create_single(name, world, player)
    world.multiworld.itempool += world.itempool

def add_mission_complete_events(world):
    complete_mission_dict = get_mission_complete_events(world)
    count = 0
    for mission_name, loc_data in complete_mission_dict.items():
        # Assuming your locations are named exactly as the mission_name
        try:
            item_name = "Mission Complete"
            if world.options.gate_unlock.value == 0:
                if mission_name == "Heinous Hexaquin":
                    item_name = "Hexaquin Defeated"
            if world.options.gate_unlock.value == 1:
                if mission_name == "Heinous Hexaquin":
                    item_name = "Southern Rivers Gate"
            location = world.multiworld.get_location(mission_name, world.player)
            event_item = Ty3Item(item_name, ItemClassification.progression, None, world.player)
            location.place_locked_item(event_item)
            count+=1
        except KeyError:
            print(f"Location {mission_name} not found in multiworld, skipping.")
    return count

barriers: Dict[str, ItemData] = {
    "Patchy Barriers": ItemData(980, ItemClassification.progression),
    "Buster Barriers": ItemData(982, ItemClassification.progression),
    "Fluffy Barriers": ItemData(981, ItemClassification.progression),
}

item_dict: Dict[str, ItemData] = {
    "Lifter Bunyip Key": ItemData(51, ItemClassification.progression),
    "Thermo Bunyip Key": ItemData(52, ItemClassification.progression),
    "Missing Persons Map": ItemData(55, ItemClassification.useful),
    "Cog Map": ItemData(56, ItemClassification.useful),
    "Mysterious Anomalies Map": ItemData(57, ItemClassification.useful),
    "Sub Bunyip Key": ItemData(59, ItemClassification.progression),
    "Gold Paw": ItemData(77, ItemClassification.useful),
    "Platinum Paw": ItemData(78, ItemClassification.useful),
    # "fourbie speed upgrade": ItemData(0x00, ItemClassification.useful),
}

def get_rangs(world) -> Dict[str, ItemData]:
    if world.options.progressive_rangs.value:
        return progressive_rangs
    else:
        print("individual rangs")
        return individual_rangs

individual_rangs: Dict[str, ItemData] = {
    "Boomerang": ItemData(0x13, ItemClassification.useful),
    "Multirang": ItemData(0x01, ItemClassification.useful),
    "Flamerang": ItemData(0x02, ItemClassification.progression),
    "Lavarang": ItemData(0x03, ItemClassification.progression),
    "Frostyrang": ItemData(0x04, ItemClassification.progression),
    "Freezerang": ItemData(0x05, ItemClassification.progression),
    "Zappyrang": ItemData(0x06, ItemClassification.useful),
    "Thunderang": ItemData(0x07, ItemClassification.useful),
    "Lasharang": ItemData(0x08, ItemClassification.progression),
    "Warperang": ItemData(0x09, ItemClassification.progression),
    "Infrarang": ItemData(0x0a, ItemClassification.progression),
    "X-Rang": ItemData(0x0b, ItemClassification.progression),
    "Smasharang": ItemData(0x0c, ItemClassification.progression),
    "Kaboomarang": ItemData(0x0d, ItemClassification.progression),
    "Megarang": ItemData(0xe, ItemClassification.useful),
    "Omegarang": ItemData(0x0f, ItemClassification.useful),
    "Deadlyrang": ItemData(0x10, ItemClassification.progression),
    "Doomerang": ItemData(0x11, ItemClassification.progression),
    # "Aquarang": ItemData(0x12, ItemClassification.progression),
    # "?": ItemData(0x13, ItemClassification.progression),
    "Craftyrang": ItemData(0x14, ItemClassification.progression),
    "Camerarang": ItemData(0x15, ItemClassification.useful),

}

progressive_rangs: Dict[str, ItemData] = {
    "Progressive Boomerang": ItemData(0x16, ItemClassification.useful, 3), #Boomerang - Multirang - Megarang - Omegarang
    "Progressive Flamerang": ItemData(0x17, ItemClassification.progression, 2),
    "Progressive Frostyrang": ItemData(0x18, ItemClassification.progression, 2),
    "Progressive Zappyrang": ItemData(0x19, ItemClassification.useful, 2),
    "Progressive Lasharang": ItemData(0x1a, ItemClassification.progression, 2),
    "Progressive Infrarang": ItemData(0x1b, ItemClassification.progression, 2),
    "Progressive Smasharang": ItemData(0x1c, ItemClassification.progression, 5), #Craftyrang - Smasharang - Kaboomarang - Deadlyrang - Doomerang
    "Camerarang": ItemData(0x15, ItemClassification.useful),

}

def get_parking_pads(world) -> Dict[str, ItemData]:
    # if world.options.progressive_parking_pads.value:
    #     return progressive_parking_pads
    # else:
    return parking_bays



parking_bays: Dict[str, ItemData] = {
    "Burramudgee Town ParkingBay": ItemData(3736, ItemClassification.progression),#patchy
    "Min Min Plains ParkingBay": ItemData(3689, ItemClassification.progression), #patchy
    "Freeway Training Grounds ParkingBay": ItemData(3688, ItemClassification.progression), #Buster
    "Beach Training Grounds ParkingBay": ItemData(4092, ItemClassification.progression), #Buster
    "Dennis Freeway ParkingBay": ItemData(3692, ItemClassification.progression), #Buster
    "Muddy Bottom ParkingBay": ItemData(3306, ItemClassification.progression), #Buster
    "Oil Rig ParkingBay": ItemData(3285, ItemClassification.progression), #Buster
    "Wobbygon Bay ParkingBay": ItemData(3287, ItemClassification.progression), #Buster
    "Hearty Beach ParkingBay": ItemData(3712, ItemClassification.progression), #Buster
    "MountBoom End ParkingBay": ItemData(3735, ItemClassification.progression),#Buster
    "MountBoom Start ParkingBay": ItemData(3694, ItemClassification.progression),#Buster
    "Frill Neck Forest ParkingBay": ItemData(3693, ItemClassification.progression), #Buster
    "Old Stony Creek ParkingBay": ItemData(3292, ItemClassification.progression), ##Buster
    "Camping ParkingBay": ItemData(4130, ItemClassification.progression), #Buster
    "Outback Oasis ParkingBay": ItemData(3685, ItemClassification.progression),#patchy
    "Refinery Run ParkingBay": ItemData(3687, ItemClassification.progression), #patchy
    "Fire Fight ParkingBay": ItemData(3983, ItemClassification.progression), #Buster
    "Sly ParkingBay": ItemData(3244, ItemClassification.progression), #Buster
    "Outback Dash ParkingBay": ItemData(3714, ItemClassification.progression), #Cass
    "Truck Tragedy ParkingBay": ItemData(3702, ItemClassification.progression), #Cass
    "Truck Stop ParkingBay": ItemData(3732, ItemClassification.progression), #Cass
    "Never Never Road ParkingBay": ItemData(3713, ItemClassification.progression), #Cass
    "Plutonium Panic ParkingBay": ItemData(3284, ItemClassification.progression), #Cass
    "50 Foot Squeaver ParkingBay": ItemData(3709, ItemClassification.progression), #Cass
    "Never Never ParkingBay": ItemData(3710, ItemClassification.progression), #Cass
    "Lava Falls Race ParkingBay": ItemData(3711, ItemClassification.progression), #Cass
    "Min Min Mining ParkingBay": ItemData(4035, ItemClassification.progression), #Cass
    "Turbo Track ParkingBay": ItemData(3300, ItemClassification.progression), #patchy
    "Patchy ParkingBay": ItemData(3951, ItemClassification.progression), #patchy
    "Lake Burramudgee ParkingBay": ItemData(3686, ItemClassification.progression), #patchy
    "Bush Fire ParkingBay": ItemData(3733, ItemClassification.progression), #fluffy
    "Sulphur Rocks ParkingBay": ItemData(3967, ItemClassification.progression), #fluffy
    "King Squeaver ParkingBay": ItemData(3690, ItemClassification.progression), #fluffy
    "Fluffy ParkingBay": ItemData(3691, ItemClassification.progression), #fluffy
    "Faire Dinkum ParkingBay": ItemData(3954, ItemClassification.progression), #fluffy
    "Wetlands ParkingBay": ItemData(3277, ItemClassification.progression), #fluffy


    "Dusty Barrows ParkingBay": ItemData(4046, ItemClassification.progression), #patchy
    "Ripper Nipper ParkingBay": ItemData(3972, ItemClassification.progression), ##Buster NEED TO ADD (lotion mission)
}

progressive_parking_bays: Dict[str, ItemData] = {
    "Progressive Parking Bay": ItemData(0x1f, ItemClassification.progression, 100),
}

def get_collectable_currencies(world) -> Dict[str, ItemData]:
    collectibles_copy: Dict[str, ItemData] = copy.deepcopy(collectibles)
    collectibles_copy["Platinum Cog"].amount += world.options.extra_cogs.value
    collectibles_copy["Kromium Orb"].amount += world.options.extra_orbs.value
    return collectibles_copy


collectibles: Dict[str, ItemData] = {
    "Platinum Cog": ItemData(0x20, ItemClassification.progression_skip_balancing, 50),
    "Kromium Orb": ItemData(0x21, ItemClassification.progression_skip_balancing, 30),
}

def get_filler(world) -> Dict[str, ItemData]:
    return junk_items

junk_items: Dict[str, ItemData] = {
    "Opal": ItemData(0x22, ItemClassification.filler),
    "50 Opals": ItemData(0x23, ItemClassification.filler),
    "100 Opals": ItemData(0x24, ItemClassification.filler),
    "200 Opals": ItemData(0x25, ItemClassification.filler),
    "500 Opals": ItemData(0x26, ItemClassification.filler),
    "Pie Slice": ItemData(0x27, ItemClassification.filler),
    "Full Heal": ItemData(0x28, ItemClassification.filler),
}

junk_weights = {
    "Opal": 5,
    "50 Opals": 30,
    "100 Opals": 20,
    "200 Opals": 15,
    "500 Opals": 5,
    "Pie Slice": 10,
    "Full Heal": 15,
}

full_item_dict: Dict[str, ItemData] = {**item_dict, **individual_rangs, **progressive_rangs, **parking_bays, **barriers, **progressive_parking_bays, **collectibles, **junk_items}