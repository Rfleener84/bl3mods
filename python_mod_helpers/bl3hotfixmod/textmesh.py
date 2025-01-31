#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2021 Christopher J. Kucera
# <cj@apocalyptech.com>
# <http://apocalyptech.com/contact.php>
#
# This Borderlands 3 Hotfix Mod is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# This Borderlands 3 Hotfix Mod is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this Borderlands 3 Hotfix Mod.  If not, see
# <https://www.gnu.org/licenses/>.
#
# --
#
# The `rotate_points` function was written by StackOverflow user M Oehm,
# and is licensed under CC BY-SA 3.0 - https://creativecommons.org/licenses/by-sa/3.0/

import math
import enum
import statistics

class Point:
    """
    A somewhat badly-named class; is just a placement of a specific mesh at an x,y,z
    coordinate, before any transforms (rotation, scaling, etc) have been performed.
    """

    def __init__(self, mesh_path, x, y, z):
        self.mesh_path = mesh_path
        self.x = x
        self.y = y
        self.z = z

class Letter:
    """
    Info about a single letter
    """

    def __init__(self, letter, width, height, origin_w, origin_h, mesh_override=None):
        """
        `letter` - The letter this object will represent
        `width` - The letter's width (in in-engine units, taken from the StaticMesh object)
        `height` - The letter's width (in in-engine units, taken from the StaticMesh object)
        `origin_w` - The letter's horizontal origin (in in-engine units, taken from the StaticMesh object)
        `origin_h` - The letter's vertical origin (in in-engine units, taken from the StaticMesh object)
        `mesh_override` - If not `None`, this is the string in the object name used to uniquely
            identify this letter.  Used in the Title Card font for things like punctuation.
        """
        self.letter = letter.upper()
        self.width = width
        self.height = height
        self.origin_w = origin_w
        self.origin_h = origin_h
        self.mesh_path = None
        self.mesh_override = mesh_override

        # A couple computed params
        self.w_offset = (self.width/2)+self.origin_w
        self.h_offset = (self.height/2)+self.origin_h

    def set_mesh_path(self, pattern):
        """
        Once we're added into a Font, call this to populate our full object path.
        """
        if self.mesh_override:
            self.mesh_path = pattern.format(self.mesh_override)
        else:
            self.mesh_path = pattern.format(self.letter)

class Font:
    """
    Aggregate info about a specific Font
    """

    def __init__(self, name, obj_pattern, char_spacing, line_spacing, line_z_offset, letters):
        """
        `name` - English description of the font; only used in mod comments.
        `obj_pattern` - Format string to generate the StaticMesh object paths
        `char_spacing` - Extra spacing to put inbetween characters
        `line_spacing` - Extra spacing to put inbetween lines
        `line_z_offset` - How much we need to lower the text so that it's oriented properly
            along the Z axis, in units of line height.  This varies depending on the font
            (just due to how the StaticMesh objects are structured, I guess).  Just determined
            via trial-and-error.
        `letters` - A list of `Letter` objects belonging to this font.
        """
        self.name = name
        self.obj_pattern = obj_pattern
        self.char_spacing = char_spacing
        self.line_spacing = line_spacing
        self.line_z_offset = line_z_offset
        self.letters = {}
        for letter in letters:
            letter.set_mesh_path(obj_pattern)
            self.letters[letter.letter] = letter

        # Compute the width of our "space" char, and also our character-derived line height.
        # We're going to omit any letters which have a mesh_override specified, since those
        # may be special chars like commas, periods, etc.
        relevant_chars = []
        for l in self.letters.values():
            if not l.mesh_override:
                relevant_chars.append(l)
        self.space_width = statistics.geometric_mean([l.width for l in relevant_chars])
        self.line_height = statistics.geometric_mean([l.height for l in relevant_chars])
        #print('Space width: {}'.format(self.space_width))
        #print('Line height: {}'.format(self.line_height))

    def get_line_width(self, text):
        """
        Given some `text`, compute how wide the line will be (including all our
        extra between-char spacing, etc)
        """
        total = 0
        first_in_sequence = True
        for letter in text:
            if letter.upper() in self.letters:
                total += self.letters[letter.upper()].width
                if first_in_sequence:
                    first_in_sequence = False
                else:
                    total += self.char_spacing
            else:
                total += self.space_width
                first_in_sequence = True
        return total

def rotate_points(points, rot_y, rot_z, rot_x):
    """
    Given a list of `Point` objects (in `points`), rotate them around the origin
    by `rot_y`, `rot_z`, and `rot_x` degrees (specified in degrees, not radians).
    Since BL3 (and presumably UE4) considers positive X to be "forward", the order
    of arguments here evaluates to pitch/yaw/roll pretty nicely.

    This code licensed CC BY-SA 3.0 - https://creativecommons.org/licenses/by-sa/3.0/
    Written by StackOverflow user M Oehm at:
    https://stackoverflow.com/questions/34050929/3d-point-rotation-algorithm/34060479#34060479

    Adapted very slightly for my own purposes here.  It'd probably make sense to
    just add in a numpy dependency and use that; I assume that there's probably
    just a single function we could call, in there, to do all this.

    Not really intended to be used by users; just called from my own `inject_text`
    method.
    """
    rot_y = math.radians(rot_y)
    rot_x = math.radians(rot_x)
    rot_z = math.radians(rot_z)

    cosa = math.cos(rot_z)
    sina = math.sin(rot_z)

    cosb = math.cos(rot_y)
    sinb = math.sin(rot_y)

    cosc = math.cos(rot_x)
    sinc = math.sin(rot_x)

    axx = cosa*cosb
    axy = cosa*sinb*sinc - sina*cosc
    axz = cosa*sinb*cosc + sina*sinc

    ayx = sina*cosb
    ayy = sina*sinb*sinc + cosa*cosc
    ayz = sina*sinb*cosc - cosa*sinc

    azx = -sinb
    azy = cosb*sinc
    azz = cosb*cosc

    for point in points:
        px = point.x
        py = point.y
        pz = point.z

        yield (point,
                axx*px + axy*py + axz*pz,
                ayx*px + ayy*py + ayz*pz,
                azx*px + azy*py + azz*pz)

class TextMesh:
    """
    Main class intended as the user-level API.  Mostly just doing this to avoid
    "from foo import *" type situations, or having to type out tons of stuff in
    the import statement.

    Methods/vars provided here:

        `inject_text` - The main method to add a block of StaticMesh text to
            a map.  See the docstrings for what the args mean

        `Align`/`VAlign` - A couple enums used to pass in alignment info to
            `inject_text`, if you want to use alignments other than center/middle.

        `inject_compass` - Given some world coordinates, inject some floating
            text which serves as a compass to let you know what the axes look like.

    Fonts provided (pass these in to `inject_text`):

        `yellowblocks` - Yellow block text, such as seen on the gateway to Ellie's
            scrapyard when you first head to unlock Outrunners in The Droughts.
            Only has letters!  No numbers or punctuation.  These meshes do have
            collision information, so they are climbable and will stop NPC/Player
            movement.

        `titlecard` - Used for the character title cards which introduce the main
            NPCs and Bosses.  These meshes don't have any collision info, so anything
            can just walk right through.  This font is missing the letter "Q", but
            does include some numbers (1, 5, and 8 are missing from those, though).
            Also includes some punctuation: & ( ) . , !
    """

    class Align(enum.Enum):
        """
        Enum to describe horizontal alignments
        """
        CENTER = 1
        LEFT = 2
        RIGHT = 3

        def __str__(self):
            return self.name.capitalize()

    class VAlign(enum.Enum):
        """
        Enum to describe vertical alignments
        """
        MIDDLE = 1
        TOP = 2
        BOTTOM = 3

        def __str__(self):
            return self.name.capitalize()

    # Font 1: Yellow block text
    yellowblocks = Font('Yellow Blocks', '/Game/LevelArt/Environments/_Global/Letters/Meshes/SM_Letter_{}',
            char_spacing=5,
            line_spacing=9,
            line_z_offset=2,
            letters=[
                # Values here are the y + z values in the StaticMesh objects, under ExtendedBounds.(BoxExtent|Origin)
                Letter('A', 51.408050, 99.852646, -25.698353, 49.926346),
                Letter('B', 52.664890, 99.974990, -22.635244, 49.980854),
                Letter('C', 50.975678, 102.010380, -25.486248, 49.984303),
                Letter('D', 48.666516, 99.960006, -24.333258, 49.980003),
                Letter('E', 36.435250, 103.467292, -16.705948, 51.733660),
                Letter('F', 33.876038, 104.168952, -16.721985, 52.084476),
                Letter('G', 48.960976, 104.936120, -24.480488, 49.964710),
                Letter('H', 55.768120, 107.433930, -26.116295, 51.949196),
                Letter('I', 23.795388, 100.061988, -10.601769, 50.031006),
                Letter('J', 51.924220, 105.250610, -21.417486, 49.102474),
                Letter('K', 57.960086, 100.061988, -22.741297, 50.031000),
                Letter('L', 34.975926, 100.062004, -16.361795, 50.031000),
                Letter('M', 73.586944, 103.600472, -35.025703, 50.032330),
                Letter('N', 52.365070, 99.142944, -24.007483, 49.571472),
                Letter('O', 52.158554, 101.402400, -25.558758, 49.972797),
                Letter('P', 53.232220, 108.187960, -24.848257, 52.326210),
                Letter('Q', 57.132748, 118.236428, -27.558954, 42.869305),
                Letter('R', 52.631380, 103.394776, -24.901249, 50.282400),
                Letter('S', 54.432938, 101.428560, -23.022789, 49.959710),
                Letter('T', 43.706780, 102.300270, -10.469986, 51.150116),
                Letter('U', 53.523464, 103.754616, -24.488916, 49.547970),
                Letter('V', 52.194954, 100.016388, -11.717011, 50.008180),
                Letter('W', 86.998986, 105.262116, -25.749828, 50.992580),
                Letter('X', 51.986862, 104.227776, -23.439910, 48.738735),
                Letter('Y', 53.430030, 103.986366, -8.987263, 51.993183),
                Letter('Z', 43.618886, 102.788440, -19.835200, 49.980003),
                ])

    # Font 2: Title Card Text
    titlecard = Font('Character Title Card', '/Game/Cinematics/Props/Characters_TitleCard/Model/Meshes/Countach/SM_Cinematic_Letter_Countach_{}',
            char_spacing=3,
            line_spacing=11,
            line_z_offset=1,
            letters=[
                # Values here are the y + z values in the StaticMesh objects, under ExtendedBounds.(BoxExtent|Origin)
                Letter('0', 39.453506, 62.659370, -0.000008, 0.000008),
                Letter('2', 41.084824, 62.659378, -0.000015, 0.000010),
                Letter('3', 39.453506, 62.659370, -0.000008, 0.000006),
                Letter('4', 37.000000, 62.659374, 0.000015, 0.000004),
                Letter('6', 39.453496, 62.659378, 0.000017, 0.000006),
                Letter('7', 39.932800, 62.659370, 0.000000, 0.000002),
                Letter('9', 39.453520, 62.659378, -0.000015, 0.000004),
                Letter('A', 36.193756, 62.659378, -0.000015, 0.000006),
                Letter('&', 38.790206, 62.659378, 0.000000, 0.000006, 'Ampersand'),
                Letter('B', 41.084870, 62.659370, 0.000015, 0.000004),
                Letter(')', 25.657814, 71.154694, 0.000000, -0.000004, 'BracketClose'),
                Letter('(', 25.799206, 71.154694, -0.000006, -0.000004, 'BracketOpen'),
                Letter('C', 39.453492, 62.659374, 0.000000, 0.000004),
                Letter(',', 14.103134, 19.923439, -0.000015, 0.000000, 'Comma'),
                Letter('D', 41.084840, 62.659378, 0.000000, 0.000004),
                Letter('E', 38.190644, 62.659370, 0.000015, 0.000002),
                Letter('!', 21.028130, 62.659378, -0.000004, 0.000006, 'ExclamationMark'),
                Letter('F', 38.190644, 62.659370, 0.000015, 0.000002),
                Letter('G', 39.453492, 62.659374, 0.000000, -0.000006),
                Letter('H', 42.651550, 62.659378, 0.000000, -0.000004),
                Letter('I', 26.635926, 62.659370, 0.000000, -0.000006),
                Letter('J', 32.029694, 62.659374, -0.000015, -0.000002),
                Letter('K', 44.903138, 62.659374, 0.000038, -0.000002),
                Letter('L', 28.207824, 62.659378, -0.000031, 0.000000),
                Letter('M', 54.460938, 62.659374, -0.000002, -0.000002),
                Letter('N', 42.651550, 62.659374, -0.000002, -0.000002),
                Letter('O', 39.453496, 62.659378, -0.000002, -0.000002),
                Letter('P', 41.084816, 62.659370, 0.000011, -0.000004),
                Letter('.', 11.554688, 9.473438, -0.000008, -0.000007, 'Period'),
                Letter('R', 41.084808, 62.659378, 0.000015, -0.000004),
                Letter('S', 39.453506, 62.659378, 0.000038, -0.000004),
                Letter('T', 34.026550, 62.659370, -0.000031, -0.000008),
                Letter('U', 40.595276, 62.659374, -0.000031, -0.000006),
                Letter('V', 36.278076, 62.659378, 0.000000, -0.000006),
                Letter('W', 53.482788, 62.659374, 0.000000, -0.000008),
                Letter('X', 45.667176, 62.659374, 0.000031, -0.000008),
                Letter('Y', 36.278076, 62.659378, -0.000061, -0.000008),
                Letter('Z', 42.607850, 62.659370, 0.000031, -0.000010),
                ])


    @staticmethod
    def inject_text(mod,
            level,
            text,
            origin,
            font=yellowblocks,
            rotation=(0,0,0),
            scale=1,
            align=Align.CENTER,
            valign=VAlign.MIDDLE,
            quiet=False,
            ):
        """
        Injects the specified text into a level by creating StaticMesh
        objects for each letter in the text.  Makes use of our new method
        for enabling arbitrary StaticMesh objects in any level, to have the
        widest possible range of alphabet meshes to do so.

        `mod` - The active Mod object in which to add our hotfixes

        `level` - The level to add the text to; should be the full path of the
            `*_P` level reference (don't bother with `*_Dynamic` or `*_Combat`, etc)

        `text` - A string or list of strings describing the text to inject into
            the level.

        `origin` - An x,y,z tuple describing where to put the text

        `font` - The Font object to use, which will determine which StaticMeshes
            to reference.  Defaults to our `yellowblocks` font.

        `rotation` - a pitch,yaw,roll tuple describing any rotations on the text,
            specified in degrees (not radians).  You may need to do some
            experimentation to figure out which ones are appropriate.  Positive X
            is considered "forward."

        `scale` - An integer describing the scale.  This does not currently
            support scaling axes individually.

        `align` - Horizontal alignment of the text.  This will also impact how
            the text attaches to its `origin`, and how `rotation` affects the
            text: right-aligned text will have its right side at the `origin`
            point, and rotate around that, whereas left-aligned text will
            have its left side at the `origin`.  Centered text will center
            itself on `origin`.  Values are: `Align.CENTER` (the default),
            `Align.LEFT`, and `Align.RIGHT`.

        `valign` - Vertical alignment of the text.  This only really impacts
            how the text attaches to `origin`, and how `rotation` affects the
            text, much like `align`.  Values are: `VAlign.MIDDLE` (the default), 
            `VAlign.TOP`, and `VAlign.BOTTOM`.

        `quiet` - By default,  this method will also inject some comments before
            the hotfixes, to describe the text that's being hotfixed into the
            mod.  Use Set this to `True` to prevent those comments.
        """

        # Support passing in either a string or list of strings
        if type(text) == str:
            text = [text]

        # Report on what we're doing, assuming we've not been told to shut up
        if not quiet:
            last_bit = level.split('/')[-1]
            mod.comment(f'Injecting text in {last_bit}:')
            mod.comment(f'- Font: {font.name}')
            mod.comment(f'- Alignment: {align}, {valign}')
            mod.comment(f'- Origin: {origin}')
            if rotation != (0, 0, 0):
                mod.comment(f'- Rotation: {rotation}')
            if scale != 1:
                mod.comment(f'- Scale: {scale}')
            mod.comment('- Text:')
            for line in text:
                mod.comment(f'>    {line}')
            mod.newline()

        # Calculate the total size (non-transformed) of the text block
        total_height = (len(text)*font.line_height) + ((len(text)-1)*font.line_spacing)
        total_width = max([font.get_line_width(l) for l in text])

        # Figure out where to center our text, based on alignment
        if align == TextMesh.Align.LEFT:
            start_y = 0
        elif align == TextMesh.Align.RIGHT:
            start_y = total_width
        else:
            start_y = total_width/2

        if valign == TextMesh.VAlign.TOP:
            start_z = -(font.line_height*font.line_z_offset)
        elif valign == TextMesh.VAlign.BOTTOM:
            start_z = total_height-(font.line_height*font.line_z_offset)
        else:
            start_z = (total_height/2)-(font.line_height*font.line_z_offset)

        start = (0, start_y, start_z)

        # Loop through and set up our non-transformed initial state
        points = []
        cur_x, cur_y, cur_z = start
        for line in text:
            line_width = font.get_line_width(line)

            # Align text properly
            if align == TextMesh.Align.LEFT:
                offset = 0
            elif align == TextMesh.Align.RIGHT:
                offset = total_width-line_width
            else:
                offset = (total_width-line_width)/2

            cur_y = start[1] - offset
            first_in_sequence = True
            for letter in line:
                if letter.upper() in font.letters:
                    if first_in_sequence:
                        first_in_sequence = False
                    else:
                        cur_y -= font.char_spacing
                    letter_obj = font.letters[letter.upper()]
                    points.append(Point(letter_obj.mesh_path, cur_x, cur_y-letter_obj.w_offset, cur_z+letter_obj.h_offset))
                    cur_y -= letter_obj.width
                else:
                    cur_y -= font.space_width
                    first_in_sequence = True
            cur_z -= font.line_height
            cur_z -= font.line_spacing

        # Finally, rotate, scale, and move to the correct location
        for point, rotated_x, rotated_y, rotated_z in rotate_points(points, *rotation):
            # TODO: it'd be fun to have a `wobble` parameter, or the like, which the
            # user could specify to have the letters randomly tilt around a little bit.
            # Would want to use a normal distribution for the randomness, which'd mean
            # either introducing a numpy dependency or implementing my own.  Don't feel
            # like doing either at the moment, so ehh.
            mod.mesh_hotfix(level,
                    point.mesh_path,
                    location=(
                        (rotated_x*scale)+origin[0],
                        (rotated_y*scale)+origin[1],
                        (rotated_z*scale)+origin[2],
                        ),
                    rotation=(
                        -rotation[0],
                        rotation[1],
                        -rotation[2],
                        ),
                    scale=(scale, scale, scale),
                    ensure=True,
                    )

        # If we're not quiet, make sure we end with a newline
        if not quiet:
            mod.newline()

    @staticmethod
    def inject_compass(mod, level, origin, quiet=False):
        """
        Given a point `origin` within `level`, injects a "compass" around that point,
        to easily show the player which direction the axes go in.  Will put the necessary
        hotfixes into the active Mod object `mod`.  The text identifiers will be
        "POS X", "NEG X", "POS Y", "NEG Y", "POS Z", and "NEG Z" (if the `origin` point
        is taken from a character's position while they're on the ground, the "NEG Z"
        label will end up under the ground).  If `quiet` is set to `True`, it will be
        passed along to `inject_text` to prevent descriptive comments from being added
        to the mod file.
        """

        distance = 250
        for text, rel_pos, rotation in [
                ('POS X', (distance, 0, 0), (0, 90, 0)),
                ('NEG X', (-distance, 0, 0), (0, -90, 0)),
                ('POS Y', (0, distance, 0), (0, 180, 0)),
                ('NEG Y', (0, -distance, 0), (0, 0, 0)),
                ('POS Z', (0, 0, distance), (0, 0, -90)),
                ('NEG Z', (0, 0, -distance), (0, 0, 90)),
                ]:

            TextMesh.inject_text(mod, level,
                    text,
                    (origin[0]+rel_pos[0], origin[1]+rel_pos[1], origin[2]+rel_pos[2]),
                    rotation=rotation,
                    font=TextMesh.titlecard,
                    quiet=quiet,
                    )
