from typing import ClassVar, Dict, Optional
from BaseClasses import Tutorial, Item, ItemClassification, CollectionState, Location
from Utils import visualize_regions
#from entrance_rando import disconnect_entrance_for_randomization, randomize_entrances
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
    The Evil Quinkan have invaded Ty's Australian outback, intent on destroying Ty and his friends. It's up to you to
    reunite Ty with the Bush Rescue Squad to battle the Quinkan -- and discover the evil force controlling them. This
    is Ty's most exciting and dangerous quest yet -- save Ty and his friends before it's too late!
    """
    game = "Ty the Tasmanian Tiger 3"
    web = Ty3Web()

    options_dataclass = Ty3Options

    options: Ty3Options

    topology_present = True

    option_groups = Ty3OptionGroups

    item_name_to_id: ClassVar[Dict[str, int]] = {item_name: item_data.code for item_name,
    item_data in full_item_dict.items()}

    location_name_to_id: ClassVar[Dict[str, int]] = {loc_name: loc_data.code for loc_name,
    loc_data in full_location_dict.items()}

    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)
        self.itempool = []
        self.locations = {}
        self.items = {}
        self.trap_weights = {}

        self.rang_prices = []
        self.cassopolis_prices = []
        self.map_prices = []
        self.bunyip_prices = []

        self.bilby_prices = []
        self.orb_prices = []
        self.berry_prices = []

    def generate_early(self) -> None:
        self.locations = create_ty3_locations(self)

        min_price, max_price = 1000, 3000
        if self.options.shop_difficulty.value == 1:
            min_price, max_price = 1000, 5000
        elif self.options.shop_difficulty.value == 2:
            min_price, max_price = 3000, 7000
        self.rang_prices = self.generate_shop(6,1000000,min_price, max_price)


        min_price, max_price = 3000, 10000
        if self.options.shop_difficulty.value == 1:
            min_price, max_price = 10000, 25000
        elif self.options.shop_difficulty.value == 2:
            min_price, max_price = 15000, 30000
        self.cassopolis_prices = self.generate_shop(11,1000000,min_price, max_price)

        min_price, max_price = 2000, 5000
        if self.options.shop_difficulty.value == 1:
            min_price, max_price = 5000, 10000
        elif self.options.shop_difficulty.value == 2:
            min_price, max_price = 10000, 15000
        self.bunyip_prices = self.generate_shop(6, 1000000, min_price, max_price)


        min_price, max_price = 1000, 4000
        if self.options.shop_difficulty.value == 1:
            min_price, max_price = 3000, 6000
        elif self.options.shop_difficulty.value == 2:
            min_price, max_price = 5000, 8000
        self.map_prices = self.generate_shop(5,1000000,min_price, max_price)


        min_price, max_price = 1, 3
        if self.options.shop_difficulty.value == 1:
            min_price, max_price = 3, 6
        elif self.options.shop_difficulty.value == 2:
            min_price, max_price = 6, 8
        self.bilby_prices = self.generate_shop(5,40,min_price, max_price)


        min_price, max_price = 1, 2
        if self.options.shop_difficulty.value == 1:
            min_price, max_price = 3, 4
        elif self.options.shop_difficulty.value == 2:
            min_price, max_price = 4, 5
        self.orb_prices = self.generate_shop(8,30, min_price, max_price)

        min_price, max_price = 1, 2
        if self.options.shop_difficulty.value == 1:
            min_price, max_price = 1, 2
        elif self.options.shop_difficulty.value == 2:
            min_price, max_price = 2, 3
        self.berry_prices = self.generate_shop(4,10, min_price, max_price)

    def create_regions(self):
        create_ty3_regions(self, self.locations)
        connect_ty3_regions(self)


    def connect_entrances(self) -> None:
        print("Connect Entrance")
        # result = randomize_entrances(self, True, {0: [0]})

    def create_item(self, item: str) -> Ty3Item:
        return Ty3Item(item, ItemClassification.useful, self.item_name_to_id[item], self.player)

    def create_items(self):
        create_ty3_items(self)

        self.push_precollected(Item("Burramudgee Town ParkingBay", ItemClassification.progression,
                                    self.item_name_to_id["Burramudgee Town ParkingBay"], self.player))

        self.push_precollected(Item("Boomerang", ItemClassification.progression,
                                        self.item_name_to_id["Boomerang"], self.player))


        if self.options.start_with_maps.value:
            self.push_precollected(Item("Missing Persons Map", ItemClassification.useful,
                                        self.item_name_to_id["Missing Persons Map"], self.player))
            self.push_precollected(Item("Cog Map", ItemClassification.useful,
                                        self.item_name_to_id["Cog Map"], self.player))
            self.push_precollected(Item("Mysterious Anomalies Map", ItemClassification.useful,
                                        self.item_name_to_id["Mysterious Anomalies Map"], self.player))

        if self.options.gate_unlock.value == 2:
            self.push_precollected(Item("Patchy Barriers", ItemClassification.progression,
                                        self.item_name_to_id["Patchy Barriers"], self.player))
            self.push_precollected(Item("Buster Barriers", ItemClassification.progression,
                                        self.item_name_to_id["Buster Barriers"], self.player))
            self.push_precollected(Item("Fluffy Barriers", ItemClassification.progression,
                                        self.item_name_to_id["Fluffy Barriers"], self.player))


    def set_rules(self):
        set_rules(self)

    def generate_output(self, output_directory: str):
        visualize_regions(self.multiworld.get_region("Menu", self.player), f"Player{self.player}.puml",
                          show_entrance_names=True,
                          regions_to_highlight=self.multiworld.get_all_state(self.player).reachable_regions[
                              self.player])

    def fill_slot_data(self) -> id:
        return {
            "ModVersion": "0.0.1",
            "Goal": self.options.goal.value,
            "MissionsToGoal": self.options.missions_for_goal.value,
            "GateUnlock": self.options.gate_unlock.value,
            "ShopDifficulty": self.options.shop_difficulty.value,
            "RangShopPrices": self.rang_prices,
            "CassopolisPrices": self.cassopolis_prices,
            "MapPrices": self.map_prices,
            "BunyipPrices": self.bunyip_prices,
            "BerryPrices": self.berry_prices,
            "BilbyPrices": self.bilby_prices,
            "OrbPrices": self.orb_prices,
            "ExtraBilbies": self.options.extra_bilbies.value,
            "ExtraOrbs": self.options.extra_orbs.value,
            "ExtraBerries": self.options.extra_berries.value,
            "ChecksRequireInfra": self.options.require_infra.value,
            "FrameSanity": self.options.frame_sanity.value,
            "SteveSanity": self.options.steve_sanity.value,
            "StoneSanity": self.options.stone_sanity.value,
            "DeathLink": self.options.death_link.value,
        }

    def generate_shop(self, item_count, total_currency, min_price, max_price):
        shop_prices = []

        remaining_currency = total_currency

        for i in range(item_count):
            items_left = item_count - i

            # Calculate the max possible price for this item so remaining items can still be at min_price
            max_affordable_price = min(max_price, remaining_currency - min_price * (items_left - 1))

            # If we can't afford even the min price, force remaining items to min price
            if max_affordable_price < min_price:

                shop_prices.extend([2] * items_left)
                break

            price = self.random.randint(min_price, max_affordable_price)
            shop_prices.append(price)
            remaining_currency -= price

        return shop_prices
