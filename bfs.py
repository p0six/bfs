#!/usr/bin/env python3
########################################################################################################################
# CPSC 481 - Artificial Intelligence
# Assignment 2 - Progress Checkpoint 1 - BFS
# Authors: Michael Romero, Miles McCloskey, Diego Franchi
# March 23, 2018
########################################################################################################################
# Implement the Breath-First Search algorithm from the textbook, Page 100
import sys


class Tree(object):
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return self.name

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)


def bfs(node, value):
    _open = [node]
    closed = []
    while len(_open):
        print('open = [' + ', '.join(str(t) for t in _open) + ']; closed = [' + ', '.join(str(t) for t in closed) + ']')
        x = _open.pop(0)
        if x.name == value:
            return True
        else:
            closed.insert(0, x)
            children = []
            for child in x.children:
                if child not in closed and child not in _open:
                    children.append(child)
            if len(children) > 0:
                _open = children + _open  # BFS
                # _open = _open + children  # DFS
    return False


def main():
    M = Tree('M')
    N = Tree('N')
    O = Tree('O')
    Q = Tree('Q')
    R = Tree('R')
    S = Tree('S')
    T = Tree('T')
    U = Tree('U')
    K = Tree('K', [S])
    L = Tree('L', [T])
    P = Tree('P', [U])
    E = Tree('E', [K, L])
    F = Tree('F', [L, M])
    G = Tree('G', [N])
    H = Tree('H', [O, P])
    I = Tree('I', [P, Q])
    J = Tree('J', [R])
    B = Tree('B', [E, F])
    C = Tree('C', [G, H])
    D = Tree('D', [I, J])
    A = Tree('A', [B, C, D])

    if bfs(A, 'U'):
        print('Found')
    else:
        print('Not found')


if __name__ == '__main__':
    main()
