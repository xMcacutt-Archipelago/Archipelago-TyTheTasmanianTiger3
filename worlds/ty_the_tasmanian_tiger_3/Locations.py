from typing import NamedTuple, Optional, Dict

from BaseClasses import Location, Region
from worlds.ty_the_tasmanian_tiger_3.data import Ty3Level, ty3_levels


class Ty3Location(Location):
    game: str = "Ty the Tasmanian Tiger 3"


class LocData(NamedTuple):
    code: Optional[int]
    region: Optional[str]
    id: Optional[int] = -1
    mission_type: Optional[str] = ""
    level: Ty3Level = None


def create_ty3_locations(world):
    all_locations = {**story_dict, **opal_shop_location_dict, **korb_shop_location_dict,
                    **berry_shop_location_dict, **bilby_shop_location_dict, **gooboo_berry_dict,
                     **kromium_orb_dict, **bilby_dict, **mission_dict}

    all_locations.update(get_mission_complete_events(world))

    if world.options.stone_sanity.value:
        all_locations.update(stone_dict)
    if world.options.steve_sanity.value:
        all_locations.update(steve_dict)
    if world.options.frame_sanity.value:
        all_locations.update(picture_frame_dict)

    return all_locations


def get_mission_complete_events(world):
    complete_mission_dict = {}
    for name, loc_data in mission_dict.items():
        if loc_data.code is None:
            continue

        new_name = f"Complete {name}"
        new_ingame_id = loc_data.id + 100  # Add 100 to ingame ID

        complete_mission_dict[new_name] = LocData(None, loc_data.region, new_ingame_id, loc_data.mission_type)
    return complete_mission_dict


story_dict: Dict[str, LocData] = {
    "Bunyip Gauntlet": LocData(0x69BE, "The Dreaming"),
    "Shadowring Piece 1": LocData(0x901, "Mount Boom Basin", level=Ty3Level.MountBoomBasin),
    "Shadowring Piece 2": LocData(0x902, "Mount Boom Basin", level=Ty3Level.MountBoomBasin),
    "Shadowring Piece 3": LocData(0x903, "Mount Boom Basin", level=Ty3Level.MountBoomBasin),
    "Quinking": LocData(None, "Quinking"),  # goal
}


opal_shop_location_dict: Dict[str, LocData] = {
    "Rang Shop Purchase 1": LocData(0x6900 + 1,  "New Burramudgee"),  #fire
    "Rang Shop Purchase 2": LocData(0x6900 + 2,  "New Burramudgee"),  #water
    "Rang Shop Purchase 3": LocData(0x6900 + 7,  "New Burramudgee"),  #mega
    "Rang Shop Purchase 4": LocData(0x6900 + 23, "New Burramudgee"),  #duo chassis
    "Rang Shop Purchase 5": LocData(0x6900 + 5,  "New Burramudgee"),  #ultra
    "Rang Shop Purchase 6": LocData(0x6900 + 24, "New Burramudgee"),  #lash chassis
    "Cassopolis Rang Shop Purchase 1": LocData(0x6900 + 3, "Cassopolis"),  # air
    "Cassopolis Rang Shop Purchase 2": LocData(0x6900 + 14, "Cassopolis"),  # magnet
    "Cassopolis Rang Shop Purchase 3": LocData(0x6900 + 9, "Cassopolis"),  # warp
    "Cassopolis Rang Shop Purchase 4": LocData(0x6900 + 4, "Cassopolis"),  # earth
    "Cassopolis Rang Shop Purchase 5": LocData(0x6900 + 11, "Cassopolis"),  # zoom
    "Cassopolis Rang Shop Purchase 6": LocData(0x6900 + 13, "Cassopolis"),  # chrono
    "Cassopolis Rang Shop Purchase 7": LocData(0x6900 + 10, "Cassopolis"),  # multi
    "Cassopolis Rang Shop Purchase 8": LocData(0x6900 + 20, "Cassopolis"),  # mega chassis
    "Cassopolis Rang Shop Purchase 9": LocData(0x6900 + 21, "Cassopolis"),  # smash chassis
    "Cassopolis Rang Shop Purchase 10": LocData(0x6900 + 22, "Cassopolis"),  # ring chassis
    "Cassopolis Rang Shop Purchase 11": LocData(0x6900 + 26, "Cassopolis"),  # doom chassis
    "Naomi's Ice Cream Truck Purchase 1": LocData(0x6900 + 150, "New Burramudgee"),  # Grav Grenade
    "Naomi's Ice Cream Truck Purchase 2": LocData(0x6900 + 151, "New Burramudgee"),  # Satellite Strike
    "Naomi's Ice Cream Truck Purchase 3": LocData(0x6900 + 152, "New Burramudgee"),  # Shadow Beam
    "Naomi's Ice Cream Truck Purchase 4": LocData(0x6900 + 153, "New Burramudgee"),  # Thermo Cannon
    "Naomi's Ice Cream Truck Purchase 5": LocData(0x6900 + 154, "New Burramudgee"),  # Nucleon Shield
    "Naomi's Ice Cream Truck Purchase 6": LocData(0x6900 + 155, "New Burramudgee"),  # Orbidrills
    "Parrotbeard's Shop Purchase 1": LocData(0x6900 + 35, "Pippy Beach"),
    "Parrotbeard's Shop Purchase 2": LocData(0x6900 + 36, "Pippy Beach"),
    "Parrotbeard's Shop Purchase 3": LocData(0x6900 + 37, "Pippy Beach"),
    "Parrotbeard's Shop Purchase 4": LocData(0x6900 + 38, "Pippy Beach"),
    "Parrotbeard's Shop Purchase 5": LocData(0x6900 + 39, "Pippy Beach"),
}


korb_shop_location_dict: Dict[str, LocData] = {
    "Rang Shop Orb Purchase 1": LocData(0x6900 + 201, "New Burramudgee"),  # Original Ty Skin
    "Rang Shop Orb Purchase 2": LocData(0x6900 + 202, "New Burramudgee"),  # Sly Skin
    "Rang Shop Orb Purchase 3": LocData(0x6900 + 203, "New Burramudgee"),  # Team Krome Skin
    "Rang Shop Orb Purchase 4": LocData(0x6900 + 204, "New Burramudgee"),  # Commando Skin
    "Rang Shop Orb Purchase 5": LocData(0x6900 + 205, "New Burramudgee"),  # Zombie Skin
    "Rang Shop Orb Purchase 6": LocData(0x6900 + 206, "New Burramudgee"),  # Quinkan Skin
    "Rang Shop Orb Purchase 7": LocData(0x6900 + 207, "New Burramudgee"),  # Ridge Skin
    "Rang Shop Orb Purchase 8": LocData(0x6900 + 208, "New Burramudgee"),  # Ghost Tiger Skin
}


berry_shop_location_dict: Dict[str, LocData] = {
    "Naomi's Ice Cream Truck Berry Purchase 1": LocData(0x6900 + 221, "New Burramudgee"),  # Midnight Crab Skin
    "Naomi's Ice Cream Truck Berry Purchase 2": LocData(0x6900 + 222, "New Burramudgee"),  # Crab Tank Crab Skin
    "Naomi's Ice Cream Truck Berry Purchase 3": LocData(0x6900 + 223, "New Burramudgee"),  # White Knight Crab Skin
    "Naomi's Ice Cream Truck Berry Purchase 4": LocData(0x6900 + 224, "New Burramudgee"),  # Mean Green Crab Skin
}


bilby_shop_location_dict = {
    "Naomi's Ice Cream Truck Bilby Purchase 1": LocData(0x6900 + 231, "New Burramudgee"),  # Cammo Gunyip Skin
    "Naomi's Ice Cream Truck Bilby Purchase 2": LocData(0x6900 + 232, "New Burramudgee"),  # Bush Rescue Gunyip Skin
    "Naomi's Ice Cream Truck Bilby Purchase 3": LocData(0x6900 + 233, "New Burramudgee"),  # Nightmare Gunyip Skin
    "Naomi's Ice Cream Truck Bilby Purchase 4": LocData(0x6900 + 234, "New Burramudgee"),  # Sky Force Gunyip Skin
    "Naomi's Ice Cream Truck Bilby Purchase 5": LocData(0x6900 + 235, "New Burramudgee"),  # Spitfire Gunyip Skin
}


gooboo_berry_dict: Dict[str, LocData] = {
    "Cinder Canyon Gooboo Berry":            LocData(0x4000, "Cinder Canyon", level=Ty3Level.GoobooGully), #Earth
    "Southern Rivers Desert Gooboo Berry":   LocData(0x4001, "SR Desert - Duke", level=Ty3Level.SouthernRiversDesert), #Behind crabs at All Your Base airship
    "Dead Dingo Marsh Gooboo Berry":          LocData(0x4002, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh), #Lash
    "Mount Boom Basin Gooboo Berry":          LocData(0x4003, "Mount Boom Basin", level=Ty3Level.MountBoomBasin), #Flame, Lash
    "New Burramudgee Gooboo Berry":           LocData(0x4004, "New Burramudgee", level=Ty3Level.NewBurramudgee),
    "Kaka Boom Island Gooboo Berry":          LocData(0x4005, "Kaka Boom Island", level=Ty3Level.KakaboomIsland), #Earth
    "Southern Rivers Swamp Gooboo Berry 1":   LocData(0x4006, "SR Swamp", level=Ty3Level.SouthernRiversSwamp),
    "Southern Rivers Swamp Gooboo Berry 2":   LocData(0x4007, "Pippy Beach", level=Ty3Level.SouthernRiversSwamp),
    "Cassopolis Gooboo Berry":                LocData(0x4008, "Cassopolis", level=Ty3Level.Cassopolis),
    "Gooboo Gully Gooboo Berry":             LocData(0x4009, "Gooboo Gully", level=Ty3Level.GoobooGully),
}


kromium_orb_dict: Dict[str, LocData] = {
    "Cinder Canyon Orb 1": LocData(0x4300, "Cinder Canyon", level=Ty3Level.CinderCanyon), #ultra
    "Cinder Canyon Orb 2": LocData(0x4301, "Cinder Canyon", level=Ty3Level.CinderCanyon), #ultra
    "Cinder Canyon Orb 3": LocData(0x4302, "Cinder Canyon", level=Ty3Level.CinderCanyon), #earth
    "Mount Boom Basin Orb 1": LocData(0x4303, "Mount Boom Basin", level=Ty3Level.MountBoomBasin), #flame
    "Dead Dingo Marsh Orb 1": LocData(0x4304, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh),
    "Dead Dingo Marsh Orb 2": LocData(0x4305, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh), #earth, zoom/mega, lash
    "Dead Dingo Marsh Orb 3": LocData(0x4306, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh), #ultra
    "New Burramudgee Orb 1": LocData(0x4307, "New Burramudgee", level=Ty3Level.NewBurramudgee), #earth
    "New Burramudgee Orb 2": LocData(0x4308, "New Burramudgee", level=Ty3Level.NewBurramudgee),
    "Dead Dingo Marsh Orb 4": LocData(0x4309, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh), #ultra
    "Cassopolis Orb 1": LocData(0x430A, "Cassopolis", level=Ty3Level.Cassopolis), #boost panel
    "Cassopolis Orb 2": LocData(0x430B, "Cassopolis", level=Ty3Level.Cassopolis), #opened by hitting all 5 red buttons
    "Mount Boom Basin Orb 2": LocData(0x430C, "Mount Boom Basin", level=Ty3Level.MountBoomBasin),
    "Mount Boom Basin Orb 3": LocData(0x430D, "Mount Boom Basin", level=Ty3Level.MountBoomBasin), #earth
    "Mount Boom Basin Orb 4": LocData(0x430E, "Mount Boom Basin", level=Ty3Level.MountBoomBasin),
    "Kaka Boom Island Orb 1": LocData(0x430F, "Kaka Boom Island", level=Ty3Level.KakaboomIsland),
    "Kaka Boom Island Orb 2": LocData(0x4310, "Kaka Boom Island", level=Ty3Level.KakaboomIsland),
    "SR Swamp Orb 1": LocData(0x4311, "Pippy Beach", level=Ty3Level.SouthernRiversSwamp), #water
    "SR Swamp Orb 2": LocData(0x4312, "SR Swamp", level=Ty3Level.SouthernRiversSwamp),
    "SR Swamp Orb 3": LocData(0x4313, "Pippy Beach", level=Ty3Level.SouthernRiversSwamp),
    "Kaka Boom Island Orb 3": LocData(0x4314, "Kaka Boom Island", level=Ty3Level.KakaboomIsland),
    "Kaka Boom Island Orb 4": LocData(0x4315, "Kaka Boom Island", level=Ty3Level.KakaboomIsland), #ultra
    "Gooboo Gully Orb 1": LocData(0x4316, "Gooboo Gully", level=Ty3Level.GoobooGully), #ultra
    "Gooboo Gully Orb 2": LocData(0x4317, "Gooboo Gully", level=Ty3Level.GoobooGully),
    "Gooboo Gully Orb 3": LocData(0x4318, "Gooboo Gully", level=Ty3Level.GoobooGully), #lash
    "Gooboo Gully Orb 4": LocData(0x4319, "Gooboo Gully", level=Ty3Level.GoobooGully), #ultra
    "Cinder Canyon Orb 4": LocData(0x431A, "Cinder Canyon", level=Ty3Level.CinderCanyon), #ultra
    "SR Desert Orb 1": LocData(0x431B, "SR Desert", level=Ty3Level.SouthernRiversDesert),
    "Razorback Stream Orb": LocData(0x431C, "Razorback Stream", level=Ty3Level.SouthernRiversDesert),
    "SR Desert Orb 2": LocData(0x431D, "SR Desert", level=Ty3Level.SouthernRiversDesert)
}


bilby_dict: Dict[str, LocData] = {
    "New Burramudgee Bilby 1": LocData(0x4100, "New Burramudgee", level=Ty3Level.NewBurramudgee),
    "New Burramudgee Bilby 2": LocData(0x4101, "New Burramudgee", level=Ty3Level.NewBurramudgee), #air
    "Cinder Canyon Bilby 1": LocData(0x4102, "Cinder Canyon", level=Ty3Level.CinderCanyon), #fire
    "Cinder Canyon Bilby 2": LocData(0x4103, "Cinder Canyon", level=Ty3Level.CinderCanyon), #warp
    "Winter Woods Bilby 1": LocData(0x4104, "Winter Woods", level=Ty3Level.WinterWoods),
    "Backwood Blizzard Bilby 1": LocData(0x4105, "Backwood Blizzard", level=Ty3Level.BackwoodBlizzard), #grav grenade or satellite strike
    "Backwood Blizzard Bilby 2": LocData(0x4106, "Backwood Blizzard", level=Ty3Level.BackwoodBlizzard), #grav grenade or satellite strike
    "Winter Woods Bilby 2": LocData(0x4107, "Winter Woods", level=Ty3Level.WinterWoods),
    "Dead Dingo Marsh Bilby 1": LocData(0x4108, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh), #lash
    "Dead Dingo Marsh Bilby 2": LocData(0x4109, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh),
    "Frozen Forest Bilby 1": LocData(0x410A, "Frozen Forest", level=Ty3Level.FrozenForest),
    "Frozen Forest Bilby 2": LocData(0x410B, "Frozen Forest", level=Ty3Level.FrozenForest), #grav grenade
    "Dead Dingo Marsh Bilby 3": LocData(0x410C, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh), # water stone
    "Cassopolis Bilby 1": LocData(0x410D, "Cassopolis", level=Ty3Level.Cassopolis),
    "Cassopolis Bilby 2": LocData(0x410E, "Cassopolis", level=Ty3Level.Cassopolis), #hardcore parkour
    "Mount Boom Basin Bilby 1": LocData(0x410F, "Mount Boom Basin", level=Ty3Level.MountBoomBasin),
    "Mount Boom Basin Bilby 2": LocData(0x4110, "Mount Boom Basin", level=Ty3Level.MountBoomBasin),
    "Mount Boom Basin Bilby 3": LocData(0x4111, "Mount Boom Basin", level=Ty3Level.MountBoomBasin),
    "Winter Woods Bilby 3": LocData(0x4112, "Winter Woods", level=Ty3Level.WinterWoods), #grav grenade
    "Kaka Boom Island Bilby 1": LocData(0x4113, "Kaka Boom Island", level=Ty3Level.KakaboomIsland),
    "Kaka Boom Island Bilby 2": LocData(0x4114, "Kaka Boom Island", level=Ty3Level.KakaboomIsland),
    "Kaka Boom Island Bilby 3": LocData(0x4115, "Kaka Boom Island", level=Ty3Level.KakaboomIsland), #earth
    "New Burramudgee Bilby 3": LocData(0x4116, "New Burramudgee", level=Ty3Level.NewBurramudgee),
    "SR Swamp Bilby 1": LocData(0x4117, "SR Swamp", level=Ty3Level.SouthernRiversSwamp), #lash
    "SR Swamp Bilby 2": LocData(0x4118, "Pippy Beach", level=Ty3Level.SouthernRiversSwamp),
    "SR Swamp Bilby 3": LocData(0x4119, "Pippy Beach", level=Ty3Level.SouthernRiversSwamp),
    "SR Swamp Bilby 4": LocData(0x411A, "SR Swamp - Duke", level=Ty3Level.SouthernRiversSwamp), #top of airship to KBI
    "Gooboo Gully Bilby 1": LocData(0x411B, "Gooboo Gully", level=Ty3Level.GoobooGully),
    "Gooboo Gully Bilby 2": LocData(0x411C, "Gooboo Gully", level=Ty3Level.GoobooGully),
    "Gooboo Gully Bilby 3": LocData(0x411D, "Gooboo Gully", level=Ty3Level.GoobooGully),
    "Backwood Blizzard Bilby 3": LocData(0x411E, "Backwood Blizzard", level=Ty3Level.BackwoodBlizzard),
    "Backwood Blizzard Bilby 4": LocData(0x411F, "Backwood Blizzard", level=Ty3Level.BackwoodBlizzard),
    "Cassopolis Bilby 3": LocData(0x4120, "Cassopolis", level=Ty3Level.Cassopolis),
    "Cinder Canyon Bilby 3": LocData(0x4121, "Cinder Canyon", level=Ty3Level.CinderCanyon),
    "Frozen Forest Bilby 3": LocData(0x4122, "Frozen Forest", level=Ty3Level.FrozenForest),
    "Razorback Stream Bilby": LocData(0x4123, "Razorback Stream", level=Ty3Level.SouthernRiversDesert), #Warp, possible without
    "SR Swamp Bilby 5": LocData(0x4124, "SR Swamp", level=Ty3Level.SouthernRiversSwamp),
    "SR Desert Bilby 1": LocData(0x4125, "SR Desert", level=Ty3Level.SouthernRiversDesert), #in building with final redback race mission
    "SR Desert Bilby 2": LocData(0x4126, "SR Desert", level=Ty3Level.SouthernRiversDesert),
    "Winter Woods Bilby 4": LocData(0x4127, "Winter Woods", level=Ty3Level.WinterWoods),
}


stone_dict: Dict[str, LocData] = {
    "Razorback Stream Stone 1": LocData(0x4600, "Razorback Stream", level=Ty3Level.SouthernRiversDesert), #fire in Rescue Julius Arena
    "Razorback Stream Stone 2": LocData(0x4601, "Razorback Stream", level=Ty3Level.SouthernRiversDesert), #water Rescue Julius reward
    "Dead Dingo Marsh Stone 1": LocData(0x4602, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh), #earth #ultra, lash
    "Dead Dingo Marsh Stone 2": LocData(0x4603, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh), #water from Steve
    "Winter Woods Stone 1": LocData(0x4604, "Winter Woods", level=Ty3Level.WinterWoods), #earth center lava tube #extreme
    "Kaka Boom Island Stone 1": LocData(0x4605, "Kaka Boom Island", level=Ty3Level.KakaboomIsland), #air above small island at end #3x magnet required
    "Kaka Boom Island Stone 2": LocData(0x4606, "Kaka Boom Island", level=Ty3Level.KakaboomIsland), #magnet underwater south shore
    "Kaka Boom Island Stone 3": LocData(0x4607, "Kaka Boom Island", level=Ty3Level.KakaboomIsland), #earth above lava floe at end #3x magnet required
    "SR Swamp Stone 1": LocData(0x4608, "SR Swamp", level=Ty3Level.SouthernRiversSwamp), #water platforming in Battle Arena Gamma
    "SR Swamp Stone 2": LocData(0x4609, "SR Swamp", level=Ty3Level.SouthernRiversSwamp), #air Battle Arena Gamma reward
    "Gooboo Gully Stone 1": LocData(0x460A, "Gooboo Gully", level=Ty3Level.GoobooGully), #fire behind orb 23
    "Gooboo Gully Stone 2": LocData(0x460B, "Gooboo Gully", level=Ty3Level.GoobooGully), #ultra behind timed gate at end
    "Gooboo Gully Stone 3": LocData(0x460C, "Gooboo Gully", level=Ty3Level.GoobooGully), #zoom behind timed gate at end
    "SR Swamp Stone 3": LocData(0x460D, "SR Swamp", level=Ty3Level.SouthernRiversSwamp), #fire behind wall in battle arena zeta
    "SR Swamp Stone 4": LocData(0x460E, "SR Swamp", level=Ty3Level.SouthernRiversSwamp), #shadow Battle Arena Zeta reward
    "Frozen Forest Stone 1": LocData(0x460F, "Frozen Forest", level=Ty3Level.FrozenForest), #shadow Ranger Endanger reward #grav grenade
    "Backwood Blizzard Stone 1": LocData(0x4610, "Backwood Blizzard", level=Ty3Level.BackwoodBlizzard), #fire from timed lava platform parkour
    "Backwood Blizzard Stone 2": LocData(0x4611, "Backwood Blizzard", level=Ty3Level.BackwoodBlizzard), #water on timed platforms
    "Razorback Stream Stone 3": LocData(0x4612, "Razorback Stream", level=Ty3Level.SouthernRiversDesert), #ultra The Big Race reward
    "SR Desert Stone 1": LocData(0x4613, "SR Desert", level=Ty3Level.SouthernRiversDesert), #fire Experi Mental Cart reward
    "SR Desert Stone 2": LocData(0x4614, "SR Desert", level=Ty3Level.SouthernRiversDesert), #ultra Respect Effect reward
    "SR Desert Stone 3": LocData(0x4615, "SR Desert - Duke", level=Ty3Level.SouthernRiversDesert), #fire All Your Base reward
    "SR Desert Stone 4": LocData(0x4616, "SR Desert - Duke", level=Ty3Level.SouthernRiversDesert), #zoom Forest Firepower reward
    "SR Swamp Stone 5": LocData(0x4617, "SR Swamp", level=Ty3Level.SouthernRiversSwamp), #earth Demolition Derby reward,
    "SR Swamp Stone 6": LocData(0x4618, "SR Swamp", level=Ty3Level.SouthernRiversSwamp), #earth Redback Stash reward
    "SR Swamp Stone 7": LocData(0x4619, "SR Swamp - Duke", level=Ty3Level.SouthernRiversSwamp), #ultra Aero Coast Guard reward
    "SR Swamp Stone 8": LocData(0x461A, "SR Swamp", level=Ty3Level.SouthernRiversSwamp), #shadow Dennis Dilemma reward
    "New Burramudgee Stone 1": LocData(0x461B, "New Burramudgee", level=Ty3Level.NewBurramudgee), #fire in rock wall by tree #earth
    "New Burramudgee Stone 2": LocData(0x461C, "New Burramudgee", level=Ty3Level.NewBurramudgee), #multi on ledge above trailer #3x magnet required
    "New Burramudgee Stone 3": LocData(0x461D, "New Burramudgee", level=Ty3Level.NewBurramudgee), #water on tree
    "Razorback Stream Stone 4": LocData(0x461E, "Razorback Stream", level=Ty3Level.SouthernRiversDesert), #fire from Steve #fire
    "SR Swamp Stone 9": LocData(0x461F, "Pippy Beach", level=Ty3Level.SouthernRiversSwamp), #ultra from Steve
    "SR Swamp Stone 10": LocData(0x4620, "SR Swamp", level=Ty3Level.SouthernRiversSwamp), #air behind breakable barriers next to Quinking
    "SR Swamp Stone 11": LocData(0x4621, "SR Swamp", level=Ty3Level.SouthernRiversSwamp), #warp in wooden maze
    "SR Swamp Stone 12": LocData(0x4622, "SR Swamp", level=Ty3Level.SouthernRiversSwamp), #magnet Platypus Cove crab parkour
    "SR Swamp Stone 13": LocData(0x4623, "SR Swamp", level=Ty3Level.SouthernRiversSwamp), #chrono southeast corner crab parkour
    "SR Swamp Stone 14": LocData(0x4624, "SR Swamp", level=Ty3Level.SouthernRiversSwamp), #multi in water outside cassopolis
    "Cinder Canyon Stone 1": LocData(0x4625, "Cinder Canyon", level=Ty3Level.CinderCanyon), #water turkey in Cinder Canyon that doesn't exist
    "Cinder Canyon Stone 2": LocData(0x4626, "Cinder Canyon", level=Ty3Level.CinderCanyon), #fire ledge after houses #3x magnet required
    "Cinder Canyon Stone 3": LocData(0x4627, "Cinder Canyon", level=Ty3Level.CinderCanyon), #fire behind rock wall at top of elevators
    "Mount Boom Basin Stone 1": LocData(0x4628, "Mount Boom Basin", level=Ty3Level.MountBoomBasin), #Warp from Steve
    "Mount Boom Basin Stone 2": LocData(0x4629, "Mount Boom Basin", level=Ty3Level.MountBoomBasin), #Chrono behind spiderwebs #flame, ultra
    "Mount Boom Basin Stone 3": LocData(0x462A, "Mount Boom Basin", level=Ty3Level.MountBoomBasin), #end of mount boom
    "Frozen Forest Stone 2": LocData(0x462B, "Frozen Forest", level=Ty3Level.FrozenForest), #magnet on ice blocks
    "Frozen Forest Stone 3": LocData(0x462C, "Frozen Forest", level=Ty3Level.FrozenForest), #water on middle platform #extreme
    "Winter Woods Stone 2": LocData(0x462D, "Winter Woods", level=Ty3Level.WinterWoods), #earth in lava tube #extreme
    "Winter Woods Stone 3": LocData(0x462E, "Winter Woods", level=Ty3Level.WinterWoods), #mega
    "Winter Woods Stone 4": LocData(0x462F, "Winter Woods", level=Ty3Level.WinterWoods), #Zoom in lava tube #extreme
    "Cassopolis Stone 1": LocData(0x4630, "Cassopolis", level=Ty3Level.Cassopolis), #ultra at end of lash portal parkour #lash
    "Cassopolis Stone 2": LocData(0x4631, "Cassopolis", level=Ty3Level.Cassopolis), #ultra
    "Cassopolis Stone 3": LocData(0x4632, "Cassopolis", level=Ty3Level.Cassopolis), #chrono at end of hardcore parkour
    "Backwood Blizzard Stone 3": LocData(0x4633, "Backwood Blizzard", level=Ty3Level.BackwoodBlizzard), #fire on fan platforms #extreme
    "SR Desert Stone 5": LocData(0x4634, "SR Desert", level=Ty3Level.SouthernRiversDesert), #water stone in near all your base inside pillar
    "SR Desert Stone 6": LocData(0x4635, "SR Desert", level=Ty3Level.SouthernRiversDesert), #water on purple platforms crab parkour
    "Razorback Stream Stone 5": LocData(0x4636, "Razorback Stream", level=Ty3Level.SouthernRiversDesert), #fire at Maurie's watering hole #ultra
    "Razorback Stream Stone 6": LocData(0x4637, "Razorback Stream", level=Ty3Level.SouthernRiversDesert), #grindrail multi #fire, air
    "Dead Dingo Marsh Stone 3": LocData(0x4638, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh), #water from Turkey
}


steve_dict: Dict[str, LocData] = {
    "Steve - New Burramudgee": LocData(0x4400, "New Burramudgee", level=Ty3Level.DeadDingoMarsh),
    "Steve - Kaka Boom Island": LocData(0x4401, "Kaka Boom Island", level=Ty3Level.KakaboomIsland), #Earth
    "Steve - Razorback Stream": LocData(0x4402, "Razorback Stream", level=Ty3Level.SouthernRiversDesert), #Fire
    "Steve - Mount Boom Basin": LocData(0x4403, "Mount Boom Basin", level=Ty3Level.MountBoomBasin),
    "Steve - Dead Dingo Marsh": LocData(0x4404, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh),
    "Steve - Pippy Beach": LocData(0x4405, "Pippy Beach", level=Ty3Level.SouthernRiversSwamp),
}


picture_frame_dict: Dict[str, LocData] = {
    "Dead Dingo Marsh Picture Frame 1": LocData(0x4200, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh), #ultra
    "Dead Dingo Marsh Picture Frame 2": LocData(0x4201, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh), #ultra, earth
    "Dead Dingo Marsh Picture Frame 3": LocData(0x4202, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh), #ultra, earth
    "Dead Dingo Marsh Picture Frame 4": LocData(0x4203, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh), #ultra, earth
    "Dead Dingo Marsh Picture Frame 5": LocData(0x4204, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh), #ultra, earth
    "Dead Dingo Marsh Picture Frame 6": LocData(0x4205, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh), #ultra, earth
    "Dead Dingo Marsh Picture Frame 7": LocData(0x4206, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh),
    "Dead Dingo Marsh Picture Frame 8": LocData(0x4207, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh), #Lash
    "Dead Dingo Marsh Picture Frame 9": LocData(0x4208, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh),
    "Dead Dingo Marsh Picture Frame 10": LocData(0x4209, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh),
    "Dead Dingo Marsh Picture Frame 11": LocData(0x420A, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh),
    "Cassopolis Picture Frame 1": LocData(0x420B, "Cassopolis", level=Ty3Level.Cassopolis), #earth
    "Cassopolis Picture Frame 2": LocData(0x420C, "Cassopolis", level=Ty3Level.Cassopolis),
    "Dead Dingo Marsh Picture Frame 12": LocData(0x420D, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh),
    "Dead Dingo Marsh Picture Frame 13": LocData(0x420E, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh),
    "Dead Dingo Marsh Picture Frame 14": LocData(0x420F, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh), #lash
    "Dead Dingo Marsh Picture Frame 15": LocData(0x4210, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh), #earth, zoom or mega, lash
    "Kaka Boom Island Picture Frame 1": LocData(0x4211, "Kaka Boom Island", level=Ty3Level.KakaboomIsland),
    "Kaka Boom Island Picture Frame 2": LocData(0x4212, "Kaka Boom Island", level=Ty3Level.KakaboomIsland),
    "Kaka Boom Island Picture Frame 3": LocData(0x4213, "Kaka Boom Island", level=Ty3Level.KakaboomIsland),
    "Kaka Boom Island Picture Frame 4": LocData(0x4214, "Kaka Boom Island", level=Ty3Level.KakaboomIsland),
    "Kaka Boom Island Picture Frame 5": LocData(0x4215, "Kaka Boom Island", level=Ty3Level.KakaboomIsland),
    "Kaka Boom Island Picture Frame 6": LocData(0x4216, "Kaka Boom Island", level=Ty3Level.KakaboomIsland),
    "Kaka Boom Island Picture Frame 7": LocData(0x4217, "Kaka Boom Island", level=Ty3Level.KakaboomIsland),
    "Kaka Boom Island Picture Frame 8": LocData(0x4218, "Kaka Boom Island", level=Ty3Level.KakaboomIsland),
    "Kaka Boom Island Picture Frame 9": LocData(0x4219, "Kaka Boom Island", level=Ty3Level.KakaboomIsland),
    "Kaka Boom Island Picture Frame 10": LocData(0x421A, "Kaka Boom Island", level=Ty3Level.KakaboomIsland), #ultra
    "Kaka Boom Island Picture Frame 11": LocData(0x421B, "Kaka Boom Island", level=Ty3Level.KakaboomIsland), #ultra
    "Kaka Boom Island Picture Frame 12": LocData(0x421C, "Kaka Boom Island", level=Ty3Level.KakaboomIsland), #ultra
    "Kaka Boom Island Picture Frame 13": LocData(0x421D, "Kaka Boom Island", level=Ty3Level.KakaboomIsland), #ultra
    "Kaka Boom Island Picture Frame 14": LocData(0x421E, "Kaka Boom Island", level=Ty3Level.KakaboomIsland), #ultra
    "Kaka Boom Island Picture Frame 15": LocData(0x421F, "Kaka Boom Island", level=Ty3Level.KakaboomIsland), #ultra
    "Winter Woods Picture Frame 1": LocData(0x4220, "Winter Woods", level=Ty3Level.WinterWoods), #grav grenade
    "Winter Woods Picture Frame 2": LocData(0x4221, "Winter Woods", level=Ty3Level.WinterWoods), #extreme
    "Winter Woods Picture Frame 3": LocData(0x4222, "Winter Woods", level=Ty3Level.WinterWoods), #extreme
    "Winter Woods Picture Frame 4": LocData(0x4223, "Winter Woods", level=Ty3Level.WinterWoods), #extreme
    "Winter Woods Picture Frame 5": LocData(0x4224, "Winter Woods", level=Ty3Level.WinterWoods), #extreme
    "Winter Woods Picture Frame 6": LocData(0x4225, "Winter Woods", level=Ty3Level.WinterWoods), #extreme
    "Winter Woods Picture Frame 7": LocData(0x4226, "Winter Woods", level=Ty3Level.WinterWoods), #extreme
    "Winter Woods Picture Frame 8": LocData(0x4227, "Winter Woods", level=Ty3Level.WinterWoods), #extreme
    "Winter Woods Picture Frame 9": LocData(0x4228, "Winter Woods", level=Ty3Level.WinterWoods), #extreme
    "Winter Woods Picture Frame 10": LocData(0x4229, "Winter Woods", level=Ty3Level.WinterWoods), #grav grenade
    "Gooboo Gully Picture Frame 1": LocData(0x422A, "Gooboo Gully", level=Ty3Level.GoobooGully),
    "Gooboo Gully Picture Frame 2": LocData(0x422B, "Gooboo Gully", level=Ty3Level.GoobooGully),
    "Gooboo Gully Picture Frame 3": LocData(0x422C, "Gooboo Gully", level=Ty3Level.GoobooGully),
    "Gooboo Gully Picture Frame 4": LocData(0x422D, "Gooboo Gully", level=Ty3Level.GoobooGully),
    "Gooboo Gully Picture Frame 5": LocData(0x422E, "Gooboo Gully", level=Ty3Level.GoobooGully),
    "Gooboo Gully Picture Frame 6": LocData(0x422F, "Gooboo Gully", level=Ty3Level.GoobooGully),
    "Gooboo Gully Picture Frame 7": LocData(0x4230, "Gooboo Gully", level=Ty3Level.GoobooGully),
    "Gooboo Gully Picture Frame 8": LocData(0x4231, "Gooboo Gully", level=Ty3Level.GoobooGully),
    "Gooboo Gully Picture Frame 9": LocData(0x4232, "Gooboo Gully", level=Ty3Level.GoobooGully),
    "Mount Boom Basin Picture Frame 1": LocData(0x4233, "Mount Boom Basin", level=Ty3Level.MountBoomBasin), #earth
    "Mount Boom Basin Picture Frame 2": LocData(0x4234, "Mount Boom Basin", level=Ty3Level.MountBoomBasin), #earth
    "Mount Boom Basin Picture Frame 3": LocData(0x4235, "Mount Boom Basin", level=Ty3Level.MountBoomBasin), #earth
    "Mount Boom Basin Picture Frame 4": LocData(0x4236, "Mount Boom Basin", level=Ty3Level.MountBoomBasin), #earth
    "Mount Boom Basin Picture Frame 5": LocData(0x4237, "Mount Boom Basin", level=Ty3Level.MountBoomBasin), #ultra
    "Mount Boom Basin Picture Frame 6": LocData(0x4238, "Mount Boom Basin", level=Ty3Level.MountBoomBasin), #ultra
    "Mount Boom Basin Picture Frame 7": LocData(0x4239, "Mount Boom Basin", level=Ty3Level.MountBoomBasin), #ultra
    "Mount Boom Basin Picture Frame 8": LocData(0x423A, "Mount Boom Basin", level=Ty3Level.MountBoomBasin), #ultra
    "Mount Boom Basin Picture Frame 9": LocData(0x423B, "Mount Boom Basin", level=Ty3Level.MountBoomBasin), #ultra
    "Mount Boom Basin Picture Frame 10": LocData(0x423C, "Mount Boom Basin", level=Ty3Level.MountBoomBasin), #ultra
    "Frozen Forest Picture Frame 1": LocData(0x423D, "Frozen Forest", level=Ty3Level.FrozenForest), #extreme
    "Frozen Forest Picture Frame 2": LocData(0x423E, "Frozen Forest", level=Ty3Level.FrozenForest), #extreme
    "Frozen Forest Picture Frame 3": LocData(0x423F, "Frozen Forest", level=Ty3Level.FrozenForest), #extreme
    "Frozen Forest Picture Frame 4": LocData(0x4240, "Frozen Forest", level=Ty3Level.FrozenForest), #extreme
    "Frozen Forest Picture Frame 5": LocData(0x4241, "Frozen Forest", level=Ty3Level.FrozenForest), #extreme
    "Cinder Canyon Picture Frame 1": LocData(0x4242, "Cinder Canyon", level=Ty3Level.CinderCanyon),
    "Cinder Canyon Picture Frame 2": LocData(0x4243, "Cinder Canyon", level=Ty3Level.CinderCanyon),
    "Cinder Canyon Picture Frame 3": LocData(0x4244, "Cinder Canyon", level=Ty3Level.CinderCanyon),
    "Cinder Canyon Picture Frame 4": LocData(0x4245, "Cinder Canyon", level=Ty3Level.CinderCanyon), #earth
    "Cinder Canyon Picture Frame 5": LocData(0x4246, "Cinder Canyon", level=Ty3Level.CinderCanyon), #earth
    "Cinder Canyon Picture Frame 6": LocData(0x4247, "Cinder Canyon", level=Ty3Level.CinderCanyon), #earth
    "Cinder Canyon Picture Frame 7": LocData(0x4248, "Cinder Canyon", level=Ty3Level.CinderCanyon), #earth
    "Cinder Canyon Picture Frame 8": LocData(0x4249, "Cinder Canyon", level=Ty3Level.CinderCanyon), #earth
    "Cinder Canyon Picture Frame 9": LocData(0x424A, "Cinder Canyon", level=Ty3Level.CinderCanyon),
    "Cinder Canyon Picture Frame 10": LocData(0x424B, "Cinder Canyon", level=Ty3Level.CinderCanyon),
    "Backwood Blizzard Picture Frame 1": LocData(0x424C, "Backwood Blizzard", level=Ty3Level.BackwoodBlizzard),
    "Backwood Blizzard Picture Frame 2": LocData(0x424D, "Backwood Blizzard", level=Ty3Level.BackwoodBlizzard),
    "Backwood Blizzard Picture Frame 3": LocData(0x424E, "Backwood Blizzard", level=Ty3Level.BackwoodBlizzard),
    "Backwood Blizzard Picture Frame 4": LocData(0x424F, "Backwood Blizzard", level=Ty3Level.BackwoodBlizzard),
    "Backwood Blizzard Picture Frame 5": LocData(0x4250, "Backwood Blizzard", level=Ty3Level.BackwoodBlizzard), #grav grenade shadow or satellite cannon extreme
    "Backwood Blizzard Picture Frame 6": LocData(0x4251, "Backwood Blizzard", level=Ty3Level.BackwoodBlizzard), #grav grenade shadow or satellite cannon extreme
    "SR Swamp Picture Frame 1": LocData(0x4252, "SR Swamp", level=Ty3Level.SouthernRiversSwamp),
    "SR Swamp Picture Frame 2": LocData(0x4253, "SR Swamp", level=Ty3Level.SouthernRiversSwamp),
    "SR Swamp Picture Frame 3": LocData(0x4254, "SR Swamp", level=Ty3Level.SouthernRiversSwamp),
    "SR Swamp Picture Frame 4": LocData(0x4255, "Pippy Beach", level=Ty3Level.SouthernRiversSwamp),
    "SR Swamp Picture Frame 5": LocData(0x4256, "SR Swamp", level=Ty3Level.SouthernRiversSwamp),
    "SR Swamp Picture Frame 6": LocData(0x4257, "Pippy Beach", level=Ty3Level.SouthernRiversSwamp),
    "SR Swamp Picture Frame 7": LocData(0x4258, "Pippy Beach", level=Ty3Level.SouthernRiversSwamp),
    "SR Swamp Picture Frame 8": LocData(0x4259, "Pippy Beach", level=Ty3Level.SouthernRiversSwamp),
    "SR Swamp Picture Frame 9": LocData(0x425A, "SR Swamp", level=Ty3Level.SouthernRiversSwamp),
    "SR Swamp Picture Frame 10": LocData(0x425B, "SR Swamp", level=Ty3Level.SouthernRiversSwamp),
    "SR Swamp Picture Frame 11": LocData(0x425C, "SR Swamp", level=Ty3Level.SouthernRiversSwamp),
    "SR Swamp Picture Frame 12": LocData(0x425D, "SR Swamp", level=Ty3Level.SouthernRiversSwamp),
    "SR Swamp Picture Frame 13": LocData(0x425E, "Pippy Beach", level=Ty3Level.SouthernRiversSwamp),
    "SR Swamp Picture Frame 14": LocData(0x425F, "SR Swamp", level=Ty3Level.SouthernRiversSwamp), #ultra
    "SR Swamp Picture Frame 15": LocData(0x4260, "SR Swamp", level=Ty3Level.SouthernRiversSwamp),
    "New Burramudgee Picture Frame 1": LocData(0x4261, "New Burramudgee", level=Ty3Level.NewBurramudgee),
    "New Burramudgee Picture Frame 2": LocData(0x4262, "New Burramudgee", level=Ty3Level.NewBurramudgee),
    "New Burramudgee Picture Frame 3": LocData(0x4263, "New Burramudgee", level=Ty3Level.NewBurramudgee),
    "New Burramudgee Picture Frame 4": LocData(0x4264, "New Burramudgee", level=Ty3Level.NewBurramudgee),
    "New Burramudgee Picture Frame 5": LocData(0x4265, "New Burramudgee", level=Ty3Level.NewBurramudgee),
    "New Burramudgee Picture Frame 6": LocData(0x4266, "New Burramudgee", level=Ty3Level.NewBurramudgee),
    "New Burramudgee Picture Frame 7": LocData(0x4267, "New Burramudgee", level=Ty3Level.NewBurramudgee), #Magnet x2
    "New Burramudgee Picture Frame 8": LocData(0x4268, "New Burramudgee", level=Ty3Level.NewBurramudgee), #Accessible in prologue
    "New Burramudgee Picture Frame 9": LocData(0x4269, "New Burramudgee", level=Ty3Level.NewBurramudgee),
    "New Burramudgee Picture Frame 10": LocData(0x426A, "New Burramudgee", level=Ty3Level.NewBurramudgee), #Accessible in prologue
    "Cassopolis Picture Frame 3": LocData(0x426B, "Cassopolis", level=Ty3Level.Cassopolis), #earth
    "Cassopolis Picture Frame 4": LocData(0x426C, "Cassopolis", level=Ty3Level.Cassopolis), #earth
    "Cassopolis Picture Frame 5": LocData(0x426D, "Cassopolis", level=Ty3Level.Cassopolis),
    "Cassopolis Picture Frame 6": LocData(0x426E, "Cassopolis", level=Ty3Level.Cassopolis), #earth, Lash
    "Cassopolis Picture Frame 7": LocData(0x426F, "Cassopolis", level=Ty3Level.Cassopolis), #earth
    "Cassopolis Picture Frame 8": LocData(0x4270, "Cassopolis", level=Ty3Level.Cassopolis), #hardcore parkour
    "Cassopolis Picture Frame 9": LocData(0x4271, "Cassopolis", level=Ty3Level.Cassopolis), #earth
    "Cassopolis Picture Frame 10": LocData(0x4272, "Cassopolis", level=Ty3Level.Cassopolis), #earth
    "Dead Dingo Marsh Picture Frame 16": LocData(0x4273, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh), #ultra
    "Dead Dingo Marsh Picture Frame 17": LocData(0x4274, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh), #ultra
    "Dead Dingo Marsh Picture Frame 18": LocData(0x4275, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh), #ultra
    "Dead Dingo Marsh Picture Frame 19": LocData(0x4276, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh), #ultra
    "Dead Dingo Marsh Picture Frame 20": LocData(0x4277, "Dead Dingo Marsh", level=Ty3Level.DeadDingoMarsh), #ultra
}


mission_dict: Dict[str, LocData] = {
    # Story
    "Save the Dreaming":       LocData(0x6d01, "The Dreaming", 1, "Story"), #prologue
    "Rescue the General":      LocData(0x6d02, "New Burramudgee - Prologue", 2, "Story", level=Ty3Level.NewBurramudgee), #prologue #save the dreaming
    "Brown Kiwi Down":         LocData(0x6d03, "Cinder Canyon", 3, "Story", level=Ty3Level.CinderCanyon), #rescue the general
    "Rescue Julius":           LocData(0x6d0a, "Razorback Stream", 10, "Story", level=Ty3Level.SouthernRiversDesert),  # rescue the general
    "Heinous Hexaquin":        LocData(0x6d0c, "SR Desert", 12, "Story", level=Ty3Level.SouthernRiversDesert), # 3 of experi mental cart, quinkan armada, egg hunt, all your base
    "Meet Shazza":             LocData(0x6d0d, "Dead Dingo Marsh", 13, "Story", level=Ty3Level.DeadDingoMarsh), # heinous hexaquin
    "Sea Change":              LocData(0x6d0e, "Kaka Boom Island", 14, "Story", level=Ty3Level.KakaboomIsland), # duke pippy beach #dennis dilemma, power struggle, aero coast guard
    "Battle Arena Gamma":      LocData(0x6d13, "SR Swamp", 19, "Story", level=Ty3Level.SouthernRiversSwamp), # dennis dilemma, power struggle, aero coast guard
    "The Search for Steve":    LocData(0x6d17, "Gooboo Gully", 23, "Story", level=Ty3Level.GoobooGully), # wrath of the dragonquin
    "Find the Shadowring":     LocData(0x6d18, "Mount Boom Basin", 24, "Story", level=Ty3Level.MountBoomBasin),  # SR desert duke, #respect effect, forest firepower
    "Battle Arena Zeta":       LocData(0x6d1a, "SR Swamp", 26, "Story", level=Ty3Level.SouthernRiversSwamp),  # find the shadowring
    "Go find Boss Cass":       LocData(0x6d46, "Cassopolis", 70, "Story", level=Ty3Level.Cassopolis), #meet shazza

    # Race
    "The Big Race":            LocData(0x6d05, "Razorback Stream", 5, "Race", level=Ty3Level.SouthernRiversDesert), #rescue the general
    "Experi Mental Cart":      LocData(0x6d06, "SR Desert", 6, "Race", level=Ty3Level.SouthernRiversDesert), #brown kiwi down, the big race, rescue julius
    "Demolition Derby":        LocData(0x6d10, "Pippy Beach", 16, "Race", level=Ty3Level.SouthernRiversSwamp),  # dennis dilemma, power struggle, aero coast guard
    "Dennis Dilemma":          LocData(0x6d0f, "SR Swamp", 15, "Race", level=Ty3Level.SouthernRiversSwamp),  # go find boss cass
    "Respect Effect":          LocData(0x6d1b, "SR Desert", 27, "Race", level=Ty3Level.SouthernRiversDesert),  # the search for steve
    "Redback Stash":           LocData(0x6d1c, "SR Swamp", 28, "Race", level=Ty3Level.SouthernRiversSwamp),  # find the shadowring

    # Bunyip
    "Quinkan Armada":          LocData(0x6d07, "Backwood Blizzard", 7, "Bunyip", level=Ty3Level.BackwoodBlizzard), # brown kiwi down, the big race, rescue julius
    "Egg Hunt":                LocData(0x6d08, "Backwood Blizzard", 8, "Bunyip", level=Ty3Level.BackwoodBlizzard), # satellite strike # quinkan armada, all your base
    "Power Struggle":          LocData(0x6d11, "Winter Woods", 17, "Bunyip", level=Ty3Level.WinterWoods),  # grav grenade, shadow beam #go find boss cass
    "Meltdown":                LocData(0x6d12, "Winter Woods", 18, "Bunyip", level=Ty3Level.WinterWoods),  # thermo cannon #sea change, power struggle
    "Ranger Endanger":         LocData(0x6d1d, "Frozen Forest", 29, "Bunyip", level=Ty3Level.FrozenForest),  # shadow beam #find the shadowring
    "Redback Rundown":         LocData(0x6d1e, "Frozen Forest", 30, "Bunyip", level=Ty3Level.FrozenForest),  # thermo cannon, satellite strike #find the shadowring, battle arena zeta, redback stash, ranger endanger #optional

    # Gunyip
    "All Your Base":           LocData(0x6d0b, "SR Desert - Duke", 11, "Gunyip", level=Ty3Level.SouthernRiversDesert), #gunyip #brown kiwi down, the big race, rescue julius
    "Aero Coast Guard":        LocData(0x6d15, "SR Swamp - Duke", 21, "Gunyip", level=Ty3Level.SouthernRiversSwamp), #gunyip #go find boss cass
    "Wrath of the Dragonquin": LocData(0x6d16, "SR Swamp - Duke", 22, "Gunyip", level=Ty3Level.SouthernRiversSwamp), #gunyip  #sea change, demolition derby, meltdown, battle arena gamma
    "Forest Firepower":        LocData(0x6d1f, "SR Desert - Duke", 31, "Gunyip", level=Ty3Level.SouthernRiversDesert), #gunyip #the search for steve
}


full_location_dict: Dict[str, LocData] = {
    **story_dict,
    **opal_shop_location_dict,
    **korb_shop_location_dict,
    **berry_shop_location_dict,
    **bilby_shop_location_dict,
    **gooboo_berry_dict,
    **kromium_orb_dict,
    **bilby_dict,
    **steve_dict,
    **stone_dict,
    **picture_frame_dict,
    **mission_dict
}


def get_location_groups() -> dict[str, set[str]]:
    location_groups = {
        "Gooboo Berry": set(name for name, data in gooboo_berry_dict.items() if data.level is not None),
        "Bilby": set(name for name, data in bilby_dict.items() if data.level is not None),
        "Mission": set(name for name, data in mission_dict.items() if data.level is not None),
        "Kromium Orb": set(name for name, data in kromium_orb_dict.items() if data.level is not None),
        "Steve": set(name for name, data in steve_dict.items() if data.level is not None),
        "Stone": set(name for name, data in stone_dict.items() if data.level is not None)
    }
    for loc_name, loc_data in full_location_dict.items():
        if loc_data.level is None:
            continue
        level_name = ty3_levels[loc_data.level]
        if loc_data.level not in location_groups:
            location_groups[level_name] = set()
        location_groups[level_name].add(loc_name)
    return location_groups


ty3_location_groups = get_location_groups()