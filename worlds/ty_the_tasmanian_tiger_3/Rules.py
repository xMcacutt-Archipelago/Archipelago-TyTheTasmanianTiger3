from BaseClasses import ItemClassification, CollectionState, Location
from worlds.ty_the_tasmanian_tiger_3.Items import Ty3Item
from worlds.ty_the_tasmanian_tiger_3.Locations import Ty3Location, mission_dict


def has_infra(world, state):
    return (state.has("Ultra Stone", world.player)),

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
            "Trader Bob's Cog 1": lambda state:
                state.has("Platinum Cog", world.player, sum(world.cog_prices[:1])),
            "Trader Bob's Cog 2": lambda state:
                state.has("Platinum Cog", world.player, sum(world.cog_prices[:2])),
            "Trader Bob's Cog 3": lambda state:
                state.has("Platinum Cog", world.player, sum(world.cog_prices[:3])),
            "Trader Bob's Cog 4": lambda state:
                state.has("Platinum Cog", world.player, sum(world.cog_prices[:4])),
            "Trader Bob's Cog 5": lambda state:
                state.has("Platinum Cog", world.player, sum(world.cog_prices[:5])),
            "Trader Bob's Cog 6": lambda state:
                state.has("Platinum Cog", world.player, sum(world.cog_prices[:6])),
            "Trader Bob's Cog 7": lambda state:
                state.has("Platinum Cog", world.player, sum(world.cog_prices[:7])),
            "Trader Bob's Cog 8": lambda state:
                state.has("Platinum Cog", world.player, sum(world.cog_prices[:8])),
            "Trader Bob's Cog 9": lambda state:
                state.has("Platinum Cog", world.player, sum(world.cog_prices[:9])),
            "Trader Bob's Cog 10": lambda state:
                state.has("Platinum Cog", world.player, sum(world.cog_prices[:10])),
            "Madam Mopoke's 1": lambda state:
                state.has("Kromium Orb", world.player, sum(world.orb_prices[:1])),
            "Madam Mopoke's 2": lambda state:
                state.has("Kromium Orb", world.player, sum(world.orb_prices[:2])),
            "Madam Mopoke's 3": lambda state:
                state.has("Kromium Orb", world.player, sum(world.orb_prices[:3])),

            #Missions
            "Haunted Hassle": lambda state:
                has_infra(world, state),
            "Lava Chill Out": lambda state:
                can_swing(world, state) or can_cold(world, state),
            "Hidden Danger": lambda state:
                has_infra(world, state),
            "Deep Sea Scare": lambda state:
                state.has("Sub Bunyip Key", world.player),
            "Sea Lab": lambda state:
                state.has("Sub Bunyip Key", world.player),
            "Oil Rig Fire": lambda state:
                state.has("Thermo Bunyip Key", world.player),
            "Truck Tragedy": lambda state:
                state.has("Lifter Bunyip Key", world.player),
            "Truck Stop": lambda state:
                state.has("Lifter Bunyip Key", world.player),
            "Bush Fire": lambda state:
                state.has("Thermo Bunyip Key", world.player),
            "Killer Koala": lambda state:
                has_infra(world, state),
            "Grub Grab": lambda state:
                state.has("Burramudgee Town ParkingBay", world.player) and (state.has("Patchy Barriers", world.player) or state.has("Buster Barriers", world.player)),
            "Ripper Nipper": lambda state:
                state.has("Wobbygon Bay ParkingBay", world.player) and state.has("Ripper Nipper ParkingBay", world.player),
            "Complete Haunted Hassle": lambda state:
                has_infra(world, state),
            "Complete Lava Chill Out": lambda state:
                can_swing(world, state) or can_cold(world, state),
            "Complete Hidden Danger": lambda state:
                has_infra(world, state),
            "Complete Deep Sea Scare": lambda state:
                state.has("Sub Bunyip Key", world.player),
            "Complete Sea Lab": lambda state:
                state.has("Sub Bunyip Key", world.player),
            "Complete Oil Rig Fire": lambda state:
                state.has("Thermo Bunyip Key", world.player),
            "Complete Truck Tragedy": lambda state:
                state.has("Lifter Bunyip Key", world.player),
            "Complete Truck Stop": lambda state:
                state.has("Lifter Bunyip Key", world.player),
            "Complete Bush Fire": lambda state:
                state.has("Thermo Bunyip Key", world.player),
            "Complete Killer Koala": lambda state:
                has_infra(world, state),
            "Complete Grub Grab": lambda state:
                state.has("Burramudgee Town ParkingBay", world.player) and (state.has("Patchy Barriers", world.player) or state.has("Buster Barriers", world.player)),
            "Complete Ripper Nipper": lambda state:
                state.has("Wobbygon Bay ParkingBay", world.player) and state.has("Ripper Nipper ParkingBay", world.player),

            #Cogs
            "Platinum Cog 2": lambda state:
                can_smash_wall(world, state),
            "Platinum Cog 4": lambda state:
                can_smash_wall(world, state),
            "Platinum Cog 6": lambda state:
                can_smash_wall(world, state),
            "Platinum Cog 12": lambda state:
                can_swing(world, state)  or can_cold(world, state),
            "Platinum Cog 17": lambda state:
                has_infra(world, state),
            "Platinum Cog 18": lambda state:
                can_swing(world, state),
            "Platinum Cog 20": lambda state:
                can_smash_wall(world, state),
            "Platinum Cog 21": lambda state:
                can_smash_wall(world, state),
            "Platinum Cog 24": lambda state:
                can_freeze(world, state),
            "Platinum Cog 25": lambda state:
                state.has("Lifter Bunyip Key", world.player),
            "Platinum Cog 32": lambda state:
                can_tp(world, state),
            "Platinum Cog 38": lambda state:
                can_tp(world, state),
            "Platinum Cog 40": lambda state:
                can_tp(world, state),
            "Platinum Cog 42": lambda state:
                can_smash_wall(world, state),
            "Platinum Cog 45": lambda state:
                can_burn(world, state),
            "Platinum Cog 50": lambda state:
                has_infra(world, state),

            #Orbs
            "Kromium Orb 1": lambda state:
                can_swing(world, state),
            "Kromium Orb 3": lambda state:
                can_swing(world, state),
            "Kromium Orb 4": lambda state:
                can_swing(world, state)  or can_freeze(world, state),
            "Kromium Orb 8": lambda state:
                can_tp(world, state) and can_smash_wall(world, state),
            "Kromium Orb 10": lambda state:
                can_smash_wall(world, state),
            "Kromium Orb 14": lambda state:
                has_infra(world, state),
            "Kromium Orb 15": lambda state:
                has_infra(world, state),
            "Kromium Orb 16": lambda state:
                can_smash_wall(world, state),
            "Kromium Orb 17": lambda state:
                can_swing(world, state),
            "Kromium Orb 23": lambda state:
                can_swing(world, state),
            "Kromium Orb 26": lambda state:
                can_swing(world, state),
            "Kromium Orb 28": lambda state:
                can_smash_wall(world, state),

            #Bilbies
            "Bilby 1": lambda state:
                can_smash_wall(world,state),
            "Bilby 5": lambda state:
                can_swing(world, state) or can_cold(world, state),
            "Bilby 16": lambda state:
                has_infra(world, state),
            "Bilby 17": lambda state:
                can_swing(world, state),
            "Bilby 19": lambda state:
                can_swing(world, state),
            "Bilby 20": lambda state:
                can_swing(world, state),
            "Bilby 22": lambda state:
                can_burn(world, state),
            "Bilby 23": lambda state:
                can_burn(world, state),
            "Bilby 26": lambda state:
                can_tp(world, state),
            "Bilby 28": lambda state:
                can_freeze(world, state),

            #Frills
            "Disguised Frill 1": lambda state:
                has_infra(world, state)
                and state.can_reach_region("Burramudgee Town", world.player)
                and can_smash_wall(world, state),
            "Disguised Frill 2": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 3": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 4": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 5": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 6": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 7": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 8": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 9": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 10": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 11": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 12": lambda state:
                has_infra(world, state)
                and state.can_reach_region("Burramudgee Town", world.player)
                and can_swing(world, state),
            "Disguised Frill 13": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 14": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 15": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 16": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 17": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 18": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 19": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 20": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 21": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 22": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 23": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 24": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),
            "Disguised Frill 25": lambda state:
                has_infra(world, state) and state.can_reach_region("Burramudgee Town", world.player),

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
                can_tp(world, state),
            "Picture Frame 2": lambda state:
                can_tp(world, state),
            "Picture Frame 3": lambda state:
                can_tp(world, state),
            "Picture Frame 5": lambda state:
                can_swing(world, state),
            "Picture Frame 7": lambda state:
                can_swing(world, state) or can_cold(world, state),
            "Picture Frame 13": lambda state:
                can_smash_wall(world, state),
            "Picture Frame 31": lambda state:
                can_smash_wall(world, state),
            "Picture Frame 32": lambda state:
                can_smash_wall(world, state),
            "Picture Frame 36": lambda state:
                can_swing(world, state),
            "Picture Frame 37": lambda state:
                can_swing(world, state),
            "Picture Frame 38": lambda state:
                can_swing(world, state),
            "Picture Frame 62": lambda state:
                can_swing(world, state),
        },
        "entrances": {
            "Burramudgee HQ -> Infra":
                lambda state: not world.options.require_infra
                or has_infra(world, state),
            "Burramudgee HQ -> Crates":
                lambda state: can_smash_crate(world, state),
            "Burramudgee Town -> Infra":
                lambda state: not world.options.require_infra
                              or has_infra(world, state),
            "Outback Oasis -> Infra":
                lambda state: not world.options.require_infra
                              or has_infra(world, state),
            "MountBoom -> Infra":
                lambda state: not world.options.require_infra
                              or has_infra(world, state),
            "Frill Neck Forest -> Infra":
                lambda state: not world.options.require_infra
                              or has_infra(world, state),
            "Wetlands -> Infra":
                lambda state: not world.options.require_infra
                              or has_infra(world, state),
            "Faire Dinkum -> Infra":
                lambda state: not world.options.require_infra
                              or has_infra(world, state),
            "Never Never -> Infra":
                lambda state: not world.options.require_infra
                              or has_infra(world, state),
            "Sulphur Rocks -> Infra":
                lambda state: not world.options.require_infra
                              or has_infra(world, state),
            "Wetlands Teleport":lambda state:
                can_tp(world, state),
            "MountBoom Start ParkingBay":
                lambda state: state.has("MountBoom Start ParkingBay", world.player),
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
            "Bush Rescue Plane":
                lambda state: (state.has("Mission Complete", world.player, world.options.missions_for_goal.value)
                               and state.has("Patchy Defeated", world.player)
                               and state.has("Buster Defeated", world.player)
                               and state.has("Fluffy Defeated", world.player)
                               ) if world.options.require_bosses.value else state.has("Mission Complete", world.player, world.options.missions_for_goal.value),
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