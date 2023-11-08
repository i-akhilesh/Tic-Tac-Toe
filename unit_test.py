import unittest
from final import TicTacToeGame,Move,TicTacToeBoard
import tkinter as tk

class TestTicTacToeGame(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToeGame()

    def test_toggle_player(self):
        player1 = self.game.current_player
        self.game.toggle_player()
        player2 = self.game.current_player
        self.assertNotEqual(player1, player2)
        self.game.toggle_player()
        player3 = self.game.current_player
        self.assertEqual(player1, player3)

    def test_is_valid_move(self):
        move = Move(0, 0)
        self.assertTrue(self.game.is_valid_move(move))
        self.game.process_move(move)
        self.assertFalse(self.game.is_valid_move(move))
        self.game.reset_game()

    def test_process_move(self):
        move = Move(0, 0, label=self.game.current_player.label)
        self.game.process_move(move)
        self.assertEqual(self.game._current_moves[0][0].label, move.label)
        self.game.reset_game()

    def test_has_winner(self):
        self.game._current_moves[0][0] = Move(0, 0, label=self.game.current_player.label)
        self.game._current_moves[0][1] = Move(0, 1, label=self.game.current_player.label)
        self.game._current_moves[0][2] = Move(0, 2, label=self.game.current_player.label)
        self.game._has_winner = True
        self.game.winner_combo = [(0,0),(0,1),(0,2)]
        self.assertTrue(self.game.has_winner())
        self.game.reset_game()

    def test_is_tied(self):
        self.game._has_winner = False
        self.game._current_moves[0][0] = Move(0, 0, label="X")
        self.game._current_moves[0][1] = Move(0, 1, label="O")
        self.game._current_moves[0][2] = Move(0, 2, label="X")
        self.game._current_moves[1][0] = Move(1, 0, label="O")
        self.game._current_moves[1][1] = Move(1, 1, label="X")
        self.game._current_moves[1][2] = Move(1, 2, label="O")
        self.game._current_moves[2][0] = Move(2, 0, label="X")
        self.game._current_moves[2][1] = Move(2, 1, label="O")
        self.game._current_moves[2][2] = Move(2, 2, label="X")
        self.assertTrue(self.game.is_tied())
        self.game.reset_game()

class TestTicTacToeBoard(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToeGame()
        self.board = TicTacToeBoard(self.game)

    def test_create_board_grid(self):
        self.assertEqual(len(self.board._cells), self.game.board_size ** 2)

if __name__ == '__main__':
    unittest.main()