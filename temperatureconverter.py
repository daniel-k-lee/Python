"""
File: temperatureconverter.py
Project 8.3
Temperature conversion between Fahrenheit and Celsius.
Illustrates the use of numeric data fields.
"""

from breezypythongui import EasyFrame

class TemperatureConverter(EasyFrame):
    """A termperature conversion program."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Temperature Converter")
        self.addLabel(text = "Celsius",
                      row = 0, column = 0)
        self.celsiusField = self.addFloatField(value = 0.0,
                                              row = 1,
                                              column = 0)
        self.addLabel(text = "Fahrenheit",
                      row = 0, column = 1)
        self.fahrField = self.addFloatField(value = 32.0,
                                           row = 1,
                                           column = 1)

        # The command button
        self.addButton(text = ">>>>", row = 2, column = 0,
                    command = self.computeFahr)
        self.addButton(text = "<<<<", row = 2, column = 1,
                    command = self.computeCelsius)

        # self.addLabel (Label for Celsius)
        # self.celsiusField (Celsius field)
        # self.addLabel (Label for Fahrenheit)
        # self.fahrField (Fahrenheit field)
        # self.addButton (Celsius button)
        # self.addButton (Fahrenheit button)

    # The controller methods
    def computeFahr(self):
        """Inputs the Celsius degrees
        and outputs the Fahrenheit degrees."""
        celsius = self.celsiusField.getNumber()
        fahr = celsius * 9//5 + 32
        self.fahrField.setNumber(fahr)

    def computeCelsius(self):
        """Inputs the Fahrenheit degrees
        and outputs the Celsius degrees."""
        fahr = self.fahrField.getNumber()
        celsius = (fahr - 32)*5/9
        self.celsiusField.setNumber(celsius)
        
def main():
    """Instantiate and pop up the window."""
    TemperatureConverter().mainloop()

if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("\nProgram closed.")

