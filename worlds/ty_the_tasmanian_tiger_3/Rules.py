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
            "Naomi's Ice Cream Truck Berry Purchase 1": lambda state:
                state.has("Gooboo Berry", world.player, 2),
            "Naomi's Ice Cream Truck Berry Purchase 2": lambda state:
                state.has("Gooboo Berry", world.player, 4),
            "Naomi's Ice Cream Truck Berry Purchase 3": lambda state:
                state.has("Gooboo Berry", world.player, 6),
            "Naomi's Ice Cream Truck Berry Purchase 4": lambda state:
                state.has("Gooboo Berry", world.player, 8),

            "Naomi's Ice Cream Truck Bilby Purchase 1": lambda state:
                state.has("Bilby", world.player, 7),
            "Naomi's Ice Cream Truck Bilby Purchase 2": lambda state:
                state.has("Bilby", world.player, 14),
            "Naomi's Ice Cream Truck Bilby Purchase 3": lambda state:
                state.has("Bilby", world.player, 21),
            "Naomi's Ice Cream Truck Bilby Purchase 4": lambda state:
                state.has("Bilby", world.player, 28),
            "Naomi's Ice Cream Truck Bilby Purchase 5": lambda state:
                state.has("Bilby", world.player, 35),

            "Rang Shop Purchase 1": lambda state:
                state.has("Kromium Orb", world.player, 3),
            "Rang Shop Purchase 2": lambda state:
                state.has("Kromium Orb", world.player, 6),
            "Rang Shop Purchase 3": lambda state:
                state.has("Kromium Orb", world.player, 9),
            "Rang Shop Purchase 4": lambda state:
                state.has("Kromium Orb", world.player, 12),
            "Rang Shop Purchase 5": lambda state:
                state.has("Kromium Orb", world.player, 15),
            "Rang Shop Purchase 6": lambda state:
                state.has("Kromium Orb", world.player, 18),
            "Rang Shop Purchase 7": lambda state:
                state.has("Kromium Orb", world.player, 21),
            "Rang Shop Purchase 8": lambda state:
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
            "Cinder Canyon Orb 1": lambda state:
                has_infra(world, state),
            "Cinder Canyon Orb 2": lambda state:
                has_infra(world, state),
            "Cinder Canyon Orb 3": lambda state:
                can_smash(world, state),
            "Mount Boom Basin Orb 1": lambda state:
                can_burn(world, state),
            "Dead Dingo Marsh Orb 2": lambda state:
                can_swing(world, state) and can_smash(world, state) and
                (state.has("Zoom Stone", world.player) or state.has("Mega Stone", world.player)),
            "Dead Dingo Marsh Orb 3": lambda state:
                has_infra(world, state),
            "New Burramudgee Orb 1": lambda state:
                can_smash(world, state),
            "Dead Dingo Marsh Orb 4": lambda state:
                has_infra(world, state),
            "Mount Boom Basin Orb 3": lambda state:
                can_smash(world, state),
            "SR Swamp Orb 1": lambda state:
                can_freeze(world, state),
            "SR Swamp Orb 3": lambda state:
                can_gunyip(world, state),
            "Kaka Boom Island Orb 4": lambda state:
                has_infra(world, state),
            "Gooboo Gully Orb 1": lambda state:
                has_infra(world, state),
            "Gooboo Gully Orb 3": lambda state:
                can_swing(world, state),
            "Gooboo Gully Orb 4": lambda state:
                has_infra(world, state),
            "Cinder Canyon Orb 4": lambda state:
                has_infra(world, state),

            #Bilbies
            "New Burramudgee Bilby 2": lambda state:
                can_zap(world,state),
            "Cinder Canyon Bilby 1": lambda state:
                can_burn(world, state),
            "Cinder Canyon Bilby 2": lambda state:
                can_tp(world, state),
            "Backwood Blizzard Bilby 1": lambda state:
                state.has("Grav Grenade", world.player) or state.has("Satellite Strike", world.player),
            "Backwood Blizzard Bilby 2": lambda state:
            state.has("Grav Grenade", world.player) or state.has("Satellite Strike", world.player),
            "Dead Dingo Marsh Bilby 1": lambda state:
                can_swing(world, state),
            "Frozen Forest Bilby 2": lambda state:
                state.has("Grav Grenade", world.player),
            "Dead Dingo Marsh Bilby 3": lambda state:
                state.has("Water Stone", world.player),
            "Winter Woods Bilby 3": lambda state:
                state.has("Grav Grenade", world.player),
            "Kaka Boom Island Bilby 3": lambda state:
                can_smash(world, state),
            "SR Swamp Bilby 1": lambda state:
                can_smash(world, state),
            "SR Swamp Bilby 4": lambda state:
                state.has("Level - Kaka Boom Island", world.player),
            "Razorback Stream Bilby": lambda state:
                can_tp(world, state), #jump is possible without warp

            #Stones
            "Razorback Stream Stone 1": lambda state:
                state.has("Karlos", world.player),
            "Razorback Stream Stone 2": lambda state:
                state.has("Karlos", world.player),
            "Dead Dingo Marsh Stone 1": lambda state:
                has_infra(world, state) and can_swing(world, state),
            "Kaka Boom Island Stone 1": lambda state:
                can_magnet(world, state),
            "SR Swamp Stone 1": lambda state:
                state.has("Karlos", world.player),
            "SR Swamp Stone 2": lambda state:
                state.has("Karlos", world.player),
            "SR Swamp Stone 3": lambda state:
                state.has("Karlos", world.player),
            "SR Swamp Stone 4": lambda state:
                state.has("Karlos", world.player),
            "Frozen Forest Stone 1": lambda state:
                state.has("Grav Grenade", world.player),
            "New Burramudgee Stone 1": lambda state:
                can_smash(world, state),
            "New Burramudgee Stone 2": lambda state:
                can_magnet(world, state),
            "Razorback Stream Stone 4": lambda state:
                can_burn(world, state),
            "Cinder Canyon Stone 2": lambda state:
                can_zap(world, state),
            "Mount Boom Basin Stone 2": lambda state:
                has_infra(world, state) and can_burn(world, state),
            "Cassopolis Stone 1": lambda state:
                can_swing(world, state),
            "Cassopolis Stone 2": lambda state:
                has_infra(world, state),
            "Razorback Stream Stone 5": lambda state:
                has_infra(world, state),
            "Razorback Stream Stone 6": lambda state:
                can_burn(world, state) and can_zap(world, state),

            #Steves
            "Steve - Razorback Stream": lambda state:
                can_burn(world, state),
            "Steve - Kaka Boom Island": lambda state:
                can_smash(world, state),

            #Berries
            "Cinder Canyon Gooboo Berry": lambda state:
                can_smash(world, state),
            "Dead Dingo Marsh Gooboo Berry": lambda state:
                can_swing(world, state),
            "Mount Boom Basin Gooboo Berry": lambda state:
                can_swing(world, state) and can_burn(world, state),
            "Kaka Boom Island Gooboo Berry": lambda state:
                can_smash(world, state),

            #Frames
            "Dead Dingo Marsh Picture Frame 1": lambda state:
                has_infra(world, state),
            "Dead Dingo Marsh Picture Frame 2": lambda state:
                has_infra(world, state) and can_smash(world, state),
            "Dead Dingo Marsh Picture Frame 3": lambda state:
                has_infra(world, state) and can_smash(world, state),
            "Dead Dingo Marsh Picture Frame 4": lambda state:
                has_infra(world, state) and can_smash(world, state),
            "Dead Dingo Marsh Picture Frame 5": lambda state:
                has_infra(world, state) and can_smash(world, state),
            "Dead Dingo Marsh Picture Frame 6": lambda state:
                has_infra(world, state) and can_smash(world, state),
            "Dead Dingo Marsh Picture Frame 7": lambda state:
                can_swing(world, state),
            "Cassopolis Picture Frame 1": lambda state:
                can_smash(world, state),
            "Dead Dingo Marsh Picture Frame 14": lambda state:
                can_swing(world, state),
            "Dead Dingo Marsh Picture Frame 15": lambda state:
                can_swing(world, state) and can_smash(world, state) and
                (state.has("Zoom Stone", world.player) or state.has("Mega Stone", world.player)),
            "Kaka Boom Island Picture Frame 10": lambda state:
                has_infra(world, state),
            "Kaka Boom Island Picture Frame 11": lambda state:
                has_infra(world, state),
            "Kaka Boom Island Picture Frame 12": lambda state:
                has_infra(world, state),
            "Kaka Boom Island Picture Frame 13": lambda state:
                has_infra(world, state),
            "Kaka Boom Island Picture Frame 14": lambda state:
                has_infra(world, state),
            "Kaka Boom Island Picture Frame 15": lambda state:
                has_infra(world, state),
            "Winter Woods Picture Frame 1": lambda state:
                state.has("Grav Grenade", world.player),
            "Winter Woods Picture Frame 10": lambda state:
                state.has("Grav Grenade", world.player),
            "Mount Boom Basin Picture Frame 1": lambda state:
                can_smash(world, state),
            "Mount Boom Basin Picture Frame 2": lambda state:
                can_smash(world, state),
            "Mount Boom Basin Picture Frame 3": lambda state:
                can_smash(world, state),
            "Mount Boom Basin Picture Frame 4": lambda state:
                can_smash(world, state),
            "Mount Boom Basin Picture Frame 5": lambda state:
                has_infra(world, state),
            "Mount Boom Basin Picture Frame 6": lambda state:
                has_infra(world, state),
            "Mount Boom Basin Picture Frame 7": lambda state:
                has_infra(world, state),
            "Mount Boom Basin Picture Frame 8": lambda state:
                has_infra(world, state),
            "Mount Boom Basin Picture Frame 9": lambda state:
                has_infra(world, state),
            "Mount Boom Basin Picture Frame 10": lambda state:
                has_infra(world, state),
            "Cinder Canyon Picture Frame 4": lambda state:
                can_smash(world, state),
            "Cinder Canyon Picture Frame 5": lambda state:
                can_smash(world, state),
            "Cinder Canyon Picture Frame 6": lambda state:
                can_smash(world, state),
            "Cinder Canyon Picture Frame 7": lambda state:
                can_smash(world, state),
            "Cinder Canyon Picture Frame 8": lambda state:
                can_smash(world, state),
            "Backwood Blizzard Picture Frame 5": lambda state:
                state.has("Grav Grenade", world.player)
                or state.has("Satellite Cannon", world.player),
            "Backwood Blizzard Picture Frame 6": lambda state:
                state.has("Grav Grenade", world.player)
                or state.has("Satellite Cannon", world.player),
            "SR Swamp Picture Frame 14": lambda state:
                has_infra(world, state),
            "New Burramudgee Picture Frame 7": lambda state:
                state.has("Magnet Stone", world.player, 2) and has_chassis(world, state, 0b10111010),
            "Cassopolis Picture Frame 3": lambda state:
                can_smash(world, state),
            "Cassopolis Picture Frame 4": lambda state:
                can_smash(world, state),
            "Cassopolis Picture Frame 6": lambda state:
                can_smash(world, state) and can_swing(world, state),
            "Cassopolis Picture Frame 7": lambda state:
                can_smash(world, state),
            "Cassopolis Picture Frame 9": lambda state:
                can_smash(world, state),
            "Cassopolis Picture Frame 10": lambda state:
                can_smash(world, state),
            "Dead Dingo Marsh Picture Frame 16": lambda state:
                has_infra(world, state),
            "Dead Dingo Marsh Picture Frame 17": lambda state:
                has_infra(world, state),
            "Dead Dingo Marsh Picture Frame 18": lambda state:
                has_infra(world, state),
            "Dead Dingo Marsh Picture Frame 19": lambda state:
                has_infra(world, state),
            "Dead Dingo Marsh Picture Frame 20": lambda state:
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
            lambda item: item.game != "Ty the Tasmanian Tiger 3" or item.name not in full_item_dict or full_item_dict[item.name].currency_type != "Opal"
    for location_name in korb_shop_location_dict:
        world.get_location(location_name).item_rule = \
            lambda item: item.game != "Ty the Tasmanian Tiger 3" or item.name not in full_item_dict or full_item_dict[item.name].currency_type not in {"Opal", "KOrb"}
    for location_name in berry_shop_location_dict:
        world.get_location(location_name).item_rule = \
            lambda item: item.game != "Ty the Tasmanian Tiger 3" or item.name not in full_item_dict or full_item_dict[item.name].currency_type not in {"Opal", "Berry"}
    for location_name in bilby_shop_location_dict:
        world.get_location(location_name).item_rule = \
            lambda item: item.game != "Ty the Tasmanian Tiger 3" or item.name not in full_item_dict or full_item_dict[item.name].currency_type not in {"Opal", "Bilby"}

    world.multiworld.get_location(f"Quinking", world.player).place_locked_item(
        Ty3Item("Victory", ItemClassification.progression, None, world.player))
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)