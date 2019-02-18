from queue import PriorityQueue


class HuffmanTree:

    class __Node:
        def __init__(self, valor, frecuencia, hijo_izq, hijo_der):
            self.valor = valor
            self.frecuencia = frecuencia
            self.hijo_izq = hijo_izq
            self.hijo_der = hijo_der

        @classmethod
        def init_leaf(self, valor, frecuencia):
            return self(valor, frecuencia, None, None)

        @classmethod
        def init_node(self, hijo_izq, hijo_der):
            frecuencia = hijo_izq.frecuencia + hijo_der.frecuencia
            return self(None, frecuencia, hijo_izq, hijo_der)

        def is_leaf(self):
            return self.valor is not None

        def __eq__(self, other):
            stup = self.valor, self.frecuencia, self.hijo_izq, self.hijo_der
            otup = other.valor, other.frecuencia, other.hijo_izq, other.hijo_der
            return stup == otup

        def __nq__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self.frecuencia < other.frecuencia

        def __le__(self, other):
            return self.frecuencia < other.frecuencia or self.frecuencia == other.frecuencia

        def __gt__(self, other):
            return not (self <= other)

        def __ge__(self, other):
            return not (self < other)

    def __init__(self, arr):
        q = PriorityQueue()

        for val, frecuencia in self.__calc_frecuencia(arr).items():
            q.put(self.__Node.init_leaf(val, frecuencia))

        while q.qsize() >= 2:
            u = q.get()
            v = q.get()

            q.put(self.__Node.init_node(u, v))

        self.__root = q.get()

        self.__valor_to_bitstring = dict()

    def valor_to_bitstring_table(self):
        if len(self.__valor_to_bitstring.keys()) == 0:
            self.__create_huffman_table()
        return self.__valor_to_bitstring

    def __create_huffman_table(self):
        def tree_traverse(current_node, bitstring=''):
            if current_node is None:
                return
            if current_node.is_leaf():
                self.__valor_to_bitstring[current_node.valor] = bitstring
                return
            tree_traverse(current_node.hijo_izq, bitstring + '0')
            tree_traverse(current_node.hijo_der, bitstring + '1')

        tree_traverse(self.__root)

    def __calc_frecuencia(self, arr):
        frecuencia_dict = dict()
        for elem in arr:
            if elem in frecuencia_dict:
                frecuencia_dict[elem] += 1
            else:
                frecuencia_dict[elem] = 1
        return frecuencia_dict