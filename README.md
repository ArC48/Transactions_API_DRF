# Transactions API

This Django REST API manages and queries transaction records. It allows users to:

- View transactions
- Track purchases by users or products
- Access detailed, paginated transaction data

The API supports JSON responses and features Swagger documentation for easy endpoint exploration.

---

## Available Endpoints

### 1. `transactions/`
- **Description**: Fetches all transactions in the system.
- **Method**: `GET`
- **Response**: A paginated list of all transactions.

---

### 2. `product-purchases/<int:item_code>/`
- **Description**: Fetches total number of item purchases on each date by its `item_code`.
- **Method**: `GET`
- **Response**: Detailed view of the specified purchase.

---

### 3. `user-purchases/<int:user_id>/`
- **Description**: Fetches total number of items a specific user purchases on each date by user's `user_id`.
- **Method**: `GET`
- **Response**: A paginated list of purchases made by the user, with total items purchased aggregated by date.

---

### 4. `default endpoint` or `api/schema/docs/`
- **Description**: Provides Swagger UI documentation for interacting with the API endpoints.
- **Method**: `GET`
- **Response**: An interactive web-based UI where users can explore and test the available API endpoints.
