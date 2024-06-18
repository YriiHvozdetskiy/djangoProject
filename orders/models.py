from django.contrib.auth.models import User
from django.db import models


class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    """
    при видалені user буде:
    on_delete:
        SET_NULL - коли видаляєм user всіх полях з якими був звязаний user буде проставлено null
        CASCADE - коли видаляєм user, виконається каскадне видалення всіх замовлень звязаних з користувачем
        PROTECT - не дозвелить видалити user, поки є звязані з ним закази
        
    null=True - всі раніше створені замовлення отримують пустого user (це якщо раніше були створені замовлення)
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
