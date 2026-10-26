import unittest
from app import app

class FoodVerseAPITests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health(self):
        r = self.client.get('/api/health')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.get_json()['status'], 'ok')

    def test_known_food(self):
        r = self.client.post('/api/food-info', json={'food': 'rice'})
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.get_json()['calories'])

    def test_empty_food_is_rejected(self):
        self.assertEqual(self.client.post('/api/food-info', json={'food': ''}).status_code, 400)

    def test_unknown_food_is_not_guessed(self):
        d = self.client.post('/api/food-info', json={'food': 'dragonfruit'}).get_json()
        self.assertIsNone(d['calories'])
        self.assertIn('no prediction', d['note'].lower())

    def test_freshness_warning(self):
        d = self.client.post('/api/freshness-check', json={'answers': {'mold': True}}).get_json()
        self.assertEqual(d['level'], 'Caution')

    def test_hygiene_score(self):
        d = self.client.post('/api/hygiene-score', json={'checks': {'hands': True, 'storage': False}}).get_json()
        self.assertEqual(d['score'], 50)

    def test_recipe_suggestion(self):
        d = self.client.post('/api/recipes', json={'ingredients': 'rice, vegetables', 'dietary': 'vegetarian'}).get_json()
        self.assertTrue(d['recipes'])

    def test_meal_plan_goal(self):
        d = self.client.post('/api/meal-plan', json={'preference': 'vegetarian', 'goal': 'protein', 'budget': 'low'}).get_json()
        self.assertEqual(d['goal'], 'protein')
        self.assertIn('protein', d['meals']['lunch'].lower())

    def test_invalid_meal_plan_option(self):
        self.assertEqual(self.client.post('/api/meal-plan', json={'preference': 'invalid'}).status_code, 400)

if __name__ == '__main__':
    unittest.main()
