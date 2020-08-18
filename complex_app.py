class ComplexApp:
    def __init__(self, webscraper):
        self.webscraper = webscraper
        self.keywords = {"python", "programming"}

    def scrape_to_file(self, path: str):
        # Extract keywords from a scraper, then save its contents to a file.
        scraped_keywords_set = self.extract_keywords()
        with open(path, "w") as f:
            f.write(str(scraped_keywords_set))

    def extract_keywords(self):
        # Uses the scraper to get some text, then analyse it for keywords.
        scraped_text_body: str = self.webscraper.scrape()

        # For each keyword, check if it exists in the scraped text.
        results = {k: 0 for k in self.keywords}
        for k in self.keywords:
            for word in scraped_text_body.lower().split(" "):
                if k in word:
                    results[k] += 1

        # Returns a set of keywords found in the scraped text.
        return results

