#!/usr/bin/env python3
# Formatted by black
# import argparse

from LeafSpine import LeafSpine, LeafSpineAgg


def main():
    test_2()


def test_2():

    t = LeafSpineAgg(12, 12, 4)
    print(t)

    new_leaf = t.add_leaf()
    print(f"{new_leaf}:\t{t.get_adj(new_leaf)}")

    new_spine = t.add_spine()
    print(f"{new_spine}:\t{t.get_adj(new_spine)}")

    new_agg = t.add_agg()
    print(f"{new_agg}:\t{t.get_adj(new_agg)}")

    t.show()


def test_1():
    t = LeafSpine(8, 4)

    t.add_leaf()
    t.add_spine()

    print(t)

    new_leaf = t.add_leaf()
    print(f"{new_leaf}:\t{t.get_adj(new_leaf)}")

    new_spine = t.add_spine()
    print(f"{new_spine}:\t{t.get_adj(new_spine)}")

    t.show()


if __name__ == "__main__":
    main()
