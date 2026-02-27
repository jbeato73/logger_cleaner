from datetime import datetime


def clean_logs():
    print("🧹 Cleaning logs...")
    cleaned_lines = []

    # 1. Open and read the raw log
    with open("raw_connections.log", "r") as file:
        for line in file:
            # 2. Split the line into Timestamp, IP, and Status
            parts = line.split(",")

            # 3. Logic: Must have 3 parts AND the IP (parts[1]) cannot be empty
            if len(parts) == 3 and parts[1].strip() != "":
                cleaned_lines.append(line.strip())

    # 4. Save the cleaned results to a new file
    with open("cleaned_audit.log", "w") as output_file:
        output_file.write("\n".join(cleaned_lines))

    return len(cleaned_lines)


def main():
    # Run the cleaning logic and get the count of successful lines
    count = clean_logs()

    # Update README timestamp
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("README.txt", "a") as f:
        f.write(f"\nLAST EXECUTION: {now} (EST) - Cleaned {count} entries.\n")

    print(f"✅ Cleanup complete at {now}. {count} lines saved to cleaned_audit.log")


if __name__ == "__main__":
    main()
