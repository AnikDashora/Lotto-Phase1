# 🛍️ Looto.com – Phase 1

Looto.com is a lightweight e-commerce prototype built using **Streamlit** and **core Python logic**, storing all data in structured **JSON files**. This phase focuses on creating a functional, multi-user shopping experience without using external databases or frameworks.

---

## 📌 Features

- 🔐 **User Authentication**
  - Signup/Login with device ID validation
  - Session management via Streamlit

- 🏠 **Home Page**
  - Product categories
  - Search bar
  - Dynamic product display

- 📄 **Product Page**
  - Product image, name, price, description
  - Add to Cart / Buy options

- 🛒 **Cart Page**
  - All added products
  - Quantity control and total price
  - Checkout redirect

- 🚚 **Tracking Page**
  - View order history
  - Track current delivery status

---

## 📁 Project Structure

```
looto/
├── .env                      # App config variables
├── app.py                   # Streamlit router and state manager
├── README.md                # Project overview and setup
│
├── .streamlit/              # Streamlit config
│   └── config.toml
│
├── pages/                   # User-facing pages
│   ├── 1_Landing_Page.py
│   ├── 2_Home.py
│   ├── 3_Product.py
│   ├── 4_Cart.py
│   └── 5_Tracking.py
│
├── auth/                    # Authentication screens
│   ├── login.py
│   └── signup.py
│
├── session_state/           # Session state handling
│   └── session_manager.py
│
├── services/                # Business logic
│   ├── auth_service.py
│   ├── cart_service.py
│   ├── product_service.py
│   ├── tracking_service.py
│   └── data_validation/
│       └── json_validator.py
│
├── data/                    # JSON-based data storage
│   ├── users.json
│   ├── products.json
│   ├── cart.json
│   ├── tracking.json
│   └── categories.json
│
└── static/
    └── products/
        └── red_tshirt.png
```

---

## 🧪 Sample JSON Format

### users.json
```json
{
  "user_id": "uid",
  "username": "username",
  "email": "email",
  "password": "Pass@123",
  "device_id": "AA:BB:CC:DD:EE:FF"
}
```

### cart.json
```json
{
  "user_id": "uid",
  "cart_items": [
    { "product_id": "pid1", "quantity": 1 },
    { "product_id": "pid2", "quantity": 2 }
  ]
}
```

### tracking.json
```json
{
  "user_id": "uid",
  "orders": [
    {
      "order_id": "oid",
      "items": [
        { "product_id": "pid", "quantity": 1, "locked_price": 0 }
      ],
      "timestamp": "YYYY-MM-DD HH:MM",
      "current_status": "Ordered"
    }
  ]
}
// Status: "Ordered", "Packed", "Shipped", "Out for Delivery", "Delivered", "Cancelled"
```

---

## 🚀 Future Advancements – Phase 2

- Use **MySQL** for persistent data storage
- Refactor services into **Object-Oriented Python**
- Add **Admin panel** for product management
- Integrate **payment gateway** (mock)
- Enable **coupon system**, **reviews**, and **ratings**

---

## 📌 Setup Instructions

1. Clone the repository
   ```bash
   git clone https://github.com/your-username/looto.com.git
   cd looto.com
   ```

2. Create `.env` file for environment variables (example provided)

3. Run the app using Streamlit:
   ```bash
   streamlit run app.py
   ```

---

## 📄 License

This project is open-sourced under the MIT License.

---

> Built with ❤️ using Python + Streamlit
