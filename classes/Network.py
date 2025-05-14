#-*- coding: utf-8 -*-


from classes.Station import Station
from classes.Time import Time
from classes.Connection import Connection


class Network:
    """
    A class to represent a network (modelled as a undirected weighted graph) in the fastest-path-finder tool.
    """
    
    def __init__(self, network_file):
        """
        Initializes a new Network.

        Args:
            network_file (str): the input file that contains the network data.

        Attributes:
            network_file (str): the input file that contains the network data.
            stations (list): an empty list to store the stations.
            connections (dictionary): an empty dictionary to store the connections between stations.
        """

        self._network_file = network_file
        self._stations = []
        self._connections = {}

        self.construct_network_from_file()
    

    def get_stations(self):
        """
        The stations in the current Network instance.

        Returns:
            list: the list of stations in the current Network instance.
        """

        return self._stations
    

    def set_stations(self, stations):
        """
        Sets the stations in the current Network instance.

        Args:
            stations (list): the list of stations in the current Network instance.

        Raises:
            ValueError: If a station already exists in the current Network instance, with the message 
                        'Duplicate station'.
        """

        for station in stations:
            self.add_station(station)


    def get_connections(self):
        """
        The connections in the current Network instance.

        Returns:
            dict: the dictionary of connections in the current Network instance.
        """

        return self._connections


    def set_connections(self, connections):
        """
        Sets the connections in the current Network instance.

        Args:
            connection (Connection): an instance of the Connection class.
        """

        for connection in connections:
            self.add_connection(connection)


    def get_network_file(self):
        """
        The file of the current Network instance.

        Returns:
            str: the file of the current Network instance.
        """
            
        return self._network_file
    
    
    def set_network_file(self, network_file):
        """
        Sets the file of the current Network instance.

        Args:
            network_file (str): the file to set for the current Network instance.
        """

        self._network_file = network_file                 

    
    def add_station(self, station):
        """
        Adds a new station to the current Network instance.

        Args:
            station (Station): the station to be added to the current Network instance.

        Raises:
            ValueError: If a station already exists in the current Network instance, with the message 
                        'Duplicate station'.
        """

        if station in self._stations:
            raise ValueError('Duplicate station')
        else:
            self._stations.append(station)
            self._connections[station] = []


    def add_connection(self, connection):
        """
        Add a connection to the current Network instance.

        Args:
            connection (Connection): an instance of the Connection class to be added to the current Network instance.

        Raise:
            ValueError: if either the source or destination stations is not in the current Network instance, 
                        with the message 'Station not in Network'
        """

        source = connection.get_source()
        destination = connection.get_destination()

        if not(source in self._stations and destination in self._stations):
            raise ValueError('Station not in Network')
        
        self._connections[source].append((destination, connection.get_time()))
        self._connections[destination].append((source, connection.get_time()))


    def stations_items(self):
            """
            Supports iteration over the stations attribute of the current Network instance.

            Yields:
                station (Station): each station in the current Network instance.
            """

            for station in self.get_stations():
                yield station
    

    def connections_items(self):
        """
        Supports iteration over the connections attribute of the current Network instance.
        
        Yields:
            tuple: a 3-element tuple containing:
                - souce_station (Station): the source station of the connection.
                - destination_station  (Station): the destination station of the connection.
                - time (Time): the time associated with the connection.
        """
        
        for source_station, connections in self.get_connections().items():
            for destination_station, time in connections:
                yield source_station, destination_station, time
        

    def children_of(self, station):
        """
        The connections originating from the given station.

        Args:
            station (Station): the station whose outgoing connections are to be retrieved.

        Returns:
            list: the list of connections originating from the given station.

        Raises:
            KeyError: if the given station is not in the current Network instance.
        """
        
        return self.get_connections()[station]

    
    def has_station(self, station):
        """
        Checks whether a given station exists in the current Network instance.

        Args:
            station (Station): the station to check for.

        Returns:
            bool:
                - True if the station exists in the current Network instance.
                - False otherwise.
        """

        return station in self.get_stations()


    def read_network_file(self):
        """
        Opens the .txt file associated with the current Network instance.

        Returns:
            file: an open file object (in read mode with UTF-8 encoding) associated with the current Network instance.
        """
                
        return open(self.get_network_file(), "r", encoding = "utf-8")
    

    def remove_header(self):
        """
        Reads the .txt file associated with the current Network instance, skipping the header lines.

        Returns:
            list: a list of strings, each representing a line of content from the .txt file associated with the
                  current Network instance, with the header lines removed.
        """
        
        lines = self.read_network_file().readlines()
        content = []
        
        for i, line in enumerate(lines, start=1):
            if i > 1:
                content.append(line)
                
        return content
    

    def construct_network_from_file(self):
        """
        Populates the current Network instance from the data contained in the input file.
        """
        
        in_file = self.remove_header()
        station_dict = {}

        for line in in_file:
            line_lst = line.rstrip().split(", ", maxsplit=2)
            name, id = line_lst[1], line_lst[0]

            station = Station(name, id)
            self.add_station(station)
            station_dict[id] = station

        for line in in_file:
            line_lst = line.rstrip().split(", ", maxsplit=2)
            id = line_lst[0]

            source_station = station_dict[id]
            
            new_string = line_lst[2].replace("[(","").replace(")]","").replace("(", "").replace(")", "")
            new_string_lst = new_string.split(', ')

            for i in range(0, len(new_string_lst)-1, 2):
                destination_station_id = new_string_lst[i]
                time = Time(new_string_lst[i+1])

                for station in self.get_stations():
                    if station.get_id() == destination_station_id:
                        destination_station = station
                        self.add_connection(Connection(source_station, destination_station, time))


    def __lt__(self, other_network):
        """
        Compares the current Network instance and another one according to their number of connections.

        Args:
            other_network (Network): another instance of the Network class.
        
        Returns:
            bool:
                - True if the current Network instance should be ordered before other_network.
                - False otherwise.
        """

        return len(self.get_connections()) < len(other_network.get_connections())
    
    
    def __eq__(self, other_network):
        """
        Checks the equality between the current Network instance and another one according to their stations and
        connections attributes.

        Args:
            other_network (Network): another instance of the Network class.

        Returns:
            bool:
                - True if both instances have the same attributes.
                - False otherwise.
        """

        return self.get_stations() == other_network.get_stations() and self.get_connections() == other_network.get_connections()


    def __str__(self):
        """
        The string representation of a Network instance.

        Returns:
            str: the current Network instance as a string.

        Example:
            >>> str(network)
            "A, Caldeirão Verde, [(B, 30), (C, 70), (D, 35)]
             B, Tornos, [(A, 30), (C, 10)]
             C, Barreiro, [(A, 70), (B, 10), (F, 10), (J, 10)]
             D, Nova, [(A, 35), (E, 15), (I, 10)]
             E, Rei, [(D, 15), (H, 5)]"
        """

        result = ''
        
        for source in self.get_stations():
            destination_time_pairs = []
            for destination, time in self.get_connections()[source]:
                destination_time_pairs.append(f"({destination.get_id()}, {time.get_time_string()})")
            
            result += f"{source.get_id()}, {source.get_name()}, [{', '.join(destination_time_pairs)}]\n"

        return result