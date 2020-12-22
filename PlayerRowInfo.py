class PlayerRowInfo:
    """
    A class used to represent the given player data from the
    Basketball Monster player ranking table.

    """

    def __init__(self,
                 name: str,
                 rank: str,
                 value: str,
                 position: str,
                 team: str,
                 injury: str,
                 games_played: str,
                 minutes_per_game: str,
                 points_per_game: str,
                 three_pointers_per_game: str,
                 rebounds_per_game: str,
                 assists_per_game: str,
                 steals_per_game: str,
                 blocks_per_game: str,
                 field_goal_shooting_percent: str,
                 field_goal_attempts_per_game: str,
                 free_throw_shooting_percent: str,
                 free_throw_attempts_per_game: str,
                 turnovers_per_game: str,
                 points_value: str,
                 three_point_value: str,
                 rebounds_value: str,
                 assists_value: str,
                 steals_value: str,
                 blocks_value: str,
                 field_goal_shooting_percent_value: str,
                 free_throw_shooting_percent_value: str,
                 turnover_value: str
                 ):
        """
        Parameters
        ----------
        name : str
            The name of the player.
        rank: str
            The rank according the Basketball Monster system
        value: str
            The value rating given by Basketball Monster
        position: str
            The position(s) the given player is eligible for
        team: str
            The team the player belongs to
        injury: str
            Any injury information for the given player if they are currently injured, blank otherwise
        games_played: str
            The number of games the player has played so far this season
        minutes_per_game: str
            The number of minutes the player is averaging per game this season
        points_per_game: str
            The number of points the player is averaging per game this season
        three_pointers_per_game: str
            The number of three pointers the player takes per game this season
        rebounds_per_game: str
            The number of rebounds the player averages per game this season
        assists_per_game: str
            The number of assists the player averages per game this season
        steals_per_game: str
            The number of steals the player averages epr game this season
        blocks_per_game: str
            The number of blocks the player averages per game this season
        field_goal_shooting_percent: str
            The

        """
        self.name = name
        self.rank = rank
        self.value = value
        self.position = position
        self.team = team
        self.injury = injury
        self.games_played = games_played
        self.minutes_per_game = minutes_per_game
        self.points_per_game = points_per_game
        self.three_pointers_per_game = three_pointers_per_game
        self.rebounds_per_game = rebounds_per_game
        self.assists_per_game = assists_per_game
        self.steals_per_game = steals_per_game
        self.blocks_per_game = blocks_per_game
        self.field_goal_shooting_percent = field_goal_shooting_percent
        self.field_goal_attempts_per_game = field_goal_attempts_per_game
        self.free_throw_shooting_percent = free_throw_shooting_percent
        self.free_throw_attempts_per_game = free_throw_attempts_per_game
        self.turnovers_per_game = turnovers_per_game
        self.points_value = points_value
        self.three_point_value = three_point_value
        self.rebounds_value = rebounds_value
        self.assists_value = assists_value
        self.steals_value = steals_value
        self.blocks_value = blocks_value
        self.field_goal_shooting_percent_value = field_goal_shooting_percent_value
        self.free_throw_shooting_percent_value = free_throw_shooting_percent_value
        self.turnover_value = turnover_value
