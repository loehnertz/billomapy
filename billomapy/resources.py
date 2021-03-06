"""
KEY and DATA_KEYS FOR THE API
"""

PROPERTY_VALUES = '-property-values'
PROPERTY_VALUE = '-property-value'

TAGS = '-tags'
TAG = '-tag'

ITEMS = '-items'
ITEM = '-item'

COMMENTS = '-comments'
COMMENT = '-comment'

PAYMENTS = '-payments'
PAYMENT = '-payment'

EMAIL_RECEIVERS = '-email-receivers'
EMAIL_RECEIVER = '-email-receiver'

DOCUMENTS = '-documents'
DOCUMENT = '-document'


CLIENTS = 'clients'
CLIENT = 'client'

CLIENT_PROPERTIES = CLIENT + PROPERTY_VALUES
CLIENT_PROPERTY = CLIENT + PROPERTY_VALUE

CLIENT_TAGS = CLIENT + TAGS
CLIENT_TAG = CLIENT + TAG

CONTACTS = 'contacts'
CONTACT = 'contact'

SUPPLIERS = 'suppliers'
SUPPLIER = 'supplier'

SUPPLIER_PROPERTIES = SUPPLIER + PROPERTY_VALUES
SUPPLIER_PROPERTY = SUPPLIER + PROPERTY_VALUE

SUPPLIER_TAGS = SUPPLIER + TAGS
SUPPLIER_TAG = SUPPLIER + TAG

ARTICLES = 'articles'
ARTICLE = 'article'

ARTICLE_PROPERTIES = ARTICLE + PROPERTY_VALUES
ARTICLE_PROPERTY = ARTICLE + PROPERTY_VALUE

ARTICLE_TAGS = ARTICLE + TAGS
ARTICLE_TAG = ARTICLE + TAG

UNITS = 'units'
UNIT = 'unit'

INVOICES = 'invoices'
INVOICE = 'invoice'

INVOICE_ITEMS = INVOICE + ITEMS
INVOICE_ITEM = INVOICE + ITEM

INVOICE_COMMENTS = INVOICE + COMMENTS
INVOICE_COMMENT = INVOICE + COMMENT

INVOICE_PAYMENTS = INVOICE + PAYMENTS
INVOICE_PAYMENT = INVOICE + PAYMENT

INVOICE_TAGS = INVOICE + TAGS
INVOICE_TAG = INVOICE + TAG

RECURRINGS = 'recurrings'
RECURRING = 'recurring'

RECURRING_ITEMS = RECURRING + ITEMS
RECURRING_ITEM = RECURRING + ITEM

RECURRING_TAGS = RECURRING + TAGS
RECURRING_TAG = RECURRING + TAG

RECURRING_EMAIL_RECEIVERS = RECURRING + EMAIL_RECEIVERS
RECURRING_EMAIL_RECEIVER = RECURRING + EMAIL_RECEIVER

INCOMINGS = 'incomings'
INCOMING = 'incoming'

INCOMING_COMMENTS = INCOMING + COMMENTS
INCOMING_COMMENT = INCOMING + COMMENT

INCOMING_PAYMENTS = INCOMING + PAYMENTS
INCOMING_PAYMENT = INCOMING + PAYMENT

INCOMING_PROPERTIES = INCOMING + PROPERTY_VALUES
INCOMING_PROPERTY = INCOMING + PROPERTY_VALUE

INCOMING_TAGS = INCOMING + TAGS
INCOMING_TAG = INCOMING + TAG

INBOX = 'inbox'

INBOX_DOCUMENTS = INBOX + DOCUMENTS
INBOX_DOCUMENT = INBOX + DOCUMENT

OFFERS = 'offers'
OFFER = 'offer'

OFFER_ITEMS = OFFER + ITEMS
OFFER_ITEM = OFFER + ITEM

OFFER_COMMENTS = OFFER + COMMENTS
OFFER_COMMENT = OFFER + COMMENT

OFFER_TAGS = OFFER + TAGS
OFFER_TAG = OFFER + TAG

CREDIT_NOTES = 'credit-notes'
CREDIT_NOTE = 'credit-note'

CREDIT_NOTE_ITEMS = CREDIT_NOTE + ITEMS
CREDIT_NOTE_ITEM = CREDIT_NOTE + ITEM

CREDIT_NOTE_COMMENTS = CREDIT_NOTE + COMMENTS
CREDIT_NOTE_COMMENT = CREDIT_NOTE + COMMENT

CREDIT_NOTE_PAYMENTS = CREDIT_NOTE + PAYMENTS
CREDIT_NOTE_PAYMENT = CREDIT_NOTE + PAYMENT

CREDIT_NOTE_TAGS = CREDIT_NOTE + TAGS
CREDIT_NOTE_TAG = CREDIT_NOTE + TAG

CONFIRMATIONS = 'confirmations'
CONFIRMATION = 'confirmation'

CONFIRMATION_ITEMS = CONFIRMATION + ITEMS
CONFIRMATION_ITEM = CONFIRMATION + ITEM

CONFIRMATION_COMMENTS = CONFIRMATION + COMMENTS
CONFIRMATION_COMMENT = CONFIRMATION + COMMENT

CONFIRMATION_TAGS = CONFIRMATION + TAGS
CONFIRMATION_TAG = CONFIRMATION + TAG

REMINDERS = 'reminders'
REMINDER = 'reminder'

REMINDER_ITEMS = REMINDER + ITEMS
REMINDER_ITEM = REMINDER + ITEM

REMINDER_TAGS = REMINDER + TAGS
REMINDER_TAG = REMINDER + TAG

DELIVERY_NOTES = 'delivery-notes'
DELIVERY_NOTE = 'delivery-note'

DELIVERY_NOTE_ITEMS = DELIVERY_NOTE + ITEMS
DELIVERY_NOTE_ITEM = DELIVERY_NOTE + ITEM

DELIVERY_NOTE_COMMENTS = DELIVERY_NOTE + COMMENTS
DELIVERY_NOTE_COMMENT = DELIVERY_NOTE + COMMENT

DELIVERY_NOTE_TAGS = DELIVERY_NOTE + TAGS
DELIVERY_NOTE_TAG = DELIVERY_NOTE + TAG

LETTERS = 'letters'
LETTER = 'letter'

LETTER_COMMENTS = LETTER + COMMENTS
LETTER_COMMENT = LETTER + COMMENT

LETTER_TAGS = LETTER + TAGS
LETTER_TAG = LETTER + TAG

TEMPLATES = 'templates'
TEMPLATE = 'template'

USER = 'users'
USERS = 'users'

"""
COMMANDS for the API
"""

COMPLETE = 'complete'
PDF = 'pdf'
UPLOAD_SIGNATURE = 'upload-signature'
EMAIL = 'email'
CANCEL = 'cancel'
UNCANCEL = 'uncancel'
WIN = 'win'
LOSE = 'lose'
CLEAR = 'clear'
UNCLEAR = 'unclear'
