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
    starting_items = []

    total_location_count = len(world.multiworld.get_unfilled_locations(world.player))
    print(total_location_count)
    #total_location_count -= add_mission_complete_events(world)
    print(total_location_count)
    for item_name, item_data in get_rangs(world).items():
        create_item(world, item_name, item_data.classification, item_data.amount)
    for item_name, item_data in item_dict.items():
        if world.options.start_with_maps.value and item_name in (
        "Missing Persons Map", "Shiny Thing Map", "Sekrit Map", "Priceless Art Map", "Forbidden Fruit Map"):
            continue
        create_item(world, item_name, item_data.classification, item_data.amount)
    for item_name, item_data in get_collectable_currencies(world).items():
        create_item(world, item_name, item_data.classification, item_data.amount)
    for item_name, item_data in get_bunyip_stones(world).items():
        if item_name in starting_items:
            continue
        create_item(world, item_name, item_data.classification, item_data.amount)
    if world.options.gate_unlock.value == 0:
        for item_name, item_data in gate.items():
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
            #if world.options.gate_unlock.value == 0:
                #if mission_name == "Heinous Hexaquin":
                    #item_name = "Hexaquin Defeated"
            #if world.options.gate_unlock.value == 1:
                #if mission_name == "Heinous Hexaquin":
                    #item_name = "Southern Rivers Gate"
            location = world.multiworld.get_location(mission_name, world.player)
            event_item = Ty3Item(item_name, ItemClassification.progression, None, world.player)
            location.place_locked_item(event_item)
            count+=1
        except KeyError:
            print(f"Location {mission_name} not found in multiworld, skipping.")
    return count

barriers: Dict[str, ItemData] = {
    "Sly": ItemData(980, ItemClassification.progression),
    "Duke": ItemData(981, ItemClassification.progression),
    "Hexaquin Arena Parking Bay": ItemData(982, ItemClassification.progression),
}

gate: Dict[str, ItemData] = {
    "Southern Rivers Gate": ItemData(983, ItemClassification.progression),
}

item_dict: Dict[str, ItemData] = {
    "Shadow Beam": ItemData(51, ItemClassification.progression),
    "Grav Grenade": ItemData(52, ItemClassification.progression),
    "Satellite Strike": ItemData(55, ItemClassification.progression),
    "Thermo Cannon": ItemData(56, ItemClassification.progression),
    "Nucleon Shield": ItemData(57, ItemClassification.useful),
    "Orbidrills": ItemData(59, ItemClassification.useful),
    "Missing Persons Map": ItemData(77, ItemClassification.useful),
    "Shiny Thing Map": ItemData(78, ItemClassification.useful),
    "Sekrit Map": ItemData(79, ItemClassification.useful),
    "Priceless Art Map": ItemData(80, ItemClassification.useful),
    "Forbidden Fruit Map": ItemData(81, ItemClassification.useful),
    "Bunyip Gauntlet": ItemData(82, ItemClassification.progression),
    "Shadow Stone 1": ItemData(83, ItemClassification.progression),
    "Shadow Stone 2": ItemData(84, ItemClassification.progression),
    "Shadow Stone 3": ItemData(85, ItemClassification.progression),
}

def get_rangs(world) -> Dict[str, ItemData]:
        return individual_rangs

individual_rangs: Dict[str, ItemData] = {
    "Mono Chassis": ItemData(0x13, ItemClassification.progression),
    "Duo Chassis": ItemData(0x01, ItemClassification.useful),
    "Lash Chassis": ItemData(0x02, ItemClassification.useful),
    "Smash Chassis": ItemData(0x03, ItemClassification.useful),
    "Mega Chassis": ItemData(0x04, ItemClassification.useful),
    "Ring Chassis": ItemData(0x05, ItemClassification.useful),
    "Shadow Chassis": ItemData(0x06, ItemClassification.progression),
    "Doom Chassis": ItemData(0x07, ItemClassification.useful),

}

def get_bunyip_stones(world) -> Dict[str, ItemData]:
    return bunyip_stones


bunyip_stones: Dict[str, ItemData] = {
    "Fire Stone": ItemData(3736, ItemClassification.progression),
    "Water Stone": ItemData(3689, ItemClassification.progression),
    "Air Stone": ItemData(3688, ItemClassification.progression),
    "Earth Stone": ItemData(4092, ItemClassification.progression,),
    "Chrono Stone": ItemData(3692, ItemClassification.useful),
    "Warp Stone": ItemData(3306, ItemClassification.progression),
    "Ultra Stone": ItemData(3285, ItemClassification.useful),
    "Mega Stone": ItemData(3287, ItemClassification.progression),
    "Multi Stone": ItemData(3712, ItemClassification.useful),
    "Zoom Stone": ItemData(3735, ItemClassification.progression),
    "Magnet Stone": ItemData(3694, ItemClassification.progression),
}


def get_collectable_currencies(world) -> Dict[str, ItemData]:
    collectibles_copy: Dict[str, ItemData] = copy.deepcopy(collectibles)
    collectibles_copy["Gooboo Berry"].amount += world.options.extra_berries.value
    collectibles_copy["Kromium Orb"].amount += world.options.extra_orbs.value
    collectibles_copy["Bilby"].amount += world.options.extra_bilbies.value
    return collectibles_copy


collectibles: Dict[str, ItemData] = {
    "Gooboo Steve": ItemData(0x20, ItemClassification.progression_skip_balancing, 6),
    "Kromium Orb": ItemData(0x21, ItemClassification.progression_skip_balancing, 30),
    "Gooboo Berry": ItemData(0x22, ItemClassification.progression_skip_balancing, 9),
    "Bilby": ItemData(0x23, ItemClassification.progression_skip_balancing, 40)
}

def get_filler(world) -> Dict[str, ItemData]:
    return junk_items

junk_items: Dict[str, ItemData] = {
    "Opal": ItemData(0x24, ItemClassification.filler),
    "50 Opals": ItemData(0x25, ItemClassification.filler),
    "100 Opals": ItemData(0x26, ItemClassification.filler),
    "200 Opals": ItemData(0x27, ItemClassification.filler),
    "500 Opals": ItemData(0x28, ItemClassification.filler),
    "Pie Slice": ItemData(0x29, ItemClassification.filler),
    "Full Heal": ItemData(0x2A, ItemClassification.filler),
}

junk_weights = {
    "Opal": 0,
    "50 Opals": 15,
    "100 Opals": 20,
    "200 Opals": 20,
    "500 Opals": 5,
    "Pie Slice": 10,
    "Full Heal": 15,
}

full_item_dict: Dict[str, ItemData] = {**item_dict, **individual_rangs,
                                       **bunyip_stones, **barriers,
                                       **collectibles, **junk_items,
                                       **gate}