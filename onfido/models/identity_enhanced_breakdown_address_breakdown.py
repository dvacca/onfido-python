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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from onfido.models.identity_enhanced_breakdown_address_breakdown_credit_agencies import IdentityEnhancedBreakdownAddressBreakdownCreditAgencies
from onfido.models.identity_enhanced_breakdown_address_breakdown_telephone_database import IdentityEnhancedBreakdownAddressBreakdownTelephoneDatabase
from onfido.models.identity_enhanced_breakdown_address_breakdown_voting_register import IdentityEnhancedBreakdownAddressBreakdownVotingRegister
from typing import Optional, Set
from typing_extensions import Self

class IdentityEnhancedBreakdownAddressBreakdown(BaseModel):
    """
    IdentityEnhancedBreakdownAddressBreakdown
    """ # noqa: E501
    credit_agencies: Optional[IdentityEnhancedBreakdownAddressBreakdownCreditAgencies] = None
    telephone_database: Optional[IdentityEnhancedBreakdownAddressBreakdownTelephoneDatabase] = None
    voting_register: Optional[IdentityEnhancedBreakdownAddressBreakdownVotingRegister] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["credit_agencies", "telephone_database", "voting_register"]

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
        """Create an instance of IdentityEnhancedBreakdownAddressBreakdown from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of credit_agencies
        if self.credit_agencies:
            _dict['credit_agencies'] = self.credit_agencies.to_dict()
        # override the default output from pydantic by calling `to_dict()` of telephone_database
        if self.telephone_database:
            _dict['telephone_database'] = self.telephone_database.to_dict()
        # override the default output from pydantic by calling `to_dict()` of voting_register
        if self.voting_register:
            _dict['voting_register'] = self.voting_register.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdentityEnhancedBreakdownAddressBreakdown from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "credit_agencies": IdentityEnhancedBreakdownAddressBreakdownCreditAgencies.from_dict(obj["credit_agencies"]) if obj.get("credit_agencies") is not None else None,
            "telephone_database": IdentityEnhancedBreakdownAddressBreakdownTelephoneDatabase.from_dict(obj["telephone_database"]) if obj.get("telephone_database") is not None else None,
            "voting_register": IdentityEnhancedBreakdownAddressBreakdownVotingRegister.from_dict(obj["voting_register"]) if obj.get("voting_register") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


