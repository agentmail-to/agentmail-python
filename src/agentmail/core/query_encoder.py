# This file was auto-generated by Fern from our API Definition.

from typing import Any, Dict, List, Optional, Tuple
import json

import pydantic


# Flattens dicts to be of the form {"key[subkey][subkey2]": value} where value is not a dict
def traverse_query_dict(dict_flat: Dict[str, Any], key_prefix: Optional[str] = None) -> List[Tuple[str, Any]]:
    result = []
    for k, v in dict_flat.items():
        key = f"{key_prefix}[{k}]" if key_prefix is not None else k
        if isinstance(v, dict):
            result.extend(traverse_query_dict(v, key))
        elif isinstance(v, list):
            for arr_v in v:
                if isinstance(arr_v, dict):
                    result.extend(traverse_query_dict(arr_v, key))
                else:
                    result.append((key, arr_v))
        else:
            result.append((key, v))
    return result


def single_query_encoder(query_key: str, query_value: Any) -> List[Tuple[str, Any]]:
    if isinstance(query_value, pydantic.BaseModel) or isinstance(query_value, dict):
        if isinstance(query_value, pydantic.BaseModel):
            obj_dict = query_value.dict(by_alias=True)
        else:
            obj_dict = query_value
        return traverse_query_dict(obj_dict, query_key)
    elif isinstance(query_value, list):
        encoded_values: List[Tuple[str, Any]] = []
        encountered_object = False
        for value in query_value:
            if isinstance(value, pydantic.BaseModel) or isinstance(value, dict):
                encountered_object = True
                if isinstance(value, pydantic.BaseModel):
                    obj_dict = value.dict(by_alias=True)
                elif isinstance(value, dict):
                    obj_dict = value

                encoded_values.extend(single_query_encoder(query_key, obj_dict))
            else:
                encoded_values.append((query_key, value))

        # for simple lists only, JSON-encode to a single query key
        if not encountered_object:
            values = [v for (_, v) in encoded_values]
            json_encoded_values = json.dumps(values)
            return [(query_key, json_encoded_values)]
        else:
            return encoded_values

    return [(query_key, query_value)]


def encode_query(query: Optional[Dict[str, Any]]) -> Optional[List[Tuple[str, Any]]]:
    if query is None:
        return None

    encoded_query = []
    for k, v in query.items():
        encoded_query.extend(single_query_encoder(k, v))
    return encoded_query
