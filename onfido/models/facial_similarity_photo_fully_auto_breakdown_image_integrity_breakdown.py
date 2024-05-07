# coding: utf-8

"""
    Onfido API v3.6

    The Onfido API (v3.6)

    The version of the OpenAPI document: v3.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from onfido.models.facial_similarity_photo_breakdown_image_integrity_breakdown_face_detected import FacialSimilarityPhotoBreakdownImageIntegrityBreakdownFaceDetected
from onfido.models.facial_similarity_photo_fully_auto_breakdown_image_integrity_breakdown_source_integrity import FacialSimilarityPhotoFullyAutoBreakdownImageIntegrityBreakdownSourceIntegrity
from typing import Optional, Set
from typing_extensions import Self

class FacialSimilarityPhotoFullyAutoBreakdownImageIntegrityBreakdown(BaseModel):
    """
    FacialSimilarityPhotoFullyAutoBreakdownImageIntegrityBreakdown
    """ # noqa: E501
    face_detected: Optional[FacialSimilarityPhotoBreakdownImageIntegrityBreakdownFaceDetected] = None
    source_integrity: Optional[FacialSimilarityPhotoFullyAutoBreakdownImageIntegrityBreakdownSourceIntegrity] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["face_detected", "source_integrity"]

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
        """Create an instance of FacialSimilarityPhotoFullyAutoBreakdownImageIntegrityBreakdown from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of face_detected
        if self.face_detected:
            _dict['face_detected'] = self.face_detected.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source_integrity
        if self.source_integrity:
            _dict['source_integrity'] = self.source_integrity.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FacialSimilarityPhotoFullyAutoBreakdownImageIntegrityBreakdown from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "face_detected": FacialSimilarityPhotoBreakdownImageIntegrityBreakdownFaceDetected.from_dict(obj["face_detected"]) if obj.get("face_detected") is not None else None,
            "source_integrity": FacialSimilarityPhotoFullyAutoBreakdownImageIntegrityBreakdownSourceIntegrity.from_dict(obj["source_integrity"]) if obj.get("source_integrity") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


