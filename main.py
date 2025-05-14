#-*- coding: utf-8 -*-


from classes.Search import Search
from classes.Network import Network
from sys import argv

from constants import NETWORK_FILE_INDEX, STATIONS_FILE_INDEX, RESULTS_FILE_INDEX


def find(network_file, stations_file, results_file):
    """
    Creates a network from the provided network file, executes a search operation using the stations file, and
    writes the results to the specified output file.

    Args:
        network_file (str): the file name containing the network data.
        stations_file (str): the file name containing the stations data.
        results_file (str): the file name where search results will be written.
    """
    
    network = Network(network_file)

    dfs_searcher = Search(stations_file, network)
    dfs_searcher.search()
    dfs_searcher.write_results(results_file)


find(argv[NETWORK_FILE_INDEX], argv[STATIONS_FILE_INDEX], argv[RESULTS_FILE_INDEX])