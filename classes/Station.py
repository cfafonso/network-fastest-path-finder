#-*- coding: utf-8 -*-


class Station:
    """
    A class to represent a station.
    """

    def __init__(self, name, id=None):
        """
        Initializes a new Station.

        Args:
            name (str): the name of the station.
            id (str, optional): the unique identifier of the station. Defaults to None.
        """

        #super().__init__(name)
        self._name = name
        self._id = id
    

    def get_name(self):
        """
        The name of the current Station instance.

        Returns:
            str: the name of the current Station instance.
        """

        return self._name
    

    def set_name(self, name):
        """
        Sets the name of the current Station instance.

        Args:
            name (str): the name to set for the current Station instance.
        """

        self._name = name


    def get_id(self):
        """
        The id of the current Station instance.

        Returns:
            str: the unique identifier of the current Station instance.
        """

        return self._id
    

    def set_id(self, id):
        """
        Sets the id of the current Station instance.

        Args:
            id (str): the unique identifier to set for the current Station instance.
        """

        self._id = id


    def __hash__(self):
        """
        The hash value for the current Station instance based on its id and name attributes, making this object usable
        as a key in dictionaries.

        Returns:
            int: a hash value unique to the current Station instance based on its id and name attributes.
        """

        return hash((self.get_id(), self.get_name()))

    
    def __lt__(self, other_station):
        """
        Compares the current Station instance and another one using lexicographical ordering of their name attribute.

        Args:
            other_station (Station): another instance of the Station class.

        Returns:
            bool:
                - True if the current Station instance should be ordered before other_station.
                - False otherwise.
        """
        
        if self.get_name() < other_station.get_name():
            return True
        else:
            return False
        
    
    def __eq__(self, other_station):
        """
        Checks the equality between the current Station instance and another one according to their hash values.

        Args:
            other_station (Station): another instance of the Station class.

        Returns:
            bool:
                - True if both instances have the same hash values.
                - False otherwise.
        """

        return hash(self) == hash(other_station)


    def __str__(self):
        """
        The string representation of a Station instance.

        Returns:
            str: the current Station instance as a string.
        
        Example:
            >>> str(station)
            "Caldeirão Verde"
        """
    
        return self.get_name()