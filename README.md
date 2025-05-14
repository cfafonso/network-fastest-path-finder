# network-fastest-path-finder
This is a command-line tool in object-oriented python that determines the fastest path between two stations in a network. It processes two text files, the first containing the network(s) of stations and the second containing pairs of station names, to produce a new text file containing the three fastest paths (if they exist) between the two input stations. 

This program includes code adapted from Chapter 14 of "Introduction to Computation and Programming Using Python" (3rd edition, 2021) by John V. Guttag. Additional functionality and modifications are original work.


## Prerequisites

- Python 3.x


## Usage

1. Run the tool by using the following command line instruction:  
    python main.py input_file_1.txt input_file_2.txt output_file.txt

  where:
  - input_file_1.txt is a text file such as `my_network.txt` containing information about the network.
  - input_file_2.txt is a text file such as `my_stations_1.txt` or `my_stations_2.txt` containing the pairs of stations (one per line).
  - output_file.txt is the name of a text file such as `my_results_1.txt` or `my_results_2.txt` to which the results are written for each pair of stations in `input_file_2.txt`.

2. The tool will produce one new .txt file, such as `my_results_1.txt` or `my_results_2.txt`, inside the `results` folder.

3. A diagram of the network defined in `my_network.txt` can be found in `network_diagram.png`.


## Specification of the project

### Input

The program receives pairs of station names and a file containing the description of the network, where the "Id" and "Name" fields of a line indicate the identifier and name of a station, whereas the "Connected" field of a line contains the IDs of stations directly connected to the current station, along with the travel time in minutes needed to reach each connected station.

### Output

The tool produces:

- "X out of the network" if X is not part of the network;
- or "X and Y do not commmunicate" if there is no path between X and Y;
- or the shortest travel time in minutes to get from the first station to the second station, followed by the complete sequence of stations in that optimal path (including both the starting and ending stations)

### Rules

- A path between two stations exists either as a direct connection between them or as an indirect connection through a series of intermediate stations.

- For stations X and Y that are directly connected, Y can be reached from X in *N* minutes, where *N* is specified in the line of the `my_network.txt` file that describes station X (or Y).

- When stations X and Y are indirectly connected through other intermediate stations, Y can be reached from X in *N* minutes, where *N* is the sum of all travel times along the entire path - including the time from X to the first intermediate station, between all intermediate stations, and from the last intermediate station to Y.

- When stations X and Y are indirectly connected, there may be multiple possible paths through different intermediate stations. In this case, we want to consider the path that provides the shortest possible travel time from X to Y.

- The direct connections between stations in the network are symmetric, meaning if Y is directly connected to X, then X is also directly connected to Y (even if only one direction is recorded in the network description file).

- Each station must be declared exactly once in the `my_network.txt` file.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Structure

```
network-fastest-path-finder/
├── classes/
    ├── Connection.py
    ├── Network.py
    ├── Search.py
    ├── Station.py
    └── Time.py
├── results/
    ├── my_results_1.txt
    └── my_results_2.txt
├── LICENSE
├── README.md
├── constants.py
├── main.py
├── my_network.txt
├── my_stations_1.txt
├── my_stations_2.txt
└── network_diagram.png
