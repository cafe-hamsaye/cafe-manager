# Backend API Documentation

This file contains the documentation for all available backend endpoints.

---

## Authentication

### `POST /api/auth/register/`

**Description:** This endpoint is used to register a new user in the system.

**Request Body:**
```json
{
  "first_name": "string",
  "last_name": "string",
  "phone_number": "09123456789",
  "password": "yourpassword",
  "password2": "yourpassword"
}
```

**Success Response:**
- **Code:** `201 Created`
- **Content:**
```json
{
  "id": 1,
  "first_name": "string",
  "last_name": "string",
  "phone_number": "09123456789"
}
```

**Error Responses:**
- **Code:** `400 Bad Request`
  - **Content:** `{ "phone_number": ["کاربری با این شماره تلفن قبلا ثبت‌نام کرده است"] }`
  - **Content:** `{ "first_name": ["لطفا نام خود را وارد کنید"] }`
  - **Content:** `{ "last_name": ["لطفا نام خانوادگی خود را وارد کنید"] }`

---

### `POST /api/auth/login/`

**Description:** This endpoint is used for user login.

**Request Body:**
```json
{
  "phone_number": "09123456789",
  "password": "yourpassword"
}
```

**Success Response:**
- **Code:** `200 OK`
- **Content:**
```json
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
```

**Error Responses:**
- **Code:** `401 Unauthorized`
  - **Content:** `{ "detail": "شماره تلفن یا رمز عبور اشتباه است" }`

---

### `POST /api/auth/admin/login/`

**Description:** This endpoint is used for admin login. It uses a standard token-based authentication. The access token will contain an `is_admin` claim set to `true`.

**Request Body:**
```json
{
  "username": "your_admin_username",
  "password": "your_admin_password"
}
```

**Success Response:**
- **Code:** `200 OK`
- **Content:**
```json
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
```

**Error Responses:**
- **Code:** `401 Unauthorized`
  - **Content:** `{ "detail": "نام کاربری یا رمز عبور اشتباه است" }`

---

### `POST /api/auth/token/refresh/`

**Description:** This endpoint is used to get a new access token using a refresh token.

**Request Body:**
```json
{
  "refresh": "your_refresh_token"
}
```

**Success Response:**
- **Code:** `200 OK`
- **Content:**
```json
{
  "access": "your_new_access_token"
}
```

**Error Responses:**
- **Code:** `401 Unauthorized`
  - **Content:** `{ "detail": "Token is invalid or expired", "code": "token_not_valid" }`

---

### `GET /api/auth/user/`



**Description:** Returns the information of the logged-in user based on the provided token.



**Headers:**

```json

{

  "Authorization": "Bearer your_access_token"

}

```



**Success Response:**

- **Code:** `200 OK`

- **Content:** (Complete user information without the password)

```json

{

  "id": 1,

  "first_name": "string",

  "last_name": "string",

  "phone_number": "09123456789"

}

```



**Error Responses:**

- **Code:** `401 Unauthorized`

  - **Content:** `{ "detail": "Authentication credentials were not provided." }`

  - **Content:** `{ "detail": "Given token not valid for any token type" }`



---



## User Management (Admin Only)



### `GET /api/auth/users/`



**Description:** Retrieves a list of all registered users. Requires admin authentication.



**Headers:**

```json

{

  "Authorization": "Bearer your_admin_access_token"

}

```



**Success Response:**

- **Code:** `200 OK`

- **Content:**

```json

[

  {

    "id": 1,

    "first_name": "string",

    "last_name": "string",

    "phone_number": "09123456789"

  },

  ...

]

```



**Error Responses:**

- **Code:** `401 Unauthorized`

  - **Content:** `{ "detail": "Authentication credentials were not provided." }`

- **Code:** `403 Forbidden`

  - **Content:** `{ "detail": "You do not have permission to perform this action." }`



---



### `DELETE /api/auth/users/{id}/`



**Description:** Deletes a specific user by their ID. Requires admin authentication.



**Headers:**

```json

{

  "Authorization": "Bearer your_admin_access_token"

}

```



**Success Response:**

- **Code:** `204 No Content`



**Error Responses:**

- **Code:** `401 Unauthorized`

- **Code:** `403 Forbidden`

- **Code:** `404 Not Found`

---

## Menu Management

### `GET /api/menu/`

**Description:** Retrieves a list of all menu items.

**Success Response:**
- **Code:** `200 OK`
- **Content:**
```json
[
  {
    "id": 1,
    "name": "string",
    "description": "string",
    "price": "string",
    "image_url": "string"
  },
  ...
]
```

---

### `POST /api/menu/`

**Description:** Creates a new menu item. Requires admin authentication.

**Headers:**
```json
{
  "Authorization": "Bearer your_admin_access_token"
}
```

**Request Body:**
```json
{
  "name": "string",
  "description": "string",
  "price": "string",
  "image_url": "string"
}
```

**Success Response:**
- **Code:** `201 Created`
- **Content:**
```json
{
  "id": 1,
  "name": "string",
  "description": "string",
  "price": "string",
  "image_url": "string"
}
```

**Error Responses:**
- **Code:** `400 Bad Request`
- **Code:** `401 Unauthorized`
- **Code:** `403 Forbidden`

---

### `PUT /api/menu/{id}/`

**Description:** Updates a specific menu item by its ID. Requires admin authentication.

**Headers:**
```json
{
  "Authorization": "Bearer your_admin_access_token"
}
```

**Request Body:**
```json
{
  "name": "string",
  "description": "string",
  "price": "string",
  "image_url": "string"
}
```

**Success Response:**
- **Code:** `200 OK`
- **Content:**
```json
{
  "id": 1,
  "name": "string",
  "description": "string",
  "price": "string",
  "image_url": "string"
}
```

**Error Responses:**
- **Code:** `400 Bad Request`
- **Code:** `401 Unauthorized`
- **Code:** `403 Forbidden`
- **Code:** `404 Not Found`

---

### `DELETE /api/menu/{id}/`

**Description:** Deletes a specific menu item by its ID. Requires admin authentication.

**Headers:**
```json
{
  "Authorization": "Bearer your_admin_access_token"
}
```

**Success Response:**
- **Code:** `204 No Content`

**Error Responses:**
- **Code:** `401 Unauthorized`
- **Code:** `403 Forbidden`
- **Code:** `404 Not Found`
