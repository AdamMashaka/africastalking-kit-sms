# AfriAuth

🚀 Plug-and-play SMS OTP authentication for FastAPI powered by Africa’s Talking.

`AfriAuth` helps developers quickly integrate secure OTP authentication, phone verification, login flows, and SMS-based authentication into FastAPI applications with minimal setup.

Built for African startups, fintechs, SaaS platforms, and mobile-first applications.

---

# ✨ Why AfriAuth?

Most developers spend days building:

* OTP generation
* SMS delivery
* OTP verification
* retry protection
* expiration handling
* rate limiting
* authentication flows
* Redis session storage

`Afriauth` solves this in minutes.

---

# ⚡ Features

## 🔐 SMS OTP Authentication

Send and verify OTP codes instantly using Africa’s Talking.

## ⚡ FastAPI Integration

Built specifically for FastAPI with async support.

## 🧠 Automatic OTP Management

Handles:

* OTP generation
* expiration
* retries
* verification
* cleanup

## 🚦 Rate Limiting

Prevent abuse and SMS spam automatically.

## 🔒 Secure by Default

Includes:

* hashed OTP storage
* expiration windows
* brute-force protection
* replay prevention

## 📦 Redis Support

Store OTP sessions efficiently with Redis.

## 🧩 Plug-and-Play API Routes

Auto-generate authentication endpoints.

## 🌍 Africa’s Talking Integration

Optimized for African telecom infrastructure.

## 🔄 Extensible Provider System

Future support planned for:

* Twilio
* Infobip
* Hubtel
* Termii
* WhatsApp OTP

---

# 📦 Installation

```bash id="69kbbi"
pip install afriauth
```

---

# 🚀 Quick Start

## 1. Initialize Afriauth

```python id="p4n0dd"
from afriauth import AfriAuth

auth = AfriAuth(
    username="sandbox",
    api_key="YOUR_AFRICASTALKING_API_KEY"
)
```

---

# 📲 Send OTP

```python id="7s4i1q"
await auth.send_otp("+255712345678")
```

---

# ✅ Verify OTP

```python id="6m8p3d"
is_valid = await auth.verify_otp(
    phone="+255712345678",
    code="123456"
)

print(is_valid)
```

---

# ⚡ FastAPI Example

```python id="fvs1d1"
from fastapi import FastAPI
from afriauth import AfriAuth

app = FastAPI()

auth = AfriAuth(
    username="sandbox",
    api_key="YOUR_API_KEY"
)


@app.post("/send-otp")
async def send_otp(phone: str):
    await auth.send_otp(phone)

    return {
        "success": True,
        "message": "OTP sent successfully"
    }


@app.post("/verify-otp")
async def verify_otp(phone: str, code: str):
    verified = await auth.verify_otp(phone, code)

    return {
        "verified": verified
    }
```

---

# ⚙️ Redis Configuration

```python id="z0rx48"
auth = AfriAuth(
    username="sandbox",
    api_key="YOUR_API_KEY",
    redis_url="redis://localhost:6379"
)
```

---

# 🔒 Security Features

Afriauth includes built-in:

* OTP expiration
* retry limits
* rate limiting
* secure OTP hashing
* brute-force prevention
* replay protection

---

# ⏳ OTP Expiration

Default:

```text id="qtk0gz"
5 minutes
```

Custom configuration:

```python id="z8u6q9"
auth = AfriAuth(
    otp_expiry=300
)
```

---

# 🚦 Rate Limiting

Example:

```python id="9h3pzb"
auth = AfriAuth(
    max_requests_per_minute=3
)
```

---

# 🧠 Custom SMS Templates

```python id="f0xnnr"
await auth.send_otp(
    "+255712345678",
    template="Your verification code is {code}"
)
```

---

# 🧩 Planned Features

## ✅ Upcoming

* CLI project generator
* Authentication starter kits
* WhatsApp OTP
* Email OTP
* PIN authentication
* biometric-ready flows
* multi-provider support
* user session management
* Docker deployment templates

---

# 🏗️ Planned CLI

```bash id="jlwm55"
afriauth init
```

Generate:

```text id="s06s3z"
project/
├── main.py
├── auth/
├── routes/
├── redis/
├── docker-compose.yml
└── .env
```

---

# 🌍 Built for African Developers

Afriauth is designed for:

* fintech apps
* mobile money platforms
* SACCO systems
* startups
* e-commerce
* mobile-first apps
* telecom applications

---

# 🔗 Africa’s Talking Support

Current provider support:

* SMS OTP
* phone verification
* authentication messaging

More integrations coming soon.

---

# 📖 Documentation

Documentation coming soon.

---

# 🤝 Contributing

Contributions, ideas, and feature requests are welcome.

Feel free to open issues and pull requests.

---

# 📜 License

MIT License

---

# ❤️ Vision

Afriauth aims to become the authentication infrastructure layer for African developers.

Simple.
Fast.
Secure.
Built for Africa.
