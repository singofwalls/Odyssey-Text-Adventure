"""
Includes methods to allow for user input
"""
import pygame

from core.configs import get_value

key_tick = get_value("input", "key tick")
key_repeat_delay = get_value("input", "key repeat delay")
max_keys_pressed = get_value("input", "max keys pressed")
unshifted_keys = get_value("input", "unshifted keys")
shifted_keys = get_value("input", "shifted keys")

alphanumerals = "abcdefghijklmnopqrstuvwxyz1234567890"


class TypingManager(object):  # TODO: Keep cursor in bounds
    """Controls typing by tracking key presses
    Called Externally.

    :type enable_cursor: bool
    """

    def __init__(self, enable_cursor=True):
        self.keys = {}
        self.cursor_pos = 0
        self.string = ""
        self.enable_cursor = enable_cursor

    @staticmethod
    def is_character(key):
        """Tests whether given key is a character.
        Used internally.

        :type key: str
        """

        if key in shifted_keys or key in unshifted_keys or key.lower() \
                in alphanumerals:
            return True
        return False

    @staticmethod
    def shift_key(key):
        """Returns shifted version of given key.
        Used internally.

        :type key: str
        """
        if key in alphanumerals:
            return key.upper()
        index = unshifted_keys.find(key)
        if index > -1:
            return shifted_keys[unshifted_keys.find(key)]
        return key

    def is_shift_held(self):
        """Gets whether shift key is pressed.
        Used internally.
        """

        return "left shift" in self.keys or "right shift" in self.keys

    def is_caps_on(self):
        """Gets whether caps lock is on
        Used internally.
        """

        return "caps lock" in self.keys

    def is_control_held(self):
        """Gets whether control is held
        Used internally.
        """

        return "left ctrl" in self.keys or "right ctrl" in self.keys

    def index_of_next_word(self, direction="right"):
        """Finds the index of the next word in string.
        Used internally.

        :type direction: str
        :param direction: Must be either 'left' or 'right' from cursor
        """

        if direction == "left":
            return self.string[:self.cursor_pos].rstrip(" ").rfind(" ")
        elif direction == "right":
            return self.string[self.cursor_pos:].lstrip(" ").find(" ") + len(
                self.string[:self.cursor_pos]) + 1
        else:
            raise ValueError("Direction must be 'left' or 'right'")

    def press_key(self, key):
        """Acknowledges key press if it is the only key being pressed or if
        multiple_key_repeat is on.
        Used internally.

        :type key: str
        """

        keys_pressed = 0
        if self.is_character(key):
            for key_to_check in self.keys.keys():
                if self.keys[key_to_check] > 0 and self.is_character(
                        key_to_check):
                    keys_pressed += 1
        if keys_pressed < max_keys_pressed:
            self.keys[key] = 1

    def reset_key(self, key):
        """Removes key from active keys.
        Used internally.

        :type key: str
        """

        self.keys.pop(key, None)

    def backspace(self):
        """Removes words or characters from input_string.
        Used internally.
        """

        if self.is_control_held():
            if " " in self.string[:self.cursor_pos].rstrip(" "):
                inp_string_len = len(self.string)
                self.string = self.string[:self.index_of_next_word(
                    "left")] + " " + self.string[self.cursor_pos:]
                self.cursor_pos -= (inp_string_len - len(self.string))
            else:
                self.string = self.string[self.cursor_pos:]
                self.cursor_pos = 0
        else:
            if self.cursor_pos != 0:
                self.string = self.string[:self.cursor_pos - 1] \
                               + self.string[self.cursor_pos:]
                self.cursor_pos -= 1

    def delete(self):
        """Removes word or character from right of cursor.
        Used internally.
        """

        if self.is_control_held():
            if " " in self.string[self.cursor_pos:].lstrip(" "):
                self.string = self.string[:self.cursor_pos] + " " \
                              + self.string[self.index_of_next_word("right"):] \
                                  .lstrip(" ")
            else:
                self.string = self.string[:self.cursor_pos]
        else:
            if self.cursor_pos != len(self.string):
                self.string = self.string[:self.cursor_pos] \
                               + self.string[self.cursor_pos + 1:]

    def move_left(self):
        """Moves the cursor_pos left a character or a word
        Used internally.
        """

        if self.is_control_held():
            if " " in self.string[:self.cursor_pos].rstrip(" "):
                self.cursor_pos = self.index_of_next_word("left")
            else:
                self.cursor_pos = 0
        else:
            self.cursor_pos -= 1

    def move_right(self):
        """Moves the cursor_pos right a character or a word
        Used internally.
        """

        if self.is_control_held():
            if " " in self.string[self.cursor_pos:].lstrip(" "):
                self.cursor_pos = self.index_of_next_word("right")
            else:
                self.cursor_pos = len(self.string)
        else:
            self.cursor_pos += 1

    def add_character(self, key):
        """Adds given key after current cursor_pos
        Used internally.

        :type key: str
        """

        new_key = key
        if new_key == "space":
            new_key = " "

        if self.is_shift_held():
            new_key = self.shift_key(new_key)
        if self.is_caps_on() != self.is_shift_held():
            new_key = new_key.upper()
        self.string = self.string[:self.cursor_pos] \
                      + new_key \
                      + self.string[self.cursor_pos:]

        self.cursor_pos += 1

    def handle_event(self, event):
        """Handles pygame events such as button presses.
        Called externally.

        :type event: pygame.Event
        """
        if event.type == pygame.KEYDOWN:
            self.press_key(pygame.key.name(event.key))
        if event.type == pygame.KEYUP:
            self.reset_key(pygame.key.name(event.key))

    def set_text(self, text):
        """Sets stored string to text
        Called externally

        :type text: str
        """
        self.cursor_pos = len(self.string)
        self.string = text

    def type_loop(self):
        """Checks all keys and updates string and cursor position
        Called externally
        """

        changed = False
        for key in self.keys.keys():
            if (self.keys[key] > key_repeat_delay and self.keys[key] % key_tick == 0) or self.keys[key] == 1:
                if key == "backspace":
                    old = self.string
                    self.backspace()
                    if old != self.string:
                        changed = True
                elif key == "delete" and self.enable_cursor:
                    old = self.string
                    self.delete()
                    if old != self.string:
                        changed = True
                elif key == "return":
                    self.keys = {}
                    return self.string, 0, True, changed
                elif key == "left" and self.enable_cursor:
                    self.move_left()
                elif key == "right" and self.enable_cursor:
                    self.move_right()
                elif len(key) < 2 or key == "space":
                    self.add_character(key)
                    changed = True

            # Increment active keys
            if self.keys[key] > 0:
                self.keys[key] += 1
            if self.cursor_pos < 0:
                self.cursor_pos = 0
            if self.cursor_pos > len(self.string):
                self.cursor_pos = len(self.string)

        return self.string, self.cursor_pos, False, changed
