import random


ATTRS = set("psyche", "strength", "endurance", "warfare")


class LogasAuction:
    # run a lords of gossamer and shadow (TTRPG) auction, with specified virtual bidders plus the player
    def __init__(self, names: list):
        self.names = names
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


if __name__ == "__main__":
    auction = LogasAuction(["Jim", "Jane", "Semour"])

    auction.report_result()

"""
'Pen and paper' notes from notional auction









"""
