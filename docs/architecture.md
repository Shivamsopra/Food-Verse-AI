# Technical Architecture
- Frontend: React + Vite single-page application.
- Backend: Flask REST API with CORS enabled for local development.
- Communication: JSON over HTTP.
- Data: Small in-memory reference dataset and rule-based logic.
- Endpoints: `GET /api/health`, `POST /api/food-info`, `/api/freshness-check`, `/api/hygiene-score`, `/api/recipes`, `/api/meal-plan`.

## Limitations
Food image upload is preview-only; no computer-vision model is connected. Nutrition figures are approximate reference values. Freshness and hygiene checklists are not validated safety assessments. Recipes and meal plans use simple rules. Future work: evaluated vision models, verified nutrition database, video analysis, authentication, persistent storage, and formal testing.
