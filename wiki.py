import wikipedia, sys
import time


def Main():
    Wiki = WikipediaSearch()
    Wiki.Start()


class WikipediaSearch:
    def __init__(self):
        self.title = ""
        self.url = ""
        self.content = ""
        self.images = []
        self.links = []

    def Start(self):
        self.StartDisplay()
        StartMenuChoice = self.StartMenu()
        if StartMenuChoice == 1:
            Query = self.RetrieveUserQuery()
            self.Search(Query)
        elif StartMenuChoice == 2:
            self.RandomArticle()

        self.DisplayContentOrSummary()

    def PageDetails(self):
        while True:
            print()
            print("🔍 What would you like to see?")
            print("1. 📄 Title")
            print("2. 🌐 URL")
            print("3. 🖼️ Images")
            print("4. 🔗 Links")
            print()
            choice = input("Enter your choice (1, 2, 3, or 4): ").strip()
            if choice == "1":
                print(f"📄 Title: {self.ReturnTitle()}")
                print()
                break
            elif choice == "2":
                print(f"🌐 URL: {self.ReturnUrl()}")
                print()
                break
            elif choice == "3":
                print(self.ReturnImages())
                print()
                break
            elif choice == "4":
                print(self.ReturnLinks())
                print()
                break
            else:
                print("❌ Invalid choice. Please try again.")

    def DisplayContentOrSummary(self):
        while True:
            print()
            print(
                "📄 Do you want to see the content, the summary, the details of the article, or choose another article?"
            )
            print("1. 📄 Content")
            print("2. 📝 Summary")
            print("3. 🔍 Details")
            print("4. 🔄 Choose another article")
            print("Q. ❌ Quit")
            print()

            choice = input("Enter your choice (1, 2, 3, 4, or Q): ").strip()
            print()
            if choice == "1":
                content = self.ReturnContent()
                print(content)
                time.sleep(5)
            elif choice == "2":
                summary = self.ReturnSummary()
                print(summary)
                time.sleep(5)
            elif choice == "3":
                self.PageDetails()
            elif choice == "4":
                self.Start()
            elif choice.upper() == "Q":
                self.Quit()
            else:
                print("❌ Invalid choice. Please try again.")

    def StartMenu(self):
        print()
        print("Please choose an option:")
        print("1. 🔍 Search for an article")
        print("2. 🎲 Get a random article")
        print()

        while True:
            choice = input("Enter your choice (1 or 2): ").strip()
            if choice.isdigit() and int(choice) in [1, 2]:
                return int(choice)
            else:
                print("❌ Invalid choice. Please try again.")

    def StartDisplay(self):
        print()
        print("===========================")
        print("🌐 Welcome to Wikipedia 🌐")
        print("===========================")
        print()

    def Search(self, query):
        print()

        QueryResults = self.SearchWikipedia(query)
        if len(QueryResults) > 0:
            query = self.Options(QueryResults)

        if query:
            self.SearchValues(query)

    def Options(self, options):
        print(f"There are {len(options)} options available.")

        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        print()

        while True:
            choice = input("Please select an option by number: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                return options[int(choice) - 1]
            else:
                print("❌ Invalid choice. Please try again.")

    def SearchWikipedia(self, query):
        print()
        try:
            search = wikipedia.search(query, results=5)
            return search
        except wikipedia.exceptions.PageError:
            return "❌ Page not found."
        except wikipedia.exceptions.DisambiguationError as e:
            return f"❌ Disambiguation error: {e.options}"
        except wikipedia.exceptions.RedirectError:
            return "❌ Redirect error."
        except wikipedia.exceptions.HTTPTimeoutError:
            return "❌ HTTP timeout error."
        except wikipedia.exceptions.WikipediaException as e:
            return f"❌ An error occurred: {e}"

    def SearchValues(self, query):
        try:
            Result = wikipedia.page(query)
            self.title = Result.title
            self.url = Result.url
            self.content = Result.content
            self.images = Result.images
            self.links = Result.links
        except wikipedia.exceptions.PageError:
            print("❌ Page not found.")
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"❌ Disambiguation error: {e.options}")
        except wikipedia.exceptions.RedirectError:
            print("❌ Redirect error.")
        except wikipedia.exceptions.HTTPTimeoutError:
            print("❌ HTTP timeout error.")
        except wikipedia.exceptions.WikipediaException as e:
            print(f"❌ An error occurred: {e}")

    def ReturnSummary(self):
        try:
            summary = wikipedia.summary(self.title, auto_suggest=False)
            return summary
        except wikipedia.exceptions.DisambiguationError as e:
            return f"❌ Disambiguation error: {e.options}"
        except wikipedia.exceptions.PageError:
            return "❌ Page not found."
        except wikipedia.exceptions.RedirectError:
            return "❌ Redirect error."
        except wikipedia.exceptions.HTTPTimeoutError:
            return "❌ HTTP timeout error."
        except wikipedia.exceptions.WikipediaException as e:
            return f"❌ An error occurred: {e}"

    def ReturnContent(self):
        return self.content

    def ReturnTitle(self):
        return self.title

    def ReturnUrl(self):
        return self.url

    def ReturnLinks(self):
        formatted_links = "\n".join(self.links)
        return f"🔗 Links:\n{formatted_links}"

    def ReturnImages(self):
        formatted_images = "\n".join(self.images)
        return f"🖼️ Images:\n{formatted_images}"

    def RandomArticle(self):
        query = wikipedia.random(pages=1)
        self.SearchValues(query)
        print(f"📄 Title: {self.ReturnTitle()}")

    def RetrieveUserQuery(self):
        query = input("🔍 What do you want to search for? (Q for exit) ").strip()
        if query.upper() == "Q":
            self.Quit()
        if not query:
            print("❌ Please enter a query")
            print()
            return self.RetrieveUserQuery()
        return query

    def Quit(self):
        print()
        print("❌" * 6)
        print("❌ Exiting ❌")
        print("❌" * 6)
        print()
        sys.exit(0)


if __name__ == "__main__":
    Main()
