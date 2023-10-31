from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    url = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    depth = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0
        super(MenuItem, self).save(*args, **kwargs)

    def get_ancestors(self):
        ancestors = []
        current_item = self
        while current_item is not None:
            ancestors.insert(0, current_item)
            current_item = current_item.parent
        return ancestors
