#-*- coding: utf-8 -*-


class Connection:
    """
    A class to represent a connection.
    """
    
    def __init__(self, source, destination, time):
        """
        Initializes a new Connection.

        Args:
            source (Station): the source station
            destination (Station): the destination station
            time (Time): the time between the source and destination stations.
        """

        self._source = source
        self._destination = destination
        self._time = time

        
    def get_source(self):
        """
        The source station of the current Connection instance.

        Returns:
            Station: the source station of the current Connection Instance.
        """

        return self._source


    def set_source(self, source):
        """
        Sets the source station of the current Connection instance.

        Args:
            source (Station): the source station to set for the current Connection instance.
        """

        self._source = source
    

    def get_destination(self):
        """
        The destination station of the current Connection instance.
        """
        
        return self._destination


    def set_destination(self, destination):
        """
        Sets the destination station of the current Connection instance.

        Args:
            destination (Station): the destination station to set for the current Connection instance.
        """

        self._destination = destination


    def get_time(self):
        """
        The time between the source and destination stations of the current Connection instance.

        Returns:
            Time: the time between the source and destination stations of the current Connection instance.
        """

        return self._time
    

    def set_time(self, time):
        """
        Sets the time of the current Connection instance.

        Args:
            time (Time): the time to set for the current Connection instance.
        """

        self._time = time
    

    def __lt__(self, other_connection):
        """
        Compares the current Connection instance and another one according to their time.

        Args:
            other_connection (Connection): another instance of the Connection class.

        Returns:
            bool:
                - True if the current Connection instance should be ordered before other_connection.
                - False otherwise.
        """

        return self.get_time() < other_connection.get_time()
        

    def __eq__(self, other_connection):
        """
        Checks the equality between the current Connection instance and another one according to their source and destination
        stations, and time.

        Args:
            other_connection (Connection): another instance of the Connection class.
        
        Returns:
            bool:
                - True if all attributes of both instances are equal
                - False otherwise.
        """
        
        return self.get_source() == other_connection.get_source() and \
            self.get_destination() == other_connection.get_destination() and self.get_time() == other_connection.get_time()


    def __str__(self):
        """
        The string representation of a Connection instance.

        Returns:
            str: the current Connection instance as a string.
        
        Example:
            >>> str(connection)
            "Caldeirão Verde -> Tornos, 30"
        """

        return self.get_source().get_name() + ' -> ' + self.get_destination().get_name() + ', ' + str(self.get_time())