from unittest import TestCase, main
import balls_collide as bc


class BallsTests(TestCase):
    def test_invalid_data(self):
        ball_one = (5.5, 7, -8)
        ball_two = (1.2, -5, 9)
        self.assertRaises(ValueError, bc.balls_collide, ball_one, ball_two)

    def test_function(self):
        ball1 = (5.5, 7, 8)
        ball2 = (1.2, 5, 9)
        self.assertEqual(bc.balls_collide(ball1, ball2), True)
        ball3 = (0, 0, 1)
        ball4 = (10, 0, 1)
        self.assertEqual(bc.balls_collide(ball3, ball4), False)
        ball5 = (0, 0, 1)
        ball6 = (0, 0, 2)
        self.assertEqual(bc.balls_collide(ball5, ball6), True)
        self.assertTrue(bc.balls_collide((2, 2, 6.6), (2, 2, 6.5)))
        self.assertTrue(bc.balls_collide((2, 2, 2), (2, 0, 0)))
        self.assertTrue(bc.balls_collide((2, 2, 0), (2, 2, 0)))
        self.assertFalse(bc.balls_collide((1, 2, 1.004), (2.005, 1, 0)))


main()
