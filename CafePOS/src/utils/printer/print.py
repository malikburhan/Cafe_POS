from pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item, Transaction
from pyinvoice.templates import SimpleInvoice

import win32api

def print_job(data=None, invoice_name='invoice.pdf'):
    # doc = SimpleInvoice(invoice_name)
    # doc.invoice_info = InvoiceInfo(invoice_id, invoice_date, invoice_due_date )  # Invoice info, optional

    # doc.add_item(Item('Item', 'Item desc', 1, '1.1')) # name, description, units, unit_price
    # doc.set_bottom_tip(f"{1}<br />{2}<br />{3}")
    # doc.finish()
    print(data)

    # win32api.ShellExecute(0, "print", invoice_name, None, ".", 0)

print_job()