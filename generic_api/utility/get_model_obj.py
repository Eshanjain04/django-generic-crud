class ModelDataHandler:

    def __init__(self, model, object_id=None, data={}):
        self.model = model
        self.object_id = object_id
        self.data = data

    def get_model_obj(self):
        try:
            return self.model.objects.filter(pk=self.object_id).first()
        except():
            return None

    def delete_model_object(self):
        obj = self.get_model_obj()
        if not obj:
            return None
        try:
            obj.delete()
            return True
        except():
            return None

    def update_model_object(self):
        try:
            if not self.get_model_obj():
                return None
            self.model.objects.filter(pk=self.object_id).update(**self.data)
            return True
        except():
            return None

    def create_model_object(self):
        try:
            self.model.objects.create(**self.data)
            return True
        except():
            return None

