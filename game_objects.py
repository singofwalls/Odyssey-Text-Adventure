"""Stores information relating to NPCs"""
import random

from core.display import Text
from core.configs import get_value, list_to_dict

from core.tools import weighted_choice

header_color = get_value("customization", "header_color")
header_size = get_value("customization", "header_size")
number_color = get_value("customization", "number_color")
npc_color = get_value("game_customization", "npc_color")

starting_health = get_value("game_objects", "starting_health")
starting_attacks = get_value("game_objects", "starting_attacks")
starting_weapons = get_value("game_objects", "starting_weapons")


class NPC(object):
    """Stores information relating to NPCs

    :type health_stats: None | Stats
    :type attacks: None | list[Attack]]
    :param aggressiveness: scale from 0 to 100 percent chance to attack
    """

    def __init__(self, name="You", _type=None, health_stats=starting_health,
                 aggressiveness=90,
                 _attacks=starting_attacks, _weapons=starting_weapons,
                 description=None, attributes=None):
        self.attributes = attributes
        self.name = name
        self.number = -1
        self.description = None
        if not isinstance(_type, type(None)):
            self._type = _type
        else:
            self._type = self.name
        if not isinstance(attributes, type(None)) and "Names" in \
                self.attributes:
            if self.name not in self.attributes["Names"]:
                # Give random name if doesnt already have one
                self.name = random.choice(self.attributes["Names"])
            if "Descriptions" in self.attributes:
                self.description = self.attributes["Descriptions"][
                    self.attributes["Names"].index(self.name)]
        if not isinstance(self.attributes, type(None)) and "Descriptions" not \
                in self.attributes:
            if isinstance(description, type(None)):
                if isinstance(self.description, type(None)):
                    self.description = []
            else:
                self.description = description
        if isinstance(attributes, type(None)):
            self.attributes = []
        self.aggressiveness = aggressiveness

        self.health_stats = health_stats

        if len(_attacks) < 1 or type(_attacks[0]) == Attack:
            # Already converted to list of Attacks
            self.attacks = _attacks
        else:
            new_attacks = []
            for _attack in _attacks:
                new_attacks.append(dict_to_attack(_attack))
            self.attacks = new_attacks

        if len(_weapons) < 1 or type(_weapons[0]) == Weapon:
            # Already converted to list of Weapons
            self.weapons = _weapons
        else:
            new_weapons = []
            for _weapon in _weapons:
                new_weapons.append(dict_to_weapon(_weapon))
            self.weapons = new_weapons

        self.target = None
        self.paid = False

    def add_attribute(self, key, val):
        self.attributes[key] = val

    def get_word(self, replace=True, strip=False):
        end = ""
        if not strip:
            end = " "
        if replace:
            name = self.get_name().replace("-", " ") + end
        else:
            name = self.get_name()
        return Text(name,
                    color=npc_color, tooltip=self.gen_desc())

    def get_type(self):
        """
        :rtype: str
        """
        return self._type

    def tick(self):
        for weapon in self.get_weapons():
            for attack in weapon.get_attacks():
                attack.tick()
        for attack in self.attacks:
            attack.tick()

    def determine_number(self, name_nums, type_nums):
        if self.number == -1:
            if self._type not in type_nums:
                type_nums[self._type] = 0
            type_nums[self._type] += 1

            if self.name in name_nums:
                name_nums[self.name] += 1
                self.number = name_nums[self.name]
            else:
                self.number = 0
                name_nums[self.name] = 1

    def gen_name(self, name_nums, type_nums):
        if "Names" in self.attributes:
            names = list(filter(lambda x: x not in name_nums,
                                self.get_attribute("Names")))
            if len(names) > 0:
                self.name = random.choice(names)
            else:
                self.name = random.choice(self.get_attribute("Names"))
        self.determine_number(name_nums, type_nums)

    def add_attacks(self, _attacks):
        self.attacks += _attacks

    def copy(self):
        """Returns a copy of this NPC"""
        _attacks = []
        for _attack in self.attacks:
            _attacks.append(_attack.copy())
        _weapons = []
        for _weapon in self.weapons:
            _weapons.append(_weapon.copy())
        npc = NPC(self.name, self._type, self.health_stats, self.aggressiveness,
                  _attacks, _weapons, self.description, self.attributes)
        npc.target = self.target
        npc.number = self.number
        npc.paid = self.paid
        return npc

    def get_name(self):
        name = self.name
        if "Story-Teller" in self.attributes and not self.paid:
            name = "Story-Teller"
        if self.number != -1 and self.number != 0:
            return name + "-" + str(self.number)
        return name

    def get_target(self, targets, is_camo=False, is_camo_plus=False):
        not_found = True
        for _target in targets:
            if _target == self.target or (
                    _target != "You" and _target.get_name()
                == self.target):
                not_found = False
                break
        if isinstance(self.target, type(None)) or not_found:
            if len(targets) > 0:
                target = random.choice(targets)
                agg = self.aggressiveness
                if target == "You":
                    if is_camo_plus:
                        agg = self.aggressiveness // 100
                    elif is_camo:
                        agg = self.aggressiveness // 2
                if random.randint(0, 100) <= agg - 1:
                    self.target = (
                    target if target == "You" else target.get_name())
                else:
                    self.target = None
            else:
                self.target = None
        return self.target

    def get_attributes(self):
        return self.attributes

    def get_attribute(self, att):
        return self.attributes[att]

    def gen_desc(self):
        """Generates a description based on stats"""

        if self.name == "yourself":
            raise Exception("Use game_save.get_stats_tooltip() instead for "
                            "player")
        if "Story-Teller" in self.attributes and not self.paid:
            return [Text("A wizened teller of tales.", new_line=True)]

        if not isinstance(self.description, type(None)):
            desc = [Text(self.description, new_line=True),
                    Text("", new_line=True)]
        else:
            desc = []

        desc += [Text("Health", new_line=True, color=header_color, bold=True,
                      font_size=header_size)]

        for stat in self.health_stats:
            desc += [Text(stat + ": ", color=header_color),
                     Text(str(self.health_stats[stat]), new_line=True,
                          color=number_color)]

        desc.append(Text("", new_line=True))
        if len(self.attacks) > 0:
            desc.append(Text("Attacks", new_line=True, color=header_color,
                             font_size=header_size, bold=True))
        total_prob = 0
        for _attack in self.attacks:
            total_prob += _attack.choice_probability
        for _attack in self.attacks:
            desc += _attack.gen_desc(total_prob=total_prob)

        return desc

    def get_health(self):
        return self.health_stats

    def set_health(self, health_stats):
        self.health_stats = health_stats

    def get_weapons(self):
        return self.weapons

    def get_attacks(self, tame=False):
        if tame:
            new_attacks = []
            for attack in self.attacks:
                attack = attack.copy()
                attack.reset_cooldown()
                attack.name = self._type + ":" + attack.name
                new_attacks.append(attack)
            return new_attacks
        return self.attacks

    def attack(self, stats, attack, weapon):
        """Attacks the target with damage stats"""

        if not isinstance(attack, type(None)):
            choices = [attack]
            choice_weights = [1]
            _weapons = [weapon]
        else:
            choices = []
            _weapons = []
            choice_weights = []
            for _attack in self.attacks:
                if _attack.current_cooldown <= 0 and \
                        not (_attack.ammo > 0 and _attack.current_ammo < 1):
                    if _attack.choice_probability > 0:
                        choices.append(_attack)
                        _weapons.append(None)
                        choice_weights.append(_attack.choice_probability)
            for _weapon in self.weapons:
                for _attack in _weapon.get_attacks():
                    if _attack.current_cooldown <= 0 and \
                            not (_attack.ammo > 0 and _attack.current_ammo < 1):
                        if _attack.choice_probability > 0:
                            choices.append(_attack)
                            _weapons.append(_weapon)
                            choice_weights.append(_attack.choice_probability)

        multiattack = False
        if len(choices) > 0:
            chosen_attack = weighted_choice(choices, choice_weights)
            _weapon = _weapons[choices.index(chosen_attack)]
            stats, damages = chosen_attack.attack(stats.copy())
            if chosen_attack.current_cooldown < 0:
                multiattack = True
            if chosen_attack.cooldown < 0 and chosen_attack.current_cooldown == 0:
                chosen_attack.current_cooldown = chosen_attack.cooldown
            return stats, damages, chosen_attack, _weapon, multiattack
        else:
            return stats, "Recovering", None, None, multiattack

    def check_if_dead(self):
        dead_healths = []
        for stat in self.get_health():
            if self.get_health()[stat] <= 0 and stat != "Agility" and stat != "Charisma":
                dead_healths.append(stat)
        return len(dead_healths) > 0, \
               ("Tame" in dead_healths or "Tame+" in dead_healths or "Tame2+" in dead_healths), \
               ("Life" in dead_healths or "Soul" in dead_healths)


class Attack(object):
    """Stores information relating to NPC Attack moves

    :type name: str
    :type choice_probability: int
    :type hit_probability: int
    :type damages: dict | None
    :type probabilities: dict | None
    :type effectiveness: dict | None
    """

    def __init__(self, name, past_tense, choice_probability=100,
                 hit_probability=100,
                 cooldown=0, damages=None, probabilities=None,
                 effectiveness=None, attributes=None, ammo=0):
        self.name = name
        self.past_tense = past_tense
        self.choice_probability = choice_probability
        self.hit_probability = hit_probability
        self.cooldown = cooldown

        if self.cooldown > 0:
            self.cooldown += 1
        if self.cooldown < 0:
            self.cooldown -= 1

        if isinstance(damages, type(None)):
            self.damages = {}
        else:
            self.damages = damages
        if isinstance(probabilities, type(None)):
            self.probabilities = {}
        else:
            self.probabilities = probabilities
        if isinstance(effectiveness, type(None)):
            self.effectiveness = {}
        else:
            self.effectiveness = effectiveness
        if isinstance(attributes, type(None)):
            self.attributes = {}
        else:
            self.attributes = attributes

        self.current_cooldown = None
        self.reset_cooldown(True)

        self.ammo = ammo
        self.current_ammo = self.ammo

    def reset_cooldown(self, first=False):
        if "Cooldown" not in self.attributes or first:
            if self.cooldown < 0:
                self.current_cooldown = self.cooldown
            else:
                self.current_cooldown = 0

    def decrease_cooldown(self):
        self.cooldown -= 1
        if self.cooldown < 0:
            self.current_cooldown = self.cooldown

    def display_current_cooldown(self):
        return self.current_cooldown

    def display_cooldown(self):
        return self.cooldown

    def copy(self):
        """Returns a copy of this attack"""
        cooldown = self.cooldown
        if self.cooldown > 0:
            cooldown -= 1
        elif self.cooldown < 0:
            cooldown += 1
        attack = Attack(self.name, self.past_tense, self.choice_probability,
                        self.hit_probability, cooldown, self.damages,
                        self.probabilities, self.effectiveness,
                        self.attributes, self.ammo)
        attack.current_cooldown = self.current_cooldown
        attack.current_ammo = self.current_ammo
        return attack

    def get_name(self):
        return self.name

    def tick(self):
        """Decrements cooldown"""
        ready = False
        if self.cooldown > 0:
            if self.current_cooldown == 1:
                ready = True
            self.current_cooldown -= 1
            if self.current_cooldown < 0:
                self.current_cooldown = 0
        return ready

    def gen_desc(self, weapon=None, show_title=True, total_prob=None,
                 flower=False):
        """Generates a description based on stats"""
        desc = []
        if not isinstance(weapon, type(None)):
            desc = [Text(weapon.get_name(), color=header_color,
                         font_size=header_size, new_line=True),
                    Text("", new_line=True)]
        if show_title:
            desc.append(
                Text(self.name, new_line=True, bold=True, color=header_color))
        if not isinstance(total_prob, type(None)):
            desc += [Text("Choice Probability: "),
                     Text(str(
                         int(self.choice_probability / total_prob * 100)) + "%",
                          color=number_color, new_line=True)]
        if not flower:
            desc += [Text("Hit Probability: "),
                     Text(str(self.hit_probability), color=number_color,
                          new_line=True),
                     Text("Cooldown: "),
                     Text(str(self.display_cooldown()), color=number_color,
                          new_line=True),
                     Text("Current Cooldown: "),
                     Text(str(self.display_current_cooldown()),
                          color=number_color,
                          new_line=True)]
            if "Consumable" in self.attributes:
                desc += [Text("Weapon destroyed on use.", new_line=True)]
            if "Thrown" in self.attributes:
                desc += [Text("Weapon dropped on use.", new_line=True)]

            if self.ammo > 0:
                desc += [Text("Ammo: "), Text(str(self.current_ammo),
                                              color=number_color,
                                              new_line=True)]

            weapon_name = ""
            if not isinstance(weapon, type(None)):
                weapon_name = weapon.get_name()

            for stat in self.damages:
                # Add probability description
                prob_desc = []
                if not isinstance(self.probabilities, type(None)):
                    if stat in self.probabilities:
                        prob_desc += [Text(", Probability: "),
                                      Text(str(self.probabilities[stat]),
                                           color=number_color)]
                    else:
                        raise Exception(f"{weapon_name}, {self.name}: " + stat + " needs probability")

                # Add effectiveness description
                effect_desc = []
                if not isinstance(self.effectiveness, type(None)):
                    if stat in self.effectiveness:
                        effect_desc += [Text(", Effectiveness: "),
                                        Text(str(self.effectiveness[stat]),
                                             color=number_color)]
                    else:
                        raise Exception(f"{weapon_name}, {self.name}: " + stat + " needs effectiveness")

                desc += [Text(stat + ": ", color=header_color),
                         Text(str(self.damages[stat]), color=number_color)]
                desc += prob_desc
                desc += effect_desc
                desc.append(Text("", new_line=True))
        desc.append(Text("", new_line=True))
        return desc

    def attack(self, stats, is_player=False, boosts=None, accurate=0):
        """Decrements given stats by self stats

        :type stats: dict
        """
        if self.cooldown > 0:
            self.current_cooldown = self.cooldown
        else:
            self.current_cooldown += 1
            if self.current_cooldown > 0:
                self.current_cooldown = 0
        if self.ammo > 0:
            self.current_ammo -= 1

        if accurate > 0:
            mult = 2
        else:
            mult = 1
        if random.randint(1, 100) > self.hit_probability*mult and not is_player:
            return stats, {}  # Missed

        new_stats = {}
        for stat in stats:
            new_stats[stat] = stats[stat]

        damages = {}
        for stat in self.damages:

            # Check if hit
            if not isinstance(self.probabilities, type(None)):
                if random.randint(0, 100) > \
                                self.probabilities[stat] - 1:
                    continue  # Stat Missed

            # Determine effectiveness
            max_damage = self.damages[stat]
            if not isinstance(self.effectiveness, type(None)):
                if max_damage > 0:
                    damage = random.randint(
                        max_damage * (self.effectiveness[stat] / 100),
                        max_damage)
                else:
                    damage = random.randint(max_damage,
                                            max_damage *
                                            (self.effectiveness[stat] / 100))
            else:
                damage = random.randint(0, max_damage)

            # Stat is in weapon's stats
            if stat not in new_stats:
                if stat != "Divine" and "+" not in stat and damage != 0 and \
                        not (stat == "Tame" and is_player):
                    new_stats[stat] = 0
            if stat in new_stats:
                if not isinstance(boosts, type(None)) and stat in boosts:
                    damage *= boosts[stat]
                new_stats[stat] -= damage  # Hit
                damages[stat] = damage

        return new_stats, damages

    def get_attributes(self):
        return self.attributes


class Weapon(object):
    """Weapons used by player and NPCs"""

    def __init__(self, name="", _attacks=None, attributes=None, description=""):
        if isinstance(_attacks, type(None)):
            self.attacks = []
        else:
            self.attacks = _attacks
        if isinstance(attributes, type(None)):
            self.attributes = {}
        else:
            self.attributes = attributes
        self.name = name
        self._type = self.name
        if "Names" in self.attributes:
            if self.name not in self.attributes["Names"]:
                self.name = random.choice(self.attributes["Names"])
        self.description = description

    def reset_cooldowns(self):
        for attack in self.attacks:
            attack.reset_cooldown()

    def get_type(self):
        return self._type

    def gen_desc(self, flower=False):
        desc = [Text(self.description, new_line=True)]
        if len(self.attacks) > 0:
            desc += [Text("", new_line=True),
                     Text("Attacks", new_line=True, color=header_color,
                          font_size=header_size, bold=True)]
        for _attack in self.attacks:
            desc += _attack.gen_desc(flower=flower)
        return desc

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_attacks(self):
        return self.attacks

    def get_attributes(self):
        return self.attributes

    def set_attribute(self, att, val):
        self.attributes[att] = val

    def get_attribute(self, att):
        return self.attributes[att]

    def copy(self, keep_name=True):
        _attacks = []
        for _attack in self.attacks:
            _attacks.append(_attack.copy())
        if keep_name:
            name = self.name
        else:
            name = ""
        return Weapon(name, _attacks, self.attributes, self.description)


class Location(object):
    """Stores information relating to locations"""

    def __init__(self, name, probability=100, treasure=None,
                 weapons=None, NPCs=None, description=None, attributes=None):
        self.attributes = attributes
        self._type = name
        if not isinstance(attributes, type(None)) and "Names" in \
                self.attributes:
            self.name = random.choice(self.attributes["Names"])
        else:
            self.name = name
        self.probability = probability
        if isinstance(treasure, type(None)):
            self.treasure = {"Max": 0, "Min": 0, "Probability": 0}
        else:
            self.treasure = treasure
        if isinstance(weapons, type(None)):
            self.weapons = []
        else:
            self.weapons = weapons
        if isinstance(NPCs, type(None)):
            self.npcs = []
        else:
            self.npcs = NPCs
        if isinstance(description, type(None)):
            self.description = []
        else:
            self.description = description

    def get_name(self):
        return self.name

    def get_type(self):
        return self._type

    def gen_name(self):
        if "Names" in self.attributes:
            self.name = random.choice(self.attributes["Names"])

    def gen_desc(self):
        text_list = []
        if not isinstance(self.description, type(None)):
            text_list.append(Text(self.description, new_line=True))
        text_list += [Text("", new_line=True),
                      Text("Treasure: ", color=header_color), Text(" Max: "),
                      Text(str(self.treasure["Max"]), color=number_color),
                      Text(", Min: "), Text(str(self.treasure["Min"]),
                                            color=number_color),
                      Text(", Probability: "),
                      Text(str(self.treasure["Probability"]),
                           color=number_color)]
        return text_list

    def get_attributes(self):
        return self.attributes

    @staticmethod
    def gen_objects(location_object_list, wander=False, current_amounts=None):
        if isinstance(current_amounts, type(None)):
            current_amounts = {}
        current_items = []
        for location_object in location_object_list:
            if type(location_object.contained_object) == NPC:
                npc = location_object.contained_object
                amount = 0
                if npc.get_type() in current_amounts:
                    amount = current_amounts[npc.get_type()]
                num = location_object.gen_number(wander, amount)
            else:
                num = location_object.gen_number()
            for i in range(0, num):
                current_items.append(location_object.contained_object)
        return current_items


class LocationObject(object):
    """Stores probability info for each item at a location

    :type contained_object: NPC | Weapons | Gear
    :type probability: int | float
    :type fraction: int | float
    """

    def __init__(self, contained_object, probability=100, fraction=2, _max=10):
        self.contained_object = contained_object
        self.probability = probability
        self.fraction = fraction
        self.max = _max
        self.current_prob = self.probability

    def gen_number(self, wander=False, current_num=0):
        """Determines a number of objects based on probability and fraction

        :param wander: Resets probability
        :param current_num: Checks if max num reached
        """
        if not wander:
            self.current_prob = self.probability
        elif self.current_prob == self.probability:
            if self.fraction >= 1:
                self.current_prob /= (self.fraction * 2)
            else:
                self.current_prob *= (self.fraction / 2)  # Do not want wandering in to have greater chance than spawning in

        num = 0
        while True:
            if (self.current_prob != 0) and random.uniform(0,
                                                           100 / self.current_prob) <= 1:
                num += 1
                if self.fraction == 0 or (num + current_num >= self.max > 0):
                    if num + current_num > self.max > 0:
                        return 0
                    return num
                fraction_nudge = self.fraction
                if self.fraction < 1:
                    fraction_nudge /= 1.5
                elif self.fraction > 1:
                    fraction_nudge *= 1.5
                self.current_prob /= fraction_nudge
            else:
                return num


def dict_to_attack(attack_info):
    """Converts a dict or str to an Attack

    :type attack_info: dict | str | Attack
    """

    if type(attack_info) == str:
        # Attack name given, get dict from all_attacks
        _attack = list_to_dict(all_attacks)[attack_info]
    else:
        _attack = attack_info

    if not "Ammo" in _attack:
        ammo = 0
    else:
        ammo = _attack["Ammo"]
    return \
        Attack(
            _attack["Name"],
            _attack["Past Tense"],
            _attack["Choice Probability"],
            _attack["Hit Probability"],
            _attack["Cooldown"],
            _attack["Damages"],
            _attack["Effect Probabilities"],
            _attack["Effectiveness"],
            _attack["Attributes"],
            ammo,
        )


def dict_to_weapon(weapon_info):
    """Converts a dict or str to a Weapon

    :type weapon_info: dict | str
    """

    if type(weapon_info) == str:
        _weapon = list_to_dict(all_weapons)[weapon_info]
    else:
        _weapon = weapon_info

    _attacks = []
    for _attack in _weapon["Attacks"]:
        _attacks.append(dict_to_attack(_attack))

    return \
        Weapon(
            _weapon["Name"],
            _attacks,
            _weapon["Attributes"],
            _weapon["Description"]
        )


def dict_to_npc(npc_info):
    """Converts a dict or str to a NPC

    :type npc_info: dict | str
    """

    if type(npc_info) == str:
        npc = list_to_dict(all_npcs)[npc_info]
    else:
        npc = npc_info

    _attacks = []
    for _attack in npc["Attacks"]:
        _attacks.append(dict_to_attack(_attack))

    _weapons = []
    for _weapon in npc["Weapons"]:
        _weapons.append(dict_to_weapon(_weapon))

    return \
        NPC(
            npc["Name"],
            None,
            npc["Health"],
            npc["Aggressiveness"],
            _attacks,
            _weapons,
            npc["Description"],
            npc["Attributes"]
        )


def dict_to_location_object(location_object_info):
    """Converts a dict or str to a LocationObject

    :type location_object_info: dict | str
    """

    if type(location_object_info) == str:
        location_object = list_to_dict(all_locations_objects)[
            location_object_info]
    else:
        location_object = location_object_info

    npcs = list_to_dict(all_npcs)
    weapons = list_to_dict(all_weapons)

    name = location_object["Name"]

    if name in npcs:
        contained_object = dict_to_npc(name)
    elif name in weapons:
        contained_object = dict_to_weapon(name)
    else:
        raise Exception(name + " is not in weapons or npcs")

    return \
        LocationObject(
            contained_object,
            location_object["Probability"],
            location_object["Fraction"],
            location_object["Max"],
        )


def dict_to_location(location_info):
    """Converts a dict or str to a Location

    :type location_info: dict | str
    """

    if type(location_info) == str:
        _location = list_to_dict(all_locations)[location_info]
    else:
        _location = location_info

    npcs = []
    for npc in _location["NPCs"]:
        npcs.append(dict_to_location_object(npc))

    _weapons = []
    for _weapon in _location["Weapons"]:
        _weapons.append(dict_to_location_object(_weapon))

    return \
        Location(
            _location["Name"],
            _location["Probability"],
            _location["Treasure"],
            _weapons,
            npcs,
            _location["Description"],
            _location["Attributes"]
        )


all_attacks = get_value("game_objects", "attacks")
all_weapons = get_value("game_objects", "weapons")
all_npcs = get_value("game_objects", "npcs")
all_locations_objects = get_value("game_objects", "location objects")
all_locations = get_value("game_objects", "locations")

ambrosia = dict_to_weapon(list_to_dict(all_weapons)["Ambrosia"])
treasure = dict_to_weapon(list_to_dict(all_weapons)["Treasure"])
bestiary = dict_to_weapon(list_to_dict(all_weapons)["Bestiary"])
anthology = dict_to_weapon(list_to_dict(all_weapons)["Herbal-Anthology"])
cook_book = dict_to_weapon(list_to_dict(all_weapons)["Cook-Book"])
dagger = dict_to_weapon(list_to_dict(all_weapons)["Dagger"])
atlas = dict_to_weapon(list_to_dict(all_weapons)["Atlas"])
cooked_meal = dict_to_weapon(list_to_dict(all_weapons)["Cooked-Meal"])
hrunting = dict_to_weapon(list_to_dict(all_weapons)["Hrunting"])
hrothgars_gift = dict_to_weapon(list_to_dict(all_weapons)["Hrothgar's-Gift"])
finely_cooked_meal = dict_to_weapon(list_to_dict(all_weapons)["Finely-Cooked-Meal"])
mead = dict_to_weapon(list_to_dict(all_weapons)["Mead"])
gold_ingot = dict_to_weapon(list_to_dict(all_weapons)["Gold-Ingot"])
adamantine_blade = dict_to_weapon(list_to_dict(all_weapons)["Adamantine-Blade"])
cerastes = dict_to_npc(list_to_dict(all_npcs)["Cerastes"])
spartae = dict_to_npc(list_to_dict(all_npcs)["Spartae"])
minotaur = dict_to_npc(list_to_dict(all_npcs)["Minotaur"])
monks_dogs = dict_to_npc(list_to_dict(all_npcs)["Monk\'s-Dog"])
grendel = dict_to_npc(list_to_dict(all_npcs)["Grendel"])

LOCATIONS_LIST = []
for location in all_locations:
    LOCATIONS_LIST.append(dict_to_location(location))

LOCATIONS_DICT = list_to_dict(LOCATIONS_LIST)
WEAPONS_LIST = [dict_to_weapon(weapon) for weapon in all_weapons]
EVERYTHING_LIST = WEAPONS_LIST + [dict_to_npc(npc) for npc in all_npcs]
