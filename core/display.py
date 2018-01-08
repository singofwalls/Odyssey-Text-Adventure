"""
Includes classes allowing for the displaying of text.
Wordwrap, fonts, scrolling, and tooltips are all handled here.
"""
import pygame

from core.configs import get_value

default_font = get_value("display", "default_font")
default_color = get_value("display", "default_color")
default_font_size = get_value("display", "default_font_size")

choice_font_size = get_value("customization", "choice_font_size")
choice_font = get_value("customization", "choice_font")

has_tooltip_color = get_value("customization", "has_tooltip_color")

lines_per_scroll = get_value("display", "lines_per_scroll")
min_scroll_bar_height = get_value("display", "min_scroll_bar_height")
scroll_bar_width = get_value("display", "scroll_bar_width")

priority_word_wrap_chars = get_value("display", "priority_word_wrap_chars")


class Text(object):
    """Stores a phrase, font, color, and tooltip

    :type text: str
    :type tooltip: list[Text] | str | None
    :type color: tuple[int, int, int]
    :type highlight_color: tuple[int, int, int] | None
    :type font_name: str
    :type font_size: int
    :type bold: bool
    :type italic: bool
    :type new_line: bool
    :param new_line: breaks line at end of phrase
    """

    def __init__(self, text, tooltip=None, hide_tooltip=False,
                 color=default_color,
                 highlight_color=None, font_name=default_font,
                 font_size=default_font_size, bold=False, italic=False,
                 new_line=False, whole=None, click=False, copying=False):

        self.text = text
        if isinstance(whole, type(None)):
            self.whole = text
        else:
            self.whole = whole
        self.click = click
        self.tooltip = tooltip
        self.hide_tooltip = hide_tooltip
        self.color = color
        self.highlight_color = highlight_color
        self.font_name = font_name
        self.font_size = font_size
        self.bold = bold
        self.italic = italic
        self.new_line = new_line

        self.x_pos = None
        self.y_pos = None

        if isinstance(self.tooltip, str):
            self.tooltip = [Text(self.tooltip)]

        if not self.hide_tooltip and not isinstance(self.tooltip, type(None)):
            self.highlight_color = has_tooltip_color  # Uncomment for tooltip
            #                                               highlight
            # self.italic = True
        if not copying:
            self.font = None
            self.update_font()

            self.width = None
            self.height = None
            self.label = None
            self.update_size()

    def update_font(self, force_update=False):
        if isinstance(self.font, type(None)) or force_update:
            try:
                self.font = pygame.font.SysFont(self.font_name, self.font_size,
                                                self.bold, self.italic)
            except OSError:
                print(
                    "Could not load font " + self.font_name + ", using default")
                self.font_name = default_font
                self.font = pygame.font.SysFont(self.font_name, self.font_size,
                                                self.bold, self.italic)

    def update_size(self, force_font=False):
        """Updates width and height based on font and text"""
        self.update_font(force_font)

        self.width = self.font.size(self.text)[0]
        self.height = self.font.size(self.text)[1]
        self.label = self.font.render(self.text.strip(), 1, self.color,
                                      self.highlight_color)

    def clear_font(self):
        """Clear font for saving"""
        self.font = None
        if not isinstance(self.tooltip, type(None)):
            for text in self.tooltip:
                text.clear_font()

    def set_x_pos(self, x_pos):
        """Sets x_pos to given pos

        :type x_pos: int
        """
        self.x_pos = x_pos

    def set_y_pos(self, y_pos):
        """Sets y_pos to given pos

        :type y_pos: int
        """
        self.y_pos = y_pos

    def get_x_pos(self):
        """Returns x_pos"""
        return self.x_pos

    def get_y_pos(self):
        """Returns y_pos"""
        return self.y_pos

    def copy(self, click=None, text_string=None, new_line=None):
        """Returns a deep copy of self"""

        if isinstance(new_line, type(None)):
            new_line = self.new_line

        copied_tooltip = self.tooltip
        if not isinstance(self.tooltip, type(None)):
            copied_tooltip = []
            for text in self.tooltip:
                copied_tooltip.append(text)  # .copy())  # Doesn't seem to have impact other than speed

        font_name = self.font_name
        font_size = self.font_size
        if isinstance(click, type(None)):
            click = self.click
        elif click:
            font_name = choice_font
            font_size = choice_font_size

        if isinstance(text_string, type(None)):
            text_string = self.text

        text = Text(text_string, copied_tooltip, self.hide_tooltip, self.color,
                    self.highlight_color, font_name, font_size,
                    self.bold, self.italic, new_line, self.whole,
                    click, True)

        text.font = self.font
        text.width = self.width
        text.height = self.height
        text.label = self.label
        text.y_pos = self.y_pos
        text.x_pos = self.x_pos
        if click:
            text.update_font(True)

        return text

    def is_new_line(self):
        """Returns whether phrase is marked for new line"""
        return self.new_line

    def append(self, text):
        """Appends text onto end of text

        :type text: str
        """

        self.text += text
        self.update_size()

    def strip(self):
        """Strips whitespace off of text"""

        self.text = self.text.strip()
        self.update_size()

    def set_text(self, text):
        """Sets the text to text.
        Called externally

        :type text: str
        """
        self.text = text
        self.update_size()

    def set_font(self, font=None, size=None):
        """Sets the font and size to given values.
        Called externally

        :type font: str | None
        :type size: int | None
        """
        if not isinstance(font, type(None)):
            self.font = font
        if not isinstance(size, type(None)):
            self.font_size = size
        self.update_size(True)

    def set_tooltip(self, text_list):
        """Sets the tooltip to text_list.
        Called externally

        :type text_list: list[Text] | str
        """

        if isinstance(text_list, str):
            self.tooltip = [Text(text_list)]
        else:
            self.tooltip = text_list

        if not self.hide_tooltip and not isinstance(self.tooltip, type(None)):
            self.highlight_color = has_tooltip_color
            self.update_font(True)

    def get_text(self):
        """Returns the text string associated with the object"""
        return self.text

    def get_whole(self):
        """Returns the original text string associated with the object"""
        return self.whole

    def update_whole(self):
        """Resets the original text string associated with the object"""
        self.whole = self.text

    def get_tooltip(self):
        """Returns the tooltip Text list associated with the object"""
        return self.tooltip

    def num_chars_fit(self, target_distance, index=0):
        """Returns the number of chars that fit from an index given a distance

        :type target_distance: int
        :type index: int
        """

        self.update_font()

        distance = 0
        num_chars = 0
        for char in self.text[index:]:
            char_size = self.font.size(char)[0]
            if char_size + distance <= target_distance:
                num_chars += 1
                distance += char_size
            else:
                return num_chars
        return num_chars

    def split(self, index):
        """Returns a list of 2 halves of original text split at index with
        parent's properties.

        :type index: int
        """
        halves = [self.copy(self.click, self.text[:index], False),
                  self.copy(self.click, self.text[index:])]
        return halves[0], halves[1]

    def split_at_phrase(self, phrase, max_split=-1):
        """Returns a list of all parts of original text split at each
        occurrence of phrase with parent's properties.

        :type phrase: str
        :type max_split: int
        :param max_split: -1 for split all. Specifies the max number of splits
        """
        phrases = []
        words = self.text.split(phrase, max_split)
        word_index = 0
        for word in words:
            if word != '':
                phrase_modifier = phrase
                new_line = False
                if word_index == len(words) - 1:
                    phrase_modifier = ""
                    new_line = True
                phrases.append(self.copy(self.click, word + phrase_modifier, new_line))
            else:
                if word_index != len(words) - 1:
                    # Next word starts with phrase
                    words[word_index + 1] = phrase + words[word_index + 1]
            word_index += 1
        return phrases

    def get_width(self):
        """Returns the width of the text in pixels"""
        return self.width

    def get_height(self):
        """Returns the height of the text in pixels"""
        return self.height

    def get_label(self):
        """Returns a pygame label which can be blit to a surface"""
        return self.label


class TextBox(object):
    """
    Creates a box with text in it

    :type name: str
    :type bounds: tuple[float, float, float, float]
    :type text_list: list[Text] | str
    :type border_size: int
    :type border_color: tuple[int, int, int]
    :type margin_size: tuple[int, int]
    :type alignment: str
    :type enable_scrolling: bool
    :type show_scroll_bar: bool
    :type scroll_bar_color: tuple[int, int, int]
    :type scroll_bar_width: int
    :param alignment: must be either "left", "right", "center", or "justified"
    :param border_size: 0 for filled rect, -1 for no border
    """

    def __init__(self, name, bounds, text_list, border_size=1,
                 border_color=(255, 255, 255), margin_size=(10, 5),
                 alignment="left", enable_scrolling=True,
                 show_scroll_bar=True, scroll_bar_color=(200, 200, 200),
                 _scroll_bar_width=scroll_bar_width):

        self.name = name
        self.x = bounds[0]
        self.y = bounds[1]
        self.x2 = bounds[2]
        self.y2 = bounds[3]
        self.text_list = text_list
        self.border_size = border_size
        self.border_color = border_color
        self.margin_size = margin_size
        self.alignment = alignment
        self.enable_scrolling = enable_scrolling
        self.show_scroll_bar = show_scroll_bar
        self.scroll_bar_color = scroll_bar_color
        self.scroll_bar_width = _scroll_bar_width

        self.pure_justified = False

        self.resolution = None
        self.width = None
        self.height = None
        self.x_coord = None
        self.y_coord = None

        self.bar_x = None
        self.bar_y = None
        self.bar_width = None
        self.bar_height = None
        self.ideal_bar_height = None
        self.total_bar_height = None

        self.drag_bar_from = None
        self.bar_remainder = None

        self.scroll_pos = 0
        self.max_scroll = 0
        self.max_active_lines = 0

        self.active_text_lines = []
        self.all_text_lines = []
        self.formatted_lines = []
        self.justified_lines = {}

        self.scroll_wrapped = False

        if type(self.text_list) == str:
            self.text_list = [Text(self.text_list)]

    @staticmethod
    def get_line_width(line):
        """Returns the width of a line given.
        Used Internally.

        :type line: list[Text]
        """
        width = 0
        for phrase in line:
            width += phrase.get_width()
        return width

    @staticmethod
    def get_height_of_line(line):
        """
        Finds the tallest phrase throughout the given line.
        Used internally.

        :type line: list[Text]
        """

        max_height = 0
        for phrase in line:
            if phrase.get_height() > max_height:
                max_height = phrase.get_height()
        return max_height

    @staticmethod
    def strip_line(line):
        """Removes trailing whitespace from given line.

        :type line: list[Text]
        """
        new_line = []
        phrase_index = 0
        for phrase in line:
            if phrase_index < len(line) - 1 and line[
                        phrase_index + 1].get_text() != " ":
                new_line.append(phrase)
            else:
                word = phrase.copy()
                word.set_text(word.get_text().rstrip())
                new_line.append(word)
            phrase_index += 1
        return new_line

    def remove_out_of_screen(self):
        text_list = []
        for line in self.active_text_lines:
            for text in line:
                text_list.append(text)
        self.text_list = text_list

    def has_overflown(self, lines):
        """Checks if lines are within y bounds. Returns True if within bounds.
        Used internally

        :type lines: list[list[Text]]
        """
        total_height = 0
        for test_line in lines:
            total_height += self.get_height_of_line(test_line)
        if total_height >= self.height:
            return True
        return False

    def update_dimensions(self, resolution):
        """Updates resolution, width, height, x_coords,
        and y_coords based on given screen resolution.
        Used internally.

        :type resolution: tuple[int, int]
        """

        self.resolution = resolution
        self.x_coord = (resolution[0] * self.x) + self.margin_size[0]
        self.y_coord = (resolution[1] * self.y) + self.margin_size[1]
        self.width = (resolution[
                          0] * self.x2 - self.x_coord) - self.margin_size[0]
        self.height = (resolution[
                           1] * self.y2 - self.y_coord) - self.margin_size[1]
        if self.show_scroll_bar:
            self.width -= self.scroll_bar_width

    def wrap(self):
        """Creates lines of wrapped words.
        Used internally.
        """
        if self.width < 1 or self.height < 1:
            # Text box too small
            return

        width = self.width
        shortened_text_list = self.text_list[:]

        lines = []
        line = []

        while len(shortened_text_list) > 0 and not (len(shortened_text_list) == 1 and shortened_text_list[0].text == ''):

            advanced_lines = False
            line, shortened_text_list = self.create_line(
                line + shortened_text_list)
            if len(shortened_text_list) == 0 and (
                            len(line) < 1 or not line[-1].is_new_line()):
                # No more words, line fits on screen
                lines.append(self.strip_line(line))
                break

            if self.get_line_width(line) < width and (
                            len(line) < 1 or not line[-1].is_new_line()):
                # Room to fit more chars but next phrase doesn't fit
                # More chars to use and not new line

                phrase = shortened_text_list[0]
                halves = []
                min_distance = width + 1
                for wrap_char in priority_word_wrap_chars:
                    # Check if phrase contains wrap chars

                    if wrap_char in phrase.get_text():
                        # Check each occurrence for distance to width
                        indexes = []
                        i = 0
                        for char in phrase.get_text():
                            if char == wrap_char:
                                indexes.append(i)
                            i += 1

                        for char_index in indexes:
                            current_halves = phrase.split(char_index)
                            current_halves[0].append(wrap_char)
                            current_halves[1].set_text(current_halves[1].text[1:])
                            distance = width - self.get_line_width(
                                line) - current_halves[0].get_width()

                            if min_distance > distance >= 0:
                                # Save halves closest to width
                                min_distance = distance
                                halves = current_halves
                            else:
                                # Half over line. Move to next wrap_char
                                break

                if len(halves) > 0:
                    # Found a wrap point close to width
                    shortened_text_list.pop(0)
                    if len(halves[0].get_text()) > 0:
                        line.append(halves[0])
                    if len(halves[1].get_text()) > 0:
                        shortened_text_list.insert(0, halves[1])

                elif phrase.get_width() <= self.width:
                    # Cutting at break points does not help
                    # Phrase fits on new line
                    lines.append(line)
                    shortened_text_list.pop(0)
                    word = phrase.copy()
                    word.set_text(word.get_text().lstrip())
                    line = [word]
                    advanced_lines = True

                elif len(phrase.get_text()) > 1:
                    # Does not fit on new line. Must split word
                    distance = width - self.get_line_width(line)
                    split_at = phrase.num_chars_fit(distance) - 1
                    halves = phrase.split(split_at)
                    if len(halves[0].get_text()) > 0 and split_at > 0:
                        halves[0].append("-")
                        line.append(halves[0])
                        shortened_text_list.pop(0)
                        shortened_text_list.insert(0, halves[1])
                else:
                    # Single Char does not fit on new line. Stop wrapping
                    shortened_text_list.pop(0)

            if not advanced_lines or len(shortened_text_list) == 0:
                lines.append(line)
                line = []

        # Update all line vars
        self.all_text_lines = lines
        self.max_active_lines = self.find_visible_lines(True)
        self.max_scroll = self.find_visible_lines(False, True)
        if self.show_scroll_bar and self.max_scroll == 0:
            # Remove scrollbar
            self.update_dimensions(self.resolution)
            self.width += self.scroll_bar_width
            self.scroll_wrapped = False
        elif self.show_scroll_bar:
            # Show scrollbar
            if not self.scroll_wrapped:
                self.update_dimensions(self.resolution)
                self.scroll_wrapped = True
        self.find_visible_lines()
        if len(self.active_text_lines) < 1:
            self.max_scroll = 0
        if self.alignment == "justified":
            self.justified_formatting()

    def create_line(self, text_list):
        """Creates a line of wrapped text from given text_list.
        Returns created line and new text_list missing used text.
        Used internally.

        :type text_list: list[Text]
        :rtype: list[Text], list[Text]
        """

        shortened_text_list = text_list[:]
        line = []
        phrase_num = 0
        for phrase in text_list:
            if phrase.text == "-1 ":
                print("HERE")
            if phrase.get_width() + self.get_line_width(
                    line) <= self.width:
                shortened_text_list.pop(0)
                word = phrase  # 10x faster without copying now #.copy()
                if phrase_num == 0:
                    word.set_text(word.get_text().lstrip())
                line.append(word)
            else:
                break
            if phrase.is_new_line():
                break
            phrase_num += 1
        return line, shortened_text_list

    def find_visible_lines(self, find_max_lines=False, find_max_scroll=False,
                           _scroll_pos=None):
        """Updates active_text_lines if neither find_max_lines nor
        find_max_scroll are True.
        Used Internally.

        :type find_max_lines: bool
        :type find_max_scroll: bool
        :type _scroll_pos: int
        :param find_max_lines: Counts number of lines displayed at top of scroll
        :param find_max_scroll: Recursively finds the max scroll amount if True
        :param _scroll_pos: For recursive checking of max scroll
        :rtype: int
        :return: Number of lines displayed
        """

        scroll_pos = 0

        if not find_max_lines and not find_max_scroll:
            if self.scroll_pos < 0:
                self.scroll_pos = 0
            if self.scroll_pos > self.max_scroll:
                self.scroll_pos = self.max_scroll
            scroll_pos = self.scroll_pos

        if find_max_scroll:
            if isinstance(_scroll_pos, type(None)):
                scroll_pos = len(self.all_text_lines) - 1
            else:
                scroll_pos = _scroll_pos

        lines = []
        line_num = 0
        overflow = False
        for line in self.all_text_lines[scroll_pos:]:
            lines.append(line)
            if self.has_overflown(lines):
                overflow = True
                lines.pop()
                break
            line_num += 1

        if not find_max_lines:
            if find_max_scroll:
                if not overflow:
                    if scroll_pos >= 0:
                        # Lines still offscreen
                        scroll_pos -= 1
                        return self.find_visible_lines(False, True, scroll_pos)
                    else:
                        # No lines offscreen
                        return 0
                else:
                    # Line touching bottom found
                    return scroll_pos + 1
            else:
                self.active_text_lines = lines

        return len(lines)

    def set_pure_justified(self, pure=True):
        """Justifies all lines if True
        Called externally

        :type pure: bool
        """
        self.pure_justified = pure

    def justified_formatting(self):
        """Formats all lines to work with justified alignment.
        Used internally.
        """

        line_num = 0
        self.justified_lines = {}
        for line in self.all_text_lines:
            if self.pure_justified or (line_num < len(self.all_text_lines) - 1
                                       and not line[-1].is_new_line()):
                # Justify if not last line and previous line is not a new_line
                # Or if pure_justified
                new_line = []
                num_spaces = 0
                phrase_num = 0
                current_line = self.strip_line(line)  # Only slowed it down
                for phrase in current_line:
                    word_num = 0
                    words = phrase.split_at_phrase(" ")
                    for word in words:
                        previous_word = None
                        if word_num != 0:
                            previous_word = words[word_num - 1]
                        elif phrase_num != 0:
                            previous_word = current_line[phrase_num - 1]
                        if word.get_text().endswith(" ") \
                                or (word.get_text().startswith(" ")
                                    and (isinstance(
                                        previous_word, type(None))
                                         or not previous_word.get_text(
                                        ).endswith(" "))):
                            num_spaces += 1
                        new_line.append(word)
                        word_num += 1
                    phrase_num += 1
                self.justified_lines[line_num] = [new_line, num_spaces]
            line_num += 1

    def is_within_bounds(self, pos, bounds=None):
        """Returns whether given pos is within given bounds.
        Used internally

        :type bounds: list[int, int, int, int] | None
        :type pos: list[int, int]
        :param bounds: if None, uses textboxes bounds. [x, y, x2, y2] format
        """

        if isinstance(bounds, type(None)):
            bounds = [int(self.x * self.resolution[0]),
                      int(self.y * self.resolution[1]),
                      int(self.x2 * self.resolution[0]),
                      int(self.y2 * self.resolution[1])]

        if bounds[2] >= pos[0] >= bounds[0]:
            if bounds[3] >= pos[1] >= bounds[1]:
                return True
        return False

    def drag_bar(self, from_cursor_pos, cursor_pos):
        """Scrolls using scroll bar from from_cursor_pos to cursor_pos.
        Used internally.

        :type from_cursor_pos: list[int, int]
        :type cursor_pos: list[int, int]
        """

        distance = from_cursor_pos[1] - cursor_pos[1]
        distance_percent = distance / (self.total_bar_height
                                       - self.ideal_bar_height)
        scroll_offset = distance_percent * self.max_scroll
        if not isinstance(self.bar_remainder, type(None)):
            scroll_offset += self.bar_remainder
        self.scroll_pos -= int(scroll_offset)
        self.find_visible_lines()
        if abs(scroll_offset) >= 1:
            self.drag_bar_from = cursor_pos
            remainder = scroll_offset % 1
            if scroll_offset < 0:
                remainder *= -1
            self.bar_remainder = remainder

    def scroll(self, scroll_amount=lines_per_scroll):
        """Scrolls the screen the given number of lines.
        Called Internally and Externally

        :type scroll_amount: int
        :param scroll_amount: Negative numbers reverse direction
        """
        self.scroll_pos += scroll_amount
        self.find_visible_lines()

    def set_text_list(self, text_list, wrap=True):
        """Updates the text_list to reflect given list and rewraps lines.
        Called externally.

        :type text_list: list[Text] | str
        """

        self.text_list = text_list[:]
        if type(self.text_list) == str:
            self.text_list = [Text(self.text_list)]
        if wrap:
            self.wrap()

    def add_text_list(self, text_list, wrap=True):
        """Appends text list onto existing text_list. Scrolls to bottom.
        Called externally.

        :type text_list: list[Text] | str
        """
        if type(self.text_list) == str:
            self.text_list.append(Text(text_list))
        else:
            for text in text_list:
                self.text_list.append(text)
        if wrap:
            self.wrap()
            self.scroll_pos = self.find_visible_lines(find_max_scroll=True)
            self.find_visible_lines()

    def set_alignment(self, alignment):
        """Updates alignment to given alignment and rewraps.
        Called externally.

        :type alignment: str
        :param alignment: must be either "left", "right", "center", or "justified"
        """

        self.alignment = alignment
        if len(self.text_list) > 1 or self.text_list[0].get_text() != "":
            self.wrap()

    def get_text_list(self):
        """Returns the current text_list
        Called externally.
        """

        return self.text_list

    def handle_event(self, event, cursor_pos):
        """Handles pygame events such as mouse scrolls and button presses.
        Returns hovered phrase's tooltip if available.
        Called Externally

        :type event: pygame.Event
        :type cursor_pos: list[int, int]
        """

        click = False

        if event.type == pygame.MOUSEMOTION:
            if not isinstance(self.drag_bar_from, type(None)):
                self.drag_bar(self.drag_bar_from, cursor_pos)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.drag_bar_from = None
                click = True

        if self.is_within_bounds(cursor_pos):

            hovered_tooltip = None
            tooltip_scroll = None
            found = False

            # Tooltips
            for line in self.formatted_lines:
                if found:
                    break
                for phrase in line:
                    x = phrase.get_x_pos()
                    if isinstance(x, type(None)):
                        raise ReferenceError(
                            "Must render box before handling events")
                    y = phrase.get_y_pos()
                    w = phrase.get_width()
                    h = phrase.get_height()
                    if self.is_within_bounds(cursor_pos, [x, y, x + w, y + h]):
                        if click:
                            return [phrase], None, True
                        if not isinstance(phrase.get_tooltip(), type(None)):
                            hovered_tooltip = phrase.get_tooltip()
                            found = True
                        break  # Hovering word

            # Mousewheel scroll
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.enable_scrolling:
                    if event.button == 4:
                        # Scroll down

                        if isinstance(hovered_tooltip, type(None)):
                            # Scrolling not on a tooltip
                            scroll_amount = min(self.max_active_lines,
                                                lines_per_scroll)
                            self.scroll(-scroll_amount)
                        else:
                            tooltip_scroll = -lines_per_scroll

                    elif event.button == 5:
                        # Scroll up
                        if isinstance(hovered_tooltip, type(None)):
                            scroll_amount = min(self.max_active_lines,
                                                lines_per_scroll)
                            self.scroll(scroll_amount)
                        else:
                            tooltip_scroll = lines_per_scroll

            # Bar scroll
            if self.show_scroll_bar and self.max_scroll > 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.is_within_bounds(cursor_pos,
                                             [self.bar_x, self.bar_y,
                                              self.bar_x + self.bar_width,
                                              self.bar_y + self.bar_height]):
                        if event.button == 1:
                            # Left mouse down on scroll bar
                            self.drag_bar_from = cursor_pos

            return hovered_tooltip, tooltip_scroll, False

        return None, None, False

    def render_scroll_bar(self, display):
        """Draws the scrollbar to the given display.
        Used internally.

        :type display: pygame.Surface
        """
        if self.show_scroll_bar and self.max_scroll > 0:
            self.bar_x = self.x2 * self.resolution[0] - self.scroll_bar_width \
                         - 1
            min_y = self.y * self.resolution[1] + 1
            self.bar_width = self.scroll_bar_width
            self.total_bar_height = (self.y2 * self.resolution[1]) - min_y

            self.ideal_bar_height = self.total_bar_height * (
                self.max_active_lines / len(self.all_text_lines))
            self.bar_height = max(min_scroll_bar_height * self.total_bar_height,
                                  self.ideal_bar_height)
            self.bar_y = min_y + (self.total_bar_height
                                  - self.bar_height) * (
                                     self.scroll_pos / self.max_scroll)

            pygame.draw.rect(display, self.scroll_bar_color,
                             [self.bar_x, self.bar_y, self.bar_width,
                              self.bar_height])

    def get_x(self):
        return (self.x_coord - self.margin_size[0]) + ((self.x2 - self.x) * self.resolution[0])

    def get_y(self, bottom=False):
        if bottom:
            return (self.y_coord - self.margin_size[1]) + ((self.y2 - self.y) * self.resolution[1])
        return (self.y_coord - self.margin_size[1])

    def render(self, display, resolution):
        """Draws the box to the given display.
        Called externally

        :type resolution: tuple[int, int]
        :type display: pygame.Surface
        """

        if resolution != self.resolution:  # Screen resized
            self.update_dimensions(resolution)
            if self.width < 1 or self.height < 1:
                return
            self.wrap()

        if self.width < 1 or self.height < 1:
            return

        # Draw border
        pygame.draw.rect(display, self.border_color,
                         [self.x_coord - self.margin_size[0],
                          self.y_coord - self.margin_size[1],
                          (self.x2 - self.x) * self.resolution[0],
                          (self.y2 - self.y) * self.resolution[1]],
                         self.border_size)

        # Draw scroll_bar
        self.render_scroll_bar(display)

        # Draw Text
        y_offset = 0
        line_num = 0

        self.formatted_lines = []
        for line in self.active_text_lines:
            formatted_line = []
            x_offset = 0
            new_line = self.strip_line(line)

            # Get alignment offset and multiplier based on alignment
            alignment_offset = 0
            alignment_multiplier = 0
            if self.alignment == "left":
                pass  # Default is left already

            elif self.alignment == "right":
                alignment_offset = self.width - self.get_line_width(new_line)

            elif self.alignment == "center":
                alignment_offset = \
                    (self.width - self.get_line_width(new_line)) / 2

            elif self.alignment == "justified":
                current_line_num = line_num + self.scroll_pos
                num_spaces = 0
                if current_line_num in self.justified_lines.keys():
                    new_line, num_spaces = self.justified_lines[
                        current_line_num]

                if len(new_line) > 1:
                    # If multiple words on line, justify. Otherwise, left align
                    if num_spaces != 0:
                        alignment_multiplier = (self.width
                                                - self.get_line_width(
                            new_line)) / num_spaces
            else:
                # Not an alignment option
                print(self.alignment + " must be 'left', 'right', 'center'"
                                       ", or 'justified'. Switching to "
                                       "'left'")
                self.alignment = "left"

            # align and render
            phrase_num = 0
            current_alignment_multiplier = 0
            for phrase in new_line:

                label = phrase.get_label()

                spaced = False
                if phrase.get_text().startswith(" ") \
                        and (phrase_num == 0 or not new_line[
                                phrase_num - 1].get_text().endswith(" ")):
                    current_alignment_multiplier += alignment_multiplier
                    spaced = True  # Space already accounted for

                x = self.x_coord + x_offset + alignment_offset \
                    + current_alignment_multiplier
                y = self.y_coord + y_offset
                display.blit(label, (x, y))

                formatted_line.append(phrase)
                formatted_line[-1].set_x_pos(x)
                formatted_line[-1].set_y_pos(y)

                if phrase.get_text().endswith(" ") and not spaced:
                    current_alignment_multiplier += alignment_multiplier

                x_offset += phrase.get_width()
                phrase_num += 1

            y_offset += self.get_height_of_line(line)
            line_num += 1
            self.formatted_lines.append(formatted_line)
