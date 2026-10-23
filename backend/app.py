from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

FOODS = {
    "apple": (95, 0.5, 25, 0.3, "one medium apple"),
    "banana": (105, 1.3, 27, 0.4, "one medium banana"),
    "rice": (205, 4.3, 45, 0.4, "one cup cooked white rice"),
    "egg": (78, 6.3, 0.6, 5.3, "one large egg"),
    "roti": (110, 3.0, 22, 1.5, "one medium plain roti"),
    "paneer": (265, 18, 1.2, 20, "100 g paneer"),
    "dal": (180, 10, 30, 2, "one cup cooked dal"),
    "oats": (154, 5.3, 27, 2.6, "40 g dry oats")
}
RECIPES = [
 {"name":"Vegetable rice bowl","ingredients":["rice","vegetables","oil"],"steps":["Cook rice.","Sauté vegetables with a little oil.","Combine, season and serve hot."],"time":"20 min","type":"vegetarian"},
 {"name":"Masala oats","ingredients":["oats","onion","tomato","spices"],"steps":["Sauté onion and tomato.","Add oats, water and spices.","Simmer until soft."],"time":"12 min","type":"vegetarian"},
 {"name":"Paneer roti roll","ingredients":["paneer","roti","onion","capsicum"],"steps":["Cook paneer with onion, capsicum and spices.","Warm roti.","Add filling and roll."],"time":"18 min","type":"vegetarian"},
 {"name":"Egg rice","ingredients":["egg","rice","vegetables"],"steps":["Cook egg thoroughly.","Add cooked rice and vegetables.","Stir-fry until steaming hot."],"time":"15 min","type":"egg"},
 {"name":"Dal and roti","ingredients":["dal","roti","spices"],"steps":["Cook dal until soft.","Season as desired.","Serve with warm roti."],"time":"25 min","type":"vegetarian"}
]

@app.get('/api/health')
def health(): return jsonify(status='ok', app='Food Verse AI')

@app.post('/api/food-info')
def food_info():
    food = str((request.get_json(silent=True) or {}).get('food','')).strip().lower()
    if not food: return jsonify(error='Enter a food name.'), 400
    if food not in FOODS:
        return jsonify(food=food.title(), calories=None, protein_g=None, carbs_g=None, fat_g=None, note='No reference entry yet; no prediction was made.', source='Demo reference data only.')
    c,p,carb,f,note = FOODS[food]
    return jsonify(food=food.title(), calories=c, protein_g=p, carbs_g=carb, fat_g=f, note=f'Approximate values for {note}.', source='Reference estimate; varies by serving and preparation.')

@app.post('/api/freshness-check')
def freshness():
    answers = (request.get_json(silent=True) or {}).get('answers', {})
    if not answers: return jsonify(error='Provide checklist answers.'), 400
    flags = [k for k,v in answers.items() if v is True]
    return jsonify(level='Caution' if flags else 'No listed flags', flags=flags,
      message='Warning signs selected. Do not taste the food; when in doubt, discard it.' if flags else 'No listed warning signs selected, but this does not prove food is safe.',
      disclaimer='Checklist only. Appearance and smell cannot rule out harmful pathogens.')

@app.post('/api/hygiene-score')
def hygiene():
    checks = (request.get_json(silent=True) or {}).get('checks', {})
    if not checks: return jsonify(error='Provide hygiene checklist answers.'), 400
    passed = sum(v is True for v in checks.values()); total = len(checks)
    return jsonify(score=round(passed/total*100), passed=passed, total=total,
      status='Checklist complete' if passed == total else 'Actions required',
      message='Rule-based checklist score; not an official inspection or certification.')

@app.post('/api/recipes')
def recipes():
    data=request.get_json(silent=True) or {}; ingredients={x.strip().lower() for x in str(data.get('ingredients','')).split(',') if x.strip()}
    dietary=str(data.get('dietary','any')).lower()
    if not ingredients: return jsonify(error='Enter ingredients separated by commas.'),400
    matches=[]
    for r in RECIPES:
        if dietary=='vegetarian' and r['type']=='egg': continue
        hits=ingredients.intersection(r['ingredients'])
        if hits: matches.append({**r,'matched_ingredients':sorted(hits)})
    return jsonify(recipes=matches[:5],message='Rule-based recipe examples. Check allergies and cook food thoroughly.')

@app.post('/api/meal-plan')
def meal_plan():
    d=request.get_json(silent=True) or {}; pref=str(d.get('preference','vegetarian')).lower(); goal=str(d.get('goal','balanced')).lower(); budget=str(d.get('budget','low')).lower()
    if pref not in {'vegetarian','egg','any'}: return jsonify(error='Choose vegetarian, egg, or any.'),400
    meals={'breakfast':'Oats with banana' if budget=='low' else 'Poha with curd','lunch':'Dal, roti and seasonal vegetables','snack':'Seasonal fruit or roasted chana','dinner':'Vegetable rice bowl' if pref=='vegetarian' else 'Rice, vegetables and a protein of choice'}
    return jsonify(preference=pref,goal=goal,budget=budget,meals=meals,note='General meal ideas, not medical or dietetic advice.')
import os

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        debug=False
    )
