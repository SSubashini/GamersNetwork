__author__ = 'Subashini Shanmugadas'
# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #
#
# For students who have subscribed to the course,
# please read the submission instructions in the Instructor Notes below.
# -----------------------------------------------------------------------------

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know
# what they are doing, having taken our web development class). However, it is
# up to you to create a data structure that manages the game-network information
# and to define several procedures that operate on the network.
#
# In a website, the data is stored in a database. In our case, however, all the
# information comes in a big string of text. Each pair of sentences in the text
# is formatted as follows:
#
# <user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.
#
# For example:
#
# John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
#
# Note that each sentence will be separated from the next by only a period. There will
# not be whitespace or new lines between sentences.
#
# Your friend records the information in that string based on user activity on
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two (e.g. lists of dictionaries). Pick one that
# will allow you to manage the data above and implement the procedures below.
#
# You may assume that <user> is a unique identifier for a user. For example, there
# can be at most one 'John' in the network. Furthermore, connections are not
# symmetric - if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is
# connected to 'Bob'.
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged
# to define any additional helper procedures that can assist you in accomplishing
# a task. You are encouraged to test your code by using print statements and the
# Test Run button.
# -----------------------------------------------------------------------------

# Example string input. Use it to test your code.
example_input = "John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

# -----------------------------------------------------------------------------
# create_data_structure(string_input):
#   Parses a block of text (such as the one above) and stores relevant
#   information into a data structure. You are free to choose and design any
#   data structure you would like to use to manage the information.
#
# Arguments:
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not
#   list B's connections or liked games.
#
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.
#
# Return:
#   The newly created network data structure


def create_data_structure(string_input):
    network = {};

    if(string_input != ""):
        # initialize string constants/patterns to look for to build the network
        str_connected_to = " is connected to ";
        str_likes_games = " likes to play ";

        # Split up the input string at the specified delimiter to extract the connection
        # and the games string separately.
        data_array = string_input.split(".");
        # add all users to the network
        network = add_users_to_network(data_array, network, str_likes_games);

        # add all users' connections.
        network = add_connections(data_array, network, str_connected_to);

    return network;

# MYOP - Helper function for the create_data_structure procedure
# -----------------------------------------------------------------------------
# add_users_to_network(data_array, network, str_likes_games_pattern):
#   Returns the network with the users from the data_array added to the network
#
# Arguments:
#   network: the gamer network data structure
#   data_array:    array of data containing information about the user's connections and games liked e.g.:
#                 ['John is connected to Bryant, Debra, Walter',
#                  'John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner',
#                  'Bryant is connected to Olive, Ollie, Freda, Mercedes',
#                  'Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man',...
#                 ]
#   str_likes_games_pattern: " likes to play "
# Return:
#   The updated network with the new user and game preferences added.
def add_users_to_network(data_array, network, str_likes_games_pattern):
    for i in range(1, len(data_array), 2):
        # extract the games user likes to play, the second string
        likes_to_play_str = data_array[i];
        likes_games_start_index = likes_to_play_str.find(str_likes_games_pattern);
        likes_games_end_index = likes_to_play_str.find(str_likes_games_pattern) + len(str_likes_games_pattern);
        user_key = likes_to_play_str[0:likes_games_start_index];
        games_str = likes_to_play_str[likes_games_end_index:];
        games = [game.strip() for game in (games_str.split(","))]
        # add the games the user likes to the network
        add_new_user(network, user_key, games);
    return network;


# MYOP - Helper function for the create_data_structure procedure
# -----------------------------------------------------------------------------
# add_connections(data_array, network, str_connected_to_pattern):
#   Returns the network with the users from the data_array added to the network
#
# Arguments:
#   network: the gamer network data structure
#   data_array:    array of data containing information about the user's connections and games liked e.g.:
#                 ['John is connected to Bryant, Debra, Walter',
#                  'John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner',
#                  'Bryant is connected to Olive, Ollie, Freda, Mercedes',
#                  'Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man',...
#                 ]
#   str_connected_to_pattern: " is connected to "
# Return:
#   The updated network with the new user and respective connections added.
def add_connections(data_array, network, str_connected_to_pattern):
    for i in range(0, (len(data_array) - 1), 2):
        # extract user's connections first as the first sentence contains the connections
        is_connected_to_str = data_array[i];
        is_conn_to_start_index = is_connected_to_str.find(str_connected_to_pattern);
        is_conn_to_end_index = is_connected_to_str.find(str_connected_to_pattern) + len(str_connected_to_pattern);
        user_key = (is_connected_to_str[0:is_conn_to_start_index]).strip();
        connections = is_connected_to_str[is_conn_to_end_index:];
        # print("%s user_key %s connections" % (user_key, connections));
        connections_arr = connections.split(",");
        for user in connections_arr:
            add_connection(network, user_key, user.strip());

    return network;


# ----------------------------------------------------------------------------- #
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        #
# ----------------------------------------------------------------------------- #

# -----------------------------------------------------------------------------
# get_connections(network, user):
#   Returns a list of all the connections that user has
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return:
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.
def get_connections(network, user):
    if (network.has_key(user)):
        return network[user]['connections'];

    return None;


# -----------------------------------------------------------------------------
# get_games_liked(network, user):
#   Returns a list of all the games a user likes
#
# Arguments: is connected to
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return:
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.
def get_games_liked(network, user):
    if (network.has_key(user)):
        return network[user]['games'];

    return None;


# -----------------------------------------------------------------------------
# add_connection(network, user_A, user_B):
#   Adds a connection from user_A to user_B. Make sure to check that both users
#   exist in network.
#
# Arguments:
#   network: the gamer network data structure
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return:
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.
def add_connection(network, user_A, user_B):
    if (network.has_key(user_A) and network.has_key(user_B)):
        data = network.get(user_A);
        if (not data.has_key('connections')):
            data['connections'] = [];
        if (user_B not in data['connections']):
            data['connections'].append(user_B);
        return network;
    else:
        return False;


# -----------------------------------------------------------------------------
# add_new_user(network, user, games):
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no
#   connections to begin with.
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return:
#   The updated network with the new user and game preferences added. The new user
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)
def add_new_user(network, user, games):
    data = {};
    if not network.has_key(user):
        data['games'] = games;
        network[user] = data;

    return network


# -----------------------------------------------------------------------------
# get_secondary_connections(network, user):
#   Finds all the secondary connections (i.e. connections of connections) of a
#   given user.
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return:
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
#
# NOTE:
#   It is OK if a user's list of secondary connections includes the user
#   himself/herself. It is also OK if the list contains a user's primary
#   connection that is a secondary connection as well.
def get_secondary_connections(network, user):
    user_vertices = {};
    secondary_conns = [];
    for user_key in network.iterkeys():
        user_vertex_data = {};
        user_vertex_data['marked'] = False;
        user_vertex_data['distTo'] = 0;
        user_vertex_data['edgeTo'] = None;
        user_vertices[user_key] = user_vertex_data;

    bf_user_vertices = breadth_first_search(user_vertices, network, user);

    for user in bf_user_vertices:
        if (bf_user_vertices[user]['distTo'] == 2):
            secondary_conns.append(user);
    return secondary_conns;


# -----------------------------------------------------------------------------
# get_secondary_connections(network, user):
#   Finds all the secondary connections (i.e. connections of connections) of a
#   given user.
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return:
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
#
# NOTE:
#   It is OK if a user's list of secondary connections includes the user
#   himself/herself. It is also OK if the list contains a user's primary
#   connection that is a secondary connection as well.
def breadth_first_search(user_vertices, network, user):
    queue = [];
    user_data = user_vertices[user];
    user_data['marked'] = True;
    user_vertices[user] = user_data;
    queue.append(user);
    while len(queue) != 0:
        curr_user = queue[0];
        queue.remove(curr_user);
        curr_user_conns = network[curr_user]['connections'];
        for user_conn in curr_user_conns:
            if (user_vertices[user_conn]['marked'] == False):
                user_vertices[user_conn]['edgeTo'] = curr_user;
                dist = user_vertices[curr_user]['distTo'];
                user_vertices[user_conn]['distTo'] = dist + 1;
                user_vertices[user_conn]['marked'] = True;
                queue.append(user_conn);

    return user_vertices;


# -----------------------------------------------------------------------------
# connections_in_common(network, user_A, user_B):
#   Finds the number of people that user_A and user_B have in common.
#
# Arguments:
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return:
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.
def connections_in_common(network, user_A, user_B):
    if (network.has_key(user_A) and network.has_key(user_B)):
        conn_A = network[user_A]['connections'];
        conn_B = network[user_B]['connections'];
        res = set(conn_A).intersection(conn_B);
        return len(res);
    else:
        return False;


# -----------------------------------------------------------------------------
# path_to_friend(network, user_A, user_B):
#   Finds a connections path from user_A to user_B. It has to be an existing
#   path but it DOES NOT have to be the shortest path.
#
# Arguments:
#   network: The network you created with create_data_structure.
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
#
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam,
#   who is connected with Zed.
#
# NOTE:
#   You must solve this problem using recursion!
#
# Hints:
# - Be careful how you handle connection loops, for example, A is connected to B.
#   B is connected to C. C is connected to B. Make sure your code terminates in
#   that case.
# - If you are comfortable with default parameters, you might consider using one
#   in this procedure to keep track of nodes already visited in your search. You
#   may safely add default parameters since all calls used in the grading script
#   will only include the arguments network, user_A, and user_B.


def path_to_friend(network, user_A, user_B):
    path_to_friend_stack = [];
    build_depth_first_paths(network, user_A);
    if ((network.has_key(user_A) and network.has_key(user_B)) and
            (network[user_B]['hasPathTo'] == True)):
        while(user_A != user_B):
            path_to_friend_stack.insert(0, user_B);
            user_B = network[user_B]['edgeTo'];
        path_to_friend_stack.insert(0, user_A);
    else:
        return None;

    return path_to_friend_stack;


# Make-Your-Own-Procedure (MYOP)
# -----------------------------------------------------------------------------
# Your MYOP should either perform some manipulation of your network data
# structure (like add_new_user) or it should perform some valuable analysis of
# your network (like path_to_friend). Don't forget to comment your MYOP. You
# may give this procedure any name you want.

# Replace this with your own procedure! You can also uncomment the lines below
# to see how your code behaves. Have fun!



###############################################################################
# -----------------------------------------------------------------------------
# build_depth_first_paths(network, user_A):
#   Analyses the given network starting from the vertex - user_A
# Arguments:
#   network: the gamer network data structure
#   user_A:  a string containing the origin vertex to begin the search
#
# Return:
#   An updated network with the following information:
#   network[user]['marked'] - if True, then the vertex has been visited
#                              while following the connections from the source
#   network[user]['edgeTo'] - used to trace the path. A value other than None
#                             signifies the origin from which this vertex was
#                             visited;
#   network[user]['hasPathTo'] - True/False - if True indicates that this vertex is reachable
#                                from the source vertex, user_A;
def build_depth_first_paths(network, user_A):
    for user in network:
        network[user]['marked'] = False;
        network[user]['edgeTo'] = None;
        network[user]['hasPathTo'] = False;

    depth_first_search(network, user_A);


# -----------------------------------------------------------------------------
# depth_first_search(network, user_A):
#   Recursive procedure that visits every unvisited vertex from the source, user_A
#
# Arguments:
#   network: the gamer network data structure
#   user_A:  a string containing the origin vertex to begin the search
#
# Return:
#   An updated network with the following information:
#   network[user]['marked'] - if True, then the vertex has been visited
#                              while following the connections from the source
#   network[user]['edgeTo'] - used to trace the path. A value other than None
#                             signifies the origin from which this vertex was
#                             visited;
#   network[user]['hasPathTo'] - True/False - if True indicates that this vertex is reachable
#                                from the source vertex, user_A;
def depth_first_search(network, user_A):
    network[user_A]['marked'] = True;
    for user in network[user_A]['connections']:
        if(network[user]['marked'] == False):
            network[user]['marked'] == True;
            network[user]['edgeTo'] = user_A;
            network[user]['hasPathTo'] = True;
            depth_first_search(network, user);


net = create_data_structure(example_input)
print net
print get_connections(net, "Debra")
print get_connections(net, "Mercedes")
print get_games_liked(net, "John")
print add_connection(net, "John", "Freda")
print add_new_user(net, "Debra", [])
print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"])  # True
print get_secondary_connections(net, "Mercedes")
print connections_in_common(net, "Mercedes", "John")
print path_to_friend(net, "John", "Ollie")
print get_games_liked(net, "Nick")