from oscar.apps.partner.abstract_models import AbstractStockRecord as OscarAbstractStockRecord, AbstractPartner as OscarAbstractPartner


class Partner(OscarAbstractPartner):
    pass


class StockRecord(OscarAbstractStockRecord):
    pass



from oscar.apps.partner.models import * 
