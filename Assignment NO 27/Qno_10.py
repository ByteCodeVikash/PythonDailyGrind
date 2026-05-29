"""
10.
Write a function that receives a list of strings representing dates in various formats. Use
list slicing and conditional checks inside a loop to standardize them into a single string
format, returning a fully processed list.
"""


def standardize_dates(date_list):
    standardized_list = []

    # Dictionary to map short month names to 2-digit numbers
    month_map = {
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12",
    }

    for date_str in date_list:
        # Clean up any accidental leading/trailing spaces
        date_str = date_str.strip()

        # Format 1: "YYYY-MM-DD" (e.g., "2026-05-29") -> Already standard
        if "-" in date_str and len(date_str) == 10 and date_str[4] == "-":
            standardized_list.append(date_str)

        # Format 2: "DD/MM/YYYY" (e.g., "29/05/2026")
        elif "/" in date_str:
            # Use slicing to extract components based on exact character positions
            day = date_str[0:2]
            month = date_str[3:5]
            year = date_str[6:10]
            standardized_list.append(f"{year}-{month}-{day}")

        # Format 3: "DD-Mon-YYYY" (e.g., "29-May-2026")
        elif "-" in date_str and len(date_str) == 11:
            day = date_str[0:2]
            month_name = date_str[3:6]  # Slices the 3-letter month abbreviation
            year = date_str[7:11]

            # Convert month abbreviation to numbers using our map
            month = month_map.get(month_name, "01")
            standardized_list.append(f"{year}-{month}-{day}")

        # Format 4: "Month DD, YYYY" (e.g., "May 29, 2026")
        elif "," in date_str:
            # Slice first 3 characters for month name
            month_name = date_str[0:3]
            # Slice characters between month and comma for day
            day = date_str[4:6]
            # Slice last 4 characters for year
            year = date_str[-4:]

            month = month_map.get(month_name, "01")
            standardized_list.append(f"{year}-{month}-{day}")

    return standardized_list


# --- Example Usage to verify the function ---
mixed_dates = [
    "2026-05-29",  # Format 1
    "29/05/2026",  # Format 2
    "29-May-2026",  # Format 3
    "May 29, 2026",  # Format 4
]

processed_dates = standardize_dates(mixed_dates)
print(processed_dates)
# Output: ['2026-05-29', '2026-05-29', '2026-05-29', '2026-05-29']
