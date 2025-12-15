from typing import ClassVar, Dict, Optional
from BaseClasses import Tutorial, Item, ItemClassification, CollectionState, Location
from Utils import visualize_regions
from worlds.AutoWorld import WebWorld, World
from worlds.ty_the_tasmanian_tiger_3.Items import create_ty3_items, full_item_dict, Ty3Item, junk_weights
from worlds.ty_the_tasmanian_tiger_3.Locations import create_ty3_locations, full_location_dict
from worlds.ty_the_tasmanian_tiger_3.Options import Ty3OptionGroups, Ty3Options
from worlds.ty_the_tasmanian_tiger_3.Regions import create_ty3_regions, connect_ty3_regions
from worlds.ty_the_tasmanian_tiger_3.Rules import set_rules


class Ty3Web(WebWorld):
    theme = "jungle"

    setup_en = Tutorial(
        tutorial_name="Multiworld Setup Guide",
        description="A guide to setting up the Ty the Tasmanian Tiger 3 randomizer connected to an Archipelago Multiworld.",
        language="English",
        file_name="setup_en.md",
        link="setup/en",
        authors=["Dashieswag92, xMcacutt, Fyreday"]
    )
    tutorials = [setup_en]


class Ty3World(World):
    """
    The evil Quinkan have invaded Ty's Australian outback, intent on destroying Ty and his friends. It's up to you to
    reunite Ty with the Bush Rescue Squad to battle the Quinkan -- and discover the evil force controlling them. This
    is Ty's most exciting and dangerous quest yet -- save Ty and his friends before it's too late!
    """
    game = "Ty the Tasmanian Tiger 3"
    web = Ty3Web()

    options_dataclass = Ty3Options

    options: Ty3Options

    topology_present = True

    option_groups = Ty3OptionGroups

    item_name_to_id: ClassVar[Dict[str, int]] = \
        {item_name: item_data.code for item_name, item_data in full_item_dict.items()}

    location_name_to_id: ClassVar[Dict[str, int]] = \
        {loc_name: loc_data.code for loc_name, loc_data in full_location_dict.items()}


    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)
        self.itempool = []
        self.locations = {}
        self.items = {}
        self.trap_weights = {}

    def fill_slot_data(self) -> id:
        return {
            "ModVersion": "1.0.1",
            "StoryMissionsToGoal": self.options.story_missions_for_goal.value,
            "BunyipMissionsToGoal": self.options.bunyip_missions_for_goal.value,
            "GunyipMissionsToGoal": self.options.gunyip_missions_for_goal.value,
            "RaceMissionsToGoal": self.options.race_missions_for_goal.value,
            "DeathLink": self.options.death_link.value,
        }


    def generate_early(self):
        self.locations = create_ty3_locations(self)


    def create_regions(self):
        create_ty3_regions(self, self.locations)
        connect_ty3_regions(self)


    def create_item(self, item: str) -> Ty3Item:
        return Ty3Item(item, ItemClassification.useful, self.item_name_to_id[item], self.player)


    def create_items(self):
        create_ty3_items(self)

        if self.options.start_with_maps.value:
            self.push_precollected(
                Item("Missing Persons Map", ItemClassification.useful, self.item_name_to_id["Missing Persons Map"], self.player)
            )
            self.push_precollected(
                Item("Sekrit Map", ItemClassification.useful, self.item_name_to_id["Sekrit Map"], self.player)
            )
            self.push_precollected(
                Item("Shiny Thing Map", ItemClassification.useful, self.item_name_to_id["Shiny Thing Map"], self.player)
            )
            self.push_precollected(
                Item("Priceless Art Map", ItemClassification.useful, self.item_name_to_id["Priceless Art Map"], self.player)
            )
            self.push_precollected(
                Item("Forbidden Fruit Map", ItemClassification.useful, self.item_name_to_id["Forbidden Fruit Map"], self.player)
            )


    def set_rules(self):
        set_rules(self)


    def generate_output(self, output_directory: str):
        visualize_regions(self.multiworld.get_region("Menu", self.player), f"Player{self.player}.puml",
                          show_entrance_names=True,
                          regions_to_highlight=self.multiworld.get_all_state(self.player).reachable_regions[
                              self.player])