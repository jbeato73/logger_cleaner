# Logger Cleaner

A specialized sanitization utility designed for infrastructure security and auditing. This tool processes raw connection logs to remove malformed entries and extract high-value data for cleaner reporting.

## 🚀 Key Features
* **Automated Sanitization:** Identifies and filters out lines with missing IP addresses or corrupted timestamps.
* **Security Focused:** Ensures that only well-formed connection data is passed on to downstream analytics tools.
* **UV-Powered:** Optimized for fast, isolated execution using the `uv` Python toolchain.

## 🛠️ Usage
1. **Prepare Data:** Place your `raw_connections.log` in the root directory.
2. **Execute Cleanup:**
   ```bash
   uv run clean

Execute Cleanup:
# Bash
uv run clean

# Data Logic
# The script performs a three-point check on every log entry to ensure data quality:

1. Validates the presence of a timestamp.
2. Ensures a non-empty IP address field.
3. Confirms a valid status (e.g., SUCCESS/ERROR).