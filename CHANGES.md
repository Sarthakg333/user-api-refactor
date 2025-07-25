 CHANGES.md

## 🛠️ Major Issues Identified in Original Code

1. ❌ **SQL Injection Vulnerability**
   - All SQL queries were constructed using string interpolation (f-strings), which is unsafe.
   - Example: `f"SELECT * FROM users WHERE id = '{user_id}'"`

2. ❌ **No Error Handling**
   - If a database operation failed, the server would crash or return unclear errors.

3. ❌ **No JSON Responses or Status Codes**
   - Responses were plain strings like `"User created"` or `"User not found"` without status codes.

4. ❌ **All Logic in One File**
   - No separation between DB logic and API routes, making it hard to scale or debug.

---

## ✅ Changes Made

1. ✅ **Used Parameterized SQL Queries**
   - Replaced all `f""` queries with `cursor.execute(..., (...))` to prevent SQL injection.

2. ✅ **Added JSON Responses**
   - All endpoints now return `jsonify({...})` with appropriate status codes (200, 201, 400, 404, 500).

3. ✅ **Error Handling**
   - Wrapped all database interactions in `try-except` blocks.

4. ✅ **Utility Function for DB Connection**
   - Created `get_db_connection()` to centralize connection logic and use `Row` factory for cleaner results.

5. ✅ **Improved `init_db.py`**
   - Used `executemany()` for cleaner sample data insertion.
   - Added comments for better readability and habit of safe query execution.