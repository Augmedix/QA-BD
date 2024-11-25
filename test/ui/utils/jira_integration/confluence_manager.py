"""
Use to manage confluence pages.
"""
import pytest
from atlassian import Confluence
from bs4 import BeautifulSoup


class ConfluenceManager:
    """
    Used to manage confluence i.e.: loading a page, parsing for analysis etc.
    """

    def __init__(self):
        self.confluence = Confluence(
            url=pytest.configs.get_config('jira_url'),
            username=pytest.configs.get_config('jira_username'),
            password=pytest.configs.get_config('jira_api_token')
        )

    def get_page_body(self, space='EN', title='Live App QA Signed Off APK'):
        """
        Get page body of a space wiki.
        :param space specifies the desired space where expected wiki is created. Default is <b>EN</b>.
        :param title expected title of the wiki. Default is <b>Live App QA Signed Off APK</b>
        """
        page_body = self.confluence.get_page_by_title(space=space, title=title, expand='body.storage')
        return page_body['body']['storage']['value']

    def get_table(self, space='EN', page_title='Live App QA Signed Off APK', table_position=1):
        """
        Gets the table as list of dicts where each dict represents a specific row.
        is assumed.
        :param space specifies the desired space where expected wiki is created. Default is <b>EN</b>.
        :param page_title expected title of the wiki. Default is <b>Live App QA Signed Off APK</b>
        :param table_position determines which table to extract. Defaults to second table as there is always
        a table stakeholder at the top.
        """
        page_body = self.get_page_body(space=space, title=page_title)
        _table = BeautifulSoup(page_body, 'html.parser').find_all('table')[table_position]
        rows = _table.find_all('tr')

        headers = {}
        theads = _table.find_all('th')
        for index, thead in enumerate(theads):
            headers[index] = thead.text.strip().lower()
        data = []

        for row in rows:
            cells = row.find_all('td')
            if theads:
                items = {}
                if len(cells) > 0:
                    for key,  value in headers.items():
                        items[value] = cells[key].text
            else:
                items = []
                for index in cells:
                    items.append(index.text.strip())
            if items:
                data.append(items)
        return data
