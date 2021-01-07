import unittest
import solution


class SolutionTest(unittest.TestCase):
    def test_block(self):
        state0 = [[0, 0, 0, 0, 0],
                  [0, 1, 1, 0, 0],
                  [0, 1, 1, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0]]

        result = solution.next_generation(state0)
        expected = [[0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 0],
                    [0, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]]
        self.assertEqual(expected, result)

    def test_lonely_death(self):
        state0 = [[0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0]]

        result = solution.next_generation(state0)
        expected = [[0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]]
        self.assertEqual(expected, result)


    def test_blinker_at_edge(self):
        state0 = [[0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0]]

        state1 = solution.next_generation(state0)
        expected_state1 = [[0, 0, 0, 0, 0],
                           [0, 0, 0, 1, 1],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0]]
        self.assertEqual(expected_state1, state1)


        state2 = solution.next_generation(state1)
        expected_state2 = [[0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0]]
        self.assertEqual(expected_state2, state2)

    def test_single_row_grid(self):
        state0 = [[0, 1, 1, 1, 0]]

        state1 = solution.next_generation(state0)
        expected_state1 = [[0, 0, 1, 0, 0]]
        self.assertEqual(expected_state1, state1)

        state2 = solution.next_generation(state1)
        expected_state2 = [[0, 0, 0, 0, 0]]
        self.assertEqual(expected_state2, state2)

    def test_single_column_grid(self):
        state0 = [[0],
                  [1],
                  [1],
                  [1],
                  [0]]

        state1 = solution.next_generation(state0)
        expected_state1 = [[0],
                           [0],
                           [1],
                           [0],
                           [0]]
        self.assertEqual(expected_state1, state1)

        state2 = solution.next_generation(state1)
        expected_state2 = [[0],
                           [0],
                           [0],
                           [0],
                           [0]]
        self.assertEqual(expected_state2, state2)

    def test_glider(self):
        state0 = [[0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 0, 0],
                  [1, 1, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]]

        state1 = solution.next_generation(state0)
        expected_state1 = [[0, 0, 0, 0, 0, 0, 0, 0],
                           [1, 0, 1, 0, 0, 0, 0, 0],
                           [0, 1, 1, 0, 0, 0, 0, 0],
                           [0, 1, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(expected_state1, state1)

        state2 = solution.next_generation(state1)
        expected_state2 = [[0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 1, 0, 0, 0, 0, 0],
                           [1, 0, 1, 0, 0, 0, 0, 0],
                           [0, 1, 1, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(expected_state2, state2)

        state3 = solution.next_generation(state2)
        expected_state3 = [[0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 1, 0, 0, 0, 0, 0, 0],
                           [0, 0, 1, 1, 0, 0, 0, 0],
                           [0, 1, 1, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(expected_state3, state3)

        state4 = solution.next_generation(state3)
        expected_state4 = [[0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 1, 0, 0, 0, 0, 0],
                           [0, 0, 0, 1, 0, 0, 0, 0],
                           [0, 1, 1, 1, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(expected_state4, state4)

if __name__ == "__main__":
    unittest.main()
