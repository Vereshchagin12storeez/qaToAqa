GET_ALL_PRODUCTS_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "results": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "barcode": {
                            "type": "string"
                        },
                        "category": {
                            "type": "string"
                        },
                        "family": {
                            "type": "string"
                        },
                        "product_name": {
                            "type": "string"
                        },
                        "is_active": {
                            "type": "boolean",
                            "value": True
                        },
                        "article": {
                            "type": "string"
                        },
                        "size": {
                            "type": "string"
                        },
                        "color": {
                            "type": "string"
                        },
                        "fabric": {
                            "type": "string"
                        },
                        "super_model_name": {
                            "type": "string"
                        },
                        "gender": {
                            "type": "string"
                        },
                        "sizes": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "string"
                                }
                            ]
                        },
                        "barcode_alt": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "string"
                                }
                            ]
                        },
                        "description": {
                            "type": "string"
                        },
                        "images": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                }
                            ]
                        },
                        "site_category": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "slug": {
                                            "type": "string"
                                        },
                                        "title": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "slug",
                                        "title"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "slug": {
                                            "type": "string"
                                        },
                                        "title": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "slug",
                                        "title"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "slug": {
                                            "type": "string"
                                        },
                                        "title": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "slug",
                                        "title"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "slug": {
                                            "type": "string"
                                        },
                                        "title": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "slug",
                                        "title"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "slug": {
                                            "type": "string"
                                        },
                                        "title": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "slug",
                                        "title"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "slug": {
                                            "type": "string"
                                        },
                                        "title": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "slug",
                                        "title"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "slug": {
                                            "type": "string"
                                        },
                                        "title": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "slug",
                                        "title"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "slug": {
                                            "type": "string"
                                        },
                                        "title": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "slug",
                                        "title"
                                    ]
                                }
                            ]
                        },
                        "size_description": {
                            "type": "string"
                        },
                        "preview": {
                            "type": "string"
                        },
                        "capsules": {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "parent_season": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "id",
                                "title",
                                "parent_season"
                            ]
                        },
                        "super_model_merging_code": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "barcode",
                        "category",
                        "family",
                        "product_name",
                        "is_active",
                        "article",
                        "size",
                        "color",
                        "fabric",
                        "super_model_name",
                        "gender",
                        "sizes",
                        "barcode_alt",
                        "description",
                        "images",
                        "site_category",
                        "size_description",
                        "preview",
                        "capsules",
                        "super_model_merging_code"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "barcode": {
                            "type": "string"
                        },
                        "category": {
                            "type": "string"
                        },
                        "family": {
                            "type": "string"
                        },
                        "product_name": {
                            "type": "string"
                        },
                        "article": {
                            "type": "string"
                        },
                        "size": {
                            "type": "string"
                        },
                        "color": {
                            "type": "string"
                        },
                        "super_model_name": {
                            "type": "string"
                        },
                        "gender": {
                            "type": "string"
                        },
                        "sizes": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "string"
                                }
                            ]
                        },
                        "barcode_alt": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "string"
                                }
                            ]
                        },
                        "site_category": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "slug": {
                                            "type": "string"
                                        },
                                        "title": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "slug",
                                        "title"
                                    ]
                                }
                            ]
                        },
                        "capsules": {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "parent_season": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "id",
                                "title",
                                "parent_season"
                            ]
                        },
                        "super_model_merging_code": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "barcode",
                        "category",
                        "family",
                        "product_name",
                        "article",
                        "size",
                        "color",
                        "super_model_name",
                        "gender",
                        "sizes",
                        "barcode_alt",
                        "site_category",
                        "capsules",
                        "super_model_merging_code"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "barcode": {
                            "type": "string"
                        },
                        "category": {
                            "type": "string"
                        },
                        "family": {
                            "type": "string"
                        },
                        "product_name": {
                            "type": "string"
                        },
                        "article": {
                            "type": "string"
                        },
                        "size": {
                            "type": "string"
                        },
                        "color": {
                            "type": "string"
                        },
                        "fabric": {
                            "type": "string"
                        },
                        "super_model_name": {
                            "type": "string"
                        },
                        "gender": {
                            "type": "string"
                        },
                        "sizes": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "string"
                                }
                            ]
                        },
                        "barcode_alt": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "string"
                                }
                            ]
                        },
                        "total_look": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                }
                            ]
                        },
                        "description": {
                            "type": "string"
                        },
                        "images": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                }
                            ]
                        }
                    },
                    "required": [
                        "barcode",
                        "category",
                        "family",
                        "product_name",
                        "article",
                        "size",
                        "color",
                        "fabric",
                        "super_model_name",
                        "gender",
                        "sizes",
                        "barcode_alt",
                        "total_look",
                        "description",
                        "images"
                    ]
                }
            ]
        }
    },
    "required": [
        "results"
    ]
}
