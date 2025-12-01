# src/config.py

# --- 1. MAGIC NUMBERS (Precios Falsos) ---
# Fuente: "Vendor Data Definitions - Magic Numbers"
# Estos precios indican estados no operables y deben ser DESCARTADOS.
INVALID_PRICES = [
    666666.666, # Unquoted/Unknown
    999999.999, # Market Order (At Best)
    999999.989, # At Open Order
    999999.988, # At Close Order
    999999.979, # Pegged Order
    999999.123  # Unquoted/Unknown
]

# --- 2. MARKET STATUS CODES (Códigos de Estado) ---
# Fuente: "Continuous Trading Code"
# Solo podemos operar si el mercado está en estos estados.
VALID_STATUS_CODES = {
    "AQUIS": [5308427],
    "BME":   [5832713, 5832756],
    "CBOE":  [12255233],
    "TURQUOISE": [7608181]
}

# --- 3. LATENCIAS A SIMULAR ---
# Fuente: "Simulate execution latencies"
LATENCIES = [0, 100, 500, 1000, 2000, 3000, 4000, 5000, 
             10000, 15000, 20000, 30000, 50000, 100000]

# --- 4. VENUES (Mercados) ---
VENUES = ["BME", "AQUIS", "CBOE", "TURQUOISE"]