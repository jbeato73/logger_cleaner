# =============================================================================
# logger_cleaner.py
#
# Author  : Jose M. Beato
# Created : March 9, 2026
# Built with the assistance of Claude (Anthropic) — claude.ai
#
# Description:
#   Reads a raw connection log file, validates each line for correct
#   format (timestamp, IP address, status), strips malformed entries,
#   and writes a clean audit log. Updates a README with execution
#   timestamp on each run.
#
# Project Setup (run in terminal before opening VS Code):
# ─────────────────────────────────────────────────────
#   1. cd /Users/jmb/PythonProjects
#   2. uv init logger-cleaner
#   3. cd logger-cleaner
#   4. code .
#   5. python3 -m venv .venv
#   6. source .venv/bin/activate
#   # No extra packages — 100% Python standard library
#   # Create this file as: logger_cleaner.py
#
# GitHub Commit (after completing):
# ──────────────────────────────────
#   git add logger_cleaner.py
#   git commit -m "refactor: standardize logger_cleaner.py header and structure"
#   git push origin main
# =============================================================================

from datetime import datetime  # Built-in: timestamp generation


# =============================================================================
# SECTION 1 — CONFIGURATION
# Best Practice: Keep file paths at the top so they're easy to find and update.
# =============================================================================

INPUT_FILE  = "raw_connections.log"   # Raw log file to process
OUTPUT_FILE = "cleaned_audit.log"     # Cleaned output log
README_FILE = "README.txt"            # Execution timestamp log


# =============================================================================
# SECTION 2 — CORE LOGIC
# Best Practice: Separate the cleaning logic from the entry point so
# this function can be imported and tested independently.
# =============================================================================


def clean_logs():
    """
    Reads raw_connections.log line by line, validates each entry,
    and writes only well-formed lines to cleaned_audit.log.

    A valid line must have exactly 3 comma-separated parts and a
    non-empty IP address field (index 1).

    Returns:
        int: Count of valid lines written to the output file.
    """
    print("[INFO] logger_cleaner.py — Starting...")
    cleaned_lines = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            # Split the line into: Timestamp, IP, Status
            parts = line.split(",")

            # Validation: must have 3 parts AND a non-empty IP field
            if len(parts) == 3 and parts[1].strip() != "":
                cleaned_lines.append(line.strip())

    with open(OUTPUT_FILE, "w") as output_file:
        output_file.write("\n".join(cleaned_lines))

    print(f"[INFO] Processed {len(cleaned_lines)} valid entries → '{OUTPUT_FILE}'")
    return len(cleaned_lines)


# =============================================================================
# SECTION 3 — README UPDATER
# Best Practice: Log execution history so you can audit when the script ran.
# =============================================================================


def update_readme(count):
    """
    Appends the current execution timestamp and result count to README.txt.

    Args:
        count (int): Number of valid log entries written.
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(README_FILE, "a") as f:
        f.write(f"\nLAST EXECUTION: {now} (EST) — Cleaned {count} entries.\n")
    print(f"[INFO] README updated with execution timestamp.")


# =============================================================================
# SECTION 4 — SUMMARY PRINT
# Best Practice: Always print a human-readable summary so you know what
# happened at a glance without opening output files.
# =============================================================================


def print_summary(count):
    """
    Prints a formatted run summary to the console.

    Args:
        count (int): Number of valid entries processed.
    """
    print()
    print("=" * 60)
    print("  LOGGER CLEANER — SUMMARY REPORT")
    print("  Jose M. Beato | March 9, 2026")
    print("=" * 60)
    print(f"  Input file      : {INPUT_FILE}")
    print(f"  Output file     : {OUTPUT_FILE}")
    print(f"  Valid entries   : {count}")
    print("=" * 60)
    print()


# =============================================================================
# SECTION 5 — MAIN ENTRY POINT
# Best Practice: Always use `if __name__ == "__main__"` to protect your
# main logic. This allows other scripts to import your functions without
# automatically running the whole pipeline.
# =============================================================================


def main():
    """
    Orchestrates the full pipeline:
    Clean Logs → Update README → Print Summary
    """
    count = clean_logs()
    update_readme(count)
    print_summary(count)


if __name__ == "__main__":
    main()

