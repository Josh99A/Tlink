from oscar.apps.dashboard.catalogue.tables import ProductTable as OscarProductTable


class ProductTable(OscarProductTable):
    class Meta(OscarProductTable.Meta):
        pass