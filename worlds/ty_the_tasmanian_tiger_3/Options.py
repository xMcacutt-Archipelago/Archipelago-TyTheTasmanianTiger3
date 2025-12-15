from dataclasses import dataclass

from Options import Choice, Range, Toggle, DeathLink, DefaultOnToggle, OptionGroup, PerGameCommonOptions

class StoryMissionsForGoal(Range):
    """
    How many story missions (missions played as Ty) do you need to unlock the airship that leads to Quinking?
    """
    display_name = "Story Missions For Goal"
    range_start = 0
    range_end = 12
    default = 8

class BunyipMissionsForGoal(Range):
    """
    How many Bunyip missions do you need to unlock the airship that leads to Quinking?
    """
    display_name = "Bunyip Missions For Goal"
    range_start = 0
    range_end = 6
    default = 3

class GunyipMissionsForGoal(Range):
    """
    How many Gunyip missions do you need to unlock the airship that leads to Quinking?
    """
    display_name = "Gunyip Missions For Goal"
    range_start = 0
    range_end = 4
    default = 1

class RaceMissionsForGoal(Range):
    """
    How many race missions do you need to unlock the airship that leads to Quinking?
    """
    display_name = "Missions For Goal"
    range_start = 0
    range_end = 6
    default = 0

#class StartingLocation(Choice):
#    """
#    Determines whether you start the game in New Burramudgee after the prologue (after saving Dennis),
#    or if you are immediately transported to Cassopolis to begin your journey.
#    """
#    display_name = "Starting Location"
#    option_NewBurramudgee = 0
#    option_Cassopolis = 1
#    default = 0

class StartWithMaps(Toggle):
    """
    Determines if you begin with the collectible maps
    """
    display_name = "Start With Maps"

class ChecksRequireInfra(Toggle):
    """
    Determines whether the generator considers checks using invisible objects logically require an Ultra Stone

    This also affects Frame Sanity
    """
    display_name = "Checks Require Ultra"

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
        StoryMissionsForGoal,
        BunyipMissionsForGoal,
        GunyipMissionsForGoal,
        RaceMissionsForGoal,
        #StartingLocation
    ]),
    OptionGroup("General Options", [
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
    story_missions_for_goal: StoryMissionsForGoal
    bunyip_missions_for_goal: BunyipMissionsForGoal
    gunyip_missions_for_goal: GunyipMissionsForGoal
    race_missions_for_goal: RaceMissionsForGoal
    #starting_location: StartingLocation
    require_infra: ChecksRequireInfra
    start_with_maps: StartWithMaps
    frame_sanity: FrameSanity
    steve_sanity: SteveSanity
    stone_sanity: StoneSanity
    death_link: DeathLink