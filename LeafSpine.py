import networkx as nx
import matplotlib.pyplot as plt


class LeafSpine:
    def __init__(self, n: int, m: int):
        self.nx_g = nx.Graph()
        self.build_leaf_spine_nx(n, m)

    def build_leaf_spine_nx(self, n: int, m: int):
        self.nx_g.add_edges_from(
            [
                (leaf_node, spine_node)
                for leaf_node in [f"l{i}" for i in range(n)]
                for spine_node in [f"s{j}" for j in range(m)]
            ]
        )

    def __str__(self):
        return str(self.nx_g.edges)

    def get_nodes(self, prefix: str):
        return [n for n in self.nx_g.nodes if prefix in n]

    def get_leaves(self):
        return self.get_nodes("l")

    def get_spines(self):
        return self.get_nodes("s")

    def get_adj(self, node: str):
        return [n for (_, n) in self.nx_g.edges(node)]

    def add_leaf(self):
        new_node = f"l{len(self.get_leaves())}"
        for spine_node in self.get_spines():
            self.nx_g.add_edge(new_node, spine_node)
        return new_node

    def add_spine(self):
        new_spine = f"s{len(self.get_spines())}"
        for leaf_node in self.get_leaves():
            self.nx_g.add_edge(leaf_node, new_spine)
        return new_spine

    def show(self):
        nx.draw(self.nx_g, with_labels=True, font_weight="bold")
        plt.draw()
        plt.show()


class LeafSpineAgg(LeafSpine):
    def __init__(self, n: int, m: int, a: int):
        self.nx_g = nx.Graph()
        self.build_leaf_spine_nx(n, m)
        self.nx_g.add_edges_from(
            [
                (spine_node, agg_node)
                for spine_node in self.get_spines()
                for agg_node in [f"a{i}" for i in range(a)]
            ]
        )

    def get_agg(self):
        return self.get_nodes("a")

    def add_spine(self):
        new_spine = f"s{len(self.get_spines())}"
        for leaf_node in self.get_leaves():
            self.nx_g.add_edge(leaf_node, new_spine)
        for agg_node in self.get_agg():
            self.nx_g.add_edge(agg_node, new_spine)
        return new_spine

    def add_agg(self):
        new_agg = f"a{len(self.get_agg())}"
        for spine_node in self.get_spines():
            self.nx_g.add_edge(spine_node, new_agg)
        return new_agg
