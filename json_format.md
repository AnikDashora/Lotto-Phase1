# 📄 JSON Format Documentation for Looto Phase 1

This document outlines the structure and expected data types for all JSON files used in Phase 1 of the Looto.com project.

---

## users.json

```json
{
  "user_id": "uid",             // string: unique user identifier
  "username": "username",       // string: display name
  "email": "email",             // string: user email address
  "password": "Pass@123"       // string: hashed password or plain (for demo)
}
```

---

## products.json

```json
{
  "product_id": "pid",             // string: unique product identifier
  "product_name": "product_name",          // string: name of product
  "product_price": 0,                      // number: current price
  "product_image": "product_image.png",    // string: image filename or URL
  "product_description": "product_description", // string: product summary
  "product_category": "category_name"      // string: product's category
}
```

---

## cart.json

```json
{
  "user_id": "uid",               // string: owner of the cart
  "cart_items": [
    { "product_id": "pid1", "quantity": 1 },  // product ID and quantity
    { "product_id": "pid2", "quantity": 2 }
  ]
}
```

---

## tracking.json

```json
{
  "user_id": "uid",                  // string: who placed the orders
  "orders": [
    {
      "order_id": "oid",             // string: unique order ID
      "items": [
        {
          "product_id": "pid",       // string: purchased product ID
          "quantity": 1,             // number: quantity bought
          "locked_price": 0          // number: price at time of purchase
        }
      ],
      "timestamp": "YYYY-MM-DD HH:MM",  // string: ISO timestamp
      "current_status": "Ordered"       // string: current stage of delivery
    },
  ]
}
// Status can be: "Ordered", "Packed", "Shipped", "Out for Delivery", "Delivered", "Cancelled"
```

---

## categories.json

```json
{
  "category_name_1": ["pid1", "pid2"],   // array of product IDs in a category
  "category_name_2": ["pid3"]
}
```
