"""
Contains the default strings to write to respective config files.
Strings must contain dicts
"""

# Indenting strings skews formatting in config files
display = \
    "{ \n\
        'default_font': '(corbel, monospace)', \n\
        'default_color': (255, 255, 255), \n\
        'default_font_size': 20, \n\
        'lines_per_scroll': 3, \n\
        'min_scroll_bar_height': .125, \n\
        'scroll_bar_width': 20, \n\
        'priority_word_wrap_chars': [' ', '-', '_', '.', ',', '?', '!'], \n\
        'fps': 60, \n\
        'resolution': [1000, 600], \n\
    }"

input = \
    "{ \n\
        'unshifted keys': '`1234567890-=[];,./\\\\\\\'', \n\
        'shifted keys':   '~!@#$%^&*()_+{}:<>?|\\\"', \n\
        'key tick': 5, \n\
        'key repeat delay': 20, \n\
        'max keys pressed': 3, \n\
        'alt_hold_time': 200, \n\
    }"

keyboard_hotkeys = \
    "{ \n\
        'q': 'Game', \n\
        'w': 'Inventory', \n\
        'e': 'Surroundings', \n\
        't': 'Attacks', \n\
        'r': 'Stats>You', \n\
        'a': 'Surroundings>Leave-Location', \n\
        's': 'Surroundings>Wait', \n\
    }"

mouse_hotkeys = \
    "{ \n\
        '6': 'Back', \n\
        '7': 'Surroundings>Wait', \n\
    }"

customization = \
    "{ \n\
        'input_color': (117, 113, 94), \n\
        'prompt_color': (166, 226, 46), \n\
        'status_color': (255, 255, 255), \n\
        'has_tooltip_color': (57, 69, 84), \n\
        'number_color': (88, 147, 255), \n\
        'background_color': (30, 35, 42), \n\
        'header_color': (230, 219, 110), \n\
        'header_size': 24, \n\
        'border_color': (50, 50, 50), \n\
        'path_font_size': 18, \n\
        'path_font': '(monospace)', \n\
        'choice_font': '(corbel, monospace)', \n\
        'choice_font_size': 40, \n\
        'border_size': 1, \n\
    }"

save = \
    "{ \n\
        'saves_path': '~Game Root~/Saves/', \n\
        'extension': 'save', \n\
    }"

game_customization = \
    "{ \n\
        'location_color': (59, 180, 82), \n\
        'weapon_color': (102, 217, 239), \n\
        'treasure_color': (253, 138, 40), \n\
        'inventory_color': (150, 113, 184), \n\
        'npc_color': (249, 38, 114), \n\
        'dead_font': '(comic sans ms, monospace)', \n\
        'dead_font_size': 36, \n\
        'dead_color': (116, 58, 58), \n\
        'cooldown_color': (204, 104, 88), \n\
        'multiattack_color': (92, 167, 202), \n\
        'self_color': (237, 189, 6), \n\
        'attack_color': (169, 183, 198), \n\
    }"

game_objects = \
    "{ \n\
        'weapons': \n\
            [ \n\
                { \n\
                    'Name': 'Dagger', \n\
                    'Description': 'A small but fast blade.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Slash', \n\
                                'Past Tense': 'slashed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 60, \n\
                                'Cooldown': -2, \n\
                                'Damages': {'Sharp': 150}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 50}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Stab', \n\
                                'Past Tense': 'stabbed', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': -1, \n\
                                'Damages': {'Sharp': 170}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Throw-At', \n\
                                'Past Tense': 'hit', \n\
                                'Choice Probability': 20, \n\
                                'Hit Probability': 60, \n\
                                'Cooldown': -2, \n\
                                'Damages': {'Sharp': 400}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 100}, \n\
                                'Attributes': {'Thrown': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Amazonian-Dagger', \n\
                    'Description': 'A small but fast blade with a milky liquid dripping from its tip.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Slash', \n\
                                'Past Tense': 'slashed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 60, \n\
                                'Cooldown': -2, \n\
                                'Damages': {'Sharp': 150, 'Agility': 20}, \n\
                                'Effect Probabilities': {'Sharp': 100, 'Agility': 100}, \n\
                                'Effectiveness': {'Sharp': 50, 'Agility': 50}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Stab', \n\
                                'Past Tense': 'stabbed', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': -1, \n\
                                'Damages': {'Sharp': 170, 'Agility': 20}, \n\
                                'Effect Probabilities': {'Sharp': 100, 'Agility': 100}, \n\
                                'Effectiveness': {'Sharp': 80, 'Agility': 60}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Throw-At', \n\
                                'Past Tense': 'hit', \n\
                                'Choice Probability': 20, \n\
                                'Hit Probability': 60, \n\
                                'Cooldown': -2, \n\
                                'Damages': {'Sharp': 400, 'Agility': 20}, \n\
                                'Effect Probabilities': {'Sharp': 100, 'Agility': 100}, \n\
                                'Effectiveness': {'Sharp': 100, 'Agility': 60}, \n\
                                'Attributes': {'Thrown': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Jeweled-Dagger', \n\
                    'Description': 'An intricate dagger of jewels white and gold.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Stick', \n\
                                'Past Tense': 'stuck', \n\
                                'Choice Probability': 1, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Sharp': 20000}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 100}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Ritual-Dagger', \n\
                    'Description': 'Very light. A wicked dagger of black rock; inscribed with odd symbols.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Slash', \n\
                                'Past Tense': 'slashed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': -4, \n\
                                'Damages': {'Sharp': 200}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Stab', \n\
                                'Past Tense': 'stabbed', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': -2, \n\
                                'Damages': {'Sharp': 300}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Throw-At', \n\
                                'Past Tense': 'hit', \n\
                                'Choice Probability': 20, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': -2, \n\
                                'Damages': {'Sharp': 350}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 90}, \n\
                                'Attributes': {'Thrown': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Xiphos', \n\
                    'Description': 'A sword with a short but reliable blade of iron.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Slash', \n\
                                'Past Tense': 'slashed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Sharp': 400}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Stab', \n\
                                'Past Tense': 'stabbed', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': 1, \n\
                                'Damages': {'Sharp': 600}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 70}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Bident', \n\
                    'Description': 'A two-pronged pitch-fork.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Stab', \n\
                                'Past Tense': 'stabbed', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': 1, \n\
                                    'Damages': {'Sharp': 1000}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Harpe', \n\
                    'Description': 'A blade of iron with a sickle-like protrusion near the end.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Slash', \n\
                                'Past Tense': 'slashed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Sharp': 600}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Maim', \n\
                                'Past Tense': 'maimed', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': 1, \n\
                                'Damages': {'Sharp': 800}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 70}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Hrunting', \n\
                    'Description': '\\'... a rare and ancient sword named Hrunting. The iron blade with its ill-boding patterns had been tempered in blood.\\'', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Slash', \n\
                                'Past Tense': 'slashed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Sharp': 1000}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Stab', \n\
                                'Past Tense': 'stabbed', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': 1, \n\
                                'Damages': {'Sharp': 1700}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 70}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Naegling', \n\
                    'Description': '\\'... ancient and silver-streaked.\\' A gift from King Hygelac for defeating the beast and its mother.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Slash', \n\
                                'Past Tense': 'slashed', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Sharp': 4000}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Stab', \n\
                                'Past Tense': 'stabbed', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': 1, \n\
                                'Damages': {'Sharp': 6800}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 70}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Hrothgar\\'s-Gift', \n\
                    'Description': '\\'...the renowned treasure-sword.\\' A gift from King Hrothgar for defeating the beast.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Slash', \n\
                                'Past Tense': 'slashed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Sharp': 2000}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Stab', \n\
                                'Past Tense': 'stabbed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': 1, \n\
                                'Damages': {'Sharp': 3400}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Kopis', \n\
                    'Description': 'A sleek sword with a curved blade.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Slash', \n\
                                'Past Tense': 'slashed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': -1, \n\
                                'Damages': {'Sharp': 400}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Stab', \n\
                                'Past Tense': 'stabbed', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Sharp': 600}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 70}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Gold-Ingot', \n\
                    'Description': 'An item of great value.', \n\
                    'Attacks': \n\
                        [ \n\
                        ], \n\
                    'Attributes': {'Treasure': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Toxa', \n\
                    'Description': 'A short bow.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Shoot', \n\
                                'Past Tense': 'shot', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 40, \n\
                                'Cooldown': 2, \n\
                                'Ammo': 10, \n\
                                'Damages': {'Sharp': 600}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Eros\\'s-Bow', \n\
                    'Description': 'A divine bow of lightly tinted red. Said to cause ardor or animosity.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Shoot', \n\
                                'Past Tense': 'shot', \n\
                                'Choice Probability': 1, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': 2, \n\
                                'Ammo': 0, \n\
                                'Damages': {'Tame': 50000}, \n\
                                'Effect Probabilities': {'Tame': 100}, \n\
                                'Effectiveness': {'Tame': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Shoot', \n\
                                'Past Tense': 'shot', \n\
                                'Choice Probability': 2, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': 2, \n\
                                'Ammo': 0, \n\
                                'Damages': {}, \n\
                                'Effect Probabilities': {}, \n\
                                'Effectiveness': {}, \n\
                                'Attributes': {'Enrage': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'?': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Amazonian-Bow', \n\
                    'Description': 'A poisoned short bow.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Shoot', \n\
                                'Past Tense': 'shot', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 40, \n\
                                'Cooldown': 2, \n\
                                'Ammo': 10, \n\
                                'Damages': {'Sharp': 600, 'Agility': 50}, \n\
                                'Effect Probabilities': {'Sharp': 100, 'Agility': 100}, \n\
                                'Effectiveness': {'Sharp': 80, 'Agility': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Horn-of-Plenty', \n\
                    'Description': 'A cornucopia. It overflows with Ambrosia.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Produce-Ambrosia', \n\
                                'Past Tense': 'healed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 10, \n\
                                'Damages': {'Brute': -2000, 'Sharp': -2000, 'Burn': -1000, 'Freeze': -1200, 'Agility': -50}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Agility': 100}, \n\
                                'Effectiveness': {'Brute': 80, 'Sharp': 80, 'Burn': 90, 'Freeze': 80, 'Agility': 100}, \n\
                                'Attributes': {'Cooldown': True, 'Self': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Rod-of-Asclepius', \n\
                    'Description': 'A powerful staff entwined with serpents. Its power is only available to you in times of need.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Heal', \n\
                                'Past Tense': 'healed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 2, \n\
                                'Damages': {}, \n\
                                'Effect Probabilities': {}, \n\
                                'Effectiveness': {}, \n\
                                'Attributes': {'Self': True, 'Rod': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Caduceus', \n\
                    'Description': 'A divine staff entwined with serpents.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Sleep', \n\
                                'Past Tense': 'slept', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {}, \n\
                                'Effect Probabilities': {}, \n\
                                'Effectiveness': {}, \n\
                                'Attributes': {'Calm': True}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Knock', \n\
                                'Past Tense': 'knocked', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 90, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Divine': 200, 'Brute': 1000}, \n\
                                'Effect Probabilities': {'Divine': 100, 'Brute': 100}, \n\
                                'Effectiveness': {'Divine': 80, 'Brute': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Inspire', \n\
                                'Past Tense': 'inspired', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {}, \n\
                                'Effect Probabilities': {}, \n\
                                'Effectiveness': {}, \n\
                                'Attributes': {'Self': True, 'Speed': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Staff', \n\
                    'Description': 'A nice staff of hard wood.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Beat', \n\
                                'Past Tense': 'beat', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 90, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': 500}, \n\
                                'Effect Probabilities': {'Brute': 100}, \n\
                                'Effectiveness': {'Brute': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Archimedes\\'s-Mirror', \n\
                    'Description': 'A large mirror capable of focusing sun rays on a point.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Burn', \n\
                                'Past Tense': 'burned', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 90, \n\
                                'Cooldown': 1, \n\
                                'Damages': {'Burn': 1000}, \n\
                                'Effect Probabilities': {'Burn': 100}, \n\
                                'Effectiveness': {'Burn': 60}, \n\
                                'Attributes': {'Cooldown': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Triton\\'s-Conch-Shell', \n\
                    'Description': 'An elegant shell of white and blue capable of commanding the sea.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Freeze', \n\
                                'Past Tense': 'froze', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 90, \n\
                                'Cooldown': 2, \n\
                                'Damages': {'Freeze': 1000}, \n\
                                'Effect Probabilities': {'Freeze': 100}, \n\
                                'Effectiveness': {'Freeze': 60}, \n\
                                'Attributes': {'Cooldown': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Kryo', \n\
                    'Description': 'A slick blade of ice.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Slash', \n\
                                'Past Tense': 'slashed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 90, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Freeze': 700, 'Sharp': 600}, \n\
                                'Effect Probabilities': {'Freeze': 100, 'Sharp': 100}, \n\
                                'Effectiveness': {'Freeze': 90, 'Sharp': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Torch', \n\
                    'Description': 'Put it out, you fools! Put it out!', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Burn', \n\
                                'Past Tense': 'burned', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 90, \n\
                                'Cooldown': -1, \n\
                                'Ammo': 5, \n\
                                'Damages': {'Burn': 700}, \n\
                                'Effect Probabilities': {'Burn': 100}, \n\
                                'Effectiveness': {'Burn': 20}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Rota-Fortunae', \n\
                    'Description': 'A wooden wheel with symbols inscribed throughout.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Spin-Wheel-For', \n\
                                'Past Tense': 'let the gods decided the fate of', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 2, \n\
                                'Damages': {'Brute': 2000, 'Sharp': 2000, 'Burn': 1000, 'Freeze': 1200}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100}, \n\
                                'Effectiveness': {'Brute': 10, 'Sharp': 10, 'Burn': 10, 'Freeze': 10}, \n\
                                'Attributes': {'Cooldown': True, 'Self': True, 'Rota': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Ambrosia', \n\
                    'Description': 'The Nectar of the Gods.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Consume', \n\
                                'Past Tense': 'healed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -2000, 'Sharp': -2000, 'Burn': -1000, 'Freeze': -1200, 'Agility': -50}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Agility': 100}, \n\
                                'Effectiveness': {'Brute': 80, 'Sharp': 80, 'Burn': 90, 'Freeze': 80, 'Agility': 90}, \n\
                                'Attributes': {'Consumable': True, 'Self': True}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Tame', \n\
                                'Past Tense': 'calmed', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Tame': 5000}, \n\
                                'Effect Probabilities': {'Tame': 100}, \n\
                                'Effectiveness': {'Tame': 1}, \n\
                                'Attributes': {'Consumable': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Mead', \n\
                    'Description': '\\'Mead,\\' said Wednesday. \\'Honey wine. The drink of heroes. The drink of the gods.\\'', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Drink', \n\
                                'Past Tense': 'inebriated', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -900, 'Freeze': -1000}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Freeze': 100}, \n\
                                'Effectiveness': {'Brute': 10, 'Freeze': 10}, \n\
                                'Attributes': {'Consumable': True, 'Self': True, 'Mead': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Cooked-Meal', \n\
                    'Description': 'A crisply cooked leg-of-lamb.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Eat', \n\
                                'Past Tense': 'filled', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -1000, 'Sharp': -1000, 'Burn': -400, 'Freeze': -400}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100}, \n\
                                'Effectiveness': {'Brute': 10, 'Sharp': 10, 'Burn': 10, 'Freeze': 10}, \n\
                                'Attributes': {'Consumable': True, 'Self': True, 'Mead': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Finely-Cooked-Meal', \n\
                    'Description': 'A mouth-watering, crisply cooked leg-of-lamb.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Eat', \n\
                                'Past Tense': 'filled', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -1500, 'Sharp': -1500, 'Burn': -1000, 'Freeze': -1000}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100}, \n\
                                'Effectiveness': {'Brute': 50, 'Sharp': 50, 'Burn': 50, 'Freeze': 50}, \n\
                                'Attributes': {'Consumable': True, 'Self': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Panacea', \n\
                    'Description': 'Ambrosia made Divine. A Cure All for the Gods.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Consume', \n\
                                'Past Tense': 'healed', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -8000, 'Sharp': -8000, 'Burn': -5000, 'Freeze': -6000, 'Agility': -500, 'Divine': -5000}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Agility': 100, 'Divine': 100}, \n\
                                'Effectiveness': {'Brute': 80, 'Sharp': 80, 'Burn': 90, 'Freeze': 80, 'Agility': 100, 'Divine': 100}, \n\
                                'Attributes': {'Consumable': True, 'Self': True}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Tame', \n\
                                'Past Tense': 'calmed', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Tame': 50000}, \n\
                                'Effect Probabilities': {'Tame': 100}, \n\
                                'Effectiveness': {'Tame': 10}, \n\
                                'Attributes': {'Consumable': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Water-of-Langia', \n\
                    'Description': 'An encrusted goblet of gold, brimming with a nearly invisible liquid.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Consume', \n\
                                'Past Tense': 'healed', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Divine': -10000}, \n\
                                'Effect Probabilities': {'Divine': 100}, \n\
                                'Effectiveness': {'Divine': 1}, \n\
                                'Attributes': {'Consumable': True, 'Self': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Ichor', \n\
                    'Description': 'The Life Blood of the Gods', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Consume', \n\
                                'Past Tense': 'healed', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -10000, 'Sharp': -10000, 'Burn': -10000, 'Freeze': -10000, 'Divine': -100000}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Divine': 100}, \n\
                                'Effectiveness': {'Brute': 80, 'Sharp': 80, 'Burn': 90, 'Freeze': 80, 'Divine': 100}, \n\
                                'Attributes': {'Consumable': True, 'Self': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Rock', \n\
                    'Description': 'A naturally occurring solid aggregate of minerals or mineraloids, ya dunce.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Hit', \n\
                                'Past Tense': 'hit', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 90, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': 400}, \n\
                                'Effect Probabilities': {'Brute': 100}, \n\
                                'Effectiveness': {'Brute': 100}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Throw-At', \n\
                                'Past Tense': 'hit', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 30, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': 600}, \n\
                                'Effect Probabilities': {'Brute': 100}, \n\
                                'Effectiveness': {'Brute': 100}, \n\
                                'Attributes': {'Thrown': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Treasure', \n\
                    'Description': 'An item of great value.', \n\
                    'Attacks': \n\
                        [ \n\
                        ], \n\
                    'Attributes': {'Treasure': True, 'Names': ['Peacock-Feather', 'Encrusted-Goblet', 'Ruby-Pendant', 'Sapphire-Ring', 'Silk-Tapestry', 'Cup-of-Apollo', 'Cup-of-Heracles', 'Gold-Coin', 'Orichalcum', 'Adamantine', 'Emerald', 'Gold-Horse-Figurine', 'Pearl-Necklace', 'Ruby', 'Saphire', 'Gold-Bracelet', 'Amethyst', 'Conch-Shell', 'Gold-Necklace', 'Garnet', 'Gold-Bridle', 'Ceremonial-Armor-Piece', 'Encrusted-Hilt', 'Apple-of-Discord', 'Golden-Apple', 'Marble-Bust', 'Jeweled-Figurine', 'Coin-Pouch', 'Jewel-Pouch', 'Encrusted-Jewelery-Box', 'Encrusted-Tome', 'Maplewood-Lyre', 'Ivory-Flute', 'Elaborate-Vase', 'Gilded-Dagger', 'Amarantos-Wreath', 'Gilded-Portrait', 'Pressed-Amarantos-Petal', 'Brand-of-Half-Dane', 'Golden-Banner', 'Adorned-Standard', 'Sword-of-Justice', 'Goblet', 'Gold-Crown', 'Encrusted-Skull', 'Silk-Banner', 'Silk-Quilt', 'Sea-Shell', 'Silk-Garments', 'Fancy-Garments', 'Jeweled-Scarab', 'Encrusted-Rock', 'Gold-Ring', 'Gold-Cutlery', 'Embossed-Brass-Dish']}, \n\
                }, \n\
                { \n\
                    'Name': 'Journal', \n\
                    'Description': 'A journal in which nothing is written. Excellent for keeping stories heard on the road.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                               'Name': 'Transcribe', \n\
                               'Past Tense': 'gave the book to', \n\
                               'Choice Probability': 0, \n\
                               'Hit Probability': 100, \n\
                               'Cooldown': 0, \n\
                               'Damages': {}, \n\
                               'Effect Probabilities': {}, \n\
                               'Effectiveness': {}, \n\
                               'Attributes': {}, \n\
                           }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Boulder', \n\
                    'Description': 'Big rock.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Lob-At', \n\
                                'Past Tense': 'lobbed at', \n\
                                'Choice Probability': 20, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': 9000}, \n\
                                'Effect Probabilities': {'Brute': 100}, \n\
                                'Effectiveness': {'Brute': 60}, \n\
                                'Attributes': { 'Thrown': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Heavy': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Magic-Staff', \n\
                    'Description': 'A mystical staff of finest wood.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Burn', \n\
                                'Past Tense': 'burned', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 60, \n\
                                'Cooldown': 2, \n\
                                'Ammo': 20, \n\
                                'Damages': {'Burn': 300}, \n\
                                'Effect Probabilities': {'Burn': 100}, \n\
                                'Effectiveness': {'Burn': 60}, \n\
                                'Attributes': {'Cooldown': True}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Freeze', \n\
                                'Past Tense': 'froze', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 50, \n\
                                'Cooldown': 2, \n\
                                'Ammo': 20, \n\
                                'Damages': {'Freeze': 400}, \n\
                                'Effect Probabilities': {'Freeze': 100}, \n\
                                'Effectiveness': {'Freeze': 80}, \n\
                                'Attributes': {'Cooldown': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Chaos-Staff', \n\
                    'Description': 'A long black staff with purple inscriptions. Use with caution.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Curse', \n\
                                'Past Tense': 'cursed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': 2, \n\
                                'Ammo': 10, \n\
                                'Damages': {'Sharp': 300, 'Brute': 300, 'Burn': 300, 'Freeze': 300}, \n\
                                'Effect Probabilities': {'Sharp': 50, 'Brute': 50, 'Burn': 50, 'Freeze': 50}, \n\
                                'Effectiveness': {'Sharp': -100, 'Brute': -100, 'Burn': -100, 'Freeze': -100}, \n\
                                'Attributes': {'Cooldown': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Sfendonai', \n\
                    'Description': 'A sling. Expertly crafted.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Shoot', \n\
                                'Past Tense': 'shot at', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 60, \n\
                                'Cooldown': 1, \n\
                                'Ammo': 20, \n\
                                'Damages': {'Brute': 400, 'Sharp': 400}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 70}, \n\
                                'Effectiveness': {'Brute': 80, 'Sharp': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Moly', \n\
                    'Description': 'A flower of pure white.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Consume', \n\
                                'Past Tense': 'used magic protection on', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Burn': -10000, 'Freeze': -10000}, \n\
                                'Effect Probabilities': {'Burn': 100, 'Freeze': 100}, \n\
                                'Effectiveness': {'Burn': 10, 'Freeze': 10}, \n\
                                'Attributes': {'Consumable': True, 'Self': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Flower': 'White'}, \n\
                }, \n\
                { \n\
                    'Name': 'Cerastes-Horns', \n\
                    'Description': 'A flower of pure white.', \n\
                    'Attacks': \n\
                        [], \n\
                    'Attributes': {'Spawn-Cerastes': True, 'Flower': 'White'}, \n\
                }, \n\
                { \n\
                    'Name': 'Poppy', \n\
                    'Description': 'A flower of pale red.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Consume', \n\
                                'Past Tense': 'tranquilized', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Sleep': 0, 'Brute': -1000, 'Sharp': -1000}, \n\
                                'Effect Probabilities': {'Sleep': 0, 'Brute': 100, 'Sharp': 100}, \n\
                                'Effectiveness': {'Sleep': 0, 'Brute': 40, 'Sharp': 40}, \n\
                                'Attributes': {'Consumable': True, 'Self': True, 'Sleep': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Flower': 'Red'}, \n\
                }, \n\
                { \n\
                    'Name': 'Peony', \n\
                    'Description': 'A flower of pale red.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Consume', \n\
                                'Past Tense': 'healed', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Burn': -1000, 'Freeze': -1000, 'Sharp': -500, 'Brute': -500}, \n\
                                'Effect Probabilities': {'Burn': 100, 'Freeze': 100, 'Sharp': 100, 'Brute': 100}, \n\
                                'Effectiveness': {'Burn': 10, 'Freeze': 10, 'Sharp': 10, 'Brute': 10}, \n\
                                'Attributes': {'Consumable': True, 'Self': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Flower': 'Red'}, \n\
                }, \n\
                { \n\
                    'Name': 'Lotus', \n\
                    'Description': 'A flower of pale red.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Consume', \n\
                                'Past Tense': 'tranquilized', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Sleep': 0}, \n\
                                'Effect Probabilities': {'Sleep': 0}, \n\
                                'Effectiveness': {'Sleep': 0}, \n\
                                'Attributes': {'Consumable': True, 'Self': True, 'Sleep+': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Flower': 'Red'}, \n\
                }, \n\
                { \n\
                    'Name': 'Wolf\\'s-Bane', \n\
                    'Description': 'A flower of dull purple.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Consume', \n\
                                'Past Tense': 'poisoned', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Divine': 1000}, \n\
                                'Effect Probabilities': {'Divine': 100}, \n\
                                'Effectiveness': {'Divine': 10}, \n\
                                'Attributes': {'Consumable': True, 'Self': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Flower': 'Purple'}, \n\
                }, \n\
                { \n\
                    'Name': 'Narcissus-Flower', \n\
                    'Description': 'A flower of pure white.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Consume', \n\
                                'Past Tense': 'poisoned', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Divine': 300, 'Agility': 200}, \n\
                                'Effect Probabilities': {'Divine': 100, 'Agility': 100}, \n\
                                'Effectiveness': {'Divine': 60, 'Agility': 50}, \n\
                                'Attributes': {'Consumable': True, 'Self': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Flower': 'White'}, \n\
                }, \n\
                { \n\
                    'Name': 'Hyacinth', \n\
                    'Description': 'A flower of dull purple.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Consume', \n\
                                'Past Tense': 'enchanted', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Divine': 400, 'Burn': 400, 'Freeze': 400, 'Agility': 400}, \n\
                                'Effect Probabilities': {'Divine': 10, 'Burn': 50, 'Freeze': 50, 'Agility': 20}, \n\
                                'Effectiveness': {'Divine': -50, 'Burn': -50, 'Freeze': -50, 'Agility': -50}, \n\
                                'Attributes': {'Consumable': True, 'Self': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Flower': 'Purple'}, \n\
                }, \n\
                { \n\
                    'Name': 'Hemlock', \n\
                    'Description': 'A flower of pure white.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Consume', \n\
                                'Past Tense': 'poisoned', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Divine': 1000}, \n\
                                'Effect Probabilities': {'Divine': 100}, \n\
                                'Effectiveness': {'Divine': 100}, \n\
                                'Attributes': {'Consumable': True, 'Self': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Flower': 'White'}, \n\
                }, \n\
                { \n\
                    'Name': 'Manna-Flower', \n\
                    'Description': 'A flower of pure white.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Consume', \n\
                                'Past Tense': 'healed', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Divine': -1000}, \n\
                                'Effect Probabilities': {'Divine': 100}, \n\
                                'Effectiveness': {'Divine': 100}, \n\
                                'Attributes': {'Consumable': True, 'Self': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Flower': 'White'}, \n\
                }, \n\
                { \n\
                    'Name': 'Panacea-Flower', \n\
                    'Description': 'A flower of deepest crimson.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Consume', \n\
                                'Past Tense': 'healed', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -8000, 'Sharp': -8000, 'Burn': -5000, 'Freeze': -6000, 'Agility': -500, 'Divine': -5000}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Agility': 100, 'Divine': 100}, \n\
                                'Effectiveness': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Agility': 100, 'Divine': 100}, \n\
                                'Attributes': {'Consumable': True, 'Self': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Flower': 'Crimson'}, \n\
                }, \n\
                { \n\
                    'Name': 'Miasma-Flower', \n\
                    'Description': 'A flower of deepest crimson.', \n\
                    'Attacks': \n\
                        [ \n\
                        ], \n\
                    'Attributes': {'Smite': True, 'Flower': 'Crimson'}, \n\
                }, \n\
                { \n\
                    'Name': 'Narthex-Flower', \n\
                    'Description': 'A flower of bright yellow.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Consume', \n\
                                'Past Tense': 'burned', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Burn': 1000}, \n\
                                'Effect Probabilities': {'Burn': 100}, \n\
                                'Effectiveness': {'Burn': 100}, \n\
                                'Attributes': {'Consumable': True, 'Self': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Flower': 'Yellow'}, \n\
                }, \n\
                { \n\
                    'Name': 'Sunflower', \n\
                    'Description': 'A flower of bright yellow.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Consume', \n\
                                'Past Tense': 'healed', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Burn': -1000}, \n\
                                'Effect Probabilities': {'Burn': 100}, \n\
                                'Effectiveness': {'Burn': 1}, \n\
                                'Attributes': {'Consumable': True, 'Self': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Flower': 'Yellow'}, \n\
                }, \n\
                { \n\
                    'Name': 'Ambrosia-Flower', \n\
                    'Description': 'A flower of shimmering gold.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Consume', \n\
                                'Past Tense': 'healed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -2000, 'Sharp': -2000, 'Burn': -1000, 'Freeze': -1200, 'Agility': -50}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Agility': 100}, \n\
                                'Effectiveness': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Agility': 100}, \n\
                                'Attributes': {'Consumable': True, 'Self': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Flower': 'Gold'}, \n\
                }, \n\
                { \n\
                    'Name': 'Amarantos-Flower', \n\
                    'Description': 'A flower of bright yellow.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Consume', \n\
                                'Past Tense': 'hurt', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': 100}, \n\
                                'Effect Probabilities': {'Brute': 100}, \n\
                                'Effectiveness': {'Brute': 100}, \n\
                                'Attributes': {'Consumable': True, 'Self': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Flower': 'Yellow', 'Treasure': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Baetylus', \n\
                    'Description': 'A black stone with veins of glowing red. It pulses.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Absorb', \n\
                                'Past Tense': 'enlivened', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Divine': -10000}, \n\
                                'Effect Probabilities': {'Divine': 100}, \n\
                                'Effectiveness': {'Divine': 10}, \n\
                                'Attributes': {'Consumable': True, 'Self': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Omphalos', \n\
                    'Description': 'A white stone with veins of glowing gold. It pulses.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Absorb', \n\
                                'Past Tense': 'enlivened', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Ammo': 3, \n\
                                'Damages': {}, \n\
                                'Effect Probabilities': {}, \n\
                                'Effectiveness': {}, \n\
                                'Attributes': {'Self': True, 'Omphalos': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Water-of-The-River-Styx', \n\
                    'Description': 'An encrusted goblet of crimson, brimming with a dark liquid.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Tempt', \n\
                                'Past Tense': 'tempted Death for', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': 100000000, 'Sharp': 100000000, 'Burn': 100000000, 'Freeze': 100000000, 'Soul': 100000000, 'Toxin': 100000000, 'Focus': 100000000, 'Life': 100000000, 'Divine': 100000000, 'Mind': -100000000}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Soul': 100, 'Toxin': 100, 'Focus': 100, 'Life': 100, 'Divine': 100, 'Mind': 100}, \n\
                                'Effectiveness': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Soul': 100, 'Toxin': 100, 'Focus': 100, 'Life': 100, 'Divine': 100, 'Mind': 100}, \n\
                                'Attributes': {'Consumable': True, 'Styx-Death': True, 'Self': True, '?': True}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Tempt', \n\
                                'Past Tense': 'tempted Death for', \n\
                                'Choice Probability': 10, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Sharp': -100000000, 'Burn': -100000000, 'Freeze': -100000000, 'Soul': -100000000, 'Toxin': -100000000, 'Focus': -100000000, 'Life': -100000000, 'Divine': -100000000, 'Mind': -100000000}, \n\
                                'Effect Probabilities': {'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Soul': 100, 'Toxin': 100, 'Focus': 100, 'Life': 100, 'Divine': 100, 'Mind': 100}, \n\
                                'Effectiveness': {'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Soul': 100, 'Toxin': 100, 'Focus': 100, 'Life': 100, 'Divine': 100, 'Mind': 100}, \n\
                                'Attributes': {'Consumable': True, 'Styx-Brute': True, 'Self': True, '?': True}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Tempt', \n\
                                'Past Tense': 'tempted Death for', \n\
                                'Choice Probability': 10, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -100000000, 'Burn': -100000000, 'Freeze': -100000000, 'Soul': -100000000, 'Toxin': -100000000, 'Focus': -100000000, 'Life': -100000000, 'Divine': -100000000, 'Mind': -100000000}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Burn': 100, 'Freeze': 100, 'Soul': 100, 'Toxin': 100, 'Focus': 100, 'Life': 100, 'Divine': 100, 'Mind': 100}, \n\
                                'Effectiveness': {'Brute': 100, 'Burn': 100, 'Freeze': 100, 'Soul': 100, 'Toxin': 100, 'Focus': 100, 'Life': 100, 'Divine': 100, 'Mind': 100}, \n\
                                'Attributes': {'Consumable': True, 'Styx-Sharp': True, 'Self': True, '?': True}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Tempt', \n\
                                'Past Tense': 'tempted Death for', \n\
                                'Choice Probability': 5, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -100000000, 'Sharp': -100000000, 'Freeze': -100000000, 'Soul': -100000000, 'Toxin': -100000000, 'Focus': -100000000, 'Life': -100000000, 'Divine': -100000000, 'Mind': -100000000}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Freeze': 100, 'Soul': 100, 'Toxin': 100, 'Focus': 100, 'Life': 100, 'Divine': 100, 'Mind': 100}, \n\
                                'Effectiveness': {'Brute': 100, 'Sharp': 100,  'Freeze': 100, 'Soul': 100, 'Toxin': 100, 'Focus': 100, 'Life': 100, 'Divine': 100, 'Mind': 100}, \n\
                                'Attributes': {'Consumable': True, 'Styx-Burn': True, 'Self': True, '?': True}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Tempt', \n\
                                'Past Tense': 'tempted Death for', \n\
                                'Choice Probability': 5, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -100000000, 'Sharp': -100000000, 'Burn': -100000000, 'Soul': -100000000, 'Toxin': -100000000, 'Focus': -100000000, 'Life': -100000000, 'Divine': -100000000, 'Mind': -100000000}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100,  'Soul': 100, 'Toxin': 100, 'Focus': 100, 'Life': 100, 'Divine': 100, 'Mind': 100}, \n\
                                'Effectiveness': {'Brute': 100, 'Sharp': 100, 'Burn': 100,   'Soul': 100, 'Toxin': 100, 'Focus': 100, 'Life': 100, 'Divine': 100, 'Mind': 100}, \n\
                                'Attributes': {'Consumable': True, 'Styx-Freeze': True, 'Self': True, '?': True}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Tempt', \n\
                                'Past Tense': 'tempted Death for', \n\
                                'Choice Probability': 1, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -100000000, 'Sharp': -100000000, 'Burn': -100000000, 'Freeze': -100000000, 'Toxin': -100000000, 'Focus': -100000000, 'Life': -100000000, 'Divine': -100000000, 'Mind': -100000000}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Toxin': 100, 'Focus': 100, 'Life': 100, 'Divine': 100, 'Mind': 100}, \n\
                                'Effectiveness': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Toxin': 100, 'Focus': 100, 'Life': 100, 'Divine': 100, 'Mind': 100}, \n\
                                'Attributes': {'Consumable': True, 'Styx-Soul': True, 'Self': True, '?': True}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Tempt', \n\
                                'Past Tense': 'tempted Death for', \n\
                                'Choice Probability': 1, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -100000000, 'Sharp': -100000000, 'Burn': -100000000, 'Freeze': -100000000, 'Focus': -100000000, 'Soul': -100000000, 'Life': -100000000, 'Divine': -100000000, 'Mind': -100000000}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Focus': 100, 'Soul': 100, 'Life': 100, 'Divine': 100, 'Mind': 100}, \n\
                                'Effectiveness': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Focus': 100, 'Soul': 100, 'Life': 100, 'Divine': 100, 'Mind': 100}, \n\
                                'Attributes': {'Consumable': True, 'Styx-Toxin': True, 'Self': True, '?': True}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Tempt', \n\
                                'Past Tense': 'tempted Death for', \n\
                                'Choice Probability': 1, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -100000000, 'Sharp': -100000000, 'Burn': -100000000, 'Freeze': -100000000, 'Soul': -100000000, 'Toxin': -100000000, 'Focus': -100000000, 'Divine': -100000000, 'Mind': -100000000}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Soul': 100, 'Toxin': 100, 'Focus': 100, 'Divine': 100, 'Mind': 100}, \n\
                                'Effectiveness': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Soul': 100, 'Toxin': 100, 'Focus': 100, 'Divine': 100, 'Mind': 100}, \n\
                                'Attributes': {'Consumable': True, 'Styx-Life': True, 'Self': True, '?': True}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Tempt', \n\
                                'Past Tense': 'tempted Death for', \n\
                                'Choice Probability': 5, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -100000000, 'Sharp': -100000000, 'Burn': -100000000, 'Freeze': -100000000, 'Soul': -100000000, 'Toxin': -100000000, 'Focus': -100000000, 'Life': -100000000, 'Mind': -100000000}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Soul': 100, 'Toxin': 100, 'Focus': 100, 'Life': 100, 'Mind': 100}, \n\
                                'Effectiveness': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Soul': 100, 'Toxin': 100, 'Focus': 100, 'Life': 100, 'Mind': 100}, \n\
                                'Attributes': {'Consumable': True, 'Styx-Divine': True, 'Self': True, '?': True}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Tempt', \n\
                                'Past Tense': 'tempted Death for', \n\
                                'Choice Probability': .5, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -100000000, 'Sharp': -100000000, 'Burn': -100000000, 'Freeze': -100000000, 'Soul': -100000000, 'Toxin': -100000000, 'Focus': -100000000, 'Life': -100000000, 'Divine': -100000000}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Soul': 100, 'Toxin': 100, 'Focus': 100, 'Life': 100, 'Divine': 100}, \n\
                                'Effectiveness': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Soul': 100, 'Toxin': 100, 'Focus': 100, 'Life': 100, 'Divine': 100}, \n\
                                'Attributes': {'Consumable': True, 'Styx-Mind': True, 'Self': True, '?': True}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Tempt', \n\
                                'Past Tense': 'tempted Death for', \n\
                                'Choice Probability': 1, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -100000000, 'Sharp': -100000000, 'Burn': -100000000, 'Freeze': -100000000, 'Soul': -100000000, 'Toxin': -100000000, 'Life': -100000000, 'Divine': -100000000}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Soul': 100, 'Toxin': 100, 'Life': 100, 'Divine': 100}, \n\
                                'Effectiveness': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Soul': 100, 'Toxin': 100, 'Life': 100, 'Divine': 100}, \n\
                                'Attributes': {'Consumable': True, 'Styx-Focus': True, 'Self': True, '?': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Unique': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Herb-of-Kheiron', \n\
                    'Description': 'A dark green herb.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Consume', \n\
                                'Past Tense': 'healed', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -500, 'Sharp': -500}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100}, \n\
                                'Effectiveness': {'Brute': 80, 'Sharp': 80}, \n\
                                'Attributes': {'Consumable': True, 'Self': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Flower': 'Herb'}, \n\
                }, \n\
                { \n\
                    'Name': 'Herb-of-Kirke', \n\
                    'Description': 'A dark green herb.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Consume', \n\
                                'Past Tense': 'poisoned', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Divine': 500}, \n\
                                'Effect Probabilities': {'Divine': 100}, \n\
                                'Effectiveness': {'Divine': 50}, \n\
                                'Attributes': {'Consumable': True, 'Self': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Flower': 'Herb'}, \n\
                }, \n\
                { \n\
                    'Name': 'Herb-of-Asklepios', \n\
                    'Description': 'A dark green herb.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Consume', \n\
                                'Past Tense': 'healed', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -10000, 'Sharp': -10000}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100}, \n\
                                'Effectiveness': {'Brute': 80, 'Sharp': 80}, \n\
                                'Attributes': {'Consumable': True, 'Self': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Flower': 'Herb'}, \n\
                }, \n\
                { \n\
                    'Name': 'Hellebore', \n\
                    'Description': 'A deep black rose.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Consume', \n\
                                'Past Tense': 'healed', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Agility': -300}, \n\
                                'Effect Probabilities': {'Agility': 100}, \n\
                                'Effectiveness': {'Agility': 50}, \n\
                                'Attributes': {'Consumable': True, 'Self': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Flower': 'Black'}, \n\
                }, \n\
                { \n\
                    'Name': 'Zeus\\'s-Thunderbolt', \n\
                    'Description': 'A bolt of pure, white, energy. The electricity causes the hairs of your arms to stand on end.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Smite', \n\
                                'Past Tense': 'smote', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 5, \n\
                                'Damages': {'Divine': 10000, 'Burn': 100000}, \n\
                                'Effect Probabilities': {'Divine': 100, 'Burn': 100}, \n\
                                'Effectiveness': {'Divine': 100, 'Burn': 100}, \n\
                                'Attributes': {'Cooldown': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Aphrodite\\'s-Magic-Girdle', \n\
                    'Description': 'A cord worn about the waste. You feel great attraction towards it.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Pacify', \n\
                                'Past Tense': 'pacified', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 5, \n\
                                'Damages': {'Tame': 1000000}, \n\
                                'Effect Probabilities': {'Tame': 100}, \n\
                                'Effectiveness': {'Tame': 100}, \n\
                                'Attributes': {'Cooldown': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Athena\\'s-Bridle', \n\
                    'Description': 'A saddle fit for a Pegasus.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Soothe', \n\
                                'Past Tense': 'soothed', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 5, \n\
                                'Damages': {'Tame+': 100}, \n\
                                'Effect Probabilities': {'Tame+': 100}, \n\
                                'Effectiveness': {'Tame+': 100}, \n\
                                'Attributes': {'Cooldown': True, 'Tame+': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Adamantine-Plough', \n\
                    'Description': 'A large plough of slick, black adamant. Fit for a bull of great strength.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Yoke', \n\
                                'Past Tense': 'yoked', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': -1, \n\
                                'Damages': {'Tame2+': 100}, \n\
                                'Effect Probabilities': {'Tame2+': 100}, \n\
                                'Effectiveness': {'Tame2+': 100}, \n\
                                'Attributes': {'Cooldown': True, 'Tame2+': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Spear-of-Ares', \n\
                    'Description': 'A flaming shaft with a dastardly point on one end.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Eviscerate', \n\
                                'Past Tense': 'eviscerated', \n\
                                'Choice Probability': 10, \n\
                                'Hit Probability': 50, \n\
                                'Cooldown': 5, \n\
                                'Damages': {'Divine': 10000, 'Burn': 7000, 'Sharp': 8000}, \n\
                                'Effect Probabilities': {'Divine': 100, 'Burn': 100, 'Sharp': 100}, \n\
                                'Effectiveness': {'Divine': 95, 'Burn': 80, 'Sharp': 80}, \n\
                                'Attributes': {'Cooldown': True}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Impale', \n\
                                'Past Tense': 'impaled', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Divine': 500, 'Burn': 1000, 'Sharp': 1000}, \n\
                                'Effect Probabilities': {'Divine': 100, 'Burn': 100, 'Sharp': 100}, \n\
                                'Effectiveness': {'Divine': 10, 'Burn': 10, 'Sharp': 10}, \n\
                                'Attributes': {'AOE': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Artemis\\'s-Bow', \n\
                    'Description': 'An elegant, silver bow crafted of moonlight.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'shoot', \n\
                                'Past Tense': 'shot', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 99, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Divine': 1000, 'Sharp': 8000}, \n\
                                'Effect Probabilities': {'Divine': 100, 'Sharp': 100}, \n\
                                'Effectiveness': {'Divine': 95, 'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Volley-Arrows-At', \n\
                                'Past Tense': 'fired dozens of arrows at', \n\
                                'Choice Probability': 1, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 10, \n\
                                'Damages': {'Divine': 10000, 'Sharp': 80000}, \n\
                                'Effect Probabilities': {'Divine': 100, 'Sharp': 100}, \n\
                                'Effectiveness': {'Divine': 95, 'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Apollo\\'s-Bow', \n\
                    'Description': 'An elegant, golden bow crafted of sunshine.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'shoot', \n\
                                'Past Tense': 'shot', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 99, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Divine': 2000, 'Sharp': 8000, 'Burn': 8000}, \n\
                                'Effect Probabilities': {'Divine': 100, 'Sharp': 100, 'Burn': 100}, \n\
                                'Effectiveness': {'Divine': 95, 'Sharp': 80, 'Burn': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Volley-Arrows-At', \n\
                                'Past Tense': 'fired dozens of arrows at', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 10, \n\
                                'Damages': {'Divine': 20000, 'Sharp': 80000, 'Burn': 80000}, \n\
                                'Effect Probabilities': {'Divine': 100, 'Sharp': 100, 'Burn': 100}, \n\
                                'Effectiveness': {'Divine': 95, 'Sharp': 80, 'Burn': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Hephaestus\\'s-Labrys', \n\
                    'Description': 'A huge double-headed axe of red and black.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Cleave', \n\
                                'Past Tense': 'cleaved', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 60, \n\
                                'Cooldown': -1, \n\
                                'Damages': {'Divine': 2500, 'Sharp': 8000}, \n\
                                'Effect Probabilities': {'Divine': 100, 'Sharp': 100}, \n\
                                'Effectiveness': {'Divine': 100, 'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Myrrh-Egg', \n\
                    'Description': 'A large egg made of Myrrh. It feels hot.', \n\
                    'Attacks': \n\
                        [ \n\
                        ], \n\
                    'Attributes': {'Egg': True, 'Body': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Shirt-of-Nessus', \n\
                    'Description': 'Said to cause the wearer to be faithful to their spouse.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Wear', \n\
                                'Past Tense': 'equipped', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -10000, 'Sharp': -10000, 'Burn': -10000, 'Freeze': -10000, 'Toxin': 1}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Toxin': 100}, \n\
                                'Effectiveness': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Toxin': 100}, \n\
                                'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Flower': 'Shirt-of-Nessus'}, \n\
                }, \n\
                { \n\
                    'Name': 'Golden-Fleece', \n\
                    'Description': 'A silky fleece with threads of glistening gold. Its presence comforts you.', \n\
                    'Attacks': \n\
                        [ \n\
                        ], \n\
                    'Attributes': {'Fleece': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Poseidon\\'s-Trident', \n\
                    'Description': 'A metal, three-pronged fork the color of the sea.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Impale', \n\
                                'Past Tense': 'impaled', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Divine': 4000, 'Sharp': 10000}, \n\
                                'Effect Probabilities': {'Divine': 100, 'Sharp': 100}, \n\
                                'Effectiveness': {'Divine': 90, 'Sharp': 60}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Chill', \n\
                                'Past Tense': 'chilled', \n\
                                'Choice Probability': 10, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': 1, \n\
                                'Damages': {'Divine': 6000, 'Freeze': 10000}, \n\
                                'Effect Probabilities': {'Divine': 100, 'Freeze': 100}, \n\
                                'Effectiveness': {'Divine': 90, 'Freeze': 60}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Hades\\'s-Bident', \n\
                    'Description': 'A metal, two-pronged fork the color of suffering.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Impale', \n\
                                'Past Tense': 'impaled', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Divine': 10000, 'Sharp': 8000}, \n\
                                'Effect Probabilities': {'Divine': 100, 'Sharp': 100}, \n\
                                'Effectiveness': {'Divine': 90, 'Sharp': 100}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Incinerate', \n\
                                'Past Tense': 'incinerated', \n\
                                'Choice Probability': 10, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': 1, \n\
                                'Damages': {'Divine': 7000, 'Burn': 10000}, \n\
                                'Effect Probabilities': {'Divine': 100, 'Burn': 100}, \n\
                                'Effectiveness': {'Divine': 90, 'Burn': 60}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Hammer-of-Hephaestus', \n\
                    'Description': 'A red and black hammer of elegant craft. \\'Renewed shall be blade that was broken.\\'', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Forge', \n\
                                'Past Tense': 'forged for', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 7, \n\
                                'Ammo': 3, \n\
                                'Damages': {}, \n\
                                'Effect Probabilities': {}, \n\
                                'Effectiveness': {}, \n\
                                'Attributes': {'Cooldown': True, 'Spawn-Weapon': True, 'Self': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Dragon\\'s-Teeth', \n\
                    'Description': 'Large and pointy. There are legends of buried dragon\\'s teeth growing into great warriors.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Plant', \n\
                                'Past Tense': 'planted for', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {}, \n\
                                'Effect Probabilities': {}, \n\
                                'Effectiveness': {}, \n\
                                'Attributes': {'Spawn-Spartae': True, 'Self': True, 'Consumable': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Body': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Pandora\\'s-Box', \n\
                    'Description': 'A black box inscribed with elegant writing in some indiscernible script. You want to open it.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Open', \n\
                                'Past Tense': 'opened before', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 10, \n\
                                'Ammo': 3, \n\
                                'Damages': {}, \n\
                                'Effect Probabilities': {}, \n\
                                'Effectiveness': {}, \n\
                                'Attributes': {'Cooldown': True, 'Spawn-Anything': True, 'Self': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Daedalus\\'s-Hand-Canon', \n\
                    'Description': 'It\\'s your lucky day.', \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Blast-At', \n\
                                'Past Tense': 'blasted at', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 60, \n\
                                'Cooldown': 5, \n\
                                'Ammo': 3, \n\
                                'Damages': {'Brute': 10000}, \n\
                                'Effect Probabilities': {'Brute': 100}, \n\
                                'Effectiveness': {'Brute': 100}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Doru', \n\
                    'Description': 'A long, sharp spear.', \n\
                    'Attacks': \n\
                        [ \n\
                             'Stab', \n\
                             'Slash', \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Achilles\\'s-Spear', \n\
                    'Description': 'A sturdy shaft of purest white in trim of gold. You have attained unimaginable power.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Impale', \n\
                                'Past Tense': 'impaled', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': -10, \n\
                                'Damages': {'Sharp': 100000}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 1}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Annihilate', \n\
                                'Past Tense': 'annihilated', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 3, \n\
                                'Damages': {'Mind': 1}, \n\
                                'Effect Probabilities': {'Mind': 100}, \n\
                                'Effectiveness': {'Mind': 100}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Giant-Club', \n\
                    'Description': 'Big and gnarled.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Smash', \n\
                                'Past Tense': 'smashed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': 1, \n\
                                'Damages': {'Brute': 1500}, \n\
                                'Effect Probabilities': {'Brute': 100}, \n\
                                'Effectiveness': {'Brute': 50}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                             { \n\
                                'Name': 'Crush', \n\
                                'Past Tense': 'crushed', \n\
                                'Choice Probability': 10, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': 3, \n\
                                'Damages': {'Brute': 2500}, \n\
                                'Effect Probabilities': {'Brute': 100}, \n\
                                'Effectiveness': {'Brute': 50}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Giant-Sword', \n\
                    'Description': 'Elegantly crafted and very large.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Slash', \n\
                                'Past Tense': 'slashed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': 1, \n\
                                'Damages': {'Sharp': 1500, 'Giant+': 1000}, \n\
                                'Effect Probabilities': {'Sharp': 100, 'Giant+': 100}, \n\
                                'Effectiveness': {'Sharp': 80, 'Giant+': 100}, \n\
                                'Attributes': {'Giant+': True, 'AOE': True}, \n\
                            }, \n\
                             { \n\
                                'Name': 'Cleave', \n\
                                'Past Tense': 'cleft', \n\
                                'Choice Probability': 10, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': 3, \n\
                                'Damages': {'Sharp': 2500, 'Giant+': 1000}, \n\
                                'Effect Probabilities': {'Sharp': 100, 'Giant+': 100}, \n\
                                'Effectiveness': {'Sharp': 80, 'Giant+': 100}, \n\
                                'Attributes': {'Giant+': True, 'AOE': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                  'Name': 'Helm-of-Darkness', \n\
                  'Description': 'The helm is black. Misted shadows swirl about it, periodically hiding it from view.', \n\
                  'Attacks': \n\
                      [ \n\
                           { \n\
                              'Name': 'Wear', \n\
                              'Past Tense': 'equipped', \n\
                              'Choice Probability': 0, \n\
                              'Hit Probability': 100, \n\
                              'Cooldown': 0, \n\
                              'Damages': {'Agility': 20}, \n\
                              'Effect Probabilities': {'Agility': 100}, \n\
                              'Effectiveness': {'Agility': 100}, \n\
                              'Attributes': {'Camo+': True, 'Consumable': True, 'Self': True, 'Worn': True}, \n\
                          }, \n\
                      ], \n\
                  'Attributes': {'Body': True}, \n\
                }, \n\
                { \n\
                  'Name': 'Thread-of-Ariadne', \n\
                  'Description': 'A silken ball of thread.', \n\
                  'Attacks': \n\
                      [ \n\
                           { \n\
                              'Name': 'Unspool', \n\
                              'Past Tense': 'enlivened', \n\
                              'Choice Probability': 0, \n\
                              'Hit Probability': 100, \n\
                              'Cooldown': 0, \n\
                              'Damages': {}, \n\
                              'Effect Probabilities': {}, \n\
                              'Effectiveness': {}, \n\
                              'Attributes': {'Thread': True, 'Consumable': True, 'Self': True}, \n\
                          }, \n\
                      ], \n\
                  'Attributes': {}, \n\
                }, \n\
                { \n\
                  'Name': 'Staff-of-Travel', \n\
                  'Description': 'A sturdy wooden staff with magical properties.', \n\
                  'Attacks': \n\
                      [ \n\
                           { \n\
                              'Name': 'Invoke', \n\
                              'Past Tense': 'teleported', \n\
                              'Choice Probability': 0, \n\
                              'Hit Probability': 100, \n\
                              'Cooldown': 0, \n\
                              'Ammo': 3, \n\
                              'Damages': {}, \n\
                              'Effect Probabilities': {}, \n\
                              'Effectiveness': {}, \n\
                              'Attributes': {'Travel': True, 'Self': True}, \n\
                          }, \n\
                      ], \n\
                  'Attributes': {}, \n\
                }, \n\
                { \n\
                  'Name': 'Kibisis', \n\
                  'Description': 'A silken sack for storing heads.', \n\
                  'Attacks': \n\
                      [ \n\
                      ], \n\
                  'Attributes': {'Sack': True}, \n\
                }, \n\
                { \n\
                  'Name': 'Prometheus\\'s-Chains', \n\
                  'Description': 'Indestructible shackles of adamant.', \n\
                  'Attacks': \n\
                      [ \n\
                           { \n\
                              'Name': 'Throw', \n\
                              'Past Tense': 'chained', \n\
                              'Choice Probability': 0, \n\
                              'Hit Probability': 20, \n\
                              'Cooldown': 0, \n\
                              'Ammo': 1, \n\
                              'Damages': {}, \n\
                              'Effect Probabilities': {}, \n\
                              'Effectiveness': {}, \n\
                              'Attributes': {'Chains': True}, \n\
                          }, \n\
                      ], \n\
                  'Attributes': {}, \n\
                }, \n\
                { \n\
                  'Name': 'Pheme\\'s-Trumpet', \n\
                  'Description': 'A golden trumpet of excellent craft.', \n\
                  'Attacks': \n\
                      [ \n\
                           { \n\
                              'Name': 'Blow', \n\
                              'Past Tense': 'played for', \n\
                              'Choice Probability': 0, \n\
                              'Hit Probability': 100, \n\
                              'Cooldown': 0, \n\
                              'Damages': {}, \n\
                              'Effect Probabilities': {}, \n\
                              'Effectiveness': {}, \n\
                              'Attributes': {'Trumpet': True, 'Self': True}, \n\
                          }, \n\
                      ], \n\
                  'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Akontia', \n\
                    'Description': 'A javelin.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Throw', \n\
                                'Past Tense': 'hit', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Sharp': 400}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 90}, \n\
                                'Attributes': {'Thrown': True}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Stab', \n\
                                'Past Tense': 'stabbed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 90, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Sharp': 300}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Pan\\'s-Flute', \n\
                    'Description': 'A beautiful melody could be played there-on by even the simplest of creatures.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Play-Melody', \n\
                                'Past Tense': 'played a beautiful melody for', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 2, \n\
                                'Damages': {'Tame': 10000}, \n\
                                'Effect Probabilities': {'Tame': 100}, \n\
                                'Effectiveness': {'Tame': 1}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Apollo\\'s-Lyre', \n\
                    'Description': 'Capable of playing a divine melody.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Play-Melody', \n\
                                'Past Tense': 'played a divine melody for', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 2, \n\
                                'Damages': {'Tame': 10000}, \n\
                                'Effect Probabilities': {'Tame': 100}, \n\
                                'Effectiveness': {'Tame': 50}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Body': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Adamantine-Blade', \n\
                    'Description': 'A divine power pulses through the slick, black, blade.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Desecrate', \n\
                                'Past Tense': 'desecrated', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 95, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Divine': 5000, 'Sharp': 1000}, \n\
                                'Effect Probabilities': {'Divine': 100, 'Sharp': 60}, \n\
                                'Effectiveness': {'Divine': 10, 'Sharp': 60}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Cronus\\'s-Scythe', \n\
                    'Description': 'Never send to know for whom the bell tolls; it tolls for thee.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Slice', \n\
                                'Past Tense': 'sliced', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 90, \n\
                                'Cooldown': -1, \n\
                                'Damages': {'Sharp': 2000}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Body': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Daedalus\\'s-Wings', \n\
                    'Description': 'A ragtag set of wings glued together with feathers and twine. Grants the wearer great speed.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Equip', \n\
                                'Past Tense': 'equipped', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Agility': -800}, \n\
                                'Effect Probabilities': {'Agility': 100}, \n\
                                'Effectiveness': {'Agility': 100}, \n\
                                'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Bag-of-Wind', \n\
                    'Description': 'The breezy wooshing of the wind contained within a silk bag of pure white.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Open', \n\
                                'Past Tense': 'opened before', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Agility': -10000}, \n\
                                'Effect Probabilities': {'Agility': 100}, \n\
                                'Effectiveness': {'Agility': 100}, \n\
                                'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Talaria', \n\
                    'Description': 'Winged sandals of imperishable gold.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Equip', \n\
                                'Past Tense': 'equipped', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Agility': -1000}, \n\
                                'Effect Probabilities': {'Agility': 100}, \n\
                                'Effectiveness': {'Agility': 100}, \n\
                                'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Body': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Brazen-Shield', \n\
                    'Description': 'Bronze and well-polished to the point of being mirror-like.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Equip', \n\
                                'Past Tense': 'equipped', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Soul': -1000, 'Agility': 90}, \n\
                                'Effect Probabilities': {'Soul': 100, 'Agility': 100}, \n\
                                'Effectiveness': {'Soul': 100, 'Agility': 100}, \n\
                                'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Bestiary', \n\
                    'Description': 'A compendium of creatures and how to tame them.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Learn-to-Tame', \n\
                                'Past Tense': 'calmed', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 1, \n\
                                'Ammo': 5, \n\
                                'Damages': {'Tame': 5000}, \n\
                                'Effect Probabilities': {'Tame': 100}, \n\
                                'Effectiveness': {'Tame': 100}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Cook-Book', \n\
                    'Description': 'A compendium of foods and how to make them.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Learn-to-Cook', \n\
                                'Past Tense': 'cooked a fine meal for', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 2, \n\
                                'Ammo': 5, \n\
                                'Damages': {}, \n\
                                'Effect Probabilities': {}, \n\
                                'Effectiveness': {}, \n\
                                'Attributes': {'Cooldown': True, 'Self': True, 'Spawn-Finely-Cooked-Meal': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Atlas', \n\
                    'Description': 'A compendium of locations and how to get there.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Learn-Locations', \n\
                                'Past Tense': 'guided', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 2, \n\
                                'Ammo': 5, \n\
                                'Damages': {}, \n\
                                'Effect Probabilities': {}, \n\
                                'Effectiveness': {}, \n\
                                'Attributes': {'Atlas': True, 'Cooldown': True, 'Self': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Herbal-Anthology', \n\
                    'Description': 'A compendium of plants and how to use them.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Read', \n\
                                'Past Tense': 'learned how to identify plants for', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 1, \n\
                                'Ammo': 5, \n\
                                'Damages': {}, \n\
                                'Effect Probabilities': {}, \n\
                                'Effectiveness': {}, \n\
                                'Attributes': {'Self': True, 'Herbal': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Bell-Cuirass', \n\
                    'Description': 'Heavy bronze breastplate.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Equip', \n\
                                'Past Tense': 'equipped', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -2800, 'Sharp': -2800, 'Burn': -500, 'Agility': 100}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Agility': 100}, \n\
                                'Effectiveness': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Agility': 100}, \n\
                                'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Linothorax', \n\
                    'Description': 'Heavy linen breastplate.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Equip', \n\
                                'Past Tense': 'equipped', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -1600, 'Sharp': -1200, 'Burn': -1000, 'Agility': 20}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Agility': 100}, \n\
                                'Effectiveness': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Agility': 100}, \n\
                                'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Armour-of-Achilles', \n\
                    'Description': 'A set of divine armor of pure gilded white. You have become an unstoppable force.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Equip', \n\
                                'Past Tense': 'equipped', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -1000000, 'Sharp': -1000000, 'Burn': -1000000, 'Freeze': -1000000, 'Agility': 200}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Agility': 100}, \n\
                                'Effectiveness': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Agility': 100}, \n\
                                'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Chitoniskos', \n\
                    'Description': 'Light linen tunic.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Equip', \n\
                                'Past Tense': 'equipped', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -1000, 'Sharp': -900, 'Burn': -900, 'Agility': 10}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Agility': 100}, \n\
                                'Effectiveness': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Agility': 100}, \n\
                                'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Corinthian-Helmet', \n\
                    'Description': 'Very heavy bronze helmet.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Equip', \n\
                                'Past Tense': 'equipped', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -1300, 'Sharp': -1300, 'Agility': 70}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Agility': 100}, \n\
                                'Effectiveness': {'Brute': 100, 'Sharp': 100, 'Agility': 100}, \n\
                                'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Phrygian-Helmet', \n\
                    'Description': 'Heavy bronze helmet.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Equip', \n\
                                'Past Tense': 'equipped', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -1250, 'Sharp': -1250, 'Agility': 50}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Agility': 100}, \n\
                                'Effectiveness': {'Brute': 100, 'Sharp': 100, 'Agility': 100}, \n\
                                'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Chalcidian-Helmet', \n\
                    'Description': 'Bronze helmet.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Equip', \n\
                                'Past Tense': 'equipped', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -1200, 'Sharp': -1200, 'Agility': 20}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Agility': 100}, \n\
                                'Effectiveness': {'Brute': 100, 'Sharp': 100, 'Agility': 100}, \n\
                                'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Boeotian-Helmet', \n\
                    'Description': 'Light bronze helmet.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Equip', \n\
                                'Past Tense': 'equipped', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -950, 'Sharp': -950, 'Agility': 10}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Agility': 100}, \n\
                                'Effectiveness': {'Brute': 100, 'Sharp': 100, 'Agility': 100}, \n\
                                'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Muscle-Cuirass', \n\
                    'Description': 'Light bronze breastplate.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Equip', \n\
                                'Past Tense': 'equipped', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -2600, 'Sharp': -2600, 'Burn': -400, 'Agility': 50}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Agility': 100}, \n\
                                'Effectiveness': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Agility': 100}, \n\
                                'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Emerald-Tablet', \n\
                    'Description': 'Light shines through the emerald slab, casting mystic rays of green about the room. The tablet is covered in cryptic writing.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Read', \n\
                                'Past Tense': 'learned alchemy for', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 3, \n\
                                'Damages': {}, \n\
                                'Effect Probabilities': {}, \n\
                                'Effectiveness': {}, \n\
                                'Attributes': {'Cooldown': True, 'Self': True, 'Spawn-Treasure': True, 'Cryptic': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Compendium', \n\
                    'Description': 'A heavy black, leather-bound book with a first symbol pressed into its front.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Learn', \n\
                                'Past Tense': 'learned skill for', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 3, \n\
                                'Damages': {}, \n\
                                'Effect Probabilities': {}, \n\
                                'Effectiveness': {}, \n\
                                'Attributes': {'Cooldown': True, 'Self': True, 'Spawn-Attack': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Wooden-Cow', \n\
                    'Description': 'A hollow, wooden cow. You could fit inside this.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Display', \n\
                                'Past Tense': 'presented', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {}, \n\
                                'Effect Probabilities': {}, \n\
                                'Effectiveness': {}, \n\
                                'Attributes': {'Self': True, 'Consumable': True, 'Cow': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Dagger-Bag', \n\
                    'Description': 'A rolled leather strap lined with three daggers.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Unwrap', \n\
                                'Past Tense': 'armed', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Ammo': 5, \n\
                                'Damages': {}, \n\
                                'Effect Probabilities': {}, \n\
                                'Effectiveness': {}, \n\
                                'Attributes': {'Self': True, 'Spawn-Dagger': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Food-Platter', \n\
                    'Description': 'A silver platter of mead and meal.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Dish', \n\
                                'Past Tense': 'dished', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {}, \n\
                                'Effect Probabilities': {}, \n\
                                'Effectiveness': {}, \n\
                                'Attributes': {'Self': True, 'Consumable': True, 'Spawn-Mead2': True, 'Spawn-Meal': True,}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Peacock\\'s-Feather', \n\
                    'Description': 'Brilliant and outlandish in its majesty. Said to grant the all-seeing wisdom of the gods.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Immerse', \n\
                                'Past Tense': 'enlightened', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {}, \n\
                                'Effect Probabilities': {}, \n\
                                'Effectiveness': {}, \n\
                                'Attributes': {'Self': True, 'Consumable': True, 'Cryptic+': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Orpheus\\'s-Lyre', \n\
                    'Description': 'An intricate lyre of finest wood.', \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Immerse', \n\
                                'Past Tense': 'immersed', \n\
                                'Choice Probability': 0, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {}, \n\
                                'Effect Probabilities': {}, \n\
                                'Effectiveness': {}, \n\
                                'Attributes': {'Self': True, 'Orpheus': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
            ], \n\
        'attacks': \n\
            [ \n\
                { \n\
                    'Name': 'Strangle', \n\
                    'Past Tense': 'strangled', \n\
                    'Choice Probability': 50, \n\
                    'Hit Probability': 50, \n\
                    'Cooldown': 3, \n\
                    'Damages': {'Brute': 200}, \n\
                    'Effect Probabilities': {'Brute': 100}, \n\
                    'Effectiveness': {'Brute': 50}, \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Bite', \n\
                    'Past Tense': 'bit', \n\
                    'Choice Probability': 100, \n\
                    'Hit Probability': 60, \n\
                    'Cooldown': 0, \n\
                    'Damages': {'Sharp': 100}, \n\
                    'Effect Probabilities': {'Sharp': 100}, \n\
                    'Effectiveness': {'Sharp': 80}, \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Claw', \n\
                    'Past Tense': 'clawed', \n\
                    'Choice Probability': 100, \n\
                    'Hit Probability': 80, \n\
                    'Cooldown': 0, \n\
                    'Damages': {'Sharp': 100}, \n\
                    'Effect Probabilities': {'Sharp': 100}, \n\
                    'Effectiveness': {'Sharp': 80}, \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Rend', \n\
                    'Past Tense': 'rent', \n\
                    'Choice Probability': 50, \n\
                    'Hit Probability': 80, \n\
                    'Cooldown': 0, \n\
                    'Damages': {'Sharp': 500}, \n\
                    'Effect Probabilities': {'Sharp': 100}, \n\
                    'Effectiveness': {'Sharp': 80}, \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Kick', \n\
                    'Past Tense': 'kicked', \n\
                    'Choice Probability': 150, \n\
                    'Hit Probability': 80, \n\
                    'Cooldown': 0, \n\
                    'Damages': {'Brute': 300}, \n\
                    'Effect Probabilities': {'Brute': 100}, \n\
                    'Effectiveness': {'Brute': 80}, \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Charge', \n\
                    'Past Tense': 'charged', \n\
                    'Choice Probability': 100, \n\
                    'Hit Probability': 60, \n\
                    'Cooldown': 2, \n\
                    'Damages': {'Brute': 300, 'Sharp': 100}, \n\
                    'Effect Probabilities': {'Brute': 100, 'Sharp': 100}, \n\
                    'Effectiveness': {'Brute': 80, 'Sharp': 80}, \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Smash', \n\
                    'Past Tense': 'smashed', \n\
                    'Choice Probability': 100, \n\
                    'Hit Probability': 60, \n\
                    'Cooldown': 1, \n\
                    'Damages': {'Brute': 500}, \n\
                    'Effect Probabilities': {'Brute': 100}, \n\
                    'Effectiveness': {'Brute': 80}, \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Punch', \n\
                    'Past Tense': 'punched', \n\
                    'Choice Probability': 100, \n\
                    'Hit Probability': 95, \n\
                    'Cooldown': 0, \n\
                    'Damages': {'Brute': 300}, \n\
                    'Effect Probabilities': {'Brute': 100}, \n\
                    'Effectiveness': {'Brute': 40}, \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Tame', \n\
                    'Past Tense': 'calmed', \n\
                    'Choice Probability': 100, \n\
                    'Hit Probability': 100, \n\
                    'Cooldown': 0, \n\
                    'Damages': {'Tame': 100}, \n\
                    'Effect Probabilities': {'Tame': 100}, \n\
                    'Effectiveness': {'Tame': 40}, \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Peck', \n\
                    'Past Tense': 'pecked', \n\
                    'Choice Probability': 100, \n\
                    'Hit Probability': 60, \n\
                    'Cooldown': 0, \n\
                    'Damages': {'Sharp': 100}, \n\
                    'Effect Probabilities': {'Sharp': 100}, \n\
                    'Effectiveness': {'Sharp': 50}, \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Stab', \n\
                    'Past Tense': 'stabbed', \n\
                    'Choice Probability': 100, \n\
                    'Hit Probability': 80, \n\
                    'Cooldown': 0, \n\
                    'Ammo': 0, \n\
                    'Damages': {'Sharp': 300}, \n\
                    'Effect Probabilities': {'Sharp': 100}, \n\
                    'Effectiveness': {'Sharp': 100}, \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Slash', \n\
                    'Past Tense': 'slashed', \n\
                    'Choice Probability': 50, \n\
                    'Hit Probability': 80, \n\
                    'Cooldown': 0, \n\
                    'Ammo': 0, \n\
                    'Damages': {'Sharp': 200}, \n\
                    'Effect Probabilities': {'Sharp': 100}, \n\
                    'Effectiveness': {'Sharp': 100}, \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Burn', \n\
                    'Past Tense': 'incinerated', \n\
                    'Choice Probability': 20, \n\
                    'Hit Probability': 100, \n\
                    'Cooldown': 5, \n\
                    'Ammo': 0, \n\
                    'Damages': {'Burn': 2000}, \n\
                    'Effect Probabilities': {'Burn': 100}, \n\
                    'Effectiveness': {'Burn': 100}, \n\
                    'Attributes': {}, \n\
                }, \n\
            ], \n\
        'npcs': \n\
            [ \n\
                { \n\
                    'Name': 'Highway-Man', \n\
                    'Description': 'A bandit.', \n\
                    'Health': {'Brute': 1000, 'Sharp': 900, 'Burn': 500, 'Freeze': 600, 'Tame': 5000, 'Agility': 200}, \n\
                    'Aggressiveness': 99, \n\
                    'Weapons': \n\
                        [ \n\
                            'Dagger', \n\
                            'Kopis', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Strangle', \n\
                            'Punch', \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Traveler', \n\
                    'Description': 'A traveler.', \n\
                    'Health': {'Brute': 1000, 'Sharp': 900, 'Burn': 500, 'Freeze': 600, 'Tame': 5000, 'Agility': 200}, \n\
                    'Aggressiveness': 50, \n\
                    'Weapons': \n\
                        [ \n\
                            'Dagger', \n\
                            'Kopis', \n\
                            'Treasure', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Strangle', \n\
                            'Punch', \n\
                        ], \n\
                    'Attributes': {'Team': ['You']}, \n\
                }, \n\
                { \n\
                    'Name': 'Mercenary', \n\
                    'Description': 'A well armed mercenary.', \n\
                    'Health': {'Brute': 1500, 'Sharp': 1200, 'Burn': 900, 'Freeze': 1000, 'Tame': 6000, 'Agility': 220}, \n\
                    'Aggressiveness': 50, \n\
                    'Weapons': \n\
                        [ \n\
                            'Dagger', \n\
                            'Xiphos', \n\
                            'Toxa', \n\
                            'Treasure', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Strangle', \n\
                            'Punch', \n\
                        ], \n\
                    'Attributes': {'Team': ['You']}, \n\
                }, \n\
                { \n\
                    'Name': 'King-Hrothgar', \n\
                    'Description': '\\'to Hrothgar success in warcraft given, honour in war, so that his retainers eagerly served him.\\'', \n\
                    'Health': {'Brute': 10000, 'Sharp': 9000, 'Burn': 9000, 'Freeze': 10000, 'Tame': 35000, 'Agility': 200}, \n\
                    'Aggressiveness': 0, \n\
                    'Weapons': \n\
                        [ \n\
                            'Jeweled-Dagger', \n\
                            'Hrothgar\\'s-Gift', \n\
                            'Treasure', \n\
                            'Treasure', \n\
                            'Treasure', \n\
                             { \n\
                                'Name': 'Golden-Crown', \n\
                                'Description': 'An item of great value.', \n\
                                'Attacks': \n\
                                    [ \n\
                                    ], \n\
                                'Attributes': {'Treasure': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Strangle', \n\
                                'Past Tense': 'strangled', \n\
                                'Choice Probability': .01, \n\
                                'Hit Probability': 50, \n\
                                'Cooldown': 3, \n\
                                'Damages': {'Brute': 600}, \n\
                                'Effect Probabilities': {'Brute': 100}, \n\
                                'Effectiveness': {'Brute': 50}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Punch', \n\
                                'Past Tense': 'punched', \n\
                                'Choice Probability': .01, \n\
                                'Hit Probability': 95, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': 600}, \n\
                                'Effect Probabilities': {'Brute': 100}, \n\
                                'Effectiveness': {'Brute': 40}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Unique': True, 'Hrothgar': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Story-Teller', \n\
                    'Description': None, \n\
                    'Health': {'Brute': 1000, 'Sharp': 900, 'Burn': 500, 'Freeze': 600, 'Tame': 5000, 'Agility': 10}, \n\
                    'Aggressiveness': 0, \n\
                    'Weapons': \n\
                        [ \n\
                            'Dagger', \n\
                            'Treasure', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Strangle', \n\
                            'Punch', \n\
                        ], \n\
                    'Attributes': { \n\
                                    'Story-Teller': True, \n\
                                    'Descriptions': [ \n\
                                                     '\\'A worthy man, Who, from the moment that he first began To ride about the world, loved chivalry, Truth, honour, freedom and all courtesy.\\'', \n\
                                                     '\\'A lover and a lusty bachelor, With locks well curled, as if they\\'d laid in press. Some twenty years of age he was, I guess. In stature he was of an average length, Wondrously active, aye, and great of strength.\\'', \n\
                                                     '\\'He was clad in coat and hood of green. A sheaf of peacock arrows bright and keen ... And in his hand he bore a mighty bow.\\'', \n\
                                                     '\\'A nun, a prioress, Who, in her smiling, modest was and coy; Her greatest oath was but \\\"By Saint Eloy!\\\"\\'', \n\
                                                     '\\'A manly man, to be an abbot able. Full many a blooded horse had he in stable: And when he rode men might his bridle hear A-jingling in the whistling wind as clear.\\'', \n\
                                                     '\\'Wanton and a merry, A limiter, a very festive man. He was an easy man to give penance When knowing he should gain a good pittance; \\'', \n\
                                                     '\\'A merchant with forked beard, and girt In motley gown, and high on horse he sat ... At money-changing he could make a crown.\\'', \n\
                                                     '\\'A clerk from Oxford was with us also, Who\\'d turned to getting knowledge, long ago.\\'', \n\
                                                     '\\'A sergeant of the law, wary and wise ... He took large fees and many robes could own. So great a purchaser was never known. All was fee simple to him, in effect, Wherefore his claims could never be suspect.  \\'', \n\
                                                     '\\'White was his beard as is the white daisy. Of sanguine temperament by every sign, He loved right well his morning sop in wine. Delightful living was the goal he\\'d won, For he was Epicurus\\' very son\\'', \n\
                                                     '\\'He could roast and seethe and broil and fry, And make a good thick soup, and bake a pie.\\'', \n\
                                                     '\\'The summer\\'s heat had burned his visage brown; And certainly he was a good fellow ... Wise in all things undertaken, By many a tempest had his beard been shaken. \\'', \n\
                                                     '\\'A doctor of physic; In all this world was none like him to pick For talk of medicine and surgery; For he was grounded in astronomy. He often kept a patient from the pall By horoscopes and magic natural.\\'', \n\
                                                     '\\'Three times she\\'d journeyed to Jerusalem; And many a foreign stream she\\'d had to stem; At Rome she\\'d been, and she\\'d been in Boulogne, In Spain at Santiago, and at Cologne.\\'', \n\
                                                     '\\'A good man of religion ... rich he was in holy thought and work. Who Christ\\'s own gospel truly sought to preach; Devoutly his parishioners would he teach.\\'', \n\
                                                     '\\'He loved God most, and that with his whole heart At all times, though he played or plied his art, And next, his neighbour, even as himself. He\\'d thresh and dig, with never thought of pelf\\'', \n\
                                                     '\\'Hardy and big of brawn and big of bone; He could steal corn and full thrice charge his fees; And yet he had a thumb of gold, begad.\\'', \n\
                                                     '\\'A manciple from an inn of court, To whom all buyers might quite well resort To learn the art of buying food and drink; For whether he paid cash or not, I think That he so knew the markets, when to buy, He never found himself left high and dry.\\'', \n\
                                                     '\\'A slender, choleric man ... Long were his legs, and they were very lean, And like a staff, with no calf to be seen.\\'', \n\
                                                     '\\'A summoner ... Who had a fiery-red, cherubic face ... He had a face that little children feared ... And drinking of strong wine as red as blood. Then would he talk and shout as madman would ... he would utter no word save Latin.\\'', \n\
                                                     '\\'A gentle pardoner ... This pardoner had hair as yellow as wax, But lank it hung as does a strike of flax ... with flattery and suchlike japes, He made the parson and the rest his apes.\\'', \n\
                                                    ], \n\
                                    'Names': ['The-Knight', 'The-Squire', 'The-Yeoman', 'The-Prioress', 'The-Monk', 'The-Friar', 'The-Merchant', 'The-Clerk', 'The-Lawyer', 'The-Franklin', 'The-Cook', 'The-Sailor', 'The-Physician', 'The-Wife-of-Bath', 'The-Parson', 'The-Plowman', 'The-Miller', 'The-Manciple', 'The-Reeve', 'The-Summoner', 'The-Pardoner'], \n\
                                   'Team': ['Story-Teller', 'You']}, \n\
                }, \n\
                { \n\
                    'Name': 'Cynocephali', \n\
                    'Description': 'A dog-headed man.', \n\
                    'Health': {'Brute': 1000, 'Sharp': 900, 'Burn': 500, 'Freeze': 600, 'Tame': 4500, 'Agility': 300}, \n\
                    'Aggressiveness': 90, \n\
                    'Weapons': \n\
                        [ \n\
                            'Ritual-Dagger', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Strangle', \n\
                            'Bite', \n\
                            'Punch', \n\
                        ], \n\
                    'Attributes': {'Team': ['Dog']}, \n\
                }, \n\
                { \n\
                    'Name': 'Amazon', \n\
                    'Description': 'A warrior woman. She looks angry.', \n\
                    'Health': {'Brute': 2000, 'Sharp': 1800, 'Burn': 2000, 'Freeze': 1700, 'Tame': 5500, 'Agility': 220}, \n\
                    'Aggressiveness': 100, \n\
                    'Weapons': \n\
                        [ \n\
                            'Amazonian-Bow', \n\
                            'Amazonian-Dagger', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Strangle', \n\
                            'Punch', \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Boar', \n\
                    'Description': 'A large, hairy, boar.', \n\
                    'Health': {'Brute': 1500, 'Sharp': 700, 'Burn': 600, 'Freeze': 700, 'Tame': 900, 'Agility': 100}, \n\
                    'Aggressiveness': 80, \n\
                    'Weapons': \n\
                        [ \n\
                             { \n\
                                'Name': 'Boar-Skin', \n\
                                'Description': 'Tough.', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                            'Name': 'Wear', \n\
                                            'Past Tense': 'equipped', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Brute': -1000, 'Agility': 5}, \n\
                                            'Effect Probabilities': {'Brute': 100, 'Agility': 100}, \n\
                                            'Effectiveness': {'Brute': 30, 'Agility': 100}, \n\
                                            'Attributes': {'Consumable': True, 'Self': True, 'Worn': True, 'Body': True}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Charge', \n\
                        ], \n\
                    'Attributes': {'Team': ['Boar']}, \n\
                }, \n\
                { \n\
                    'Name': 'Calydonian-Boar', \n\
                    'Description': 'A monstrous boar. It towers even above the tallest trees.', \n\
                    'Health': {'Brute': 10000, 'Sharp': 6000, 'Burn': 6000, 'Freeze': 8000, 'Tame': 10000, 'Agility': 150}, \n\
                    'Aggressiveness': 0, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Calydonian-Boar-Skin', \n\
                                'Description': 'Exceptionally tough. No amount of brute force can tear it.', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                            'Name': 'Wear', \n\
                                            'Past Tense': 'equipped', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Brute': -10000, 'Agility': 50}, \n\
                                            'Effect Probabilities': {'Brute': 100, 'Agility': 100}, \n\
                                            'Effectiveness': {'Brute': 70, 'Agility': 100}, \n\
                                            'Attributes': {'Consumable': True, 'Self': True, 'Worn': True, 'Body': True}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                          { \n\
                                'Name': 'Charge', \n\
                                'Past Tense': 'charged at', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 60, \n\
                                'Cooldown': 3, \n\
                                'Damages': {'Brute': 3000}, \n\
                                'Effect Probabilities': {'Brute': 100}, \n\
                                'Effectiveness': {'Brute': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Unique': True, 'Team': ['Boar']}, \n\
                }, \n\
                { \n\
                    'Name': 'Clazomenae-Boar', \n\
                    'Description': 'A monstrous winged boar. It towers even above the tallest trees - and it can fly.', \n\
                    'Health': {'Brute': 12000, 'Sharp': 8000, 'Burn': 6000, 'Freeze': 10000, 'Tame': 15000, 'Agility': 450}, \n\
                    'Aggressiveness': 100, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Clazomenae-Boar-Skin', \n\
                                'Description': 'Exceptionally tough. No amount of brute force can tear it. Its wings allow the wearer great agility.', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                            'Name': 'Wear', \n\
                                            'Past Tense': 'equipped', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Brute': -12000, 'Agility': -500}, \n\
                                            'Effect Probabilities': {'Brute': 100, 'Agility': 100}, \n\
                                            'Effectiveness': {'Brute': 70, 'Agility': 100}, \n\
                                            'Attributes': {'Consumable': True, 'Self': True, 'Worn': True, 'Body': True}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                          { \n\
                                'Name': 'Charge', \n\
                                'Past Tense': 'charged at', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 60, \n\
                                'Cooldown': 3, \n\
                                'Damages': {'Brute': 3500}, \n\
                                'Effect Probabilities': {'Brute': 100}, \n\
                                'Effectiveness': {'Brute': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Unique': True, 'Team': ['Boar']}, \n\
                }, \n\
                { \n\
                    'Name': 'Serpent', \n\
                    'Description': 'A small, slithering, snake. It looks venomous.', \n\
                    'Health': {'Brute': 20, 'Sharp': 30, 'Burn': 30, 'Freeze': 30, 'Tame': 100, 'Agility': 50}, \n\
                    'Aggressiveness': 70, \n\
                    'Weapons': \n\
                        [ \n\
                           { \n\
                                'Name': 'Fang', \n\
                                'Description': 'A small, white, snake fang. It drips with a milky liquid.', \n\
                                'Attacks': \n\
                                    [ \n\
                                        { \n\
                                            'Name': 'Stab', \n\
                                            'Past Tense': 'stabbed', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 90, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Sharp': 100,'Brute': 100, 'Freeze': 100, 'Burn': 100, 'Agility': 10}, \n\
                                            'Effect Probabilities': {'Sharp': 100,'Brute': 50, 'Freeze': 50, 'Burn': 50, 'Agility': 90}, \n\
                                            'Effectiveness': {'Sharp': 100,'Brute': 100, 'Freeze': 100, 'Burn': 100, 'Agility': 100}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Consumable': True, 'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Bite', \n\
                                'Past Tense': 'bit', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 60, \n\
                                'Cooldown': 1, \n\
                                'Damages': {'Sharp': 100,'Brute': 100, 'Freeze': 100, 'Burn': 100, 'Agility': 10}, \n\
                                'Effect Probabilities': {'Sharp': 100,'Brute': 50, 'Freeze': 50, 'Burn': 50, 'Agility': 80}, \n\
                                'Effectiveness': {'Sharp': 10,'Brute': 10, 'Freeze': 10, 'Burn': 10, 'Agility': 100}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Team': ['Snake']}, \n\
                }, \n\
                { \n\
                    'Name': 'Giant-Serpent', \n\
                    'Description': 'A gigantic, slithering, snake. It looks venomous.', \n\
                    'Health': {'Brute': 200, 'Sharp': 300, 'Burn': 300, 'Freeze': 300, 'Tame': 1000, 'Agility': 40}, \n\
                    'Aggressiveness': 90, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                               'Name': 'Large-Fang', \n\
                               'Description': 'A large, white, snake fang. It drips with a dark liquid.', \n\
                               'Attacks': \n\
                                   [ \n\
                                       { \n\
                                           'Name': 'Stab', \n\
                                           'Past Tense': 'stabbed', \n\
                                           'Choice Probability': 0, \n\
                                           'Hit Probability': 90, \n\
                                           'Cooldown': 0, \n\
                                           'Damages': {'Sharp': 300,'Brute': 300, 'Freeze': 300, 'Burn': 300, 'Agility': 20}, \n\
                                           'Effect Probabilities': {'Sharp': 100,'Brute': 90, 'Freeze': 90, 'Burn': 90, 'Agility': 90}, \n\
                                           'Effectiveness': {'Sharp': 70,'Brute': 70, 'Freeze': 70, 'Burn': 70, 'Agility': 90}, \n\
                                           'Attributes': {}, \n\
                                       }, \n\
                                   ], \n\
                               'Attributes': {'Body': True}, \n\
                           }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Bite', \n\
                                'Past Tense': 'bit', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': 3, \n\
                                'Damages': {'Sharp': 300,'Brute': 300, 'Freeze': 300, 'Burn': 300, 'Agility': 20}, \n\
                                'Effect Probabilities': {'Sharp': 100,'Brute': 90, 'Freeze': 90, 'Burn': 90, 'Agility': 90}, \n\
                                'Effectiveness': {'Sharp': 70,'Brute': 70, 'Freeze': 70, 'Burn': 70, 'Agility': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Team': ['Snake']}, \n\
                }, \n\
                { \n\
                    'Name': 'Cerastes', \n\
                    'Description': 'A sandy, slithering, snake. Its white horns are easily mistaken for flowers as it burrows under the sand. It looks deadly.', \n\
                    'Health': {'Brute': 200, 'Sharp': 300, 'Burn': 300, 'Freeze': 300, 'Tame': 1000, 'Agility': 400}, \n\
                    'Aggressiveness': 100, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                               'Name': 'Black-Fang', \n\
                               'Description': 'A small, dark, snake fang. It drips with an oily black liquid.', \n\
                               'Attacks': \n\
                                   [ \n\
                                       { \n\
                                           'Name': 'Stab', \n\
                                           'Past Tense': 'stabbed', \n\
                                           'Choice Probability': 0, \n\
                                           'Hit Probability': 90, \n\
                                           'Cooldown': 0, \n\
                                           'Damages': {'Sharp': 200,'Brute': 100, 'Freeze': 1000, 'Burn': 1000, 'Agility': 200}, \n\
                                           'Effect Probabilities': {'Sharp': 100,'Brute': 90, 'Freeze': 90, 'Burn': 90, 'Agility': 90}, \n\
                                           'Effectiveness': {'Sharp': 70,'Brute': 70, 'Freeze': 70, 'Burn': 70, 'Agility': 90}, \n\
                                           'Attributes': {}, \n\
                                       }, \n\
                                   ], \n\
                               'Attributes': {'Body': True}, \n\
                           }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Bite', \n\
                                'Past Tense': 'bit', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': 3, \n\
                                'Damages': {'Sharp': 200,'Brute': 100, 'Freeze': 1000, 'Burn': 1000, 'Agility': 100}, \n\
                                'Effect Probabilities': {'Sharp': 100,'Brute': 90, 'Freeze': 90, 'Burn': 90, 'Agility': 90}, \n\
                                'Effectiveness': {'Sharp': 70,'Brute': 70, 'Freeze': 70, 'Burn': 70, 'Agility': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Team': ['Snake']}, \n\
                }, \n\
                { \n\
                    'Name': 'Stymphalian-Bird', \n\
                    'Description': 'A man-eating bird with a beak and feathers of bronze.', \n\
                    'Health': {'Brute': 20, 'Sharp': 30, 'Burn': 30, 'Tame': 30, 'Tame': 300, 'Agility': 500}, \n\
                    'Aggressiveness': 100, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Bronze-Feather', \n\
                                'Description': 'A bronze feather. It\\'s very heavy.', \n\
                                'Attacks': \n\
                                    [ \n\
                                        { \n\
                                            'Name': 'Throw-At', \n\
                                            'Past Tense': 'hit', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 70, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Sharp': 500, 'Brute': 500}, \n\
                                            'Effect Probabilities': {'Sharp': 100, 'Brute': 100}, \n\
                                            'Effectiveness': {'Sharp': 40, 'Brute': 30}, \n\
                                            'Attributes': {'Thrown': True}, \n\
                                         }, \n\
                                     ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Peck', \n\
                            'Rend', \n\
                            { \n\
                                'Name': 'shoot-a-bronze-feather-at', \n\
                                'Past Tense': 'shot a bronze feather at', \n\
                                'Choice Probability': 20, \n\
                                'Hit Probability': 60, \n\
                                'Cooldown': 2, \n\
                                'Damages': {'Sharp': 300}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Ornithes-Areioi', \n\
                    'Description': 'An aggressive bird with dart-like feathers.', \n\
                    'Health': {'Brute': 30, 'Sharp': 25, 'Burn': 30, 'Tame': 30, 'Tame': 300, 'Agility': 500}, \n\
                    'Aggressiveness': 100, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Dart-Feather', \n\
                                'Description': 'A dart-like feather. It\\'s very heavy.', \n\
                                'Attacks': \n\
                                    [ \n\
                                        { \n\
                                            'Name': 'Throw-At', \n\
                                            'Past Tense': 'hit', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 80, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Sharp': 300}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 50}, \n\
                                            'Attributes': {'Thrown': True}, \n\
                                         }, \n\
                                     ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Peck', \n\
                            { \n\
                                'Name': 'shoot-a-dart-feather-at', \n\
                                'Past Tense': 'shot a dart feather at', \n\
                                'Choice Probability': 30, \n\
                                'Hit Probability': 60, \n\
                                'Cooldown': 1, \n\
                                'Damages': {'Sharp': 300}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Arae', \n\
                    'Description': 'A terrifying demon.', \n\
                    'Health': {'Brute': 4000, 'Sharp': 3000, 'Burn': 2000, 'Freeze': 2000, 'Tame': 10000, 'Agility': 5000}, \n\
                    'Aggressiveness': 100, \n\
                    'Weapons': \n\
                        [ \n\
                            'Chaos-Staff', \n\
                            { \n\
                                'Name': 'Demon-Claws', \n\
                                'Description': 'Sickeningly sharp.', \n\
                                'Attacks': \n\
                                    [ \n\
                                        { \n\
                                            'Name': 'Stab', \n\
                                            'Past Tense': 'stabbed', \n\
                                            'Choice Probability': 100, \n\
                                            'Hit Probability': 60, \n\
                                            'Cooldown': -1, \n\
                                            'Damages': {'Sharp': 1000}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 90}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                        { \n\
                                            'Name': 'Slash', \n\
                                            'Past Tense': 'slashed', \n\
                                            'Choice Probability': 70, \n\
                                            'Hit Probability': 60, \n\
                                            'Cooldown': -3, \n\
                                            'Damages': {'Sharp': 500}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 60}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                        { \n\
                                            'Name': 'Rend', \n\
                                            'Past Tense': 'rent', \n\
                                            'Choice Probability': 20, \n\
                                            'Hit Probability': 90, \n\
                                            'Cooldown': 2, \n\
                                            'Damages': {'Sharp': 2000}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 100}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                        ], \n\
                    'Attributes': {'Unique': True, 'Team': ['Demon']}, \n\
                }, \n\
                { \n\
                    'Name': 'Erinyes', \n\
                    'Description': 'A Fury. A Goddess of Vengeance.', \n\
                    'Health': {'Brute': 4000, 'Sharp': 3000, 'Burn': 2000, 'Freeze': 2000, 'Tame': 10000, 'Agility': 6000}, \n\
                    'Aggressiveness': 100, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Fury-Claws', \n\
                                'Description': 'Sickeningly sharp.', \n\
                                'Attacks': \n\
                                    [ \n\
                                        { \n\
                                            'Name': 'Stab', \n\
                                            'Past Tense': 'stabbed', \n\
                                            'Choice Probability': 100, \n\
                                            'Hit Probability': 60, \n\
                                            'Cooldown': -1, \n\
                                            'Damages': {'Sharp': 3000}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 90}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                        { \n\
                                            'Name': 'Slash', \n\
                                            'Past Tense': 'slashed', \n\
                                            'Choice Probability': 70, \n\
                                            'Hit Probability': 60, \n\
                                            'Cooldown': -3, \n\
                                            'Damages': {'Sharp': 3000}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 20}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                        { \n\
                                            'Name': 'Rend', \n\
                                            'Past Tense': 'rent', \n\
                                            'Choice Probability': 20, \n\
                                            'Hit Probability': 70, \n\
                                            'Cooldown': 2, \n\
                                            'Damages': {'Sharp': 6000}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 70}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                        ], \n\
                    'Attributes': {'Unique': True, 'Team': ['Demon'], 'Names': ['Alecto', 'Megaera', 'Tisiphone']}, \n\
                }, \n\
                { \n\
                    'Name': 'Triple-Bodied-Daemon', \n\
                    'Description': 'A mortifying demon. It has three separate bodies attached to one head.', \n\
                    'Health': {'Brute': 12000, 'Sharp': 9000, 'Burn': 6000, 'Freeze': 6000, 'Tame': 20000, 'Agility': 5500}, \n\
                    'Aggressiveness': 100, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Demon-Claws', \n\
                                'Description': 'Sickeningly sharp.', \n\
                                'Attacks': \n\
                                    [ \n\
                                        { \n\
                                            'Name': 'Stab', \n\
                                            'Past Tense': 'stabbed', \n\
                                            'Choice Probability': 100, \n\
                                            'Hit Probability': 60, \n\
                                            'Cooldown': -1, \n\
                                            'Damages': {'Sharp': 1000}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 90}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                        { \n\
                                            'Name': 'Slash', \n\
                                            'Past Tense': 'slashed', \n\
                                            'Choice Probability': 70, \n\
                                            'Hit Probability': 60, \n\
                                            'Cooldown': -3, \n\
                                            'Damages': {'Sharp': 500}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 60}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                        { \n\
                                            'Name': 'Rend', \n\
                                            'Past Tense': 'rent', \n\
                                            'Choice Probability': 20, \n\
                                            'Hit Probability': 90, \n\
                                            'Cooldown': 2, \n\
                                            'Damages': {'Sharp': 2000}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 100}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                            'Cronus\\'s-Scythe', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                        ], \n\
                    'Attributes': {'Unique': True, 'Team': ['Demon']}, \n\
                }, \n\
                { \n\
                    'Name': 'Ceuthonymus', \n\
                    'Description': 'A terrifying demon of the underworld.', \n\
                    'Health': {'Brute': 5000, 'Sharp': 4000, 'Burn': 5000, 'Freeze': 1000, 'Tame': 10000, 'Agility': 5300}, \n\
                    'Aggressiveness': 100, \n\
                    'Weapons': \n\
                        [ \n\
                            'Magic-Staff', \n\
                            { \n\
                                'Name': 'Demon-Claws', \n\
                                'Description': 'Sickeningly sharp.', \n\
                                'Attacks': \n\
                                    [ \n\
                                        { \n\
                                            'Name': 'Stab', \n\
                                            'Past Tense': 'stabbed', \n\
                                            'Choice Probability': 100, \n\
                                            'Hit Probability': 60, \n\
                                            'Cooldown': -1, \n\
                                            'Damages': {'Sharp': 1000}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 90}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                        { \n\
                                            'Name': 'Slash', \n\
                                            'Past Tense': 'slashed', \n\
                                            'Choice Probability': 70, \n\
                                            'Hit Probability': 60, \n\
                                            'Cooldown': -3, \n\
                                            'Damages': {'Sharp': 500}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 60}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                        { \n\
                                            'Name': 'Rend', \n\
                                            'Past Tense': 'rent', \n\
                                            'Choice Probability': 20, \n\
                                            'Hit Probability': 90, \n\
                                            'Cooldown': 2, \n\
                                            'Damages': {'Sharp': 2000}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 100}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                        ], \n\
                    'Attributes': {'Unique': True, 'Team': ['Demon']}, \n\
                }, \n\
                { \n\
                    'Name': 'Eurynomos', \n\
                    'Description': 'A terrifying demon.', \n\
                    'Health': {'Brute': 4000, 'Sharp': 3000, 'Burn': 2000, 'Freeze': 2000, 'Tame': 10000, 'Agility': 5200}, \n\
                    'Aggressiveness': 100, \n\
                    'Weapons': \n\
                        [ \n\
                            'Magic-Staff', \n\
                            { \n\
                                'Name': 'Demon-Claws', \n\
                                'Description': 'Sickeningly sharp.', \n\
                                'Attacks': \n\
                                    [ \n\
                                        { \n\
                                            'Name': 'Stab', \n\
                                            'Past Tense': 'stabbed', \n\
                                            'Choice Probability': 100, \n\
                                            'Hit Probability': 60, \n\
                                            'Cooldown': -1, \n\
                                            'Damages': {'Sharp': 1000}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 90}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                        { \n\
                                            'Name': 'Slash', \n\
                                            'Past Tense': 'slashed', \n\
                                            'Choice Probability': 70, \n\
                                            'Hit Probability': 60, \n\
                                            'Cooldown': -3, \n\
                                            'Damages': {'Sharp': 500}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 60}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                        { \n\
                                            'Name': 'Rend', \n\
                                            'Past Tense': 'rent', \n\
                                            'Choice Probability': 20, \n\
                                            'Hit Probability': 90, \n\
                                            'Cooldown': 2, \n\
                                            'Damages': {'Sharp': 2000}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 100}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                        ], \n\
                    'Attributes': {'Unique': True, 'Team': ['Demon']}, \n\
                }, \n\
                { \n\
                    'Name': 'Pygmy', \n\
                    'Description': 'A tiny, yet very aggressive, man. He stands no higher than a foot and a half from the ground.', \n\
                    'Health': {'Brute': 500, 'Sharp': 400, 'Burn': 400, 'Freeze': 450, 'Tame': 2000, 'Agility': 200}, \n\
                    'Aggressiveness': 70, \n\
                    'Weapons': \n\
                        [ \n\
                            'Doru', \n\
                            'Sfendonai', \n\
                            'Akontia', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Bite', \n\
                            'Punch', \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Nymph', \n\
                    'Description': 'A minor nature goddess.', \n\
                    'Health': {'Brute': 500, 'Sharp': 400, 'Burn': 1000, 'Freeze': 1000, 'Tame': 6000, 'Divine': 1000, 'Agility': 200}, \n\
                    'Aggressiveness': 70, \n\
                    'Weapons': \n\
                        [ \n\
                            'Magic-Staff', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                        ], \n\
                    'Attributes': {'Team': ['Dryad']}, \n\
                }, \n\
                { \n\
                    'Name': 'Spartae', \n\
                    'Description': 'A heavily clad, ghostly skeleton warrior.', \n\
                    'Health': {'Brute': 3000, 'Sharp': 2700, 'Burn': 2500, 'Freeze': 2600, 'Tame': 0, 'Agility': 100}, \n\
                    'Aggressiveness': 0, \n\
                    'Weapons': \n\
                        [ \n\
                            'Doru', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Stab', \n\
                                'Past Tense': 'stabbed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': -2, \n\
                                'Damages': {'Sharp': 2000}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Gigantic-Tortoise', \n\
                    'Description': 'A giant, man-eating, tortoise.', \n\
                    'Health': {'Brute': 6000, 'Sharp': 5500, 'Burn': 500, 'Freeze': 3000, 'Tame': 7000, 'Agility': 1}, \n\
                    'Aggressiveness': 100, \n\
                    'Weapons': \n\
                        [ \n\
                           { \n\
                                'Name': 'Gigantic-Tortoise-Shell', \n\
                                'Description': 'Exceptionally hard. Neither your sharpest blade nor your most forceful blow can penetrate it.', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                            'Name': 'Wear', \n\
                                            'Past Tense': 'equipped', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Sharp': -5500, 'Brute': -6000, 'Agility': 120}, \n\
                                            'Effect Probabilities': {'Sharp': 100, 'Brute': 100, 'Agility': 100}, \n\
                                            'Effectiveness': {'Sharp': 95, 'Brute': 95, 'Agility': 100}, \n\
                                            'Attributes': {'Consumable': True, 'Self': True, 'Worn': True, 'Body': True}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Bite', \n\
                                'Past Tense': 'bit', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 60, \n\
                                'Cooldown': 4, \n\
                                'Damages': {'Brute': 800}, \n\
                                'Effect Probabilities': {'Brute': 100}, \n\
                                'Effectiveness': {'Brute': 70}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Unique': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Giant-Tortoise', \n\
                    'Description': 'A giant tortoise.', \n\
                    'Health': {'Brute': 3500, 'Sharp': 3000, 'Burn': 2500, 'Freeze': 3000, 'Tame': 100, 'Agility': 1}, \n\
                    'Aggressiveness': 0, \n\
                    'Weapons': \n\
                        [ \n\
                           { \n\
                                'Name': 'Giant-Tortoise-Shell', \n\
                                'Description': 'Extremely hard. Much effort is required to penetrate it.', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                            'Name': 'Wear', \n\
                                            'Past Tense': 'equipped', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Sharp': -3000, 'Brute': -3500, 'Agility': 100}, \n\
                                            'Effect Probabilities': {'Sharp': 100, 'Brute': 100, 'Agility': 100}, \n\
                                            'Effectiveness': {'Sharp': 95, 'Brute': 95, 'Agility': 100}, \n\
                                            'Attributes': {'Consumable': True, 'Self': True, 'Worn': True, 'Body': True}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Bite', \n\
                                'Past Tense': 'bit', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 60, \n\
                                'Cooldown': 4, \n\
                                'Damages': {'Brute': 200}, \n\
                                'Effect Probabilities': {'Brute': 100}, \n\
                                'Effectiveness': {'Brute': 70}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Wolf', \n\
                    'Description': 'A shaggy wolf. It\\'s snarling at you.', \n\
                    'Health': {'Brute': 700, 'Sharp': 500, 'Burn': 300, 'Freeze': 700, 'Tame': 300, 'Agility': 1500}, \n\
                    'Aggressiveness': 70, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                              'Name': 'Wolf-Pelt', \n\
                              'Description': 'Thick and warm.', \n\
                              'Attacks': \n\
                                  [ \n\
                                       { \n\
                                          'Name': 'Wear', \n\
                                          'Past Tense': 'equipped', \n\
                                          'Choice Probability': 0, \n\
                                          'Hit Probability': 100, \n\
                                          'Cooldown': 0, \n\
                                          'Damages': {'Freeze': -500, 'Agility': 5}, \n\
                                          'Effect Probabilities': {'Freeze': 100, 'Agility': 100}, \n\
                                          'Effectiveness': {'Freeze': 30, 'Agility': 100}, \n\
                                          'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                                      }, \n\
                                  ], \n\
                              'Attributes': {'Body': True}, \n\
                          }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Bite', \n\
                            'Claw', \n\
                        ], \n\
                    'Attributes': {'Team': ['Dog']}, \n\
                }, \n\
                { \n\
                    'Name': 'Monk\\'s-Dog', \n\
                    'Description': 'A shaggy hound. It\\'s snarling at you.', \n\
                    'Health': {'Brute': 600, 'Sharp': 400, 'Burn': 300, 'Freeze': 600, 'Tame': 500, 'Agility': 300}, \n\
                    'Aggressiveness': 100, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                              'Name': 'Dog-Pelt', \n\
                              'Description': 'Thick and warm.', \n\
                              'Attacks': \n\
                                  [ \n\
                                       { \n\
                                          'Name': 'Wear', \n\
                                          'Past Tense': 'equipped', \n\
                                          'Choice Probability': 0, \n\
                                          'Hit Probability': 100, \n\
                                          'Cooldown': 0, \n\
                                          'Damages': {'Freeze': -600, 'Agility': 5}, \n\
                                          'Effect Probabilities': {'Freeze': 100, 'Agility': 100}, \n\
                                          'Effectiveness': {'Freeze': 30, 'Agility': 100}, \n\
                                          'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                                      }, \n\
                                  ], \n\
                              'Attributes': {'Body': True}, \n\
                          }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Bite', \n\
                            'Claw', \n\
                        ], \n\
                    'Attributes': {'Team': ['Dog', 'Story-Teller']}, \n\
                }, \n\
                { \n\
                    'Name': 'Werewolf', \n\
                    'Description': 'A lycanthrope. Shaggy and strange.', \n\
                    'Health': {'Brute': 1700, 'Sharp': 1500, 'Burn': 1300, 'Freeze': 1700, 'Tame': 1300, 'Agility': 4500}, \n\
                    'Aggressiveness': 90, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Werewolf-Pelt', \n\
                                'Description': 'Thick and warm and ...unnerving.', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                            'Name': 'Wear', \n\
                                            'Past Tense': 'equipped', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Freeze': -900, 'Agility': 10}, \n\
                                            'Effect Probabilities': {'Freeze': 100, 'Agility': 100}, \n\
                                            'Effectiveness': {'Freeze': 30, 'Agility': 100}, \n\
                                            'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Moon-Pendant', \n\
                                'Description': 'A moon-shaped, silvery pendant which glimmers before you.', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                            'Name': 'Wear', \n\
                                            'Past Tense': 'equipped', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Agility': -200}, \n\
                                            'Effect Probabilities': {'Agility': 100}, \n\
                                            'Effectiveness': {'Agility': 100}, \n\
                                            'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Bite', \n\
                                'Past Tense': 'bit', \n\
                                'Choice Probability': 10, \n\
                                'Hit Probability': 90, \n\
                                'Cooldown': 1, \n\
                                'Damages': {'Sharp': 400}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 80}, \n\
                                'Attributes': {'Wolf': True}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Claw', \n\
                                'Past Tense': 'clawed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 90, \n\
                                'Cooldown': -1, \n\
                                'Damages': {'Sharp': 1300}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Team': ['Dog'], 'Names': ['Agriopas', 'Damarchus', 'Lycaon']}, \n\
                }, \n\
                { \n\
                    'Name': 'Vampire', \n\
                    'Description': 'A demonic vampire.', \n\
                    'Health': {'Brute': 1000, 'Sharp': 800, 'Burn': 10, 'Freeze': 1000, 'Tame': 5000, 'Agility': 100}, \n\
                    'Aggressiveness': 90, \n\
                    'Weapons': \n\
                        [ \n\
                            'Dagger', \n\
                            { \n\
                                'Name': 'Blood-Pendant', \n\
                                'Description': 'A tear-shaped, crimson pendant which glimmers before you.', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                            'Name': 'Wear', \n\
                                            'Past Tense': 'equipped', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Divine': -1000}, \n\
                                            'Effect Probabilities': {'Divine': 100}, \n\
                                            'Effectiveness': {'Divine': 100}, \n\
                                            'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Bite', \n\
                                'Past Tense': 'bit', \n\
                                'Choice Probability': 10, \n\
                                'Hit Probability': 90, \n\
                                'Cooldown': 1, \n\
                                'Damages': {'Sharp': 200}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 80}, \n\
                                'Attributes': {'Vampire': True}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Names': ['Empousa', 'Lamia', 'Mormo', 'Mormolykeia']}, \n\
                }, \n\
                { \n\
                    'Name': 'Amalthea', \n\
                    'Description': 'A shaggy goat with divine and golden hair.', \n\
                    'Health': {'Brute': 100, 'Sharp': 50, 'Burn': 100, 'Freeze': 400, 'Tame': 10, 'Agility': 20}, \n\
                    'Aggressiveness': 0, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Golden-Pelt', \n\
                                'Description': 'An item of great value.', \n\
                                'Attacks': \n\
                                    [ \n\
                                    ], \n\
                                'Attributes': {'Body': True, 'Treasure': True}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Aegis', \n\
                                'Description': 'A huge, gilded, white shield belonging to the god of gods. The head of a gorgon is mounted in its center.', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                            'Name': 'Petrify', \n\
                                            'Past Tense': 'petrified', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 25, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Soul': 1}, \n\
                                            'Effect Probabilities': {'Soul': 100}, \n\
                                            'Effectiveness': {'Soul': 100}, \n\
                                            'Attributes': {'Cooldown': True}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Shield': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                        ], \n\
                    'Attributes': {'Unique': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Unicorn', \n\
                    'Description': 'A majestic horse of pure white with a single, ivory horn jutting from its head.', \n\
                    'Health': {'Brute': 300, 'Sharp': 100, 'Burn': 100, 'Freeze': 200, 'Tame': 1000, 'Divine': 1000, 'Agility': 300}, \n\
                    'Aggressiveness': 0, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Unicorn-Horn', \n\
                                'Description': 'Innocent and white.', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                           'Name': 'Consume', \n\
                                           'Past Tense': 'healed', \n\
                                           'Choice Probability': 0, \n\
                                           'Hit Probability': 100, \n\
                                           'Cooldown': 0, \n\
                                           'Damages': {}, \n\
                                           'Effect Probabilities': {}, \n\
                                           'Effectiveness': {}, \n\
                                           'Attributes': {'Unicorn': True}, \n\
                                         }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Kick', \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Harpy', \n\
                    'Description': 'A flying creature which appears to be half woman and half bird.', \n\
                    'Health': {'Brute': 600, 'Sharp': 400, 'Burn': 200, 'Freeze': 500, 'Tame': 10000, 'Agility': 400}, \n\
                    'Aggressiveness': 100, \n\
                    'Weapons': \n\
                        [ \n\
                           { \n\
                                'Name': 'Harpy-Feather', \n\
                                'Description': 'A blue feather. It\\'s heavy.', \n\
                                'Attacks': \n\
                                    [ \n\
                                        { \n\
                                            'Name': 'Throw-At', \n\
                                            'Past Tense': 'hit', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 60, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Sharp': 600}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 90}, \n\
                                            'Attributes': {'Thrown': True}, \n\
                                         }, \n\
                                     ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Claw', \n\
                                'Past Tense': 'clawed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Sharp': 600}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 50}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Aethon', \n\
                    'Description': 'A gigantic eagle. It looks angry.', \n\
                    'Health': {'Brute': 1000, 'Sharp': 900, 'Burn': 900, 'Freeze': 900, 'Tame': 10000, 'Agility': 350}, \n\
                    'Aggressiveness': 100, \n\
                    'Weapons': \n\
                        [ \n\
                           { \n\
                                'Name': 'Talon', \n\
                                'Description': 'A polished, black, talon. Naturally sharp, and naturally deadly.', \n\
                                'Attacks': \n\
                                    [ \n\
                                        { \n\
                                            'Name': 'Slash', \n\
                                            'Past Tense': 'slashed', \n\
                                            'Choice Probability': 70, \n\
                                            'Hit Probability': 90, \n\
                                            'Cooldown': -1, \n\
                                            'Damages': {'Sharp': 700}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 30}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                        { \n\
                                            'Name': 'Rend', \n\
                                            'Past Tense': 'rent', \n\
                                            'Choice Probability': 20, \n\
                                            'Hit Probability': 90, \n\
                                            'Cooldown': 2, \n\
                                            'Damages': {'Sharp': 1000}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 95}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Rend', \n\
                            'Claw', \n\
                        ], \n\
                    'Attributes': {'Unique': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Griffin', \n\
                    'Description': 'A large creature with the lower half of a lion and the upper half of an eagle.', \n\
                    'Health': {'Brute': 3000, 'Sharp': 2000, 'Burn': 1500, 'Freeze': 2000, 'Tame': 6000, 'Agility': 400}, \n\
                    'Aggressiveness': 100, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Griffin-Claws', \n\
                                'Description': 'Rather sharp. Known to have medicinal properties.', \n\
                                'Attacks': \n\
                                    [ \n\
                                        { \n\
                                            'Name': 'Stab', \n\
                                            'Past Tense': 'stabbed', \n\
                                            'Choice Probability': 100, \n\
                                            'Hit Probability': 60, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Sharp': 300}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 80}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                        { \n\
                                            'Name': 'Slash', \n\
                                            'Past Tense': 'slashed', \n\
                                            'Choice Probability': 70, \n\
                                            'Hit Probability': 90, \n\
                                            'Cooldown': -3, \n\
                                            'Damages': {'Sharp': 200}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 40}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                        { \n\
                                            'Name': 'Rend', \n\
                                            'Past Tense': 'rent', \n\
                                            'Choice Probability': 20, \n\
                                            'Hit Probability': 70, \n\
                                            'Cooldown': 2, \n\
                                            'Damages': {'Sharp': 600}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 100}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                        { \n\
                                            'Name': 'Consume', \n\
                                            'Past Tense': 'healed', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Brute': -3000, 'Sharp': -3000, 'Burn': -1500, 'Freeze': -1800}, \n\
                                            'Effect Probabilities': {'Brute': 100, 'Sharp': 90, 'Burn': 75, 'Freeze': 75}, \n\
                                            'Effectiveness': {'Brute': 60, 'Sharp': 60, 'Burn': 60, 'Freeze': 50}, \n\
                                            'Attributes': {'Consumable': True, 'Self': True}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Golden-Egg', \n\
                                'Description': 'An item of great value.', \n\
                                'Attacks': \n\
                                    [ \n\
                                    ], \n\
                                'Attributes': {'Body': True, 'Treasure': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Rend', \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Pegasus', \n\
                    'Description': 'A pure white, winged horse. Majestic and divine. Something about it seems oddly terrifying.', \n\
                    'Health': {'Brute': 5000, 'Sharp': 3500, 'Burn': 3000, 'Freeze': 3500, 'Tame': 100000000, 'Divine': 1000, 'Tame+': 10, 'Agility': 400}, \n\
                    'Aggressiveness': 0, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Divine-Pelt', \n\
                                'Description': 'Ethereal and white.', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                            'Name': 'Wear', \n\
                                            'Past Tense': 'equipped', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Divine': -2000, 'Agility': 20}, \n\
                                            'Effect Probabilities': {'Divine': 100, 'Agility': 100}, \n\
                                            'Effectiveness': {'Divine': 70, 'Agility': 100}, \n\
                                            'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                                         }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Kick', \n\
                            { \n\
                                'Name': 'Evanesce', \n\
                                'Past Tense': 'evanesced', \n\
                                'Choice Probability': 1, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 5, \n\
                                'Damages': {'Life': 1}, \n\
                                'Effect Probabilities': {'Life': 100}, \n\
                                'Effectiveness': {'Life': 100}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Siren', \n\
                    'Description': 'A Siren. A female figure with bird legs and wings. Beware her deadly song.', \n\
                    'Health': {'Brute': 1000, 'Sharp': 800, 'Burn': 800, 'Freeze': 800, 'Tame': 1000000000, 'Agility': 400}, \n\
                    'Aggressiveness': 100, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Crown-of-Feathers', \n\
                                'Description': 'A crown of feathery white. Crafted from the remains of a dead Siren.', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                            'Name': 'Wear', \n\
                                            'Past Tense': 'equipped', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Divine': -1000, 'Agility': 20}, \n\
                                            'Effect Probabilities': {'Divine': 100, 'Agility': 100}, \n\
                                            'Effectiveness': {'Divine': 100, 'Agility': 100}, \n\
                                            'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                                         }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Siren-Wings', \n\
                                'Description': 'Wings of white.', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                            'Name': 'Wear', \n\
                                            'Past Tense': 'equipped', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Agility': -500}, \n\
                                            'Effect Probabilities': {'Agility': 100}, \n\
                                            'Effectiveness': {'Agility': 100}, \n\
                                            'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                                         }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Sing', \n\
                                'Past Tense': 'sang to', \n\
                                'Choice Probability': 5, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 5, \n\
                                'Damages': {'Brute': -1}, \n\
                                'Effect Probabilities': {'Brute': 100}, \n\
                                'Effectiveness': {'Brute': 100}, \n\
                                'Attributes': {'Sleep+': True}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Watch', \n\
                                'Past Tense': 'warily watched', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': -1}, \n\
                                'Effect Probabilities': {'Brute': 100}, \n\
                                'Effectiveness': {'Brute': 100}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Names': ['Aglaope', 'Leucosia', 'Ligeia', 'Molpe', 'Parthenope', 'Peisinoe', 'Thelxiope'], 'Team': ['All']}, \n\
                }, \n\
                { \n\
                    'Name': 'Bear', \n\
                    'Description': 'A large grizzly.', \n\
                    'Health': {'Brute': 900, 'Sharp': 600, 'Burn': 600, 'Freeze': 700, 'Tame': 1000, 'Agility': 200}, \n\
                    'Aggressiveness':90, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                 'Name': 'Bear-Pelt', \n\
                                 'Description': 'Very thick and very warm.', \n\
                                 'Attacks': \n\
                                     [ \n\
                                         { \n\
                                            'Name': 'Wear', \n\
                                            'Past Tense': 'equipped', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Freeze': -500, 'Agility': 12}, \n\
                                            'Effect Probabilities': {'Freeze': 100, 'Agility': 100}, \n\
                                            'Effectiveness': {'Freeze': 70, 'Agility': 100}, \n\
                                            'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                                         }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Bite', \n\
                                'Past Tense': 'bit', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 60, \n\
                                'Cooldown': 1, \n\
                                'Damages': {'Sharp': 300}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 10}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Claw', \n\
                                'Past Tense': 'clawed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Sharp': 400}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Arachne', \n\
                    'Description': 'A disturbing creature with the lower half of a spider and the upper half of a woman.', \n\
                    'Health': {'Brute': 2000, 'Sharp': 1500, 'Burn': 1000, 'Freeze': 2000, 'Tame': 10000, 'Agility': 300}, \n\
                    'Aggressiveness':100, \n\
                    'Weapons': \n\
                        [ \n\
                            'Akontia', \n\
                            'Thread-of-Ariadne', \n\
                            'Thread-of-Ariadne', \n\
                            'Thread-of-Ariadne', \n\
                            { \n\
                                'Name': 'Web', \n\
                                'Description': 'A tangled mess of silk. Great for disarming foes.', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                            'Name': 'Cast-At', \n\
                                            'Past Tense': 'cast at', \n\
                                            'Choice Probability': 20, \n\
                                            'Hit Probability': 60, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {}, \n\
                                            'Effect Probabilities': {}, \n\
                                            'Effectiveness': {}, \n\
                                            'Attributes': {'Thrown': True, 'Disarm': True}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Slash', \n\
                                'Past Tense': 'slashed', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': -3, \n\
                                'Damages': {'Sharp': 300, 'Agility': 100}, \n\
                                'Effect Probabilities': {'Sharp': 100, 'Agility': 70}, \n\
                                'Effectiveness': {'Sharp': 100, 'Agility': 5}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Unique': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Graeae', \n\
                    'Description': 'A Graeae. One of three hags who share a single eye between them.', \n\
                    'Health': {'Brute': 1000, 'Sharp': 500, 'Burn': 500, 'Freeze': 1000, 'Tame': 10000, 'Agility': 60}, \n\
                    'Aggressiveness':100, \n\
                    'Weapons': \n\
                        [ \n\
                            'Ritual-Dagger', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Strangle', \n\
                            'Punch', \n\
                        ], \n\
                    'Attributes': {'Unique': True, 'Names': ['Deino', 'Enyo', 'Pemphredo']}, \n\
                }, \n\
                { \n\
                    'Name': 'Dragon', \n\
                    'Description': 'A huge, fire-breathing dragon.', \n\
                    'Health': {'Brute': 10000, 'Sharp': 9000, 'Burn': 100000, 'Freeze': 5000, 'Tame': 20000, 'Agility': 200}, \n\
                    'Aggressiveness': 100, \n\
                    'Weapons': \n\
                        [ \n\
                            'Dragon\\'s-Teeth', \n\
                            { \n\
                                'Name': 'Dragon-Claws', \n\
                                'Description': 'A handful of wicked-sharp claws of a dragon.', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                            'Name': 'Eviscerate', \n\
                                            'Past Tense': 'eviscerated', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 80, \n\
                                            'Cooldown': 1, \n\
                                            'Ammo': 4, \n\
                                            'Damages': {'Sharp': 10000}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 10}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Burn', \n\
                            { \n\
                                'Name': 'Bite', \n\
                                'Past Tense': 'bit', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 90, \n\
                                'Cooldown': 1, \n\
                                'Damages': {'Sharp': 1500}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Claw', \n\
                                'Past Tense': 'clawed', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 90, \n\
                                'Cooldown': -1, \n\
                                'Damages': {'Sharp': 2000}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Team': ['Snake'], 'Names': ['Cychreides', 'Delphyne', 'Giantomachian-Dragon', 'Ismenian-Dragon', 'Maeonian-Drakon', 'Pitanian-Dragon', 'Thespian-Dragon', 'Rhodian-Dragon', 'Python', 'Trojan-Dragon']}, \n\
                }, \n\
                { \n\
                    'Name': 'Pyrausta', \n\
                    'Description': 'A fire-breathing dragon the size of a large fly.', \n\
                    'Health': {'Brute': 10, 'Sharp': 20, 'Burn': 100000, 'Freeze': 1, 'Tame': 20, 'Agility': 400}, \n\
                    'Aggressiveness':100, \n\
                    'Weapons': \n\
                        [ \n\
                            'Dragon\\'s-Teeth', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                           { \n\
                                'Name': 'Burn', \n\
                                'Past Tense': 'incinerated', \n\
                                'Choice Probability': 75, \n\
                                'Hit Probability': 95, \n\
                                'Cooldown': 3, \n\
                                'Ammo': 0, \n\
                                'Damages': {'Burn': 200}, \n\
                                'Effect Probabilities': {'Burn': 100}, \n\
                                'Effectiveness': {'Burn': 40}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Bite', \n\
                                'Past Tense': 'bit', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 90, \n\
                                'Cooldown': 1, \n\
                                'Damages': {'Sharp': 10}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Claw', \n\
                                'Past Tense': 'clawed', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 90, \n\
                                'Cooldown': -1, \n\
                                'Damages': {'Sharp': 20}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Team': ['Snake']}, \n\
                }, \n\
                { \n\
                    'Name': 'Grendel', \n\
                    'Description': '\\'...the other, warped - in the shape of a man, moves beyond the pale - bigger than any man, an unnatural birth - called Grendel by the country people, in former days.\\'', \n\
                    'Health': {'Brute': 1000, 'Sharp': 9000, 'Burn': 6000, 'Freeze': 10000, 'Tame': 20000, 'Agility': 4000}, \n\
                    'Aggressiveness':100, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Grendel\\'s-Arm', \n\
                                'Description': '\\'Every nail, claw-scale and spur, every spike and welt on the hand of that heathen brute was like barbed steel.\\'', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                            'Name': 'Eviscerate', \n\
                                            'Past Tense': 'eviscerated', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 25, \n\
                                            'Cooldown': 1, \n\
                                            'Damages': {'Sharp': 3000}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 100}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                        { \n\
                                            'Name': 'Pummel', \n\
                                            'Past Tense': 'pummeled', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 80, \n\
                                            'Cooldown': 1, \n\
                                            'Damages': {'Brute': 3000}, \n\
                                            'Effect Probabilities': {'Brute': 100}, \n\
                                            'Effectiveness': {'Brute': 10}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                               'Name': 'Eviscerate', \n\
                               'Past Tense': 'eviscerated', \n\
                               'Choice Probability': 50, \n\
                               'Hit Probability': 80, \n\
                               'Cooldown': 1, \n\
                               'Damages': {'Sharp': 3000}, \n\
                               'Effect Probabilities': {'Sharp': 100}, \n\
                               'Effectiveness': {'Sharp': 10}, \n\
                               'Attributes': {}, \n\
                           }, \n\
                           { \n\
                               'Name': 'Pummel', \n\
                               'Past Tense': 'pummeled', \n\
                               'Choice Probability': 50, \n\
                               'Hit Probability': 80, \n\
                               'Cooldown': 1, \n\
                               'Damages': {'Brute': 2000}, \n\
                               'Effect Probabilities': {'Brute': 100}, \n\
                               'Effectiveness': {'Brute': 10}, \n\
                               'Attributes': {}, \n\
                           }, \n\
                        ], \n\
                    'Attributes': {'Team': ['All'], 'Unique': True, 'Grendel': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Earth-Dragon', \n\
                    'Description': 'A ferocious, fire-breathing dragon. \\'The plaguer of the people for three hundred winters ... the terrible earth-dragon.\\'', \n\
                    'Health': {'Brute': 20000, 'Sharp': 19000, 'Burn': 50000, 'Freeze': 10000, 'Tame': 100000, 'Agility': 2000}, \n\
                    'Aggressiveness':100, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Dastardly-Claw', \n\
                                'Description': 'Terribly sharp.', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                            'Name': 'Eviscerate', \n\
                                            'Past Tense': 'eviscerated', \n\
                                            'Choice Probability': 10, \n\
                                            'Hit Probability': 80, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Sharp': 10000}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 60}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                           { \n\
                                'Name': 'Burn', \n\
                                'Past Tense': 'incinerated', \n\
                                'Choice Probability': 5, \n\
                                'Hit Probability': 95, \n\
                                'Cooldown': 5, \n\
                                'Ammo': 0, \n\
                                'Damages': {'Burn': 20000}, \n\
                                'Effect Probabilities': {'Burn': 100}, \n\
                                'Effectiveness': {'Burn': 10}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Bite', \n\
                                'Past Tense': 'bit', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': 1, \n\
                                'Damages': {'Sharp': 5000}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Claw', \n\
                                'Past Tense': 'clawed', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': -1, \n\
                                'Damages': {'Sharp': 3000}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Team': ['All'], 'Unique': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Grendel\\'s-Mother', \n\
                    'Description': '\\'A monstrous hag.\\'', \n\
                    'Health': {'Brute': 100000, 'Sharp': 100000, 'Burn': 100000, 'Freeze': 100000, 'Tame': 100000, 'Giant+': 100, 'Agility': 4000}, \n\
                    'Aggressiveness':100, \n\
                    'Weapons': \n\
                        [ \n\
                            'Naegling', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Eviscerate', \n\
                                'Past Tense': 'eviscerated', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': 1, \n\
                                'Damages': {'Sharp': 6000}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 70}, \n\
                                'Attributes': {}, \n\
                             }, \n\
                             { \n\
                                'Name': 'Pummel', \n\
                                'Past Tense': 'pummeled', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': 1, \n\
                                'Damages': {'Brute': 5000}, \n\
                                'Effect Probabilities': {'Brute': 100}, \n\
                                'Effectiveness': {'Brute': 60}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Team': ['All'], 'Unique': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Teumessian-Fox', \n\
                    'Description': 'A gigantic orange-red fox. It towers majestically over the tallest trees.', \n\
                    'Health': {'Brute': 100000, 'Sharp': 100000, 'Burn': 100000, 'Freeze': 100000, 'Tame': 100000, 'Laelaps+': 10, 'Agility': 0}, \n\
                    'Aggressiveness':0, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Teumessian-Fox-Pelt', \n\
                                'Description': 'An orange-red belt so smooth as to be silky and so beautiful as to be indescribable.', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                            'Name': 'Wear', \n\
                                            'Past Tense': 'equipped', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Agility': -10000000}, \n\
                                            'Effect Probabilities': {'Agility': 100}, \n\
                                            'Effectiveness': {'Agility': 100}, \n\
                                            'Attributes': {'Speed': True, 'Consumable': True, 'Self': True, 'Worn': True}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                        ], \n\
                    'Attributes': {'Unique': True, 'Team': ['All'], 'Fox': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Laelaps', \n\
                    'Description': 'An alert, brown greyhound. It watches you happily.', \n\
                    'Health': {'Brute': 2000, 'Sharp': 1000, 'Burn': 1000, 'Freeze': 2000, 'Tame': 100, 'Agility': 0}, \n\
                    'Aggressiveness':0, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Dog-Collar', \n\
                                'Description': 'A sad reminder of a life lost.', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                            'Name': 'Wear', \n\
                                            'Past Tense': 'equipped', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Charisma': -1}, \n\
                                            'Effect Probabilities': {'Charisma': 100}, \n\
                                            'Effectiveness': {'Charisma': 100}, \n\
                                            'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                               'Name': 'Bite', \n\
                               'Past Tense': 'bit', \n\
                               'Choice Probability': 100, \n\
                               'Hit Probability': 100, \n\
                               'Cooldown': 0, \n\
                               'Damages': {'Sharp': 700, 'Laelaps+': 100}, \n\
                               'Effect Probabilities': {'Sharp': 100, 'Laelaps+': 100}, \n\
                               'Effectiveness': {'Sharp': 80, 'Laelaps+': 100}, \n\
                               'Attributes': {}, \n\
                           }, \n\
                        ], \n\
                    'Attributes': {'Unique': True, 'Team': ['Dog']}, \n\
                }, \n\
                { \n\
                    'Name': 'Colchian-Dragon', \n\
                    'Description': 'An ancient, monstrous serpent. Ever-wakeful, the serpent far surpasses in length and breadth a ship of fifty oars.', \n\
                    'Health': {'Brute': 80000, 'Sharp': 70000, 'Burn': 1000000, 'Freeze': 40000, 'Divine': 4900, 'Tame': 100000000, 'Agility': 1000}, \n\
                    'Aggressiveness': 0, \n\
                    'Weapons': \n\
                        [ \n\
                            'Dragon\\'s-Teeth', \n\
                            'Panacea', \n\
                            'Water-of-Langia', \n\
                            'Golden-Fleece', \n\
                            { \n\
                                'Name': 'Adamantine-Dragon-Claws', \n\
                                'Description': 'A handful of wicked-sharp, adamantine claws of the deadliest of dragons.', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                            'Name': 'Eviscerate', \n\
                                            'Past Tense': 'eviscerated', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 80, \n\
                                            'Cooldown': -2, \n\
                                            'Damages': {'Sharp': 10000, 'Divine': 2000}, \n\
                                            'Effect Probabilities': {'Sharp': 100, 'Divine': 100}, \n\
                                            'Effectiveness': {'Sharp': 100, 'Divine': 90}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                           { \n\
                                'Name': 'Burn', \n\
                                'Past Tense': 'incinerated', \n\
                                'Choice Probability': 1, \n\
                                'Hit Probability': 95, \n\
                                'Cooldown': 5, \n\
                                'Ammo': 0, \n\
                                'Damages': {'Burn': 25000}, \n\
                                'Effect Probabilities': {'Burn': 100}, \n\
                                'Effectiveness': {'Burn': 10}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Bite', \n\
                                'Past Tense': 'bit', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': 1, \n\
                                'Damages': {'Sharp': 9000}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Claw', \n\
                                'Past Tense': 'clawed', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': -1, \n\
                                'Damages': {'Sharp': 6000}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Unique': True, 'Team': ['Snake', 'Bull']}, \n\
                }, \n\
                { \n\
                    'Name': 'Nemean-Dragon', \n\
                    'Description': 'A monstrous serpent. A gold crest is proudly set into its chest.', \n\
                    'Health': {'Brute': 20000, 'Sharp': 19000, 'Burn': 50000, 'Freeze': 10000, 'Divine': 4000, 'Tame': 40000, 'Agility': 1000}, \n\
                    'Aggressiveness': 0, \n\
                    'Weapons': \n\
                        [ \n\
                            'Dragon\\'s-Teeth', \n\
                            'Panacea', \n\
                            'Water-of-Langia', \n\
                            { \n\
                                'Name': 'Golden-Dragon-Claws', \n\
                                'Description': 'A handful of wicked-sharp, golden claws of an ancient dragon.', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                            'Name': 'Eviscerate', \n\
                                            'Past Tense': 'eviscerated', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 80, \n\
                                            'Cooldown': 1, \n\
                                            'Ammo': 4, \n\
                                            'Damages': {'Sharp': 10000}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 98}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                           { \n\
                                'Name': 'Burn', \n\
                                'Past Tense': 'incinerated', \n\
                                'Choice Probability': 1, \n\
                                'Hit Probability': 95, \n\
                                'Cooldown': 5, \n\
                                'Ammo': 0, \n\
                                'Damages': {'Burn': 20000}, \n\
                                'Effect Probabilities': {'Burn': 100}, \n\
                                'Effectiveness': {'Burn': 10}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Bite', \n\
                                'Past Tense': 'bit', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': 1, \n\
                                'Damages': {'Sharp': 5000}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Claw', \n\
                                'Past Tense': 'clawed', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': -1, \n\
                                'Damages': {'Sharp': 3000}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Unique': True, 'Team': ['Snake', 'Nemea']}, \n\
                }, \n\
                { \n\
                    'Name': 'Chimera', \n\
                    'Description': 'A majestic three-headed monster. Part lion, part goat, and part serpent.', \n\
                    'Health': {'Brute': 6000, 'Sharp': 5000, 'Burn': 50000, 'Freeze': 5000, 'Tame': 10000, 'Agility': 100000}, \n\
                    'Aggressiveness':100, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Chimera-Skin', \n\
                                'Description': 'The skin shifts and fades out of focus before your eyes.', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                            'Name': 'Wear', \n\
                                            'Past Tense': 'equipped', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Agility': 10}, \n\
                                            'Effect Probabilities': {'Agility': 100}, \n\
                                            'Effectiveness': {'Agility': 100}, \n\
                                            'Attributes': {'Camo': True, 'Consumable': True, 'Self': True, 'Worn': True}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Burn', \n\
                            { \n\
                                'Name': 'Bite', \n\
                                'Past Tense': 'bit', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 90, \n\
                                'Cooldown': -2, \n\
                                'Damages': {'Sharp': 1500}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Claw', \n\
                                'Past Tense': 'clawed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 90, \n\
                                'Cooldown': -1, \n\
                                'Damages': {'Sharp': 2000, 'Agility': 100}, \n\
                                'Effect Probabilities': {'Sharp': 100, 'Agility': 90}, \n\
                                'Effectiveness': {'Sharp': 80, 'Agility': 60}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Satyr', \n\
                    'Description': 'A man with two goat legs and two goat horns.', \n\
                    'Health': {'Brute': 2000, 'Sharp': 1500, 'Burn': 1000, 'Freeze': 1500, 'Tame': 3000, 'Agility': 150}, \n\
                    'Aggressiveness':70, \n\
                    'Weapons': \n\
                        [ \n\
                            'Dagger', \n\
                            'Pan\\'s-Flute', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Kick', \n\
                            'Charge', \n\
                        ], \n\
                    'Attributes': {'Team': ['Dryad']}, \n\
                }, \n\
                { \n\
                    'Name': 'Ox-of-the-Sun', \n\
                    'Description': 'A majestic ox.', \n\
                    'Health': {'Brute': 1000, 'Sharp': 600, 'Burn': 100000, 'Freeze': 300, 'Tame': 3000, 'Agility': 10}, \n\
                    'Aggressiveness':0, \n\
                    'Weapons': \n\
                        [ \n\
                            'Apollo\\'s-Bow', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Kick', \n\
                            'Charge', \n\
                        ], \n\
                    'Attributes': {'Team': ['All'], 'Smite': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Dryad', \n\
                    'Description': 'A tree spirit with features similar to a woman.', \n\
                    'Health': {'Brute': 2500, 'Sharp': 2000, 'Burn': 3000, 'Freeze': 3000, 'Tame': 2500, 'Agility': 200}, \n\
                    'Aggressiveness':80, \n\
                    'Weapons': \n\
                        [ \n\
                            'Magic-Staff', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                        ], \n\
                    'Attributes': {'Team': ['Dryad']}, \n\
                }, \n\
                { \n\
                    'Name': 'Aeternae', \n\
                    'Description': 'Large fauna with bony bumps on its head. Its skin is leathery.', \n\
                    'Health': {'Brute': 4000, 'Sharp': 3500, 'Burn': 8000, 'Freeze': 3500, 'Tame': 6000, 'Agility': 300}, \n\
                    'Aggressiveness':90, \n\
                    'Weapons': \n\
                        [ \n\
                             { \n\
                                'Name': 'Aeternae-Skin', \n\
                                'Description': 'Exceptionally flame-resistant. No amount of heat affects it.', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                            'Name': 'Wear', \n\
                                            'Past Tense': 'equipped', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Burn': -8000, 'Agility': 10}, \n\
                                            'Effect Probabilities': {'Burn': 100, 'Agility': 100}, \n\
                                            'Effectiveness': {'Burn': 70, 'Agility': 100}, \n\
                                            'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Kick', \n\
                            { \n\
                                'Name': 'Head-Butt', \n\
                                'Past Tense': 'head-butted', \n\
                                'Choice Probability': 300, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': 2, \n\
                                'Damages': {'Brute': 2000, 'Sharp': 2000}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100}, \n\
                                'Effectiveness': {'Brute': 90, 'Sharp': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Ophiotaurus', \n\
                    'Description': 'Part bull, part serpent. It is believed that burning one grants the ability to slay gods.', \n\
                    'Health': {'Brute': 3000, 'Sharp': 2500, 'Burn': 1000, 'Freeze': 7000, 'Tame': 10000, 'Agility': 300}, \n\
                    'Aggressiveness':70, \n\
                    'Weapons': \n\
                        [ \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Kick', \n\
                            { \n\
                                'Name': 'Head-Butt', \n\
                                'Past Tense': 'head-butted', \n\
                                'Choice Probability': 300, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': 2, \n\
                                'Damages': {'Brute': 500, 'Sharp': 2000}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100}, \n\
                                'Effectiveness': {'Brute': 50, 'Sharp': 70}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Ophiotaurus': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Catoblepas', \n\
                    'Description': 'A large, buffalo-like creature. It\\'s staring at the ground.', \n\
                    'Health': {'Brute': 4000, 'Sharp': 3500, 'Burn': 3000, 'Freeze': 8000, 'Tame': 8000, 'Agility': 300}, \n\
                    'Aggressiveness':70, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Catoblepas-Fur', \n\
                                'Description': 'Exceptionally thick. No amount of cold affects it.', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                            'Name': 'Wear', \n\
                                            'Past Tense': 'equipped', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Freeze': -8000}, \n\
                                            'Effect Probabilities': {'Freeze': 100}, \n\
                                            'Effectiveness': {'Freeze': 70}, \n\
                                            'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Kick', \n\
                            { \n\
                                'Name': 'Head-Butt', \n\
                                'Past Tense': 'head-butted', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': 2, \n\
                                'Damages': {'Brute': 1000, 'Sharp': 1000}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100}, \n\
                                'Effectiveness': {'Brute': 60, 'Sharp': 60}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Stare-At', \n\
                                'Past Tense': 'looked at', \n\
                                'Choice Probability': 10, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': 5, \n\
                                'Damages': {'Toxin': 1}, \n\
                                'Effect Probabilities': {'Toxin': 100}, \n\
                                'Effectiveness': {'Toxin': 100}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Odontotyrannos', \n\
                    'Description': 'A pitch-black fauna with a horse-like head. Three dangerous horns jut from it\\'s skull. The creature exceeds the size of an elephant.', \n\
                    'Health': {'Brute': 20000, 'Sharp': 8000, 'Burn': 7000, 'Freeze': 8000, 'Tame': 20000, 'Agility': 120}, \n\
                    'Aggressiveness':70, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Tusk', \n\
                                'Description': 'A large animal tusk. Could be an effective weapon.', \n\
                                'Attacks': \n\
                                    [ \n\
                                        { \n\
                                            'Name': 'Impale', \n\
                                            'Past Tense': 'impaled', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 70, \n\
                                            'Cooldown': 1, \n\
                                            'Damages': {'Sharp': 6000}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 90}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Head-Butt', \n\
                                'Past Tense': 'head-butted', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': 3, \n\
                                'Damages': {'Brute': 6000, 'Sharp': 5000}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100}, \n\
                                'Effectiveness': {'Brute': 60, 'Sharp': 60}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Trample', \n\
                                'Past Tense': 'trampled', \n\
                                'Choice Probability': 20, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': 2, \n\
                                'Damages': {'Brute': 10000}, \n\
                                'Effect Probabilities': {'Brute': 100}, \n\
                                'Effectiveness': {'Brute': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Crocotta', \n\
                    'Description': 'It looks like a hyena--a very angry hyena.', \n\
                    'Health': {'Brute': 400, 'Sharp': 200, 'Burn': 200, 'Freeze': 300, 'Tame': 300, 'Agility': 500}, \n\
                    'Aggressiveness':100, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                  'Name': 'Crocotta-Pelt', \n\
                                  'Description': 'Rather thick and rather warm.', \n\
                                  'Attacks': \n\
                                      [ \n\
                                           { \n\
                                              'Name': 'Wear', \n\
                                              'Past Tense': 'equipped', \n\
                                              'Choice Probability': 0, \n\
                                              'Hit Probability': 100, \n\
                                              'Cooldown': 0, \n\
                                              'Damages': {'Freeze': -600, 'Agility': 8}, \n\
                                              'Effect Probabilities': {'Freeze': 100, 'Agility': 100}, \n\
                                              'Effectiveness': {'Freeze': 50, 'Agility': 100}, \n\
                                              'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                                          }, \n\
                                      ], \n\
                                  'Attributes': {'Body': True}, \n\
                              }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                          { \n\
                                'Name': 'Bite', \n\
                                'Past Tense': 'bit', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 60, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Sharp': 300}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 20}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Claw', \n\
                                'Past Tense': 'clawed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': -1, \n\
                                'Damages': {'Sharp': 400}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Cannibal': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Medusa', \n\
                    'Description': 'Best look away.', \n\
                    'Health': {'Brute': 1000, 'Sharp': 500, 'Burn': 400, 'Freeze': 500, 'Tame': 500000, 'Agility': 200}, \n\
                    'Aggressiveness': 0, \n\
                    'Weapons': \n\
                        [ \n\
                             { \n\
                                'Name': 'Medusa\\'s-Head', \n\
                                'Description': 'What are you doing!? Don\\'t look at it!', \n\
                                'Attacks': \n\
                                    [ \n\
                                        { \n\
                                            'Name': 'Petrify', \n\
                                            'Past Tense': 'petrified', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 2, \n\
                                            'Damages': {'Soul': 1}, \n\
                                            'Effect Probabilities': {'Soul': 100}, \n\
                                            'Effectiveness': {'Soul': 100}, \n\
                                            'Attributes': {'Cooldown': True}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True, 'Head': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Slash', \n\
                                { \n\
                                    'Name': 'Petrify', \n\
                                    'Past Tense': 'petrified', \n\
                                    'Choice Probability': 80, \n\
                                    'Hit Probability': 100, \n\
                                    'Cooldown': 2, \n\
                                    'Damages': {'Soul': 1}, \n\
                                    'Effect Probabilities': {'Soul': 1}, \n\
                                    'Effectiveness': {'Soul': 1}, \n\
                                    'Attributes': {'Cooldown': True}, \n\
                                }, \n\
                        ], \n\
                    'Attributes': {'Unique': True, 'Team': ['All'], 'Medusa': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Circe', \n\
                    'Description': '\\'Everyone who isn\\'t us is an enemy.\\'', \n\
                    'Health': {'Brute': 2000, 'Sharp': 1000, 'Burn': 800, 'Freeze': 1000, 'Tame': 5000, 'Agility': 200}, \n\
                    'Aggressiveness': 100, \n\
                    'Weapons': \n\
                        [ \n\
                             { \n\
                                'Name': 'Circe\\'s-Staff', \n\
                                'Description': 'An awkward staff of deepest black wood whose strange branchings and inlaid amethysts warn of power and chaos.', \n\
                                'Attacks': \n\
                                    [ \n\
                                        { \n\
                                            'Name': 'Cast', \n\
                                            'Past Tense': 'obliterated', \n\
                                            'Choice Probability': 1, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 3, \n\
                                            'Damages': {'Soul': 1}, \n\
                                            'Effect Probabilities': {'Soul': 1}, \n\
                                            'Effectiveness': {'Soul': 1}, \n\
                                            'Attributes': {'Cooldown': True}, \n\
                                        }, \n\
                                        { \n\
                                            'Name': 'Cast', \n\
                                            'Past Tense': 'stranged', \n\
                                            'Choice Probability': 5, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 3, \n\
                                            'Damages': {}, \n\
                                            'Effect Probabilities': {}, \n\
                                            'Effectiveness': {}, \n\
                                            'Attributes': {'Reverse': True, 'Cooldown': True}, \n\
                                        }, \n\
                                        { \n\
                                            'Name': 'Cast', \n\
                                            'Past Tense': 'fire-balled', \n\
                                            'Choice Probability': 5, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 3, \n\
                                            'Damages': {'Burn': 10000}, \n\
                                            'Effect Probabilities': {'Burn': 100}, \n\
                                            'Effectiveness': {'Burn': 100}, \n\
                                            'Attributes': {'Cooldown': True}, \n\
                                        }, \n\
                                        { \n\
                                            'Name': 'Cast', \n\
                                            'Past Tense': 'is summoning a demon near', \n\
                                            'Choice Probability': 5, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 3, \n\
                                            'Damages': {}, \n\
                                            'Effect Probabilities': {}, \n\
                                            'Effectiveness': {}, \n\
                                            'Attributes': {'Spawn-Demon': True, 'Cooldown': True}, \n\
                                        }, \n\
                                        { \n\
                                            'Name': 'Cast', \n\
                                            'Past Tense': 'magicked', \n\
                                            'Choice Probability': 100, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 3, \n\
                                            'Damages': {'Brute': 2000, 'Sharp': 2000, 'Burn': 1000, 'Freeze': 1000, 'Agility': 1000}, \n\
                                            'Effect Probabilities': {'Brute': 50, 'Sharp': 50, 'Burn': 30, 'Freeze': 30, 'Agility': 20}, \n\
                                            'Effectiveness': {'Brute': -50, 'Sharp': -50, 'Burn': -50, 'Freeze': -50, 'Agility': -50}, \n\
                                            'Attributes': {'Cooldown': True}, \n\
                                        }, \n\
                                        { \n\
                                            'Name': 'Cast', \n\
                                            'Past Tense': 'marked', \n\
                                            'Choice Probability': 10, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 3, \n\
                                            'Damages': {}, \n\
                                            'Effect Probabilities': {}, \n\
                                            'Effectiveness': {}, \n\
                                            'Attributes': {'Mark': True, 'Cooldown': True}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'?': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                        ], \n\
                    'Attributes': {'Unique': True, 'Team': ['All']}, \n\
                }, \n\
                { \n\
                    'Name': 'Manticore', \n\
                    'Description': 'A lion body with a human head.', \n\
                    'Health': {'Brute': 500, 'Sharp': 200, 'Burn': 300, 'Freeze': 400, 'Tame': 500, 'Agility': 400}, \n\
                    'Aggressiveness':100, \n\
                    'Weapons': \n\
                        [ \n\
                             { \n\
                                'Name': 'Tail-Spike', \n\
                                'Description': 'A strange, black, spike. Exceptionally sharp.', \n\
                                'Attacks': \n\
                                    [ \n\
                                        { \n\
                                            'Name': 'Stab', \n\
                                            'Past Tense': 'stabbed', \n\
                                            'Choice Probability': 1, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Sharp': 8000}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 1}, \n\
                                            'Attributes': {'Consumable': True}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Bite', \n\
                                'Past Tense': 'bit', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 90, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Sharp': 550}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 60}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Claw', \n\
                                'Past Tense': 'clawed', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': -1, \n\
                                'Damages': {'Sharp': 600}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Tiger', \n\
                    'Description': 'A majestic cat. Not for petting.', \n\
                    'Health': {'Brute': 500, 'Sharp': 200, 'Burn': 300, 'Freeze': 400, 'Tame': 500, 'Agility': 1000}, \n\
                    'Aggressiveness': 100, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Tiger-Claws', \n\
                                'Description': 'Deadly.', \n\
                                'Attacks': \n\
                                    [ \n\
                                        { \n\
                                            'Name': 'Slash', \n\
                                            'Past Tense': 'slashed', \n\
                                            'Choice Probability': 1, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 0, \n\
                                            'Ammo': 4, \n\
                                            'Damages': {'Sharp': 5000}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 10}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Bite', \n\
                                'Past Tense': 'bit', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 60, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Sharp': 300}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 70}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Claw', \n\
                                'Past Tense': 'clawed', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': -1, \n\
                                'Damages': {'Sharp': 400}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 70}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Nemean-Lion', \n\
                    'Description': 'A gigantic lion. Its coat has a strange sheen.', \n\
                    'Health': {'Brute': 10000000, 'Sharp': 10000000, 'Burn': 10000000, 'Freeze': 10000000, 'Toxin': 10000000, 'Focus': 10000000, 'Tame': 10000000, 'Divine': 100, 'Agility': 4000}, \n\
                    'Aggressiveness': 0, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Lion-Pelt', \n\
                                'Description': 'In a coat of gold or a coat of red, a lion still has claws.', \n\
                                'Attacks': \n\
                                    [ \n\
                                         { \n\
                                            'Name': 'Wear', \n\
                                            'Past Tense': 'equipped', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 0, \n\
                                            'Damages': {'Brute': -10000000, 'Sharp': -10000000, 'Burn': -10000000, 'Freeze': -10000000, 'Agility': 100}, \n\
                                            'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Agility': 100}, \n\
                                            'Effectiveness': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Agility': 100}, \n\
                                            'Attributes': {'Consumable': True, 'Self': True, 'Worn': True}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Lion-Claws', \n\
                                'Description': 'And mine are long and sharp, my lord, as long and sharp as yours.', \n\
                                'Attacks': \n\
                                    [ \n\
                                        { \n\
                                            'Name': 'Rend', \n\
                                            'Past Tense': 'rent', \n\
                                            'Choice Probability': 1, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': -1, \n\
                                            'Ammo': 4, \n\
                                            'Damages': {'Sharp': 10000}, \n\
                                            'Effect Probabilities': {'Sharp': 100}, \n\
                                            'Effectiveness': {'Sharp': 90}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Bite', \n\
                                'Past Tense': 'bit', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Sharp': 650}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Claw', \n\
                                'Past Tense': 'clawed', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': -1, \n\
                                'Damages': {'Sharp': 700}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Unique': True, 'Team': ['Nemea']}, \n\
                }, \n\
                { \n\
                    'Name': 'Hippogriff', \n\
                    'Description': 'It has the front of an eagle and the back of a horse.', \n\
                    'Health': {'Brute': 700, 'Sharp': 600, 'Burn': 600, 'Freeze': 700, 'Tame': 3000, 'Divine': 1000, 'Agility': 300}, \n\
                    'Aggressiveness':100, \n\
                    'Weapons': \n\
                        [ \n\
                            'Apollo\\'s-Lyre', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Rend', \n\
                            { \n\
                                'Name': 'Claw', \n\
                                'Past Tense': 'clawed', \n\
                                'Choice Probability': 50, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': -1, \n\
                                'Damages': {'Sharp': 500}, \n\
                                'Effect Probabilities': {'Sharp': 100}, \n\
                                'Effectiveness': {'Sharp': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Minotaur', \n\
                    'Description': 'A giant man-bull.', \n\
                    'Health': {'Brute': 6000, 'Sharp': 5500, 'Burn': 5000, 'Freeze': 5500, 'Tame': 10000, 'Agility': 10000}, \n\
                    'Aggressiveness':100, \n\
                    'Weapons': \n\
                        [ \n\
                            'Pandora\\'s-Box', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Charge', \n\
                                'Past Tense': 'charged at', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 60, \n\
                                'Cooldown': 2, \n\
                                'Damages': {'Sharp': 5000, 'Brute': 1000}, \n\
                                'Effect Probabilities': {'Sharp': 100, 'Brute': 90}, \n\
                                'Effectiveness': {'Sharp': 80, 'Brute': 20}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Unique': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Khalkotauroi', \n\
                    'Description': 'An intimidating, fire-breathing bull of bronze. Forged by the gods.', \n\
                    'Health': {'Brute': 40500, 'Sharp': 50000, 'Burn': 40000, 'Freeze': 30500, 'Divine': 4000, 'Tame': 100000000, 'Tame2+': 10,'Agility': 1000}, \n\
                    'Aggressiveness': 0, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Brazen-Horn', \n\
                                'Description': 'A jagged horn of bronze and adamantine. Hot to the touch.', \n\
                                'Attacks': \n\
                                    [ \n\
                                        { \n\
                                            'Name': 'Rend', \n\
                                            'Past Tense': 'rent', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': -1, \n\
                                            'Damages': {'Sharp': 8000, 'Burn': 10000}, \n\
                                            'Effect Probabilities': {'Sharp': 100, 'Burn': 90}, \n\
                                            'Effectiveness': {'Sharp': 90, 'Burn': 50}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                        { \n\
                                            'Name': 'Impale', \n\
                                            'Past Tense': 'impaled', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': 0, \n\
                                            'Ammo': 1, \n\
                                            'Damages': {'Sharp': 10000, 'Burn': 10000, 'Divine': 10000}, \n\
                                            'Effect Probabilities': {'Sharp': 100, 'Burn': 95, 'Divine': 100}, \n\
                                            'Effectiveness': {'Sharp': 100, 'Burn': 100, 'Divine': 80}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                    ], \n\
                                'Attributes': {'Body': True}, \n\
                            }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Charge', \n\
                                'Past Tense': 'charged at', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 60, \n\
                                'Cooldown': 2, \n\
                                'Damages': {'Sharp': 8000, 'Brute': 1000}, \n\
                                'Effect Probabilities': {'Sharp': 100, 'Brute': 90}, \n\
                                'Effectiveness': {'Sharp': 80, 'Brute': 20}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                            { \n\
                                'Name': 'Burn', \n\
                                'Past Tense': 'incinerated', \n\
                                'Choice Probability': 20, \n\
                                'Hit Probability': 90, \n\
                                'Cooldown': 1, \n\
                                'Ammo': 0, \n\
                                'Damages': {'Burn': 6000}, \n\
                                'Effect Probabilities': {'Burn': 100}, \n\
                                'Effectiveness': {'Burn': 100}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Unique': True, 'Team': ['Bull']}, \n\
                }, \n\
                { \n\
                    'Name': 'Centaur', \n\
                    'Description': 'Half man, half horse. He seems nice.', \n\
                    'Health': {'Brute': 2000, 'Sharp': 1500, 'Burn': 1000, 'Freeze': 1200, 'Tame': 2000, 'Agility': 400}, \n\
                    'Aggressiveness': 20, \n\
                    'Weapons': \n\
                        [ \n\
                            'Akontia', \n\
                            'Toxa', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                        ], \n\
                    'Attributes': {'Team': ['Centaur']}, \n\
                }, \n\
                { \n\
                    'Name': 'Cyprian-Centaur', \n\
                    'Description': 'Half man, half horse. Bull horns. He seems ok.', \n\
                    'Health': {'Brute': 2500, 'Sharp': 2000, 'Burn': 1500, 'Freeze': 1700, 'Tame': 2500, 'Agility': 450}, \n\
                    'Aggressiveness':40, \n\
                    'Weapons': \n\
                        [ \n\
                            'Akontia', \n\
                            'Doru', \n\
                            'Toxa', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Ram', \n\
                                'Past Tense': 'rammed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': 2, \n\
                                'Damages': {'Sharp': 700, 'Brute': 800}, \n\
                                'Effect Probabilities': {'Sharp': 100, 'Brute': 90}, \n\
                                'Effectiveness': {'Sharp': 50, 'Brute': 30}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Team': ['Centaur']}, \n\
                }, \n\
                { \n\
                    'Name': 'Nessus', \n\
                    'Description': 'Half man, half horse. Bull horns. He is angry.', \n\
                    'Health': {'Brute': 3000, 'Sharp': 2500, 'Burn': 2000, 'Freeze': 2500, 'Tame': 5000, 'Agility': 400}, \n\
                    'Aggressiveness':100, \n\
                    'Weapons': \n\
                        [ \n\
                            'Akontia', \n\
                            'Shirt-of-Nessus', \n\
                            'Doru', \n\
                            'Toxa', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Ram', \n\
                                'Past Tense': 'rammed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 70, \n\
                                'Cooldown': 2, \n\
                                'Damages': {'Sharp': 800, 'Brute': 900, 'Agility': 50}, \n\
                                'Effect Probabilities': {'Sharp': 100, 'Brute': 90, 'Agility': 10}, \n\
                                'Effectiveness': {'Sharp': 50, 'Brute': 30, 'Agility': 1}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Unique': True, 'Team': ['Centaur']}, \n\
                }, \n\
                { \n\
                    'Name': 'Giant', \n\
                    'Description': 'A very large man--a giant, even.', \n\
                    'Health': {'Brute': 6000, 'Sharp': 5000, 'Burn': 4000, 'Freeze': 5000, 'Tame': 7000, 'Agility': 150}, \n\
                    'Aggressiveness':100, \n\
                    'Weapons': \n\
                        [ \n\
                            'Giant-Club', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Smash', \n\
                        ], \n\
                    'Attributes': {'Team': ['Giant'], 'Names': ['Asterius', 'Athos', 'Alcyoneus', 'Almops', 'Azeus', 'Chthonius', 'Diomedes-of-Thrace', 'Echion', 'Eurytus', 'Enceladus', 'Mimas', 'Pallas', 'Polybotes', 'Thoon', 'Tityos']}, \n\
                }, \n\
                { \n\
                    'Name': 'Cyclops', \n\
                    'Description': 'A very large man--a giant, even ...except with just the one eye.', \n\
                    'Health': {'Brute': 6500, 'Sharp': 5500, 'Burn': 4500, 'Freeze': 5500, 'Tame': 7500, 'Agility': 130}, \n\
                    'Aggressiveness':100, \n\
                    'Weapons': \n\
                        [ \n\
                            'Giant-Sword', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            'Smash', \n\
                        ], \n\
                    'Attributes': {'Team': ['Giant']}, \n\
                }, \n\
                { \n\
                    'Name': 'Talos', \n\
                    'Description': 'A large, bronze automaton made to resemble a giant man. A protector.', \n\
                    'Health': {'Brute': 10000, 'Sharp': 10000, 'Burn': 5000, 'Freeze': 10000, 'Tame': 8000, 'Agility': 100}, \n\
                    'Aggressiveness': 100, \n\
                    'Weapons': \n\
                        [ \n\
                            'Boulder', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Pulverize', \n\
                                'Past Tense': 'pulverized', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': 3, \n\
                                'Damages': {'Brute': 10000}, \n\
                                'Effect Probabilities': {'Brute': 100}, \n\
                                'Effectiveness': {'Brute': 70}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Unique': True, 'Team': ['You']}, \n\
                }, \n\
                { \n\
                    'Name': 'Hecatoncheir', \n\
                    'Description': 'A very large giant with (upon a quick count) exactly 100 arms.', \n\
                    'Health': {'Brute': 16000, 'Sharp': 15000, 'Burn': 14000, 'Freeze': 15000, 'Tame': 17000, 'Agility': 200}, \n\
                    'Aggressiveness':100, \n\
                    'Weapons': \n\
                        [ \n\
                            'Giant-Club', \n\
                            'Panacea', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                           { \n\
                                'Name': 'Smash', \n\
                                'Past Tense': 'smashed', \n\
                                'Choice Probability': 1000, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Brute': 5000}, \n\
                                'Effect Probabilities': {'Brute': 100}, \n\
                                'Effectiveness': {'Brute': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                           { \n\
                                'Name': 'Pulverize', \n\
                                'Past Tense': 'pulverized', \n\
                                'Choice Probability': 1, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': -100, \n\
                                'Damages': {'Brute': 5000}, \n\
                                'Effect Probabilities': {'Brute': 100}, \n\
                                'Effectiveness': {'Brute': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Unique': True, 'Team': ['Giant']}, \n\
                }, \n\
                { \n\
                    'Name': 'Phoenix', \n\
                    'Description': 'A majestic, flaming bird. Ashes to ashes, bird to bird.', \n\
                    'Health': {'Brute': 6000, 'Sharp': 5000, 'Burn': 1000000, 'Freeze': 500, 'Tame': 10000, 'Agility': 300}, \n\
                    'Aggressiveness':70, \n\
                    'Weapons': \n\
                        [ \n\
                            'Myrrh-Egg', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                           { \n\
                                'Name': 'Burn', \n\
                                'Past Tense': 'burned', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': 0, \n\
                                'Damages': {'Burn': 3000}, \n\
                                'Effect Probabilities': {'Burn': 100}, \n\
                                'Effectiveness': {'Burn': 90}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                           { \n\
                                'Name': 'Claw', \n\
                                'Past Tense': 'clawed', \n\
                                'Choice Probability': 80, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': -1, \n\
                                'Damages': {'Burn': 1000, 'Sharp': 1000}, \n\
                                'Effect Probabilities': {'Burn': 100, 'Sharp': 100}, \n\
                                'Effectiveness': {'Burn': 90, 'Sharp': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Unique': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Zeus', \n\
                    'Description': 'The King of Gods.', \n\
                    'Health': {'Brute': 1000000, 'Sharp': 1000000, 'Burn': 1000000, 'Freeze': 1000000, 'Tame': 1000000, 'Soul': 1000000, 'Toxin': 1000000, 'Focus': 10000000, 'Divine': 10000, 'Agility': 10}, \n\
                    'Aggressiveness':0, \n\
                    'Weapons': \n\
                        [ \n\
                            'Zeus\\'s-Thunderbolt', \n\
                            'Ichor', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                        ], \n\
                    'Attributes': {'Unique': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Aphrodite', \n\
                    'Description': 'Goddess of Love.', \n\
                    'Health': {'Brute': 1000000, 'Sharp': 1000000, 'Burn': 1000000, 'Freeze': 1000000, 'Tame': 1000000, 'Soul': 1000000, 'Toxin': 1000000, 'Focus': 10000000, 'Divine': 5000, 'Agility': 10}, \n\
                    'Aggressiveness':0, \n\
                    'Weapons': \n\
                        [ \n\
                            'Aphrodite\\'s-Magic-Girdle', \n\
                            'Ichor', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                             { \n\
                                'Name': 'Heal', \n\
                                'Past Tense': 'healed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 100, \n\
                                'Damages': {'Brute': -4000, 'Sharp': -4000, 'Burn': -4000, 'Freeze': -4000}, \n\
                                'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100}, \n\
                                'Effectiveness': {'Brute': 80, 'Sharp': 80, 'Burn': 90, 'Freeze': 80}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Unique': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Ares', \n\
                    'Description': 'God of War.', \n\
                    'Health': {'Brute': 1000000, 'Sharp': 1000000, 'Burn': 1000000, 'Freeze': 1000000, 'Tame': 1000000, 'Soul': 1000000, 'Toxin': 1000000, 'Focus': 10000000, 'Divine': 5000, 'Agility': 10}, \n\
                    'Aggressiveness':50, \n\
                    'Weapons': \n\
                        [ \n\
                            'Spear-of-Ares', \n\
                            'Ichor', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                        ], \n\
                    'Attributes': {'Unique': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Artemis', \n\
                    'Description': 'Goddess of the Hunt.', \n\
                    'Health': {'Brute': 1000000, 'Sharp': 1000000, 'Burn': 1000000, 'Freeze': 1000000, 'Tame': 1000000, 'Soul': 1000000, 'Toxin': 1000000, 'Focus': 10000000, 'Divine': 5000, 'Agility': 10}, \n\
                    'Aggressiveness':0, \n\
                    'Weapons': \n\
                        [ \n\
                            'Artemis\\'s-Bow', \n\
                            'Ichor', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                        ], \n\
                    'Attributes': {'Unique': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Hermes', \n\
                    'Description': 'God of Travel.', \n\
                    'Health': {'Brute': 1000000, 'Sharp': 1000000, 'Burn': 1000000, 'Freeze': 1000000, 'Tame': 1000000, 'Soul': 1000000, 'Toxin': 1000000, 'Focus': 10000000, 'Divine': 5000, 'Agility': 10}, \n\
                    'Aggressiveness':0, \n\
                    'Weapons': \n\
                        [ \n\
                            'Talaria', \n\
                            'Caduceus', \n\
                            'Ichor', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                        ], \n\
                    'Attributes': {'Unique': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Poseidon', \n\
                    'Description': 'God of the Sea.', \n\
                    'Health': {'Brute': 1000000, 'Sharp': 1000000, 'Burn': 1000000, 'Freeze': 1000000, 'Tame': 1000000, 'Soul': 1000000, 'Toxin': 1000000, 'Focus': 10000000, 'Divine': 5000, 'Agility': 10}, \n\
                    'Aggressiveness':0, \n\
                    'Weapons': \n\
                        [ \n\
                            'Poseidon\\'s-Trident', \n\
                            'Ichor', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                        ], \n\
                    'Attributes': {'Unique': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Athena', \n\
                    'Description': 'Goddess of Wisdom.', \n\
                    'Health': {'Brute': 1000000, 'Sharp': 1000000, 'Burn': 1000000, 'Freeze': 1000000, 'Tame': 1000000, 'Soul': 1000000, 'Toxin': 1000000, 'Focus': 10000000, 'Divine': 5000, 'Agility': 10}, \n\
                    'Aggressiveness':0, \n\
                    'Weapons': \n\
                        [ \n\
                            'Athena\\'s-Bridle', \n\
                            'Compendium', \n\
                            'Ichor', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Concentrate-On', \n\
                                'Past Tense': 'Hurt', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 80, \n\
                                'Cooldown': 3, \n\
                                'Damages': {'Divine': 10000}, \n\
                                'Effect Probabilities': {'Divine': 100}, \n\
                                'Effectiveness': {'Divine': 5}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Unique': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Hephaestus', \n\
                    'Description': 'God of Metal-Working.', \n\
                    'Health': {'Brute': 1000000, 'Sharp': 1000000, 'Burn': 1000000, 'Freeze': 1000000, 'Tame': 1000000, 'Soul': 1000000, 'Toxin': 1000000, 'Focus': 10000000, 'Divine': 5000, 'Agility': 10}, \n\
                    'Aggressiveness':0, \n\
                    'Weapons': \n\
                        [ \n\
                            'Hephaestus\\'s-Labrys', \n\
                            'Hammer-of-Hephaestus', \n\
                            'Adamantine-Plough', \n\
                            'Ichor', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                        ], \n\
                    'Attributes': {'Unique': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Hades', \n\
                    'Description': 'God of the Underworld.', \n\
                    'Health': {'Brute': 1000000, 'Sharp': 1000000, 'Burn': 1000000, 'Freeze': 1000000, 'Tame': 1000000, 'Soul': 1000000, 'Toxin': 1000000, 'Focus': 10000000, 'Divine': 8000, 'Agility': 10}, \n\
                    'Aggressiveness':100, \n\
                    'Weapons': \n\
                        [ \n\
                            'Hades\\'s-Bident', \n\
                            'Helm-of-Darkness', \n\
                            'Pandora\\'s-Box', \n\
                            'Ichor', \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                        ], \n\
                    'Attributes': {'Unique': True}, \n\
                }, \n\
                { \n\
                    'Name': 'Typhon', \n\
                    'Description': 'The Father of Monsters. A giant so tall his head scrapes the stars.', \n\
                    'Health': {'Brute': 100000000, 'Sharp': 100000000, 'Burn': 100000000, 'Freeze': 100000000, 'Tame': 100000000, 'Soul': 100000000, 'Toxin': 100000000, 'Focus': 10000000, 'Life': 100000000, 'Divine': 100000000, 'Agility': 100000}, \n\
                    'Aggressiveness':100, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Laurel-Wreath', \n\
                                'Description': 'You did it. You killed Typhon. You are a god.', \n\
                                'Attacks': \n\
                                    [ \n\
                                        { \n\
                                            'Name': 'End', \n\
                                            'Past Tense': 'ended', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': -100, \n\
                                            'Damages': {'End': 1}, \n\
                                            'Effect Probabilities': {'End': 100}, \n\
                                            'Effectiveness': {'End': 100}, \n\
                                            'Attributes': {}, \n\
                                        }, \n\
                                        { \n\
                                            'Name': 'Begin', \n\
                                            'Past Tense': 'began', \n\
                                            'Choice Probability': 0, \n\
                                            'Hit Probability': 100, \n\
                                            'Cooldown': -100, \n\
                                            'Damages': {'Brute': -1000000, 'Sharp': -1000000, 'Burn': -1000000, 'Freeze': -1000000, 'Divine': -1000000, 'Toxin': -1000000, 'Soul': -1000000, 'Life': -1000000, 'Focus': -1000000}, \n\
                                            'Effect Probabilities': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Divine': 100, 'Toxin': 100, 'Soul': 100, 'Life': 100, 'Focus': 100}, \n\
                                            'Effectiveness': {'Brute': 100, 'Sharp': 100, 'Burn': 100, 'Freeze': 100, 'Divine': 100, 'Toxin': 100, 'Soul': 100, 'Life': 100, 'Focus': 100}, \n\
                                            'Attributes': {}, \n\
                                       }, \n\
                                   ], \n\
                                'Attributes': {'Body': True}, \n\
                             }, \n\
                        ], \n\
                    'Attacks': \n\
                        [ \n\
                            { \n\
                                'Name': 'Gib', \n\
                                'Past Tense': 'gibbed', \n\
                                'Choice Probability': 100, \n\
                                'Hit Probability': 100, \n\
                                'Cooldown': 100, \n\
                                'Damages': {'Brute': 1000000}, \n\
                                'Effect Probabilities': {'Brute': 100}, \n\
                                'Effectiveness': {'Brute': 100}, \n\
                                'Attributes': {}, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Unique': True}, \n\
                }, \n\
            ], \n\
        'location objects': \n\
            [ \n\
                { \n\
                    'Name': 'Rock', \n\
                    'Probability': 5, \n\
                    'Fraction': 3, \n\
                    'Max': 0, \n\
                }, \n\
                { \n\
                    'Name': 'Mead', \n\
                    'Probability': 100, \n\
                    'Fraction': 5, \n\
                    'Max': 5, \n\
                }, \n\
                { \n\
                    'Name': 'Cooked-Meal', \n\
                    'Probability': 100, \n\
                    'Fraction': 3, \n\
                    'Max': 5, \n\
                }, \n\
                { \n\
                   'Name': 'Teumessian-Fox', \n\
                   'Probability': 1, \n\
                   'Fraction': 0, \n\
                   'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Torch', \n\
                    'Probability': 30, \n\
                    'Fraction': 3, \n\
                    'Max': 0, \n\
                }, \n\
                { \n\
                    'Name': 'Dagger', \n\
                    'Probability': 90, \n\
                    'Fraction': 3, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Bell-Cuirass', \n\
                    'Probability': 10, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Linothorax', \n\
                    'Probability': 15, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Corinthian-Helmet', \n\
                    'Probability': 10, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Chitoniskos', \n\
                    'Probability': 15, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Phrygian-Helmet', \n\
                    'Probability': 12, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Chalcidian-Helmet', \n\
                    'Probability': 14, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Boeotian-Helmet', \n\
                    'Probability': 16, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Muscle-Cuirass', \n\
                    'Probability': 20, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Xiphos', \n\
                    'Probability': 40, \n\
                    'Fraction': 6, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Staff', \n\
                    'Probability': 30, \n\
                    'Fraction': 6, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Harpe', \n\
                    'Probability': 30, \n\
                    'Fraction': 6, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Bident', \n\
                    'Probability': 30, \n\
                    'Fraction': 6, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Journal', \n\
                    'Probability': 0, \n\
                    'Fraction': 6, \n\
                    'Max': 2, \n\
                }, \n\
                { \n\
                    'Name': 'Ambrosia', \n\
                    'Probability': 10, \n\
                    'Fraction': 5, \n\
                    'Max': 0, \n\
                }, \n\
                { \n\
                    'Name': 'Panacea', \n\
                    'Probability': 10, \n\
                    'Fraction': 5, \n\
                    'Max': 0, \n\
                }, \n\
                { \n\
                    'Name': 'Toxa', \n\
                    'Probability': 5, \n\
                    'Fraction': 6, \n\
                    'Max': 0, \n\
                }, \n\
                { \n\
                    'Name': 'Akontia', \n\
                    'Probability': 5, \n\
                    'Fraction': 2, \n\
                    'Max': 0, \n\
                }, \n\
                { \n\
                    'Name': 'Horn-of-Plenty', \n\
                    'Probability': 1, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Rod-of-Asclepius', \n\
                    'Probability': 2, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Archimedes\\'s-Mirror', \n\
                    'Probability': 5, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Triton\\'s-Conch-Shell', \n\
                    'Probability': 5, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Kryo', \n\
                    'Probability': 7, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Prometheus\\'s-Chains', \n\
                    'Probability': 1, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Thread-of-Ariadne', \n\
                    'Probability': 10, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Staff-of-Travel', \n\
                    'Probability': 10, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Kibisis', \n\
                    'Probability': 1.5, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Daedalus\\'s-Wings', \n\
                    'Probability': 3, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Water-of-The-River-Styx', \n\
                    'Probability': .5, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Baetylus', \n\
                    'Probability': .5, \n\
                    'Fraction': 2, \n\
                    'Max': 3, \n\
                }, \n\
                { \n\
                    'Name': 'Eros\\'s-Bow', \n\
                    'Probability': .3, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Pheme\\'s-Trumpet', \n\
                    'Probability': 1, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Bag-of-Wind', \n\
                    'Probability': 10, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Omphalos', \n\
                    'Probability': 1.5, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Emerald-Tablet', \n\
                    'Probability': 2, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Compendium', \n\
                    'Probability': 0, \n\
                    'Fraction': 0, \n\
                    'Max': 0, \n\
                }, \n\
                { \n\
                    'Name': 'Wooden-Cow', \n\
                    'Probability': 1, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Brazen-Shield', \n\
                    'Probability': 2, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Rota-Fortunae', \n\
                    'Probability': 1, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Hellebore', \n\
                    'Probability': 4, \n\
                    'Fraction': 90, \n\
                    'Max': 3, \n\
                }, \n\
                { \n\
                    'Name': 'Poppy', \n\
                    'Probability': 15, \n\
                    'Fraction': 90, \n\
                    'Max': 3, \n\
                }, \n\
                { \n\
                    'Name': 'Narcissus-Flower', \n\
                    'Probability': 10, \n\
                    'Fraction': 90, \n\
                    'Max': 3, \n\
                }, \n\
                { \n\
                    'Name': 'Peony', \n\
                    'Probability': 20, \n\
                    'Fraction': 90, \n\
                    'Max': 3, \n\
                }, \n\
                { \n\
                    'Name': 'Lotus', \n\
                    'Probability': 15, \n\
                    'Fraction': 90, \n\
                    'Max': 3, \n\
                }, \n\
                { \n\
                    'Name': 'Hemlock', \n\
                    'Probability': 5, \n\
                    'Fraction': 90, \n\
                    'Max': 3, \n\
                }, \n\
                { \n\
                    'Name': 'Narthex-Flower', \n\
                    'Probability': 7, \n\
                    'Fraction': 90, \n\
                    'Max': 3, \n\
                }, \n\
                { \n\
                    'Name': 'Amarantos-Flower', \n\
                    'Probability': 2, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Manna-Flower', \n\
                    'Probability': 1, \n\
                    'Fraction': 90, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Ambrosia-Flower', \n\
                    'Probability': 2, \n\
                    'Fraction': 90, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Miasma-Flower', \n\
                    'Probability': .2, \n\
                    'Fraction': 90, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Panacea-Flower', \n\
                    'Probability': .2, \n\
                    'Fraction': 90, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Herb-of-Kheiron', \n\
                    'Probability': 10, \n\
                    'Fraction': 10, \n\
                    'Max': 3, \n\
                }, \n\
                { \n\
                    'Name': 'Herb-of-Kirke', \n\
                    'Probability': 10, \n\
                    'Fraction': 10, \n\
                    'Max': 3, \n\
                }, \n\
                { \n\
                    'Name': 'Herb-of-Asklepios', \n\
                    'Probability': .3, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Wolf\\'s-Bane', \n\
                    'Probability': 20, \n\
                    'Fraction': 10, \n\
                    'Max': 3, \n\
                }, \n\
                { \n\
                    'Name': 'Hyacinth', \n\
                    'Probability': 20, \n\
                    'Fraction': 10, \n\
                    'Max': 3, \n\
                }, \n\
                { \n\
                    'Name': 'Cerastes-Horns', \n\
                    'Probability': 10, \n\
                    'Fraction': 10, \n\
                    'Max': 3, \n\
                }, \n\
                { \n\
                    'Name': 'Giant-Sword', \n\
                    'Probability': 100, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Daedalus\\'s-Hand-Canon', \n\
                    'Probability': .05, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Moly', \n\
                    'Probability': 15, \n\
                    'Fraction': 2, \n\
                    'Max': 0, \n\
                }, \n\
                { \n\
                    'Name': 'Sunflower', \n\
                    'Probability': 6, \n\
                    'Fraction': 2, \n\
                    'Max': 0, \n\
                }, \n\
                { \n\
                    'Name': 'Peacock\\'s-Feather', \n\
                    'Probability': 100, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
                { \n\
                    'Name': 'Orpheus\\'s-Lyre', \n\
                    'Probability': .8, \n\
                    'Fraction': 0, \n\
                    'Max': 1, \n\
                }, \n\
            ], \n\
        'locations': \n\
            [ \n\
                { \n\
                    'Name': 'Acherusia', \n\
                    'Description': 'It\\'s a bog! He\\'s led us into a swamp!', \n\
                    'Probability': 10, \n\
                    'Treasure': {'Max': 1, 'Min': 0, 'Probability': 1}, \n\
                    'Weapons': \n\
                        [ \n\
                            'Rock', \n\
                        ], \n\
                    'NPCs': \n\
                        [ \n\
                             { \n\
                                'Name': 'Serpent', \n\
                                'Probability': 80, \n\
                                'Fraction': 1.5, \n\
                                'Max': 5, \n\
                            }, \n\
                            'Teumessian-Fox', \n\
                             { \n\
                                'Name': 'Giant-Serpent', \n\
                                'Probability': 40, \n\
                                'Fraction': 2, \n\
                                'Max': 5, \n\
                            }, \n\
                             { \n\
                                'Name': 'Stymphalian-Bird', \n\
                                'Probability': 25, \n\
                                'Fraction': .02, \n\
                                'Max': 3, \n\
                            }, \n\
                             { \n\
                                'Name': 'Arae', \n\
                                'Probability': 2, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Erinyes', \n\
                                'Probability': .5, \n\
                                'Fraction': .005, \n\
                                'Max': 3, \n\
                            }, \n\
                             { \n\
                                'Name': 'Triple-Bodied-Daemon', \n\
                                'Probability': .5, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Ceuthonymus', \n\
                                'Probability': 1, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Eurynomos', \n\
                                'Probability': 1, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Island', \n\
                    'Description': 'An Island', \n\
                    'Probability': 30, \n\
                    'Treasure': {'Max': 1, 'Min': 0, 'Probability': 5}, \n\
                    'Weapons': \n\
                        [ \n\
                            'Rock', \n\
                            'Herb-of-Kheiron', \n\
                            'Herb-of-Kirke', \n\
                            'Herb-of-Asklepios', \n\
                            'Narcissus-Flower', \n\
                            'Poppy', \n\
                            'Peony', \n\
                            'Lotus', \n\
                            'Hemlock', \n\
                            'Sunflower', \n\
                            'Narthex-Flower', \n\
                            'Amarantos-Flower', \n\
                            'Manna-Flower', \n\
                            'Wolf\\'s-Bane', \n\
                            'Cerastes-Horns', \n\
                            'Hyacinth', \n\
                            'Triton\\'s-Conch-Shell', \n\
                        ], \n\
                    'NPCs': \n\
                        [ \n\
                             { \n\
                                'Name': 'Serpent', \n\
                                'Probability': 80, \n\
                                'Fraction': 1.5, \n\
                                'Max': 3, \n\
                            }, \n\
                             { \n\
                               'Name': 'Traveler', \n\
                               'Probability': 6, \n\
                               'Fraction': 1.5, \n\
                               'Max': 3, \n\
                           }, \n\
                            { \n\
                               'Name': 'Mercenary', \n\
                               'Probability': 4, \n\
                               'Fraction': 1.5, \n\
                               'Max': 1, \n\
                           }, \n\
                            { \n\
                                'Name': 'Story-Teller', \n\
                                'Probability': 5, \n\
                                'Fraction': 3, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Siren', \n\
                                'Probability': 2, \n\
                                'Fraction': 1.5, \n\
                                'Max': 3, \n\
                            }, \n\
                             { \n\
                                'Name': 'Pyrausta', \n\
                                'Probability': .5, \n\
                                'Fraction': 1.5, \n\
                                'Max': 3, \n\
                            }, \n\
                           'Teumessian-Fox', \n\
                             { \n\
                                'Name': 'Talos', \n\
                                'Probability': 2, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Ox-of-the-Sun', \n\
                                'Probability': 5, \n\
                                'Fraction': .23, \n\
                                'Max': 3, \n\
                            }, \n\
                             { \n\
                                'Name': 'Medusa', \n\
                                'Probability': 1, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Circe', \n\
                                'Probability': .5, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Pygmy', \n\
                                'Probability': 10, \n\
                                'Fraction': .2, \n\
                                'Max': 3, \n\
                            }, \n\
                            { \n\
                               'Name': 'Clazomenae-Boar', \n\
                               'Probability': 1, \n\
                               'Fraction': 5, \n\
                               'Max': 1, \n\
                            }, \n\
                            { \n\
                                'Name': 'Boar', \n\
                                'Probability': 60, \n\
                                'Fraction': 2, \n\
                                'Max': 0, \n\
                            }, \n\
                            { \n\
                                'Name': 'Gigantic-Tortoise', \n\
                                'Probability': 6, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Giant-Tortoise', \n\
                                'Probability': 10, \n\
                                'Fraction': 10, \n\
                                'Max': 0, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Names': ['Aegilips', 'Corfu', 'Ithaca', 'Krocylea', 'Neritum', 'Ortygia', 'Panchaea', 'Same']}, \n\
                }, \n\
                { \n\
                    'Name': 'Nemea', \n\
                    'Description': 'An arid island with familiar yet strange creatures.', \n\
                    'Probability': 2, \n\
                    'Treasure': {'Max': 4, 'Min': 1, 'Probability': 90}, \n\
                    'Weapons': \n\
                        [ \n\
                            'Rock', \n\
                            'Herb-of-Kheiron', \n\
                            'Peony', \n\
                            'Herb-of-Asklepios', \n\
                            'Manna-Flower', \n\
                            'Narthex-Flower', \n\
                            'Hyacinth', \n\
                            'Amarantos-Flower', \n\
                        ], \n\
                    'NPCs': \n\
                        [ \n\
                             { \n\
                                'Name': 'Serpent', \n\
                                'Probability': 80, \n\
                                'Fraction': 1.5, \n\
                                'Max': 3, \n\
                            }, \n\
                            'Teumessian-Fox', \n\
                             { \n\
                                'Name': 'Nymph', \n\
                                'Probability': 90, \n\
                                'Fraction': 10, \n\
                                'Max': 3, \n\
                            }, \n\
                             { \n\
                                'Name': 'Nemean-Lion', \n\
                                'Probability': 30, \n\
                                'Fraction': 0, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Nemean-Dragon', \n\
                                'Probability': 10, \n\
                                'Fraction': 0, \n\
                                'Max': 1, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Sacred-Grove', \n\
                    'Description': 'A luscious island of exotic creatures.', \n\
                    'Probability': .5, \n\
                    'Treasure': {'Max': 4, 'Min': 1, 'Probability': 95}, \n\
                    'Weapons': \n\
                        [ \n\
                            'Rock', \n\
                            'Ambrosia', \n\
                            'Herb-of-Kheiron', \n\
                            'Peony', \n\
                            'Herb-of-Asklepios', \n\
                            'Manna-Flower', \n\
                            'Narthex-Flower', \n\
                            'Hyacinth', \n\
                            'Amarantos-Flower', \n\
                            'Ambrosia-Flower', \n\
                            { \n\
                                'Name': 'Omphalos', \n\
                                'Probability': 100, \n\
                                'Fraction': 20, \n\
                                'Max': 0, \n\
                            }, \n\
                        ], \n\
                    'NPCs': \n\
                        [ \n\
                             { \n\
                                'Name': 'Serpent', \n\
                                'Probability': 80, \n\
                                'Fraction': 1.5, \n\
                                'Max': 3, \n\
                            }, \n\
                            'Teumessian-Fox', \n\
                             { \n\
                                'Name': 'Nymph', \n\
                                'Probability': 90, \n\
                                'Fraction': 10, \n\
                                'Max': 3, \n\
                            }, \n\
                             { \n\
                                'Name': 'Khalkotauroi', \n\
                                'Probability': 100, \n\
                                'Fraction': .05, \n\
                                'Max': 2, \n\
                            }, \n\
                             { \n\
                                'Name': 'Colchian-Dragon', \n\
                                'Probability': 100, \n\
                                'Fraction': 0, \n\
                                'Max': 1, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Town', \n\
                    'Description': 'A nice place to rest.', \n\
                    'Probability': 10, \n\
                    'Treasure': {'Max': 0, 'Min': 0, 'Probability': 0}, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Dagger-Bag', \n\
                                'Probability': 80, \n\
                                'Fraction': 5, \n\
                                'Max': 2, \n\
                            }, \n\
                            { \n\
                                'Name': 'Staff', \n\
                                'Probability': 40, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                            { \n\
                                'Name': 'Food-Platter', \n\
                                'Probability': 70, \n\
                                'Fraction': 5, \n\
                                'Max': 2, \n\
                            }, \n\
                            { \n\
                                'Name': 'Xiphos', \n\
                                'Probability': 20, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                            { \n\
                                'Name': 'Bident', \n\
                                'Probability': 10, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                            { \n\
                                'Name': 'Harpe', \n\
                                'Probability': 10, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                            { \n\
                                'Name': 'Staff-of-Travel', \n\
                                'Probability': .5, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                            { \n\
                                'Name': 'Chitoniskos', \n\
                                'Probability': 30, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                            { \n\
                                'Name': 'Toxa', \n\
                                'Probability': 20, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                            { \n\
                                'Name': 'Akontia', \n\
                                'Probability': 20, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                            { \n\
                                'Name': 'Bell-Cuirass', \n\
                                'Probability': 5, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                            { \n\
                                'Name': 'Linothorax', \n\
                                'Probability': 15, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                            { \n\
                                'Name': 'Corinthian-Helmet', \n\
                                'Probability': 15, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                            { \n\
                                'Name': 'Phrygian-Helmet', \n\
                                'Probability': 15, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                            { \n\
                                'Name': 'Chalcidian-Helmet', \n\
                                'Probability': 15, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                            { \n\
                                'Name': 'Boeotian-Helmet', \n\
                                'Probability': 15, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                            { \n\
                                'Name': 'Muscle-Cuirass', \n\
                                'Probability': 15, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                            { \n\
                                'Name': 'Torch', \n\
                                'Probability': 15, \n\
                                'Fraction': 5, \n\
                                'Max': 2, \n\
                            }, \n\
                        ], \n\
                    'NPCs': \n\
                        [ \n\
                        ], \n\
                    'Attributes': {'Names': ['Aulis', 'Ismara', 'Libethra', 'Lyrnessus', 'Megara', 'Mycenae', 'Pedasus', 'Percote', 'Pimpleia', 'Scheria', 'Sparta', 'Tenea', 'Trachis', 'Troy', 'Zeleia']}, \n\
                }, \n\
                { \n\
                    'Name': 'Mountain', \n\
                    'Description': 'A looming peak of rock.', \n\
                    'Probability': 40, \n\
                    'Treasure': {'Max': 1, 'Min': 0, 'Probability': 2}, \n\
                    'Weapons': \n\
                        [ \n\
                            'Rock', \n\
                            'Hellebore', \n\
                            'Narthex-Flower', \n\
                            'Amarantos-Flower', \n\
                            'Panacea-Flower', \n\
                            'Miasma-Flower', \n\
                            'Ambrosia-Flower', \n\
                            'Wolf\\'s-Bane', \n\
                            'Poppy', \n\
                            'Hyacinth', \n\
                            'Prometheus\\'s-Chains', \n\
                        ], \n\
                    'NPCs': \n\
                        [ \n\
                             { \n\
                                'Name': 'Boar', \n\
                                'Probability': 40, \n\
                                'Fraction': 1.5, \n\
                                'Max': 2, \n\
                            }, \n\
                            { \n\
                               'Name': 'Traveler', \n\
                               'Probability': 6, \n\
                               'Fraction': 1.5, \n\
                               'Max': 3, \n\
                           }, \n\
                            { \n\
                               'Name': 'Mercenary', \n\
                               'Probability': 4, \n\
                               'Fraction': 1.5, \n\
                               'Max': 1, \n\
                           }, \n\
                            { \n\
                                'Name': 'Story-Teller', \n\
                                'Probability': 5, \n\
                                'Fraction': 3, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Werewolf', \n\
                                'Probability': 1, \n\
                                'Fraction': 0, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Amalthea', \n\
                                'Probability': .1, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                            'Teumessian-Fox', \n\
                             { \n\
                                'Name': 'Laelaps', \n\
                                'Probability': 1, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Calydonian-Boar', \n\
                                'Probability': 4, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Highway-Man', \n\
                                'Probability': 30, \n\
                                'Fraction': 3, \n\
                                'Max': 2, \n\
                            }, \n\
                             { \n\
                                'Name': 'Wolf', \n\
                                'Probability': 10, \n\
                                'Fraction': 10, \n\
                                'Max': 3, \n\
                            }, \n\
                             { \n\
                                'Name': 'Harpy', \n\
                                'Probability': 10, \n\
                                'Fraction': 5, \n\
                                'Max': 2, \n\
                            }, \n\
                             { \n\
                                'Name': 'Aethon', \n\
                                'Probability': 5, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Griffin', \n\
                                'Probability': 4, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Pegasus', \n\
                                'Probability': 5, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Dragon', \n\
                                'Probability': 7, \n\
                                'Fraction': 10, \n\
                                'Max': 0, \n\
                            }, \n\
                             { \n\
                                'Name': 'Cynocephali', \n\
                                'Probability': 10, \n\
                                'Fraction': .5, \n\
                                'Max': 3, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Names': ['Besparmak Mountains', 'Dikti', 'Mount Agdistis', 'Mount Triphyle']}, \n\
                }, \n\
                { \n\
                    'Name': 'Jungle', \n\
                    'Description': 'A Jungle: a vast network of tangling overgrowth and tall trees.', \n\
                    'Probability': 35, \n\
                    'Treasure': {'Max': 1, 'Min': 0, 'Probability': 2}, \n\
                    'Weapons': \n\
                        [ \n\
                            'Rock', \n\
                            'Herb-of-Kheiron', \n\
                            'Poppy', \n\
                            'Peony', \n\
                            'Herb-of-Kirke', \n\
                            'Herb-of-Asklepios', \n\
                        ], \n\
                    'NPCs': \n\
                        [ \n\
                             { \n\
                                'Name': 'Tiger', \n\
                                'Probability': 10, \n\
                                'Fraction': 10, \n\
                                'Max': 2, \n\
                            }, \n\
                            { \n\
                               'Name': 'Traveler', \n\
                               'Probability': 6, \n\
                               'Fraction': 1.5, \n\
                               'Max': 3, \n\
                           }, \n\
                            { \n\
                               'Name': 'Mercenary', \n\
                               'Probability': 4, \n\
                               'Fraction': 1.5, \n\
                               'Max': 1, \n\
                           }, \n\
                            'Teumessian-Fox', \n\
                             { \n\
                                'Name': 'Giant-Serpent', \n\
                                'Probability': 20, \n\
                                'Fraction': 5, \n\
                                'Max': 2, \n\
                            }, \n\
                             { \n\
                                'Name': 'Serpent', \n\
                                'Probability': 40, \n\
                                'Fraction': 5, \n\
                                'Max': 3, \n\
                            }, \n\
                             { \n\
                                'Name': 'Ornithes-Areioi', \n\
                                'Probability': 30, \n\
                                'Fraction': 1.5, \n\
                                'Max': 3, \n\
                            }, \n\
                             { \n\
                                'Name': 'Amazon', \n\
                                'Probability': 30, \n\
                                'Fraction': .05, \n\
                                'Max': 3, \n\
                            }, \n\
                             { \n\
                                'Name': 'Chimera', \n\
                                'Probability': 5, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Names': ['Lycia', 'Libya', 'Thermodon']}, \n\
                }, \n\
                { \n\
                    'Name': 'Cave', \n\
                    'Description': 'A cavernous hole in the ground.', \n\
                    'Probability': 20, \n\
                    'Treasure': {'Max': 2, 'Min': 0, 'Probability': 7}, \n\
                    'Weapons': \n\
                        [ \n\
                            'Rock', \n\
                            'Archimedes\\'s-Mirror', \n\
                            'Thread-of-Ariadne', \n\
                            'Journal', \n\
                            'Staff', \n\
                            'Kryo', \n\
                            'Rod-of-Asclepius', \n\
                        ], \n\
                    'NPCs': \n\
                        [ \n\
                             { \n\
                                'Name': 'Arachne', \n\
                                'Probability': 5, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                            { \n\
                               'Name': 'Traveler', \n\
                               'Probability': 5, \n\
                               'Fraction': 1.5, \n\
                               'Max': 3, \n\
                           }, \n\
                            { \n\
                               'Name': 'Mercenary', \n\
                               'Probability': 3, \n\
                               'Fraction': 1.5, \n\
                               'Max': 1, \n\
                           }, \n\
                            { \n\
                                'Name': 'Story-Teller', \n\
                                'Probability': 5, \n\
                                'Fraction': 3, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Vampire', \n\
                                'Probability': 2, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Bear', \n\
                                'Probability': 30, \n\
                                'Fraction': 10, \n\
                                'Max': 2, \n\
                            }, \n\
                             { \n\
                                'Name': 'Graeae', \n\
                                'Probability': 5, \n\
                                'Fraction': .05, \n\
                                'Max': 3, \n\
                            }, \n\
                             { \n\
                                'Name': 'Dragon', \n\
                                'Probability': 7, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Wolf', \n\
                                'Probability': 10, \n\
                                'Fraction': 2, \n\
                                'Max': 0, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Path-to-Canterbury', \n\
                    'Description': '\\'Then do folk long to go on pilgrimage, And palmers to go seeking out strange strands, To distant shrines well known in sundry lands.\\'', \n\
                    'Probability': 10, \n\
                    'Treasure': {'Max': 1, 'Min': 0, 'Probability': 2}, \n\
                    'Weapons': \n\
                        [ \n\
                            'Rock', \n\
                        ], \n\
                    'NPCs': \n\
                        [ \n\
                             { \n\
                                'Name': 'Story-Teller', \n\
                                'Probability': 100, \n\
                                'Fraction': 50, \n\
                                'Max': 1, \n\
                            }, \n\
                            { \n\
                               'Name': 'Traveler', \n\
                               'Probability': 10, \n\
                               'Fraction': 1.5, \n\
                               'Max': 3, \n\
                           }, \n\
                            { \n\
                               'Name': 'Mercenary', \n\
                               'Probability': 5, \n\
                               'Fraction': 1.5, \n\
                               'Max': 1, \n\
                           }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Labyrinth', \n\
                    'Description': 'A twisting maze as terrifying as it is incomprehensible.', \n\
                    'Probability': 2, \n\
                    'Treasure': {'Max': 1, 'Min': 0, 'Probability': 30}, \n\
                    'Weapons': \n\
                        [ \n\
                            'Daedalus\\'s-Hand-Canon', \n\
                            'Daedalus\\'s-Wings', \n\
                            'Pheme\\'s-Trumpet', \n\
                            'Eros\\'s-Bow', \n\
                            'Brazen-Shield', \n\
                            'Journal', \n\
                            'Emerald-Tablet', \n\
                            'Staff-of-Travel', \n\
                            'Orpheus\\'s-Lyre', \n\
                            'Kibisis', \n\
                            'Baetylus', \n\
                            'Omphalos', \n\
                            'Water-of-The-River-Styx', \n\
                            'Wooden-Cow', \n\
                        ], \n\
                    'NPCs': \n\
                        [ \n\
                             { \n\
                                'Name': 'Minotaur', \n\
                                'Probability': 10, \n\
                                'Fraction': 0, \n\
                                'Max': 1, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Forest', \n\
                    'Description': 'A mystical woodlands.', \n\
                    'Probability': 50, \n\
                    'Treasure': {'Max': 1, 'Min': 0, 'Probability': 1}, \n\
                    'Weapons': \n\
                        [ \n\
                            'Rock', \n\
                            'Rota-Fortunae', \n\
                            'Hemlock', \n\
                            'Herb-of-Kheiron', \n\
                            'Poppy', \n\
                            'Peony', \n\
                            'Sunflower', \n\
                            'Narcissus-Flower', \n\
                            'Herb-of-Asklepios', \n\
                            'Manna-Flower', \n\
                            'Narthex-Flower', \n\
                            'Herb-of-Kirke', \n\
                            'Wolf\\'s-Bane', \n\
                            'Hyacinth', \n\
                        ], \n\
                    'NPCs': \n\
                        [ \n\
                             { \n\
                                'Name': 'Satyr', \n\
                                'Probability': 60, \n\
                                'Fraction': 3, \n\
                                'Max': 0, \n\
                            }, \n\
                            { \n\
                               'Name': 'Traveler', \n\
                               'Probability': 10, \n\
                               'Fraction': 1.5, \n\
                               'Max': 3, \n\
                           }, \n\
                            { \n\
                               'Name': 'Mercenary', \n\
                               'Probability': 5, \n\
                               'Fraction': 1.5, \n\
                               'Max': 1, \n\
                           }, \n\
                             { \n\
                                'Name': 'Story-Teller', \n\
                                'Probability': 5, \n\
                                'Fraction': 3, \n\
                                'Max': 1, \n\
                            }, \n\
                            'Teumessian-Fox', \n\
                             { \n\
                                'Name': 'Cyprian-Centaur', \n\
                                'Probability': 10, \n\
                                'Fraction': 1.2, \n\
                                'Max': 0, \n\
                            }, \n\
                             { \n\
                                'Name': 'Nessus', \n\
                                'Probability': 1, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Centaur', \n\
                                'Probability': 20, \n\
                                'Fraction': 1.2, \n\
                                'Max': 0, \n\
                            }, \n\
                             { \n\
                                'Name': 'Highway-Man', \n\
                                'Probability': 60, \n\
                                'Fraction': 3, \n\
                                'Max': 0, \n\
                            }, \n\
                             { \n\
                                'Name': 'Bear', \n\
                                'Probability': 30, \n\
                                'Fraction': 4, \n\
                                'Max': 2, \n\
                            }, \n\
                             { \n\
                                'Name': 'Wolf', \n\
                                'Probability': 10, \n\
                                'Fraction': 3, \n\
                                'Max': 3, \n\
                            }, \n\
                             { \n\
                                'Name': 'Dryad', \n\
                                'Probability': 50, \n\
                                'Fraction': 3, \n\
                                'Max': 0, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Northern-Plains', \n\
                    'Description': 'A vast, open plain of odd and terrifying creatures.', \n\
                    'Probability': 15, \n\
                    'Treasure': {'Max': 1, 'Min': 0, 'Probability': 5}, \n\
                    'Weapons': \n\
                        [ \n\
                            'Rock', \n\
                            'Ambrosia-Flower', \n\
                            'Panacea-Flower', \n\
                            'Miasma-Flower', \n\
                            'Horn-of-Plenty', \n\
                            'Moly', \n\
                            'Hemlock', \n\
                        ], \n\
                    'NPCs': \n\
                        [ \n\
                             { \n\
                                'Name': 'Aeternae', \n\
                                'Probability': 20, \n\
                                'Fraction': 10, \n\
                                'Max': 2, \n\
                            }, \n\
                            { \n\
                               'Name': 'Traveler', \n\
                               'Probability': 7, \n\
                               'Fraction': 1.5, \n\
                               'Max': 3, \n\
                           }, \n\
                            { \n\
                               'Name': 'Mercenary', \n\
                               'Probability': 5, \n\
                               'Fraction': 1.5, \n\
                               'Max': 1, \n\
                           }, \n\
                             { \n\
                                'Name': 'Unicorn', \n\
                                'Probability': .5, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                            'Teumessian-Fox', \n\
                             { \n\
                                'Name': 'Ophiotaurus', \n\
                                'Probability': 10, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Catoblepas', \n\
                                'Probability': 10, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Odontotyrannos', \n\
                                'Probability': 5, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Crocotta', \n\
                                'Probability': 70, \n\
                                'Fraction': 10, \n\
                                'Max': 5, \n\
                            }, \n\
                             { \n\
                                'Name': 'Manticore', \n\
                                'Probability': 20, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Hippogriff', \n\
                                'Probability': 5, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Phlegra', \n\
                    'Description': 'A volcanic wasteland stretching as far as the eye can see.', \n\
                    'Probability': 10, \n\
                    'Treasure': {'Max': 2, 'Min': 0, 'Probability': 6}, \n\
                    'Weapons': \n\
                        [ \n\
                            'Rock', \n\
                            'Ambrosia-Flower', \n\
                            'Panacea-Flower', \n\
                            'Miasma-Flower', \n\
                        ], \n\
                    'NPCs': \n\
                        [ \n\
                             { \n\
                                'Name': 'Giant', \n\
                                'Probability': 70, \n\
                                'Fraction': 3, \n\
                                'Max': 5, \n\
                            }, \n\
                            'Teumessian-Fox', \n\
                             { \n\
                                'Name': 'Cyclops', \n\
                                'Probability': 50, \n\
                                'Fraction': 5, \n\
                                'Max': 2, \n\
                            }, \n\
                            { \n\
                                'Name': 'Hecatoncheir', \n\
                                'Probability': 3, \n\
                                'Fraction': 3, \n\
                                'Max': 3, \n\
                            }, \n\
                            { \n\
                                'Name': 'Phoenix', \n\
                                'Probability': 5, \n\
                                'Fraction': 5, \n\
                                'Max': 1, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Herot', \n\
                    'Description': '\\'The foremost of halls under heaven.\\'', \n\
                    'Probability': 4, \n\
                    'Treasure': {'Max': 2, 'Min': 0, 'Probability': 20}, \n\
                    'Weapons': \n\
                        [ \n\
                            'Mead', \n\
                            'Cooked-Meal', \n\
                        ], \n\
                    'NPCs': \n\
                        [ \n\
                             { \n\
                                'Name': 'Grendel', \n\
                                'Probability': 0, \n\
                                'Fraction': 0, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'King-Hrothgar', \n\
                                'Probability': 100, \n\
                                'Fraction': 0, \n\
                                'Max': 1, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Strange-Cavern', \n\
                    'Description': '\\'... some strange cavern where the fangs of the depths could never reach.\\'', \n\
                    'Probability': 3, \n\
                    'Treasure': {'Max': 1, 'Min': 0, 'Probability': 10}, \n\
                    'Weapons': \n\
                        [ \n\
                            'Ambrosia', \n\
                            'Journal', \n\
                            'Giant-Sword', \n\
                        ], \n\
                    'NPCs': \n\
                        [ \n\
                             { \n\
                                'Name': 'Grendel\\'s-Mother', \n\
                                'Probability': 100, \n\
                                'Fraction': 0, \n\
                                'Max': 1, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Treasure-Hall', \n\
                    'Description': '\\'A hall beneath the ground, a mound covered with earth close to the breakers, the dashing of the waves. It was filled within with treasures and ornaments.\\'', \n\
                    'Probability': 2, \n\
                    'Treasure': {'Max': 15, 'Min': 5, 'Probability': 100}, \n\
                    'Weapons': \n\
                        [ \n\
                            'Peacock\\'s-Feather', \n\
                        ], \n\
                    'NPCs': \n\
                        [ \n\
                             { \n\
                                'Name': 'Earth-Dragon', \n\
                                'Probability': 100, \n\
                                'Fraction': 0, \n\
                                'Max': 1, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {}, \n\
                }, \n\
                { \n\
                    'Name': 'Olympus', \n\
                    'Description': 'Atop this mountain the Gods are said to dwell.', \n\
                    'Probability': 0, \n\
                    'Treasure': {'Max': 1, 'Min': 0, 'Probability': 10}, \n\
                    'Weapons': \n\
                        [ \n\
                            { \n\
                                'Name': 'Ambrosia', \n\
                                'Probability': 30, \n\
                                'Fraction': 5, \n\
                                'Max': 0, \n\
                            }, \n\
                            { \n\
                                'Name': 'Ambrosia', \n\
                                'Probability': 30, \n\
                                'Fraction': 5, \n\
                                'Max': 0, \n\
                            }, \n\
                            { \n\
                                'Name': 'Ambrosia', \n\
                                'Probability': 30, \n\
                                'Fraction': 5, \n\
                                'Max': 0, \n\
                            }, \n\
                            { \n\
                                'Name': 'Ambrosia', \n\
                                'Probability': 30, \n\
                                'Fraction': 5, \n\
                                'Max': 0, \n\
                            }, \n\
                            { \n\
                                'Name': 'Ambrosia', \n\
                                'Probability': 30, \n\
                                'Fraction': 5, \n\
                                'Max': 0, \n\
                            }, \n\
                            { \n\
                                'Name': 'Ambrosia', \n\
                                'Probability': 30, \n\
                                'Fraction': 5, \n\
                                'Max': 0, \n\
                            }, \n\
                            'Bag-of-Wind', \n\
                        ], \n\
                    'NPCs': \n\
                        [ \n\
                             { \n\
                                'Name': 'Zeus', \n\
                                'Probability': 100, \n\
                                'Fraction': 0, \n\
                                'Max': 1, \n\
                            }, \n\
                             { \n\
                                'Name': 'Hermes', \n\
                                'Probability': 100, \n\
                                'Fraction': 0, \n\
                                'Max': 2, \n\
                            }, \n\
                             { \n\
                                'Name': 'Aphrodite', \n\
                                'Probability': 100, \n\
                                'Fraction': 0, \n\
                                'Max': 2, \n\
                            }, \n\
                             { \n\
                                'Name': 'Athena', \n\
                                'Probability': 100, \n\
                                'Fraction': 0, \n\
                                'Max': 2, \n\
                            }, \n\
                             { \n\
                                'Name': 'Ares', \n\
                                'Probability': 100, \n\
                                'Fraction': 0, \n\
                                'Max': 2, \n\
                            }, \n\
                             { \n\
                                'Name': 'Artemis', \n\
                                'Probability': 100, \n\
                                'Fraction': 0, \n\
                                'Max': 2, \n\
                            }, \n\
                             { \n\
                                'Name': 'Hephaestus', \n\
                                'Probability': 100, \n\
                                'Fraction': 0, \n\
                                'Max': 2, \n\
                            }, \n\
                             { \n\
                                'Name': 'Poseidon', \n\
                                'Probability': 100, \n\
                                'Fraction': 0, \n\
                                'Max': 2, \n\
                            }, \n\
                             { \n\
                                'Name': 'Hades', \n\
                                'Probability': 100, \n\
                                'Fraction': 0, \n\
                                'Max': 2, \n\
                            }, \n\
                        ], \n\
                    'Attributes': {'Boss': True}, \n\
                }, \n\
            ], \n\
        'starting_health': \n\
            { \n\
                'Brute': 3000, \n\
                'Sharp': 2000, \n\
                'Burn': 1000, \n\
                'Freeze': 1500, \n\
                'Divine': 1000, \n\
                'Agility': 400, \n\
            }, \n\
        'starting_attacks': \n\
            [ \n\
                'Punch', \n\
                'Tame', \n\
            ], \n\
        'starting_weapons': \n\
            [ \n\
                'Dagger', \n\
                'Treasure', \n\
            ], \n\
    }"
# TODO: Olympus is war zone of infinite gods and their duplicates

# TODO: Figure out why thread ammo is universal to all thread
# TODO: Only allowed to pay story tellers once

# TODO: DONE DONE DONE Make thread one use. Teles to laby. Laby is now a system. Leaving location within just regens the room. give 1/20 chance of escaping laby.
# TODO: ^Same with olympus. (Eventually, same with underworld)

# TODO: You team
# TODO: if don't have tame health, can't be tamed
# TODO: Individual story tellers are unique (don't come back after death)
# TODO: Spawn-Demon summons demon after 3 moves.
# TODO: Mark causes all creatures 100% aggro on target.
# TODO: Reverse attribute inverses all damages done to you
# TODO: Styx-Death attribute kills player and gives message: You could not withstand the pull of the dead.
# TODO: Attributes: Styx-Brute, Styx-Sharp, Styx-Burn, Styx-Freeze, Styx-Soul, Styx-Life, Styx-Toxin, Styx-Focus, Styx-Divine, Styx-Mind cause attack to immediately reduce respective health to 1.
# TODO: Werewolf attribute causes victim to (after 10 turns) be shown the message: "You feel yourself transforming!" and gain 1000 agility. Also gain werewolf's attacks (as if tamed it). You now randomly transform in and out of werewolf form, causing you to gain and lose these perks. Kill a werewolf to be cured.
# TODO: Vampire attribute causes victim to (after 10 turns) be shown the message: "You feel yourself transforming!" and divine damage now is reversed.
# TODO: Unicorn attribute gives total invincibility for 10 turns *
# TODO: ? attribute causes weapon to choose randomly between its attacks when fired *
# TODO: Sack attribute causes user to not take petrify damage when picking up medusas head
# TODO: trumpet attribute forces a creature to wander in. The rarer the creature, the more likely to wander.
# TODO: Mead attribute = damages given by item are temporary (restore after 10 moves). you deal 1.2x more Brute and sharp damage
# TODO: AOE Attribute
# TODO: Worn attribute displays used item in inventory as being worn
# TODO: enrage attribute causes creature to do double damage *
# TODO: Flower text color should be green or something (also rock text color)

# New Excessive Things
# TODO: More expensive items in towns (Made cheaper with charisma). Alternatively, charisma unlocks rarer items in towns
# TODO: Hades death boss battle (In death, tele to underworld. Roam around avoiding demons and monsters until find Hades. Allow for discovery of boatman who can be paid with rare item to respawn.
# TODO: Create a main health bar. Odd healths are essentially shields which, when depleted, begin damaging main health bar. (Poison plants would do general health damage, not divine.)

tutorials = \
    "{ \n\
        'Windows/Layout': \n\
            [ \n\
                'The large box this text is in is the Events Box. All events, prompts, and your responses will be displayed in here.', \n\
                'The long box at the bottom of the screen is the Input Box. Everything you type will be displayed in that box. In most cases, your typing is constrained to the choices displayed in the Objects and Actions Boxes.', \n\
                'The Objects box is the third box down on the right side of the screen. All objects that you can interact with are displayed there. Pressing \\'Tab\\' cycles through the available choices. \\'Shift\\'+\\'Tab\\ cycles backwards (Not 100% reliable).', \n\
                'The Actions box is the second box down on the right side of the screen. All actions that are available are displayed there. Pressing \\'Tab\\' cycles through the available choices.', \n\
                'The second box down on the left is the path box. It displays the path to the object you are currently interacting with. If you wish to go backwards through the path, press \\'Backspace\\' while nothing is typed in the input box.', \n\
                'The first box on the right is the Tooltips Box. It displays extra information text viewable by hovering the cursor over highlighted words.', \n\
            ], \n\
        'Controls': \n\
            [ \n\
                'You can click words on the screen to interact with them.' \n\
                'When given a choice between actions and/or objects, your typing is limited to the choices shown in their respective boxes. Pressing \\'Tab\\' cycles through choices that match anything currently entered in the Input Box. You can start a word in the input box and press tab to complete it. Press \\'Enter\\' to use whatever object or action you\\'ve selected.', \n\
                'Go backwards in your Path (Shown in the Path tab) by backspacing or using \\'CTRL\\'+\\'Backspace\\' (faster). Or by clicking on words in the path (fastest).', \n\
                'You can enter the Attacks tab to equip an attack. To use the attack, enter the Surroundings tab and select the creature you want to attack.', \n\
                'The game Auto-Saves on exit. To Load an old game save, choose \\'Load\\' as opposed to \\'New\\' after skipping the tutorial. Then just type the name of the previous save and hit Enter.' \n\
            ], \n\
        'Gameplay': \n\
            [ \n\
                'As you play, you enter random locations with various creatures and objects shown in the Surroundings tab.', \n\
                'You can attempt to flee a location (success rate of fleeing is based on your agility and the agility of creatures attacking you) at any time from the Surroundings tab. You can pick up items in the surroundings tab by selecting them.', \n\
                'IMPORTANT CONCEPT: if you have selected an enemy, the Objects tab will display the items they have equipped. Do not confuse these items with items in your surroundings. These items are only accessible by killing the enemy in question, which will then drop them.', \n\
                'This is a survival game, there is no way to win. The goal is to survive for as long as you can and find cool weapons and creatures (If you somehow manage to kill a god, I\\'d count that as a win in my book. Also, if you manage to kill a god I want to hear the story).', \n\
                'FUNDAMENTAL CONCEPT: You and other creatures have various types of health (Such as Brute, Sharp, Burn, Freeze, Divine, et cetera). To be killed (or to kill something else) any one of those health types must reach zero.', \n\
                'Tame health is special in that if it reaches zero, you gain the ability to use the defeated creature\\'s attacks. In a sense, you have tamed the creature and it now fights with you.', \n\
                'Hover the cursor over creatures to display their health stats in the tooltips box. Hover the cursor over \\'Stats\\' in the Objects box to view your health.', \n\
            ], \n\
        'Attack-Stats': \n\
            [ \n\
                'IMPORTANT (Kinda): If you or a creature has damage dealt to it in a health category not listed in said creature\\'s stats, the damage will insta-kill the creature (with some exceptions [generally these exceptions have \\'+\\' in the name.]). For example, if a creature hurts you with \\'Toxic\\' damage, you will die instantly, as you do not have Toxic health listed in your stats.', \n\
                'When viewing a weapon\\'s tooltip, its Hit Probability for any specific attack refers to the percent chance that the attack in question will hit the selected creature. Some weapons never miss (Hit Probability: 100), others rarely hit.', \n\
                'Listed under the Hit Probability, an attack\\'s Cooldown refers to the number of times the attack can be used before enemies can attack again. A Cooldown of zero means that every time you use the attack, the enemies fighting you will be able to attack back. A Cooldown of 1 means that after using the attack, you must use a different attack or perform some other action before being able to use the attack again, and during this time your enemies will be able to attack you once. A Cooldown of -1 means you can attack twice before being attacked back. It\\'s important to realize that many enemies also use attacks with cooldowns, so if an enemy has a cooldown of 1 and you have a cooldown of 0, you\\'ll be able to attack twice before it can attack again.', \n\
                'Under the Cooldown, an attack\\'s Current Cooldown refers to the number of actions you have to perform before being able to use the attack again. If the Current Cooldown is greater than zero, you can not use the attack. Attacks with a current cooldown greater than zero display in red.', \n\
                'Depending on the attack, the Ammo stat may be listed under the Current Cooldown stat. If an attack has Ammo, that number signifies the number of times you can use the attack. There is no way to replenish Ammo.', \n\
                'Listed next, the max damage(s) dealt by the attack is(are) displayed for one or many various health categories.', \n\
                'The Probability listed to the right of the damage is the percent chance of the attack dealing that type of damage.', \n\
                'The Effectiveness (listed to the very right) determines the likely hood of the attack dealing higher amounts of damage. If, for instance, the max damage (that\\'s the first number) is 100 and the Effectiveness is 80, the attack is capable of dealing between 80% of 100 and 100 damage in its category. The higher the Effectiveness, the closer to 100% of the max damage the attack will do.', \n\
                'Viewing the Tooltip of a creature displays the creature\\'s attacks and the attack stats for each. It also shows the probability of the creature choosing an individual attack. ', \n\
            ], \n\
        'Credits': \n\
            [ \n\
                'Created by Graham and Reece Mathews for Mrs. Abker\\'s AP Literature Greek Project. Oct. 2017. Made mostly in less than a week.', \n\
                'Beowulf and Canterbury Tales (as well as treasure, new creatures/weapons, clicking, hotkeys, monsters attacking monsters, agility, plants, and much more) content added for Mrs. Abker\\'s AP Literature Renaissance Project. Dec. 2017. Added entirely in, like, a week.', \n\
                'If you have suggestions (especially suggestions regarding the balancing of attacks), questions, or would like to report a bug, email grahammathews3.14@gmail.com or mathewsreece@gmail.com depending on your preference in twin. We want all the suggestions. Give them.', \n\
                'And just for the record, it is theoretically possible to kill every creature (Including Typhon!). You just have to get good.', \n\
            ], \n\
    }"


def check(string):
    """Check a config string for mismatched brackets"""
    openers = "([{"
    closers = ")]}"
    stack = []
    ind = 0
    new_string = ""
    for char in string:
        new_string += char
        if char in openers:
            stack.append([char, new_string])
        elif char in closers:
            if len(stack) > 0:
                if stack[-1][0] in openers:
                    if openers.index(stack[-1][0]) != closers.index(char):
                        print("Latest Opener: " + stack[-1][0], "Given closer: " + char, "\n", "Text up to opener: " + stack[-1][1], "\n", "Text up to closer: " + new_string)
                        raise Exception("Previous opener not closed")
                    else:
                        stack.pop()
        if len(new_string) > 300:
            new_string = new_string[1:]
        ind += 1
    for obj in stack:
        print("Unclosed openers: ")
        print("Opener: ", obj[0], "Text up to opener: ", obj[1])


check(game_objects)
