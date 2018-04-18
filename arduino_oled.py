from . import Arduino 


__author__ = "S.Aoki"
__copyright__ = "Copyright 2018, Shokara"
__email__ = "pynq_support@xilinx.com"


ARDUINO_OLED_PROGRAM = "arduino_oled.bin"
CLEAR_DISPLAY = 0x1
PRINT_STRING = 0x3
DRAW_LINE = 0x5
DRAW_RECT = 0x7


class Arduino_OLED(object):
    """This class controls an OLED Pmod.

    The Pmod OLED (PB 200-222) is 128x32 pixel monochrome organic LED (OLED) 
    panel powered by the Solomon Systech SSD1306.
    
    Attributes
    ----------
    microblaze : Arduino
        Microblaze processor instance used by this module.

    """

    def __init__(self, mb_info):
        """Return a new instance of an OLED object. 
        
        Parameters
        ----------
        mb_info : dict
            A dictionary storing Microblaze information, such as the
            IP name and the reset name.
        text: str
            The text to be displayed after initialization.
            
        """
        self.microblaze = Arduino(mb_info, ARDUINO_OLED_PROGRAM)
            
    def write(self, text, x=0, y=0):
        """Write a new text string on the OLED.

        Parameters
        ----------
        text : str
            The text string to be displayed on the OLED screen.
        x : int
            The x-position of the display.
        y : int
            The y-position of the display.

        Returns
        -------
        None

        """
        if not 0 <= x <= 255:
            raise ValueError("X-position should be in [0, 255]")
        if not 0 <= y <= 255:
            raise ValueError("Y-position should be in [0, 255]")
        if len(text) >= 64:
            raise ValueError("Text too long to be displayed.")

        # First write length, x, y, then write rest of string
        data = [len(text), x, y]
        data += [ord(char) for char in text]
        self.microblaze.write_mailbox(0, data)

        # Finally write the print string command
        self.microblaze.write_blocking_command(PRINT_STRING)

    def draw_line(self, x1, y1, x2, y2):
        """Draw a straight line on the OLED.
        
        Parameters
        ----------
        x1 : int
            The x-position of the starting point.
        y1 : int
            The y-position of the starting point.
        x2 : int
            The x-position of the ending point.
        y2 : int
            The y-position of the ending point.
            
        Returns
        -------
        None
        
        """
        if not 0 <= x1 <= 255:
            raise ValueError("X-position should be in [0, 255]")
        if not 0 <= x2 <= 255:
            raise ValueError("X-position should be in [0, 255]")
        if not 0 <= y1 <= 255:
            raise ValueError("Y-position should be in [0, 255]")
        if not 0 <= y2 <= 255:
            raise ValueError("Y-position should be in [0, 255]")

        self.microblaze.write_mailbox(0, [x1, y1, x2, y2])
        self.microblaze.write_blocking_command(DRAW_LINE)

    def draw_rect(self, x1, y1, x2, y2):
        """Draw a rectangle on the OLED.

        Parameters
        ----------
        x1 : int
            The x-position of the starting point.
        y1 : int
            The y-position of the starting point.
        x2 : int
            The x-position of the ending point.
        y2 : int
            The y-position of the ending point.
            
        Returns
        -------
        None
        
        """
        if not 0 <= x1 <= 255:
            raise ValueError("X-position should be in [0, 255]")
        if not 0 <= x2 <= 255:
            raise ValueError("X-position should be in [0, 255]")
        if not 0 <= y1 <= 255:
            raise ValueError("Y-position should be in [0, 255]")
        if not 0 <= y2 <= 255:
            raise ValueError("Y-position should be in [0, 255]")

        self.microblaze.write_mailbox(0, [x1, y1, x2, y2])
        self.microblaze.write_blocking_command(DRAW_RECT)
