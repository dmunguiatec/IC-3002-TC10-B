import unittest

from simulated_annealing import optimizar
from dominio import Dominio3SAT


class CasosDePrueba(unittest.TestCase):

    def test_optimizar_peq(self):
        dominio = Dominio3SAT('./datos/f20-91.cnf')
        sol = optimizar(dominio)
        self.assertEqual(dominio.fcosto(sol), 0)

    def test_optimizar_gde(self):
        dominio = Dominio3SAT('./datos/f100-430.cnf')
        sol = optimizar(dominio)
        self.assertLess(dominio.fcosto(sol), dominio.fcosto([True] * 100))
