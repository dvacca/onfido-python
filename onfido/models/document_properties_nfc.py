# coding: utf-8

"""
    Onfido API v3.6

    The Onfido API

    The version of the OpenAPI document: 3.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DocumentPropertiesNfc(BaseModel):
    """
    DocumentPropertiesNfc
    """ # noqa: E501
    document_type: Optional[StrictStr] = None
    issuing_country: Optional[StrictStr] = None
    full_name: Optional[StrictStr] = None
    document_number: Optional[StrictStr] = None
    nationality: Optional[StrictStr] = None
    date_of_birth: Optional[date] = None
    gender: Optional[StrictStr] = None
    date_of_expiry: Optional[date] = None
    personal_number: Optional[StrictStr] = None
    place_of_birth: Optional[StrictStr] = None
    address: Optional[StrictStr] = None
    issuing_date: Optional[date] = None
    issuing_authority: Optional[StrictStr] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["document_type", "issuing_country", "full_name", "document_number", "nationality", "date_of_birth", "gender", "date_of_expiry", "personal_number", "place_of_birth", "address", "issuing_date", "issuing_authority"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DocumentPropertiesNfc from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocumentPropertiesNfc from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "document_type": obj.get("document_type"),
            "issuing_country": obj.get("issuing_country"),
            "full_name": obj.get("full_name"),
            "document_number": obj.get("document_number"),
            "nationality": obj.get("nationality"),
            "date_of_birth": obj.get("date_of_birth"),
            "gender": obj.get("gender"),
            "date_of_expiry": obj.get("date_of_expiry"),
            "personal_number": obj.get("personal_number"),
            "place_of_birth": obj.get("place_of_birth"),
            "address": obj.get("address"),
            "issuing_date": obj.get("issuing_date"),
            "issuing_authority": obj.get("issuing_authority")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


