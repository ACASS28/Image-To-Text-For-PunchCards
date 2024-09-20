import svgwrite
from xml.etree import ElementTree as ET
from numberDraw import draw_numbers

machine_config = {
    "card_width": 142.0,
    "stitches": 24,
    "row_height": 5.0,
    "stitch_width": 4.5,
    "pattern_hole_diameter": 3.5,
    "pattern_hole_xoffset": 19.25,
    "pattern_hole_yoffset": 12.5,
    "clip_hole_diameter": 3.5,
    "clip_hole_xoffset": 6.75,
    "clip_hole_yoffset": 5.0,
    "tractor_hole_diameter": 3.0,
    "tractor_hole_xoffset": 13.5,
    "tractor_hole_yoffset": 2.5,
    "overlapping_rows": 2,
    "overlapping_row_xoffset": 19.25,
    "overlapping_row_yoffset": 2.5,
    "corner_offset": 2.0,
    "force_solid_fill": False,
    "half_hole_at_bottom": False,
    "number_xoffset":9.5,
    "number_yoffset":3.0
}

class Layout:
     def __init__(self, machine_id, stitches, rows, horz_repeat, vert_repeat, is_blank, is_solid_fill, maincolors):
        global machine_config

        self.machine_id = machine_id
        self.card_width = machine_config['card_width']
        self.card_stitches = stitches
        self.maincolors = maincolors
        self.row_height = machine_config['row_height']
        self.stitch_width = machine_config['stitch_width']
        self.pattern_hole_diameter = machine_config['pattern_hole_diameter']
        self.pattern_hole_xoffset = machine_config['pattern_hole_xoffset']
        self.pattern_hole_yoffset = machine_config['pattern_hole_yoffset']
        self.clip_hole_diameter = machine_config['clip_hole_diameter']
        self.clip_hole_xoffset = machine_config['clip_hole_xoffset']
        self.clip_hole_yoffset = machine_config['clip_hole_yoffset']
        self.tractor_hole_diameter = machine_config['tractor_hole_diameter']
        self.tractor_hole_xoffset = machine_config['tractor_hole_xoffset']
        self.tractor_hole_yoffset = machine_config['tractor_hole_yoffset']
        self.overlapping_rows = machine_config['overlapping_rows']
        self.overlapping_row_xoffset = machine_config['overlapping_row_xoffset']
        self.overlapping_row_yoffset = machine_config['overlapping_row_yoffset']
        self.corner_offset = machine_config['corner_offset']
        self.half_hole_at_bottom = machine_config['half_hole_at_bottom']
        self.number_xoffset = machine_config['number_xoffset']
        self.number_yoffset = machine_config['number_yoffset']
        if machine_config['force_solid_fill']:
            self.solid_fill = True
        else:
            self.solid_fill = is_solid_fill

        self.card_rows = rows 
        self.horz_repeat = horz_repeat
        self.vert_repeat = 1
        self.is_blank = is_blank
        self.main_colors = maincolors
        self.card_height = (self.pattern_hole_yoffset * 2) + (((self.card_rows) - 1) * self.row_height)


class PCGenerator:
    def __init__(self, handler, txt_filepath, machine_id, vert_repeat, maincolors,is_blank=False, is_solid_fill=False):
        global machine_config

        self.handler = handler
        self.txt_filepath = txt_filepath
        if is_blank:
            self.data = ['x' * machine_config['stitches']]
        else:
            with open(txt_filepath, 'r') as f:
                self.data = f.readlines()
            self.data = [line.strip() for line in self.data if line.strip()]

        self.layout = Layout(
            machine_id,
            len(self.data[0]),  # Number of stitches per row (length of each line)
            len(self.data),  # Number of rows in the pattern (number of lines)
            int(machine_config['stitches'] / len(self.data[0])),
            vert_repeat,
            is_blank,
            is_solid_fill,
            maincolors)
        
    def get_polygon_y(self,polygon):
        # Get the y-coordinates of the points in the polygon
        points = polygon.points
        y_coords = [point[1] for point in points]  # Extract y-coordinate (the second value in each point)
        return sum(y_coords) / len(y_coords)  # Return the average y-coordinate (centroid)
    
    def generate(self):
        diagram = self.create_card()
        objects = []
        
        # Draw overlapping rows if applicable
        if (self.layout.overlapping_rows and
                self.layout.overlapping_row_xoffset and
                self.layout.overlapping_row_yoffset):
            self.draw_overlapped_lines(diagram, objects)
        
        # Draw clip holes for feeding the punchcard into the machine
        if (self.layout.clip_hole_diameter and
                self.layout.clip_hole_xoffset):
            self.draw_clip_holes(diagram, objects)
        
        # Draw tractor holes for moving the punchcard
        if (self.layout.tractor_hole_diameter and
                self.layout.tractor_hole_xoffset):
            self.draw_tractor_holes(diagram, objects)
        
        self.drawNumbers(diagram, objects)
        
        # Draw the actual pattern for the punch card
        self.draw_pattern(diagram, self.data, objects)

        # Sort objects to optimize cutting order (if applicable)
        sorted_objects = sorted(objects, key=lambda x: (
            float(x.attribs['cy']) if isinstance(x, svgwrite.shapes.Circle) else 
            float(x.attribs['y']) if isinstance(x, svgwrite.shapes.BaseElement) and 'y' in x.attribs else
            float(x.attrib['y']) if isinstance(x, ET.Element) and 'y' in x.attrib else
            self.get_polygon_y(x) if isinstance(x, svgwrite.shapes.Polygon) else 0
        ))

        # Add sorted svgwrite objects to the diagram
        for i in sorted_objects:
            if not isinstance(i, ET.Element):
                diagram.add(i)

        # Manually insert external SVG elements (ET.Element objects)
        raw_svg_content = diagram.tostring()  # Get the SVG string
        for i in sorted_objects:
            if isinstance(i, ET.Element):
                raw_svg_content = raw_svg_content.replace('</svg>', ET.tostring(i).decode('utf-8') + '</svg>')

        return '<?xml version="1.0" encoding="UTF-8" standalone="no"?>{}'.format(raw_svg_content)




    def create_card(self):
        diagram = svgwrite.Drawing(
            "punchcard.svg",
            size=('{0}mm'.format(self.layout.card_width), '{0}mm'.format(self.layout.card_height)),
            viewBox=('0 0 {0} {1}'.format(self.layout.card_width, self.layout.card_height)),
            preserveAspectRatio='none')

        diagram.add(diagram.polygon(
            points=self.get_card_shape(),
            fill='white',
            stroke='black',
            stroke_width=.1))

        return diagram
    
    def draw_overlapped_lines(self, diagram, objects):

		# overlapping rows at top
        yoffset = self.layout.overlapping_row_yoffset
        for rows in range(self.layout.overlapping_rows):
            xoffset = self.layout.overlapping_row_xoffset
            for stitch_repeat in range(self.layout.horz_repeat):
                for stitches in range(self.layout.card_stitches):
                    objects.append(diagram.circle(
                        center=(xoffset, yoffset),
                        fill='white',
                        r = (self.layout.pattern_hole_diameter / 2),
                        stroke='black',
                        stroke_width=.1))
                    xoffset += self.layout.stitch_width
            yoffset += self.layout.row_height

        # overlapping rows at bottom
        yoffset = self.layout.card_height - self.layout.overlapping_row_yoffset
        for rows in range(self.layout.overlapping_rows):
            xoffset = self.layout.overlapping_row_xoffset
            for stitch_repeat in range(self.layout.horz_repeat):
                for stitches in range(self.layout.card_stitches):
                    objects.append(diagram.circle(
                        center=(xoffset, yoffset),
                        fill='white',
                        r = (self.layout.pattern_hole_diameter / 2),
                        stroke='black',
                        stroke_width=.1))
                    xoffset += self.layout.stitch_width
            yoffset -= self.layout.row_height   
    
    def draw_clip_holes(self, diagram, objects):
    # Draw clip holes on both sides of the punchcard
        self.draw_side_holes(
            diagram,
            objects,
            self.layout.clip_hole_xoffset,
            self.layout.clip_hole_yoffset,
            self.layout.clip_hole_diameter,
            True)

    def draw_tractor_holes(self, diagram, objects):
        # Draw tractor holes on both sides of the punchcard
        self.draw_side_holes(
            diagram,
            objects,
            self.layout.tractor_hole_xoffset,
            self.layout.tractor_hole_yoffset,
            self.layout.tractor_hole_diameter,
            False)

    # 
    def add_existing_element(self,right_xoffset,yoffset,objects):
        tree = ET.parse('number1.svg')  # Replace with your premade SVG file path
        root = tree.getroot()
        scale_factor = .02
    

        for element in root:
        # Check if the element has 'x' and 'y' attributes (like 'rect', 'image', etc.)
            if 'x' in element.attrib and 'y' in element.attrib:
                element.set('x', str(right_xoffset))  # Adjust X coordinate
                element.set('y', str(yoffset))        # Adjust Y coordinate

        current_transform = element.get('transform', '')
        new_transform = f'scale({scale_factor})'
        if current_transform:
            new_transform = f'{current_transform} {new_transform}'
        element.set('transform', new_transform)
        objects.append(root)
    
    def draw_side_holes(self, diagram, objects, xoffset, yoffset, diameter,clipHoles):


        left_xoffset = xoffset
        right_xoffset = self.layout.card_width - left_xoffset

          # Starting row number, adjust this as needed
        if(clipHoles):
            row_number = 1
            while yoffset <= self.layout.card_height:
                # Holes on the left side (still circles)
                if(row_number == 1 or row_number == 3 or row_number == self.layout.card_rows+3 or row_number == self.layout.card_rows+1):
                    objects.append(diagram.circle(
                        center=(left_xoffset, yoffset),
                        fill='white',
                        r=(diameter / 2),
                        stroke='black',
                        stroke_width=.1))
                        # Holes on the right side
                    objects.append(diagram.circle(
                        center=(right_xoffset, yoffset),
                        fill='white',
                        r=(diameter / 2),
                        stroke='black',
                        stroke_width=.1))
                # Increment y position to move to the next hole
                yoffset += self.layout.row_height
                row_number +=1

                # Stop if the yoffset exceeds the card height, unless we want half holes at the bottom
                if yoffset >= self.layout.card_height and not self.layout.half_hole_at_bottom:
                    break
        else:
            while yoffset <= self.layout.card_height:
            # Holes on the left side (still circles)
                objects.append(diagram.circle(
                    center=(left_xoffset, yoffset),
                    fill='white',
                    r=(diameter / 2),
                    stroke='black',
                    stroke_width=.1))
                    # Holes on the right side
                objects.append(diagram.circle(
                    center=(right_xoffset, yoffset),
                    fill='white',
                    r=(diameter / 2),
                    stroke='black',
                    stroke_width=.1))


                # Increment y position to move to the next hole
                yoffset += self.layout.row_height

                # Stop if the yoffset exceeds the card height, unless we want half holes at the bottom
                if yoffset >= self.layout.card_height and not self.layout.half_hole_at_bottom:
                    break

    def drawNumbers(self, diagram, objects):
        startLineReached = False
        xoffset = self.layout.number_xoffset
        yoffset = self.layout.number_yoffset
        left_xoffset = xoffset
        right_xoffset = self.layout.card_width - left_xoffset
        diameter = 3.5
        symbolList = self.layout.main_colors[::-1]
        symbolNumber = 4
        row_number = self.layout.card_rows-3  # Starting row number, adjust this as needed
        numberOffset = diameter/2
        while yoffset <= self.layout.card_height:
            if(row_number == 0):
                row_number = self.layout.card_rows
                startLineReached = True
            if(row_number == self.layout.card_rows-3 and startLineReached):
                break
            
            draw_numbers(row_number,right_xoffset,left_xoffset,yoffset,objects,diagram)
            print(self.layout.vert_repeat)
            if symbolNumber == self.layout.card_rows:
                symbolNumber = 0
            #print(symbolNumber)
            currentColor = self.layout.main_colors[symbolNumber]
            
            if(currentColor == 1):
                objects.append(diagram.rect(
                    insert=(left_xoffset - diameter / 2, yoffset - diameter / 2),  # Top-left corner of the square
                    size=(diameter, diameter),  # Width and height (same for a square)
                    fill='white',  # Fill color for the square
                    stroke='black',  # Outline (stroke) color
                    stroke_width=.1  # Outline (stroke) width
))
            if(currentColor == 2):
                objects.append(diagram.polygon(
                    points=[
                        (left_xoffset, yoffset - diameter / 2),  # Top vertex
                        (left_xoffset - diameter / 2, yoffset + diameter / 2),  # Bottom-left vertex
                        (left_xoffset + diameter / 2, yoffset + diameter / 2)  # Bottom-right vertex
                    ],
                    fill='white',  # Fill color for the triangle
                    stroke='black',  # Outline (stroke) color
                    stroke_width=.1  # Outline (stroke) width
                ))
            row_number -= 1
            symbolNumber +=1
            yoffset += self.layout.row_height
            if yoffset >= self.layout.card_height and not self.layout.half_hole_at_bottom:
                break


    def draw_pattern(self, diagram, lines, objects):
        fill = 'black' if self.layout.solid_fill else 'white'

        yoffset = self.layout.pattern_hole_yoffset
        for row_repeat in range(self.layout.vert_repeat):
            for rows in range(self.layout.card_rows):
                xoffset = self.layout.pattern_hole_xoffset
                for stitch_repeat in range(self.layout.horz_repeat):
                    for stitches in range(self.layout.card_stitches):
                        if lines[rows][stitches] == 'x':
                            objects.append(diagram.circle(
                                center=(xoffset, yoffset),
                                fill=fill,
                                r=(self.layout.pattern_hole_diameter / 2),
                                stroke='black',
                                stroke_width=.1))
                        xoffset += self.layout.stitch_width
                yoffset += self.layout.row_height

    def get_card_shape(self):
        corner_diameter = self.layout.corner_offset + 1

        a = (corner_diameter, 0)
        b = (self.layout.card_width - corner_diameter, 0)
        c = (self.layout.card_width - self.layout.corner_offset, 1)
        d = (self.layout.card_width - self.layout.corner_offset, 20)
        e = (self.layout.card_width, 22)
        f = (self.layout.card_width, self.layout.card_height - 22)
        g = (self.layout.card_width - self.layout.corner_offset, self.layout.card_height - 20)
        h = (self.layout.card_width - self.layout.corner_offset, self.layout.card_height - 1)
        i = (self.layout.card_width - corner_diameter, self.layout.card_height)
        j = (corner_diameter, self.layout.card_height)
        k = (self.layout.corner_offset, self.layout.card_height - 1)
        l = (self.layout.corner_offset, self.layout.card_height - 20)
        m = (0, self.layout.card_height - 22)
        n = (0, 22)
        o = (self.layout.corner_offset, 20)
        p = (self.layout.corner_offset, 1)

        # Returning the list of points to create the card shape
        return [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p]
       

