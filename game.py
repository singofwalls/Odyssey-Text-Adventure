"""
Start the actual Game
"""
import time
import random

from functools import reduce

from core.configs import get_value
from core.display import Text
from core.files import get_files
from core.save import get_saves_path, save_to_file, load_from_file
from core.tools import weighted_choice, cap_all_words
from game_objects import dict_to_attack, LOCATIONS_LIST, WEAPONS_LIST, EVERYTHING_LIST, all_attacks, NPC, \
    ambrosia, starting_health, treasure, cerastes, gold_ingot, spartae, minotaur,\
    bestiary, anthology, cook_book, finely_cooked_meal, cooked_meal, mead, atlas, monks_dogs, dagger, hrunting, \
    hrothgars_gift, grendel, adamantine_blade \

# TODO: Store lines out of screen past configurable char limit in variables

header_color = get_value("customization", "header_color")
header_size = get_value("customization", "header_size")
number_color = get_value("customization", "number_color")
prompt_color = get_value("customization", "prompt_color")
input_color = get_value("customization", "input_color")

path_font_size = get_value("customization", "path_font_size")
path_font = get_value("customization", "path_font")
choice_font = get_value("customization", "choice_font")
choice_font_size = get_value("customization", "choice_font_size")

location_color = get_value("game_customization", "location_color")
weapon_color = get_value("game_customization", "weapon_color")
attack_color = get_value("game_customization", "attack_color")
inventory_color = get_value("game_customization", "inventory_color")
npc_color = get_value("game_customization", "npc_color")
dead_font = get_value("game_customization", "dead_font")
dead_font_size = get_value("game_customization", "dead_font_size")
dead_color = get_value("game_customization", "dead_color")
default_color = get_value("display", "default_color")
multiattack_color = get_value("game_customization", "multiattack_color")
cooldown_color = get_value("game_customization", "cooldown_color")
self_color = get_value("game_customization", "self_color")
treasure_color = get_value("game_customization", "treasure_color")

starting_health = get_value("game_objects", "starting_health")

extension = get_value("save", "extension")

tutorials = get_value("tutorials")


# Game Object Classes

class GameAction(object):
    """Stores object traits

    :type text_list: None | list[Text] | str
    """

    def __init__(self, text_list=None):
        if isinstance(text_list, str):
            text_list = [Text(text_list)]
        self.text_list = text_list

    def clear_font(self):
        for text in self.text_list:
            text.clear_font()

    def set_text(self, text):
        old_text = self.get_text_object()
        old_text.set_text(text)
        old_text.update_whole()
        self.text_list = [old_text]

    def set_text_list(self, text_list):
        self.text_list = text_list

    def get_text_string(self):
        """Returns entire text list as a single string"""
        if isinstance(self.text_list, type(None)):
            raise Exception("Text should not be None")
        string = ""
        for text in self.text_list:
            string += text.get_whole()
        return string

    def get_text_object(self):
        """Returns Text object with intact attributes and all text from list"""
        if isinstance(self.text_list, type(None)):
            raise Exception("Text should not be None")
        string = ""
        for text in self.text_list:
            string += text.get_text()
        text_object = self.text_list[0].copy(True)
        text_object.set_text(string)
        return text_object

    def get_text_list(self):
        text_list = []
        for text in self.text_list:
            text_list.append(text.copy(True))
        return text_list


class GameObject(GameAction):
    """Stores information related to in-game actions

    :type text_list: None | list[Text] | str
    :type _actions: list[GameAction]
    :type _objects: list[GameObjects]
    """

    def __init__(self, text_list=None, _objects=None, _actions=None,
                 attributes=None):
        GameAction.__init__(self, text_list)
        self.contained_objects = _objects
        self.contained_actions = _actions
        if isinstance(self.contained_objects, type(None)):
            self.contained_objects = []
        if isinstance(self.contained_actions, type(None)):
            self.contained_actions = []

        if isinstance(attributes, type(None)):
            self.attributes = {}
        else:
            self.attributes = attributes
        self.tooltip = self.get_tooltip()

    def clear_font(self):
        GameAction.clear_font(self)
        for _object in self.contained_objects:
            _object.clear_font()
        for _object in self.contained_actions:
            _object.clear_font()

    def copy(self):
        new_obj = GameObject(self.text_list, self.contained_objects,
                             self.contained_actions, self.attributes)
        return new_obj

    def show_attacks_desc(self):
        if not isinstance(self.text_list, type(None)):
            for text in self.text_list:
                text.set_tooltip(self.tooltip)

    def hide_attacks_desc(self):
        if not isinstance(self.text_list, type(None)):
            self.tooltip = self.get_tooltip()
            for text in self.text_list:
                text.set_tooltip([self.get_tooltip()[0]])

    def update_tooltip(self):
        """Adds objects and actions to the tooltip"""

        for text in self.text_list:
            text.tooltip.append(Text("", None, new_line=True))
            text.tooltip.append(Text("", None, new_line=True))

            text.tooltip.append(
                Text("Objects:", None, new_line=True, color=header_color,
                     bold=True))
            for _object in self.contained_objects:
                text.tooltip.append(_object.get_text_list()[0])
                text.tooltip.append(Text(" "))

            text.tooltip.append(Text("", None, new_line=True))
            text.tooltip.append(Text("", None, new_line=True))

            text.tooltip.append(
                Text("Actions:", None, new_line=True, color=header_color,
                     bold=True))
            for action in self.contained_actions:
                text.tooltip.append(action.get_text_list()[0])
                text.tooltip.append(Text(" "))

    def set_tooltip(self, tooltip):
        for text in self.text_list:
            text.tooltip = tooltip

    def get_tooltip(self):
        for text in self.text_list:
            if not isinstance(text.tooltip, type(None)):
                return text.tooltip

    def add_action(self, action):
        self.contained_actions.append(action)

    def set_actions(self, actions):
        self.contained_actions = actions

    def clear_actions(self):
        self.contained_actions = []

    def get_actions(self):
        return self.contained_actions

    def add_object(self, _object):
        self.contained_objects.append(_object)

    def remove_object(self, _object):
        self.contained_objects.remove(_object)

    def remove_action(self, _action):
        self.contained_actions.remove(_action)

    def add_objects(self, _objects):
        for _object in _objects:
            self.contained_objects.append(_object)

    def clear_objects(self):
        self.contained_objects = []

    def get_objects(self):
        return self.contained_objects

    def get_object_names(self):
        names = []
        for _object in self.contained_objects:
            names.append(_object.get_text_string())
        return names

    def get_action_names(self):
        names = []
        for _action in self.contained_actions:
            names.append(_action.get_text_string())
        return names

    def find_object(self, _name):
        for _object in self.contained_objects:
            if _object.get_text_string().strip() == _name:
                return _object

    def find_action(self, _name):
        for _action in self.contained_actions:
            if _action.get_text_string().strip() == _name:
                return _action

    def add_attribute(self, key, value):
        self.attributes[key] = value

    def remove_attribute(self, key):
        self.attributes.pop(key)

    def get_attribute(self, key):
        return self.attributes[key]

    def get_attributes(self):
        return self.attributes


# Save Classes

class GameSave(object):
    """Stores all game values"""

    def __init__(self, name="", add_event=None):
        self.name = name
        self.cryptic = False
        self.temp_cryptic = False
        self.camo = False
        self.camo_plus = False
        self.orpheus = False
        self.shield = False
        self.wolf = False
        self.fleece = False
        self.sack = False
        self.sleep = 0
        self.path = [
            GameObject([Text("Game", color=input_color)],
                       [
                           GameObject(
                               [Text("Inventory", color=inventory_color)]),
                           GameObject(
                               [Text("Surroundings", color=inventory_color)]),
                           GameObject(
                               [Text("Stats", color=inventory_color)],
                               attributes={
                                   "Character": NPC("yourself"),
                               },
                           ),
                           GameObject(
                               [Text("Attacks", color=inventory_color)],
                           ),
                       ]
                       )
        ]
        if isinstance(add_event, type(None)):
            raise Exception("Game Save object needs add_event")
        else:
            self.add_event = add_event
        self.path[0].find_object("Stats").add_object(
            GameObject([self.get_you_word(tooltip=[Text("")], strip=True)],
                       _actions=[GameAction([Text("Use")])]))
        self.update_weapons()
        self.update_attacks(True)
        # Equip first attack by default
        self.equip_default()
        self.current_objects = None  # For showing/hiding objects
        self.update_stats_tooltip()
        self.new_location = True
        self.name_nums = {}
        self.uniques = []

        self.boosts = []
        self.accurate = 0
        self.viewed_npc = None
        self.herot = False

        self.hotkey_action = None
        self.current_path = None

    def notify_switch(self):
        self.add_event([Text("Equipped attack not available, switched to ",
                             color=prompt_color), Text(
            game_save.get_equipped().get_attribute("Attack").name + ".",
            tooltip=game_save.get_equipped().get_attribute("Attack").gen_desc(),
            new_line=True)])

    def update_attacks(self, first=False):
        """Clears actions and adds starting actions"""
        self.path[0].find_object("Attacks").clear_objects()
        current_attacks = []
        for attack in self.get_character().get_attacks():
            if attack.get_name() not in current_attacks:
                if attack.name not in current_attacks:
                    if attack.current_cooldown > 0:
                        attack_color = cooldown_color
                    elif attack.current_cooldown < 0:
                        attack_color = multiattack_color
                    elif "Self" in attack.attributes:
                        attack_color = self_color
                    else:
                        attack_color = default_color
                    self.path[0].find_object("Attacks").add_object(GameObject(
                        [Text(attack.get_name(), tooltip=attack.gen_desc(
                            None, False), color=attack_color)],
                        _actions=[GameAction("Equip")],
                        attributes={"Attack": attack}))
                    current_attacks.append(attack.get_name())

        for weapon in self.path[0].find_object("Inventory").get_objects():
            for attack in weapon.get_attribute("Item").get_attacks():
                if "Cryptic" in attack.get_attributes() and not self.cryptic:
                    continue
                attack_name = weapon.get_attribute(
                    "Item").get_name() + ":" + attack.get_name()
                if attack_name not in current_attacks:
                    if attack.current_cooldown > 0:
                        attack_color = cooldown_color
                    elif attack.current_cooldown < 0:
                        attack_color = multiattack_color
                    elif "Self" in attack.attributes:
                        attack_color = self_color
                    else:
                        attack_color = default_color

                    flower = False
                    if "Flower" in weapon.get_attribute("Item"). \
                            get_attributes() and not self.cryptic:
                        flower = True

                    self.path[0].find_object("Attacks").add_object(GameObject(
                        [Text(attack_name, tooltip=attack.gen_desc(
                            weapon.get_attribute("Item"), False, flower=flower),
                              color=attack_color)],
                        _actions=[GameAction("Equip")],
                        attributes={"Attack": attack, "Weapon": weapon}))
                    current_attacks.append(attack_name)

        inv = list([weap.get_attribute("Item") for weap in
                    self.get_path()[0].find_object(
                        "Inventory").get_objects()])
        equipped = True
        if "Equipped" not in self.path[0].find_object(
                "Attacks").get_attributes():
            equipped = False
        found = True
        if equipped and "Weapon" in self.get_equipped().get_attributes():
            weapon = self.get_equipped().get_attribute("Weapon").get_attribute(
                "Item")
            attack = self.get_equipped().get_attribute("Attack")
            if weapon not in inv:  # If weapon is lost, set all identical weapons to same cooldown for continued multiuse
                found = False
                for weap in inv:  # Update all cooldowns of same weapons/attacks
                    if weap.get_name() == weapon.get_name():
                        found = True
                        for atta in weap.get_attacks():
                            if atta.get_name() == attack.get_name():
                                atta.current_cooldown = attack.current_cooldown
                        weapon = weap
                if found:
                    for atta_obj in self.get_path()[0].find_object(
                            "Attacks").get_objects():  # Find same weapon/attack to equip instead
                        temp_atta = atta_obj.get_attribute("Attack")
                        if temp_atta.get_name() == attack.get_name():
                            if "Weapon" in atta_obj.get_attributes():
                                if atta_obj.get_attribute(
                                        "Weapon").get_attribute(
                                    "Item").get_name() == weapon.get_name():
                                    # Same attack name, same weapon name
                                    if temp_atta != attack:
                                        # Different attack
                                        self.path[0].find_object(
                                            "Attacks").add_attribute("Equipped",
                                                                     atta_obj)
                                        self.update_attacks_tooltip()
                                        break

        if not equipped or not found:

            self.equip_default()
            if not first:
                self.open_path()
                self.notify_switch()
                return True
        return False

    def open_path(self, pth="Attacks"):
        # pth = cap_all_words(pth, [">", "-", ":"])
        if pth == "Game":
            self.set_path_index(0)
        elif pth == "Back":
            if len(self.get_path()) > 1:
                self.remove_path_index(-1)
        else:
            self.set_path_index(0)
            for step in pth.split(">"):
                if step in self.get_path()[-1].get_object_names():
                    self.append_path(self.get_path()[-1].find_object(step))
                elif step in self.get_path()[-1].get_action_names():
                    return self.get_path()[-1].find_action(step)

    def update_attacks_tooltip(self):
        text_list = [Text("Equipped Attack", color=header_color,
                          font_size=header_size, new_line=True),
                     Text("", new_line=True)]
        attack = self.get_equipped().get_attribute("Attack")
        if "Weapon" in self.get_equipped().get_attributes():
            weapon = self.get_equipped().get_attribute("Weapon").get_attribute(
                "Item")
        else:
            weapon = None

        flower = False
        if not isinstance(weapon, type(None)):
            if "Flower" in weapon.get_attributes() and not self.cryptic:
                flower = True

        text_list += attack.gen_desc(weapon, flower=flower)
        self.get_path()[0].find_object("Attacks").set_tooltip(text_list)

    def rename_flowers(self):
        flowers = []

        for item in self.get_path()[0].find_object("Inventory").get_objects():
            flowers.append(item)

        for item in self.get_path()[0].find_object(
                "Surroundings").get_objects():
            flowers.append(item)

        for item in flowers:
            if "Item" in item.get_attributes():
                flower_item = item.get_attribute("Item")
                if "Flower" in flower_item.get_attributes():
                    if not self.cryptic:
                        new_name = flower_item.get_attributes()["Flower"]
                        if new_name != "Herb" and new_name != "Shirt-of-Nessus":
                            new_name += "-Flower"
                        item.hide_attacks_desc()
                    else:
                        new_name = flower_item.get_type()
                        item.show_attacks_desc()
                    flower_item.set_name(new_name)
                    item.set_text(new_name)

    def equip_default(self):
        self.path[0].find_object("Attacks").add_attribute(
            "Equipped", self.path[0].find_object(
                "Attacks").get_objects()[0])
        self.update_attacks_tooltip()

    def get_equipped(self):
        return self.get_path()[0].find_object("Attacks").get_attribute(
            "Equipped")

    def update_weapons(self):
        """Clears the inventory and adds starting weapons"""
        self.path[0].find_object("Inventory").clear_objects()
        for weapon in self.get_character().get_weapons():
            if "Treasure" in weapon.get_attributes():
                color = treasure_color
            else:
                color = weapon_color
            self.path[0].find_object("Inventory").add_object(GameObject(
                [Text(weapon.get_name(), color=color,
                      tooltip=weapon.gen_desc())], attributes={
                    "Item": weapon,
                }, _actions=[GameAction("Drop")]))

    def get_character(self):
        return self.path[0].find_object("Stats").get_attribute(
            "Character")

    def append_path(self, _object):
        self.path.append(_object)

    def remove_path_index(self, ind):
        self.path.pop(ind)

    def add_health_boost(self, healths, turns, name_word):
        """Additive effect"""
        self.boosts.append(
            {"Healths": healths, "Turns": turns, "Teller": name_word})
        self.boost_health(len(self.boosts) - 1, True)

    def add_attack_boost(self, attacks, turns, name_word):
        """Multiplicative effect"""
        self.boosts.append(
            {"Attacks": attacks, "Turns": turns, "Teller": name_word})

    def boost_health(self, ind, on=True):
        current_boost = self.boosts[ind]
        health = self.get_health().copy()
        for stat in current_boost["Healths"]:
            if stat not in health:
                health[stat] = 0
            if on:
                health[stat] += current_boost["Healths"][stat]
            else:
                health[stat] -= current_boost["Healths"][stat]
        self.set_health(health)

    def boost_attacks(self):
        attacks_dict = {}
        for attacks in list(filter(lambda x: "Attacks" in x, self.boosts)):
            for attack in attacks["Attacks"]:
                if attack not in attacks_dict:
                    attacks_dict[attack] = 0
                attacks_dict[attack] += attacks["Attacks"][attack]
        return attacks_dict

    def check_boosts(self):
        if self.accurate > 0:
            self.accurate -= 1
            if self.accurate == 0:
                self.add_event(
                    [Text("The effects of hearing ", color=prompt_color),
                     self.accurate_word,
                     Text("'s story have worn off.", color=prompt_color,
                          new_line=True)])
        ind = 0
        for boost in self.boosts:
            boost["Turns"] -= 1
            if boost["Turns"] <= 0:
                if "Healths" in boost:
                    self.boost_health(ind, False)
                self.add_event(
                    [Text("The effects of hearing ", color=prompt_color),
                     boost["Teller"],
                     Text("'s story have worn off.", color=prompt_color,
                          new_line=True)])
                self.boosts.pop(ind)
            ind += 1

    def canterbury(self, npc, treasures):
        name_parts = npc.get_name().split("-")
        if name_parts[-1].isnumeric():
            name_parts.pop()
        name = reduce(lambda x, y: x + "-" + y, name_parts)

        if not name == "The-Franklin":
            for item in treasures:
                npc.weapons.append(item.get_attribute("Item"))

        desc = None

        if name == "The-Knight":
            desc = "inspires you to persevere through pain."
            self.add_health_boost({"Sharp": 100000}, 30,
                                  npc.get_word(True, True))
        elif name == "The-Squire":
            desc = "inspires you to stay strong."
            self.add_health_boost({"Brute": 100000}, 30,
                                  npc.get_word(True, True))
        elif name == "The-Plowman":
            desc = "inspires you to be more righteous."
            self.add_health_boost({"Divinity": 100000}, 30,
                                  npc.get_word(True, True))
        elif name == "The-Reeve":
            desc = "inspires you to be quick on your feet."
            self.add_health_boost({"Agility": 100000}, 30,
                                  npc.get_word(True, True))
        elif name == "The-Franklin":
            desc = "inspires you to be friendlier."
            self.add_health_boost({"Charisma": 1}, 30,
                                  npc.get_word(True, True))
            self.add_event([npc.get_word(True, False),
                            Text("gave you back your payment.",
                                 color=prompt_color, new_line=True)])
            for _treasure in treasures:
                self.add_inv_item(_treasure)
        elif name == "The-Sailor":
            desc = "inspires you to be one with nature."
            self.add_attack_boost({"Tame": 2}, 30,
                                  npc.get_word(True, True))
            bestiary_word = Text(bestiary.get_name(), color=weapon_color,
                                 tooltip=bestiary.gen_desc())
            self.add_event(
                [npc.get_word(), Text("handed you a ", color=prompt_color),
                 bestiary_word, Text(".", color=prompt_color, new_line=True)])
            self.add_inv_item(GameObject([bestiary_word],
                                         attributes={"Item": bestiary}))
        elif name == "The-Parson":
            desc = "inspires you to spread the word of God."
            self.add_attack_boost({"Divinity": 2}, 30,
                                  npc.get_word(True, True))
        elif name == "The-Clerk":
            anthology_word = Text(anthology.get_name(), color=weapon_color,
                                  tooltip=anthology.gen_desc())
            self.add_event(
                [npc.get_word(), Text("handed you a ", color=prompt_color),
                 anthology_word, Text(".", color=prompt_color, new_line=True)])
            self.add_inv_item(GameObject([anthology_word],
                                         attributes={"Item": anthology}))
        elif name == "The-Cook":
            cook_word = Text(cook_book.get_name(), color=weapon_color,
                             tooltip=cook_book.gen_desc())
            self.add_event(
                [npc.get_word(), Text("handed you a ", color=prompt_color),
                 cook_word, Text(".", color=prompt_color, new_line=True)])
            self.add_inv_item(GameObject([cook_word],
                                         attributes={"Item": cook_book}))
        elif name == "The-Wife-of-Bath":
            atlas_word = Text(atlas.get_name(), color=weapon_color,
                              tooltip=atlas.gen_desc())
            self.add_event(
                [npc.get_word(), Text("handed you a ", color=prompt_color),
                 atlas_word, Text(".", color=prompt_color, new_line=True)])
            self.add_inv_item(GameObject([atlas_word],
                                         attributes={"Item": atlas}))
        elif name == "The-Yeoman":
            desc = "inspires you to focus in combat."
            self.accurate = 30
            self.accurate_word = npc.get_word(True, True)
        elif name == "The-Monk":
            game_save.gen_npc(monks_dogs)
            game_save.gen_npc(monks_dogs)
            self.add_event(
                [npc.get_word(True, True),
                 Text("'s dogs attack you while he tells you his story.",
                      color=prompt_color, new_line=True)])
        elif name == "The-Friar":
            health = self.get_health()
            health["Divine"] = 1
            self.set_health(health)
            self.add_event([npc.get_word(True),
                            Text("absolves your sins.", color=prompt_color,
                                 new_line=True)])
        elif name == "The-Merchant":
            success, items = self.get_payment(1, True)
            for item in items:
                npc.weapons.append(item.get_attribute("Item"))
        elif name == "The-Lawyer":
            success, items = self.get_payment(-1, True)
            for item in items:
                npc.weapons.append(item.get_attribute("Item"))

        if not isinstance(desc, type(None)):
            self.add_event([npc.get_word(True, True), Text("'s story ",
                                                           color=prompt_color),
                            Text(desc, color=prompt_color, new_line=True)])
        self.update_surroundings()

    def get_payment(self, num, trick=False):
        treasures = []
        treasure_words = []
        for _object in self.get_path()[0].find_object(
                "Inventory").get_objects():
            item = _object.get_attribute("Item")
            if "Treasure" in item.get_attributes():
                treasures.append(_object)
                treasure_words.append(
                    Text(item.get_name(), color=treasure_color,
                         tooltip=item.gen_desc()))
                if len(treasures) == num:
                    break
        if len(treasures) == num or num == -1:
            treasure_string = []
            i = 0
            for word in treasure_words:
                if i == 0:
                    treasure_string.append(word)
                elif i == len(treasure_words) - 1:
                    treasure_string.append(
                        Text(", and ", color=prompt_color))
                    treasure_string.append(word)
                else:
                    treasure_string.append(
                        Text(", ", color=prompt_color))
                    treasure_string.append(word)
                i += 1

            if trick:
                sentence = "He takes your "
            else:
                sentence = "You hand over "
            self.add_event(
                [Text(sentence, color=prompt_color),
                 *treasure_string,
                 Text(".", color=prompt_color,
                      new_line=True)])
            for item in treasures:
                self.remove_inv_item(item)

            return True, treasures
        else:
            if not trick:
                self.add_event([Text("You don't have enough treasure.",
                                     color=prompt_color, new_line=True)])
            return False, treasures

    def add_inv_item(self, item):
        self.path[0].find_object("Inventory").add_object(item)
        self.path[0].find_object("Inventory").get_objects()[-1].set_actions(
            [
                GameAction("Drop")])
        health = self.get_health()
        health["Agility"] -= 5
        self.set_health(health)  # Reduce agility

    def remove_inv_item(self, item):
        if item not in self.path[0].find_object("Inventory").get_objects():
            for _item in self.path[0].find_object(
                    "Inventory").get_objects():
                if item.get_text_string() == _item.get_text_string():
                    self.path[0].find_object("Inventory").remove_object(
                        _item)
                    break
        else:
            self.path[0].find_object("Inventory").remove_object(item)
        health = self.get_health()
        health["Agility"] += 5
        self.set_health(health)  # Increase agility

    def add_ground_item(self, item, npc=False):
        self.path[0].find_object("Surroundings").add_object(item)
        if not npc:
            self.path[0].find_object("Surroundings").get_objects()[
                -1].set_actions([GameAction("Pick-up")])

    def remove_ground_item(self, item):
        self.path[0].find_object("Surroundings").remove_object(item)

    def add_main_action(self, action):
        self.path[0].add_action(action)

    def clear_main_actions(self):
        self.path[0].clear_actions()

    def hide_objects(self):
        self.path[0].set_text_list([Text("Menu", color=input_color,
                                         font_size=path_font_size,
                                         font_name=path_font)])
        self.current_objects = self.path[-1].get_objects()[:]
        self.path[-1].clear_objects()

    def show_objects(self):
        self.path[0].set_text_list([Text("Game", color=input_color,
                                         font_size=path_font_size,
                                         font_name=path_font)])
        self.path[-1].add_objects(self.current_objects)
        self.current_objects = None

    def set_path_index(self, ind):
        self.path = self.path[:ind + 1]

    def get_path(self):
        return self.path

    def get_path_text_list(self, string=False):
        path_text_list = []
        for _object in self.get_path():
            if not string:
                path_obj = _object.get_text_object()
                path_obj.set_font(choice_font, choice_font_size)
                path_text_list.append(path_obj)
            else:
                path_text_list.append(_object.get_text_string())
            if type(_object) == GameObject:
                if not string:
                    path_text_list.append(Text(">", color=input_color,
                                               font_size=choice_font_size,
                                               font_name=choice_font))
                else:
                    path_text_list.append(">")
        if string:
            return "".join(path_text_list)
        return path_text_list

    def check_caught(self):
        """Check if cannot leave"""
        for npc in self.get_npcs():
            if npc.target == "You":
                if random.randint(0, npc.get_health()["Agility"]) > \
                        self.get_health()["Agility"]:
                    return npc  # You were caught
        return False

    def gen_location(self, location_name=None):
        """Chooses a random location to spawn in"""

        self.path[0].find_object("Surroundings").clear_objects()
        self.path[0].find_object("Surroundings").clear_actions()

        available_locations = list(filter(lambda
                                              x: x.get_name() != "Strange-Cavern" and x.get_name() != "Treasure-Hall",
                                          LOCATIONS_LIST))
        if "Grendel" in self.uniques:
            available_locations = list(
                filter(lambda x: x.get_name() != "Treasure-Hall",
                       LOCATIONS_LIST))
        if "Grendel's-Mother" in self.uniques:
            available_locations = LOCATIONS_LIST

        probabilities = [l.probability for l in available_locations]
        if isinstance(location_name, type(None)):
            location = weighted_choice(available_locations, probabilities)
        else:  # Given name, find location
            location = None
            for _location in available_locations:
                if _location.get_type() == location_name:
                    location = _location
                    break
        location.gen_name()
        self.path[0].find_object("Surroundings").add_attribute(
            "location", location)

        self.path[0].find_object("Surroundings").add_action(GameAction(
            "Leave-Location"))
        self.path[0].find_object("Surroundings").add_action(GameAction(
            "Wait"))
        self.path[0].find_object("Surroundings").set_tooltip(
            [Text("Location", color=header_color, bold=True, new_line=True,
                  font_size=header_size),
             Text(location.get_name(), new_line=True),
             Text("", new_line=True),
             *location.gen_desc()])
        # Gen items
        objects = []
        for _weapon in location.gen_objects(location.weapons):
            objects.append(GameObject([Text(_weapon.get_name(),
                                            color=weapon_color,
                                            tooltip=_weapon.gen_desc())],
                                      _actions=[GameAction("Pick-up")],
                                      attributes={"Item": _weapon}))

        tmax = location.treasure["Max"]
        tmin = location.treasure["Min"]
        tprob = location.treasure["Probability"]
        treasures = []
        if random.randint(0, 100) <= tprob:
            for i in range(0, random.randint(tmin, tmax)):
                treasure_item = treasure.copy(False)
                treasures.append(GameObject([Text(
                    treasure_item.get_name(), color=treasure_color,
                    tooltip=treasure_item.gen_desc())], _actions=[
                    GameAction("Pick-up")], attributes={"Treasure": True,
                                                        "Item": treasure_item}))

        self.gen_npcs()
        if location.get_name() == "Herot":
            if self.herot:
                self.gen_npc(grendel)
        self.path[0].find_object("Surroundings").add_objects(objects)
        self.path[0].find_object("Surroundings").add_objects(treasures)
        self.new_location = True
        self.rename_flowers()
        self.reset_cooldowns()

    def gen_npcs(self, wander=False):
        if not wander:
            self.name_nums = {}
        # Gen NPCs
        location = self.get_path()[0].find_object(
            "Surroundings").get_attribute("location")
        if "Boss" not in location.get_attributes():
            npc_amounts = {}
            for npc in self.get_npcs():
                if npc.get_type() not in npc_amounts:
                    npc_amounts[npc.get_type()] = 0
                npc_amounts[npc.get_type()] += 1
            npc_word_list = []
            for npc in location.gen_objects(location.npcs, wander,
                                            npc_amounts):
                if self.gen_npc(npc):
                    npc = self.get_path()[0].find_object(
                        "Surroundings").get_objects()[-1].get_attribute(
                        "NPC")
                    npc_word_list.append(npc.get_word())
            return npc_word_list
        else:
            # Only spawn one random creature
            npcs = location.gen_objects(location.npcs)
            living_npcs = []
            for npc in npcs:
                if "Unique" in npc.get_attributes():
                    if npc.get_type() in self.uniques:
                        # Already been killed
                        continue
                living_npcs.append(npc)
            while len(living_npcs) > 0:
                if self.gen_npc(random.choice(living_npcs)):
                    npc = self.get_path()[0].find_object(
                        "Surroundings").get_objects()[-1].get_attribute(
                        "NPC")
                    return [npc.get_word()]
        return []

    def gen_npc(self, _npc, new_name=True):
        """Creates an npc and adds to surroundings"""
        npc = _npc.copy()
        if npc.get_type() in self.uniques and new_name:
            return False
        if new_name:
            npc.gen_name(self.name_nums)
        else:
            npc.determine_number(self.name_nums)

        weapon_objects = []
        for _weapon in npc.get_weapons():
            if "Treasure" in _weapon.get_attributes():
                color = treasure_color
            else:
                color = weapon_color
            weapon_objects.append(GameObject([
                Text(_weapon.get_name(), color=color,
                     tooltip=_weapon.gen_desc())],
                attributes={"Item": _weapon}))

        actions = [GameAction("Attack")]
        if "Story-Teller" in npc.get_attributes():
            if isinstance(npc.target, type(None)):
                actions.append(GameAction([Text("Pay", color=treasure_color,
                                                new_line=True)]))
        if "Hrothgar" in npc.get_attributes() and isinstance(npc.target,
                                                             type(None)):
            actions.append(GameAction([Text("Talk", new_line=True)]))

        self.add_ground_item(
            GameObject([npc.get_word(False)], _actions=actions,
                       _objects=weapon_objects,
                       attributes={"NPC": npc}), npc=True)
        return True

    def get_npcs(self):
        """Returns NPCs in current surroundings"""
        npcs = []
        for _object in self.path[0].find_object(
                "Surroundings").get_objects():
            if "NPC" in _object.get_attributes():
                npcs.append(_object.get_attribute("NPC"))

        return npcs

    def get_health(self):
        """Return Health Stats of self"""
        return self.get_character().get_health()

    def set_health(self, stats):
        """Sets the health stats for self"""
        self.get_character().set_health(stats)
        self.update_stats_tooltip()

    def update_stats_tooltip(self):
        """Updates stats tooltip with current info"""
        desc = [Text("Health", color=header_color, bold=True,
                     new_line=True, font_size=header_size)]
        for stat in self.get_health():
            desc += [Text(stat + ": ", color=header_color),
                     Text(str(self.get_health()[stat]), new_line=True,
                          color=number_color)]
        self.path[0].find_object("Stats").set_tooltip(desc)
        self.path[0].find_object("Stats").find_object("You").set_tooltip(
            desc)

    def get_you_word(self, caps=True, tooltip=None, strip=False,
                     yourself=False):
        if caps:
            word = "You "
        else:
            word = "you "
        if yourself:
            word = "yourself"
        if strip:
            word = word.strip()
        if isinstance(tooltip, type(None)):
            tooltip = self.get_stats_tooltip()[:]
        return Text(word, tooltip=tooltip,
                    color=self_color)

    def get_stats_tooltip(self):
        return self.path[0].find_object("Stats").get_tooltip()

    def update_surroundings(self):
        self.viewed_npc = None
        if "NPC" in self.get_path()[-1].get_attributes():
            self.viewed_npc = self.get_path()[-1].get_attribute(
                "NPC").get_name()
        in_surroundings = False
        if self.path[-1] == self.path[0].find_object("Surroundings"):
            self.remove_path_index(-1)
            in_surroundings = True
        new_objects = []
        new_npcs = []
        for _object in self.path[0].find_object(
                "Surroundings").get_objects():
            if "NPC" not in _object.get_attributes():
                new_objects.append(_object)
            else:
                new_npcs.append(_object.get_attribute("NPC"))
        self.path[0].find_object("Surroundings").clear_objects()
        for npc in new_npcs:
            self.gen_npc(npc, new_name=False)
        self.path[0].find_object("Surroundings").add_objects(new_objects)
        if in_surroundings:
            self.open_path("Surroundings")
        if not isinstance(self.viewed_npc, type(None)):
            self.remove_path_index(-1)
            self.append_path(
                self.get_path()[0].find_object(
                    "Surroundings").find_object(self.viewed_npc))

    def reset_cooldowns(self):
        for attack in self.get_path()[0].find_object(
                "Attacks").get_objects():
            attack_item = attack.get_attribute("Attack")
            attack_item.reset_cooldown()

    def tick(self):
        for attack in self.get_path()[0].find_object(
                "Attacks").get_objects():
            attack_item = attack.get_attribute("Attack")
            if attack_item.tick():
                weapon = None
                flower = False
                if "Weapon" in attack.get_attributes():
                    weapon = attack.get_attribute("Weapon").get_attribute(
                        "Item")
                    if "Flower" in weapon.get_attributes() and not self.cryptic:
                        flower = True
                self.add_event([Text(attack.get_text_string() + " ",
                                     tooltip=attack_item.gen_desc(weapon,
                                                                  False,
                                                                  None,
                                                                  flower)),
                                Text("is ready to use.", color=prompt_color,
                                     new_line=True)])

    def check_combat(self):
        current_living_npcs = self.get_npcs()[:]
        while len(current_living_npcs) > 0:
            _npc = current_living_npcs.pop(0)
            if "Chained" in _npc.attributes:
                continue
            attack = None
            weapon = None
            while True:
                if not isinstance(weapon,
                                  type(None)) and weapon not in _npc.weapons:
                    found = False
                    for weap in _npc.weapons:
                        if weap.get_name() == weapon.get_name():
                            for atta in weap.get_attacks():
                                if atta.get_name() == attack.get_name():
                                    atta.current_cooldown = attack.current_cooldown
                                    break
                            weapon = weap
                            found = True
                            break  # Found same type of weapon, allow continued attack
                    if not found:
                        weapon = None
                        break  # End multiattack turn because weapon was lost
                targets = []
                npc_teams = None
                for _target in self.get_npcs():
                    if _target != _npc:
                        npc_teams = []
                        target_teams = []
                        if "Team" in _npc.get_attributes():
                            npc_teams = _npc.get_attribute("Team")
                        if "Team" in _target.get_attributes():
                            target_teams = _target.get_attribute("Team")
                        if "All" in target_teams:
                            # Target is a friend to all
                            continue
                        elif len(list(set(target_teams) & set(
                                npc_teams))) > 0:
                            # Shares a team
                            continue
                        elif "All" in npc_teams and not ("You" in target_teams):
                            continue  # Do not add enemy to teams unless attacking a teammate of player's
                        if _target.get_type() == _npc.get_type():
                            if "Cannibal" in _npc.get_attributes():
                                targets.append(_target)
                        else:
                            targets.append(_target)

                your_team = False
                if not isinstance(npc_teams, type(None)) and "You" in npc_teams:
                    your_team = True
                if not self.check_if_dead() and not your_team:
                    targets.append("You")
                target = _npc.get_target(targets, self.camo, self.camo_plus)
                for _target in targets:
                    if (_target != "You" and _target.get_name() == target) \
                            or target == _target:
                        target = _target
                        break
                if not isinstance(target, type(None)):
                    if target == "You":
                        health = self.get_health()
                    else:
                        health = target.get_health()
                    stats, damages, attack, weapon, multiattack = _npc.attack(
                        health, attack, weapon)
                    if target != "You":
                        target.target = _npc.get_name()
                    if not isinstance(attack, type(None)):
                        if "Thrown" in attack.get_attributes():
                            self.path[0].find_object(
                                "Surroundings").add_object(
                                GameObject([Text(weapon.get_name(),
                                                 color=weapon_color,
                                                 tooltip=weapon.gen_desc())],
                                           _actions=[
                                               GameAction("Pick-up")],
                                           attributes={"Item": weapon}))
                            _npc.weapons.remove(weapon)
                        elif "Consumable" in attack.get_attributes():
                            _npc.weapons.remove(weapon)
                        elif "Disarm" in attack.get_attributes():
                            if target == "You":
                                if "Weapon" in self.get_equipped(). \
                                        get_attributes():
                                    item = self.get_equipped().get_attribute(
                                        "Weapon")
                                    self.add_ground_item(
                                        item)  # Add to ground
                                    self.remove_inv_item(
                                        item)  # Remove from inventory
                                    item = item.get_attribute("Item")
                                    self.add_event([self.get_you_word(),
                                                    Text("dropped "),
                                                    Text(item.get_name(),
                                                         color=weapon_color,
                                                         tooltip=item.gen_desc(),
                                                         new_line=True)])
                            else:
                                if len(target.weapons) > 0:
                                    # Remove random weapon
                                    disarmed_weapon = random.choice(
                                        _npc.weapons)
                                    _npc.weapons.remove(disarmed_weapon)
                                    self.get_path()[0].find_object(
                                        "Surroundings").add_object(
                                        GameObject(
                                            [Text(
                                                disarmed_weapon.get_name(),
                                                color=weapon_color, tooltip=
                                                disarmed_weapon.gen_desc())],
                                            attributes={
                                                "Item": disarmed_weapon},
                                            _actions=[
                                                GameAction("Pick-up")]))
                                    self.add_event(
                                        [_npc.get_word(), Text("dropped "),
                                         Text(
                                             disarmed_weapon.get_name(),
                                             color=weapon_color,
                                             tooltip=disarmed_weapon.gen_desc(),
                                             new_line=True)])
                        elif "Sleep+" in attack.get_attributes():
                            if target == "You":
                                if not game_save.orpheus:
                                    game_save.sleep = 10
                                    self.add_event(
                                        [Text("You have fallen into a deep sleep.",
                                              new_line=True, color=prompt_color)])
                                elif "Sleep+" in attack.get_attributes() and game_save.orpheus:
                                    game_save.orpheus = False
                                    self.add_event([Text(
                                        "The music of Orpheus\\'s Lyre keeps you alert. Its effects have now worn off.",
                                        new_line=True, color=prompt_color)])
                        elif "Wolf" in attack.get_attributes():
                            if target == "You":
                                game_save.wolf = True
                        if target == "You":
                            self.set_health(stats)
                        else:
                            target.set_health(stats)
                        is_dead = False
                        life = False
                        if len(damages) >= 1:
                            # Hit
                            tame = False
                            if target == "You":
                                is_dead = self.check_if_dead()
                            else:
                                is_dead, tame, life = target.check_if_dead()
                            self.hit_event(attack, damages, _npc, weapon,
                                           is_dead, tame, target)
                        else:
                            self.miss_event(attack, damages, _npc, weapon,
                                            target)

                        if target != "You" and is_dead:
                            # Target was killed
                            if "Unique" in target.get_attributes():
                                self.uniques.append(target.get_type())
                            if target in current_living_npcs:
                                current_living_npcs.remove(target)
                            npc_num = self.get_npcs().index(target)
                            self.get_path()[0].find_object(
                                "Surroundings").contained_objects.pop(
                                npc_num)
                            for _weapon in target.get_weapons():
                                if "Retained" not in _weapon.get_attributes() \
                                        and not life:
                                    self.get_path()[0].find_object(
                                        "Surroundings").add_object(
                                        GameObject(
                                            [Text(_weapon.get_name(),
                                                  color=weapon_color,
                                                  tooltip=
                                                  _weapon.gen_desc())],
                                            attributes={
                                                "Item": _weapon},
                                            _actions=[
                                                GameAction("Pick-up")]))
                            self.drop_ambrosia(target)
                            if game_save.viewed_npc == target.get_name():
                                # remove inv of observed npc
                                self.remove_path_index(-1)
                else:
                    break  # No targets
                if not multiattack:
                    _npc.tick()
                    break

        self.update_surroundings()

    def drop_ambrosia(self, target):
        if random.randint(1, 20000) \
                <= target.get_health()["Tame"]:
            self.add_event([Text(
                "Ambrosia dropped to the ground.",
                color=prompt_color, new_line=True)])
            self.get_path()[0].find_object(
                "Surroundings").add_object(GameObject(
                [Text(ambrosia.get_name(),
                      color=weapon_color,
                      tooltip=ambrosia.gen_desc())],
                attributes={
                    "Item": ambrosia,
                }, _actions=[GameAction("Pick-up")]))

    def check_egg(self):
        egg = False
        for weapon in self.get_path()[0].find_object(
                "Inventory").get_objects():
            if "Egg" in weapon.get_attribute("Item").attributes:
                self.remove_inv_item(weapon)
                self.set_health(starting_health)
                self.update_attacks()
                egg = True
        if egg:
            self.add_event([Text("YOU ARE DEAD", color=dead_color,
                                 font_name=dead_font,
                                 font_size=dead_font_size, new_line=True)])
            time.sleep(2)

            self.add_event([Text(
                "You hear a crack.",
                color=prompt_color, new_line=True)])

            time.sleep(2)

            self.add_event([Text("YOU LIVE AGAIN", color=dead_color,
                                 new_line=True, font_size=dead_font_size,
                                 font_name=dead_font)])
        return egg

    def check_if_dead(self):
        return self.get_character().check_if_dead()[0]

    def hit_event(self, _attack, damages, attacker, _weapon,
                  _is_dead=False, tame=False, target=None):

        is_you_target = target == "You" or target.get_name() == "yourself"
        is_you_attacker = attacker == "You" or attacker.get_name() == "yourself"

        if is_you_attacker:
            attacker_word = self.get_you_word()
        else:
            attacker_word = attacker.get_word()
        attack_word = Text(_attack.past_tense + " ",
                           tooltip=self.gen_attack_tooltip(_attack,
                                                           damages),
                           color=attack_color)
        if is_you_target:
            target_word = self.get_you_word(caps=False, strip=True,
                                            yourself=is_you_attacker)
        else:
            target_word = target.get_word(strip=True)
        text_list = [attacker_word, attack_word, target_word]

        flower = False
        if not isinstance(_weapon, type(None)):
            if "Flower" in _weapon.get_attributes() and not self.cryptic:
                flower = True

        if not isinstance(_weapon, type(None)):
            text_list += [Text(" "), Text("with "),
                          Text(_weapon.get_name().replace("-", " "),
                               color=weapon_color,
                               tooltip=_weapon.gen_desc(flower=flower))]
        if tame:
            text_list.append(Text(" "))
            text_list.append(Text("taming them"))
        elif _is_dead and not is_you_target:
            text_list.append(Text(" "))
            text_list.append(Text("killing them"))

        text_list.append(Text(".", new_line=True))
        self.add_event(text_list)

    def miss_event(self, _attack, damages, attacker, _weapon, target):
        is_you_target = target == "You" or target.get_name() == "yourself"
        is_you_attacker = attacker == "You" or attacker.get_name() == "yourself"

        if is_you_attacker:
            attacker_word = self.get_you_word()
        else:
            attacker_word = attacker.get_word()
        attack_word = Text(_attack.name.lower().replace("-", " ") + " ",
                           tooltip=self.gen_attack_tooltip(_attack,
                                                           damages),
                           color=attack_color)
        if is_you_target:
            target_word = self.get_you_word(caps=False, strip=True,
                                            yourself=is_you_attacker)
        else:
            target_word = target.get_word()
        text_list = [attacker_word, Text("tried to "), attack_word,
                     target_word]

        flower = False
        if not isinstance(_weapon, type(None)):
            if "Flower" in _weapon.get_attributes() and not self.cryptic:
                flower = True

        if not isinstance(_weapon, type(None)):
            text_list += [Text(" "), Text("with "),
                          Text(_weapon.get_name().replace("-", " "),
                               color=weapon_color,
                               tooltip=_weapon.gen_desc(flower=flower))]
        text_list.append(Text(" "))
        text_list.append(Text("but missed.", new_line=True))
        self.add_event(text_list)

    @staticmethod
    def gen_attack_tooltip(_attack, damages):
        # Add Attack name to attack tooltip
        desc = [Text(_attack.get_name(), font_size=header_size,
                     color=header_color, new_line=True),
                Text("Current Cooldown: "), Text(str(
                _attack.display_current_cooldown()), color=number_color,
                new_line=True)]
        if len(damages) == 0:
            desc.append(Text("No damage.", new_line=True))
        else:
            # Add attack stats to attack tooltip
            for damage in damages:
                desc += [Text(damage + ": ", color=header_color),
                         Text(str(damages[damage]), new_line=True,
                              color=number_color)]
        return desc

    game_save = None


def start(_get_input, update_textbox, _set_choices, mark_temporary,
          clear_temporary, is_running, set_caption, check_hotkeys,
          disable_hotkeys, enable_hotkeys, set_dead):
    """Function to start gameplay"""
    global game_save

    # TODO: Hotkey's/Shortcuts box?
    # TODO: Choose an object and see its actions

    # Interface functions

    def add_event(_event=""):
        """Adds an event to the events box

        :type _event: str | list[Text]
        :param _event: "" for new line
        """

        if _event == "":
            _event = [Text("", new_line=True)]

        update_textbox("events", _event)

    game_save = GameSave(add_event=add_event)

    def get_input(prompt=None, display_answer=True, allow_path_change=True,
                  constrict=True, hotkeys=False):
        """Creates a prompt and waits for input

        :type prompt: str | None
        :type display_answer: bool
        :type allow_path_change: bool
        :type constrict: bool
        :type hotkeys: bool
        """

        set_choices(constrict)
        if not hotkeys:
            disable_hotkeys()
        user_input, path_changed = _get_input(prompt, game_save.get_path(),
                                              allow_path_change)
        if not hotkeys:
            enable_hotkeys()
        if isinstance(path_changed, type(None)):
            # Main thread quit
            return None, None

        if display_answer:
            add_event([Text("Menu>", color=input_color,
                            font_size=path_font_size, font_name=path_font),
                       Text(user_input, color=input_color,
                            font_size=path_font_size, font_name=path_font)])

        return user_input, path_changed

    def find_choice(_choice):
        """Returns the object or action chosen based on given name

        :type _choice: str
        :rtype: GameObject | GameAction | None
        """

        if _choice == "":
            return

        # Down a path
        current_objects = game_save.get_path()[-1].get_objects()
        current_actions = game_save.get_path()[-1].get_actions()

        for _object in current_objects:
            if _object.get_text_string().strip() == _choice:
                return _object
        for _action in current_actions:
            if _action.get_text_string().strip() == _choice:
                return _action
                # raise Exception("Could not find choice: " + _choice)

    def set_choices(constrict=True):
        """Sets the choices to cycle between"""
        if constrict:
            _set_choices(game_save.get_path()[-1].get_objects(),
                         game_save.get_path()[-1].get_actions())
        else:
            _set_choices([], [])

    def get_from_choices(prompt, choices, display_answer=True):
        game_save.set_path_index(0)
        game_save.hide_objects()
        for choice in choices:
            game_save.add_main_action(GameAction([Text(choice)]))
        _choice = get_choice(prompt, display_answer=display_answer)
        if isinstance(_choice, type(None)):
            save_to_file(game_save, game_save.name + "." + extension)
            raise SystemExit

        game_save.clear_main_actions()
        game_save.show_objects()
        display_objects()
        return _choice

    def select_action(chosen_object, display_answer, return_string):
        if display_answer:
            # Get Path and reduce font size
            path_text_list = []
            for _object in game_save.get_path_text_list():
                object_text = _object.copy(False)
                object_text.set_font(path_font, path_font_size)
                path_text_list.append(object_text)

            # Get chosen object and reduce font size
            object_text = chosen_object.get_text_object().copy(
                False)
            object_text.set_font(path_font, path_font_size)
            path_text_list.append(object_text)

            # Add newline and add to events
            path_text_list[-1].new_line = True
            add_event(path_text_list)

        if return_string:
            return chosen_object.get_text_string().strip()
        return chosen_object

    def get_choice(prompt=None, display_answer=True, return_string=True,
                   allow_path_change=True, choose_action=False, hotkeys=False):
        """Gets user input based on current objects/actions

        :type prompt: None | str
        :type display_answer: bool
        :type return_string: bool
        :type allow_path_change: bool
        :type choose_action: bool
        """

        if not isinstance(prompt, type(None)):  # Display Prompt
            add_event([Text(prompt, color=prompt_color, new_line=True)])

        display_objects()
        chosen_object, back = get_input(display_answer=False,
                                        allow_path_change=allow_path_change,
                                        hotkeys=hotkeys)
        if isinstance(back, type(None)):
            # Main thread quit
            return None

        if back == len(game_save.get_path()) - 1:
            # Path was not changed

            chosen_object = find_choice(chosen_object)
            if type(chosen_object) == GameObject:
                game_save.append_path(chosen_object)
            if type(chosen_object) == GameAction or not choose_action:

                return select_action(chosen_object, display_answer,
                                     return_string)

            return get_choice(None, display_answer, return_string,
                              allow_path_change, choose_action, hotkeys)

        elif back == "HOTKEY":
            current_path = game_save.get_path_text_list(True)
            action = game_save.open_path(chosen_object)
            if not isinstance(action, type(None)):
                game_save.current_path = current_path
                return select_action(action, display_answer, return_string)
            display_objects()
            return get_choice(None, display_answer, return_string,
                              allow_path_change, choose_action, hotkeys)
        else:
            # Path moved back via delete
            if len(game_save.get_path()) > 1:
                game_save.set_path_index(back)
            display_objects()
            return get_choice(None, display_answer, return_string,
                              allow_path_change, choose_action, hotkeys)

    def get_yes(prompt=None, display_answer=True, choices=None):
        """Returns the users response to a yes/no question

        :type prompt: None | str
        :type display_answer: bool
        :type choices: None | list[str]
        :param choices: Provide two choices in a list. 'Yes'/'No' if None
        """
        if not isinstance(prompt, type(None)):
            add_event(
                [Text(prompt, None, color=prompt_color, new_line=True)])

        if isinstance(choices, type(None)):
            choices = ["Yes", "No"]

        if len(choices) > 2:
            raise Exception("Too many choices provided")

        game_save.set_path_index(0)
        game_save.hide_objects()
        game_save.add_main_action(GameAction([Text(choices[0])]))
        game_save.add_main_action(GameAction([Text(choices[1])]))

        _choice = get_choice(display_answer=display_answer)
        if isinstance(_choice, type(None)):
            raise SystemExit

        game_save.clear_main_actions()
        game_save.show_objects()
        display_objects()

        if _choice == choices[0]:
            return True
        if _choice == choices[1]:
            return False
        raise Exception("Non yes/no answer given to yes/no question")

    def continue_prompt():
        """Prompts the user to press 'Enter'"""
        add_event([Text("Press 'Enter' to continue...", new_line=True,
                        color=input_color)])

        game_save.set_path_index(0)

        game_save.hide_objects()

        display_objects()
        while True:
            user_input = get_input(display_answer=False,
                                   allow_path_change=False)
            if isinstance(user_input[1], type(None)):
                raise SystemExit
            elif user_input[1] != "HOTKEY":
                break

        game_save.show_objects()

        display_objects()

    def display_objects():
        """Sends the current objects to the gui"""

        set_choices()

        # Object selected
        current_objects = game_save.get_path()[-1].get_objects()
        current_actions = game_save.get_path()[-1].get_actions()

        if len(current_objects) < 1:  # Clear box if empty
            update_textbox("objects", "", True)
        if len(current_actions) < 1:
            update_textbox("actions", "", True)

        first = True  # Clear textbox on first word
        i = 1
        for _object in current_objects:
            comma = ""
            if i < len(current_objects):
                comma = ","
            text = _object.get_text_list()[:]
            text[-1].strip()
            text[-1].append(comma)
            text[-1].append(" ")
            update_textbox("objects", text, first)
            first = False
            i += 1

        first = True  # Clear textbox on first word
        i = 1
        for _action in current_actions:
            comma = ""
            if i < len(current_actions):
                comma = ","
            text_list = _action.get_text_list()
            text_list[-1].strip()
            text_list[-1].append(comma)
            text_list[-1].append(" ")
            update_textbox("actions", text_list, first)
            first = False
            i += 1

        # Display path

        update_textbox("path", game_save.get_path_text_list(), True)

    # Game Functions

    def tutorial():
        """Displays the tutorial"""
        # TODO: Update. Add Gameplay
        if get_yes("Do you want to view a tutorial? "
                   "(Use 'Tab' and 'Enter' to select an option)",
                   choices=["View", "Skip"]):

            prompt = "What would you like to learn about?"

            while True:

                _choice = get_from_choices(prompt, list(tutorials) + ["Cancel"])

                if _choice != "Cancel":
                    for line in tutorials[_choice]:
                        add_event([Text(line, new_line=True)])
                        continue_prompt()
                        add_event()
                    add_event()
                else:
                    break

    def save_and_load():
        """Save or load a game"""

        global game_save

        saves = list(filter(lambda x: x.endswith("." + extension),
                            get_files(
                                get_saves_path())))  # Get all save files
        if len(saves) < 1 or get_yes("Would you like to start a new game?",
                                     choices=["New", "Load"]):
            game_save.hide_objects()
            display_objects()

            name, _exit = get_input(
                "What do you want to name your game save?",
                constrict=False)
            if isinstance(_exit, type(None)):
                raise SystemExit

            game_save.show_objects()
            display_objects()

            game_save = GameSave(name, add_event=add_event)
            game_save.gen_location("Town")
            save_to_file(game_save, name + "." + extension)
        else:
            game_save.set_path_index(0)
            game_save.hide_objects()

            for file in saves:
                game_save.add_main_action(GameAction(
                    file[:-len(extension) - 1]))

            save_file = get_choice("Choose a save file.") + "." + extension
            if isinstance(save_file, type(None)):
                raise SystemExit

            game_save.clear_main_actions()
            game_save.show_objects()

            game_save = load_from_file(save_file)
            game_save.set_path_index(0)
            game_save.add_event = add_event
            display_objects()
        set_caption("The Odyssey+: " + game_save.name)

    def display_location():
        location = game_save.get_path()[0].find_object(
            "Surroundings").get_attribute("location")
        add_event(
            [game_save.get_you_word(), Text("are in "),
             Text(location.get_name(), color=location_color,
                  tooltip=location.gen_desc()), Text(".", new_line=True)])

    # Start game

    tutorial()

    save_and_load()

    add_event()

    # Spawn Location
    display_location()

    # Main game loop
    alive = not game_save.check_if_dead()
    while alive:  # Main game loop
        save_to_file(game_save, game_save.name + "." + extension)

        multiattack = False
        # Combat

        game_save.update_attacks()

        if game_save.check_if_dead():
            if not game_save.check_egg():
                break  # Died, break loop

        game_save.check_combat()

        game_save.check_boosts()

        if game_save.check_if_dead():
            if not game_save.check_egg():
                break  # Died, break loop

        game_save.update_attacks()

        choosing = True

        # Choices
        if game_save.sleep > 0:
            game_save.sleep -= 1
            if game_save.sleep == 0:
                add_event([Text("You awaken.", color=prompt_color,
                                new_line=True)])

        if game_save.temp_cryptic:
            if game_save.cryptic:
                game_save.temp_cryptic = False
                game_save.cryptic = False
            else:
                game_save.cryptic = True
            game_save.rename_flowers()

        weapon = None

        while (choosing or multiattack) and game_save.sleep == 0:  # Main choice loop
            cancel = False
            reset_cooldowns = False
            if not isinstance(game_save.current_path, type(None)):
                game_save.open_path(game_save.current_path)
                game_save.current_path = None
            choice = get_choice(return_string=True, choose_action=True,
                                hotkeys=True)
            if isinstance(choice, type(None)):
                # Game exit
                break

            if game_save.fleece:
                if game_save.get_health()["Brute"] < 10000:
                    game_save.get_health()["Brute"] += 200
                if game_save.get_health()["Sharp"] < 10000:
                    game_save.get_health()["Sharp"] += 200
                if game_save.get_health()["Burn"] < 10000:
                    game_save.get_health()["Burn"] += 200
                if game_save.get_health()["Freeze"] < 10000:
                    game_save.get_health()["Freeze"] += 200
                if game_save.get_health()["Divine"] < 10000:
                    game_save.get_health()["Divine"] += 300
                if game_save.get_health()["Agility"] < 1000:
                    game_save.get_health()["Agility"] += 50
                game_save.update_stats_tooltip()

            if choice == "Pick-up":
                if not multiattack:
                    multiattack = False
                    item = game_save.get_path()[-1]

                    too_heavy = False
                    if "Heavy" in item.get_attribute(
                                    "Item").get_attributes():
                        too_heavy = game_save.get_health()["Brute"] < 10000
                    if not too_heavy:
                        if game_save.get_path()[0].find_object(
                                "Surroundings").get_attribute(
                                "location").get_type() != "Town":
                            success = True
                        else:
                            success, treasures = game_save.get_payment(1, False)
                        if success:
                            if "Spawn-Cerastes" in item.get_attribute(
                                    "Item").get_attributes():
                                game_save.gen_npc(cerastes)
                                add_event([Text("You pull a ", color=dead_color),
                                           cerastes.get_word(),
                                           Text("out of the sand.",
                                                color=dead_color,
                                                new_line=True)])
                            elif "Smite" in item.get_attribute(
                                    "Item").get_attributes():
                                add_event([Text(
                                    "Zeus smote you with a lightning bolt.",
                                    color=dead_color, new_line=True)])
                                game_save.get_health()["Divine"] = 0
                                if not game_save.check_egg():
                                    break  # Died, break loop
                            elif "Sack" in item.get_attribute("Item").get_attributes():
                                game_save.sack = True
                            elif "Head" in item.get_attribute("Item").get_attributes():
                                if not game_save.sack:
                                    add_event([Text(
                                        "Medusa\'s eyes stare into your soul.",
                                        color=dead_color, new_line=True)])
                                    game_save.get_health()["Soul"] = 0
                                    if not game_save.check_egg():
                                        break  # Died, break loop
                                else:
                                    add_event([Text(
                                        "You pick up the head with the Kibisis.",
                                        color=prompt_color, new_line=True)])
                                    item.get_attribute("Item").reset_cooldowns()
                                    game_save.add_inv_item(item)  # Add to inventory
                            elif "Shield" in item.get_attribute("Item").get_attributes():
                                if not game_save.shield:
                                    game_save.shield = True
                                    game_save.get_health()["Brute"] += 100000
                                    game_save.get_health()["Sharp"] += 100000
                                    game_save.get_health()["Burn"] += 100000
                                    game_save.get_health()["Agility"] -= 100
                                    item.get_attribute("Item").reset_cooldowns()
                                    game_save.add_inv_item(item)  # Add to inventory
                                    game_save.update_stats_tooltip()
                                else:
                                    item.get_attribute("Item").reset_cooldowns()
                                    game_save.add_inv_item(item)  # Add to inventory
                            elif "Fleece" in item.get_attribute("Item").get_attributes():
                                if not game_save.fleece:
                                    game_save.fleece = True
                                    item.get_attribute("Item").reset_cooldowns()
                                    game_save.add_inv_item(item)  # Add to inventory
                                else:
                                    item.get_attribute("Item").reset_cooldowns()
                                    game_save.add_inv_item(item)  # Add to inventory
                            else:
                                item.get_attribute("Item").reset_cooldowns()
                                game_save.add_inv_item(item)  # Add to inventory
                            game_save.remove_ground_item(item)  # Remove from ground
                            game_save.remove_path_index(-1)  # Remove from Path
                            choosing = False
                    else:
                        add_event([Text("The item is too heavy.",
                                        color=prompt_color, new_line=True)])
                else:
                    add_event([Text("You have not finished your attack.",
                                    color=prompt_color, new_line=True)])

            elif choice == "Drop":
                multiattack = False
                item = game_save.get_path()[-1]
                item.get_attribute("Item").reset_cooldowns()
                if "Fleece" in item.get_attribute("Item").get_attributes():
                    game_save.fleece = False
                game_save.add_ground_item(item)  # Add to ground
                game_save.remove_inv_item(item)  # Remove from inventory
                game_save.remove_path_index(-1)  # Remove from Path

            elif choice == "Leave-Location":
                multiattack = False
                monster = game_save.check_caught()
                if monster:  # Objects eval to True
                    # Was caught
                    add_event([monster.get_word(), Text("caught "),
                               game_save.get_you_word(False, strip=True),
                               Text(".", new_line=True)])
                else:
                    # Escaped
                    game_save.gen_location()
                    display_location()
                choosing = False

            elif choice == "Wait":
                multiattack = False
                choosing = False

            elif choice == "Equip":
                equipped_attack = game_save.get_path()[0].find_object(
                    "Attacks").get_attribute("Equipped").get_attribute(
                    "Attack")
                if equipped_attack.current_cooldown <= 0 or "Cooldown" \
                        in equipped_attack.get_attributes():
                    game_save.get_path()[0].find_object("Attacks"). \
                        add_attribute("Equipped", game_save.get_path()[-1])
                    game_save.update_attacks_tooltip()
                    if "Self" in game_save.get_path()[-1].get_attribute(
                            "Attack").get_attributes():
                        game_save.set_path_index(0)
                        stats = game_save.get_path()[0].find_object("Stats")
                        game_save.get_path().append(stats)
                        game_save.get_path().append(
                            stats.find_object("You"))
                    else:
                        game_save.set_path_index(0)
                        game_save.append_path(
                            game_save.get_path()[0].find_object(
                                "Surroundings"))
                    if multiattack:  # If multiattacking, end turn
                        multiattack = False
                        choosing = False
                else:
                    add_event(
                        [Text("Cannot change weapons while equipped is "
                              "cooling down.", color=prompt_color,
                              new_line=True)])
            elif choice == "Talk":
                npc = game_save.get_path()[-1].get_attribute(
                    "NPC")
                if not multiattack:
                    item = GameObject(
                        [Text(hrunting.get_name(),
                              color=weapon_color,
                              tooltip=hrunting.gen_desc())],
                        attributes={"Item": hrunting,
                                    }, _actions=[GameAction("Drop")])
                    game_save.add_inv_item(item)
                    add_event([Text("Hrothgar gives you Hrunting on behalf of Unferth.",
                                    color=prompt_color, new_line=True)])
                    add_event([npc.get_word(), Text(
                        "says, 'The holy Creator usward sent him, To West-Dane warriors, I ween, for to render ’Gainst Grendel’s grimness gracious assistance: I shall give to the good one gift-gems for courage.'",
                        color=prompt_color, new_line=True)])
                    game_save.herot = True
                    game_save.uniques.append(npc.get_type())
                    game_save.get_path()[-1].remove_action(
                        game_save.get_path()[-1].get_actions()[1])
                else:
                    add_event([Text("You have not finished your attack.",
                                    color=prompt_color, new_line=True)])
            elif choice == "Pay":
                npc = game_save.get_path()[-1].get_attribute(
                    "NPC")
                if not multiattack:
                    success, treasures = game_save.get_payment(1)
                    if success:
                        npc.paid = True
                        game_save.canterbury(
                            npc, treasures)
                        multiattack = False
                        choosing = False
                else:
                    add_event([Text("You have not finished your attack.",
                                    color=prompt_color, new_line=True)])

            elif choice == "Attack" or choice == "Use":
                disarmed_weapon = None
                power = False
                # Get equipped attack
                attack_object = game_save.get_path()[0].find_object(
                    "Attacks").get_attribute("Equipped")
                # Get Attack from object
                attack = attack_object.get_attribute("Attack")

                # Check if attack has cooldown
                if attack.ammo > 0 and attack.current_ammo < 1:
                    add_event([Text("Equipped attack is out of ammo.",
                                    color=prompt_color, new_line=True)])
                    multiattack = False
                    weapon_object = attack_object.get_attribute(
                        "Weapon")
                    game_save.remove_inv_item(weapon_object)
                    game_save.update_surroundings()
                elif attack.current_cooldown > 0:
                    add_event(
                        [Text("Equipped attack is still cooling down.",
                              color=prompt_color, new_line=True)])
                    game_save.open_path("Surroundings")
                else:
                    # Get target npc
                    npc_num = 0
                    is_you = False
                    if game_save.get_path()[-1].get_text_string() == "You":
                        _npc = game_save.get_character()
                        is_you = True
                    else:
                        if "Self" in attack.get_attributes():
                            add_event(
                                [Text("Can only be used on self.",
                                      color=prompt_color, new_line=True)])
                            game_save.set_path_index(0)
                            stats = game_save.get_path()[0].find_object(
                                "Stats")
                            game_save.get_path().append(stats)
                            game_save.get_path().append(
                                stats.find_object("You"))
                            continue
                        _npc = game_save.get_path()[-1].get_attribute("NPC")
                        for npc in game_save.get_path()[0].find_object(
                                "Surroundings").get_objects():
                            if "NPC" in npc.get_attributes():
                                npc_name = npc.get_attribute(
                                    "NPC").get_name()
                                if npc_name == _npc.get_name():
                                    _npc = npc.get_attribute("NPC")
                                    break
                            npc_num += 1
                    stats, _damages = attack.attack(_npc.get_health(), is_you,
                                                    game_save.boost_attacks(),
                                                    game_save.accurate)

                    taming = False
                    for _damage in _damages:
                        if _damages[_damage] > 0:
                            if _damage == "Tame" or _damage == "Tame+" or _damage == "Tame2+":
                                taming = True
                    if not taming:
                        _npc.target = "You"
                    # Update npc health
                    _npc.set_health(stats)
                    # Update npc tooltip
                    if is_you:
                        game_save.update_stats_tooltip()
                    else:
                        game_save.get_path()[-1].set_tooltip(
                            _npc.gen_desc())

                    if "Disarm" in attack.get_attributes():
                        if len(_npc.weapons) > 0:
                            disarmed_weapon = random.choice(
                                list(filter(lambda x: "Body" not in
                                                      x.get_attributes(),
                                            _npc.weapons)))
                            _npc.weapons.remove(disarmed_weapon)
                            disarmed_weapon.reset_cooldowns()
                            game_save.get_path()[0].find_object(
                                "Surroundings").add_object(GameObject(
                                [Text(disarmed_weapon.get_name(),
                                      color=weapon_color,
                                      tooltip=disarmed_weapon.gen_desc())],
                                attributes={
                                    "Item": disarmed_weapon,
                                }, _actions=[GameAction("Pick-up")]))
                    if "Weapon" in attack_object.get_attributes():

                        weapon_object = attack_object.get_attribute(
                            "Weapon")
                        weapon = weapon_object.get_attribute("Item")
                        if "Thrown" in attack.get_attributes():
                            reset_cooldowns = True
                            game_save.add_ground_item(weapon_object)
                            game_save.remove_inv_item(weapon_object)
                        elif "Consumable" in attack.get_attributes():
                            game_save.remove_inv_item(weapon_object)
                    else:
                        weapon = None
                    if "Speed" in attack.get_attributes():
                        power = True
                        # Allow reduce cooldown weapons
                        for _weapon in _npc.weapons:
                            for _attack in _weapon.attacks:
                                _attack.decrease_cooldown()
                        for _attack in _npc.attacks:
                            _attack.decrease_cooldown()
                    if "Cryptic+" in attack.get_attributes():
                        power = True
                        game_save.cryptic = True
                        game_save.temp_cryptic = False
                        game_save.rename_flowers()
                    if "Orpheus" in attack.get_attributes():
                        power = True
                        game_save.orpheus = True
                    if "Calm" in attack.get_attributes():
                        power = True
                        _npc.target = None
                        _npc.aggressiveness /= 2
                    if "Enrage" in attack.get_attributes():
                        power = True
                        _npc.target = None
                        for _attack in _npc.attacks:
                            _attack *= 2
                    if "Herbal" in attack.get_attributes():
                        if not game_save.cryptic:
                            game_save.temp_cryptic = True
                            power = True
                        else:
                            add_event([Text("You already have this knowledge.",
                                            color=prompt_color, new_line=True)])
                            cancel = True
                    if "Camo" in attack.get_attributes():
                        power = True
                        game_save.camo = True
                    if "Camo+" in attack.get_attributes():
                        power = True
                        game_save.camo_plus = True
                    if "Trumpet" in attack.get_attributes():
                        power = True
                        npc_word_list = game_save.gen_npcs(
                            True)  # Allow for wandering monsters
                        for npc_word in npc_word_list:
                        #   if not isinstance(npc_word, type(None)):
                            add_event([npc_word, Text("wandered into the vicinity at the call of the trumpet.",
                                                            new_line=True,
                                                            color=treasure_color)])
                    if "Atlas" in attack.get_attributes():
                        location_choices = []
                        probabilities = [l.probability for l in LOCATIONS_LIST]
                        while True:
                            location = weighted_choice(LOCATIONS_LIST,
                                                       probabilities)
                            if location not in location_choices:
                                location_choices.append(location)
                            if len(location_choices) == 3:
                                break
                        choice = get_from_choices(
                            "Choose a location to travel to.", list(
                                location.get_name() for location in list(
                                    filter(lambda x: x.get_name() != "Olympus",
                                           location_choices))))
                        game_save.gen_location(choice)
                        display_location()
                    if "Sleep" in attack.get_attributes() and not game_save.orpheus:
                        game_save.sleep = 5
                        power = True
                        add_event([Text("You have fallen asleep.",
                                        new_line=True, color=prompt_color)])
                    elif "Sleep" in attack.get_attributes() and game_save.orpheus:
                        game_save.orpheus = False
                        add_event([Text("The music of Orpheus\\'s Lyre keeps you alert. Its effects have now worn off.",
                                        new_line=True, color=prompt_color)])
                    if "Omphalos" in attack.get_attributes():
                        game_save.gen_location("Olympus")
                        display_location()
                    if "Travel" in attack.get_attributes():
                        game_save.gen_location("Town")
                        display_location()
                    if "Thread" in attack.get_attributes():
                        game_save.gen_location("Labyrinth")
                        display_location()
                    if "Chains" in attack.get_attributes():
                        power = True
                        if "Chained" not in _npc.get_attributes():
                            _npc.add_attribute("Chained", True)
                            add_event([Text("Unbreakable chains wrap around them "
                                            "and they can't move.", new_line=True,
                                            color=prompt_color)])
                            if "Fox" in _npc.get_attributes():
                                _npc.set_health(starting_health)
                    if "Sleep+" in attack.get_attributes() and not game_save.orpheus:
                        game_save.sleep = 10
                        power = True
                        add_event(
                            [Text("You have fallen into a deep sleep.",
                                  new_line=True, color=prompt_color)])
                    if "Rod" in attack.get_attributes():
                        if game_save.get_health()["Brute"] < 3000:
                            game_save.get_health()["Brute"] += 100
                        if game_save.get_health()["Sharp"] < 2000:
                            game_save.get_health()["Sharp"] += 100
                        if game_save.get_health()["Burn"] < 1000:
                            game_save.get_health()["Burn"] += 100
                        if game_save.get_health()["Freeze"] < 1500:
                            game_save.get_health()["Freeze"] += 100
                        if game_save.get_health()["Agility"] < 400:
                            game_save.get_health()["Agility"] += 50
                        game_save.update_stats_tooltip()
                    elif "Sleep+" in attack.get_attributes() and game_save.orpheus:
                        game_save.orpheus = False
                        add_event([Text("The music of Orpheus\\'s Lyre keeps you alert. Its effects have now worn off.",
                                        new_line=True, color=prompt_color)])
                    if "Spawn-Weapon" in attack.get_attributes():
                        power = True
                        random_weapon = random.choice(WEAPONS_LIST)
                        random_weapon = GameObject(
                            [Text(random_weapon.get_name(),
                                  color=weapon_color,
                                  tooltip=random_weapon.gen_desc())],
                            attributes={
                                "Item": random_weapon,
                            }, _actions=[GameAction("Pick-Up")])
                        game_save.add_ground_item(random_weapon)
                        game_save.rename_flowers()
                 #   if "Spawn-Attack" in attack.get_attributes():
                  #      power = True
                   #     random_attack = dict_to_attack(random.choice(all_attacks))
                    #    game_save.get_character().add_attacks(
                     #       random_attack)
                    if "Spawn-Finely-Cooked-Meal" in attack.get_attributes():
                        power = True
                        item = GameObject(
                            [Text(finely_cooked_meal.get_name(),
                                  color=weapon_color,
                                  tooltip=finely_cooked_meal.gen_desc())],
                            attributes={"Item": finely_cooked_meal,
                                        }, _actions=[GameAction("Drop")])
                        game_save.add_inv_item(item)
                        add_event([Text("You created a finely cooked meal.",
                                        color=prompt_color, new_line=True)])
                    if "Spawn-Meal" in attack.get_attributes():
                        power = True
                        item = GameObject(
                            [Text(cooked_meal.get_name(),
                                  color=weapon_color,
                                  tooltip=cooked_meal.gen_desc())],
                            attributes={"Item": cooked_meal,
                                        }, _actions=[GameAction("Drop")])
                        game_save.add_inv_item(item)
                        add_event([Text("You created a cooked meal.",
                                        color=prompt_color, new_line=True)])
                    if "Spawn-Mead2" in attack.get_attributes():
                        power = True
                        item = GameObject(
                            [Text(mead.get_name(),
                                  color=weapon_color,
                                  tooltip=mead.gen_desc())],
                            attributes={"Item": mead,
                                        }, _actions=[GameAction("Drop")])
                        game_save.add_inv_item(item)
                        game_save.add_inv_item(item)
                        add_event([Text("You obtained some mead.",
                                        color=prompt_color, new_line=True)])
                    if "Spawn-Dagger" in attack.get_attributes():
                        power = True
                        item = GameObject(
                            [Text(dagger.get_name(),
                                  color=weapon_color,
                                  tooltip=dagger.gen_desc())],
                            attributes={"Item": dagger,
                                        }, _actions=[GameAction("Drop")])
                        game_save.add_inv_item(item)
                        add_event([Text("You unsheath a dagger.",
                                        color=prompt_color, new_line=True)])
                    if "Spawn-Treasure" in attack.get_attributes():
                        power = True
                        item = GameObject(
                            [Text(gold_ingot.get_name(),
                                  color=treasure_color,
                                  tooltip=gold_ingot.gen_desc())],
                            attributes={'Treasure': True,
                                        "Item": gold_ingot,
                                        }, _actions=[GameAction("Drop")])
                        game_save.add_inv_item(item)
                        add_event([Text("You create a gold ingot.",
                                        color=prompt_color, new_line=True)])
                    if "Spawn-Anything" in attack.get_attributes():
                        power = True
                        random_object = random.choice(EVERYTHING_LIST)
                        if type(random_object) != NPC:
                            random_object = GameObject(
                                [Text(random_object.get_name(),
                                      color=weapon_color,
                                      tooltip=random_object.gen_desc())],
                                attributes={
                                    "Item": random_object,
                                }, _actions=[GameAction("Pick-Up")])
                            game_save.add_ground_item(random_object)
                            game_save.rename_flowers()
                        else:
                            game_save.gen_npc(random_object)
                    if "Spawn-Spartae" in attack.get_attributes():
                        power = True
                        game_save.gen_npc(spartae)
                    if "Cow" in attack.get_attributes():
                        power = True
                        game_save.gen_npc(minotaur)
                    if "Self" in attack.get_attributes():
                        power = True

                    is_dead, tame, life = _npc.check_if_dead()

                    if len(_damages) >= 1 or power:
                        # Hit
                        game_save.hit_event(attack, _damages, "You", weapon,
                                            is_dead, tame, _npc)
                    else:
                        game_save.miss_event(attack, _damages, "You",
                                             weapon,
                                             _npc)

                    if not isinstance(disarmed_weapon, type(None)):
                        add_event([_npc.get_word(), Text("dropped "),
                                   Text(disarmed_weapon.get_name(),
                                        color=weapon_color,
                                        tooltip=disarmed_weapon.gen_desc(),
                                        new_line=True)])

                    if is_dead and not is_you:
                        if isinstance(_npc.attributes, type(None)):
                            _npc.attributes = []
                        if "Unique" in _npc.get_attributes():
                            game_save.uniques.append(_npc.get_type())
                        if "Smite" in _npc.attributes and not tame:
                            add_event([Text(
                                "Zeus smote you with a lightning bolt.",
                                color=dead_color, new_line=True)])
                            game_save.get_health()["Divine"] = 0
                            if not game_save.check_egg():
                                break  # Died, break loop
                        if "Grendel" in _npc.attributes and not tame:
                            item = GameObject(
                                [Text(hrothgars_gift.get_name(),
                                      color=weapon_color,
                                      tooltip=hrothgars_gift.gen_desc())],
                                attributes={"Item": hrothgars_gift,
                                            }, _actions=[GameAction("Drop")])
                            game_save.add_inv_item(item)
                            add_event([Text(
                                "Hrothgar is pleased. He presents you with a beautiful blade.",
                                color=prompt_color, new_line=True)])
                        if "Ophiotaurus" in _npc.attributes and not tame and _npc.get_health()["Burn"] <= 0:
                            item = GameObject(
                                [Text(adamantine_blade.get_name(),
                                      color=weapon_color,
                                      tooltip=adamantine_blade.gen_desc())],
                                attributes={"Item": adamantine_blade,
                                            }, _actions=[GameAction("Drop")])
                            game_save.add_inv_item(item)
                        for weapon in game_save.get_path()[0].find_object(
                                "Surroundings").get_objects()[
                            npc_num].get_objects():
                            weapon_item = weapon.get_attribute("Item")
                            if "Retained" not in weapon_item.get_attributes() \
                                    and not life and not tame:
                                # Dont drop if killed with life, tame, or is retained
                                weapon.add_action(GameAction("Pick-up"))
                                weapon_item.reset_cooldowns()
                                game_save.get_path()[0].find_object(
                                    "Surroundings").add_object(weapon)

                        current_npc = game_save.get_path()[0].find_object(
                            "Surroundings").get_objects()[npc_num]

                        if tame:
                            game_save.get_character().add_attacks(
                                current_npc.get_attribute("NPC").get_attacks(
                                    True))
                        else:
                            game_save.drop_ambrosia(_npc)

                        # Remove npc
                        game_save.get_path()[0].find_object("Surroundings"). \
                            remove_object(current_npc)
                        game_save.set_path_index(
                            len(game_save.get_path()) - 2)
                    else:
                        # Was not killed
                        if not is_you:
                            if "Fox" in _npc.get_attributes() and "Chained" not in _npc.get_attributes():
                                # Fox flees if attacked
                                add_event([_npc.get_word(),
                                           Text("fled.", color=dead_color,
                                                new_line=True)])

                                game_save.get_path()[0].find_object(
                                    "Surroundings").remove_object(
                                    game_save.get_path()[
                                        -1])
                                game_save.set_path_index(
                                    len(game_save.get_path()) - 2)

                    game_save.update_surroundings()
                    if attack.current_cooldown < 0:
                        multiattack = True
                    if attack.cooldown < 0 and attack.current_cooldown == 0:
                        attack.current_cooldown = attack.cooldown
                        multiattack = False
                    if attack.current_cooldown > 0:
                        game_save.open_path("Surroundings")
                        add_event([Text("Must wait ", color=prompt_color),
                                   Text(str(
                                       attack.current_cooldown - 1) + " ",
                                        color=number_color), Text(
                                "more turns until attack is ready to be used.",
                                new_line=True, color=prompt_color)])
                    if not cancel:
                        choosing = False

            if game_save.update_attacks():
                multiattack = False

            if reset_cooldowns:
                attack.reset_cooldown()

        if not multiattack and not cancel:
            game_save.tick()

        if not game_save.new_location:
            npc_word_list = game_save.gen_npcs(
                True)  # Allow for wandering monsters
            for npc_word in npc_word_list:
                if not isinstance(npc_word, type(None)):
                    add_event([npc_word, Text("wandered into the vicinity.",
                                              new_line=True,
                                              color=dead_color)])
        game_save.new_location = False

        display_objects()
        time.sleep(.01)
        if not is_running():
            break

    if is_running():
        add_event(
            [Text("YOU ARE DEAD", color=dead_color, font_name=dead_font,
                  font_size=dead_font_size, new_line=True)])

        # TODO: Add boss fight
        game_save.set_path_index(0)
        game_save.get_path()[0].clear_objects()
        game_save.get_path()[0].clear_actions()
        display_objects()
        set_dead()

    save_to_file(game_save, game_save.name + "." + extension)

    # TODO: 'AOE' att on attacks: Area of effect
    # TODO: Only allow "Combat" att to heal in combat |||READ: I changed it so that the rod can only heal when below starting health. This todo is now irrelevant.X
    # TODO: Display worn items ('Worn' Attribute)
    # TODO: Buy with treasure at towns
    # TODO: Read/Write stories with book
    # TODO: '?' att on weapon chooses random attack to use
    # TODO: Allow use straight from ground/inventory for self items
    # TODO: Add multiplayer
    # TODO: River Stix makes you invincible except for one random health
    # TODO: 'Unique' att on items
    # TODO: Fix story teller not mad if attacked
