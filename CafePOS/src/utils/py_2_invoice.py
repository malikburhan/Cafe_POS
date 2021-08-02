from datetime import datetime, date
from pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item, Transaction
from pyinvoice.templates import SimpleInvoice

import win32api

def print_job(data, invoice_name='invoice.pdf', invoice_id=None, invoice_date=None, invoice_due_date=None):
    doc = SimpleInvoice(invoice_name)
    doc.invoice_info = InvoiceInfo(invoice_id, invoice_date, invoice_due_date )  # Invoice info, optional

    # Add Item
    doc.add_item(Item('Item', 'Item desc', 1, '1.1'))
    doc.finish()

    # win32api.ShellExecute(0, "print", invoice_name, None, ".", 0)
