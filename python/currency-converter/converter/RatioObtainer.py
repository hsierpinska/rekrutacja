import json, datetime, urllib.request


class RatioObtainer:
    base = None
    target = None

    def __init__(self, base, target):
        self.base = base
        self.target = target

    def was_ratio_saved_today(self):

        try:
            with open('ratios.json') as f:
                f_data = json.loads(f.read())
                for i in f_data:
                    if i["date_fetched"] == str(datetime.date.today()):
                        return True
                return False
        except FileNotFoundError:
            return False

        # This function checks if given ratio was saved today and if the file with ratios is created at all
        # should return false when file doesn't exist or if there's no today's exchange rate for given values at all
        # should return true otherwise
        pass

    def fetch_ratio(self):

        url = 'https://api.exchangerate.host/latest?base={self.base}&symbols={self.target}'
        self.save_ratio((json.load(urllib.request.urlopen(url)))['rates'][self.target])
        # This function calls API for today's exchange ratio
        # Should ask API for today's exchange ratio with given base and target currency
        # and call save_ratio method to save it
        pass

    def save_ratio(self, ratio):
        filename = "ratios.json"

        with open(filename, 'r') as f:
            f_data = json.loads(f.read())
            for i in f_data:
                if i["base_currency"] == self.base and i["target_currency"] == self.target:
                    i["date_fetched"] = str(datetime.date.today())
                    i["ratio"] = ratio
                    return
            current_ratio = {
                "base_currency": self.base,
                "target_currency": self.target,
                "date_fetched": str(datetime.date.today()),
                "ratio": ratio
            }
            f_data.append(current_ratio)
        with open(filename, "w") as f:
            json.dump(f_data, f)

        # Should save or update exchange rate for given pair in json file
        # takes ratio as argument
        # example file structure is shipped in project's directory, yours can differ (as long as it works)
        pass

    def get_matched_ratio_value(self):
        filename = "ratios.json"
        with open(filename, 'r') as f:
            f_data = json.loads(f.read())
            for i in f_data:
                if i["base_currency"] == self.base and i["target_currency"] == self.target:
                    return i["ratio"]
        # Should read file and receive exchange rate for given base and target currency from that file
        pass
