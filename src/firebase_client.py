from __future__ import annotations
import os
from typing import Any

import requests

from sources import FirebaseSource

class FirebaseClient:
    def __init__(
        self,
        firebase_url: str | None = None,
        auth_token: str | None = None,
        timeout: int = 30
     ) -> None:
        self.firebase_url = firebase_url
        self.auth_token = auth_token
        self.timeout = timeout

        if not self.firebase_url:
            raise ValueError("Firebase URL is required. Set it via environment variable or constructor argument.")
    
    @classmethod
    def from_source(
        cls,
        source: FirebaseSource,

    ) -> FirebaseClient:
        
        firebase_url=os.getenv(source.url_env)
        auth_token=os.getenv("FIREBASE_AUTH_TOKEN")
        if not firebase_url:
            raise ValueError(f"Firebase URL for source '{source.name}' is not set. Please set the environment variable '{source.url_env}'.")
        return cls(firebase_url=firebase_url, auth_token=auth_token)
    
    @staticmethod
    def build_date_query(
        date_field: str,
        start_date: str,
        end_date: str
    ) -> dict[str, str]:

        if start_date == end_date:
            return {
                "orderBy": f'"{date_field}"',
                "equalTo": f'"{start_date}"'
            }

        return {
            "orderBy": f'"{date_field}"',
            "startAt": f'"{start_date}"',
            "endAt": f'"{end_date}"'
        }

    def get_data(self, params: dict[str, str] | None = None) -> Any:
        if params is None:
            params = {}
        if self.auth_token:
            params["auth"] = self.auth_token
        response = requests.get(
            self.firebase_url,
            params=params,
            timeout=self.timeout
        )

        response.raise_for_status()

        return response.json()