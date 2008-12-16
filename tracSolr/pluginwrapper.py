from trac.core import *
from trac.ticket import *
from trac.wiki import *

class SolrModule(Component):
    implements(IWikiChangeListener, ITicketChangeListener)

    

    def wiki_page_added(self, page):
        self.env.log.debug("page created")

    def wiki_page_changed(self, page, version, t, comment, author, ipnr):
        self.env.log.debug(page)

    def wiki_page_deleted(self, page):
        pass

    def wiki_page_version_deleted(self, page):
        pass

    def ticket_created(self, ticket):
        pass

    def ticket_changed(self, ticket, comment, author, old_values):
        pass

    def ticket_deleted(self, ticket):
        pass
