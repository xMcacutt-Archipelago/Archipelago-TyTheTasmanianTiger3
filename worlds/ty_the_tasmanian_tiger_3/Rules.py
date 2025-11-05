from BaseClasses import ItemClassification, CollectionState, Location
from worlds.ty_the_tasmanian_tiger_3.Items import Ty3Item
from worlds.ty_the_tasmanian_tiger_3.Locations import Ty3Location, mission_dict


def has_infra(world, state):
    return (state.has("Ultra Stone", world.player)),

def can_magnet(world, state):
    return (state.has("Magnet Stone", world.player, 3)),

def can_bunyip(world, state):
    return (state.has("Sly", world.player)),

def can_gunyip(world, state):
    return (state.has("Duke", world.player)),

def can_smash(world, state):
    return (state.has("Earth Stone", world.player)
            or state.has("Smash Chassis", world.player)
            or state.has("Doom Chassis", world.player)),

def can_burn(world, state):
    return (state.has("Fire Stone", world.player)),

def can_freeze(world, state):
    return (state.has("Water Stone", world.player)),

def can_zap(world, state):
    return (state.has("Air Stone", world.player)),

def can_swing(world, state):
    return (state.has("Lash Chassis", world.player)),

def can_tp(world, state):
    return (state.has("Warp Stone", world.player)),

def get_rules(world):
    rules = {
        "locations": {
            #collectable shops
            "Naomi's Ice Cream Truck Berry Blast 1": lambda state:
                state.has("Gooboo Berry", world.player, sum(world.berry_prices[:1])),
            "Naomi's Ice Cream Truck Berry Blast 2": lambda state:
                state.has("Gooboo Berry", world.player, sum(world.berry_prices[:2])),
            "Naomi's Ice Cream Truck Berry Blast 3": lambda state:
                state.has("Gooboo Berry", world.player, sum(world.berry_prices[:3])),
            "Naomi's Ice Cream Truck Berry Blast 4": lambda state:
                state.has("Gooboo Berry", world.player, sum(world.berry_prices[:4])),
            "Naomi's Ice Cream Truck Bilby Banana Split 1": lambda state:
            state.has("Bilby", world.player, sum(world.bilby_prices[:1])),
            "Naomi's Ice Cream Truck Bilby Banana Split 2": lambda state:
            state.has("Bilby", world.player, sum(world.bilby_prices[:2])),
            "Naomi's Ice Cream Truck Bilby Banana Split 3": lambda state:
            state.has("Bilby", world.player, sum(world.bilby_prices[:3])),
            "Naomi's Ice Cream Truck Bilby Banana Split 4": lambda state:
            state.has("Bilby", world.player, sum(world.bilby_prices[:4])),
            "Naomi's Ice Cream Truck Bilby Banana Split 5": lambda state:
            state.has("Bilby", world.player, sum(world.bilby_prices[:5])),

            "Rang Shop Korb 1": lambda state:
                state.has("Kromium Orb", world.player, sum(world.orb_prices[:1])),
            "MRang Shop Korb 2": lambda state:
                state.has("Kromium Orb", world.player, sum(world.orb_prices[:2])),
            "Rang Shop Korb 3": lambda state:
                state.has("Kromium Orb", world.player, sum(world.orb_prices[:3])),
            "Rang Shop Korb 4": lambda state:
                state.has("Kromium Orb", world.player, sum(world.orb_prices[:4])),
            "Rang Shop Korb 5": lambda state:
                state.has("Kromium Orb", world.player, sum(world.orb_prices[:5])),
            "Rang Shop Korb 6": lambda state:
                state.has("Kromium Orb", world.player, sum(world.orb_prices[:6])),
            "Rang Shop Korb 7": lambda state:
                state.has("Kromium Orb", world.player, sum(world.orb_prices[:7])),
            "Rang Shop Korb 8": lambda state:
                state.has("Kromium Orb", world.player, sum(world.orb_prices[:8])),

            #Missions
            "Egg Hunt": lambda state:
                state.has("Satellite Strike", world.player),
            "Power Struggle": lambda state:
                state.has("Grav Grenade", world.player) and state.has("Shadow Beam", world.player),
            "Meltdown": lambda state:
                state.has("Thermo Cannon", world.player),
            "Ranger Endanger": lambda state:
                state.has("Shadow Beam", world.player),
            "Redback Rundown": lambda state:
                state.has("Thermo Cannon", world.player),
            "All Your Base": lambda state:
                can_gunyip(world, state),
            "Aero Coast Guard": lambda state:
                can_gunyip(world, state),
            "Wrath of the Dragonquin": lambda state:
                can_gunyip(world, state),
            "Forest Firepower": lambda state:
                can_gunyip(world, state),

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
            "Bilby 19": lambda state:
                state.has("Grav Grenade", world.player),
            "Bilby 22": lambda state:
                can_smash(world, state),
            "Bilby 24": lambda state:
                can_smash(world, state),
            "Bilby 36": lambda state:
                can_tp(world, state), #jump is possible without warp

            #Stones
            "Stone 3": lambda state:
                has_infra(world, state) and can_swing(world, state),
            "Stone 6": lambda state:
                can_magnet(world, state),
            "Stone 8": lambda state:
                can_magnet(world, state),
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
                state.has("Grav Grenade", world.player) or state.has("Satellite Cannon", world.player),
            "Picture Frame 82": lambda state:
                state.has("Grav Grenade", world.player) or state.has("Satellite Cannon", world.player),
            "Picture Frame 96": lambda state:
                has_infra(world, state),
            "Picture Frame 104": lambda state:
                state.has("Magnet Stone", world.player, 2),
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
            "Desert Duke Airship":
                lambda state: state.has("Duke", world.player),
            "Desert Sly Airship":
                lambda state: state.has("Sly", world.player),
            "Swamp Duke Airship":
                lambda state: state.has("Duke", world.player),
            "Swamp Sly Airship":
                lambda state: state.has("Sly", world.player),
            "Sly Airship - FF":
                lambda state: state.has("Sly", world.player),
            "Sly Airship - BB":
                lambda state: state.has("Sly", world.player),
            "Sly Airship - WW":
                lambda state: state.has("Sly", world.player),
            "Duke Airship - MBB":
                lambda state: state.has("Duke", world.player),
            "Duke Airship - KBI":
                lambda state: state.has("Duke", world.player),
            "SR Gate":
                lambda state: (state.has("Hexaquin Defeated", world.player) and world.options.gate_unlock == 0) or
                              (state.has("Southern Rivers Gate", world.player) and world.options.gate_unlock == 1) or
                              world.options.gate_unlock == 2,
            "MountBoom Start Lava":
                lambda state: state.has("Thermo Bunyip Key", world.player),
            "MountBoom End Lava":
                lambda state: state.has("Thermo Bunyip Key", world.player),
            "MountBoom End ParkingBay":
                lambda state: state.has("MountBoom End ParkingBay", world.player),
            "Burramudgee ParkingBay":
                lambda state: state.has("Burramudgee Town ParkingBay", world.player),
            "Min Min Plains ParkingBay":
                lambda state: state.has("Min Min Plains ParkingBay", world.player),
            "Freeway Training Grounds ParkingBay":
                lambda state: state.has("Freeway Training Grounds ParkingBay", world.player),
            "Beach Training Grounds ParkingBay":
                lambda state: state.has("Beach Training Grounds ParkingBay", world.player),
            "Dennis Freeway ParkingBay":
                lambda state: state.has("Dennis Freeway ParkingBay", world.player),
            "Wobbygon Bay ParkingBay":
                lambda state: state.has("Wobbygon Bay ParkingBay", world.player),
            "Lava Falls Race ParkingBay":
                lambda state: state.has("Lava Falls Race ParkingBay", world.player),
            "Frill Neck Forest ParkingBay":
                lambda state: state.has("Frill Neck Forest ParkingBay", world.player),
            "Old Stony Creek ParkingBay":
                lambda state: state.has("Old Stony Creek ParkingBay", world.player),
            "Camping ParkingBay":
                lambda state: state.has("Camping ParkingBay", world.player),
            "Outback Oasis ParkingBay":
                lambda state: state.has("Outback Oasis ParkingBay", world.player),
            "Refinery Run ParkingBay":
                lambda state: state.has("Refinery Run ParkingBay", world.player),
            "Fire Fight ParkingBay":
                lambda state: state.has("Fire Fight ParkingBay", world.player),
            "Sly ParkingBay":
                lambda state: state.has("Sly ParkingBay", world.player),
            "Outback Dash ParkingBay":
                lambda state: state.has("Outback Dash ParkingBay", world.player),
            "Never Never Road ParkingBay":
                lambda state: state.has("Never Never Road ParkingBay", world.player),
            "Truck Tragedy ParkingBay":
                lambda state: state.has("Truck Tragedy ParkingBay", world.player),
            "Truck Stop ParkingBay":
                lambda state: state.has("Truck Stop ParkingBay", world.player),
            "Plutonium Panic ParkingBay":
                lambda state: state.has("Plutonium Panic ParkingBay", world.player),
            "50 Foot Squeaver ParkingBay":
                lambda state: state.has("50 Foot Squeaver ParkingBay", world.player),
            "Never Never ParkingBay":
                lambda state: state.has("Never Never ParkingBay", world.player),
            "Lava Falls ParkingBay":
                lambda state: state.has("Lava Falls ParkingBay", world.player),
            "Min Min Mining ParkingBay":
                lambda state: state.has("Min Min Mining ParkingBay", world.player),
            "Turbo Track ParkingBay":
                lambda state: state.has("Turbo Track ParkingBay", world.player),
            "King Squeaver ParkingBay":
                lambda state: state.has("King Squeaver ParkingBay", world.player),
            "Bush Fire ParkingBay":
                lambda state: state.has("Bush Fire ParkingBay", world.player),
            "Sulphur Rocks ParkingBay":
                lambda state: state.has("Sulphur Rocks ParkingBay", world.player),
            "Lake Burramudgee ParkingBay":
                lambda state: state.has("Lake Burramudgee ParkingBay", world.player),
            "Muddy Bottom ParkingBay":
                lambda state: state.has("Muddy Bottom ParkingBay", world.player),
            "Dusty Barrows ParkingBay":
                lambda state: state.has("Dusty Barrows ParkingBay", world.player),
            "Ripper Nipper ParkingBay":
                lambda state: state.has("Ripper Nipper ParkingBay", world.player),
            "Faire Dinkum ParkingBay":
                lambda state: state.has("Faire Dinkum ParkingBay", world.player),
            "Wetlands ParkingBay":
                lambda state: state.has("Wetlands ParkingBay", world.player),
            "Hearty Beach ParkingBay":
                lambda state: state.has("Hearty Beach ParkingBay", world.player),
            "Patchy Barriers West":
                lambda state: state.has("Patchy Barriers", world.player),
            "Patchy Barriers South":
                lambda state: state.has("Patchy Barriers", world.player),
            "Fluffy Barriers South":
                lambda state: state.has("Fluffy Barriers", world.player),
            "Fluffy Barriers North":
                lambda state: state.has("Fluffy Barriers", world.player),
            "Buster Barriers West":
                lambda state: state.has("Buster Barriers", world.player),
            "Buster Barriers East":
                lambda state: state.has("Buster Barriers", world.player),
            "Truck Stop Clear":
                lambda state: state.has("Truck Stop ParkingBay", world.player),
            "Patchy ParkingBay":
                lambda state: state.has("Patchy ParkingBay", world.player),
            "Oil Rig ParkingBay":
                lambda state: state.has("Oil Rig ParkingBay", world.player),
            "Oil Rig Button":
                lambda state: state.has("Thermo Bunyip Key", world.player),
            "Fluffy ParkingBay":
                lambda state: state.has("Fluffy ParkingBay", world.player),
            "Airship - Quinking":
                lambda state: state.has("Mission Complete", world.player, world.options.missions_for_goal.value),
        }
    }
    return rules



def set_rules(world):

    rules_lookup = get_rules(world)

    world.explicit_indirect_conditions = False

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

    world.multiworld.get_location(f"Quinking", world.player).place_locked_item(
        Ty3Item("Victory", ItemClassification.progression, None, world.player))
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)