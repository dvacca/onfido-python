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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from onfido.models.report_document import ReportDocument
from onfido.models.report_name import ReportName
from onfido.models.report_result import ReportResult
from onfido.models.report_status import ReportStatus
from onfido.models.report_sub_result import ReportSubResult
from onfido.models.watchlist_aml_breakdown import WatchlistAmlBreakdown
from onfido.models.watchlist_aml_properties import WatchlistAmlProperties
from typing import Optional, Set
from typing_extensions import Self

class WatchlistAmlReport(BaseModel):
    """
    WatchlistAmlReport
    """ # noqa: E501
    id: StrictStr = Field(description="The unique identifier for the report. Read-only.")
    created_at: Optional[datetime] = Field(default=None, description="The date and time at which the report was first initiated. Read-only.")
    href: Optional[StrictStr] = Field(default=None, description="The API endpoint to retrieve the report. Read-only.")
    status: Optional[ReportStatus] = None
    result: Optional[ReportResult] = None
    sub_result: Optional[ReportSubResult] = None
    check_id: Optional[StrictStr] = Field(default=None, description="The ID of the check to which the report belongs. Read-only.")
    documents: Optional[List[ReportDocument]] = Field(default=None, description="Array of objects with document ids that were used in the Onfido engine. [ONLY POPULATED FOR DOCUMENT AND FACIAL SIMILARITY REPORTS]")
    name: ReportName
    breakdown: Optional[WatchlistAmlBreakdown] = None
    properties: Optional[WatchlistAmlProperties] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "created_at", "href", "status", "result", "sub_result", "check_id", "documents", "name", "breakdown", "properties"]

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
        """Create an instance of WatchlistAmlReport from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in documents (list)
        _items = []
        if self.documents:
            for _item in self.documents:
                if _item:
                    _items.append(_item.to_dict())
            _dict['documents'] = _items
        # override the default output from pydantic by calling `to_dict()` of breakdown
        if self.breakdown:
            _dict['breakdown'] = self.breakdown.to_dict()
        # override the default output from pydantic by calling `to_dict()` of properties
        if self.properties:
            _dict['properties'] = self.properties.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WatchlistAmlReport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "href": obj.get("href"),
            "status": obj.get("status"),
            "result": obj.get("result"),
            "sub_result": obj.get("sub_result"),
            "check_id": obj.get("check_id"),
            "documents": [ReportDocument.from_dict(_item) for _item in obj["documents"]] if obj.get("documents") is not None else None,
            "name": obj.get("name"),
            "breakdown": WatchlistAmlBreakdown.from_dict(obj["breakdown"]) if obj.get("breakdown") is not None else None,
            "properties": WatchlistAmlProperties.from_dict(obj["properties"]) if obj.get("properties") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


