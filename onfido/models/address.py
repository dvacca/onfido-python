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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from onfido.models.country_codes import CountryCodes
from typing import Optional, Set
from typing_extensions import Self

class Address(BaseModel):
    """
    Address
    """ # noqa: E501
    flat_number: Optional[StrictStr] = Field(default=None, description="The flat number of this address")
    building_number: Optional[StrictStr] = Field(default=None, description="The building number of this address")
    building_name: Optional[StrictStr] = Field(default=None, description="The building name of this address")
    street: Optional[StrictStr] = Field(default=None, description="The street of the applicant's address")
    sub_street: Optional[StrictStr] = Field(default=None, description="The sub-street of the applicant's address")
    town: Optional[StrictStr] = Field(default=None, description="The town of the applicant's address")
    postcode: StrictStr = Field(description="The postcode or ZIP of the applicant's address")
    country: CountryCodes = Field(description="The 3 character ISO country code of this address. For example, GBR is the country code for the United Kingdom")
    state: Optional[StrictStr] = Field(default=None, description="The address state. US states must use the USPS abbreviation (see also ISO 3166-2:US), for example AK, CA, or TX.")
    line1: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Line 1 of the applicant's address")
    line2: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Line 2 of the applicant's address")
    line3: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Line 3 of the applicant's address")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["flat_number", "building_number", "building_name", "street", "sub_street", "town", "postcode", "country", "state", "line1", "line2", "line3"]

    @field_validator('line1')
    def line1_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[^!$%^*=<>]*$", value):
            raise ValueError(r"must validate the regular expression /^[^!$%^*=<>]*$/")
        return value

    @field_validator('line2')
    def line2_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[^!$%^*=<>]*$", value):
            raise ValueError(r"must validate the regular expression /^[^!$%^*=<>]*$/")
        return value

    @field_validator('line3')
    def line3_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[^!$%^*=<>]*$", value):
            raise ValueError(r"must validate the regular expression /^[^!$%^*=<>]*$/")
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
        """Create an instance of Address from a JSON string"""
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

        # set to None if line1 (nullable) is None
        # and model_fields_set contains the field
        if self.line1 is None and "line1" in self.model_fields_set:
            _dict['line1'] = None

        # set to None if line2 (nullable) is None
        # and model_fields_set contains the field
        if self.line2 is None and "line2" in self.model_fields_set:
            _dict['line2'] = None

        # set to None if line3 (nullable) is None
        # and model_fields_set contains the field
        if self.line3 is None and "line3" in self.model_fields_set:
            _dict['line3'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Address from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "flat_number": obj.get("flat_number"),
            "building_number": obj.get("building_number"),
            "building_name": obj.get("building_name"),
            "street": obj.get("street"),
            "sub_street": obj.get("sub_street"),
            "town": obj.get("town"),
            "postcode": obj.get("postcode"),
            "country": obj.get("country"),
            "state": obj.get("state"),
            "line1": obj.get("line1"),
            "line2": obj.get("line2"),
            "line3": obj.get("line3")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


