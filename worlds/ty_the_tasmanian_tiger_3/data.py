from enum import Enum

class Ty3Level(Enum):
    NewBurramudgee = 0
    Cassopolis = 1
    CinderCanyon = 2
    DeadDingoMarsh = 3
    GoobooGully = 4
    MountBoomBasin = 5
    KakaboomIsland = 6
    SouthernRiversSwamp = 7
    SouthernRiversDesert = 8
    FrozenForest = 9
    BackwoodBlizzard = 10
    WinterWoods = 11

ty3_levels = {
    Ty3Level.NewBurramudgee: "New Burramudgee",
    Ty3Level.BackwoodBlizzard: "Backwood Blizzard",
    Ty3Level.SouthernRiversDesert: "Southern Rivers Desert",
    Ty3Level.SouthernRiversSwamp: "Southern Rivers Swamp",
    Ty3Level.DeadDingoMarsh: "Dead Dingo Marsh",
    Ty3Level.GoobooGully: "Gooboo Gully",
    Ty3Level.KakaboomIsland: "Kaka Boom Island",
    Ty3Level.Cassopolis: "Cassopolis",
    Ty3Level.CinderCanyon: "Cinder Canyon",
    Ty3Level.WinterWoods: "Winter Woods",
    Ty3Level.MountBoomBasin: "Mount Boom Basin",
    Ty3Level.FrozenForest: "Frozen Forest"
}