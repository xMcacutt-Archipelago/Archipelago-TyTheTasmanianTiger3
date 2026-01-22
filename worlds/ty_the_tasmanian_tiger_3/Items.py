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
    extra_amount: Optional[int] = 0
    currency_type: Optional[str] = ""

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
    total_location_count -= add_mission_complete_events(world)
    for item_name, item_data in individual_rangs.items():
        create_item(world, item_name, item_data.classification, item_data.amount)
    for item_name, item_data in item_dict.items():
        if world.options.start_with_maps.value and item_name in (
        "Missing Persons Map", "Shiny Thing Map", "Sekrit Map", "Priceless Art Map", "Forbidden Fruit Map"):
            continue
        create_item(world, item_name, item_data.classification, item_data.amount)
    for item_name, item_data in collectibles.items():
        create_item(world, item_name, item_data.classification, item_data.amount)
        create_item(world, item_name, ItemClassification.useful, item_data.extra_amount)
    for item_name, item_data in bunyip_stones.items():
        if item_name in starting_items:
            continue
        create_item(world, item_name, item_data.classification, item_data.amount)
    for item_name, item_data in barriers.items():
        create_item(world, item_name, item_data.classification)
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
            item_name = f"{loc_data.mission_type} Mission Complete"
            location = world.multiworld.get_location(mission_name, world.player)
            event_item = Ty3Item(item_name, ItemClassification.progression, None, world.player)
            location.place_locked_item(event_item)
            count+=1
        except KeyError:
            print(f"Location {mission_name} not found in multiworld, skipping.")
    return count

barriers: Dict[str, ItemData] = {
    "Sly": ItemData(0x981, ItemClassification.progression),
    "Duke": ItemData(0x982, ItemClassification.progression),
    "Karlos": ItemData(0x983, ItemClassification.progression),
    "Crabmersible": ItemData(0x984, ItemClassification.progression),
    "Southern Rivers Gate": ItemData(0x985, ItemClassification.progression),
    "Level - Cinder Canyon":    ItemData(0x946, ItemClassification.progression),
    "Level - Dead Dingo Marsh": ItemData(0x947, ItemClassification.progression),
    "Level - Gooboo Gully":     ItemData(0x948, ItemClassification.progression),
    "Level - Kaka Boom Island": ItemData(0x949, ItemClassification.progression),
    "Level - Mount Boom Basin": ItemData(0x94A, ItemClassification.progression),
}

item_dict: Dict[str, ItemData] = {
    "Shadow Beam": ItemData(0x51, ItemClassification.progression),
    "Grav Grenade": ItemData(0x52, ItemClassification.progression),
    "Satellite Strike": ItemData(0x53, ItemClassification.progression),
    "Thermo Cannon": ItemData(0x54, ItemClassification.progression),
    "Nucleon Shield": ItemData(0x55, ItemClassification.useful),
    "Orbidrills": ItemData(0x56, ItemClassification.useful),
    "Missing Persons Map": ItemData(0x57, ItemClassification.useful),
    "Shiny Thing Map": ItemData(0x58, ItemClassification.useful),
    "Sekrit Map": ItemData(0x59, ItemClassification.useful),
    "Priceless Art Map": ItemData(0x5a, ItemClassification.useful),
    "Forbidden Fruit Map": ItemData(0x5b, ItemClassification.useful),
    "Bunyip Gauntlet": ItemData(0x5c, ItemClassification.progression),
    "Shadow Stone 1": ItemData(0x5d, ItemClassification.progression),
    "Shadow Stone 2": ItemData(0x5e, ItemClassification.progression),
    "Shadow Stone 3": ItemData(0x5f, ItemClassification.progression),
}

individual_rangs: Dict[str, ItemData] = {
    "Duo Chassis": ItemData(0x02, ItemClassification.progression),
    "Lash Chassis": ItemData(0x03, ItemClassification.progression),
    "Smash Chassis": ItemData(0x04, ItemClassification.progression),
    "Mega Chassis": ItemData(0x05, ItemClassification.progression),
    "Ring Chassis": ItemData(0x06, ItemClassification.progression),
    "Shadow Chassis": ItemData(0x07, ItemClassification.progression),
    "Doom Chassis": ItemData(0x08, ItemClassification.progression),
}

bunyip_stones: Dict[str, ItemData] = {
    "Fire Stone": ItemData(4601, ItemClassification.progression, 3),
    "Water Stone": ItemData(4602, ItemClassification.progression, 3),
    "Air Stone": ItemData(4603, ItemClassification.progression, 3),
    "Earth Stone": ItemData(4604, ItemClassification.progression, 3),
    "Chrono Stone": ItemData(4605, ItemClassification.useful, 6),
    "Warp Stone": ItemData(4606, ItemClassification.progression, 3),
    "Ultra Stone": ItemData(4607, ItemClassification.progression, 3),
    "Mega Stone": ItemData(4608, ItemClassification.progression, 3),
    "Multi Stone": ItemData(4609, ItemClassification.useful, 5),
    "Zoom Stone": ItemData(4610, ItemClassification.progression, 3),
    "Magnet Stone": ItemData(4611, ItemClassification.progression, 3),
}

collectibles: Dict[str, ItemData] = {
    "Kromium Orb": ItemData(0x20, ItemClassification.progression_skip_balancing, 24, 6, currency_type="KOrb"),
    "Gooboo Berry": ItemData(0x21, ItemClassification.progression_skip_balancing, 8, 2, currency_type="Berry"),
    "Bilby": ItemData(0x22, ItemClassification.progression_skip_balancing, 35, 5, currency_type="Bilby")
}

junk_items: Dict[str, ItemData] = {
    "50 Opals": ItemData(0x25, ItemClassification.skip_balancing, currency_type="Opal"),
    "100 Opals": ItemData(0x26, ItemClassification.skip_balancing, currency_type="Opal"),
    "250 Opals": ItemData(0x27, ItemClassification.skip_balancing, currency_type="Opal"),
    "500 Opals": ItemData(0x28, ItemClassification.skip_balancing, currency_type="Opal"),
    "1000 Opals": ItemData(0x29, ItemClassification.skip_balancing, currency_type="Opal"),
    "Full Heal": ItemData(0x2A, ItemClassification.skip_balancing),
}

junk_weights = {
    "50 Opals": 15,
    "100 Opals": 20,
    "250 Opals": 20,
    "500 Opals": 10,
    "1000 Opals": 5,
    "Full Heal": 20,
}

full_item_dict: Dict[str, ItemData] = {
    **item_dict,
    **individual_rangs,
    **bunyip_stones,
    **barriers,
    **collectibles,
    **junk_items,
}