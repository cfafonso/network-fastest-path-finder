#-*- coding: utf-8 -*-


import os

from classes.Station import Station

from constants import RESULTS_PATH


class Search:
    """
    A class that performs depth-first search on a network of the fastest-path-finder tool.
    """

    def __init__(self, stations_file, network):
        """
        Initializes a new Search.

        Args:
            stations_file (str): the name of the input stations file that contains the stations requests
            network (Network): the network where the depth-first search is to be performed.
        """

        self._stations_file = stations_file
        self._network = network
        self._stations = []
        self._in_network_stations = []
        self._out_of_network_stations = []
        self._search_results = []
        
        self.check_network_stations()


    def get_stations_file(self):
        """
        The stations file name of the current Search instance.

        Returns:
            str: the stations file name of the current Search instance.
        """

        return self._stations_file
        

    def set_stations_file(self, stations_file):
        """
        Sets the stations file name of the current Search instance.

        Args:
            stations_file (str): the stations file name to set for the current Search instance.
        """

        self._stations_file = stations_file

    
    def get_network(self):
        """
        The network of the current Search instance.

        Returns:
            Network: the network of the current Search instance.
        """

        return self._network
    

    def set_network(self, network):
        """
        Sets the network of the current Search instance.

        Args:
            network (Network): the network to set for the current Search instance.
        """

        self._network = network

    
    def get_stations(self):
        """
        The stations of the current Search instance.

        Returns:
            list: the list of stations of the current Search instance.
        """

        return self._stations
    
    
    def set_stations(self, stations):
        """
        Sets the stations of the current Search instance.

        Args:
            stations (list): the list of stations to set for the current Search instance.
        """

        self._stations = stations


    def get_in_network_stations(self):
        """
        The in-network stations of the current Search instance.

        Returns:
            list: the list of in-network stations of the current Search instance.
        """

        return self._in_network_stations
    

    def set_in_network_stations(self, in_network_stations):
        """
        Sets the in-network stations of the current Search instance.

        Args:
            in_network_stations (list): the list of in-network stations to set for the current Search instance.
        """

        self._in_network_stations = in_network_stations

        
    def get_out_of_network_stations(self):
        """
        The out-of-network stations of the current Search instance.

        Returns:
            list: the list of out-of-network stations of the current Search instance.
        """

        return self._out_of_network_stations
    

    def set_out_of_network_stations(self, out_of_network_stations):
        """
        Sets the out-of-network stations of the current Search instance.

        Args:
            out_of_network_stations (list): the list of out-of-network stations to set for the current Search instance.
        """

        self._out_of_network_stations = out_of_network_stations


    def get_search_results(self):
        """
        The results of the current Search instance.

        Returns:
            list: the list of results of the current Search instance.
        """

        return self._search_results
    

    def set_search_results(self, search_results):
        """
        Sets the results of the current Search instance.

        Args:
            search_results (list): the list of results of the current Search instance.
        """

        self._search_results = search_results


    def read_stations_file(self):
        """
        Reads the stations file of the current Search instance.

        Returns:
            list: a list of lists, where each inner list contains two strings representing a pair of stations (source and
                  destination), as specified in each line of the file
        """

        in_file = open(self.get_stations_file(), "r", encoding="utf-8-sig")
        lines = []
        
        for line in in_file:
            start, end = line.rstrip().split(" - ")
            lines.append([start, end])

        return lines
    

    def check_network_stations(self):
        """
        Checks which stations from the stations file are in and out of the network in the current Search instance.
        """

        stations = []
        out_of_network_stations = []
        in_network_stations = []

        station_pairs = self.read_stations_file()

        for station_pair in station_pairs:
            start_station = None
            end_station = None

            for station in self.get_network().stations_items():
                if station.get_name() == station_pair[0]:
                    start_station = station
                    
                if station.get_name() == station_pair[1]:
                    end_station = station

            if start_station is not None and end_station is not None:
                in_network_stations.append([start_station, end_station])
                stations.append([start_station, end_station])
            
            elif start_station is None and end_station is not None:
                out_of_network_stations.append(Station(station_pair[0]))
                stations.append([Station(station_pair[0]), end_station])
            
            elif start_station is not None and end_station is None:
                out_of_network_stations.append(Station(station_pair[1]))
                stations.append([start_station, Station(station_pair[1])])
            
            elif start_station is None and end_station is None:
                out_of_network_stations.append(Station(station_pair[0]))
                out_of_network_stations.append(Station(station_pair[1]))
                stations.append([Station(station_pair[0]), Station(station_pair[1])])
            
        self.set_stations(stations)
        self.set_in_network_stations(in_network_stations)
        self.set_out_of_network_stations(out_of_network_stations)


    def stations_items(self):
        """
        Supports iteration over the stations attribute of the current Search instance.

        Yields:
            list: the list where the first element is the start station and the second element is the end station.
        """

        for station_pair in self.get_stations():
            yield station_pair


    def print_path(self, path):
        """
        The string representation of a path.

        Args:
            path (list): the list of stations representing the given path.

        Returns:
            result (str): the given path as a string, with the time and station names separated by '->'.
        """

        result = ''
        for i in range(len(path)):
            result = result + str(path[i])
            if i != len(path) - 1:
                result = result + '->'
        
        return result
        

    def depth_first_search(self, start, end, path, fastest_paths):
        """
        Performs depth-first search to find the three fastest paths between two stations of the current Search instance

        Args:
            start (Station):
            end (Station): 
            path (list): the list of stations that make a path.
            
        Returns:
            fastest_paths (list): a list of lists, where each inner list corresponds to one of the fastest paths (maximum of 3)
                                  found between the start and end stations.
        """

        if fastest_paths is None:
            fastest_paths = []

        if not path:
            path = [0, start]

        current_time = path[0]
        current_path = path[1:]

        if start == end:
            self.update_fastest_paths(path, fastest_paths)
            return fastest_paths

        if self.is_current_path_longer_than_third_fastest(fastest_paths, current_time):
            return fastest_paths

        for neighbor, time in self.get_network().children_of(start):
            if neighbor not in current_path:
                new_time = current_time + time.get_minutes()
                new_path = [new_time] + current_path + [neighbor]
                fastest_paths = self.depth_first_search(neighbor, end, new_path, fastest_paths)

        return fastest_paths


    def update_fastest_paths(self, path, fastest_paths):
        """
        Updates the collection of fastest paths for the current Search instance.

        Args:
            fastest_paths (list): list of lists where each inner list corresponds to one of the fastest paths found so far
                                  between the source and destination stations.
            path (list): the path to potentially add, where the first element corresponds to the time and the subsequent ones
                         to the stations.
        """

        if len(fastest_paths) < 3:
            fastest_paths.append(path)
        else:
            if path[0] < max(path[0] for path in fastest_paths):
                fastest_paths.remove(max(fastest_paths, key=lambda x: (x[0], -len(x[1:]), x[2])))
                fastest_paths.append(path)

    
    def is_current_path_longer_than_third_fastest(self, fastest_paths, current_time):
        """
        Checks whether the current time of a path is longer than the third fastest path found so far between the start and
        end stations.
        
        Args:
            fastest_paths (list): a list of lists, where each inner list corresponds to one of the fastest paths (up to
                                  three) between the start and end stations.
            current_time (int): the current time of the path.

        Returns:
            bool:
                - True if the current path time is longer than the less fastest path in fastest paths.
                - False otherwise.
        """

        if len(fastest_paths) == 3:
            third_best_path_time = max(fastest_paths, key=lambda x: x[0])[0]
            if current_time >= third_best_path_time:
                return True
        return False


    def sort_fastest_paths(self, fastest_paths):
        """
        Sorts the depth-first search results for the current Search instance, according to the criteria defined in the
        specification of the network-fastest-path-find tool.

        Args:
            fastest_paths (list): a list of lists, where each inner list corresponds to one of the fastest paths (up to
                                  three) between the start and end stations.
        
        Returns:
            list: the sorted list of fastest paths.
        """

        return sorted(fastest_paths, key=lambda x: (x[0], -len(x[1:]), x[2]))


    def search(self):
        """
        Performs depth-first search to find the three fastest paths between the station pairs provided in the stations file
        and present in the network of the current Search instance.
        """
        
        for station_pair in self.get_in_network_stations():
            start = station_pair[0]
            end = station_pair[1]
            
            fastest_paths = self.depth_first_search(start, end, [], None)
            sorted_paths = self.sort_fastest_paths(fastest_paths)

            self._search_results.append(sorted_paths)


    def write_results(self, file, path = RESULTS_PATH):
        """
        Writes the results of the current Search instance.

        Args:
            file (str): the name of the file to where the search results are written to.
            path (str): the path to where the file is written to.
        """

        os.makedirs(path, exist_ok=True)

        in_file = open(os.path.join(path, file), "w", encoding="utf-8-sig")
        in_file.write(str(self))
        in_file.close()


    def __lt__(self, other_search):
        """
        Compares the current Search instance and another one according to the number of their results.

        Args:
            other_search (Search): another instance of the Search class.
        
        Returns:
            bool:
                - True if the current Search instance should be ordered before other_search.
                - False otherwise.
        """

        return len(self.search_results) < len(other_search.search_results)


    def __eq__(self, other_search):
        """
        Checks the equality between the current Search instance and another one according to their stations and results
        attributes.

        Args:
            other_search (Search): another instance of the Search class.

        Returns:
            bool:
                - True if both instances have teh same stations and results attributes.
                - False otherwise.
        """

        return self.get_stations() == other_search.get_stations() and self.search_results == other_search.search_results


    def __str__(self):
        """
        The string representation of a Search instance.

        Returns:
            result (str): the current Search instance as a string.
        """

        result = ""
        for station_pair in self.stations_items():
            
            station_pairs_result = None
            result += '# ' + ' - '.join([str(station) for station in station_pair]) + "\n"

            if station_pair[0] in self.get_out_of_network_stations() and station_pair[1] not in self.get_out_of_network_stations():
                result += f"{station_pair[0]} out of the network\n"
            elif station_pair[1] in self.get_out_of_network_stations() and station_pair[0] not in self.get_out_of_network_stations():
                result += f"{station_pair[1]} out of the network\n"
            elif station_pair[0] in self.get_out_of_network_stations() and station_pair[1] in self.get_out_of_network_stations():
                result += f"{station_pair[0]} and {station_pair[1]} out of the network\n"

            for result_path in self.get_search_results():
                for i in range(len(result_path)):
                    if station_pair[0] == result_path[i][1] and station_pair[1] == result_path[i][-1]:
                        station_pairs_result = ', '.join([str(station) for station in result_path[i]])
                        result += station_pairs_result + "\n"

            if station_pairs_result is None and station_pair[0] not in self.get_out_of_network_stations() \
                                          and station_pair[1] not in self.get_out_of_network_stations():
                result += f"{station_pair[0]} and {station_pair[1]} do not communicate\n"
        
        return result.rstrip()