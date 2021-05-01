import re


class PageViewParser:

    LOG_PATTERN = r"(\d+\.\d+\.\d+\.\d+) - " \
                  r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.*)\] .* " \
                  r"(.*:\/\/www\..*\.com.*) \| " \
                  r"device_id\:(.*) \| " \
                  r"referer\: (.*\:\/\/.*)"

    URL_PATTERN = r".*?(\?ad_creative_id=)?(\d*)?([&\?]campaign_id=)(\d*)?"

    def parse(self, df):
        return [self.parse_log_line(tuple(logline)[0]) for logline in df.collect()]

    @staticmethod
    def parse_log_line(logline):
        match = re.search(PageViewParser.LOG_PATTERN, logline)
        if match is None:
            raise Exception("Invalid logline: %s" % logline)
        match_url = re.search(PageViewParser.URL_PATTERN, match.group(3))
        return (
            match.group(1),  # ip_address
            match.group(2),  # datetime
            match.group(3),  # url
            "" if match_url is None else match_url.group(4),  # campaign_id
            "" if match_url is None else match_url.group(2),  # ad_creative_id=
            match.group(4),  # device_id
            match.group(5)  # referer
        )




