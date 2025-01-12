from django.db import models

class BaseEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        'users.CustomUser',  # Lazy reference to avoid circular import
        related_name="%(class)s_created",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        'users.CustomUser',
        related_name="%(class)s_updated",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

class ResultView():
    def __init__(self, is_success=False, data=None, msg=''):
        self.is_success = is_success
        self.data = data
        self.msg = msg
    def to_dict(self):
        return {
            'is_success': self.is_success,
            'data': self.data,
            'msg': self.msg
        }
    def __str__(self):
        return f'Operation Is{'' if self.is_success else 'n\'t'} Successful | Data: {self.data} | Msg: {self.msg}'

