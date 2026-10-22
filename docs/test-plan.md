# Test Plan
1. `GET /api/health` returns status `ok`.
2. Food lookup with `{"food":"rice"}` returns approximate reference values.
3. Unknown food returns no prediction and an explanatory message.
4. Freshness checklist with any true flag returns a caution message.
5. Hygiene checklist returns a percentage from 0 to 100.
6. Recipe request with `rice, vegetables` returns matching sample recipes.
7. Meal planner returns a sample plan for a valid preference and budget.
8. UI: navigate all five modules, submit each form, and verify an error appears when the backend is stopped.

Record actual test results and screenshots after running the app. Do not report unrun tests as passed.
