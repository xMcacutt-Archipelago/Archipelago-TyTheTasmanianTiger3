from dataclasses import dataclass

from Options import Choice, Range, Toggle, DeathLink, DefaultOnToggle, OptionGroup, PerGameCommonOptions

class Goal(Choice):
    """
    Determines the goal of the seed

    Quinking: Defeat the Quinking
    All Missions: Complete all missions (including defeat Quinking)
    """
    display_name = "Goal"
    option_final_battle = 0
    option_all_missions = 1
    default = 0

class TotalMissionsForGoal(Range):
    """
    How Many Missions do you need to unlock the area that leads to Quinking?
    """
    display_name = "Missions For Goal"
    range_start = 0
    range_end = 29
    default = 26

#class StartingLocation(Choice):
#    """
#    Determines whether you start the game in New Burramudgee after the prologue (after saving Dennis),
#    or if you are immediately transported to Cassopolis to begin your journey.
#    """
#    display_name = "Starting Location"
#    option_NewBurramudgee = 0
#    option_Cassopolis = 1
#    default = 0

class SouthernRiversGateUnlock(Choice):
    """
    When should the gate between Southern Rivers Desert and Swamp be unlocked? (this does not affect parking pads)
    Vanilla: When Hexaquin is defeated
    On Item Receive: Unlocks when you receive Southern Rivers Gate
    Open World: Southern Rivers is completely open
    """
    display_name = "Gate Unlock Conditions"
    option_vanilla = 0
    option_items = 1
    option_open_world = 2
    default = 0

class ShopPrices(Choice):
    """
    Determines how expensive the shops are
    """
    display_name = "Shop Prices"
    option_cheap = 0
    option_normal = 1
    option_expensive = 2
    default = 1

class ExtraBerries(Range):
    """
    Sets number of additional Gooboo Berries to add to the pool
    """
    display_name = "Extra Berries"
    range_start = 0
    range_end = 10
    default = 5

class ExtraBilbies(Range):
    """
    Sets number of additional Bilbies to add to the pool
    """
    display_name = "Extra Bilbies"
    range_start = 0
    range_end = 20
    default = 10

class ExtraOrbs(Range):
    """
    Sets number of additional Kromium Orbs to add to the pool
    """
    display_name = "Extra Orbs"
    range_start = 0
    range_end = 20
    default = 10

class StartWithMaps(Toggle):
    """
    Determines if you begin with the collectible maps
    """
    display_name = "Start With Maps"

class ChecksRequireInfra(Toggle):
    """
    Determines whether the generator considers checks using invisible objects logically require the Infrarang

    This also affects Frame Sanity
    """
    display_name = "Frames Require Infra"

class FrameSanity(Toggle):
    """
    Determines if collecting Picture Frames grants checks
    """
    display_name = "Frame Sanity"

class SteveSanity(Toggle):
    """
    Determines if talking to Steve grants checks
    """
    display_name = "Steve Sanity"

class StoneSanity(Toggle):
    """
    Determines if finding Rang Stones grants checks
    """
    display_name = "Stone Sanity"


# class TrapFill(Range):
#     """
#     Determines the percentage of the junk fill which is filled with traps.
#     """
#     display_name = "Trap Fill Percentage"
#     range_start = 0
#     range_end = 100
#     default = 0
#
# class GravityTrapWeight(Range):
#     """The weight of Gravity Traps in the trap pool.
#     Gravity Traps cause Ty to fall much faster, and limit his jump height."""
#     display_name = "Gravity Trap Weight"
#     range_start = 0
#     range_end = 100
#     default = 20
#
#
# class KnockedDownTrapWeight(Range):
#     """The weight of Knocked Down Traps in the trap pool.
#     Knocked Down Traps knock you over and set your health to 1"""
#     display_name = "Knocked Down Trap Weight"
#     range_start = 0
#     range_end = 100
#     default = 20
#
#
# class SlowTrapWeight(Range):
#     """The weight of Slow Traps in the trap pool.
#     Slow Traps cause Ty to move slower."""
#     display_name = "Slow Trap Weight"
#     range_start = 0
#     range_end = 100
#     default = 20

@dataclass
class Ty3OptionGroups(PerGameCommonOptions):
    OptionGroup("Goal Options", [
        Goal,
        TotalMissionsForGoal,
        #StartingLocation
        SouthernRiversGateUnlock,
    ]),
    OptionGroup("General Options", [
        ShopPrices,
        ExtraBerries,
        ExtraBilbies,
        ExtraOrbs,
        ChecksRequireInfra,
        StartWithMaps
    ]),
    OptionGroup("Sanity Options", [
        FrameSanity,
        SteveSanity,
        StoneSanity
    ]),
    # OptionGroup("Traps", [
    # ]),
    OptionGroup("Death Link", [
        DeathLink
    ])

@dataclass
class Ty3Options(PerGameCommonOptions):
    goal: Goal
    missions_for_goal: TotalMissionsForGoal
    #starting_location: StartingLocation
    gate_unlock: SouthernRiversGateUnlock
    shop_difficulty: ShopPrices
    extra_berries: ExtraBerries
    extra_bilbies: ExtraBilbies
    extra_orbs: ExtraOrbs
    require_infra: ChecksRequireInfra
    start_with_maps: StartWithMaps

    frame_sanity: FrameSanity
    steve_sanity: SteveSanity
    stone_sanity: StoneSanity

    death_link: DeathLink