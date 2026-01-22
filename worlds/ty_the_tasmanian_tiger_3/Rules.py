from BaseClasses import ItemClassification, CollectionState, Location
from worlds.ty_the_tasmanian_tiger_3.Items import Ty3Item, full_item_dict
from worlds.ty_the_tasmanian_tiger_3.Locations import *
from worlds.generic.Rules import forbid_item

def has_infra(world, state):
    return state.has("Ultra Stone", world.player)

def has_chassis(world, state, flags):
    if flags & 0b00000010:
        if state.has("Duo Chassis", world.player):
            return True
    if flags & 0b00000100:
        if state.has("Lash Chassis", world.player):
            return True
    if flags & 0b00001000:
        if state.has("Mega Chassis", world.player):
            return True
    if flags & 0b00010000:
        if state.has("Smash Chassis", world.player):
            return True
    if flags & 0b00100000:
        if state.has("Ring Chassis", world.player):
            return True
    if flags & 0b01000000:
        if state.has("Shadow Chassis", world.player):
            return True
    if flags & 0b10000000:
        if state.has("Doom Chassis", world.player):
            return True
    return True

def can_magnet(world, state):
    return state.has("Magnet Stone", world.player, 3) and has_chassis(world, state, 0b10111000)

def can_bunyip(world, state):
    return state.has("Sly", world.player)

def can_gunyip(world, state):
    return state.has("Duke", world.player)

def can_smash(world, state):
    return (state.has("Earth Stone", world.player)
            or state.has("Doom Chassis", world.player))

def can_burn(world, state):
    return state.has("Fire Stone", world.player)

def can_freeze(world, state):
    return state.has("Water Stone", world.player)

def can_zap(world, state):
    return state.has("Air Stone", world.player)

def can_swing(world, state):
    return state.has("Lash Chassis", world.player)

def can_tp(world, state):
    return state.has("Warp Stone", world.player)

def get_rules(world):
    rules = {
        "locations": {
            # Shops
            "Naomi's Ice Cream Truck Berry Blast 1": lambda state:
                state.has("Gooboo Berry", world.player, 2),
            "Naomi's Ice Cream Truck Berry Blast 2": lambda state:
                state.has("Gooboo Berry", world.player, 4),
            "Naomi's Ice Cream Truck Berry Blast 3": lambda state:
                state.has("Gooboo Berry", world.player, 6),
            "Naomi's Ice Cream Truck Berry Blast 4": lambda state:
                state.has("Gooboo Berry", world.player, 8),

            "Naomi's Ice Cream Truck Bilby Banana Split 1": lambda state:
                state.has("Bilby", world.player, 7),
            "Naomi's Ice Cream Truck Bilby Banana Split 2": lambda state:
                state.has("Bilby", world.player, 14),
            "Naomi's Ice Cream Truck Bilby Banana Split 3": lambda state:
                state.has("Bilby", world.player, 21),
            "Naomi's Ice Cream Truck Bilby Banana Split 4": lambda state:
                state.has("Bilby", world.player, 28),
            "Naomi's Ice Cream Truck Bilby Banana Split 5": lambda state:
                state.has("Bilby", world.player, 35),

            "Rang Shop Korb 1": lambda state:
                state.has("Kromium Orb", world.player, 3),
            "Rang Shop Korb 2": lambda state:
                state.has("Kromium Orb", world.player, 6),
            "Rang Shop Korb 3": lambda state:
                state.has("Kromium Orb", world.player, 9),
            "Rang Shop Korb 4": lambda state:
                state.has("Kromium Orb", world.player, 12),
            "Rang Shop Korb 5": lambda state:
                state.has("Kromium Orb", world.player, 15),
            "Rang Shop Korb 6": lambda state:
                state.has("Kromium Orb", world.player, 18),
            "Rang Shop Korb 7": lambda state:
                state.has("Kromium Orb", world.player, 21),
            "Rang Shop Korb 8": lambda state:
                state.has("Kromium Orb", world.player, 24),

            #Missions
            "Egg Hunt": lambda state:
                state.has("Satellite Strike", world.player),
            "Complete Egg Hunt": lambda state:
                state.can_reach_location("Egg Hunt", world.player),
            "Power Struggle": lambda state:
                state.has("Grav Grenade", world.player) and state.has("Shadow Beam", world.player),
            "Complete Power Struggle": lambda state:
                state.can_reach_location("Power Struggle", world.player),
            "Meltdown": lambda state:
                state.has("Thermo Cannon", world.player),
            "Complete Meltdown": lambda state:
                state.can_reach_location("Meltdown", world.player),
            "Ranger Endanger": lambda state:
                state.has("Shadow Beam", world.player),
            "Complete Ranger Endanger": lambda state:
                state.can_reach_location("Ranger Endanger", world.player),
            "Redback Rundown": lambda state:
                state.has("Thermo Cannon", world.player),
            "Complete Redback Rundown": lambda state:
                state.can_reach_location("Redback Rundown", world.player),
            "All Your Base": lambda state:
                can_gunyip(world, state),
            "Complete All Your Base": lambda state:
                state.can_reach_location("All Your Base", world.player),
            "Aero Coast Guard": lambda state:
                can_gunyip(world, state),
            "Complete Aero Coast Guard": lambda state:
                state.can_reach_location("Aero Coast Guard", world.player),
            "Wrath of the Dragonquin": lambda state:
                can_gunyip(world, state),
            "Complete Wrath of the Dragonquin": lambda state:
                state.can_reach_location("Wrath of the Dragonquin", world.player),
            "Forest Firepower": lambda state:
                can_gunyip(world, state),
            "Complete Forest Firepower": lambda state:
                state.can_reach_location("Forest Firepower", world.player),
            "Rescue Julius": lambda state:
                state.has("Karlos", world.player),
            "Complete Rescue Julius": lambda state:
                state.can_reach_location("Rescue Julius", world.player),
            "Battle Arena Gamma": lambda state:
                state.has("Karlos", world.player),
            "Complete Battle Arena Gamma": lambda state:
                state.can_reach_location("Battle Arena Gamma", world.player),
            "Battle Arena Zeta": lambda state:
                state.has("Karlos", world.player),
            "Complete Battle Arena Zeta": lambda state:
                state.can_reach_location("Battle Arena Zeta", world.player),
            "Quinking": lambda state:
                state.has("Bunyip Gauntlet", world.player)
                and state.has("Shadow Chassis", world.player)
                and state.has("Shadow Stone 1", world.player)
                and state.has("Shadow Stone 2", world.player)
                and state.has("Shadow Stone 3", world.player),

            #Orbs
            "Kromium Orb 1": lambda state:
                has_infra(world, state),
            "Kromium Orb 2": lambda state:
                has_infra(world, state),
            "Kromium Orb 3": lambda state:
                can_smash(world, state),
            "Kromium Orb 4": lambda state:
                can_burn(world, state),
            "Kromium Orb 6": lambda state:
                can_swing(world, state) and can_smash(world, state) and
                (state.has("Zoom Stone", world.player) or state.has("Mega Stone", world.player)),
            "Kromium Orb 7": lambda state:
                has_infra(world, state),
            "Kromium Orb 8": lambda state:
                can_smash(world, state),
            "Kromium Orb 10": lambda state:
                has_infra(world, state),
            "Kromium Orb 14": lambda state:
                can_smash(world, state),
            "Kromium Orb 18": lambda state:
                can_freeze(world, state),
            "Kromium Orb 20": lambda state:
                can_gunyip(world, state),
            "Kromium Orb 22": lambda state:
                has_infra(world, state),
            "Kromium Orb 23": lambda state:
                has_infra(world, state),
            "Kromium Orb 25": lambda state:
                can_swing(world, state),
            "Kromium Orb 26": lambda state:
                has_infra(world, state),
            "Kromium Orb 27": lambda state:
                has_infra(world, state),

            #Bilbies
            "Bilby 2": lambda state:
                can_zap(world,state),
            "Bilby 3": lambda state:
                can_burn(world, state),
            "Bilby 4": lambda state:
                can_tp(world, state),
            "Bilby 6": lambda state:
                state.has("Grav Grenade", world.player) or state.has("Satellite Strike", world.player),
            "Bilby 7": lambda state:
            state.has("Grav Grenade", world.player) or state.has("Satellite Strike", world.player),
            "Bilby 9": lambda state:
                can_swing(world, state),
            "Bilby 12": lambda state:
                state.has("Grav Grenade", world.player),
            "Bilby 13": lambda state:
                state.has("Water Stone", world.player),
            "Bilby 19": lambda state:
                state.has("Grav Grenade", world.player),
            "Bilby 22": lambda state:
                can_smash(world, state),
            "Bilby 24": lambda state:
                can_smash(world, state),
            "Bilby 27": lambda state:
                state.has("Level - Kaka Boom Island", world.player),
            "Bilby 36": lambda state:
                can_tp(world, state), #jump is possible without warp

            #Stones
            "Stone 1": lambda state:
                state.has("Karlos", world.player),
            "Stone 2": lambda state:
                state.has("Karlos", world.player),
            "Stone 3": lambda state:
                has_infra(world, state) and can_swing(world, state),
            "Stone 6": lambda state:
                can_magnet(world, state),
            "Stone 8": lambda state:
                can_magnet(world, state),
            "Stone 9": lambda state:
                state.has("Karlos", world.player),
            "Stone 10": lambda state:
                state.has("Karlos", world.player),
            "Stone 14": lambda state:
                state.has("Karlos", world.player),
            "Stone 15": lambda state:
                state.has("Karlos", world.player),
            "Stone 16": lambda state:
                state.has("Grav Grenade", world.player),
            "Stone 28": lambda state:
                can_smash(world, state),
            "Stone 29": lambda state:
                can_magnet(world, state),
            "Stone 31": lambda state:
                can_burn(world, state),
            "Stone 39": lambda state:
                can_magnet(world, state),
            "Stone 42": lambda state:
                has_infra(world, state) and can_burn(world, state),
            "Stone 49": lambda state:
                can_swing(world, state),
            "Stone 50": lambda state:
                has_infra(world, state),
            "Stone 55": lambda state:
                has_infra(world, state),
            "Stone 56": lambda state:
                can_burn(world, state) and can_zap(world, state),

            #Steves
            "Steve - Razorback Stream": lambda state:
                can_burn(world, state),
            "Steve - Kaka Boom Island": lambda state:
                can_smash(world, state),

            #Berries
            "Gooboo Berry 1": lambda state:
                can_smash(world, state),
            "Gooboo Berry 3": lambda state:
                can_swing(world, state),
            "Gooboo Berry 4": lambda state:
                can_swing(world, state) and can_burn(world, state),
            "Gooboo Berry 6": lambda state:
                can_smash(world, state),

            #Frames
            "Picture Frame 1": lambda state:
                has_infra(world, state),
            "Picture Frame 2": lambda state:
                has_infra(world, state) and can_smash(world, state),
            "Picture Frame 3": lambda state:
                has_infra(world, state) and can_smash(world, state),
            "Picture Frame 4": lambda state:
                has_infra(world, state) and can_smash(world, state),
            "Picture Frame 5": lambda state:
                has_infra(world, state) and can_smash(world, state),
            "Picture Frame 6": lambda state:
                has_infra(world, state) and can_smash(world, state),
            "Picture Frame 8": lambda state:
                can_swing(world, state),
            "Picture Frame 12": lambda state:
                can_smash(world, state),
            "Picture Frame 16": lambda state:
                can_swing(world, state),
            "Picture Frame 17": lambda state:
                can_swing(world, state) and can_smash(world, state) and
                (state.has("Zoom Stone", world.player) or state.has("Mega Stone", world.player)),
            "Picture Frame 27": lambda state:
                has_infra(world, state),
            "Picture Frame 28": lambda state:
                has_infra(world, state),
            "Picture Frame 29": lambda state:
                has_infra(world, state),
            "Picture Frame 30": lambda state:
                has_infra(world, state),
            "Picture Frame 31": lambda state:
                has_infra(world, state),
            "Picture Frame 32": lambda state:
                has_infra(world, state),
            "Picture Frame 33": lambda state:
                state.has("Grav Grenade", world.player),
            "Picture Frame 42": lambda state:
                state.has("Grav Grenade", world.player),
            "Picture Frame 52": lambda state:
                can_smash(world, state),
            "Picture Frame 53": lambda state:
                can_smash(world, state),
            "Picture Frame 54": lambda state:
                can_smash(world, state),
            "Picture Frame 55": lambda state:
                can_smash(world, state),
            "Picture Frame 56": lambda state:
                has_infra(world, state),
            "Picture Frame 57": lambda state:
                has_infra(world, state),
            "Picture Frame 58": lambda state:
                has_infra(world, state),
            "Picture Frame 59": lambda state:
                has_infra(world, state),
            "Picture Frame 60": lambda state:
                has_infra(world, state),
            "Picture Frame 61": lambda state:
                has_infra(world, state),
            "Picture Frame 70": lambda state:
                can_smash(world, state),
            "Picture Frame 71": lambda state:
                can_smash(world, state),
            "Picture Frame 72": lambda state:
                can_smash(world, state),
            "Picture Frame 73": lambda state:
                can_smash(world, state),
            "Picture Frame 74": lambda state:
                can_smash(world, state),
            "Picture Frame 81": lambda state:
                state.has("Grav Grenade", world.player)
                or state.has("Satellite Cannon", world.player),
            "Picture Frame 82": lambda state:
                state.has("Grav Grenade", world.player)
                or state.has("Satellite Cannon", world.player),
            "Picture Frame 96": lambda state:
                has_infra(world, state),
            "Picture Frame 104": lambda state:
                state.has("Magnet Stone", world.player, 2) and has_chassis(world, state, 0b10111010),
            "Picture Frame 108": lambda state:
                can_smash(world, state),
            "Picture Frame 109": lambda state:
                can_smash(world, state),
            "Picture Frame 111": lambda state:
                can_smash(world, state) and can_swing(world, state),
            "Picture Frame 112": lambda state:
                can_smash(world, state),
            "Picture Frame 114": lambda state:
                can_smash(world, state),
            "Picture Frame 115": lambda state:
                can_smash(world, state),
            "Picture Frame 116": lambda state:
                has_infra(world, state),
            "Picture Frame 117": lambda state:
                has_infra(world, state),
            "Picture Frame 118": lambda state:
                has_infra(world, state),
            "Picture Frame 119": lambda state:
                has_infra(world, state),
            "Picture Frame 120": lambda state:
                has_infra(world, state),
        },
        "entrances": {
            "Razorback Stream Crab": lambda state:
                state.has("Crabmersible", world.player),
            "Desert Duke Airship": lambda state:
                can_gunyip(world, state),
            "Desert Sly Airship": lambda state:
                can_bunyip(world, state),
            "Swamp Duke Airship": lambda state:
                can_gunyip(world, state),
            "Swamp Sly Airship": lambda state:
                can_bunyip(world, state),
            "Sly Airship - FF": lambda state:
                can_bunyip(world, state),
            "Sly Airship - BB": lambda state:
                can_bunyip(world, state),
            "Sly Airship - WW": lambda state:
                can_bunyip(world, state),
            "Duke Airship - MBB": lambda state:
                can_gunyip(world, state) and state.has("Level - Mount Boom Basin", world.player),
            "Duke Airship - KBI": lambda state:
                can_gunyip(world, state) and state.has("Level - Kaka Boom Island", world.player),
            "Dead Dingo Marsh Tunnel": lambda state:
                state.has("Level - Dead Dingo Marsh", world.player),
            "Gooboo Gully Tunnel": lambda state:
                state.has("Level - Gooboo Gully", world.player),
            "Cinder Canyon Cave": lambda state:
                state.has("Level - Cinder Canyon", world.player) and can_gunyip(world, state),
            "SR Gate": lambda state:
                state.has("Southern Rivers Gate", world.player),
            "Portal": lambda state:
                state.has("Southern Rivers Gate", world.player),
            "Airship - Quinking": lambda state:
                state.has("Story Mission Complete", world.player, world.options.story_missions_for_goal.value)
                and state.has("Bunyip Mission Complete", world.player, world.options.bunyip_missions_for_goal.value)
                and state.has("Gunyip Mission Complete", world.player, world.options.gunyip_missions_for_goal.value)
                and state.has("Race Mission Complete", world.player, world.options.race_missions_for_goal.value),
        }
    }
    return rules


def set_rules(world):

    rules_lookup = get_rules(world)

    for entrance_name, rule in rules_lookup["entrances"].items():
        try:
            world.get_entrance(entrance_name).access_rule = rule
        except KeyError as e:
            #print(f"Key error, {e}")
            pass

    for location_name, rule in rules_lookup["locations"].items():
        try:
            world.get_location(location_name).access_rule = rule
        except KeyError as e:
            #print(f"Key error, {e}")
            pass

    for location_name in opal_shop_location_dict:
        world.get_location(location_name).item_rule = \
            lambda item: item.name not in full_item_dict or full_item_dict[item.name].currency_type != "Opal"
    for location_name in korb_shop_location_dict:
        world.get_location(location_name).item_rule = \
            lambda item: item.name not in full_item_dict or full_item_dict[item.name].currency_type not in {"Opal", "KOrb"}
    for location_name in berry_shop_location_dict:
        world.get_location(location_name).item_rule = \
            lambda item: item.name not in full_item_dict or full_item_dict[item.name].currency_type not in {"Opal", "Berry"}
    for location_name in bilby_shop_location_dict:
        world.get_location(location_name).item_rule = \
            lambda item: item.name not in full_item_dict or full_item_dict[item.name].currency_type not in {"Opal", "Bilby"}

    world.multiworld.get_location(f"Quinking", world.player).place_locked_item(
        Ty3Item("Victory", ItemClassification.progression, None, world.player))
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)