from models.sms_notifier import SMSNotifier
from models.StockObservable import ProductStockObservable
from models.email_notifier import EmailNotifier
from models.sms_notifier import SMSNotifier

iphone_observable = ProductStockObservable("iphone14")
mail_observer = EmailNotifier(iphone_observable)
sms_observer = SMSNotifier(iphone_observable)
iphone_observable.add_observer(mail_observer)
iphone_observable.add_observer(sms_observer)
iphone_observable.set_data(5)


