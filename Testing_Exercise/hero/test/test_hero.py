from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("Terax", 17, 100, 35)
        self.enemy = Hero("Enemy", 10, 100, 20)

    def test_correct_init(self):
        self.assertEqual("Terax", self.hero.username)
        self.assertEqual(17, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(35, self.hero.damage)

    def test_battle_cannot_fight_with_yourself_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_when_health_is_negative_raises_value_error(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))


    def test_battle_when_enemy_health_is_negative_raises_value_error(self):
        self.enemy.health = 0 #Arrange

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy) #Act

        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ve.exception)) # Assert

    def test_battle_both_take_damage_result_and_returns_draw(self):
        result = self.hero.battle(self.enemy)

        self.assertEqual("Draw", result)
        self.assertEqual(-100, self.hero.health)
        self.assertEqual(-495, self.enemy.health)

    def test_battle_when_enemy_lose_and_and_hero_gains_level_health_damage_returns_string(self):
        self.enemy.damage = 1
        expected_level = self.hero.level + 1
        expected_health = self.hero.health - self.enemy.damage * self.enemy.level + 5
        expected_damage = self.hero.damage + 5

        result = self.hero.battle(self.enemy)

        self.assertEqual("You win", result)
        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)

    def test_battle_when_enemy_wins_enemy_gains_level_health_damage_returns_string(self):
        self.hero.level = 1
        expected_level = self.enemy.level + 1
        expected_health = self.enemy.health - self.hero.level * self.hero.damage + 5
        expected_damage = self.enemy.damage + 5

        result = self.hero.battle(self.enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(expected_level, self.enemy.level)
        self.assertEqual(expected_health, self.enemy.health)
        self.assertEqual(expected_damage, self.enemy.damage)

    def test_correct__str__method(self):
        expected_string = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                          f"Health: {self.hero.health}\n" \
                          f"Damage: {self.hero.damage}\n"

        self.assertEqual(expected_string, str(self.hero))

if __name__ == "__main__":
    main()