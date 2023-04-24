from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    """Schema used when loading and dumping Item data"""
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class ItemUpdateSchema(Schema):
    """Schema  used when updating an item"""
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()


class PlainStoreSchema(Schema):
    """Schema used when loading and dumping Store"""
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
