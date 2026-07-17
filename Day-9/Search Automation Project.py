import webbrowser
import urllib.parse
from datetime import datetime
import time

# Read dorks
with open("dorks.txt", "r", encoding="utf-8") as f:
    dorks = [line.strip() for line in f if line.strip()]

with open("results.txt", "w", encoding="utf-8") as out:

    out.write("=" * 70 + "\n")
    out.write("SEARCH AUTOMATION REPORT\n")
    out.write("=" * 70 + "\n")
    out.write(f"Generated: {datetime.now()}\n\n")

    for i, dork in enumerate(dorks, start=1):

        print(f"Opening search {i}: {dork}")

        search_url = (
            "https://www.google.com/search?q="
            + urllib.parse.quote_plus(dork)
        )

        # Opens the search in your default browser
        webbrowser.open_new_tab(search_url)

        out.write(f"Dork {i}\n")
        out.write(f"Query : {dork}\n")
        out.write(f"Search URL : {search_url}\n")
        out.write("-" * 60 + "\n")

        # Delay between opening tabs
        time.sleep(3)

print("Completed!")