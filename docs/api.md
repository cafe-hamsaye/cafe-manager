# Backend API Documentation

This file contains the documentation for all available backend endpoints.

---

## Authentication

### `POST /api/auth/register`

**Description:** This endpoint is used to register a new user in the system.

**Request Body:**
```json
{
  "firstName": "string",
  "lastName": "string",
  "phoneNumber": "09123456789",
  "password": "yourpassword"
}
```

**Success Response:**
- **Code:** `201 Created`
- **Content:**
```json
{
  "id": 1,
  "firstName": "string",
  "lastName": "string",
  "token": "your_jwt_token"
}
```

**Error Responses:**
- **Code:** `400 Bad Request`
  - **Content:** `{ "message": "لطفا تمام فیلدها را وارد کنید" }`
  - **Content:** `{ "message": "کاربری با این شماره تلفن قبلا ثبت‌نام کرده است" }`
- **Code:** `500 Internal Server Error`
  - **Content:** `{ "message": "خطایی در سرور رخ داده است", "error": "error_details" }`

---

### `POST /api/auth/login`

**Description:** This endpoint is used for user login.

**Request Body:**
```json
{
  "phoneNumber": "09123456789",
  "password": "yourpassword"
}
```

**Success Response:**
- **Code:** `200 OK`
- **Content:**
```json
{
  "id": 1,
  "firstName": "string",
  "lastName": "string",
  "token": "your_jwt_token"
}
```

**Error Responses:**
- **Code:** `400 Bad Request`
  - **Content:** `{ "message": "لطفا تمام فیلدها را وارد کنید" }`
- **Code:** `401 Unauthorized`
  - **Content:** `{ "message": "شماره تلفن یا رمز عبور اشتباه است" }`
- **Code:** `500 Internal Server Error`
  - **Content:** `{ "message": "خطایی در سرور رخ داده است", "error": "error_details" }`

---

### `GET /api/auth/user`

**Description:** Returns the information of the logged-in user based on the provided token. This endpoint is used for server-side token validation.

**Headers:**
```json
{
  "Authorization": "Bearer your_jwt_token"
}
```

**Success Response:**
- **Code:** `200 OK`
- **Content:** (Complete user information without the password)
```json
{
  "id": 1,
  "firstName": "string",
  "lastName": "string",
  "phoneNumber": "09123456789",
  "createdAt": "2023-10-27T10:00:00.000Z",
  "updatedAt": "2023-10-27T10:00:00.000Z"
}
```

**Error Responses:**
- **Code:** `401 Unauthorized`
  - **Content:** `{ "message": "خطای دسترسی: توکن ارسال نشده است" }`
  - **Content:** `{ "message": "خطای دسترسی: توکن نامعتبر است" }`
  - **Content:** `{ "message": "خطای دسترسی: کاربر یافت نشد" }`
