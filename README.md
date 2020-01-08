# Dijkstra-map
Mapping shortest cost walk using Dijkstra's algorithm.

The input file gives the number of test cases on the first line, followed by the number of lines for the first case, then the information for each item in that case (latitude, longitude, location name). The final line of the first case denotes the "fuel tank", or maximum distance of a path between two vertices, which is taken into consideration.

The python file reads the input (with consideration to the curvature of the earth) and uses Dijkstra's algorithm to calculate the most cost effective (or "fastest") route. The 'Output' file is the result, which matches the 'Desired output' given.
