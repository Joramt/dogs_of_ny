from urllib import parse


class QueryHelper():
    def queryStringToDict(url=None, query_string=None):
        # TODO : test url param against URL pattern

        if not url and not query_string:
            raise ValueError("You must provide either an URL or a querystring")

        # pep8 ternary identation https://stackoverflow.com/a/26233610/4780833
        qs = (
            query_string
            if query_string is not None
            else parse.urlsplit(url).query)
        return parse.parse_qsl(qs)
