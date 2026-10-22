# Food Verse AI — MVP

A lightweight SmartBridge project prototype with a React frontend and Flask API. It demonstrates food information, freshness warning checklist, kitchen hygiene checklist, recipe suggestions, and a sample meal planner.

**Honest scope:** This MVP uses reference nutrition data and rule-based checklists/suggestions. It does not include trained image recognition or video analysis; image upload is preview-only. Freshness and hygiene results are not food-safety certifications.

## Run locally

### Backend
```bash
cd backend
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
python app.py
```
Runs on http://127.0.0.1:5000.

### Frontend (new terminal)
```bash
cd frontend
npm install
npm run dev
```
Open the Vite URL shown (usually http://localhost:5173).

## API
`GET /api/health`; `POST /api/food-info`; `POST /api/freshness-check`; `POST /api/hygiene-score`; `POST /api/recipes`; `POST /api/meal-plan`.

## Submission checklist
1. Test all five modules and capture screenshots.
2. Push this folder to your own GitHub repository.
3. Deploy the frontend and backend if a live demo is required. Set `VITE_API_URL` to the deployed backend URL when building the frontend.
4. Add actual GitHub and demo URLs to MySkillWallet.
5. Update Kanban cards honestly and inform the SmartBridge WhatsApp group for review.
