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
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ProofOfAddressProperties(BaseModel):
    """
    ProofOfAddressProperties
    """ # noqa: E501
    address: Optional[StrictStr] = Field(default=None, description="This property provides the address on the document.")
    document_type: Optional[StrictStr] = Field(default=None, description="This property provides the document type according to the set of supported documents.")
    first_names: Optional[StrictStr] = Field(default=None, description="This property provides the first names on the document, including any initials and middle names.")
    last_names: Optional[StrictStr] = Field(default=None, description="This property provided the last names on the document.")
    issue_date: Optional[date] = Field(default=None, description="This property provides the issue date of the document.")
    issuer: Optional[StrictStr] = Field(default=None, description="This property provides the document issuer (e.g. HSBC, British Gas).")
    summary_period_start: Optional[date] = Field(default=None, description="This property provides the summary period start date.")
    summary_period_end: Optional[date] = Field(default=None, description="This property provides the summary period end date.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["address", "document_type", "first_names", "last_names", "issue_date", "issuer", "summary_period_start", "summary_period_end"]

    @field_validator('document_type')
    def document_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['bank_building_society_statement', 'utility_bill', 'council_tax', 'benefit_letters', 'mortgage_statement', 'mobile_phone_bill', 'general_letter', 'insurance_statement', 'pension_property_statement_letter', 'identity_document_with_address', 'exchange_house_statement']):
            raise ValueError("must be one of enum values ('bank_building_society_statement', 'utility_bill', 'council_tax', 'benefit_letters', 'mortgage_statement', 'mobile_phone_bill', 'general_letter', 'insurance_statement', 'pension_property_statement_letter', 'identity_document_with_address', 'exchange_house_statement')")
        return value

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
        """Create an instance of ProofOfAddressProperties from a JSON string"""
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
        """Create an instance of ProofOfAddressProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": obj.get("address"),
            "document_type": obj.get("document_type"),
            "first_names": obj.get("first_names"),
            "last_names": obj.get("last_names"),
            "issue_date": obj.get("issue_date"),
            "issuer": obj.get("issuer"),
            "summary_period_start": obj.get("summary_period_start"),
            "summary_period_end": obj.get("summary_period_end")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


