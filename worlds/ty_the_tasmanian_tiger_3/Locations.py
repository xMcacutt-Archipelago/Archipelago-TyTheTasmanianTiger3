from typing import NamedTuple, Optional, Dict

from BaseClasses import Location


class Ty3Location(Location):
    game: str = "Ty the Tasmanian Tiger 3"

class LocData(NamedTuple):
    code: Optional[int]
    region: Optional[str]
    id: Optional[int] = -1

def create_ty3_locations(world):
    all_locations = {** story_dict, **shop_location_dict, **gooboo_berry_dict,
                     **kromium_orb_dict, **bilby_dict, **mission_dict}
    all_locations.update(get_mission_complete_events(world))

    if world.options.stone_sanity.value:
        all_locations.update(stone_dict)
    if world.options.steve_sanity.value:
        all_locations.update(steve_dict)
    if world.options.frame_sanity.value:
        all_locations.update(picture_frame_dict)

    return all_locations

story_dict: Dict[str, LocData] = {
    "Bunyip Gauntlet": LocData(0x9000, "The Dreaming"),
    "Shadowring Piece 1": LocData(0x901, "Mount Boom Basin"),
    "Shadowring Piece 2": LocData(0x902, "Mount Boom Basin"),
    "Shadowring Piece 3": LocData(0x903, "Mount Boom Basin"),
    }
shop_location_dict: Dict[str, LocData] = {
    "Rang Shop 1": LocData(8, "New Burramudgee"), #water
    "Rang Shop 2": LocData(9, "New Burramudgee"), #duo chassis
    "Rang Shop 3": LocData(10, "New Burramudgee"), #fire
    "Rang Shop 4": LocData(11, "New Burramudgee"), #mega
    "Rang Shop 5": LocData(12, "New Burramudgee"), #ultra
    "Rang Shop 6": LocData(13, "New Burramudgee"), #lash chassis

    "Rang Shop Korb 1": LocData(14, "New Burramudgee"), #Original Ty Skin
    "Rang Shop Korb 2": LocData(15, "New Burramudgee"), #Sly Skin
    "Rang SHop Korb 3": LocData(16, "New Burramudgee"), #Team Krome Skin
    "Rang SHop Korb 4": LocData(17, "New Burramudgee"), #Commando Skin
    "Rang Shop Korb 5": LocData(18, "New Burramudgee"), #Zombie Skin
    "Rang Shop Korb 6": LocData(19, "New Burramudgee"), #Quinkan Skin
    "Rang Shop Korb 7": LocData(20, "New Burramudgee"), #Ridge Skin
    "Rang Shop Korb 8": LocData(21, "New Burramudgee"), #Ghost Tiger Skin

    "Cassopolis Rang Shop 1": LocData(22, "Cassopolis"), #air
    "Cassopolis Rang Shop 2": LocData(23, "Cassopolis"), #multi
    "Cassopolis Rang Shop 3": LocData(24, "Cassopolis"), #magnet
    "Cassopolis Rang Shop 4": LocData(25, "Cassopolis"), #zoom
    "Cassopolis Rang Shop 5": LocData(26, "Cassopolis"), #warp
    "Cassopolis Rang Shop 6": LocData(27, "Cassopolis"), #earth
    "Cassopolis Rang Shop 7": LocData(28, "Cassopolis"), #mega chassis
    "Cassopolis Rang Shop 8": LocData(29, "Cassopolis"), #chrono
    "Cassopolis Rang Shop 9": LocData(30, "Cassopolis"), #smash chassis
    "Cassopolis Rang Shop 10": LocData(31, "Cassopolis"), #ring chassis
    "Cassopolis Rang Shop 11": LocData(32, "Cassopolis"), #doom chassis
    "Naomi's Ice Cream Truck 1": LocData(74, "New Burramudgee"), #Shadow Beam
    "Naomi's Ice Cream Truck 2": LocData(75, "New Burramudgee"), #Grav Grenade
    "Naomi's Ice Cream Truck 3": LocData(76, "New Burramudgee"), #Satellite Strike
    "Naomi's Ice Cream Truck 4": LocData(77, "New Burramudgee"), #Thermo Cannon
    "Naomi's Ice Cream Truck 5": LocData(78, "New Burramudgee"), #Nucleon Shield
    "Naomi's Ice Cream Truck 6": LocData(79, "New Burramudgee"), #Orbidrills
    "Naomi's Ice Cream Truck Berry Blast 1": LocData(80, "New Burramudgee"), #Midnight Crab Skin
    "Naomi's Ice Cream Truck Berry Blast 2": LocData(81, "New Burramudgee"), #Crab Tank Crab Skin
    "Naomi's Ice Cream Truck Berry Blast 3": LocData(82, "New Burramudgee"), #White Knight Crab Skin
    "Naomi's Ice Cream Truck Berry Blast 4": LocData(83, "New Burramudgee"), #Mean Green Crab Skin
    "Naomi's Ice Cream Truck Bilby Banana Split 1": LocData(84, "New Burramudgee"), #Cammo Gunyip Skin
    "Naomi's Ice Cream Truck Bilby Banana Split 2": LocData(85, "New Burramudgee"), #Bush Rescue Gunyip Skin
    "Naomi's Ice Cream Truck Bilby Banana Split 3": LocData(86, "New Burramudgee"), #Nightmare Gunyip Skin
    "Naomi's Ice Cream Truck Bilby Banana Split 4": LocData(87, "New Burramudgee"), #Sky Force Gunyip Skin
    "Naomi's Ice Cream Truck Bilby Banana Split 5": LocData(88, "New Burramudgee"), #Spitfire Gunyip Skin
    "Parrotbeard's Shop - Bilby Map": LocData(89, "Pippy Beach"),
    "Parrotbeard's Shop - Kromium Orb Map": LocData(90, "Pippy Beach"),
    "Parrotbeard's Shop - Steve Map": LocData(91, "Pippy Beach"),
    "Parrotbeard's Shop - Picture Frame Map": LocData(92, "Pippy Beach"),
    "Parrotbeard's Shop - Gooboo Berry Map": LocData(93, "Pippy Beach"),

}

gooboo_berry_dict: Dict[str, LocData] = {
    "Gooboo Berry 1": LocData(0x4300, "Cinder Canyon"), #Earth
    "Gooboo Berry 2": LocData(0x4301, "SR Desert - Duke"), #Behind crabs at All Your Base airship
    "Gooboo Berry 3": LocData(0x4302, "Dead Dingo Marsh"), #Lash
    "Gooboo Berry 4": LocData(0x4303, "Mount Boom Basin"), #Flame, Lash
    "Gooboo Berry 5": LocData(0x4304, "New Burramudgee"),
    "Gooboo Berry 6": LocData(0x4305, "Kaka Boom Island"), #Earth
    "Gooboo Berry 7": LocData(0x4306, "SR Swamp"),
    "Gooboo Berry 8": LocData(0x4307, "Pippy Beach"),
    "Gooboo Berry 9": LocData(0x4308, "Cassopolis"),
    "Gooboo Berry 10": LocData(0x4309, "Gooboo Gully"),
}

kromium_orb_dict: Dict[str, LocData] = {
    "Kromium Orb 1": LocData(0x4B00, "Cinder Canyon"), #ultra
    "Kromium Orb 2": LocData(0x4B01, "Cinder Canyon"), #ultra
    "Kromium Orb 3": LocData(0x4B02, "Cinder Canyon"), #earth
    "Kromium Orb 4": LocData(0x4B03, "Mount Boom Basin"), #flame
    "Kromium Orb 5": LocData(0x4B04, "Dead Dingo Marsh"),
    "Kromium Orb 6": LocData(0x4B05, "Dead Dingo Marsh"), #earth, zoom/mega, lash
    "Kromium Orb 7": LocData(0x4B06, "Dead Dingo Marsh"), #ultra
    "Kromium Orb 8": LocData(0x4B07, "New Burramudgee"), #earth
    "Kromium Orb 9": LocData(0x4B08, "New Burramudgee"),
    "Kromium Orb 10": LocData(0x4B09, "Dead Dingo Marsh"), #ultra
    "Kromium Orb 11": LocData(0x4B0A, "Cassopolis"), #boost panel
    "Kromium Orb 12": LocData(0x4B0B, "Cassopolis"), #opened by hitting all 5 red buttons
    "Kromium Orb 13": LocData(0x4B0C, "Mount Boom Basin"),
    "Kromium Orb 14": LocData(0x4B0D, "Mount Boom Basin"), #earth
    "Kromium Orb 15": LocData(0x4B0E, "Mount Boom Basin"),
    "Kromium Orb 16": LocData(0x4B0F, "Kaka Boom Island"),
    "Kromium Orb 17": LocData(0x4B10, "Kaka Boom Island"),
    "Kromium Orb 18": LocData(0x4B11, "Pippy Beach"), #water
    "Kromium Orb 19": LocData(0x4B12, "SR Swamp"),
    "Kromium Orb 20": LocData(0x4B13, "Pippy Beach"),
    "Kromium Orb 21": LocData(0x4B14, "Kaka Boom Island"),
    "Kromium Orb 22": LocData(0x4B15, "Kaka Boom Island"), #ultra
    "Kromium Orb 23": LocData(0x4B16, "Gooboo Gully"), #ultra
    "Kromium Orb 24": LocData(0x4B17, "Gooboo Gully"),
    "Kromium Orb 25": LocData(0x4B18, "Gooboo Gully"), #lash
    "Kromium Orb 26": LocData(0x4B19, "Gooboo Gully"), #ultra
    "Kromium Orb 27": LocData(0x4B1A, "Cinder Canyon"), #ultra
    "Kromium Orb 28": LocData(0x4B1B, "SR Desert"),
    "Kromium Orb 29": LocData(0x4B1C, "Razorback Stream"),
    "Kromium Orb 30": LocData(0x4B1D, "SR Desert"),
}

bilby_dict: Dict[str, LocData] = {
    "Bilby 1": LocData(0x4200, "New Burramudgee"),
    "Bilby 2": LocData(0x4201, "New Burramudgee"), #air
    "Bilby 3": LocData(0x4202, "Cinder Canyon"), #fire
    "Bilby 4": LocData(0x4203, "Cinder Canyon"), #warp
    "Bilby 5": LocData(0x4204, "Winter Woods"),
    "Bilby 6": LocData(0x4205, "Backwood Blizzard"), #grav grenade or satellite strike
    "Bilby 7": LocData(0x4206, "Backwood Blizzard"), #grav grenade or satellite strike
    "Bilby 8": LocData(0x4207, "Winter Woods"),
    "Bilby 9": LocData(0x4208, "Dead Dingo Marsh"), #lash
    "Bilby 10": LocData(0x4209, "Dead Dingo Marsh"),
    "Bilby 11": LocData(0x420A, "Frozen Forests"),
    "Bilby 12": LocData(0x420B, "Frozen Forests"), #grav grenade
    "Bilby 13": LocData(0x420C, "Dead Dingo Marsh"),
    "Bilby 14": LocData(0x420D, "Cassopolis"),
    "Bilby 15": LocData(0x420E, "Cassopolis"), #hardcore parkour
    "Bilby 16": LocData(0x420F, "Mount Boom Basin"),
    "Bilby 17": LocData(0x4210, "Mount Boom Basin"),
    "Bilby 18": LocData(0x4211, "Mount Boom Basin"),
    "Bilby 19": LocData(0x4212, "Winter Woods"), #grav grenade
    "Bilby 20": LocData(0x4213, "Kaka Boom Island"),
    "Bilby 21": LocData(0x4214, "Kaka Boom Island"),
    "Bilby 22": LocData(0x4215, "Kaka Boom Island"), #earth
    "Bilby 23": LocData(0x4216, "New Burramudgee"),
    "Bilby 24": LocData(0x4217, "SR Swamp"), #lash
    "Bilby 25": LocData(0x4218, "Pippy Beach"),
    "Bilby 26": LocData(0x4219, "Pippy Beach"),
    "Bilby 27": LocData(0x421A, "Pippy Beach"), #top of airship to KBI
    "Bilby 28": LocData(0x421B, "Gooboo Gully"),
    "Bilby 29": LocData(0x421C, "Gooboo Gully"),
    "Bilby 30": LocData(0x421D, "Gooboo Gully"),
    "Bilby 31": LocData(0x421E, "Backwood Blizzard"),
    "Bilby 32": LocData(0x421F, "Backwood Blizzard"),
    "Bilby 33": LocData(0x4220, "Cassopolis"),
    "Bilby 34": LocData(0x4221, "Cinder Canyon"),
    "Bilby 35": LocData(0x4222, "Frozen Forests"),
    "Bilby 36": LocData(0x4223, "Razorback Stream"), #Warp, possible without
    "Bilby 37": LocData(0x4224, "SR Swamp"),
    "Bilby 38": LocData(0x4225, "SR Desert"), #in building with final redback race mission
    "Bilby 39": LocData(0x4225, "SR Desert"),
    "Bilby 40": LocData(0x4226, "Winter Woods"),
}


stone_dict: Dict[str, LocData] = {
    #"Stone 1": LocData(0x4600, "UNKNOWN"),
    "Stone 2": LocData(0x4601, "Razorback Stream"), #water Rescue Julius reward
    "Stone 3": LocData(0x4602, "Dead Dingo Marsh"), #earth #ultra, lash
    "Stone 4": LocData(0x4603, "Dead Dingo Marsh"), #water from Steve
    "Stone 5": LocData(0x4604, "Winter Woods"), #earth center lava tube #extreme
    "Stone 6": LocData(0x4605, "Kaka Boom Island"), #air above small island at end #3x magnet required
    "Stone 7": LocData(0x4606, "Kaka Boom Island"), #magnet underwater south shore
    "Stone 8": LocData(0x4607, "Kaka Boom Island"), #earth above lava floe at end #3x magnet required
    "Stone 9": LocData(0x4608, "SR Swamp"), #water platforming in Battle Arena Gamma
    "Stone 10": LocData(0x4609, "SR Swamp"), #air Battle Arena Gamma reward
    #"Stone 11": LocData(0x460A, "UNKNOWN"),
    "Stone 12": LocData(0x460B, "Gooboo Gully"), #ultra behind timed gate at end
    "Stone 13": LocData(0x460C, "Gooboo Gully"), #zoom behind timed gate at end
    #"Stone 14": LocData(0x460D, "UNKNOWN"),
    "Stone 15": LocData(0x460E, "SR Swamp"), #shadow Battle Arena Zeta reward
    "Stone 16": LocData(0x460F, "Frozen Forest"), #shadow Ranger Endanger reward #grav grenade
    "Stone 17": LocData(0x4610, "Backwood Blizzard"), #fire from timed lava platform parkour
    "Stone 18": LocData(0x4611, "Backwood Blizzard"), #water on timed platforms
    "Stone 19": LocData(0x4612, "Razorback Stream"), #ultra The Big Race reward
    "Stone 20": LocData(0x4613, "SR Desert"), #fire Experi Mental Cart reward
    "Stone 21": LocData(0x4614, "SR Desert"), #ultra Respect Effect reward
    "Stone 22": LocData(0x4615, "SR Desert - Duke"), #fire All Your Base reward
    "Stone 23": LocData(0x4616, "SR Desert - Duke"), #zoom Forest Firepower reward
    "Stone 24": LocData(0x4617, "SR Swamp"), #earth Demolition Derby reward,
    "Stone 25": LocData(0x4618, "SR Swamp"), #earth Redback Stash reward
    "Stone 26": LocData(0x4619, "SR Swamp - Duke"), #ultra Aero Coast Guard reward
    "Stone 27": LocData(0x461A, "SR Swamp"), #shadow Dennis Dilemma reward
    "Stone 28": LocData(0x461B, "New Burramudgee"), #fire in rock wall by tree #earth
    "Stone 29": LocData(0x461C, "New Burramudgee"), #multi on ledge above trailer #3x magnet required
    "Stone 30": LocData(0x461D, "New Burramudgee"), #water on tree
    "Stone 31": LocData(0x461E, "Razorback Stream"), #fire from Steve #fire
    "Stone 32": LocData(0x461F, "Pippy Beach"), #ultra from Steve
    "Stone 33": LocData(0x4620, "SR Swamps"), #air behind breakable barriers next to Quinking
    "Stone 34": LocData(0x4621, "SR Swamp"), #warp in wooden maze
    "Stone 35": LocData(0x4622, "SR Swamp"), #magnet Platypus Cove crab parkour
    "Stone 36": LocData(0x4623, "SR Swamp"), #chrono southeast corner crab parkour
    #"Stone 37": LocData(0x4624, "UNKNOWN"),
    #"Stone 38": LocData(0x4625, "UNKNOWN"), #water files indicate turkey in Cinder Canyon that doesn't exist
    "Stone 39": LocData(0x4626, "Cinder Canyon"), #fire ledge after houses #3x magnet required
    "Stone 40": LocData(0x4627, "Cinder Canyon"), #fire behind rock wall at top of elevators
    "Stone 41": LocData(0x4628, "Mount Boom Basin"), #Warp from Steve
    "Stone 42": LocData(0x4629, "Mount Boom Basin"), #Chrono behind spiderwebs #flame, ultra
    "Stone 43": LocData(0x462A, "Mount Boom Basin"), #end of mount boom
    "Stone 44": LocData(0x462B, "Frozen Forests"), #magnet on ice blocks
    "Stone 45": LocData(0x462C, "Frozen Forests"), #water on middle platform #extreme
    "Stone 46": LocData(0x462D, "Winter Woods"), #earth in lava tube #extreme
    "Stone 47": LocData(0x462E, "Winter Woods"), #mega
    "Stone 48": LocData(0x462F, "Winter Woods"), #Zoom in lava tube #extreme
    "Stone 49": LocData(0x4630, "Cassopolis"), #ultra at end of lash portal parkour #lash
    "Stone 50": LocData(0x4631, "Cassopolis"), #ultra
    "Stone 51": LocData(0x4632, "Cassopolis"), #chrono at end of hardcore parkour
    "Stone 52": LocData(0x4633, "Backwood Blizzard"), #fire on fan platforms #extreme
    #"Stone 53": LocData(0x4634, "UNKNOWN"),
    "Stone 54": LocData(0x4635, "SR Desert"), #water on purple platforms crab parkour
    "Stone 55": LocData(0x4636, "Razorback Stream"), #fire at Maurie's watering hole #ultra
    "Stone 56": LocData(0x4637, "Razorback Stream"), #grindrail multi #fire, air
    "Stone 57": LocData(0x4638, "Dead Dingo Marsh"), #water from Turkey
}

steve_dict: Dict[str, LocData] = {
    "Steve - New Burramudgee": LocData(0x5300, "New Burramudgee"),
    "Steve - Kaka Boom Island": LocData(0x5301, "Kaka Boom Island"), #Earth
    "Steve - Razorback Stream": LocData(0x5302, "SR Razorback Stream"), #Fire
    "Steve - Mount Boom Basin": LocData(0x5303, "Mount Boom Basin"),
    "Steve - Dead Dingo Marsh": LocData(0x5304, "Dead Dingo Marsh"),
    "Steve - Pippy Beach": LocData(0x5305, "SR Pippy Beach"),
}

picture_frame_dict: Dict[str, LocData] = {
    "Picture Frame 1": LocData(0x5000, "Dead Dingo Marsh"), #ultra
    "Picture Frame 2": LocData(0x5001, "Dead Dingo Marsh"), #ultra, earth
    "Picture Frame 3": LocData(0x5002, "Dead Dingo Marsh"), #ultra, earth
    "Picture Frame 4": LocData(0x5003, "Dead Dingo Marsh"), #ultra, earth
    "Picture Frame 5": LocData(0x5004, "Dead Dingo Marsh"), #ultra, earth
    "Picture Frame 6": LocData(0x5005, "Dead Dingo Marsh"), #ultra, earth
    "Picture Frame 7": LocData(0x5006, "Dead Dingo Marsh"),
    "Picture Frame 8": LocData(0x5007, "Dead Dingo Marsh"), #Lash
    "Picture Frame 9": LocData(0x5008, "Dead Dingo Marsh"),
    "Picture Frame 10": LocData(0x5009, "Dead Dingo Marsh"),
    "Picture Frame 11": LocData(0x500A, "Dead Dingo Marsh"),
    "Picture Frame 12": LocData(0x500B, "Cassopolis"), #earth
    "Picture Frame 13": LocData(0x500C, "Cassopolis"),
    "Picture Frame 14": LocData(0x500D, "Dead Dingo Marsh"),
    "Picture Frame 15": LocData(0x500E, "Dead Dingo Marsh"),
    "Picture Frame 16": LocData(0x500F, "Dead Dingo Marsh"), #lash
    "Picture Frame 17": LocData(0x5010, "Dead Dingo Marsh"), #earth, zoom or mega, lash
    "Picture Frame 18": LocData(0x5011, "Kaka Boom Island"),
    "Picture Frame 19": LocData(0x5012, "Kaka Boom Island"),
    "Picture Frame 20": LocData(0x5013, "Kaka Boom Island"),
    "Picture Frame 21": LocData(0x5014, "Kaka Boom Island"),
    "Picture Frame 22": LocData(0x5015, "Kaka Boom Island"),
    "Picture Frame 23": LocData(0x5016, "Kaka Boom Island"),
    "Picture Frame 24": LocData(0x5017, "Kaka Boom Island"),
    "Picture Frame 25": LocData(0x5018, "Kaka Boom Island"),
    "Picture Frame 26": LocData(0x5019, "Kaka Boom Island"),
    "Picture Frame 27": LocData(0x501A, "Kaka Boom Island"), #ultra
    "Picture Frame 28": LocData(0x501B, "Kaka Boom Island"), #ultra
    "Picture Frame 29": LocData(0x501C, "Kaka Boom Island"), #ultra
    "Picture Frame 30": LocData(0x501D, "Kaka Boom Island"), #ultra
    "Picture Frame 31": LocData(0x501E, "Kaka Boom Island"), #ultra
    "Picture Frame 32": LocData(0x501F, "Kaka Boom Island"), #ultra
    "Picture Frame 33": LocData(0x5020, "Winter Woods"), #grav grenade
    "Picture Frame 34": LocData(0x5021, "Winter Woods"), #extreme
    "Picture Frame 35": LocData(0x5022, "Winter Woods"), #extreme
    "Picture Frame 36": LocData(0x5023, "Winter Woods"), #extreme
    "Picture Frame 37": LocData(0x5024, "Winter Woods"), #extreme
    "Picture Frame 38": LocData(0x5025, "Winter Woods"), #extreme
    "Picture Frame 39": LocData(0x5026, "Winter Woods"), #extreme
    "Picture Frame 40": LocData(0x5027, "Winter Woods"), #extreme
    "Picture Frame 41": LocData(0x5028, "Winter Woods"), #extreme
    "Picture Frame 42": LocData(0x5029, "Winter Woods"), #grav grenade
    "Picture Frame 43": LocData(0x502A, "Gooboo Gully"),
    "Picture Frame 44": LocData(0x502B, "Gooboo Gully"),
    "Picture Frame 45": LocData(0x502C, "Gooboo Gully"),
    "Picture Frame 46": LocData(0x502D, "Gooboo Gully"),
    "Picture Frame 47": LocData(0x502E, "Gooboo Gully"),
    "Picture Frame 48": LocData(0x502F, "Gooboo Gully"),
    "Picture Frame 49": LocData(0x5030, "Gooboo Gully"),
    "Picture Frame 50": LocData(0x5031, "Gooboo Gully"),
    "Picture Frame 51": LocData(0x5032, "Gooboo Gully"),
    "Picture Frame 52": LocData(0x5033, "Mount Boom Basin"), #earth
    "Picture Frame 53": LocData(0x5034, "Mount Boom Basin"), #earth
    "Picture Frame 54": LocData(0x5035, "Mount Boom Basin"), #earth
    "Picture Frame 55": LocData(0x5036, "Mount Boom Basin"), #earth
    "Picture Frame 56": LocData(0x5037, "Mount Boom Basin"), #ultra
    "Picture Frame 57": LocData(0x5038, "Mount Boom Basin"), #ultra
    "Picture Frame 58": LocData(0x5039, "Mount Boom Basin"), #ultra
    "Picture Frame 59": LocData(0x503A, "Mount Boom Basin"), #ultra
    "Picture Frame 60": LocData(0x503B, "Mount Boom Basin"), #ultra
    "Picture Frame 61": LocData(0x503C, "Mount Boom Basin"), #ultra
    "Picture Frame 62": LocData(0x503D, "Frozen Forest"), #extreme
    "Picture Frame 63": LocData(0x503E, "Frozen Forest"), #extreme
    "Picture Frame 64": LocData(0x503F, "Frozen Forest"), #extreme
    "Picture Frame 65": LocData(0x5040, "Frozen Forest"), #extreme
    "Picture Frame 66": LocData(0x5041, "Frozen Forest"), #extreme
    "Picture Frame 67": LocData(0x5042, "Cinder Canyon"),
    "Picture Frame 68": LocData(0x5043, "Cinder Canyon"),
    "Picture Frame 69": LocData(0x5044, "Cinder Canyon"),
    "Picture Frame 70": LocData(0x5045, "Cinder Canyon"), #earth
    "Picture Frame 71": LocData(0x5046, "Cinder Canyon"), #earth
    "Picture Frame 72": LocData(0x5047, "Cinder Canyon"), #earth
    "Picture Frame 73": LocData(0x5048, "Cinder Canyon"), #earth
    "Picture Frame 74": LocData(0x5049, "Cinder Canyon"), #earth
    "Picture Frame 75": LocData(0x504A, "Cinder Canyon"),
    "Picture Frame 76": LocData(0x504B, "Cinder Canyon"),
    "Picture Frame 77": LocData(0x504C, "Backwood Blizzard"),
    "Picture Frame 78": LocData(0x504D, "Backwood Blizzard"),
    "Picture Frame 79": LocData(0x504E, "Backwood Blizzard"),
    "Picture Frame 80": LocData(0x504F, "Backwood Blizzard"),
    "Picture Frame 81": LocData(0x5050, "Backwood Blizzard"), #grav grenade shadow or satellite cannon extreme
    "Picture Frame 82": LocData(0x5051, "Backwood Blizzard"), #grav grenade shadow or satellite cannon extreme
    "Picture Frame 83": LocData(0x5052, "SR Swamp"),
    "Picture Frame 84": LocData(0x5053, "SR Swamp"),
    "Picture Frame 85": LocData(0x5054, "SR Swamp"),
    "Picture Frame 86": LocData(0x5055, "Pippy Beach"),
    "Picture Frame 87": LocData(0x5056, "SR Swamp"),
    "Picture Frame 88": LocData(0x5057, "Pippy Beach"),
    "Picture Frame 89": LocData(0x5058, "Pippy Beach"),
    "Picture Frame 90": LocData(0x5059, "Pippy Beach"),
    "Picture Frame 91": LocData(0x505A, "SR Swamp"),
    "Picture Frame 92": LocData(0x505B, "SR Swamp"),
    "Picture Frame 93": LocData(0x505C, "SR Swamp"),
    "Picture Frame 94": LocData(0x505D, "SR Swamp"),
    "Picture Frame 95": LocData(0x505E, "Pippy Beach"),
    "Picture Frame 96": LocData(0x505F, "SR Swamp"), #ultra
    "Picture Frame 97": LocData(0x5060, "SR Swamp"),
    "Picture Frame 98": LocData(0x5061, "New Burramudgee"),
    "Picture Frame 99": LocData(0x5062, "New Burramudgee"),
    "Picture Frame 100": LocData(0x5063, "New Burramudgee"),
    "Picture Frame 101": LocData(0x5064, "New Burramudgee"),
    "Picture Frame 102": LocData(0x5065, "New Burramudgee"),
    "Picture Frame 103": LocData(0x5066, "New Burramudgee"),
    "Picture Frame 104": LocData(0x5067, "New Burramudgee"), #Magnet x2
    "Picture Frame 105": LocData(0x5068, "New Burramudgee"), #Accessible in prologue
    "Picture Frame 106": LocData(0x5069, "New Burramudgee"),
    "Picture Frame 107": LocData(0x506A, "New Burramudgee"), #Accessible in prologue
    "Picture Frame 108": LocData(0x506B, "Cassopolis"), #earth
    "Picture Frame 109": LocData(0x506C, "Cassopolis"), #earth
    "Picture Frame 110": LocData(0x506D, "Cassopolis"),
    "Picture Frame 111": LocData(0x506E, "Cassopolis"), #earth, Lash
    "Picture Frame 112": LocData(0x506F, "Cassopolis"), #earth
    "Picture Frame 113": LocData(0x5070, "Cassopolis"), #hardcore parkour
    "Picture Frame 114": LocData(0x5071, "Cassopolis"), #earth
    "Picture Frame 115": LocData(0x5072, "Cassopolis"), #earth
    "Picture Frame 116": LocData(0x5073, "Dead Dingo Marsh"), #ultra
    "Picture Frame 117": LocData(0x5074, "Dead Dingo Marsh"), #ultra
    "Picture Frame 118": LocData(0x5075, "Dead Dingo Marsh"), #ultra
    "Picture Frame 119": LocData(0x5076, "Dead Dingo Marsh"), #ultra
    "Picture Frame 120": LocData(0x5077, "Dead Dingo Marsh"), #ultra
}

def get_mission_complete_events(world):
    complete_mission_dict = {}
    for name, loc_data in mission_dict.items():
        if loc_data.code is None:
            continue

        new_name = f"Complete {name}"
        new_ingame_id = loc_data.id + 100  # Add 100 to ingame ID

        complete_mission_dict[new_name] = LocData(None, loc_data.region, new_ingame_id)

    if world.options.gate_unlock.value == 0:
        complete_mission_dict["Heinous Hexaquin"] = LocData(None, "Hexaquin", 980)
    return complete_mission_dict

mission_dict: Dict[str, LocData] = {
    "Save the Dreaming": LocData(0x6d000001, "The Dreaming", 1), #prologue
    "Rescue the General": LocData(0x6d000002, "New Burramudgee - Prologue", 2), #prologue #save the dreaming
    "Brown Kiwi Down": LocData(0x6d000003, "Cinder Canyon", 3), #rescue the general
    "The Big Race": LocData(0x6d000005, "Razorback Stream", 5), #rescue the general
    "Experi Mental Cart": LocData(0x6d000006, "SR Desert", 6), #brown kiwi down, the big race, rescue julius
    "Quinkan Armada": LocData(0x6d000007, "Backwood Blizzard", 7), #brown kiwi down, the big race, rescue julius
    "Egg Hunt": LocData(0x6d00008, "Backwood Blizzard", 8), #satellite strike #quinkan armada, all your base
    "Rescue Julius": LocData(0x6d000009, "Razorback Stream", 10), #rescue the general
    "All Your Base": LocData(0x6d00000a, "SR Desert - Duke", 11), #gunyip #brown kiwi down, the big race, rescue julius
    "Heinous Hexaquin": LocData(0x6d00000b, "Hexaquin Arena", 12), #3 of experi mental cart, quinkan armada, egg hunt, all your base
    "Meet Shazza": LocData(0x6d00000c, "Dead Dingo Marsh", 13), #heinous hexaquin
    "Sea Change": LocData(0x6d00000d, "Kaka Boom Island", 14), #duke pippy beach #dennis dilemma, power struggle, aero coast guard
    "Dennis Dilemma": LocData(0x6d00000e, "SR Swamp", 15), #go find boss cass
    "Demolition Derby": LocData(0x6d00000f, "Pippy Beach", 16), #dennis dilemma, power struggle, aero coast guard
    "Power Struggle": LocData(0x6d000010, "Winter Woods", 17), #grav grenade, shadow beam #go find boss cass
    "Meltdown": LocData(0x6d000011, "Winter Woods", 18), #thermo cannon #sea change, power struggle
    "Battle Arena Gamma": LocData(0x6d000012, "SR Swamp", 19), #dennis dilemma, power struggle, aero coast guard
    "Aero Coast Guard": LocData(0x6d000014, "SR Swamp - Duke", 21), #gunyip #go find boss cass
    "Wrath of the Dragonquin": LocData(0x6d000015, "SR Swamp - Duke", 22), #gunyip  #sea change, demolition derby, meltdown, battle arena gamma
    "The Search for Steve": LocData(0x6d000018, "Gooboo Gully", 23), #wrath of the dragonquin
    "Find the Shadowring": LocData(0x6d000019, "Mount Boom Basin", 24), #SR desert duke, #respect effect, forest firepower
    "Battle Arena Zeta": LocData(0x6d00001b, "SR Swamp", 26), #find the shadowring
    "Respect Effect": LocData(0x6d00001c, "SR Desert", 27), #the search for steve
    "Redback Stash": LocData(0x6d00001d, "SR Swamp", 28), #find the shadowring
    "Ranger Endanger": LocData(0x6d00001e, "Frozen Forest", 29), #shadow beam #find the shadowring
    "Redback Rundown": LocData(0x6d00001f, "Frozen Forest", 30), #thermo cannon, satellite strike #find the shadowring, battle arena zeta, redback stash, ranger endanger #optional
    "Forest Firepower": LocData(0x6d000020, "SR Desert - Duke", 31), #gunyip #the search for steve
    "Quinking": LocData(0x6d000023, "Quinking", 34), #goal #battle arena zeta, redback stash, ranger endanger
    "Go find Boss Cass": LocData(0x6d000046, "Cassopolis", 70), #meet shazza
}

full_location_dict: Dict[str, LocData] = {** story_dict,
                                          **shop_location_dict,
                                          **gooboo_berry_dict,
                                          **kromium_orb_dict,
                                          **bilby_dict,
                                          **steve_dict,
                                          **stone_dict,
                                          **picture_frame_dict,
                                          **mission_dict,}