#-*- coding: utf-8 -*-


class Time:
    """
    A class to represent a time.
    """
    
    def __init__(self, time_string, minutes = None):
        """
        Initializes a new Time.

        Args:
            time_string (str): minutes component of the time as a string.
            minutes (int, optional): minutes component of the time as an integer. Defaults to None.
        
        Note:
        If the minutes attribute is not provided, the convert_string_to_int method is called to 
        populate it based on the time_string attribute.
        """
        
        self._time_string = time_string
        self._minutes = minutes

        self.convert_string_to_int()


    def get_time_string(self):
        """
        The string representation with the format "HhM" of the current Time instance.

        Returns:
            str: the string representation with the format "HhM" of the current Time instance.
        """
        
        return self._time_string
    

    def set_time_string(self, time_string):
        """
        Sets the string representation of the current Time instance.
        
        Args:
            time_string (str): the string representation with the format "HhM" to set for the current Time instance.
        """
        
        self._time_string = time_string


    def get_minutes(self):
        """
        The minutes of the current Time instance.

        Returns:
            int: the minutes of the current Time instance.
        """
        
        return self._minutes
    

    def set_minutes(self, minutes):
        """
        Sets the minutes of the current Time instance.

        Args:
            minutes (int): the minutes to set for the current Time instance.
        """
        
        self._minutes = minutes
    

    def convert_string_to_int(self):
        """
        Uses the time_string attribute of the current Time instance to set its minutes attribute.
        """
    
        self.set_minutes(int(self.get_time_string()))
    

    def convert_int_to_string(self):
        """
        Uses the minutes attribute of the current Time instance to set its time_string attribute
        """
        
        self.set_time_string(str(self.get_minutes()))
    

    def __lt__(self, other_time):
        """
        Compares the current Time instance and another one based on their minutes attribute.

        Args:
            other_time (int): another instance of the Time class.
        
        Returns:
            bool:
                - True of the current Time instance occurs before other_time
                - False otherwise.
        """

        return self.get_minutes() < other_time.get_minutes()


    def __eq__(self, other_time):
        """
        Checks the equality between the current Time instance and another one based on their minutes attribute.

        Args:
            other_time (Time): another instance of the Time class.

        Returns:
            bool:
                - True if the minutes attribute of both instances is equal.
                - False otherwise.
        """

        return self.get_minutes() == other_time.get_minutes()
        
    
    def __str__(self):
        """
        The string representation of the current Time instance.

        Returns:
            str: the current Time instance as a string.
        
        Example:
            >>> str(time)
            "30"
        """

        return self.get_time_string()