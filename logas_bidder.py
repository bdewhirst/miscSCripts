import random


class LogasAuction:
    # simulate a lords of gossamer and shadow (TTRPG) auction, with specified virtual bidders plus the player
    def __init__(self, names: list):
        self.names = names  # instead pass list of Bidder objects?
        self.categories = ""
        self.dft_points = 100

    def run_auction(self):
        # effectively the main execution loop
        pass

    def report_result(self):
        # indicate who won each ranking, what the 'rungs' of the ladder are, etc.
        pass


class Bidder:
    def __init__(self, name):
        self.name = name
        self.points = 100
        self.max_bid = 100 - random.choice([25, 35, 50, 60, 75])
        self.fave_attr = random.choice(
            [
                "psyche",
                "psyche",
                "psyche",
                "psyche",
                "psyche",
                "strength",
                "strength",
                "endurance",
                "warfare",
                "warfare",
                "warfare",
            ]
        )  # weighted.

        self.stuff: int = 0
        self.psyche: int = 0
        self.strength: int = 0
        self.endurance: int = 0
        self.warfare: int = 0

    def print_character(self):
        print(self.name, "psyche:", self.psyche, "strength:", self.strenght, "endurance:", self.endurance, "warfare:", self.warfare, "stuff and powers:", (100 - self.points))




if __name__ == "__main__":
    jim = Bidder(name="Jim")
    jane = Bidder(name="Jane")
    semour = Bidder(name="Semour")
    auction = LogasAuction([jim, jane, semour])

    # likely will be an abandoned project, as I've worked out what I intended to here.
    auction.report_result()
