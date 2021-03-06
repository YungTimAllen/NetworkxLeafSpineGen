# Networkx Leaf-Spine-Agg Generator

![Example Topology](https://i.imgur.com/m8pXQXP.png)

```python
    t = LeafSpineAgg(12, 12, 4)
    print(t)

    new_leaf = t.add_leaf()
    print(f"{new_leaf}:\t{t.get_adj(new_leaf)}")

    new_spine = t.add_spine()
    print(f"{new_spine}:\t{t.get_adj(new_spine)}")

    new_agg = t.add_agg()
    print(f"{new_agg}:\t{t.get_adj(new_agg)}")
```

```
[('l0', 's0'), ('l0', 's1'), ('l0', 's2'), ('l0', 's3'), ('l0', 's4'), ('l0', 's5'), ('l0', 's6'), ('l0', 's7'), ('l0', 's8'), ('l0', 's9'), ('l0', 's10'), ('l0', 's11'), ('s0', 'l1'), ('s0', 'l2'), ('s0', 'l3'), ('s0', 'l4'), ('s0', 'l5'), ('s0', 'l6'), ('s0', 'l7'), ('s0', 'l8'), ('s0', 'l9'), ('s0', 'l10'), ('s0', 'l11'), ('s0', 'a0'), ('s0', 'a1'), ('s0', 'a2'), ('s0', 'a3'), ('s1', 'l1'), ('s1', 'l2'), ('s1', 'l3'), ('s1', 'l4'), ('s1', 'l5'), ('s1', 'l6'), ('s1', 'l7'), ('s1', 'l8'), ('s1', 'l9'), ('s1', 'l10'), ('s1', 'l11'), ('s1', 'a0'), ('s1', 'a1'), ('s1', 'a2'), ('s1', 'a3'), ('s2', 'l1'), ('s2', 'l2'), ('s2', 'l3'), ('s2', 'l4'), ('s2', 'l5'), ('s2', 'l6'), ('s2', 'l7'), ('s2', 'l8'), ('s2', 'l9'), ('s2', 'l10'), ('s2', 'l11'), ('s2', 'a0'), ('s2', 'a1'), ('s2', 'a2'), ('s2', 'a3'), ('s3', 'l1'), ('s3', 'l2'), ('s3', 'l3'), ('s3', 'l4'), ('s3', 'l5'), ('s3', 'l6'), ('s3', 'l7'), ('s3', 'l8'), ('s3', 'l9'), ('s3', 'l10'), ('s3', 'l11'), ('s3', 'a0'), ('s3', 'a1'), ('s3', 'a2'), ('s3', 'a3'), ('s4', 'l1'), ('s4', 'l2'), ('s4', 'l3'), ('s4', 'l4'), ('s4', 'l5'), ('s4', 'l6'), ('s4', 'l7'), ('s4', 'l8'), ('s4', 'l9'), ('s4', 'l10'), ('s4', 'l11'), ('s4', 'a0'), ('s4', 'a1'), ('s4', 'a2'), ('s4', 'a3'), ('s5', 'l1'), ('s5', 'l2'), ('s5', 'l3'), ('s5', 'l4'), ('s5', 'l5'), ('s5', 'l6'), ('s5', 'l7'), ('s5', 'l8'), ('s5', 'l9'), ('s5', 'l10'), ('s5', 'l11'), ('s5', 'a0'), ('s5', 'a1'), ('s5', 'a2'), ('s5', 'a3'), ('s6', 'l1'), ('s6', 'l2'), ('s6', 'l3'), ('s6', 'l4'), ('s6', 'l5'), ('s6', 'l6'), ('s6', 'l7'), ('s6', 'l8'), ('s6', 'l9'), ('s6', 'l10'), ('s6', 'l11'), ('s6', 'a0'), ('s6', 'a1'), ('s6', 'a2'), ('s6', 'a3'), ('s7', 'l1'), ('s7', 'l2'), ('s7', 'l3'), ('s7', 'l4'), ('s7', 'l5'), ('s7', 'l6'), ('s7', 'l7'), ('s7', 'l8'), ('s7', 'l9'), ('s7', 'l10'), ('s7', 'l11'), ('s7', 'a0'), ('s7', 'a1'), ('s7', 'a2'), ('s7', 'a3'), ('s8', 'l1'), ('s8', 'l2'), ('s8', 'l3'), ('s8', 'l4'), ('s8', 'l5'), ('s8', 'l6'), ('s8', 'l7'), ('s8', 'l8'), ('s8', 'l9'), ('s8', 'l10'), ('s8', 'l11'), ('s8', 'a0'), ('s8', 'a1'), ('s8', 'a2'), ('s8', 'a3'), ('s9', 'l1'), ('s9', 'l2'), ('s9', 'l3'), ('s9', 'l4'), ('s9', 'l5'), ('s9', 'l6'), ('s9', 'l7'), ('s9', 'l8'), ('s9', 'l9'), ('s9', 'l10'), ('s9', 'l11'), ('s9', 'a0'), ('s9', 'a1'), ('s9', 'a2'), ('s9', 'a3'), ('s10', 'l1'), ('s10', 'l2'), ('s10', 'l3'), ('s10', 'l4'), ('s10', 'l5'), ('s10', 'l6'), ('s10', 'l7'), ('s10', 'l8'), ('s10', 'l9'), ('s10', 'l10'), ('s10', 'l11'), ('s10', 'a0'), ('s10', 'a1'), ('s10', 'a2'), ('s10', 'a3'), ('s11', 'l1'), ('s11', 'l2'), ('s11', 'l3'), ('s11', 'l4'), ('s11', 'l5'), ('s11', 'l6'), ('s11', 'l7'), ('s11', 'l8'), ('s11', 'l9'), ('s11', 'l10'), ('s11', 'l11'), ('s11', 'a0'), ('s11', 'a1'), ('s11', 'a2'), ('s11', 'a3')]
l12:	['s0', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11']
s12:	['l0', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9', 'l10', 'l11', 'l12', 'a0', 'a1', 'a2', 'a3']
a4:	['s0', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12']
```