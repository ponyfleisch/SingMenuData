import rumps, requests, bs4, time

class SingMenuData(rumps.App):
    def __init__(self, title):
        super(SingMenuData, self).__init__(title)
        self.title = "loading..."
        self.last_update = time.time()


    @rumps.clicked("update")
    def sayhi(self, _):
        self.request_data(False)


    @rumps.timer(60)
    def request_data(self, sender):
        doc = bs4.BeautifulSoup(requests.get("https://hi.singtel.com/welcome.do").text, "html.parser")
        totals = doc.select(".divTblSocialPlans .tblRowMiddle span")
        total = sum(map((lambda plan: int(plan.getText().strip().split()[0])), totals))
        self.title = str(total) + " MB"
        self.last_update = time.time()

    @rumps.timer(1)
    def update_menu(self, sender):
        self._menu['update'].title = "Updated " + str(int(time.time() - self.last_update)) + " seconds ago"


if __name__ == "__main__":
    SingMenuData("Singtel Data").run()
