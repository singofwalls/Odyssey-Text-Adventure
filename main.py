"""Initializes word game"""
import time
import threading

import pygame
from core.display import TextBox, Text
from core.user_input import TypingManager

from core.configs import get_value, change_config

# Initialize Pygame
pygame.init()

# Pull values from configs
fps = get_value("display", "fps")
resolution = get_value("display", "resolution")

border_color = get_value("customization", "border_color")
border_size = get_value("customization", "border_size")

mouse_hotkeys = get_value("mouse_hotkeys")
keyboard_hotkeys = get_value("keyboard_hotkeys")
alt_hold_time = get_value("input", "alt_hold_time")

display = pygame.display.set_mode(resolution, pygame.RESIZABLE)
pygame.display.set_caption("The Odyssey+")
pygame_clock = pygame.time.Clock()

status_color = get_value("customization", "status_color")
dead_color = get_value("game_customization", "dead_color")
number_color = get_value("customization", "number_color")
prompt_color = get_value("customization", "prompt_color")
input_color = get_value("customization", "input_color")
background_color = get_value("customization", "background_color")

default_font = get_value("display", "default_font")
default_font_size = get_value("display", "default_font_size")
default_color = get_value("display", "default_color")

textbox_updates = {}

temporary_box_starts = {}

user_input = None

return_pressed = False

actions = []
objects = []

choices_cycle = []
current_choice_num = -1

path = []

TEXTBOX_LOCK = threading.Lock()

running = True

caption = None

waiting = False

pressed_hotkeys = []
hotkey_enabled = True
hotkeys_locked = False
was_hotkey_enabled = False
alt_hold = 0

dead = False


class Game(threading.Thread):
    """Gameplay takes place here."""

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        """Run the game thread"""
        from game import start
        start(get_input, update_textbox, set_choices, mark_temporary,
              clear_temporary, is_running, set_caption, check_hotkeys,
              disable_hotkeys, enable_hotkeys, set_dead)


def set_dead():
    global dead
    dead = True


def check_hotkeys():
    """Returns all hotkeys that have been pressed"""
    global pressed_hotkeys
    targets = []
    for hotkey in pressed_hotkeys:
        if hotkey[0] == "keyboard":
            targets.append(keyboard_hotkeys[hotkey[1]])
        elif hotkey[0] == "mouse":
            targets.append(mouse_hotkeys[hotkey[1]])
        else:
            raise Exception("Add new button medium")
    pressed_hotkeys = []
    return targets


def disable_hotkeys():
    global hotkey_enabled, hotkeys_locked, was_hotkey_enabled
    was_hotkey_enabled = hotkey_enabled
    hotkey_enabled = False
    hotkeys_locked = True


def enable_hotkeys():
    global hotkey_enabled, hotkeys_locked
    if was_hotkey_enabled:
        hotkey_enabled = True
    hotkeys_locked = False


def set_caption(_caption):
    global caption
    caption = _caption


def is_running():
    """Returns whether main thread has finished"""
    global running
    return running


def get_input(prompt=None, _path=None,
              allow_path_change=True):
    """Sets the prompt and waits for input.

    :type prompt: None | list[Text] | str
    :type _path: None | list[GameObject] | list[GameAction]
    :type allow_path_change: bool
    """
    global path, waiting

    if not isinstance(prompt, type(None)):
        if type(prompt) == str:
            text_list = [Text(prompt, color=prompt_color,
                              new_line=True)]
        elif type(prompt) == list:
            text_list = prompt
        else:
            raise Exception("Must be None, str, or list[Text]")
        update_textbox("events", text_list)

    path = _path[:]
    _user_input = check_input()
    waiting = True
    while isinstance(_user_input, type(None)):
        time.sleep(.01)
        if len(path) != len(_path) and allow_path_change:
            # Backspace pressed. Path changed
            return None, len(path) - 1
        if not is_running():
            return None, None
        _user_input = check_input()
        hotkeys = check_hotkeys()
        if len(hotkeys) > 0:
            key = hotkeys[-1]
            return key, "HOTKEY"
    waiting = False
    return _user_input, len(path) - 1


def check_input():
    """Returns the current user input and sets back to None if not already.

    :rtype: str
    """
    global user_input
    _text = user_input
    if not isinstance(_text, type(None)):
        user_input = None
    return _text


def set_choices(_objects, _actions):
    """Sets the objects and actions choices and guides input"""
    global objects, actions

    objects = _objects
    actions = _actions


def match_choices():
    """Confines user input to options in objects and actions"""
    global current_input_string

    options = []
    if len(objects) > 0 or len(actions) > 0:
        while True:
            for _action in actions:
                if _action.get_text_string().lower().strip().startswith(
                        current_input_string.lower()):
                    options.append(_action)
            for _object in objects:
                if _object.get_text_string().lower().strip().startswith(
                        current_input_string.lower()):
                    options.append(_object)

            if len(options) < 1:
                current_input_string = current_input_string[:-1]
            else:
                break

    return options


def check_choices():
    """Checks if string matches one choice"""
    global choices_cycle, current_choice_num

    options = match_choices()
    for option in options:
        if option not in choices_cycle:
            choices_cycle.append(option)
    for option in options:
        if current_input_string.lower() == option.get_text_string().lower(

        ).strip():
            return option.get_text_string().strip()

    # Does not match any specific choice
    choices_cycle = options
    current_choice_num = -1
    if len(options) < 1 and len(actions) < 1:
        return current_input_string
    return None


def move_choices(forward, _typing_manager):
    """Moves though choices in given direction

    :type forward: bool
    :type _typing_manager: TypingManager
    """
    global current_choice_num, current_input_string

    if forward:
        current_choice_num += 1
        if current_choice_num > len(choices_cycle) - 1:
            current_choice_num = 0
    else:
        current_choice_num -= 1
        if current_choice_num < 0:
            current_choice_num = len(choices_cycle) - 1

    current_input_string = choices_cycle[
        current_choice_num].get_text_string().strip()
    _typing_manager.set_text(current_input_string)


def next_choice(_typing_manager):
    """Cycles input string through choices_cycle

    :type _typing_manager: TypingManager
    """
    global current_choice_num, current_input_string

    if len(choices_cycle) > 0:
        old_string = current_input_string
        move_choices(True, _typing_manager)
        if old_string == current_input_string:
            move_choices(True, _typing_manager)


def previous_choice(_typing_manager):
    """Cycles input string backwards through choices_cycle

    :type _typing_manager: TypingManager
    """
    global current_choice_num, current_input_string

    if len(choices_cycle) > 0:
        old_string = current_input_string
        move_choices(False, _typing_manager)
        if old_string == current_input_string:
            move_choices(False, _typing_manager)


def mark_temporary(_box="events"):
    """Marks the start of temporary text"""
    while len(textbox_updates[_box]) > 0:
        time.sleep(.01)  # Wait for box to finish updating
    TEXTBOX_LOCK.acquire()
    temporary_box_starts[_box] = len(text_boxes[_box].get_text_list())
    TEXTBOX_LOCK.release()


def clear_temporary():
    """Clears text that is temporary"""
    TEXTBOX_LOCK.acquire()
    for _box in temporary_box_starts:
        if not isinstance(temporary_box_starts[_box], type(None)):
            text_boxes[_box].set_text_list(text_boxes[_box].get_text_list()[
                                           :temporary_box_starts[_box]])
            text_boxes[_box].wrap()
            temporary_box_starts[_box] = None
    TEXTBOX_LOCK.release()


def alt_held():
    """Get's whether alt is held"""
    if alt_hold > 0:
        if (time.time() * 1000) - alt_hold > alt_hold_time:
            return True
    return False


def get_key_press():
    global quit_running, display, resolution
    close = False
    while not close:
        for __event in pygame.event.get():
            if __event.type == pygame.KEYDOWN:
                close = True
            elif __event.type == pygame.MOUSEBUTTONDOWN:
                close = True
            elif __event.type == pygame.VIDEORESIZE:
                display = pygame.display.set_mode(
                    __event.dict["size"],
                    pygame.RESIZABLE)
                resolution = __event.dict["size"]

            # Screen closed
            elif __event.type == pygame.QUIT:
                quit_running = True
                close = True
                break


def update_textbox(_box, text, clear=False):
    """Updates events textbox with new event.

    :type _box: str
    :type text: list[Text] | str
    :type clear: bool

    :param _box: Must be 'events', 'objects', or 'actions'
    :param text: list of text to update box with
    :param clear: Overwrites the box if true.
    """
    if type(text) == str:
        text_list = [Text(text, new_line=True)]
    elif type(text) == list:
        text_list = text
    else:
        raise Exception("Must be None, str, or list[Text]")
    textbox_updates[_box].append([text_list, clear])


# Declare textboxes  # TODO: Add to config
bounds = [(0, 0, .55, .80), (0, .90, .55, 1), (.55, 0, 1, .65),
          (.55, .65, 1, .75),
          (.55, .75, 1, 1), (0, .80, .55, .90)]
text_box_names = ["events", "input", "tooltips", "actions", "objects", "path"]
text_boxes = {}
index = 0
TEXTBOX_LOCK.acquire()
for box in text_box_names:
    textbox_updates[box] = []
    temporary_box_starts[box] = None
    text_boxes[box] = TextBox(box, bounds[index], "", border_color=border_color,
                              border_size=border_size)
    # Action and objects boxes are justified
    if box == "actions" or box == "objects":
        text_boxes[box].set_alignment("justified")
        text_boxes[box].set_pure_justified()
    index += 1
TEXTBOX_LOCK.release()

# Declare typing manager
typing_manager = TypingManager(False)

# Initialize Game
game = Game()
game.start()

deleted_char = False

# Begin game loop
quit_running = False

first = True

while True:
    display.fill(background_color)

    if not first:
        color = dead_color
        if waiting:
            color = prompt_color

        rad = 5
        box = text_boxes["input"]
        pygame.draw.circle(display, color, [int(box.get_x()) - rad * 2,
                                            int(box.get_y()) + rad * 2], rad)

        color = dead_color
        if hotkey_enabled:
            color = prompt_color
        if alt_hold:
            color = number_color
        rad = 5
        box = text_boxes["input"]
        pygame.draw.circle(display, color, [
            int(box.get_x()) - rad * 2, int(box.get_y(True)) - rad * 2], rad)

    first = False

    if not isinstance(caption, type(None)):
        pygame.display.set_caption(caption)
        caption = None

    # Update all textboxes
    TEXTBOX_LOCK.acquire()
    for box in textbox_updates:
        while len(textbox_updates[box]) > 0:
            update = textbox_updates[box][0]
            if box == "events":
                wrap = False
            else:
                wrap = True
            if update[1]:  # Box set to clear
                text_boxes[box].set_text_list(update[0], wrap=wrap)
            else:
                text_boxes[box].add_text_list(update[0], wrap=wrap)
            if not isinstance(text_boxes["events"].width, type(None)) \
                    and box == "events":
                text_boxes[box].wrap()
                text_boxes[box].scroll_pos = text_boxes[box].find_visible_lines(
                    find_max_scroll=True)
                text_boxes[box].find_visible_lines()
                text_boxes["events"].remove_out_of_screen()
                text_boxes[box].wrap()

            textbox_updates[box].pop(0)

    # Render Textboxes
    for box in text_boxes:
        text_boxes[box].render(display, resolution)
    TEXTBOX_LOCK.release()

    # Handle typing
    typing_returns = typing_manager.type_loop()
    current_input_string = typing_returns[0]  # Get key presses
    choice = check_choices()
    typing_manager.set_text(current_input_string)  # Conform to choices
    string_returned = typing_returns[2]
    string_changed = typing_returns[3]
    if string_changed:
        deleted_char = True
        choices_cycle = []
        current_choice_num = -1
        check_choices()

    if string_returned and not return_pressed:
        if not isinstance(choice, type(None)):
            return_pressed = True
            user_input = choice
            current_input_string = ""
            typing_manager.set_text("")
            actions = []
            objects = []

    TEXTBOX_LOCK.acquire()
    text_boxes["input"].set_text_list(current_input_string)
    TEXTBOX_LOCK.release()

    if not pygame.key.get_mods() & pygame.KMOD_LALT:
        alt_hold = 0

    # Handle Pygame Events
    for event in pygame.event.get():
        # Screen Resized
        if not hotkey_enabled:
            typing_manager.handle_event(event)

        if event.type == pygame.KEYDOWN and waiting:
            if hotkey_enabled and "unicode" in event.dict:
                _key = str(event.dict["unicode"])
                if _key in keyboard_hotkeys and not isinstance(
                        keyboard_hotkeys[_key], type(None)):
                    pressed_hotkeys.append(["keyboard", _key])
            if event.key == pygame.K_RETURN:
                return_pressed = False
            if event.key == pygame.K_LALT:
                alt_hold = time.time() * 1000
            if event.key == pygame.K_TAB:
                # TODO: Handle key overwrites in config
                if typing_manager.is_shift_held():
                    previous_choice(typing_manager)
                else:
                    next_choice(typing_manager)
            if event.key == pygame.K_BACKSPACE:  # Move back through path
                if deleted_char:
                    deleted_char = False
                elif len(current_input_string) < 1:
                    if len(path) > 0:
                        path.pop()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LALT:
                if not hotkeys_locked and not alt_held():
                    hotkey_enabled = not hotkey_enabled
                alt_hold = 0

        if event.type == pygame.MOUSEBUTTONDOWN and waiting:
            if hotkey_enabled and "button" in event.dict:
                _key = str(event.dict["button"])
                if _key in mouse_hotkeys and not isinstance(mouse_hotkeys[_key],
                                                            type(None)):
                    pressed_hotkeys.append(["mouse", _key])

        if event.type == pygame.VIDEORESIZE:
            display = pygame.display.set_mode(event.dict["size"],
                                              pygame.RESIZABLE)
            resolution = event.dict["size"]

        # Screen closed
        elif event.type == pygame.QUIT:
            pygame.display.quit()
            quit_running = True
            break

        else:
            # Push events to textboxes and typing manager
            TEXTBOX_LOCK.acquire()
            old_tooltip = None
            found_tooltip = False
            for box in text_boxes:
                new_tooltip, tooltip_scroll, click = text_boxes[
                    box].handle_event(event, pygame.mouse.get_pos())
                if not click:
                    if new_tooltip != old_tooltip:
                        # Only display tooltip if have not already
                        text_boxes["tooltips"].set_text_list(new_tooltip)
                        old_tooltip = new_tooltip
                        found_tooltip = True
                    if not isinstance(tooltip_scroll, type(None)):
                        text_boxes["tooltips"].scroll(tooltip_scroll)
                elif new_tooltip[0].click and waiting:
                    if box != "path":
                        if alt_held():
                            display.fill(background_color)
                            font = pygame.font.SysFont(default_font,
                                                       default_font_size)
                            message = "Press a key to assign as a hotkey. " \
                                      "ESC cancels."
                            label = font.render(message, 1, default_color)
                            display.blit(label, (resolution[0] // 2 -
                                                 font.size(message)[0] // 2,
                                                 resolution[1] // 2))
                            pygame.display.flip()
                            _key = None
                            medium = None
                            while isinstance(_key, type(None)):
                                for _event in pygame.event.get():
                                    if _event.type == pygame.KEYDOWN:
                                        if "unicode" in _event.dict:
                                            _key = str(_event.dict["unicode"])
                                            medium = "keyboard_hotkeys"
                                            break
                                    elif _event.type == pygame.MOUSEBUTTONDOWN:
                                        if "button" in _event.dict:
                                            _key = str(_event.dict["button"])
                                            medium = "mouse_hotkeys"
                                            break
                                    elif _event.type == pygame.VIDEORESIZE:
                                        display = pygame.display.set_mode(
                                            _event.dict["size"],
                                            pygame.RESIZABLE)
                                        resolution = _event.dict["size"]

                                    # Screen closed
                                    elif _event.type == pygame.QUIT:
                                        quit_running = True
                                        break
                            _path = None
                            if not isinstance(_key, type(None)) and _key != \
                                    '\x1b':
                                _path = ">".join(
                                    [text.get_text_string() for text in
                                     path]) + ">" + new_tooltip[0].get_whole()
                                change_config(medium, _key, _path)
                                mouse_hotkeys = get_value("mouse_hotkeys")
                                keyboard_hotkeys = get_value("keyboard_hotkeys")
                            display.fill(background_color)
                            font = pygame.font.SysFont(default_font,
                                                       default_font_size)
                            if isinstance(_path, type(None)):
                                message = "Cancelled."
                            else:
                                message = "'" + _path + "' assigned to "\
                                          + medium[:medium.find("_")] \
                                          + " key: '" + _key + "'"
                            label = font.render(message, 1, default_color)
                            display.blit(label, (resolution[0] // 2 -
                                                 font.size(message)[0] // 2,
                                                 resolution[1] // 2))
                            new_message = "Press any key to continue."
                            label = font.render(new_message, 1,
                                                default_color)
                            display.blit(label, (resolution[0] // 2 -
                                                 font.size(new_message)[0] // 2,
                                                 resolution[1] // 2 +
                                                 font.size(message)[1]))
                            pygame.display.flip()
                            get_key_press()
                        else:
                            user_input = new_tooltip[0].get_whole()
                    else:
                        current_input_string = ""
                        typing_manager.set_text("")
                        user_input = None
                        if len(path) > 0:
                            ind = 0
                            for obj in path:
                                if obj.get_text_string() == \
                                        new_tooltip[0].get_whole():
                                    break
                                ind += 1
                            path = path[:ind + 1]
                if found_tooltip:
                    break
            if not found_tooltip:
                text_boxes["tooltips"].set_text_list("")

            TEXTBOX_LOCK.release()

    if quit_running:
        try:
            pygame.display.quit()
        except pygame.error:
            pass
        break

    pygame_clock.tick(fps)
    pygame.display.flip()

running = False
